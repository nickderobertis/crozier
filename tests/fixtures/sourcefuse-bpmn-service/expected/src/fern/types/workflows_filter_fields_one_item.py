

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WorkflowsFilterFieldsOneItem(enum.StrEnum):
    DELETED = "deleted"
    DELETED_ON = "deletedOn"
    DELETED_BY = "deletedBy"
    CREATED_ON = "createdOn"
    MODIFIED_ON = "modifiedOn"
    CREATED_BY = "createdBy"
    MODIFIED_BY = "modifiedBy"
    ID = "id"
    WORKFLOW_VERSION = "workflowVersion"
    EXTERNAL_IDENTIFIER = "externalIdentifier"
    NAME = "name"
    PROVIDER = "provider"
    INPUT_SCHEMA = "inputSchema"
    DESCRIPTION = "description"

    def visit(
        self,
        deleted: typing.Callable[[], T_Result],
        deleted_on: typing.Callable[[], T_Result],
        deleted_by: typing.Callable[[], T_Result],
        created_on: typing.Callable[[], T_Result],
        modified_on: typing.Callable[[], T_Result],
        created_by: typing.Callable[[], T_Result],
        modified_by: typing.Callable[[], T_Result],
        id: typing.Callable[[], T_Result],
        workflow_version: typing.Callable[[], T_Result],
        external_identifier: typing.Callable[[], T_Result],
        name: typing.Callable[[], T_Result],
        provider: typing.Callable[[], T_Result],
        input_schema: typing.Callable[[], T_Result],
        description: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WorkflowsFilterFieldsOneItem.DELETED:
            return deleted()
        if self is WorkflowsFilterFieldsOneItem.DELETED_ON:
            return deleted_on()
        if self is WorkflowsFilterFieldsOneItem.DELETED_BY:
            return deleted_by()
        if self is WorkflowsFilterFieldsOneItem.CREATED_ON:
            return created_on()
        if self is WorkflowsFilterFieldsOneItem.MODIFIED_ON:
            return modified_on()
        if self is WorkflowsFilterFieldsOneItem.CREATED_BY:
            return created_by()
        if self is WorkflowsFilterFieldsOneItem.MODIFIED_BY:
            return modified_by()
        if self is WorkflowsFilterFieldsOneItem.ID:
            return id()
        if self is WorkflowsFilterFieldsOneItem.WORKFLOW_VERSION:
            return workflow_version()
        if self is WorkflowsFilterFieldsOneItem.EXTERNAL_IDENTIFIER:
            return external_identifier()
        if self is WorkflowsFilterFieldsOneItem.NAME:
            return name()
        if self is WorkflowsFilterFieldsOneItem.PROVIDER:
            return provider()
        if self is WorkflowsFilterFieldsOneItem.INPUT_SCHEMA:
            return input_schema()
        if self is WorkflowsFilterFieldsOneItem.DESCRIPTION:
            return description()
