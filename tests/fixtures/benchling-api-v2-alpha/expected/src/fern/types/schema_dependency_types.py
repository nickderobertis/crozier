

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SchemaDependencyTypes(enum.StrEnum):
    CONTAINER_SCHEMA = "container_schema"
    PLATE_SCHEMA = "plate_schema"
    LOCATION_SCHEMA = "location_schema"
    BOX_SCHEMA = "box_schema"
    RUN_SCHEMA = "run_schema"
    RESULT_SCHEMA = "result_schema"
    REQUEST_SCHEMA = "request_schema"
    ENTRY_SCHEMA = "entry_schema"
    WORKFLOW_TASK_SCHEMA = "workflow_task_schema"

    def visit(
        self,
        container_schema: typing.Callable[[], T_Result],
        plate_schema: typing.Callable[[], T_Result],
        location_schema: typing.Callable[[], T_Result],
        box_schema: typing.Callable[[], T_Result],
        run_schema: typing.Callable[[], T_Result],
        result_schema: typing.Callable[[], T_Result],
        request_schema: typing.Callable[[], T_Result],
        entry_schema: typing.Callable[[], T_Result],
        workflow_task_schema: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SchemaDependencyTypes.CONTAINER_SCHEMA:
            return container_schema()
        if self is SchemaDependencyTypes.PLATE_SCHEMA:
            return plate_schema()
        if self is SchemaDependencyTypes.LOCATION_SCHEMA:
            return location_schema()
        if self is SchemaDependencyTypes.BOX_SCHEMA:
            return box_schema()
        if self is SchemaDependencyTypes.RUN_SCHEMA:
            return run_schema()
        if self is SchemaDependencyTypes.RESULT_SCHEMA:
            return result_schema()
        if self is SchemaDependencyTypes.REQUEST_SCHEMA:
            return request_schema()
        if self is SchemaDependencyTypes.ENTRY_SCHEMA:
            return entry_schema()
        if self is SchemaDependencyTypes.WORKFLOW_TASK_SCHEMA:
            return workflow_task_schema()
