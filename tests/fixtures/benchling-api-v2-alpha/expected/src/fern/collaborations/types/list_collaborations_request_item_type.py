

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListCollaborationsRequestItemType(enum.StrEnum):
    CONNECTION = "connection"
    CONNECTION_SCHEMA = "connection_schema"
    ENTITY_SCHEMA = "entity_schema"
    ENZYME_LIST = "enzyme_list"
    FEATURE_LIBRARY = "feature_library"
    FOLDER = "folder"
    LEGACY_ASSEMBLY = "legacy_assembly"
    LEGACY_WORKFLOW_TEMPLATE = "legacy_workflow_template"
    PROJECT = "project"
    REGISTRY = "registry"
    RESULT_SCHEMA = "result_schema"
    RUN_SCHEMA = "run_schema"
    SAVED_SEARCH = "saved_search"
    SCHEMA_INTERFACE = "schema_interface"
    TEMPLATE_COLLECTION = "template_collection"
    WORKLIST = "worklist"

    def visit(
        self,
        connection: typing.Callable[[], T_Result],
        connection_schema: typing.Callable[[], T_Result],
        entity_schema: typing.Callable[[], T_Result],
        enzyme_list: typing.Callable[[], T_Result],
        feature_library: typing.Callable[[], T_Result],
        folder: typing.Callable[[], T_Result],
        legacy_assembly: typing.Callable[[], T_Result],
        legacy_workflow_template: typing.Callable[[], T_Result],
        project: typing.Callable[[], T_Result],
        registry: typing.Callable[[], T_Result],
        result_schema: typing.Callable[[], T_Result],
        run_schema: typing.Callable[[], T_Result],
        saved_search: typing.Callable[[], T_Result],
        schema_interface: typing.Callable[[], T_Result],
        template_collection: typing.Callable[[], T_Result],
        worklist: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListCollaborationsRequestItemType.CONNECTION:
            return connection()
        if self is ListCollaborationsRequestItemType.CONNECTION_SCHEMA:
            return connection_schema()
        if self is ListCollaborationsRequestItemType.ENTITY_SCHEMA:
            return entity_schema()
        if self is ListCollaborationsRequestItemType.ENZYME_LIST:
            return enzyme_list()
        if self is ListCollaborationsRequestItemType.FEATURE_LIBRARY:
            return feature_library()
        if self is ListCollaborationsRequestItemType.FOLDER:
            return folder()
        if self is ListCollaborationsRequestItemType.LEGACY_ASSEMBLY:
            return legacy_assembly()
        if self is ListCollaborationsRequestItemType.LEGACY_WORKFLOW_TEMPLATE:
            return legacy_workflow_template()
        if self is ListCollaborationsRequestItemType.PROJECT:
            return project()
        if self is ListCollaborationsRequestItemType.REGISTRY:
            return registry()
        if self is ListCollaborationsRequestItemType.RESULT_SCHEMA:
            return result_schema()
        if self is ListCollaborationsRequestItemType.RUN_SCHEMA:
            return run_schema()
        if self is ListCollaborationsRequestItemType.SAVED_SEARCH:
            return saved_search()
        if self is ListCollaborationsRequestItemType.SCHEMA_INTERFACE:
            return schema_interface()
        if self is ListCollaborationsRequestItemType.TEMPLATE_COLLECTION:
            return template_collection()
        if self is ListCollaborationsRequestItemType.WORKLIST:
            return worklist()
