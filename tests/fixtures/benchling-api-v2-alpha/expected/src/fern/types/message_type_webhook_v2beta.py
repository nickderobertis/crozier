

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MessageTypeWebhookV2Beta(enum.StrEnum):
    """
    The event that the app is subscribed to.
    """

    V2BETA_APP_CONFIGURATION_UPDATED = "v2-beta.app.configuration.updated"
    V2BETA_CANVAS_CREATED = "v2-beta.canvas.created"
    V2APP_ACTIVATE_REQUESTED = "v2.app.activateRequested"
    V2APP_DEACTIVATED = "v2.app.deactivated"
    V2APP_INSTALLED = "v2.app.installed"
    V2ASSAY_RUN_CREATED = "v2.assayRun.created"
    V2ASSAY_RUN_UPDATED_FIELDS = "v2.assayRun.updated.fields"
    V2AUTOMATION_FILE_TRANSFORM_UPDATED_STATUS_FAILED = "v2.automationFileTransform.updated.status.failed"
    V2AUTOMATION_FILE_TRANSFORM_UPDATED_STATUS_PENDING = "v2.automationFileTransform.updated.status.pending"
    V2AUTOMATION_FILE_TRANSFORM_UPDATED_STATUS_RUNNING = "v2.automationFileTransform.updated.status.running"
    V2AUTOMATION_FILE_TRANSFORM_UPDATED_STATUS_SUCCEEDED = "v2.automationFileTransform.updated.status.succeeded"
    V2CANVAS_CREATED = "v2.canvas.created"
    V2CANVAS_INITIALIZED = "v2.canvas.initialized"
    V2CANVAS_USER_INTERACTED = "v2.canvas.userInteracted"
    V2ENTITY_REGISTERED = "v2.entity.registered"
    V2ENTRY_CREATED = "v2.entry.created"
    V2ENTRY_UPDATED_FIELDS = "v2.entry.updated.fields"
    V2ENTRY_UPDATED_REVIEW_RECORD = "v2.entry.updated.reviewRecord"
    V2REQUEST_CREATED = "v2.request.created"
    V2REQUEST_UPDATED_FIELDS = "v2.request.updated.fields"
    V2REQUEST_UPDATED_STATUS = "v2.request.updated.status"
    V2WORKFLOW_OUTPUT_CREATED = "v2.workflowOutput.created"
    V2WORKFLOW_OUTPUT_UPDATED_FIELDS = "v2.workflowOutput.updated.fields"
    V2WORKFLOW_TASK_CREATED = "v2.workflowTask.created"
    V2WORKFLOW_TASK_UPDATED_ASSIGNEE = "v2.workflowTask.updated.assignee"
    V2WORKFLOW_TASK_UPDATED_FIELDS = "v2.workflowTask.updated.fields"
    V2WORKFLOW_TASK_UPDATED_SCHEDULED_ON = "v2.workflowTask.updated.scheduledOn"
    V2WORKFLOW_TASK_UPDATED_STATUS = "v2.workflowTask.updated.status"
    V2WORKFLOW_TASK_GROUP_CREATED = "v2.workflowTaskGroup.created"
    V2WORKFLOW_TASK_GROUP_MAPPING_COMPLETED = "v2.workflowTaskGroup.mappingCompleted"
    V2WORKFLOW_TASK_GROUP_UPDATED_WATCHERS = "v2.workflowTaskGroup.updated.watchers"
    V3CUSTOM_ENTITY_CREATED = "v3.customEntity.created"
    V3CUSTOM_ENTITY_UPDATED = "v3.customEntity.updated"
    V3DNA_OLIGO_CREATED = "v3.dnaOligo.created"
    V3DNA_OLIGO_UPDATED = "v3.dnaOligo.updated"
    V3DNA_SEQUENCE_CREATED = "v3.dnaSequence.created"
    V3DNA_SEQUENCE_UPDATED = "v3.dnaSequence.updated"
    V3ENTRY_CREATED = "v3.entry.created"
    V3PROJECT_CREATED = "v3.project.created"
    V3PROJECT_UPDATED = "v3.project.updated"
    V3RNA_OLIGO_CREATED = "v3.rnaOligo.created"
    V3RNA_OLIGO_UPDATED = "v3.rnaOligo.updated"
    V3RNA_SEQUENCE_CREATED = "v3.rnaSequence.created"
    V3RNA_SEQUENCE_UPDATED = "v3.rnaSequence.updated"
    V3RUN_CREATED = "v3.run.created"

    def visit(
        self,
        v2beta_app_configuration_updated: typing.Callable[[], T_Result],
        v2beta_canvas_created: typing.Callable[[], T_Result],
        v2app_activate_requested: typing.Callable[[], T_Result],
        v2app_deactivated: typing.Callable[[], T_Result],
        v2app_installed: typing.Callable[[], T_Result],
        v2assay_run_created: typing.Callable[[], T_Result],
        v2assay_run_updated_fields: typing.Callable[[], T_Result],
        v2automation_file_transform_updated_status_failed: typing.Callable[[], T_Result],
        v2automation_file_transform_updated_status_pending: typing.Callable[[], T_Result],
        v2automation_file_transform_updated_status_running: typing.Callable[[], T_Result],
        v2automation_file_transform_updated_status_succeeded: typing.Callable[[], T_Result],
        v2canvas_created: typing.Callable[[], T_Result],
        v2canvas_initialized: typing.Callable[[], T_Result],
        v2canvas_user_interacted: typing.Callable[[], T_Result],
        v2entity_registered: typing.Callable[[], T_Result],
        v2entry_created: typing.Callable[[], T_Result],
        v2entry_updated_fields: typing.Callable[[], T_Result],
        v2entry_updated_review_record: typing.Callable[[], T_Result],
        v2request_created: typing.Callable[[], T_Result],
        v2request_updated_fields: typing.Callable[[], T_Result],
        v2request_updated_status: typing.Callable[[], T_Result],
        v2workflow_output_created: typing.Callable[[], T_Result],
        v2workflow_output_updated_fields: typing.Callable[[], T_Result],
        v2workflow_task_created: typing.Callable[[], T_Result],
        v2workflow_task_updated_assignee: typing.Callable[[], T_Result],
        v2workflow_task_updated_fields: typing.Callable[[], T_Result],
        v2workflow_task_updated_scheduled_on: typing.Callable[[], T_Result],
        v2workflow_task_updated_status: typing.Callable[[], T_Result],
        v2workflow_task_group_created: typing.Callable[[], T_Result],
        v2workflow_task_group_mapping_completed: typing.Callable[[], T_Result],
        v2workflow_task_group_updated_watchers: typing.Callable[[], T_Result],
        v3custom_entity_created: typing.Callable[[], T_Result],
        v3custom_entity_updated: typing.Callable[[], T_Result],
        v3dna_oligo_created: typing.Callable[[], T_Result],
        v3dna_oligo_updated: typing.Callable[[], T_Result],
        v3dna_sequence_created: typing.Callable[[], T_Result],
        v3dna_sequence_updated: typing.Callable[[], T_Result],
        v3entry_created: typing.Callable[[], T_Result],
        v3project_created: typing.Callable[[], T_Result],
        v3project_updated: typing.Callable[[], T_Result],
        v3rna_oligo_created: typing.Callable[[], T_Result],
        v3rna_oligo_updated: typing.Callable[[], T_Result],
        v3rna_sequence_created: typing.Callable[[], T_Result],
        v3rna_sequence_updated: typing.Callable[[], T_Result],
        v3run_created: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MessageTypeWebhookV2Beta.V2BETA_APP_CONFIGURATION_UPDATED:
            return v2beta_app_configuration_updated()
        if self is MessageTypeWebhookV2Beta.V2BETA_CANVAS_CREATED:
            return v2beta_canvas_created()
        if self is MessageTypeWebhookV2Beta.V2APP_ACTIVATE_REQUESTED:
            return v2app_activate_requested()
        if self is MessageTypeWebhookV2Beta.V2APP_DEACTIVATED:
            return v2app_deactivated()
        if self is MessageTypeWebhookV2Beta.V2APP_INSTALLED:
            return v2app_installed()
        if self is MessageTypeWebhookV2Beta.V2ASSAY_RUN_CREATED:
            return v2assay_run_created()
        if self is MessageTypeWebhookV2Beta.V2ASSAY_RUN_UPDATED_FIELDS:
            return v2assay_run_updated_fields()
        if self is MessageTypeWebhookV2Beta.V2AUTOMATION_FILE_TRANSFORM_UPDATED_STATUS_FAILED:
            return v2automation_file_transform_updated_status_failed()
        if self is MessageTypeWebhookV2Beta.V2AUTOMATION_FILE_TRANSFORM_UPDATED_STATUS_PENDING:
            return v2automation_file_transform_updated_status_pending()
        if self is MessageTypeWebhookV2Beta.V2AUTOMATION_FILE_TRANSFORM_UPDATED_STATUS_RUNNING:
            return v2automation_file_transform_updated_status_running()
        if self is MessageTypeWebhookV2Beta.V2AUTOMATION_FILE_TRANSFORM_UPDATED_STATUS_SUCCEEDED:
            return v2automation_file_transform_updated_status_succeeded()
        if self is MessageTypeWebhookV2Beta.V2CANVAS_CREATED:
            return v2canvas_created()
        if self is MessageTypeWebhookV2Beta.V2CANVAS_INITIALIZED:
            return v2canvas_initialized()
        if self is MessageTypeWebhookV2Beta.V2CANVAS_USER_INTERACTED:
            return v2canvas_user_interacted()
        if self is MessageTypeWebhookV2Beta.V2ENTITY_REGISTERED:
            return v2entity_registered()
        if self is MessageTypeWebhookV2Beta.V2ENTRY_CREATED:
            return v2entry_created()
        if self is MessageTypeWebhookV2Beta.V2ENTRY_UPDATED_FIELDS:
            return v2entry_updated_fields()
        if self is MessageTypeWebhookV2Beta.V2ENTRY_UPDATED_REVIEW_RECORD:
            return v2entry_updated_review_record()
        if self is MessageTypeWebhookV2Beta.V2REQUEST_CREATED:
            return v2request_created()
        if self is MessageTypeWebhookV2Beta.V2REQUEST_UPDATED_FIELDS:
            return v2request_updated_fields()
        if self is MessageTypeWebhookV2Beta.V2REQUEST_UPDATED_STATUS:
            return v2request_updated_status()
        if self is MessageTypeWebhookV2Beta.V2WORKFLOW_OUTPUT_CREATED:
            return v2workflow_output_created()
        if self is MessageTypeWebhookV2Beta.V2WORKFLOW_OUTPUT_UPDATED_FIELDS:
            return v2workflow_output_updated_fields()
        if self is MessageTypeWebhookV2Beta.V2WORKFLOW_TASK_CREATED:
            return v2workflow_task_created()
        if self is MessageTypeWebhookV2Beta.V2WORKFLOW_TASK_UPDATED_ASSIGNEE:
            return v2workflow_task_updated_assignee()
        if self is MessageTypeWebhookV2Beta.V2WORKFLOW_TASK_UPDATED_FIELDS:
            return v2workflow_task_updated_fields()
        if self is MessageTypeWebhookV2Beta.V2WORKFLOW_TASK_UPDATED_SCHEDULED_ON:
            return v2workflow_task_updated_scheduled_on()
        if self is MessageTypeWebhookV2Beta.V2WORKFLOW_TASK_UPDATED_STATUS:
            return v2workflow_task_updated_status()
        if self is MessageTypeWebhookV2Beta.V2WORKFLOW_TASK_GROUP_CREATED:
            return v2workflow_task_group_created()
        if self is MessageTypeWebhookV2Beta.V2WORKFLOW_TASK_GROUP_MAPPING_COMPLETED:
            return v2workflow_task_group_mapping_completed()
        if self is MessageTypeWebhookV2Beta.V2WORKFLOW_TASK_GROUP_UPDATED_WATCHERS:
            return v2workflow_task_group_updated_watchers()
        if self is MessageTypeWebhookV2Beta.V3CUSTOM_ENTITY_CREATED:
            return v3custom_entity_created()
        if self is MessageTypeWebhookV2Beta.V3CUSTOM_ENTITY_UPDATED:
            return v3custom_entity_updated()
        if self is MessageTypeWebhookV2Beta.V3DNA_OLIGO_CREATED:
            return v3dna_oligo_created()
        if self is MessageTypeWebhookV2Beta.V3DNA_OLIGO_UPDATED:
            return v3dna_oligo_updated()
        if self is MessageTypeWebhookV2Beta.V3DNA_SEQUENCE_CREATED:
            return v3dna_sequence_created()
        if self is MessageTypeWebhookV2Beta.V3DNA_SEQUENCE_UPDATED:
            return v3dna_sequence_updated()
        if self is MessageTypeWebhookV2Beta.V3ENTRY_CREATED:
            return v3entry_created()
        if self is MessageTypeWebhookV2Beta.V3PROJECT_CREATED:
            return v3project_created()
        if self is MessageTypeWebhookV2Beta.V3PROJECT_UPDATED:
            return v3project_updated()
        if self is MessageTypeWebhookV2Beta.V3RNA_OLIGO_CREATED:
            return v3rna_oligo_created()
        if self is MessageTypeWebhookV2Beta.V3RNA_OLIGO_UPDATED:
            return v3rna_oligo_updated()
        if self is MessageTypeWebhookV2Beta.V3RNA_SEQUENCE_CREATED:
            return v3rna_sequence_created()
        if self is MessageTypeWebhookV2Beta.V3RNA_SEQUENCE_UPDATED:
            return v3rna_sequence_updated()
        if self is MessageTypeWebhookV2Beta.V3RUN_CREATED:
            return v3run_created()
