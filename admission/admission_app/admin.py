from pyexpat.errors import messages
from django.contrib import admin
from .models import *

# from django_fsm import TransactionNotAllowed

from django.contrib.admin.models import LogEntry, CHANGE
from django.contrib.contenttypes.models import ContentType
from django.utils.encoding import force_str


# Register your models here.


class ApplicationAdmin(admin.ModelAdmin):
    model= Application
    fields =['name', 'Application_status' ]
    list_display = ('name', 'course', 'email', 'phone_no', 'address', 'date_joined', 'Application_Status', 'message')
    actions= ['approve_application', 'reject_application']

    def approve_application(self, request, queryset):
        queryset.update(Application_Status='Approved')
        self.message_user(request, "Application Approved")
        for obj in queryset:
            LogEntry.objects.log_action(
                user_id=request.user.id,
                content_type_id=ContentType.objects.get_for_model(obj).pk,
                object_id=obj.id,
                object_repr=force_str(obj),
                action_flag=CHANGE,
                change_message="Application Approved",
            )
    
    def reject_application(self, request, queryset):
        queryset.update(Application_Status='Rejected')
        self.message_user(request, "Application Rejected")
        for obj in queryset:
            LogEntry.objects.log_action(
                user_id=request.user.id,
                content_type_id=ContentType.objects.get_for_model(obj).pk,
                object_id=obj.id,
                object_repr=force_str(obj),
                action_flag=CHANGE,
                change_message="Application Rejected",
            )


   

    # def get_queryset(self, request):
    #         return (
    #         super(ApplicationAdmin, self)
    #         .get_queryset(request)
    #         .prefetch_related("user")
            
    #     )

    # def perform_action (self, request,queryset, action):
    #     try:
    #         method = getattr(Application, action)
    #     except:
    #         self.message_user(request, 'Illegal action.', level=messages.ERROR)
    #         return
    #     failed_count = 0
    #     queryset_count = queryset.count()
    #     for entry in queryset:
    #         try:
    #             method(entry)
    #             entry.save()

    #             LogEntry.objects.log_action(
    #                 user_id=request.user.id,
    #                 content_type_id=ContentType.objects.get_for_model(entry).pk,
    #                 object_id=entry.id,
    #                 object_repr=force_str(entry),
    #                 action_flag=CHANGE,
    #                 change_message="{action} action initiated by user.".format(
    #                     action=action.replace("_", " ").strip().capitalize()
    #                 ),
    #             )
    #         except TransitionNotAllowed:
    #             failed_count += 1
    #     if failed_count:
    #         if failed_count == queryset_count:
    #             self.message_user(
    #                 request, "Illegal state change attempt.", level=messages.ERROR
    #             )
    #         else:
    #             self.message_user(
    #                 request,
    #                 "%d state(s) changed (%d failed)."
    #                 % (queryset_count - failed_count, failed_count),
    #                 level=messages.WARNING,
    #             )
    #     else:
    #         self.message_user(
    #             request, "Successfully changed %d state(s)." % queryset_count
    #         )
    
    # def approve(self, request, queryset):
    #     self.perform_action(request, 'activate', queryset)
    # approve.short_description ='Approve the selected application(s)'

    # def reject(self, request, queryset):
    #     self.perform_action(request, 'reject',queryset)
    # reject.short_description = 'Reject the selected Application(s)'


admin.site.register(Profile)
admin.site.register(Application, ApplicationAdmin)



