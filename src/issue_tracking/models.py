from django.db import models
from django.conf import settings

# Use the AUTH_USER_MODEL setting to reference the User model
User = settings.AUTH_USER_MODEL

# Choices for the models
TYPE_CHOICES = [
    ("BE", "Back-end"),
    ("FE", "Front-end"),
    ("iOS", "iOS"),
    ("Andr", "Android"),
]

TAG_CHOICES = [
    ("BUG", "Bug"),
    ("IMPROVEMENT", "Amélioration"),
    ("TASK", "Tâche"),
]

PRIORITY_CHOICES = [
    ("LOW", "Faible"),
    ("MEDIUM", "Moyenne"),
    ("HIGH", "Élevée"),
]

STATUS_CHOICES = [
    ("TODO", "À faire"),
    ("IN_PROGRESS", "En cours"),
    ("DONE", "Terminé"), 
]


class Project(models.Model):
    # Project model represents a project in the system
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    type = models.CharField(max_length=4, choices=TYPE_CHOICES, default="BE")
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Author of the project
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Contributor(models.Model):
    # Contributor model represents a user contributing to a project
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user", "project")  # Ensure unique user-project pairs

    def __str__(self):
        return f"{self.user} - {self.project}"


class Issue(models.Model):
    # Issue model represents a task or bug within a project
    title = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=250)
    tag = models.CharField(max_length=11, choices=TAG_CHOICES)
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField(max_length=11, choices=STATUS_CHOICES, default="TODO")
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Author of the issue
    assignee = models.ForeignKey(User, on_delete=models.CASCADE, related_name="assignee")  # Assigned user
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.project} ({self.status})"


class Comment(models.Model):
    # Comment model represents a comment on an issue within a project
    description = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.issue} - {self.description[:20]}"
