from rest_framework import serializers

from . import models


class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Case
        fields = ["id", "owner", "is_open", "name", "description"]


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields = (
            "id",
            "case",
            "title",
            "description",
            "status",
            "created_at",
            "updated_at",
            "done_at",
        )
        extra_kwargs = {"case": {"write_only": True}}
