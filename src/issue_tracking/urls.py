from django.urls import path
from . import views

urlpatterns = [
    # Endpoint for retrieving a list of projects
    path('', views.ProjectList.as_view(), name='project_list'),

    # Endpoint for retrieving details of a specific project
    path('<int:pk>/', views.ProjectDetail.as_view(), name='project_detail'),

    # Endpoint for retrieving the list of contributors for a project
    path('<int:project_id>/users/', views.ContributorList.as_view(), name='contributor_list'),

    # Endpoint for removing a contributor from a project
    path('<int:project_id>/users/<int:user_id>/', views.ContributorDelete.as_view(), name='contributor_delete'),

    # Endpoint for retrieving the list of issues for a project
    path('<int:project_id>/issues/', views.IssueList.as_view(), name='issue_list'),

    # Endpoint for updating details of a specific issue in a project
    path('<int:project_id>/issues/<int:issue_id>/', views.IssueUpdate.as_view(), name='issue_update'),

    # Endpoint for retrieving the list of comments for a specific issue
    path('<int:project_id>/issues/<int:issue_id>/comments/', views.CommentList.as_view(), name='comment_list'),

    # Endpoint for updating details of a specific comment in an issue
    path('<int:project_id>/issues/<int:issue_id>/comments/<comment_id>/', views.CommentUpdate.as_view(), name='comment_update'),
]
