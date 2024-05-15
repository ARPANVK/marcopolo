import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class Candidate_data(AbstractUser):
    name = models.CharField(max_length = 300)
    email = models.EmailField(max_length = 100)
    password = models.CharField(max_length = 50)
    key = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    # Define unique related_name for groups and permissions to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='candidate_data_set',
        related_query_name='candidate_data',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='candidate_data_set',
        related_query_name='candidate_data',
    )

    
