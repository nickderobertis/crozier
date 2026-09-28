



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .add_table_column_request_column import AddTableColumnRequestColumn
    from .add_table_column_request_column_options_item import AddTableColumnRequestColumnOptionsItem
    from .add_table_column_request_column_type import AddTableColumnRequestColumnType
    from .add_table_workflow_group_request_group import AddTableWorkflowGroupRequestGroup
    from .add_table_workflow_group_request_group_dependencies import AddTableWorkflowGroupRequestGroupDependencies
    from .add_table_workflow_group_request_group_deployment_mode import AddTableWorkflowGroupRequestGroupDeploymentMode
    from .add_table_workflow_group_request_group_input_mappings_item import (
        AddTableWorkflowGroupRequestGroupInputMappingsItem,
    )
    from .add_table_workflow_group_request_group_outputs_item import AddTableWorkflowGroupRequestGroupOutputsItem
    from .add_table_workflow_group_request_group_type import AddTableWorkflowGroupRequestGroupType
    from .add_table_workflow_group_request_output_columns_item import AddTableWorkflowGroupRequestOutputColumnsItem
    from .add_table_workflow_group_request_output_columns_item_type import (
        AddTableWorkflowGroupRequestOutputColumnsItemType,
    )
    from .bulk_update_table_rows_request_updates_item import BulkUpdateTableRowsRequestUpdatesItem
    from .cancel_table_runs_request_scope import CancelTableRunsRequestScope
    from .create_table_dispatch_request_limit import CreateTableDispatchRequestLimit
    from .create_table_dispatch_request_limit_type import CreateTableDispatchRequestLimitType
    from .create_table_dispatch_request_run_mode import CreateTableDispatchRequestRunMode
    from .create_table_export_request_format import CreateTableExportRequestFormat
    from .create_table_import_request_source import (
        CreateTableImportRequestSource,
        CreateTableImportRequestSource_Upload,
        CreateTableImportRequestSource_WorkspaceFile,
    )
    from .create_table_import_request_target import (
        CreateTableImportRequestTarget,
        CreateTableImportRequestTarget_Existing,
        CreateTableImportRequestTarget_New,
    )
    from .create_table_import_request_target_existing import CreateTableImportRequestTargetExisting
    from .create_table_import_request_target_existing_mode import CreateTableImportRequestTargetExistingMode
    from .create_table_import_request_target_new import CreateTableImportRequestTargetNew
    from .create_table_request_schema import CreateTableRequestSchema
    from .create_table_request_schema_columns_item import CreateTableRequestSchemaColumnsItem
    from .create_table_request_schema_columns_item_options_item import CreateTableRequestSchemaColumnsItemOptionsItem
    from .create_table_request_schema_columns_item_type import CreateTableRequestSchemaColumnsItemType
    from .create_table_view_request_config import CreateTableViewRequestConfig
    from .create_table_view_request_config_sort_item import CreateTableViewRequestConfigSortItem
    from .create_table_view_request_config_sort_item_direction import CreateTableViewRequestConfigSortItemDirection
    from .delete_tables_folder_request_recursive import DeleteTablesFolderRequestRecursive
    from .list_tables_folders_request_sort_by import ListTablesFoldersRequestSortBy
    from .list_tables_folders_request_sort_order import ListTablesFoldersRequestSortOrder
    from .list_tables_request_scope import ListTablesRequestScope
    from .list_tables_request_sort_by import ListTablesRequestSortBy
    from .list_tables_request_sort_order import ListTablesRequestSortOrder
    from .query_table_rows_request_sort_item import QueryTableRowsRequestSortItem
    from .query_table_rows_request_sort_item_direction import QueryTableRowsRequestSortItemDirection
    from .search_table_rows_request_sort_item import SearchTableRowsRequestSortItem
    from .search_table_rows_request_sort_item_direction import SearchTableRowsRequestSortItemDirection
    from .update_table_column_request_updates import UpdateTableColumnRequestUpdates
    from .update_table_column_request_updates_options_item import UpdateTableColumnRequestUpdatesOptionsItem
    from .update_table_column_request_updates_type import UpdateTableColumnRequestUpdatesType
    from .update_table_view_request_config import UpdateTableViewRequestConfig
    from .update_table_view_request_config_patch import UpdateTableViewRequestConfigPatch
    from .update_table_view_request_config_patch_sort_item import UpdateTableViewRequestConfigPatchSortItem
    from .update_table_view_request_config_patch_sort_item_direction import (
        UpdateTableViewRequestConfigPatchSortItemDirection,
    )
    from .update_table_view_request_config_sort_item import UpdateTableViewRequestConfigSortItem
    from .update_table_view_request_config_sort_item_direction import UpdateTableViewRequestConfigSortItemDirection
    from .update_table_workflow_group_request_dependencies import UpdateTableWorkflowGroupRequestDependencies
    from .update_table_workflow_group_request_deployment_mode import UpdateTableWorkflowGroupRequestDeploymentMode
    from .update_table_workflow_group_request_input_mappings_item import (
        UpdateTableWorkflowGroupRequestInputMappingsItem,
    )
    from .update_table_workflow_group_request_mapping_updates_item import (
        UpdateTableWorkflowGroupRequestMappingUpdatesItem,
    )
    from .update_table_workflow_group_request_new_output_columns_item import (
        UpdateTableWorkflowGroupRequestNewOutputColumnsItem,
    )
    from .update_table_workflow_group_request_new_output_columns_item_type import (
        UpdateTableWorkflowGroupRequestNewOutputColumnsItemType,
    )
    from .update_table_workflow_group_request_outputs_item import UpdateTableWorkflowGroupRequestOutputsItem
    from .update_table_workflow_group_request_type import UpdateTableWorkflowGroupRequestType
