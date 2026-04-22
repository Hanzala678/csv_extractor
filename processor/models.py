from django.db import models

class Execution(models.Model):
    input_file = models.FileField(upload_to='inputs/')
    output_file = models.FileField(upload_to='outputs/', null=True, blank=True)
    rows_input = models.IntegerField(default=0)
    rows_output = models.IntegerField(default=0)
    status = models.CharField(max_length=50, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Execution {self.id} - {self.status}"