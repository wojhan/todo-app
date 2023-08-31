from rest_framework import serializers

from . import models


class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Case
        fields = ["id", "owner", "is_open", "name", "description"]


class TaskSerializer(serializers.ModelSerializer):
    def validate_case(self, value):
        if not value.is_open:
            raise serializers.ValidationError(
                "Tasks can be created or updated only in open cases"
            )
        return value

    def validate_status(self, value):
        instance = self.instance

        if instance and instance.status == 2 and value != 2:
            raise serializers.ValidationError("Done tasks can't change their status")

        return value

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
        extra_kwargs = {"case": {"write_only": True}, "done_at": {"read_only": True}}