_dynamic_imports: typing.Dict[str, str] = {
    "AddTableColumnRequestColumn": ".add_table_column_request_column",
    "AddTableColumnRequestColumnOptionsItem": ".add_table_column_request_column_options_item",
    "AddTableColumnRequestColumnType": ".add_table_column_request_column_type",
    "AddTableWorkflowGroupRequestGroup": ".add_table_workflow_group_request_group",
    "AddTableWorkflowGroupRequestGroupDependencies": ".add_table_workflow_group_request_group_dependencies",
    "AddTableWorkflowGroupRequestGroupDeploymentMode": ".add_table_workflow_group_request_group_deployment_mode",
    "AddTableWorkflowGroupRequestGroupInputMappingsItem": ".add_table_workflow_group_request_group_input_mappings_item",
    "AddTableWorkflowGroupRequestGroupOutputsItem": ".add_table_workflow_group_request_group_outputs_item",
    "AddTableWorkflowGroupRequestGroupType": ".add_table_workflow_group_request_group_type",
    "AddTableWorkflowGroupRequestOutputColumnsItem": ".add_table_workflow_group_request_output_columns_item",
    "AddTableWorkflowGroupRequestOutputColumnsItemType": ".add_table_workflow_group_request_output_columns_item_type",
    "BulkUpdateTableRowsRequestUpdatesItem": ".bulk_update_table_rows_request_updates_item",
    "CancelTableRunsRequestScope": ".cancel_table_runs_request_scope",
    "CreateTableDispatchRequestLimit": ".create_table_dispatch_request_limit",
    "CreateTableDispatchRequestLimitType": ".create_table_dispatch_request_limit_type",
    "CreateTableDispatchRequestRunMode": ".create_table_dispatch_request_run_mode",
    "CreateTableExportRequestFormat": ".create_table_export_request_format",
    "CreateTableImportRequestSource": ".create_table_import_request_source",
    "CreateTableImportRequestSource_Upload": ".create_table_import_request_source",
    "CreateTableImportRequestSource_WorkspaceFile": ".create_table_import_request_source",
    "CreateTableImportRequestTarget": ".create_table_import_request_target",
    "CreateTableImportRequestTargetExisting": ".create_table_import_request_target_existing",
    "CreateTableImportRequestTargetExistingMode": ".create_table_import_request_target_existing_mode",
    "CreateTableImportRequestTargetNew": ".create_table_import_request_target_new",
    "CreateTableImportRequestTarget_Existing": ".create_table_import_request_target",
    "CreateTableImportRequestTarget_New": ".create_table_import_request_target",
    "CreateTableRequestSchema": ".create_table_request_schema",
    "CreateTableRequestSchemaColumnsItem": ".create_table_request_schema_columns_item",
    "CreateTableRequestSchemaColumnsItemOptionsItem": ".create_table_request_schema_columns_item_options_item",
    "CreateTableRequestSchemaColumnsItemType": ".create_table_request_schema_columns_item_type",
    "CreateTableViewRequestConfig": ".create_table_view_request_config",
    "CreateTableViewRequestConfigSortItem": ".create_table_view_request_config_sort_item",
    "CreateTableViewRequestConfigSortItemDirection": ".create_table_view_request_config_sort_item_direction",
    "DeleteTablesFolderRequestRecursive": ".delete_tables_folder_request_recursive",
    "ListTablesFoldersRequestSortBy": ".list_tables_folders_request_sort_by",
    "ListTablesFoldersRequestSortOrder": ".list_tables_folders_request_sort_order",
    "ListTablesRequestScope": ".list_tables_request_scope",
    "ListTablesRequestSortBy": ".list_tables_request_sort_by",
    "ListTablesRequestSortOrder": ".list_tables_request_sort_order",
    "QueryTableRowsRequestSortItem": ".query_table_rows_request_sort_item",
    "QueryTableRowsRequestSortItemDirection": ".query_table_rows_request_sort_item_direction",
    "SearchTableRowsRequestSortItem": ".search_table_rows_request_sort_item",
    "SearchTableRowsRequestSortItemDirection": ".search_table_rows_request_sort_item_direction",
    "UpdateTableColumnRequestUpdates": ".update_table_column_request_updates",
    "UpdateTableColumnRequestUpdatesOptionsItem": ".update_table_column_request_updates_options_item",
    "UpdateTableColumnRequestUpdatesType": ".update_table_column_request_updates_type",
    "UpdateTableViewRequestConfig": ".update_table_view_request_config",
    "UpdateTableViewRequestConfigPatch": ".update_table_view_request_config_patch",
    "UpdateTableViewRequestConfigPatchSortItem": ".update_table_view_request_config_patch_sort_item",
    "UpdateTableViewRequestConfigPatchSortItemDirection": ".update_table_view_request_config_patch_sort_item_direction",
    "UpdateTableViewRequestConfigSortItem": ".update_table_view_request_config_sort_item",
    "UpdateTableViewRequestConfigSortItemDirection": ".update_table_view_request_config_sort_item_direction",
    "UpdateTableWorkflowGroupRequestDependencies": ".update_table_workflow_group_request_dependencies",
    "UpdateTableWorkflowGroupRequestDeploymentMode": ".update_table_workflow_group_request_deployment_mode",
    "UpdateTableWorkflowGroupRequestInputMappingsItem": ".update_table_workflow_group_request_input_mappings_item",
    "UpdateTableWorkflowGroupRequestMappingUpdatesItem": ".update_table_workflow_group_request_mapping_updates_item",
    "UpdateTableWorkflowGroupRequestNewOutputColumnsItem": ".update_table_workflow_group_request_new_output_columns_item",
    "UpdateTableWorkflowGroupRequestNewOutputColumnsItemType": ".update_table_workflow_group_request_new_output_columns_item_type",
    "UpdateTableWorkflowGroupRequestOutputsItem": ".update_table_workflow_group_request_outputs_item",
    "UpdateTableWorkflowGroupRequestType": ".update_table_workflow_group_request_type",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "AddTableColumnRequestColumn",
    "AddTableColumnRequestColumnOptionsItem",
    "AddTableColumnRequestColumnType",
    "AddTableWorkflowGroupRequestGroup",
    "AddTableWorkflowGroupRequestGroupDependencies",
    "AddTableWorkflowGroupRequestGroupDeploymentMode",
    "AddTableWorkflowGroupRequestGroupInputMappingsItem",
    "AddTableWorkflowGroupRequestGroupOutputsItem",
    "AddTableWorkflowGroupRequestGroupType",
    "AddTableWorkflowGroupRequestOutputColumnsItem",
    "AddTableWorkflowGroupRequestOutputColumnsItemType",
    "BulkUpdateTableRowsRequestUpdatesItem",
    "CancelTableRunsRequestScope",
    "CreateTableDispatchRequestLimit",
    "CreateTableDispatchRequestLimitType",
    "CreateTableDispatchRequestRunMode",
    "CreateTableExportRequestFormat",
    "CreateTableImportRequestSource",
    "CreateTableImportRequestSource_Upload",
    "CreateTableImportRequestSource_WorkspaceFile",
    "CreateTableImportRequestTarget",
    "CreateTableImportRequestTargetExisting",
    "CreateTableImportRequestTargetExistingMode",
    "CreateTableImportRequestTargetNew",
    "CreateTableImportRequestTarget_Existing",
    "CreateTableImportRequestTarget_New",
    "CreateTableRequestSchema",
    "CreateTableRequestSchemaColumnsItem",
    "CreateTableRequestSchemaColumnsItemOptionsItem",
    "CreateTableRequestSchemaColumnsItemType",
    "CreateTableViewRequestConfig",
    "CreateTableViewRequestConfigSortItem",
    "CreateTableViewRequestConfigSortItemDirection",
    "DeleteTablesFolderRequestRecursive",
    "ListTablesFoldersRequestSortBy",
    "ListTablesFoldersRequestSortOrder",
    "ListTablesRequestScope",
    "ListTablesRequestSortBy",
    "ListTablesRequestSortOrder",
    "QueryTableRowsRequestSortItem",
    "QueryTableRowsRequestSortItemDirection",
    "SearchTableRowsRequestSortItem",
    "SearchTableRowsRequestSortItemDirection",
    "UpdateTableColumnRequestUpdates",
    "UpdateTableColumnRequestUpdatesOptionsItem",
    "UpdateTableColumnRequestUpdatesType",
    "UpdateTableViewRequestConfig",
    "UpdateTableViewRequestConfigPatch",
    "UpdateTableViewRequestConfigPatchSortItem",
    "UpdateTableViewRequestConfigPatchSortItemDirection",
    "UpdateTableViewRequestConfigSortItem",
    "UpdateTableViewRequestConfigSortItemDirection",
    "UpdateTableWorkflowGroupRequestDependencies",
    "UpdateTableWorkflowGroupRequestDeploymentMode",
    "UpdateTableWorkflowGroupRequestInputMappingsItem",
    "UpdateTableWorkflowGroupRequestMappingUpdatesItem",
    "UpdateTableWorkflowGroupRequestNewOutputColumnsItem",
    "UpdateTableWorkflowGroupRequestNewOutputColumnsItemType",
    "UpdateTableWorkflowGroupRequestOutputsItem",
    "UpdateTableWorkflowGroupRequestType",
]
