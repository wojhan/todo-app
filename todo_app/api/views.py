from drf_spectacular.utils import extend_schema
from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from . import models, serializers


class CaseList(generics.ListCreateAPIView):
    queryset = models.Case.objects.all()
    serializer_class = serializers.CaseSerializer

    @extend_schema(description="Getting all cases for the authenticated user")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        description="Creates a new case for the authenticated user. Sets owner based on actual credentials"
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class CaseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Case.objects.all()
    serializer_class = serializers.CaseSerializer

    @extend_schema(description="Details of the given user's case")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(description="Updates case information")
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(description="Updates case information")
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(description="Deletes case information")
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class CaseTaskList(generics.ListCreateAPIView):
    serializer_class = serializers.TaskSerializer

    def get_queryset(self):
        case_id = self.kwargs["case_pk"]
        case = get_object_or_404(models.Case.objects.filter(pk=case_id))
        return models.Task.objects.filter(case=case)

    @extend_schema(
        description="Creates a new task for the given case. Tasks can not exist without case."
    )
    def post(self, request, *args, **kwargs):
        case_id = self.kwargs["case_pk"]

        request_data = request.data.copy()
        request_data["case"] = case_id

        task_write_serializer = self.get_serializer(data=request_data)
        task_write_serializer.is_valid(raise_exception=True)
        task_write_serializer.save()

        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @extend_schema(description="Getting list of task assigned to the user's case")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.TaskSerializer
    queryset = models.Task.objects.all()

    @extend_schema(
        description="Updates a task. It can be done only if the case is open"
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        description="Updates a task. It can be done only if the case is open"
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(
        description="Deletes a task. It can be done only if the case is open"
    )
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.case.is_open:
            return super().delete(request, *args, **kwargs)

        return Response(
            {"detail": "Tasks can be created or updated only in open cases"},
            status=status.HTTP_400_BAD_REQUEST,
        )
