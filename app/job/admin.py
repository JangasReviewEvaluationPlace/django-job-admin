from django.contrib import admin
from . import models


@admin.register(models.JobType)
class JobTypeAdmin(admin.ModelAdmin):
    pass


class LogInline(admin.StackedInline):
    model = models.JobExecutionLog
    readonly_fields = ("timestamp", )
    extra = 0

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(models.Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("title", "job_type", "last_execution", "frequency", "is_active",
                    "is_one_time_job", )
    list_filter = ("job_type", "is_active", "is_one_time_job", )
    search_fields = ("title", )
    readonly_fields = ("timestamp", "last_execution", "next_execution", )
    inlines = (LogInline, )


@admin.register(models.JobExecutionLog)
class JobExecutionLogAdmin(admin.ModelAdmin):
    list_display = ("title", "timestamp", )
    search_fields = ("title", )
    readonly_fields = ("title", "description", "timestamp", )

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
