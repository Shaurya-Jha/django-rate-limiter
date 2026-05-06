from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=200, blank=True)
    category = models.TextField(max_length=100, blank=True)
    created_by = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="creator")
    assigned_to = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="assignee", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        if (self.created_by == self.assigned_to):
            return f"{self.created_by} assigned task {self.title} to self"
        return f"{self.created_by} assigned task {self.title} to {self.assigned_to}"