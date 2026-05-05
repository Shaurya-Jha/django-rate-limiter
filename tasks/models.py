from django.db import models

class Tasks(models.Model):
    title = models.TextField(required=True, null=False)
    description = models.TextField(max_length=200)
    category = models.TextField(max_length=100)
    created_by = models.ForeignKey("User", on_delete=models.CASCADE)
    assigned_to = models.ForeignKey("User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        if (self.created_by == self.assigned_to):
            return f"{self.created_by} assigned task {self.title} to self"
        return f"{self.created_by} assigned task {self.title} to {self.assigned_to}"