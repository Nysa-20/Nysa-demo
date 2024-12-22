from django.db import models

# Subject model to store subject names
class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# File model to store files related to a specific subject
class File(models.Model):
    subject = models.ForeignKey(Subject, related_name='files', on_delete=models.CASCADE)
    uploaded_file = models.FileField(upload_to='uploads/')  # Files will be stored in the 'uploads' directory
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.uploaded_file.name
