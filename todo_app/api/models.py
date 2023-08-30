from django.db import models


class Case(models.Model):
    """
    Represents a user case

    Attributes:
        owner (User): owner of the case (ForeignKey relationship)
        is_open (bool): specifies whether the case is open (default: True)
        name (str): name of the case (Max 64 chars)
        description (str): brief description of the case (Max 200 chars)
    """

    owner = models.ForeignKey(
        "auth.User", related_name="cases", on_delete=models.SET_NULL, null=True
    )
    is_open = models.BooleanField(default=True)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.owner}'s case - {self.name}"


class Task(models.Model):
    """
    Represents a task assigned to user's case

    Attributes:
        case (Case): a case the task is assigned to, task can't exists without the case (ForeignKey relationship)
        title (str): title of the task (Max 64 chars)
        description (str): details of the task (Max 600 chars)
        status (int): status of the task, can be one of these values: 0 - Created, 1 - In progress, 2 - Done
        created_at (datetime): when task was created (Auto fill when model is being inserted)
        update_at (datetime): date with time of last modification (Auto fill when model is being updated)
        done_at (datetime): date with time when a status of the task is set to done
    """

    STATUS_CHOICES = [
        (0, "Created"),
        (1, "In progress"),
        (2, "Done"),
    ]

    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=600)
    status = models.IntegerField(
        choices=STATUS_CHOICES,
        default=0,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    done_at = models.DateTimeField()

    def __str__(self):
        return f"{self.case}: {self.title}"
