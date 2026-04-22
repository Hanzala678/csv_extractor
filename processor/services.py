import pandas as pd

def process_csv(input_path, output_path):
    df = pd.read_csv(input_path)

    # ===== Excel-based Calculation Logic =====
    xls = pd.ExcelFile(input_path.replace('inputs', '').replace('.csv', '.xlsx')) if False else None

    valuation_date = pd.to_datetime("2024-12-31")
    discount_rate = 0.0545
    salary_increase_rate = 0.05
    retirement_age = 60

    df['salary'] = (
    df['salary']
    .astype(str)
    .str.replace(',', '', regex=False)
    .astype(float)
)

    df['date_birth'] = pd.to_datetime(df['date_birth'])
    df['date_joining'] = pd.to_datetime(df['date_joining'])

    lookup_df = pd.read_csv("processor\helpers\survival_probabilities.csv")

    results = []

    for _, row in df.iterrows():
        age = int((valuation_date - row['date_birth']).days / 365)
        current_salary = row['salary']

        yearly_rows = []

        for t in range(retirement_age - age):
            future_age = age + t
            future_salary = current_salary * ((1 + salary_increase_rate) ** (t + 1))

            death_prob = float(lookup_df.loc[
                lookup_df['age'] == future_age, 'qx'
            ].values[0].strip('%')) / 100
            survival_prob = 1 - death_prob

            expected_outflow = round(future_salary * death_prob * survival_prob, 2)

            yearly_rows.append({
                'emp_id': row['emp_id'],
                'age': future_age,
                'future_salary': future_salary,
                'survival_prob': survival_prob,
                'death_prob': death_prob,
                'expected_outflow': expected_outflow
            })

        results.extend(yearly_rows)

    result_df = pd.DataFrame(results)
    result_df.to_csv(output_path, index=False)

    return len(df), len(result_df)
