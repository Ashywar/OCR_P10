from rest_framework import serializers
from . import models
from django.shortcuts import get_object_or_404

# Serializer for retrieving and displaying project details
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Project


# Serializer for creating a new project
class ProjectCreateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['title', 'description', 'type']
        model = models.Project


# Serializer for retrieving and displaying contributor details
class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['user']
        model = models.Contributor


# Serializer for retrieving and displaying issue details
class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Issue


# Serializer for creating a new issue
class IssueCreateSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['project', 'author']
        model = models.Issue

    # Custom validation for the assignee field
    def validate_assignee(self, value):
        project_id = self.context.get('view').kwargs.get('project_id')
        project = get_object_or_404(models.Project, id=project_id)
        if not models.Contributor.objects.filter(project=project, user=value).exists():
            raise serializers.ValidationError("The assignee must be a contributor to the project.")
        return value


# Serializer for retrieving and displaying comment details
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Comment


# Serializer for creating a new comment
class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['author', 'issue', 'project']
        model = models.Comment
