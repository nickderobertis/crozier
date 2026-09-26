

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.create_table_rows_request import CreateTableRowsRequest
from ..types.folder_path_input import FolderPathInput
from ..types.non_root_folder_path_input import NonRootFolderPathInput
from ..types.table_predicate import TablePredicate
from ..types.table_predicate_input import TablePredicateInput
from ..types.v2add_table_workflow_group_response import V2AddTableWorkflowGroupResponse
from ..types.v2bulk_delete_tables_response import V2BulkDeleteTablesResponse
from ..types.v2bulk_update_table_rows_response import V2BulkUpdateTableRowsResponse
from ..types.v2cancel_table_dispatch_response import V2CancelTableDispatchResponse
from ..types.v2cancel_table_export_response import V2CancelTableExportResponse
from ..types.v2cancel_table_import_response import V2CancelTableImportResponse
from ..types.v2cancel_table_runs_response import V2CancelTableRunsResponse
from ..types.v2complete_table_import_upload_response import V2CompleteTableImportUploadResponse
from ..types.v2count_table_rows_response import V2CountTableRowsResponse
from ..types.v2create_table_dispatch_response import V2CreateTableDispatchResponse
from ..types.v2create_table_export_response import V2CreateTableExportResponse
from ..types.v2create_table_folder_response import V2CreateTableFolderResponse
from ..types.v2create_table_import_part_urls_response import V2CreateTableImportPartUrlsResponse
from ..types.v2create_table_import_response import V2CreateTableImportResponse
from ..types.v2create_table_response import V2CreateTableResponse
from ..types.v2create_table_rows_response import V2CreateTableRowsResponse
from ..types.v2create_table_view_response import V2CreateTableViewResponse
from ..types.v2delete_table_folder_response import V2DeleteTableFolderResponse
from ..types.v2delete_table_response import V2DeleteTableResponse
from ..types.v2delete_table_row_response import V2DeleteTableRowResponse
from ..types.v2delete_table_rows_response import V2DeleteTableRowsResponse
from ..types.v2delete_table_view_response import V2DeleteTableViewResponse
from ..types.v2delete_table_workflow_group_response import V2DeleteTableWorkflowGroupResponse
from ..types.v2download_table_export_response import V2DownloadTableExportResponse
from ..types.v2move_tables_response import V2MoveTablesResponse
from ..types.v2query_table_rows_response import V2QueryTableRowsResponse
from ..types.v2relocate_table_folder_response import V2RelocateTableFolderResponse
from ..types.v2restore_table_folder_response import V2RestoreTableFolderResponse
from ..types.v2restore_table_response import V2RestoreTableResponse
from ..types.v2row_enrichment_response import V2RowEnrichmentResponse
from ..types.v2run_row_enrichment_response import V2RunRowEnrichmentResponse
from ..types.v2search_table_rows_response import V2SearchTableRowsResponse
from ..types.v2table_columns_response import V2TableColumnsResponse
from ..types.v2table_export_response import V2TableExportResponse
from ..types.v2table_folder_list_response import V2TableFolderListResponse
from ..types.v2table_import_response import V2TableImportResponse
from ..types.v2table_list_response import V2TableListResponse
from ..types.v2table_response import V2TableResponse
from ..types.v2table_row_data import V2TableRowData
from ..types.v2table_row_list_response import V2TableRowListResponse
from ..types.v2table_row_response import V2TableRowResponse
from ..types.v2table_run_dispatch_list_response import V2TableRunDispatchListResponse
from ..types.v2table_run_dispatch_response import V2TableRunDispatchResponse
from ..types.v2table_view_list_response import V2TableViewListResponse
from ..types.v2table_view_response import V2TableViewResponse
from ..types.v2table_workflow_group_list_response import V2TableWorkflowGroupListResponse
from ..types.v2update_table_response import V2UpdateTableResponse
from ..types.v2update_table_rows_response import V2UpdateTableRowsResponse
from ..types.v2update_table_workflow_group_response import V2UpdateTableWorkflowGroupResponse
from ..types.v2upsert_table_row_response import V2UpsertTableRowResponse
from .raw_client import AsyncRawTablesClient, RawTablesClient
from .types.add_table_column_request_column import AddTableColumnRequestColumn
from .types.add_table_workflow_group_request_group import AddTableWorkflowGroupRequestGroup
from .types.add_table_workflow_group_request_output_columns_item import AddTableWorkflowGroupRequestOutputColumnsItem
from .types.bulk_update_table_rows_request_updates_item import BulkUpdateTableRowsRequestUpdatesItem
from .types.cancel_table_runs_request_scope import CancelTableRunsRequestScope
from .types.create_table_dispatch_request_limit import CreateTableDispatchRequestLimit
from .types.create_table_dispatch_request_run_mode import CreateTableDispatchRequestRunMode
from .types.create_table_export_request_format import CreateTableExportRequestFormat
from .types.create_table_import_request_source import CreateTableImportRequestSource
from .types.create_table_import_request_target import CreateTableImportRequestTarget
from .types.create_table_request_schema import CreateTableRequestSchema
from .types.create_table_view_request_config import CreateTableViewRequestConfig
from .types.delete_tables_folder_request_recursive import DeleteTablesFolderRequestRecursive
from .types.list_tables_folders_request_sort_by import ListTablesFoldersRequestSortBy
from .types.list_tables_folders_request_sort_order import ListTablesFoldersRequestSortOrder
from .types.list_tables_request_scope import ListTablesRequestScope
from .types.list_tables_request_sort_by import ListTablesRequestSortBy
from .types.list_tables_request_sort_order import ListTablesRequestSortOrder
from .types.query_table_rows_request_sort_item import QueryTableRowsRequestSortItem
from .types.search_table_rows_request_sort_item import SearchTableRowsRequestSortItem
from .types.update_table_column_request_updates import UpdateTableColumnRequestUpdates
from .types.update_table_view_request_config import UpdateTableViewRequestConfig
from .types.update_table_view_request_config_patch import UpdateTableViewRequestConfigPatch
from .types.update_table_workflow_group_request_dependencies import UpdateTableWorkflowGroupRequestDependencies
from .types.update_table_workflow_group_request_deployment_mode import UpdateTableWorkflowGroupRequestDeploymentMode
from .types.update_table_workflow_group_request_input_mappings_item import (
    UpdateTableWorkflowGroupRequestInputMappingsItem,
)
from .types.update_table_workflow_group_request_mapping_updates_item import (
    UpdateTableWorkflowGroupRequestMappingUpdatesItem,
)
from .types.update_table_workflow_group_request_new_output_columns_item import (
    UpdateTableWorkflowGroupRequestNewOutputColumnsItem,
)
from .types.update_table_workflow_group_request_outputs_item import UpdateTableWorkflowGroupRequestOutputsItem
from .types.update_table_workflow_group_request_type import UpdateTableWorkflowGroupRequestType


OMIT = typing.cast(typing.Any, ...)


class TablesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTablesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTablesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTablesClient
        """
        return self._raw_client

    def list_tables(
        self,
        *,
        workspace_id: str,
        scope: typing.Optional[ListTablesRequestScope] = None,
        folder_path: typing.Optional[FolderPathInput] = None,
        search: typing.Optional[str] = None,
        sort_by: typing.Optional[ListTablesRequestSortBy] = None,
        sort_order: typing.Optional[ListTablesRequestSortOrder] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2TableListResponse:
        """
        List active tables with folder filtering, search, sorting, and cursor pagination. Use `scope=archived` to find tables available for restoration. Workspace folder trees exceeding 10,000 folders return `413`.

        OAuth scope: `api:read`.

        Parameters
        ----------
        workspace_id : str
            Workspace whose tables should be listed.

        scope : typing.Optional[ListTablesRequestScope]
            Which lifecycle set to list: `active` (default) for live tables, `archived` for tables a delete archived and a table restore can bring back. `folderPath` resolves against active folders only, so pairing it with `scope=archived` returns an empty page when the containing folder was archived too.

        folder_path : typing.Optional[FolderPathInput]
            Restrict results to tables in this folder. Unknown folder paths contribute no matches.

        search : typing.Optional[str]
            Case-insensitive substring match against the resource name.

        sort_by : typing.Optional[ListTablesRequestSortBy]
            Field used to sort the result. Sorting by `name` is case-sensitive and follows the storage collation, so do not rely on a case-insensitive order.

        sort_order : typing.Optional[ListTablesRequestSortOrder]
            Sort direction.

        limit : typing.Optional[int]
            Maximum tables to return per page. Values outside 1–1000 are truncated and clamped into that range rather than rejected. Defaults to 100.

        cursor : typing.Optional[str]
            Opaque cursor from the previous page. Send it back with the same sort and filters; only `limit` may change. Change anything else and pagination must restart without a cursor.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2TableListResponse
            A page of tables in the workspace.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tables.list_tables(
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.list_tables(
            workspace_id=workspace_id,
            scope=scope,
            folder_path=folder_path,
            search=search,
            sort_by=sort_by,
            sort_order=sort_order,
            limit=limit,
            cursor=cursor,
            request_options=request_options,
        )
        return _response.data

    def create_table(
        self,
        *,
        name: str,
        workspace_id: str,
        schema: CreateTableRequestSchema,
        description: typing.Optional[str] = OMIT,
        folder_path: typing.Optional[FolderPathInput] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2CreateTableResponse:
        """
        Create a table with a typed column schema and optional folder placement.

        OAuth scope: `api:write`.

        Parameters
        ----------
        name : str
            Table name.

        workspace_id : str
            Unique workspace identifier.

        schema : CreateTableRequestSchema
            Initial table column definitions.

        description : typing.Optional[str]
            Optional table description.

        folder_path : typing.Optional[FolderPathInput]
            Folder in which to create the table.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2CreateTableResponse
            The created table.

        Examples
        --------
        from fern.tables import (
            CreateTableRequestSchema,
            CreateTableRequestSchemaColumnsItem,
            CreateTableRequestSchemaColumnsItemType,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tables.create_table(
            name="name",
            workspace_id="workspaceId",
            schema=CreateTableRequestSchema(
                columns=[
                    CreateTableRequestSchemaColumnsItem(
                        name="name",
                        type=CreateTableRequestSchemaColumnsItemType.STRING,
                    )
                ],
            ),
        )
        """
        _response = self._raw_client.create_table(
            name=name,
            workspace_id=workspace_id,
            schema=schema,
            description=description,
            folder_path=folder_path,
            request_options=request_options,
        )
        return _response.data

    def get_table(
        self, table_id: str, *, workspace_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> V2TableResponse:
        """
        Get a table with its metadata, column schema, locks, and current job. Workspace folder trees exceeding 10,000 folders return `413`.

        OAuth scope: `api:read`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        workspace_id : str
            Workspace that owns the table.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2TableResponse
            The requested table.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tables.get_table(
            table_id="tableId",
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.get_table(table_id, workspace_id=workspace_id, request_options=request_options)
        return _response.data

    def delete_table(
        self, table_id: str, *, workspace_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> V2DeleteTableResponse:
        """
        Archive a table while retaining its rows. Use List Tables with `scope=archived` to find it and Restore Table to recover it.

        OAuth scope: `api:write`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        workspace_id : str
            Workspace that owns the table.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2DeleteTableResponse
            Table deletion acknowledgement.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tables.delete_table(
            table_id="tableId",
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.delete_table(table_id, workspace_id=workspace_id, request_options=request_options)
        return _response.data

    def update_table(
        self,
        table_id: str,
        *,
        workspace_id: str,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        folder_path: typing.Optional[FolderPathInput] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2UpdateTableResponse:
        """
        Rename a table, edit its description, or move it to a folder. Fields are saved independently: a failed request may leave partial changes. `error.details.applied` lists saved fields; retry only the remaining fields. If absent, nothing changed. Lock flags are read-only. Workspace folder trees exceeding 10,000 folders return `413`.

        OAuth scope: `api:write`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        workspace_id : str
            Unique workspace identifier.

        name : typing.Optional[str]
            Replacement table name.

        description : typing.Optional[str]
            Replacement table description, or null to clear it.

        folder_path : typing.Optional[FolderPathInput]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2UpdateTableResponse
            The updated table.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tables.update_table(
            table_id="tableId",
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.update_table(
            table_id,
            workspace_id=workspace_id,
            name=name,
            description=description,
            folder_path=folder_path,
            request_options=request_options,
        )
        return _response.data

    def add_table_column(
        self,
        table_id: str,
        *,
        workspace_id: str,
        column: AddTableColumnRequestColumn,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2TableColumnsResponse:
        """
        Add a typed column and return the complete resulting table schema.

        OAuth scope: `api:write`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        workspace_id : str
            Workspace that owns the table.

        column : AddTableColumnRequestColumn
            Column definition to add.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2TableColumnsResponse
            The updated table columns.

        Examples
        --------
        from fern.tables import (
            AddTableColumnRequestColumn,
            AddTableColumnRequestColumnType,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tables.add_table_column(
            table_id="tableId",
            workspace_id="a91c4b2e-6d3f-4e8a-b5c7-0d9e2f1a8c64",
            column=AddTableColumnRequestColumn(
                name="plan",
                type=AddTableColumnRequestColumnType.STRING,
            ),
        )
        """
        _response = self._raw_client.add_table_column(
            table_id, workspace_id=workspace_id, column=column, request_options=request_options
        )
        return _response.data

    def delete_table_column(
        self,
        table_id: str,
        *,
        workspace_id: str,
        column_name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2TableColumnsResponse:
        """
        Delete a column by name while preserving at least one table column.

        OAuth scope: `api:write`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        workspace_id : str
            Unique workspace identifier.

        column_name : str
            Name of the column to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2TableColumnsResponse
            The surviving table columns.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tables.delete_table_column(
            table_id="tableId",
            workspace_id="a91c4b2e-6d3f-4e8a-b5c7-0d9e2f1a8c64",
            column_name="legacyStatus",
        )
        """
        _response = self._raw_client.delete_table_column(
            table_id, workspace_id=workspace_id, column_name=column_name, request_options=request_options
        )
        return _response.data

    def update_table_column(
        self,
        table_id: str,
        *,
        workspace_id: str,
        column_name: str,
        updates: UpdateTableColumnRequestUpdates,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2TableColumnsResponse:
        """
        Update a column by name and return the complete resulting table schema.

        OAuth scope: `api:write`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        workspace_id : str
            Workspace that owns the table.

        column_name : str
            Current name of the column to update.

        updates : UpdateTableColumnRequestUpdates
            Mutable column fields.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2TableColumnsResponse
            The updated table columns.

        Examples
        --------
        from fern.tables import UpdateTableColumnRequestUpdates

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tables.update_table_column(
            table_id="tableId",
            workspace_id="a91c4b2e-6d3f-4e8a-b5c7-0d9e2f1a8c64",
            column_name="plan",
            updates=UpdateTableColumnRequestUpdates(
                name="subscriptionPlan",
            ),
        )
        """
        _response = self._raw_client.update_table_column(
            table_id,
            workspace_id=workspace_id,
            column_name=column_name,
            updates=updates,
            request_options=request_options,
        )
        return _response.data

    def list_table_rows(
        self,
        table_id: str,
        *,
        workspace_id: str,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        include_run_state: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2TableRowListResponse:
        """
        List rows in default order with cursor pagination. Pages default to a 5 MB limit and may contain fewer rows than requested; continue until `nextCursor` is null. Use Query Rows for filtering and sorting. `includeRunState=true` adds per-group run outcomes and reduces the row limit.

        OAuth scope: `api:read`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        workspace_id : str
            Workspace that owns the table.

        limit : typing.Optional[int]
            Maximum rows to return per page. Must be a whole number from 1 to 1000. Defaults to 100.

        cursor : typing.Optional[str]
            Opaque cursor from the previous page. Send it back with the same sort and filters; only `limit` may change. Change anything else and pagination must restart without a cursor.

        include_run_state : typing.Optional[bool]
            Include per-workflow-group run state on every returned row. Off by default: run state is a separate sidecar read and its `blockErrors` are unbounded, so a full page carries it only when asked. Caps `limit` at 200.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2TableRowListResponse
            A page of table rows.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tables.list_table_rows(
            table_id="tableId",
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.list_table_rows(
            table_id,
            workspace_id=workspace_id,
            limit=limit,
            cursor=cursor,
            include_run_state=include_run_state,
            request_options=request_options,
        )
        return _response.data

    def create_table_rows(
        self, table_id: str, *, request: CreateTableRowsRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> V2CreateTableRowsResponse:
        """
        Insert one row with a data object or insert a bounded batch with a rows array. Cell keys are column names.

        OAuth scope: `api:write`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        request : CreateTableRowsRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2CreateTableRowsResponse
            The inserted row or rows.

        Examples
        --------
        from fern import CreateTableRowsRequestRows, FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tables.create_table_rows(
            table_id="tableId",
            request=CreateTableRowsRequestRows(
                workspace_id="workspaceId",
                rows=[{"key": "value"}],
            ),
        )
        """
        _response = self._raw_client.create_table_rows(table_id, request=request, request_options=request_options)
        return _response.data

    def delete_table_rows(
        self,
        table_id: str,
        *,
        workspace_id: str,
        filter: typing.Optional[TablePredicate] = OMIT,
        limit: typing.Optional[int] = OMIT,
        row_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2DeleteTableRowsResponse:
        """
        Delete rows by a non-empty predicate or an explicit bounded list of row identifiers.

        OAuth scope: `api:write`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        workspace_id : str
            Unique workspace identifier.

        filter : typing.Optional[TablePredicate]

        limit : typing.Optional[int]
            Maximum matching rows to delete.

        row_ids : typing.Optional[typing.Sequence[str]]
            Explicit row identifiers to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2DeleteTableRowsResponse
            The bulk deletion result.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tables.delete_table_rows(
            table_id="tableId",
            workspace_id="a91c4b2e-6d3f-4e8a-b5c7-0d9e2f1a8c64",
            row_ids=["row_1f3e5d7c9b8a4c2d806e4a6b8d0f2e93"],
        )
        """
        _response = self._raw_client.delete_table_rows(
            table_id,
            workspace_id=workspace_id,
            filter=filter,
            limit=limit,
            row_ids=row_ids,
            request_options=request_options,
        )
        return _response.data

    def update_table_rows(
        self,
        table_id: str,
        *,
        workspace_id: str,
        filter: TablePredicate,
        data: V2TableRowData,
        limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2UpdateTableRowsResponse:
        """
        Apply the same partial data patch to every row matching a non-empty predicate.

        OAuth scope: `api:write`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        workspace_id : str
            Unique workspace identifier.

        filter : TablePredicate

        data : V2TableRowData
            Row-data patch applied to every matching row.

        limit : typing.Optional[int]
            Maximum matching rows to update.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2UpdateTableRowsResponse
            The bulk update result.

        Examples
        --------
        from fern import FernApi, TablePredicateAll

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tables.update_table_rows(
            table_id="tableId",
            workspace_id="workspaceId",
            filter=TablePredicateAll(
                all_=[],
            ),
            data={"key": "value"},
        )
        """
        _response = self._raw_client.update_table_rows(
            table_id, workspace_id=workspace_id, filter=filter, data=data, limit=limit, request_options=request_options
        )
        return _response.data

    def get_table_row(
        self,
        table_id: str,
        row_id: str,
        *,
        workspace_id: str,
        include_run_state: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2TableRowResponse:
        """
        Get one row by identifier. Set `includeRunState=true` to attach the row's per-workflow-group run outcomes.

        OAuth scope: `api:read`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        row_id : str
            Unique table row identifier.

        workspace_id : str
            Workspace that owns the table.

        include_run_state : typing.Optional[bool]
            Include per-workflow-group run state on the returned row. Off by default.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2TableRowResponse
            The requested table row.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tables.get_table_row(
            table_id="tableId",
            row_id="rowId",
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.get_table_row(
            table_id,
            row_id,
            workspace_id=workspace_id,
            include_run_state=include_run_state,
            request_options=request_options,
        )
        return _response.data

    def delete_table_row(
        self, table_id: str, row_id: str, *, workspace_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> V2DeleteTableRowResponse:
        """
        Delete one row by identifier.

        OAuth scope: `api:write`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        row_id : str
            Unique table row identifier.

        workspace_id : str
            Workspace that owns the table.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2DeleteTableRowResponse
            The row deletion result.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tables.delete_table_row(
            table_id="tableId",
            row_id="rowId",
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.delete_table_row(
            table_id, row_id, workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    def update_table_row(
        self,
        table_id: str,
        row_id: str,
        *,
        workspace_id: str,
        data: V2TableRowData,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2TableRowResponse:
        """
        Merge a partial data patch into one row by identifier.

        OAuth scope: `api:write`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        row_id : str
            Unique table row identifier.

        workspace_id : str
            Unique workspace identifier.

        data : V2TableRowData
            Partial row-data patch keyed by column name.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2TableRowResponse
            The updated table row.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tables.update_table_row(
            table_id="tableId",
            row_id="rowId",
            workspace_id="a91c4b2e-6d3f-4e8a-b5c7-0d9e2f1a8c64",
            data={"status": "active"},
        )
        """
        _response = self._raw_client.update_table_row(
            table_id, row_id, workspace_id=workspace_id, data=data, request_options=request_options
        )
        return _response.data

    def upsert_table_row(
        self,
        table_id: str,
        *,
        workspace_id: str,
        data: V2TableRowData,
        conflict_target: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2UpsertTableRowResponse:
        """
        Insert a row or replace the row matching a selected unique column. On replacement, omitted columns are cleared; send the complete row. Use Update Row for a partial patch.

        OAuth scope: `api:write`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        workspace_id : str
            Unique workspace identifier.

        data : V2TableRowData
            Complete set of row cells keyed by column name. On the update branch this REPLACES the matched row: any column not present here is cleared, unlike a single-row update, which merges.

        conflict_target : typing.Optional[str]
            Unique column used to detect a conflict.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2UpsertTableRowResponse
            The upserted row and operation performed.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tables.upsert_table_row(
            table_id="tableId",
            workspace_id="a91c4b2e-6d3f-4e8a-b5c7-0d9e2f1a8c64",
            data={"email": "jane@example.com", "status": "active"},
            conflict_target="email",
        )
        """
        _response = self._raw_client.upsert_table_row(
            table_id,
            workspace_id=workspace_id,
            data=data,
            conflict_target=conflict_target,
            request_options=request_options,
        )
        return _response.data

    def query_table_rows(
        self,
        table_id: str,
        *,
        workspace_id: str,
        predicate: typing.Optional[TablePredicateInput] = OMIT,
        sort: typing.Optional[typing.Sequence[QueryTableRowsRequestSortItem]] = OMIT,
        limit: typing.Optional[int] = OMIT,
        cursor: typing.Optional[str] = OMIT,
        include_run_state: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2QueryTableRowsResponse:
        """
        Query rows with typed predicates, sorting, and cursor pagination. Omit the predicate to match all rows. Pages default to a 5 MB limit; continue until `nextCursor` is null. Oversized predicates return `413`. `includeRunState` adds per-group outcomes and reduces the row limit. Counts are read separately and can differ from paged results if rows change.

        OAuth scope: `api:read`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        workspace_id : str
            Unique workspace identifier.

        predicate : typing.Optional[TablePredicateInput]

        sort : typing.Optional[typing.Sequence[QueryTableRowsRequestSortItem]]
            Ordered table-row sort specification.

        limit : typing.Optional[int]
            Maximum rows to return; zero requests an unbounded result.

        cursor : typing.Optional[str]
            Opaque cursor returned by the previous query page.

        include_run_state : typing.Optional[bool]
            Include per-workflow-group run state on every returned row. Off by default: run state is a separate sidecar read and its `blockErrors` are unbounded, so a full page carries it only when asked. Incompatible with `limit: 0`, and caps `limit` at 200.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2QueryTableRowsResponse
            A page of matching table rows.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tables.query_table_rows(
            table_id="tableId",
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.query_table_rows(
            table_id,
            workspace_id=workspace_id,
            predicate=predicate,
            sort=sort,
            limit=limit,
            cursor=cursor,
            include_run_state=include_run_state,
            request_options=request_options,
        )
        return _response.data

    def count_table_rows(
        self,
        table_id: str,
        *,
        workspace_id: str,
        predicate: typing.Optional[TablePredicateInput] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2CountTableRowsResponse:
        """
        Count rows matching a typed predicate, or omit the predicate to count all rows. The count is read separately from row pages and can change between requests. Oversized predicates return `413`.

        OAuth scope: `api:read`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        workspace_id : str
            Unique workspace identifier.

        predicate : typing.Optional[TablePredicateInput]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2CountTableRowsResponse
            The number of matching table rows.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tables.count_table_rows(
            table_id="tableId",
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.count_table_rows(
            table_id, workspace_id=workspace_id, predicate=predicate, request_options=request_options
        )
        return _response.data

    def list_table_views(
        self, table_id: str, *, workspace_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> V2TableViewListResponse:
        """
        List saved table views, omitting references to removed columns. Returns the complete set in one page; `nextCursor` is always null.

        OAuth scope: `api:read`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        workspace_id : str
            Workspace that owns the table.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2TableViewListResponse
            The saved table views.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tables.list_table_views(
            table_id="tableId",
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.list_table_views(
            table_id, workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    def create_table_view(
        self,
        table_id: str,
        *,
        workspace_id: str,
        name: str,
        config: CreateTableViewRequestConfig,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2CreateTableViewResponse:
        """
        Save a filter, sort, and column layout as a named presentation of a table.

        OAuth scope: `api:write`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        workspace_id : str
            Workspace that owns the table.

        name : str
            Saved-view display name.

        config : CreateTableViewRequestConfig
            Saved filter, sort, and column-layout configuration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2CreateTableViewResponse
            The created table view.

        Examples
        --------
        from fern.tables import CreateTableViewRequestConfig

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tables.create_table_view(
            table_id="tableId",
            workspace_id="workspaceId",
            name="name",
            config=CreateTableViewRequestConfig(),
        )
        """
        _response = self._raw_client.create_table_view(
            table_id, workspace_id=workspace_id, name=name, config=config, request_options=request_options
        )
        return _response.data

    def get_table_view(
        self, table_id: str, view_id: str, *, workspace_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> V2TableViewResponse:
        """
        Get one saved table view by identifier.

        OAuth scope: `api:read`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        view_id : str
            Unique saved-view identifier.

        workspace_id : str
            Workspace that owns the table.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2TableViewResponse
            The requested table view.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tables.get_table_view(
            table_id="tableId",
            view_id="viewId",
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.get_table_view(
            table_id, view_id, workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    def delete_table_view(
        self, table_id: str, view_id: str, *, workspace_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> V2DeleteTableViewResponse:
        """
        Delete a saved presentation without changing any table rows.

        OAuth scope: `api:write`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        view_id : str
            Unique saved-view identifier.

        workspace_id : str
            Workspace that owns the table.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2DeleteTableViewResponse
            Table view deletion acknowledgement.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tables.delete_table_view(
            table_id="tableId",
            view_id="viewId",
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.delete_table_view(
            table_id, view_id, workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    def update_table_view(
        self,
        table_id: str,
        view_id: str,
        *,
        workspace_id: str,
        name: typing.Optional[str] = OMIT,
        config: typing.Optional[UpdateTableViewRequestConfig] = OMIT,
        config_patch: typing.Optional[UpdateTableViewRequestConfigPatch] = OMIT,
        is_default: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2TableViewResponse:
        """
        Rename a view, replace or shallow-merge its configuration, or promote it to the table default.

        OAuth scope: `api:write`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        view_id : str
            Unique saved-view identifier.

        workspace_id : str
            Workspace that owns the table.

        name : typing.Optional[str]
            Replacement saved-view display name.

        config : typing.Optional[UpdateTableViewRequestConfig]
            Complete replacement saved-view configuration.

        config_patch : typing.Optional[UpdateTableViewRequestConfigPatch]
            Saved-view configuration fields to shallow-merge.

        is_default : typing.Optional[bool]
            Whether to promote this view to the table default.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2TableViewResponse
            The updated table view.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tables.update_table_view(
            table_id="tableId",
            view_id="viewId",
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.update_table_view(
            table_id,
            view_id,
            workspace_id=workspace_id,
            name=name,
            config=config,
            config_patch=config_patch,
            is_default=is_default,
            request_options=request_options,
        )
        return _response.data

    def list_table_workflow_groups(
        self, table_id: str, *, workspace_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> V2TableWorkflowGroupListResponse:
        """
        List the workflow and enrichment groups that can be dispatched for a table. Returns the complete set in one page; `nextCursor` is always null.

        OAuth scope: `api:read`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        workspace_id : str
            Workspace that owns the table.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2TableWorkflowGroupListResponse
            The table workflow groups.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tables.list_table_workflow_groups(
            table_id="tableId",
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.list_table_workflow_groups(
            table_id, workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    def add_table_workflow_group(
        self,
        table_id: str,
        *,
        workspace_id: str,
        group: AddTableWorkflowGroupRequestGroup,
        output_columns: typing.Sequence[AddTableWorkflowGroupRequestOutputColumnsItem],
        auto_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2AddTableWorkflowGroupResponse:
        """
        Bind a workflow or enrichment to the table and create the columns populated by its outputs.

        OAuth scope: `api:write`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        workspace_id : str
            Unique workspace identifier.

        group : AddTableWorkflowGroupRequestGroup
            Workflow or enrichment producer definition.

        output_columns : typing.Sequence[AddTableWorkflowGroupRequestOutputColumnsItem]
            Columns created for producer outputs.

        auto_run : typing.Optional[bool]
            Whether to schedule existing rows after group creation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2AddTableWorkflowGroupResponse
            The created workflow group and resulting columns.

        Examples
        --------
        from fern.tables import (
            AddTableWorkflowGroupRequestGroup,
            AddTableWorkflowGroupRequestGroupOutputsItem,
            AddTableWorkflowGroupRequestOutputColumnsItem,
            AddTableWorkflowGroupRequestOutputColumnsItemType,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tables.add_table_workflow_group(
            table_id="tableId",
            workspace_id="a91c4b2e-6d3f-4e8a-b5c7-0d9e2f1a8c64",
            group=AddTableWorkflowGroupRequestGroup(
                workflow_id="3b1f7c92-8d4e-4a6b-9c0d-5e2f8a714b36",
                name="Enrich company",
                outputs=[
                    AddTableWorkflowGroupRequestGroupOutputsItem(
                        block_id="block_lookup",
                        path="output.revenue",
                        column_name="revenue",
                    )
                ],
            ),
            output_columns=[
                AddTableWorkflowGroupRequestOutputColumnsItem(
                    name="revenue",
                    type=AddTableWorkflowGroupRequestOutputColumnsItemType.NUMBER,
                )
            ],
        )
        """
        _response = self._raw_client.add_table_workflow_group(
            table_id,
            workspace_id=workspace_id,
            group=group,
            output_columns=output_columns,
            auto_run=auto_run,
            request_options=request_options,
        )
        return _response.data

    def delete_table_workflow_group(
        self,
        table_id: str,
        *,
        workspace_id: str,
        group_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2DeleteTableWorkflowGroupResponse:
        """
        Delete a workflow group and every table column populated by that group.

        OAuth scope: `api:write`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        workspace_id : str
            Unique workspace identifier.

        group_id : str
            Workflow group to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2DeleteTableWorkflowGroupResponse
            Workflow-group deletion acknowledgement and surviving columns.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tables.delete_table_workflow_group(
            table_id="tableId",
            workspace_id="a91c4b2e-6d3f-4e8a-b5c7-0d9e2f1a8c64",
            group_id="grp_5d8b2f0a6c1e4739a8b3d5f7e9c1a204",
        )
        """
        _response = self._raw_client.delete_table_workflow_group(
            table_id, workspace_id=workspace_id, group_id=group_id, request_options=request_options
        )
        return _response.data

    def update_table_workflow_group(
        self,
        table_id: str,
        *,
        workspace_id: str,
        group_id: str,
        workflow_id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        dependencies: typing.Optional[UpdateTableWorkflowGroupRequestDependencies] = OMIT,
        outputs: typing.Optional[typing.Sequence[UpdateTableWorkflowGroupRequestOutputsItem]] = OMIT,
        new_output_columns: typing.Optional[
            typing.Sequence[UpdateTableWorkflowGroupRequestNewOutputColumnsItem]
        ] = OMIT,
        mapping_updates: typing.Optional[typing.Sequence[UpdateTableWorkflowGroupRequestMappingUpdatesItem]] = OMIT,
        input_mappings: typing.Optional[typing.Sequence[UpdateTableWorkflowGroupRequestInputMappingsItem]] = OMIT,
        deployment_mode: typing.Optional[UpdateTableWorkflowGroupRequestDeploymentMode] = OMIT,
        type: typing.Optional[UpdateTableWorkflowGroupRequestType] = OMIT,
        auto_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2UpdateTableWorkflowGroupResponse:
        """
        Restructure a workflow group, its producer, outputs, or execution behavior. Repointing the group at a different workflow concurrently invalidates the resolved output types and returns `409` — retry the update.

        OAuth scope: `api:write`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        workspace_id : str
            Unique workspace identifier.

        group_id : str
            Workflow group to update.

        workflow_id : typing.Optional[str]
            Replacement backing workflow identifier.

        name : typing.Optional[str]
            Replacement workflow-group display name.

        dependencies : typing.Optional[UpdateTableWorkflowGroupRequestDependencies]
            Replacement input dependencies.

        outputs : typing.Optional[typing.Sequence[UpdateTableWorkflowGroupRequestOutputsItem]]
            Replacement producer outputs.

        new_output_columns : typing.Optional[typing.Sequence[UpdateTableWorkflowGroupRequestNewOutputColumnsItem]]
            Columns to add for new outputs.

        mapping_updates : typing.Optional[typing.Sequence[UpdateTableWorkflowGroupRequestMappingUpdatesItem]]
            Existing output-column mapping changes.

        input_mappings : typing.Optional[typing.Sequence[UpdateTableWorkflowGroupRequestInputMappingsItem]]
            Replacement workflow input mappings.

        deployment_mode : typing.Optional[UpdateTableWorkflowGroupRequestDeploymentMode]
            Replacement workflow execution mode.

        type : typing.Optional[UpdateTableWorkflowGroupRequestType]
            Workflow-group producer type. Must match the group's stored type — a group's producer cannot be changed after creation.

        auto_run : typing.Optional[bool]
            Replacement automatic-run setting.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2UpdateTableWorkflowGroupResponse
            The updated workflow group and resulting columns.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tables.update_table_workflow_group(
            table_id="tableId",
            workspace_id="a91c4b2e-6d3f-4e8a-b5c7-0d9e2f1a8c64",
            group_id="grp_5d8b2f0a6c1e4739a8b3d5f7e9c1a204",
            name="Company profile enrichment",
        )
        """
        _response = self._raw_client.update_table_workflow_group(
            table_id,
            workspace_id=workspace_id,
            group_id=group_id,
            workflow_id=workflow_id,
            name=name,
            dependencies=dependencies,
            outputs=outputs,
            new_output_columns=new_output_columns,
            mapping_updates=mapping_updates,
            input_mappings=input_mappings,
            deployment_mode=deployment_mode,
            type=type,
            auto_run=auto_run,
            request_options=request_options,
        )
        return _response.data

    def list_table_dispatches(
        self, table_id: str, *, workspace_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> V2TableRunDispatchListResponse:
        """
        List in-flight run dispatches for a table in one page; `nextCursor` is always null. Use Get Run Dispatch to read a settled dispatch.

        OAuth scope: `api:read`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        workspace_id : str
            Workspace that owns the table.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2TableRunDispatchListResponse
            The table's active run dispatches.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tables.list_table_dispatches(
            table_id="tableId",
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.list_table_dispatches(
            table_id, workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    def create_table_dispatch(
        self,
        table_id: str,
        *,
        workspace_id: str,
        group_ids: typing.Sequence[str],
        run_mode: typing.Optional[CreateTableDispatchRequestRunMode] = OMIT,
        row_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        filter: typing.Optional[TablePredicate] = OMIT,
        exclude_row_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        limit: typing.Optional[CreateTableDispatchRequestLimit] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2CreateTableDispatchResponse:
        """
        Start workflow or enrichment groups across all rows or selected rows. Poll Get Run Dispatch until `complete` or `canceled`. A null `dispatchId` means no dispatch is available to poll; check row outcomes with `includeRunState`. Use Cancel Run Dispatch to stop further scheduling.

        OAuth scope: `api:write`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        workspace_id : str
            Unique workspace identifier.

        group_ids : typing.Sequence[str]
            Workflow or enrichment groups to run.

        run_mode : typing.Optional[CreateTableDispatchRequestRunMode]
            Whether to run all or only incomplete cells.

        row_ids : typing.Optional[typing.Sequence[str]]
            Explicit row subset to run.

        filter : typing.Optional[TablePredicate]

        exclude_row_ids : typing.Optional[typing.Sequence[str]]
            Rows excluded from a select-all run scope.

        limit : typing.Optional[CreateTableDispatchRequestLimit]
            Optional cap on eligible rows to run.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2CreateTableDispatchResponse
            The accepted run dispatch.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tables.create_table_dispatch(
            table_id="tableId",
            workspace_id="a91c4b2e-6d3f-4e8a-b5c7-0d9e2f1a8c64",
            group_ids=["grp_5d8b2f0a6c1e4739a8b3d5f7e9c1a204"],
        )
        """
        _response = self._raw_client.create_table_dispatch(
            table_id,
            workspace_id=workspace_id,
            group_ids=group_ids,
            run_mode=run_mode,
            row_ids=row_ids,
            filter=filter,
            exclude_row_ids=exclude_row_ids,
            limit=limit,
            request_options=request_options,
        )
        return _response.data

    def get_row_enrichment(
        self,
        table_id: str,
        row_id: str,
        group_id: str,
        *,
        workspace_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2RowEnrichmentResponse:
        """
        Get an enrichment cell's provider attempts, statuses, hosted-key costs, durations, and matching provider. Null means no run detail was recorded; `404` means the table, row, or group does not exist.

        OAuth scope: `api:read`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        row_id : str
            Unique table row identifier.

        group_id : str
            Workflow or enrichment group to run.

        workspace_id : str
            Workspace that owns the table.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2RowEnrichmentResponse
            The enrichment run detail, or null when none was recorded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tables.get_row_enrichment(
            table_id="tableId",
            row_id="rowId",
            group_id="groupId",
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.get_row_enrichment(
            table_id, row_id, group_id, workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    def run_row_enrichment(
        self,
        table_id: str,
        row_id: str,
        group_id: str,
        *,
        workspace_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2RunRowEnrichmentResponse:
        """
        Start one workflow or enrichment group for a table row. Poll Get Run Dispatch using the returned `dispatchId`. A null `dispatchId` means no dispatch is available to poll; check row outcomes with `includeRunState`.

        OAuth scope: `api:write`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        row_id : str
            Unique table row identifier.

        group_id : str
            Workflow or enrichment group to run.

        workspace_id : str
            Unique workspace identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2RunRowEnrichmentResponse
            The accepted row enrichment dispatch.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tables.run_row_enrichment(
            table_id="tableId",
            row_id="rowId",
            group_id="groupId",
            workspace_id="a91c4b2e-6d3f-4e8a-b5c7-0d9e2f1a8c64",
        )
        """
        _response = self._raw_client.run_row_enrichment(
            table_id, row_id, group_id, workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    def search_table_rows(
        self,
        table_id: str,
        *,
        workspace_id: str,
        q: str,
        predicate: typing.Optional[TablePredicate] = OMIT,
        sort: typing.Optional[typing.Sequence[SearchTableRowsRequestSortItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2SearchTableRowsResponse:
        """
        Search cell text for a case-insensitive substring within an optional filtered and sorted view. Returns cell coordinates, not row data; `ordinal` matches the view used by Query Rows. Results are unpaginated and capped at 1000. If `truncated` is true, narrow the search or predicate.

        OAuth scope: `api:read`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        workspace_id : str
            Unique workspace identifier.

        q : str
            Case-insensitive cell substring to find.

        predicate : typing.Optional[TablePredicate]

        sort : typing.Optional[typing.Sequence[SearchTableRowsRequestSortItem]]
            Ordered table-row sort specification.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2SearchTableRowsResponse
            The matching table cells.

        Examples
        --------
        from fern import (
            FernApi,
            TablePredicateAll,
            TablePredicateAllAllItemField,
            TablePredicateAllAllItemFieldOp,
        )

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tables.search_table_rows(
            table_id="tableId",
            workspace_id="a91c4b2e-6d3f-4e8a-b5c7-0d9e2f1a8c64",
            q="acme",
            predicate=TablePredicateAll(
                all_=[
                    TablePredicateAllAllItemField(
                        field="status",
                        op=TablePredicateAllAllItemFieldOp.EQ,
                        value="active",
                    )
                ],
            ),
        )
        """
        _response = self._raw_client.search_table_rows(
            table_id, workspace_id=workspace_id, q=q, predicate=predicate, sort=sort, request_options=request_options
        )
        return _response.data

    def create_table_import(
        self,
        *,
        workspace_id: str,
        source: CreateTableImportRequestSource,
        target: CreateTableImportRequestTarget,
        mapping: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        create_columns: typing.Optional[typing.Sequence[str]] = OMIT,
        timezone: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2CreateTableImportResponse:
        """
        Create a CSV import. Upload sources receive signed transfer instructions; workspace-file sources start processing directly.

        OAuth scope: `api:write`.

        Parameters
        ----------
        workspace_id : str
            Unique workspace identifier.

        source : CreateTableImportRequestSource
            CSV source for the import.

        target : CreateTableImportRequestTarget
            New or existing table import target.

        mapping : typing.Optional[typing.Dict[str, typing.Optional[str]]]
            CSV headers mapped to existing table columns.

        create_columns : typing.Optional[typing.Sequence[str]]
            CSV headers for which new columns should be created.

        timezone : typing.Optional[str]
            IANA timezone used to interpret local date values.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2CreateTableImportResponse
            The created table import and optional transfer instructions.

        Examples
        --------
        from fern.tables import (
            CreateTableImportRequestSource_Upload,
            CreateTableImportRequestTarget_New,
        )

        from fern import FernApi, V2TableUploadImportSourceType

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tables.create_table_import(
            workspace_id="workspaceId",
            source=CreateTableImportRequestSource_Upload(
                type=V2TableUploadImportSourceType.UPLOAD,
                name="name",
                content_type="contentType",
                size=1,
            ),
            target=CreateTableImportRequestTarget_New(
                name="name",
            ),
        )
        """
        _response = self._raw_client.create_table_import(
            workspace_id=workspace_id,
            source=source,
            target=target,
            mapping=mapping,
            create_columns=create_columns,
            timezone=timezone,
            request_options=request_options,
        )
        return _response.data

    def get_table_import(
        self,
        import_id: str,
        *,
        workspace_id: str,
        upload_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2TableImportResponse:
        """
        Get an import's progress and status. During `uploading`, the signed upload token is required; omitting it returns `404`.

        OAuth scope: `api:read`.

        Parameters
        ----------
        import_id : str
            Unique table-import identifier.

        workspace_id : str
            Workspace that owns the transfer resource.

        upload_token : typing.Optional[str]
            Signed upload control token returned when an upload-backed import was created.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2TableImportResponse
            The requested table import.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tables.get_table_import(
            import_id="importId",
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.get_table_import(
            import_id, workspace_id=workspace_id, upload_token=upload_token, request_options=request_options
        )
        return _response.data

    def cancel_table_import(
        self,
        import_id: str,
        *,
        workspace_id: str,
        upload_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2CancelTableImportResponse:
        """
        Cancel an upload or processing import. Committed row batches remain. Non-cancelable states, including `expired`, return `409`; unknown or purged imports return `404`.

        OAuth scope: `api:write`.

        Parameters
        ----------
        import_id : str
            Unique table-import identifier.

        workspace_id : str
            Workspace that owns the transfer resource.

        upload_token : typing.Optional[str]
            Signed upload control token returned when an upload-backed import was created.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2CancelTableImportResponse
            The canceled table import.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tables.cancel_table_import(
            import_id="importId",
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.cancel_table_import(
            import_id, workspace_id=workspace_id, upload_token=upload_token, request_options=request_options
        )
        return _response.data

    def create_table_import_part_urls(
        self,
        import_id: str,
        *,
        workspace_id: str,
        upload_token: str,
        part_numbers: typing.Sequence[int],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2CreateTableImportPartUrlsResponse:
        """
        Create signed URLs for multipart upload parts. Requires the `uploading` state; other states return `409`. Unknown or purged imports return `404`.

        OAuth scope: `api:write`.

        Parameters
        ----------
        import_id : str
            Unique table-import identifier.

        workspace_id : str
            Workspace that owns the transfer resource.

        upload_token : str
            Signed upload control token returned when the upload session was created.

        part_numbers : typing.Sequence[int]
            Multipart part numbers for which signed URLs should be created.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2CreateTableImportPartUrlsResponse
            The signed multipart upload URLs.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tables.create_table_import_part_urls(
            import_id="importId",
            upload_token="upload-token",
            workspace_id="workspaceId",
            part_numbers=[1, 2, 3],
        )
        """
        _response = self._raw_client.create_table_import_part_urls(
            import_id,
            workspace_id=workspace_id,
            upload_token=upload_token,
            part_numbers=part_numbers,
            request_options=request_options,
        )
        return _response.data

    def complete_table_import_upload(
        self,
        import_id: str,
        *,
        workspace_id: str,
        upload_token: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2CompleteTableImportUploadResponse:
        """
        Verify or assemble uploaded CSV bytes and start processing under the same import ID. Requires an import awaiting upload completion; other states return `409`. Unknown or purged imports return `404`.

        OAuth scope: `api:write`.

        Parameters
        ----------
        import_id : str
            Unique table-import identifier.

        workspace_id : str
            Workspace that owns the transfer resource.

        upload_token : str
            Signed upload control token returned when the upload session was created.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2CompleteTableImportUploadResponse
            The table import after upload completion.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tables.complete_table_import_upload(
            import_id="importId",
            upload_token="upload-token",
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.complete_table_import_upload(
            import_id, workspace_id=workspace_id, upload_token=upload_token, request_options=request_options
        )
        return _response.data

    def create_table_export(
        self,
        table_id: str,
        *,
        workspace_id: str,
        format: typing.Optional[CreateTableExportRequestFormat] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2CreateTableExportResponse:
        """
        Create a CSV or JSON export. Exports of small tables finish during the request; larger exports run asynchronously.

        OAuth scope: `api:write`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        workspace_id : str
            Unique workspace identifier.

        format : typing.Optional[CreateTableExportRequestFormat]
            Export file format.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2CreateTableExportResponse
            The created table export.

        Examples
        --------
        from fern.tables import CreateTableExportRequestFormat

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tables.create_table_export(
            table_id="tableId",
            workspace_id="a91c4b2e-6d3f-4e8a-b5c7-0d9e2f1a8c64",
            format=CreateTableExportRequestFormat.CSV,
        )
        """
        _response = self._raw_client.create_table_export(
            table_id, workspace_id=workspace_id, format=format, request_options=request_options
        )
        return _response.data

    def get_table_export(
        self,
        table_id: str,
        export_id: str,
        *,
        workspace_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2TableExportResponse:
        """
        Get a table export's progress and status.

        OAuth scope: `api:read`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        export_id : str
            Unique table-export identifier.

        workspace_id : str
            Workspace that owns the transfer resource.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2TableExportResponse
            The requested table export.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tables.get_table_export(
            table_id="tableId",
            export_id="exportId",
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.get_table_export(
            table_id, export_id, workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    def cancel_table_export(
        self,
        table_id: str,
        export_id: str,
        *,
        workspace_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2CancelTableExportResponse:
        """
        Cancel an export that is still in progress.

        OAuth scope: `api:write`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        export_id : str
            Unique table-export identifier.

        workspace_id : str
            Workspace that owns the transfer resource.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2CancelTableExportResponse
            The canceled table export.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tables.cancel_table_export(
            table_id="tableId",
            export_id="exportId",
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.cancel_table_export(
            table_id, export_id, workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    def download_table_export(
        self,
        table_id: str,
        export_id: str,
        *,
        workspace_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2DownloadTableExportResponse:
        """
        Get a short-lived signed download URL for a completed export. Other states return `409`; an unavailable export file returns `404`.

        OAuth scope: `api:read`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        export_id : str
            Unique table-export identifier.

        workspace_id : str
            Workspace that owns the transfer resource.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2DownloadTableExportResponse
            Signed table-export download information.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tables.download_table_export(
            table_id="tableId",
            export_id="exportId",
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.download_table_export(
            table_id, export_id, workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    def cancel_table_runs(
        self,
        table_id: str,
        *,
        workspace_id: str,
        scope: CancelTableRunsRequestScope,
        row_id: typing.Optional[str] = OMIT,
        filter: typing.Optional[TablePredicate] = OMIT,
        exclude_row_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2CancelTableRunsResponse:
        """
        Stop in-flight and pending workflow or enrichment cell runs across the table or one selected row.

        OAuth scope: `api:write`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        workspace_id : str
            Unique workspace identifier.

        scope : CancelTableRunsRequestScope
            Whether to cancel across the table or one row.

        row_id : typing.Optional[str]
            Row whose runs should be canceled for row scope.

        filter : typing.Optional[TablePredicate]

        exclude_row_ids : typing.Optional[typing.Sequence[str]]
            Rows excluded from an all-scope cancellation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2CancelTableRunsResponse
            The number of canceled cell runs.

        Examples
        --------
        from fern.tables import CancelTableRunsRequestScope

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tables.cancel_table_runs(
            table_id="tableId",
            workspace_id="a91c4b2e-6d3f-4e8a-b5c7-0d9e2f1a8c64",
            scope=CancelTableRunsRequestScope.ROW,
            row_id="row_1f3e5d7c9b8a4c2d806e4a6b8d0f2e93",
        )
        """
        _response = self._raw_client.cancel_table_runs(
            table_id,
            workspace_id=workspace_id,
            scope=scope,
            row_id=row_id,
            filter=filter,
            exclude_row_ids=exclude_row_ids,
            request_options=request_options,
        )
        return _response.data

    def list_tables_folders(
        self,
        *,
        workspace_id: str,
        parent_path: typing.Optional[FolderPathInput] = None,
        search: typing.Optional[str] = None,
        sort_by: typing.Optional[ListTablesFoldersRequestSortBy] = None,
        sort_order: typing.Optional[ListTablesFoldersRequestSortOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2TableFolderListResponse:
        """
        List table folders, optionally limiting results to direct children of a parent path. Returns the complete set in one page; `nextCursor` is always null.

        OAuth scope: `api:read`.

        Parameters
        ----------
        workspace_id : str
            Workspace whose folders should be listed.

        parent_path : typing.Optional[FolderPathInput]
            Restrict results to direct children of this parent path. Unknown folder paths contribute no matches.

        search : typing.Optional[str]
            Case-insensitive substring match against the folder name.

        sort_by : typing.Optional[ListTablesFoldersRequestSortBy]
            Field used to sort the result. Sorting by `name` is case-sensitive and follows the storage collation, so do not rely on a case-insensitive order.

        sort_order : typing.Optional[ListTablesFoldersRequestSortOrder]
            Sort direction.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2TableFolderListResponse
            The table folders.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tables.list_tables_folders(
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.list_tables_folders(
            workspace_id=workspace_id,
            parent_path=parent_path,
            search=search,
            sort_by=sort_by,
            sort_order=sort_order,
            request_options=request_options,
        )
        return _response.data

    def create_tables_folder(
        self,
        *,
        workspace_id: str,
        path: NonRootFolderPathInput,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2CreateTableFolderResponse:
        """
        Create one table-folder leaf whose parent path already exists.

        OAuth scope: `api:write`.

        Parameters
        ----------
        workspace_id : str
            Workspace in which to create the folder.

        path : NonRootFolderPathInput
            Path of the folder to create.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2CreateTableFolderResponse
            The created table folder.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tables.create_tables_folder(
            workspace_id="workspaceId",
            path="path",
        )
        """
        _response = self._raw_client.create_tables_folder(
            workspace_id=workspace_id, path=path, request_options=request_options
        )
        return _response.data

    def delete_tables_folder(
        self,
        *,
        workspace_id: str,
        path: NonRootFolderPathInput,
        recursive: typing.Optional[DeleteTablesFolderRequestRecursive] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2DeleteTableFolderResponse:
        """
        Archive an empty folder, or set `recursive=true` to archive its tables and subfolders. Use Restore Folder to recover the archived contents.

        OAuth scope: `api:write`.

        Parameters
        ----------
        workspace_id : str
            Workspace containing the folder.

        path : NonRootFolderPathInput
            Path of the folder to delete.

        recursive : typing.Optional[DeleteTablesFolderRequestRecursive]
            Delete the folder's nested files and folders too. An empty folder deletes either way; a non-empty one needs this. The listed spellings are the whole accepted vocabulary and are case-sensitive; any other value is rejected.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2DeleteTableFolderResponse
            Table-folder deletion acknowledgement.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tables.delete_tables_folder(
            workspace_id="workspaceId",
            path="path",
        )
        """
        _response = self._raw_client.delete_tables_folder(
            workspace_id=workspace_id, path=path, recursive=recursive, request_options=request_options
        )
        return _response.data

    def relocate_tables_folder(
        self,
        *,
        workspace_id: str,
        path: NonRootFolderPathInput,
        destination_path: NonRootFolderPathInput,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2RelocateTableFolderResponse:
        """
        Rename or move a table folder and update all descendant paths.

        OAuth scope: `api:write`.

        Parameters
        ----------
        workspace_id : str
            Workspace containing the folder.

        path : NonRootFolderPathInput
            Current folder path.

        destination_path : NonRootFolderPathInput
            New full path for the folder and its descendants.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2RelocateTableFolderResponse
            The relocated table folder.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tables.relocate_tables_folder(
            workspace_id="workspaceId",
            path="path",
            destination_path="destinationPath",
        )
        """
        _response = self._raw_client.relocate_tables_folder(
            workspace_id=workspace_id, path=path, destination_path=destination_path, request_options=request_options
        )
        return _response.data

    def restore_tables_folder(
        self,
        *,
        workspace_id: str,
        path: NonRootFolderPathInput,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2RestoreTableFolderResponse:
        """
        Restore an archived table folder, its descendants, and tables using its former path. An archived parent moves it to the root; name conflicts may change the returned `path`. Non-archived paths return `404`. Save the path from Delete Folder, because List Folders does not include archived table folders.

        OAuth scope: `api:write`.

        Parameters
        ----------
        workspace_id : str
            Workspace that owns the archived folder.

        path : NonRootFolderPathInput
            Path the folder held when a folder delete archived it.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2RestoreTableFolderResponse
            The restored table folder and what it brought back.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tables.restore_tables_folder(
            workspace_id="workspaceId",
            path="path",
        )
        """
        _response = self._raw_client.restore_tables_folder(
            workspace_id=workspace_id, path=path, request_options=request_options
        )
        return _response.data

    def restore_table(
        self, table_id: str, *, workspace_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> V2RestoreTableResponse:
        """
        Restore a table and its archived rows, views, and workflow groups. Active tables return unchanged without a new audit event. Name conflicts may change the returned `name`. Find archived tables with List Tables and `scope=archived`.

        OAuth scope: `api:write`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        workspace_id : str
            Unique workspace identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2RestoreTableResponse
            The restored table.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tables.restore_table(
            table_id="tableId",
            workspace_id="a91c4b2e-6d3f-4e8a-b5c7-0d9e2f1a8c64",
        )
        """
        _response = self._raw_client.restore_table(table_id, workspace_id=workspace_id, request_options=request_options)
        return _response.data

    def bulk_update_table_rows(
        self,
        table_id: str,
        *,
        workspace_id: str,
        updates: typing.Sequence[BulkUpdateTableRowsRequestUpdatesItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2BulkUpdateTableRowsResponse:
        """
        Apply separate partial patches to up to 1,000 rows, preserving omitted columns. A row outside the table rejects the entire request with `400` and lists missing IDs. Use Update Rows by Filter to apply one patch to every matching row.

        OAuth scope: `api:write`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        workspace_id : str
            Workspace that owns the table.

        updates : typing.Sequence[BulkUpdateTableRowsRequestUpdatesItem]
            One merge patch per row. Each row identifier may appear at most once.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2BulkUpdateTableRowsResponse
            The bulk update result.

        Examples
        --------
        from fern.tables import BulkUpdateTableRowsRequestUpdatesItem

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tables.bulk_update_table_rows(
            table_id="tableId",
            workspace_id="a91c4b2e-6d3f-4e8a-b5c7-0d9e2f1a8c64",
            updates=[
                BulkUpdateTableRowsRequestUpdatesItem(
                    row_id="row_1f3e5d7c9b8a4c2d806e4a6b8d0f2e93",
                    data={"status": "active"},
                ),
                BulkUpdateTableRowsRequestUpdatesItem(
                    row_id="row_2b4d6f8a0c1e3759b8d0f2a4c6e80193",
                    data={"status": "churned"},
                ),
            ],
        )
        """
        _response = self._raw_client.bulk_update_table_rows(
            table_id, workspace_id=workspace_id, updates=updates, request_options=request_options
        )
        return _response.data

    def get_table_dispatch(
        self,
        table_id: str,
        dispatch_id: str,
        *,
        workspace_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2TableRunDispatchResponse:
        """
        Get a dispatch's current state. Poll until `complete` or `canceled`; use row reads with `includeRunState` for per-cell outcomes.

        OAuth scope: `api:read`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        dispatch_id : str
            Unique table run-dispatch identifier.

        workspace_id : str
            Workspace that owns the transfer resource.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2TableRunDispatchResponse
            The requested run dispatch.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tables.get_table_dispatch(
            table_id="tableId",
            dispatch_id="dispatchId",
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.get_table_dispatch(
            table_id, dispatch_id, workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    def cancel_table_dispatch(
        self,
        table_id: str,
        dispatch_id: str,
        *,
        workspace_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2CancelTableDispatchResponse:
        """
        Stop a dispatch from scheduling more cells. Already queued or running cells continue; use Cancel Column Runs to stop them. Completed or canceled dispatches return unchanged.

        OAuth scope: `api:write`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        dispatch_id : str
            Unique table run-dispatch identifier.

        workspace_id : str
            Workspace that owns the transfer resource.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2CancelTableDispatchResponse
            The dispatch in its post-cancellation state.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tables.cancel_table_dispatch(
            table_id="tableId",
            dispatch_id="dispatchId",
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.cancel_table_dispatch(
            table_id, dispatch_id, workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    def move_tables(
        self,
        *,
        workspace_id: str,
        table_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        folder_paths: typing.Optional[typing.Sequence[FolderPathInput]] = OMIT,
        target_folder_path: typing.Optional[FolderPathInput] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2MoveTablesResponse:
        """
        Move up to 100 tables and folders to one destination. Items succeed or fail independently: covered tables are `skipped`, missing items are `notFound`, and lock or cycle failures include reasons in `failed`. An invalid destination rejects the request before any move.

        OAuth scope: `api:write`.

        Parameters
        ----------
        workspace_id : str
            Workspace that owns every selected item.

        table_ids : typing.Optional[typing.Sequence[str]]
            Tables to move, by identifier.

        folder_paths : typing.Optional[typing.Sequence[FolderPathInput]]
            Table folders to re-parent, by canonical path.

        target_folder_path : typing.Optional[FolderPathInput]
            Destination folder path. Omit to move the selection to the workspace root.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2MoveTablesResponse
            Per-item outcome of the bulk move.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tables.move_tables(
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.move_tables(
            workspace_id=workspace_id,
            table_ids=table_ids,
            folder_paths=folder_paths,
            target_folder_path=target_folder_path,
            request_options=request_options,
        )
        return _response.data

    def bulk_delete_tables(
        self,
        *,
        workspace_id: str,
        table_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        folder_paths: typing.Optional[typing.Sequence[FolderPathInput]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2BulkDeleteTablesResponse:
        """
        Archive up to 100 selected tables and folders, including folder contents. Items succeed or fail independently, with `skipped`, `notFound`, and `failed` outcomes. `deletedItems` includes all descendants. Use Restore Table or Restore Folder to recover archived items.

        OAuth scope: `api:write`.

        Parameters
        ----------
        workspace_id : str
            Workspace that owns every selected item.

        table_ids : typing.Optional[typing.Sequence[str]]
            Tables to archive, by identifier.

        folder_paths : typing.Optional[typing.Sequence[FolderPathInput]]
            Table folders to delete, by canonical path. Each cascades to everything inside it.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2BulkDeleteTablesResponse
            Per-item outcome of the bulk delete.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tables.bulk_delete_tables(
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.bulk_delete_tables(
            workspace_id=workspace_id, table_ids=table_ids, folder_paths=folder_paths, request_options=request_options
        )
        return _response.data


class AsyncTablesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTablesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTablesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTablesClient
        """
        return self._raw_client

    async def list_tables(
        self,
        *,
        workspace_id: str,
        scope: typing.Optional[ListTablesRequestScope] = None,
        folder_path: typing.Optional[FolderPathInput] = None,
        search: typing.Optional[str] = None,
        sort_by: typing.Optional[ListTablesRequestSortBy] = None,
        sort_order: typing.Optional[ListTablesRequestSortOrder] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2TableListResponse:
        """
        List active tables with folder filtering, search, sorting, and cursor pagination. Use `scope=archived` to find tables available for restoration. Workspace folder trees exceeding 10,000 folders return `413`.

        OAuth scope: `api:read`.

        Parameters
        ----------
        workspace_id : str
            Workspace whose tables should be listed.

        scope : typing.Optional[ListTablesRequestScope]
            Which lifecycle set to list: `active` (default) for live tables, `archived` for tables a delete archived and a table restore can bring back. `folderPath` resolves against active folders only, so pairing it with `scope=archived` returns an empty page when the containing folder was archived too.

        folder_path : typing.Optional[FolderPathInput]
            Restrict results to tables in this folder. Unknown folder paths contribute no matches.

        search : typing.Optional[str]
            Case-insensitive substring match against the resource name.

        sort_by : typing.Optional[ListTablesRequestSortBy]
            Field used to sort the result. Sorting by `name` is case-sensitive and follows the storage collation, so do not rely on a case-insensitive order.

        sort_order : typing.Optional[ListTablesRequestSortOrder]
            Sort direction.

        limit : typing.Optional[int]
            Maximum tables to return per page. Values outside 1–1000 are truncated and clamped into that range rather than rejected. Defaults to 100.

        cursor : typing.Optional[str]
            Opaque cursor from the previous page. Send it back with the same sort and filters; only `limit` may change. Change anything else and pagination must restart without a cursor.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2TableListResponse
            A page of tables in the workspace.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.list_tables(
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_tables(
            workspace_id=workspace_id,
            scope=scope,
            folder_path=folder_path,
            search=search,
            sort_by=sort_by,
            sort_order=sort_order,
            limit=limit,
            cursor=cursor,
            request_options=request_options,
        )
        return _response.data

    async def create_table(
        self,
        *,
        name: str,
        workspace_id: str,
        schema: CreateTableRequestSchema,
        description: typing.Optional[str] = OMIT,
        folder_path: typing.Optional[FolderPathInput] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2CreateTableResponse:
        """
        Create a table with a typed column schema and optional folder placement.

        OAuth scope: `api:write`.

        Parameters
        ----------
        name : str
            Table name.

        workspace_id : str
            Unique workspace identifier.

        schema : CreateTableRequestSchema
            Initial table column definitions.

        description : typing.Optional[str]
            Optional table description.

        folder_path : typing.Optional[FolderPathInput]
            Folder in which to create the table.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2CreateTableResponse
            The created table.

        Examples
        --------
        import asyncio

        from fern.tables import (
            CreateTableRequestSchema,
            CreateTableRequestSchemaColumnsItem,
            CreateTableRequestSchemaColumnsItemType,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.create_table(
                name="name",
                workspace_id="workspaceId",
                schema=CreateTableRequestSchema(
                    columns=[
                        CreateTableRequestSchemaColumnsItem(
                            name="name",
                            type=CreateTableRequestSchemaColumnsItemType.STRING,
                        )
                    ],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_table(
            name=name,
            workspace_id=workspace_id,
            schema=schema,
            description=description,
            folder_path=folder_path,
            request_options=request_options,
        )
        return _response.data

    async def get_table(
        self, table_id: str, *, workspace_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> V2TableResponse:
        """
        Get a table with its metadata, column schema, locks, and current job. Workspace folder trees exceeding 10,000 folders return `413`.

        OAuth scope: `api:read`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        workspace_id : str
            Workspace that owns the table.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2TableResponse
            The requested table.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.get_table(
                table_id="tableId",
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_table(
            table_id, workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    async def delete_table(
        self, table_id: str, *, workspace_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> V2DeleteTableResponse:
        """
        Archive a table while retaining its rows. Use List Tables with `scope=archived` to find it and Restore Table to recover it.

        OAuth scope: `api:write`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        workspace_id : str
            Workspace that owns the table.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2DeleteTableResponse
            Table deletion acknowledgement.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.delete_table(
                table_id="tableId",
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_table(
            table_id, workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    async def update_table(
        self,
        table_id: str,
        *,
        workspace_id: str,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        folder_path: typing.Optional[FolderPathInput] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2UpdateTableResponse:
        """
        Rename a table, edit its description, or move it to a folder. Fields are saved independently: a failed request may leave partial changes. `error.details.applied` lists saved fields; retry only the remaining fields. If absent, nothing changed. Lock flags are read-only. Workspace folder trees exceeding 10,000 folders return `413`.

        OAuth scope: `api:write`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        workspace_id : str
            Unique workspace identifier.

        name : typing.Optional[str]
            Replacement table name.

        description : typing.Optional[str]
            Replacement table description, or null to clear it.

        folder_path : typing.Optional[FolderPathInput]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2UpdateTableResponse
            The updated table.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.update_table(
                table_id="tableId",
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_table(
            table_id,
            workspace_id=workspace_id,
            name=name,
            description=description,
            folder_path=folder_path,
            request_options=request_options,
        )
        return _response.data

    async def add_table_column(
        self,
        table_id: str,
        *,
        workspace_id: str,
        column: AddTableColumnRequestColumn,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2TableColumnsResponse:
        """
        Add a typed column and return the complete resulting table schema.

        OAuth scope: `api:write`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        workspace_id : str
            Workspace that owns the table.

        column : AddTableColumnRequestColumn
            Column definition to add.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2TableColumnsResponse
            The updated table columns.

        Examples
        --------
        import asyncio

        from fern.tables import (
            AddTableColumnRequestColumn,
            AddTableColumnRequestColumnType,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.add_table_column(
                table_id="tableId",
                workspace_id="a91c4b2e-6d3f-4e8a-b5c7-0d9e2f1a8c64",
                column=AddTableColumnRequestColumn(
                    name="plan",
                    type=AddTableColumnRequestColumnType.STRING,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_table_column(
            table_id, workspace_id=workspace_id, column=column, request_options=request_options
        )
        return _response.data

    async def delete_table_column(
        self,
        table_id: str,
        *,
        workspace_id: str,
        column_name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2TableColumnsResponse:
        """
        Delete a column by name while preserving at least one table column.

        OAuth scope: `api:write`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        workspace_id : str
            Unique workspace identifier.

        column_name : str
            Name of the column to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2TableColumnsResponse
            The surviving table columns.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.delete_table_column(
                table_id="tableId",
                workspace_id="a91c4b2e-6d3f-4e8a-b5c7-0d9e2f1a8c64",
                column_name="legacyStatus",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_table_column(
            table_id, workspace_id=workspace_id, column_name=column_name, request_options=request_options
        )
        return _response.data

    async def update_table_column(
        self,
        table_id: str,
        *,
        workspace_id: str,
        column_name: str,
        updates: UpdateTableColumnRequestUpdates,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2TableColumnsResponse:
        """
        Update a column by name and return the complete resulting table schema.

        OAuth scope: `api:write`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        workspace_id : str
            Workspace that owns the table.

        column_name : str
            Current name of the column to update.

        updates : UpdateTableColumnRequestUpdates
            Mutable column fields.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2TableColumnsResponse
            The updated table columns.

        Examples
        --------
        import asyncio

        from fern.tables import UpdateTableColumnRequestUpdates

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.update_table_column(
                table_id="tableId",
                workspace_id="a91c4b2e-6d3f-4e8a-b5c7-0d9e2f1a8c64",
                column_name="plan",
                updates=UpdateTableColumnRequestUpdates(
                    name="subscriptionPlan",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_table_column(
            table_id,
            workspace_id=workspace_id,
            column_name=column_name,
            updates=updates,
            request_options=request_options,
        )
        return _response.data

    async def list_table_rows(
        self,
        table_id: str,
        *,
        workspace_id: str,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        include_run_state: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2TableRowListResponse:
        """
        List rows in default order with cursor pagination. Pages default to a 5 MB limit and may contain fewer rows than requested; continue until `nextCursor` is null. Use Query Rows for filtering and sorting. `includeRunState=true` adds per-group run outcomes and reduces the row limit.

        OAuth scope: `api:read`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        workspace_id : str
            Workspace that owns the table.

        limit : typing.Optional[int]
            Maximum rows to return per page. Must be a whole number from 1 to 1000. Defaults to 100.

        cursor : typing.Optional[str]
            Opaque cursor from the previous page. Send it back with the same sort and filters; only `limit` may change. Change anything else and pagination must restart without a cursor.

        include_run_state : typing.Optional[bool]
            Include per-workflow-group run state on every returned row. Off by default: run state is a separate sidecar read and its `blockErrors` are unbounded, so a full page carries it only when asked. Caps `limit` at 200.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2TableRowListResponse
            A page of table rows.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.list_table_rows(
                table_id="tableId",
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_table_rows(
            table_id,
            workspace_id=workspace_id,
            limit=limit,
            cursor=cursor,
            include_run_state=include_run_state,
            request_options=request_options,
        )
        return _response.data

    async def create_table_rows(
        self, table_id: str, *, request: CreateTableRowsRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> V2CreateTableRowsResponse:
        """
        Insert one row with a data object or insert a bounded batch with a rows array. Cell keys are column names.

        OAuth scope: `api:write`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        request : CreateTableRowsRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2CreateTableRowsResponse
            The inserted row or rows.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, CreateTableRowsRequestRows

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.create_table_rows(
                table_id="tableId",
                request=CreateTableRowsRequestRows(
                    workspace_id="workspaceId",
                    rows=[{"key": "value"}],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_table_rows(table_id, request=request, request_options=request_options)
        return _response.data

    async def delete_table_rows(
        self,
        table_id: str,
        *,
        workspace_id: str,
        filter: typing.Optional[TablePredicate] = OMIT,
        limit: typing.Optional[int] = OMIT,
        row_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2DeleteTableRowsResponse:
        """
        Delete rows by a non-empty predicate or an explicit bounded list of row identifiers.

        OAuth scope: `api:write`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        workspace_id : str
            Unique workspace identifier.

        filter : typing.Optional[TablePredicate]

        limit : typing.Optional[int]
            Maximum matching rows to delete.

        row_ids : typing.Optional[typing.Sequence[str]]
            Explicit row identifiers to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2DeleteTableRowsResponse
            The bulk deletion result.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.delete_table_rows(
                table_id="tableId",
                workspace_id="a91c4b2e-6d3f-4e8a-b5c7-0d9e2f1a8c64",
                row_ids=["row_1f3e5d7c9b8a4c2d806e4a6b8d0f2e93"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_table_rows(
            table_id,
            workspace_id=workspace_id,
            filter=filter,
            limit=limit,
            row_ids=row_ids,
            request_options=request_options,
        )
        return _response.data

    async def update_table_rows(
        self,
        table_id: str,
        *,
        workspace_id: str,
        filter: TablePredicate,
        data: V2TableRowData,
        limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2UpdateTableRowsResponse:
        """
        Apply the same partial data patch to every row matching a non-empty predicate.

        OAuth scope: `api:write`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        workspace_id : str
            Unique workspace identifier.

        filter : TablePredicate

        data : V2TableRowData
            Row-data patch applied to every matching row.

        limit : typing.Optional[int]
            Maximum matching rows to update.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2UpdateTableRowsResponse
            The bulk update result.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, TablePredicateAll

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.update_table_rows(
                table_id="tableId",
                workspace_id="workspaceId",
                filter=TablePredicateAll(
                    all_=[],
                ),
                data={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_table_rows(
            table_id, workspace_id=workspace_id, filter=filter, data=data, limit=limit, request_options=request_options
        )
        return _response.data

    async def get_table_row(
        self,
        table_id: str,
        row_id: str,
        *,
        workspace_id: str,
        include_run_state: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2TableRowResponse:
        """
        Get one row by identifier. Set `includeRunState=true` to attach the row's per-workflow-group run outcomes.

        OAuth scope: `api:read`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        row_id : str
            Unique table row identifier.

        workspace_id : str
            Workspace that owns the table.

        include_run_state : typing.Optional[bool]
            Include per-workflow-group run state on the returned row. Off by default.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2TableRowResponse
            The requested table row.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.get_table_row(
                table_id="tableId",
                row_id="rowId",
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_table_row(
            table_id,
            row_id,
            workspace_id=workspace_id,
            include_run_state=include_run_state,
            request_options=request_options,
        )
        return _response.data

    async def delete_table_row(
        self, table_id: str, row_id: str, *, workspace_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> V2DeleteTableRowResponse:
        """
        Delete one row by identifier.

        OAuth scope: `api:write`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        row_id : str
            Unique table row identifier.

        workspace_id : str
            Workspace that owns the table.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2DeleteTableRowResponse
            The row deletion result.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.delete_table_row(
                table_id="tableId",
                row_id="rowId",
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_table_row(
            table_id, row_id, workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    async def update_table_row(
        self,
        table_id: str,
        row_id: str,
        *,
        workspace_id: str,
        data: V2TableRowData,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2TableRowResponse:
        """
        Merge a partial data patch into one row by identifier.

        OAuth scope: `api:write`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        row_id : str
            Unique table row identifier.

        workspace_id : str
            Unique workspace identifier.

        data : V2TableRowData
            Partial row-data patch keyed by column name.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2TableRowResponse
            The updated table row.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.update_table_row(
                table_id="tableId",
                row_id="rowId",
                workspace_id="a91c4b2e-6d3f-4e8a-b5c7-0d9e2f1a8c64",
                data={"status": "active"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_table_row(
            table_id, row_id, workspace_id=workspace_id, data=data, request_options=request_options
        )
        return _response.data

    async def upsert_table_row(
        self,
        table_id: str,
        *,
        workspace_id: str,
        data: V2TableRowData,
        conflict_target: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2UpsertTableRowResponse:
        """
        Insert a row or replace the row matching a selected unique column. On replacement, omitted columns are cleared; send the complete row. Use Update Row for a partial patch.

        OAuth scope: `api:write`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        workspace_id : str
            Unique workspace identifier.

        data : V2TableRowData
            Complete set of row cells keyed by column name. On the update branch this REPLACES the matched row: any column not present here is cleared, unlike a single-row update, which merges.

        conflict_target : typing.Optional[str]
            Unique column used to detect a conflict.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2UpsertTableRowResponse
            The upserted row and operation performed.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.upsert_table_row(
                table_id="tableId",
                workspace_id="a91c4b2e-6d3f-4e8a-b5c7-0d9e2f1a8c64",
                data={"email": "jane@example.com", "status": "active"},
                conflict_target="email",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upsert_table_row(
            table_id,
            workspace_id=workspace_id,
            data=data,
            conflict_target=conflict_target,
            request_options=request_options,
        )
        return _response.data

    async def query_table_rows(
        self,
        table_id: str,
        *,
        workspace_id: str,
        predicate: typing.Optional[TablePredicateInput] = OMIT,
        sort: typing.Optional[typing.Sequence[QueryTableRowsRequestSortItem]] = OMIT,
        limit: typing.Optional[int] = OMIT,
        cursor: typing.Optional[str] = OMIT,
        include_run_state: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2QueryTableRowsResponse:
        """
        Query rows with typed predicates, sorting, and cursor pagination. Omit the predicate to match all rows. Pages default to a 5 MB limit; continue until `nextCursor` is null. Oversized predicates return `413`. `includeRunState` adds per-group outcomes and reduces the row limit. Counts are read separately and can differ from paged results if rows change.

        OAuth scope: `api:read`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        workspace_id : str
            Unique workspace identifier.

        predicate : typing.Optional[TablePredicateInput]

        sort : typing.Optional[typing.Sequence[QueryTableRowsRequestSortItem]]
            Ordered table-row sort specification.

        limit : typing.Optional[int]
            Maximum rows to return; zero requests an unbounded result.

        cursor : typing.Optional[str]
            Opaque cursor returned by the previous query page.

        include_run_state : typing.Optional[bool]
            Include per-workflow-group run state on every returned row. Off by default: run state is a separate sidecar read and its `blockErrors` are unbounded, so a full page carries it only when asked. Incompatible with `limit: 0`, and caps `limit` at 200.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2QueryTableRowsResponse
            A page of matching table rows.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.query_table_rows(
                table_id="tableId",
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.query_table_rows(
            table_id,
            workspace_id=workspace_id,
            predicate=predicate,
            sort=sort,
            limit=limit,
            cursor=cursor,
            include_run_state=include_run_state,
            request_options=request_options,
        )
        return _response.data

    async def count_table_rows(
        self,
        table_id: str,
        *,
        workspace_id: str,
        predicate: typing.Optional[TablePredicateInput] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2CountTableRowsResponse:
        """
        Count rows matching a typed predicate, or omit the predicate to count all rows. The count is read separately from row pages and can change between requests. Oversized predicates return `413`.

        OAuth scope: `api:read`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        workspace_id : str
            Unique workspace identifier.

        predicate : typing.Optional[TablePredicateInput]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2CountTableRowsResponse
            The number of matching table rows.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.count_table_rows(
                table_id="tableId",
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.count_table_rows(
            table_id, workspace_id=workspace_id, predicate=predicate, request_options=request_options
        )
        return _response.data

    async def list_table_views(
        self, table_id: str, *, workspace_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> V2TableViewListResponse:
        """
        List saved table views, omitting references to removed columns. Returns the complete set in one page; `nextCursor` is always null.

        OAuth scope: `api:read`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        workspace_id : str
            Workspace that owns the table.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2TableViewListResponse
            The saved table views.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.list_table_views(
                table_id="tableId",
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_table_views(
            table_id, workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    async def create_table_view(
        self,
        table_id: str,
        *,
        workspace_id: str,
        name: str,
        config: CreateTableViewRequestConfig,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2CreateTableViewResponse:
        """
        Save a filter, sort, and column layout as a named presentation of a table.

        OAuth scope: `api:write`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        workspace_id : str
            Workspace that owns the table.

        name : str
            Saved-view display name.

        config : CreateTableViewRequestConfig
            Saved filter, sort, and column-layout configuration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2CreateTableViewResponse
            The created table view.

        Examples
        --------
        import asyncio

        from fern.tables import CreateTableViewRequestConfig

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.create_table_view(
                table_id="tableId",
                workspace_id="workspaceId",
                name="name",
                config=CreateTableViewRequestConfig(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_table_view(
            table_id, workspace_id=workspace_id, name=name, config=config, request_options=request_options
        )
        return _response.data

    async def get_table_view(
        self, table_id: str, view_id: str, *, workspace_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> V2TableViewResponse:
        """
        Get one saved table view by identifier.

        OAuth scope: `api:read`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        view_id : str
            Unique saved-view identifier.

        workspace_id : str
            Workspace that owns the table.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2TableViewResponse
            The requested table view.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.get_table_view(
                table_id="tableId",
                view_id="viewId",
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_table_view(
            table_id, view_id, workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    async def delete_table_view(
        self, table_id: str, view_id: str, *, workspace_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> V2DeleteTableViewResponse:
        """
        Delete a saved presentation without changing any table rows.

        OAuth scope: `api:write`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        view_id : str
            Unique saved-view identifier.

        workspace_id : str
            Workspace that owns the table.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2DeleteTableViewResponse
            Table view deletion acknowledgement.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.delete_table_view(
                table_id="tableId",
                view_id="viewId",
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_table_view(
            table_id, view_id, workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    async def update_table_view(
        self,
        table_id: str,
        view_id: str,
        *,
        workspace_id: str,
        name: typing.Optional[str] = OMIT,
        config: typing.Optional[UpdateTableViewRequestConfig] = OMIT,
        config_patch: typing.Optional[UpdateTableViewRequestConfigPatch] = OMIT,
        is_default: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2TableViewResponse:
        """
        Rename a view, replace or shallow-merge its configuration, or promote it to the table default.

        OAuth scope: `api:write`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        view_id : str
            Unique saved-view identifier.

        workspace_id : str
            Workspace that owns the table.

        name : typing.Optional[str]
            Replacement saved-view display name.

        config : typing.Optional[UpdateTableViewRequestConfig]
            Complete replacement saved-view configuration.

        config_patch : typing.Optional[UpdateTableViewRequestConfigPatch]
            Saved-view configuration fields to shallow-merge.

        is_default : typing.Optional[bool]
            Whether to promote this view to the table default.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2TableViewResponse
            The updated table view.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.update_table_view(
                table_id="tableId",
                view_id="viewId",
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_table_view(
            table_id,
            view_id,
            workspace_id=workspace_id,
            name=name,
            config=config,
            config_patch=config_patch,
            is_default=is_default,
            request_options=request_options,
        )
        return _response.data

    async def list_table_workflow_groups(
        self, table_id: str, *, workspace_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> V2TableWorkflowGroupListResponse:
        """
        List the workflow and enrichment groups that can be dispatched for a table. Returns the complete set in one page; `nextCursor` is always null.

        OAuth scope: `api:read`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        workspace_id : str
            Workspace that owns the table.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2TableWorkflowGroupListResponse
            The table workflow groups.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.list_table_workflow_groups(
                table_id="tableId",
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_table_workflow_groups(
            table_id, workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    async def add_table_workflow_group(
        self,
        table_id: str,
        *,
        workspace_id: str,
        group: AddTableWorkflowGroupRequestGroup,
        output_columns: typing.Sequence[AddTableWorkflowGroupRequestOutputColumnsItem],
        auto_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2AddTableWorkflowGroupResponse:
        """
        Bind a workflow or enrichment to the table and create the columns populated by its outputs.

        OAuth scope: `api:write`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        workspace_id : str
            Unique workspace identifier.

        group : AddTableWorkflowGroupRequestGroup
            Workflow or enrichment producer definition.

        output_columns : typing.Sequence[AddTableWorkflowGroupRequestOutputColumnsItem]
            Columns created for producer outputs.

        auto_run : typing.Optional[bool]
            Whether to schedule existing rows after group creation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2AddTableWorkflowGroupResponse
            The created workflow group and resulting columns.

        Examples
        --------
        import asyncio

        from fern.tables import (
            AddTableWorkflowGroupRequestGroup,
            AddTableWorkflowGroupRequestGroupOutputsItem,
            AddTableWorkflowGroupRequestOutputColumnsItem,
            AddTableWorkflowGroupRequestOutputColumnsItemType,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.add_table_workflow_group(
                table_id="tableId",
                workspace_id="a91c4b2e-6d3f-4e8a-b5c7-0d9e2f1a8c64",
                group=AddTableWorkflowGroupRequestGroup(
                    workflow_id="3b1f7c92-8d4e-4a6b-9c0d-5e2f8a714b36",
                    name="Enrich company",
                    outputs=[
                        AddTableWorkflowGroupRequestGroupOutputsItem(
                            block_id="block_lookup",
                            path="output.revenue",
                            column_name="revenue",
                        )
                    ],
                ),
                output_columns=[
                    AddTableWorkflowGroupRequestOutputColumnsItem(
                        name="revenue",
                        type=AddTableWorkflowGroupRequestOutputColumnsItemType.NUMBER,
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_table_workflow_group(
            table_id,
            workspace_id=workspace_id,
            group=group,
            output_columns=output_columns,
            auto_run=auto_run,
            request_options=request_options,
        )
        return _response.data

    async def delete_table_workflow_group(
        self,
        table_id: str,
        *,
        workspace_id: str,
        group_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2DeleteTableWorkflowGroupResponse:
        """
        Delete a workflow group and every table column populated by that group.

        OAuth scope: `api:write`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        workspace_id : str
            Unique workspace identifier.

        group_id : str
            Workflow group to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2DeleteTableWorkflowGroupResponse
            Workflow-group deletion acknowledgement and surviving columns.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.delete_table_workflow_group(
                table_id="tableId",
                workspace_id="a91c4b2e-6d3f-4e8a-b5c7-0d9e2f1a8c64",
                group_id="grp_5d8b2f0a6c1e4739a8b3d5f7e9c1a204",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_table_workflow_group(
            table_id, workspace_id=workspace_id, group_id=group_id, request_options=request_options
        )
        return _response.data

    async def update_table_workflow_group(
        self,
        table_id: str,
        *,
        workspace_id: str,
        group_id: str,
        workflow_id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        dependencies: typing.Optional[UpdateTableWorkflowGroupRequestDependencies] = OMIT,
        outputs: typing.Optional[typing.Sequence[UpdateTableWorkflowGroupRequestOutputsItem]] = OMIT,
        new_output_columns: typing.Optional[
            typing.Sequence[UpdateTableWorkflowGroupRequestNewOutputColumnsItem]
        ] = OMIT,
        mapping_updates: typing.Optional[typing.Sequence[UpdateTableWorkflowGroupRequestMappingUpdatesItem]] = OMIT,
        input_mappings: typing.Optional[typing.Sequence[UpdateTableWorkflowGroupRequestInputMappingsItem]] = OMIT,
        deployment_mode: typing.Optional[UpdateTableWorkflowGroupRequestDeploymentMode] = OMIT,
        type: typing.Optional[UpdateTableWorkflowGroupRequestType] = OMIT,
        auto_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2UpdateTableWorkflowGroupResponse:
        """
        Restructure a workflow group, its producer, outputs, or execution behavior. Repointing the group at a different workflow concurrently invalidates the resolved output types and returns `409` — retry the update.

        OAuth scope: `api:write`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        workspace_id : str
            Unique workspace identifier.

        group_id : str
            Workflow group to update.

        workflow_id : typing.Optional[str]
            Replacement backing workflow identifier.

        name : typing.Optional[str]
            Replacement workflow-group display name.

        dependencies : typing.Optional[UpdateTableWorkflowGroupRequestDependencies]
            Replacement input dependencies.

        outputs : typing.Optional[typing.Sequence[UpdateTableWorkflowGroupRequestOutputsItem]]
            Replacement producer outputs.

        new_output_columns : typing.Optional[typing.Sequence[UpdateTableWorkflowGroupRequestNewOutputColumnsItem]]
            Columns to add for new outputs.

        mapping_updates : typing.Optional[typing.Sequence[UpdateTableWorkflowGroupRequestMappingUpdatesItem]]
            Existing output-column mapping changes.

        input_mappings : typing.Optional[typing.Sequence[UpdateTableWorkflowGroupRequestInputMappingsItem]]
            Replacement workflow input mappings.

        deployment_mode : typing.Optional[UpdateTableWorkflowGroupRequestDeploymentMode]
            Replacement workflow execution mode.

        type : typing.Optional[UpdateTableWorkflowGroupRequestType]
            Workflow-group producer type. Must match the group's stored type — a group's producer cannot be changed after creation.

        auto_run : typing.Optional[bool]
            Replacement automatic-run setting.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2UpdateTableWorkflowGroupResponse
            The updated workflow group and resulting columns.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.update_table_workflow_group(
                table_id="tableId",
                workspace_id="a91c4b2e-6d3f-4e8a-b5c7-0d9e2f1a8c64",
                group_id="grp_5d8b2f0a6c1e4739a8b3d5f7e9c1a204",
                name="Company profile enrichment",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_table_workflow_group(
            table_id,
            workspace_id=workspace_id,
            group_id=group_id,
            workflow_id=workflow_id,
            name=name,
            dependencies=dependencies,
            outputs=outputs,
            new_output_columns=new_output_columns,
            mapping_updates=mapping_updates,
            input_mappings=input_mappings,
            deployment_mode=deployment_mode,
            type=type,
            auto_run=auto_run,
            request_options=request_options,
        )
        return _response.data

    async def list_table_dispatches(
        self, table_id: str, *, workspace_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> V2TableRunDispatchListResponse:
        """
        List in-flight run dispatches for a table in one page; `nextCursor` is always null. Use Get Run Dispatch to read a settled dispatch.

        OAuth scope: `api:read`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        workspace_id : str
            Workspace that owns the table.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2TableRunDispatchListResponse
            The table's active run dispatches.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.list_table_dispatches(
                table_id="tableId",
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_table_dispatches(
            table_id, workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    async def create_table_dispatch(
        self,
        table_id: str,
        *,
        workspace_id: str,
        group_ids: typing.Sequence[str],
        run_mode: typing.Optional[CreateTableDispatchRequestRunMode] = OMIT,
        row_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        filter: typing.Optional[TablePredicate] = OMIT,
        exclude_row_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        limit: typing.Optional[CreateTableDispatchRequestLimit] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2CreateTableDispatchResponse:
        """
        Start workflow or enrichment groups across all rows or selected rows. Poll Get Run Dispatch until `complete` or `canceled`. A null `dispatchId` means no dispatch is available to poll; check row outcomes with `includeRunState`. Use Cancel Run Dispatch to stop further scheduling.

        OAuth scope: `api:write`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        workspace_id : str
            Unique workspace identifier.

        group_ids : typing.Sequence[str]
            Workflow or enrichment groups to run.

        run_mode : typing.Optional[CreateTableDispatchRequestRunMode]
            Whether to run all or only incomplete cells.

        row_ids : typing.Optional[typing.Sequence[str]]
            Explicit row subset to run.

        filter : typing.Optional[TablePredicate]

        exclude_row_ids : typing.Optional[typing.Sequence[str]]
            Rows excluded from a select-all run scope.

        limit : typing.Optional[CreateTableDispatchRequestLimit]
            Optional cap on eligible rows to run.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2CreateTableDispatchResponse
            The accepted run dispatch.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.create_table_dispatch(
                table_id="tableId",
                workspace_id="a91c4b2e-6d3f-4e8a-b5c7-0d9e2f1a8c64",
                group_ids=["grp_5d8b2f0a6c1e4739a8b3d5f7e9c1a204"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_table_dispatch(
            table_id,
            workspace_id=workspace_id,
            group_ids=group_ids,
            run_mode=run_mode,
            row_ids=row_ids,
            filter=filter,
            exclude_row_ids=exclude_row_ids,
            limit=limit,
            request_options=request_options,
        )
        return _response.data

    async def get_row_enrichment(
        self,
        table_id: str,
        row_id: str,
        group_id: str,
        *,
        workspace_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2RowEnrichmentResponse:
        """
        Get an enrichment cell's provider attempts, statuses, hosted-key costs, durations, and matching provider. Null means no run detail was recorded; `404` means the table, row, or group does not exist.

        OAuth scope: `api:read`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        row_id : str
            Unique table row identifier.

        group_id : str
            Workflow or enrichment group to run.

        workspace_id : str
            Workspace that owns the table.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2RowEnrichmentResponse
            The enrichment run detail, or null when none was recorded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.get_row_enrichment(
                table_id="tableId",
                row_id="rowId",
                group_id="groupId",
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_row_enrichment(
            table_id, row_id, group_id, workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    async def run_row_enrichment(
        self,
        table_id: str,
        row_id: str,
        group_id: str,
        *,
        workspace_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2RunRowEnrichmentResponse:
        """
        Start one workflow or enrichment group for a table row. Poll Get Run Dispatch using the returned `dispatchId`. A null `dispatchId` means no dispatch is available to poll; check row outcomes with `includeRunState`.

        OAuth scope: `api:write`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        row_id : str
            Unique table row identifier.

        group_id : str
            Workflow or enrichment group to run.

        workspace_id : str
            Unique workspace identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2RunRowEnrichmentResponse
            The accepted row enrichment dispatch.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.run_row_enrichment(
                table_id="tableId",
                row_id="rowId",
                group_id="groupId",
                workspace_id="a91c4b2e-6d3f-4e8a-b5c7-0d9e2f1a8c64",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.run_row_enrichment(
            table_id, row_id, group_id, workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    async def search_table_rows(
        self,
        table_id: str,
        *,
        workspace_id: str,
        q: str,
        predicate: typing.Optional[TablePredicate] = OMIT,
        sort: typing.Optional[typing.Sequence[SearchTableRowsRequestSortItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2SearchTableRowsResponse:
        """
        Search cell text for a case-insensitive substring within an optional filtered and sorted view. Returns cell coordinates, not row data; `ordinal` matches the view used by Query Rows. Results are unpaginated and capped at 1000. If `truncated` is true, narrow the search or predicate.

        OAuth scope: `api:read`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        workspace_id : str
            Unique workspace identifier.

        q : str
            Case-insensitive cell substring to find.

        predicate : typing.Optional[TablePredicate]

        sort : typing.Optional[typing.Sequence[SearchTableRowsRequestSortItem]]
            Ordered table-row sort specification.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2SearchTableRowsResponse
            The matching table cells.

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            TablePredicateAll,
            TablePredicateAllAllItemField,
            TablePredicateAllAllItemFieldOp,
        )

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.search_table_rows(
                table_id="tableId",
                workspace_id="a91c4b2e-6d3f-4e8a-b5c7-0d9e2f1a8c64",
                q="acme",
                predicate=TablePredicateAll(
                    all_=[
                        TablePredicateAllAllItemField(
                            field="status",
                            op=TablePredicateAllAllItemFieldOp.EQ,
                            value="active",
                        )
                    ],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search_table_rows(
            table_id, workspace_id=workspace_id, q=q, predicate=predicate, sort=sort, request_options=request_options
        )
        return _response.data

    async def create_table_import(
        self,
        *,
        workspace_id: str,
        source: CreateTableImportRequestSource,
        target: CreateTableImportRequestTarget,
        mapping: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        create_columns: typing.Optional[typing.Sequence[str]] = OMIT,
        timezone: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2CreateTableImportResponse:
        """
        Create a CSV import. Upload sources receive signed transfer instructions; workspace-file sources start processing directly.

        OAuth scope: `api:write`.

        Parameters
        ----------
        workspace_id : str
            Unique workspace identifier.

        source : CreateTableImportRequestSource
            CSV source for the import.

        target : CreateTableImportRequestTarget
            New or existing table import target.

        mapping : typing.Optional[typing.Dict[str, typing.Optional[str]]]
            CSV headers mapped to existing table columns.

        create_columns : typing.Optional[typing.Sequence[str]]
            CSV headers for which new columns should be created.

        timezone : typing.Optional[str]
            IANA timezone used to interpret local date values.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2CreateTableImportResponse
            The created table import and optional transfer instructions.

        Examples
        --------
        import asyncio

        from fern.tables import (
            CreateTableImportRequestSource_Upload,
            CreateTableImportRequestTarget_New,
        )

        from fern import AsyncFernApi, V2TableUploadImportSourceType

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.create_table_import(
                workspace_id="workspaceId",
                source=CreateTableImportRequestSource_Upload(
                    type=V2TableUploadImportSourceType.UPLOAD,
                    name="name",
                    content_type="contentType",
                    size=1,
                ),
                target=CreateTableImportRequestTarget_New(
                    name="name",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_table_import(
            workspace_id=workspace_id,
            source=source,
            target=target,
            mapping=mapping,
            create_columns=create_columns,
            timezone=timezone,
            request_options=request_options,
        )
        return _response.data

    async def get_table_import(
        self,
        import_id: str,
        *,
        workspace_id: str,
        upload_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2TableImportResponse:
        """
        Get an import's progress and status. During `uploading`, the signed upload token is required; omitting it returns `404`.

        OAuth scope: `api:read`.

        Parameters
        ----------
        import_id : str
            Unique table-import identifier.

        workspace_id : str
            Workspace that owns the transfer resource.

        upload_token : typing.Optional[str]
            Signed upload control token returned when an upload-backed import was created.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2TableImportResponse
            The requested table import.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.get_table_import(
                import_id="importId",
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_table_import(
            import_id, workspace_id=workspace_id, upload_token=upload_token, request_options=request_options
        )
        return _response.data

    async def cancel_table_import(
        self,
        import_id: str,
        *,
        workspace_id: str,
        upload_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2CancelTableImportResponse:
        """
        Cancel an upload or processing import. Committed row batches remain. Non-cancelable states, including `expired`, return `409`; unknown or purged imports return `404`.

        OAuth scope: `api:write`.

        Parameters
        ----------
        import_id : str
            Unique table-import identifier.

        workspace_id : str
            Workspace that owns the transfer resource.

        upload_token : typing.Optional[str]
            Signed upload control token returned when an upload-backed import was created.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2CancelTableImportResponse
            The canceled table import.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.cancel_table_import(
                import_id="importId",
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cancel_table_import(
            import_id, workspace_id=workspace_id, upload_token=upload_token, request_options=request_options
        )
        return _response.data

    async def create_table_import_part_urls(
        self,
        import_id: str,
        *,
        workspace_id: str,
        upload_token: str,
        part_numbers: typing.Sequence[int],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2CreateTableImportPartUrlsResponse:
        """
        Create signed URLs for multipart upload parts. Requires the `uploading` state; other states return `409`. Unknown or purged imports return `404`.

        OAuth scope: `api:write`.

        Parameters
        ----------
        import_id : str
            Unique table-import identifier.

        workspace_id : str
            Workspace that owns the transfer resource.

        upload_token : str
            Signed upload control token returned when the upload session was created.

        part_numbers : typing.Sequence[int]
            Multipart part numbers for which signed URLs should be created.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2CreateTableImportPartUrlsResponse
            The signed multipart upload URLs.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.create_table_import_part_urls(
                import_id="importId",
                upload_token="upload-token",
                workspace_id="workspaceId",
                part_numbers=[1, 2, 3],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_table_import_part_urls(
            import_id,
            workspace_id=workspace_id,
            upload_token=upload_token,
            part_numbers=part_numbers,
            request_options=request_options,
        )
        return _response.data

    async def complete_table_import_upload(
        self,
        import_id: str,
        *,
        workspace_id: str,
        upload_token: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2CompleteTableImportUploadResponse:
        """
        Verify or assemble uploaded CSV bytes and start processing under the same import ID. Requires an import awaiting upload completion; other states return `409`. Unknown or purged imports return `404`.

        OAuth scope: `api:write`.

        Parameters
        ----------
        import_id : str
            Unique table-import identifier.

        workspace_id : str
            Workspace that owns the transfer resource.

        upload_token : str
            Signed upload control token returned when the upload session was created.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2CompleteTableImportUploadResponse
            The table import after upload completion.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.complete_table_import_upload(
                import_id="importId",
                upload_token="upload-token",
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.complete_table_import_upload(
            import_id, workspace_id=workspace_id, upload_token=upload_token, request_options=request_options
        )
        return _response.data

    async def create_table_export(
        self,
        table_id: str,
        *,
        workspace_id: str,
        format: typing.Optional[CreateTableExportRequestFormat] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2CreateTableExportResponse:
        """
        Create a CSV or JSON export. Exports of small tables finish during the request; larger exports run asynchronously.

        OAuth scope: `api:write`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        workspace_id : str
            Unique workspace identifier.

        format : typing.Optional[CreateTableExportRequestFormat]
            Export file format.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2CreateTableExportResponse
            The created table export.

        Examples
        --------
        import asyncio

        from fern.tables import CreateTableExportRequestFormat

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.create_table_export(
                table_id="tableId",
                workspace_id="a91c4b2e-6d3f-4e8a-b5c7-0d9e2f1a8c64",
                format=CreateTableExportRequestFormat.CSV,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_table_export(
            table_id, workspace_id=workspace_id, format=format, request_options=request_options
        )
        return _response.data

    async def get_table_export(
        self,
        table_id: str,
        export_id: str,
        *,
        workspace_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2TableExportResponse:
        """
        Get a table export's progress and status.

        OAuth scope: `api:read`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        export_id : str
            Unique table-export identifier.

        workspace_id : str
            Workspace that owns the transfer resource.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2TableExportResponse
            The requested table export.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.get_table_export(
                table_id="tableId",
                export_id="exportId",
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_table_export(
            table_id, export_id, workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    async def cancel_table_export(
        self,
        table_id: str,
        export_id: str,
        *,
        workspace_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2CancelTableExportResponse:
        """
        Cancel an export that is still in progress.

        OAuth scope: `api:write`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        export_id : str
            Unique table-export identifier.

        workspace_id : str
            Workspace that owns the transfer resource.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2CancelTableExportResponse
            The canceled table export.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.cancel_table_export(
                table_id="tableId",
                export_id="exportId",
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cancel_table_export(
            table_id, export_id, workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    async def download_table_export(
        self,
        table_id: str,
        export_id: str,
        *,
        workspace_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2DownloadTableExportResponse:
        """
        Get a short-lived signed download URL for a completed export. Other states return `409`; an unavailable export file returns `404`.

        OAuth scope: `api:read`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        export_id : str
            Unique table-export identifier.

        workspace_id : str
            Workspace that owns the transfer resource.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2DownloadTableExportResponse
            Signed table-export download information.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.download_table_export(
                table_id="tableId",
                export_id="exportId",
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.download_table_export(
            table_id, export_id, workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    async def cancel_table_runs(
        self,
        table_id: str,
        *,
        workspace_id: str,
        scope: CancelTableRunsRequestScope,
        row_id: typing.Optional[str] = OMIT,
        filter: typing.Optional[TablePredicate] = OMIT,
        exclude_row_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2CancelTableRunsResponse:
        """
        Stop in-flight and pending workflow or enrichment cell runs across the table or one selected row.

        OAuth scope: `api:write`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        workspace_id : str
            Unique workspace identifier.

        scope : CancelTableRunsRequestScope
            Whether to cancel across the table or one row.

        row_id : typing.Optional[str]
            Row whose runs should be canceled for row scope.

        filter : typing.Optional[TablePredicate]

        exclude_row_ids : typing.Optional[typing.Sequence[str]]
            Rows excluded from an all-scope cancellation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2CancelTableRunsResponse
            The number of canceled cell runs.

        Examples
        --------
        import asyncio

        from fern.tables import CancelTableRunsRequestScope

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.cancel_table_runs(
                table_id="tableId",
                workspace_id="a91c4b2e-6d3f-4e8a-b5c7-0d9e2f1a8c64",
                scope=CancelTableRunsRequestScope.ROW,
                row_id="row_1f3e5d7c9b8a4c2d806e4a6b8d0f2e93",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cancel_table_runs(
            table_id,
            workspace_id=workspace_id,
            scope=scope,
            row_id=row_id,
            filter=filter,
            exclude_row_ids=exclude_row_ids,
            request_options=request_options,
        )
        return _response.data

    async def list_tables_folders(
        self,
        *,
        workspace_id: str,
        parent_path: typing.Optional[FolderPathInput] = None,
        search: typing.Optional[str] = None,
        sort_by: typing.Optional[ListTablesFoldersRequestSortBy] = None,
        sort_order: typing.Optional[ListTablesFoldersRequestSortOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2TableFolderListResponse:
        """
        List table folders, optionally limiting results to direct children of a parent path. Returns the complete set in one page; `nextCursor` is always null.

        OAuth scope: `api:read`.

        Parameters
        ----------
        workspace_id : str
            Workspace whose folders should be listed.

        parent_path : typing.Optional[FolderPathInput]
            Restrict results to direct children of this parent path. Unknown folder paths contribute no matches.

        search : typing.Optional[str]
            Case-insensitive substring match against the folder name.

        sort_by : typing.Optional[ListTablesFoldersRequestSortBy]
            Field used to sort the result. Sorting by `name` is case-sensitive and follows the storage collation, so do not rely on a case-insensitive order.

        sort_order : typing.Optional[ListTablesFoldersRequestSortOrder]
            Sort direction.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2TableFolderListResponse
            The table folders.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.list_tables_folders(
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_tables_folders(
            workspace_id=workspace_id,
            parent_path=parent_path,
            search=search,
            sort_by=sort_by,
            sort_order=sort_order,
            request_options=request_options,
        )
        return _response.data

    async def create_tables_folder(
        self,
        *,
        workspace_id: str,
        path: NonRootFolderPathInput,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2CreateTableFolderResponse:
        """
        Create one table-folder leaf whose parent path already exists.

        OAuth scope: `api:write`.

        Parameters
        ----------
        workspace_id : str
            Workspace in which to create the folder.

        path : NonRootFolderPathInput
            Path of the folder to create.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2CreateTableFolderResponse
            The created table folder.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.create_tables_folder(
                workspace_id="workspaceId",
                path="path",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_tables_folder(
            workspace_id=workspace_id, path=path, request_options=request_options
        )
        return _response.data

    async def delete_tables_folder(
        self,
        *,
        workspace_id: str,
        path: NonRootFolderPathInput,
        recursive: typing.Optional[DeleteTablesFolderRequestRecursive] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2DeleteTableFolderResponse:
        """
        Archive an empty folder, or set `recursive=true` to archive its tables and subfolders. Use Restore Folder to recover the archived contents.

        OAuth scope: `api:write`.

        Parameters
        ----------
        workspace_id : str
            Workspace containing the folder.

        path : NonRootFolderPathInput
            Path of the folder to delete.

        recursive : typing.Optional[DeleteTablesFolderRequestRecursive]
            Delete the folder's nested files and folders too. An empty folder deletes either way; a non-empty one needs this. The listed spellings are the whole accepted vocabulary and are case-sensitive; any other value is rejected.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2DeleteTableFolderResponse
            Table-folder deletion acknowledgement.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.delete_tables_folder(
                workspace_id="workspaceId",
                path="path",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_tables_folder(
            workspace_id=workspace_id, path=path, recursive=recursive, request_options=request_options
        )
        return _response.data

    async def relocate_tables_folder(
        self,
        *,
        workspace_id: str,
        path: NonRootFolderPathInput,
        destination_path: NonRootFolderPathInput,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2RelocateTableFolderResponse:
        """
        Rename or move a table folder and update all descendant paths.

        OAuth scope: `api:write`.

        Parameters
        ----------
        workspace_id : str
            Workspace containing the folder.

        path : NonRootFolderPathInput
            Current folder path.

        destination_path : NonRootFolderPathInput
            New full path for the folder and its descendants.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2RelocateTableFolderResponse
            The relocated table folder.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.relocate_tables_folder(
                workspace_id="workspaceId",
                path="path",
                destination_path="destinationPath",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.relocate_tables_folder(
            workspace_id=workspace_id, path=path, destination_path=destination_path, request_options=request_options
        )
        return _response.data

    async def restore_tables_folder(
        self,
        *,
        workspace_id: str,
        path: NonRootFolderPathInput,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2RestoreTableFolderResponse:
        """
        Restore an archived table folder, its descendants, and tables using its former path. An archived parent moves it to the root; name conflicts may change the returned `path`. Non-archived paths return `404`. Save the path from Delete Folder, because List Folders does not include archived table folders.

        OAuth scope: `api:write`.

        Parameters
        ----------
        workspace_id : str
            Workspace that owns the archived folder.

        path : NonRootFolderPathInput
            Path the folder held when a folder delete archived it.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2RestoreTableFolderResponse
            The restored table folder and what it brought back.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.restore_tables_folder(
                workspace_id="workspaceId",
                path="path",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.restore_tables_folder(
            workspace_id=workspace_id, path=path, request_options=request_options
        )
        return _response.data

    async def restore_table(
        self, table_id: str, *, workspace_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> V2RestoreTableResponse:
        """
        Restore a table and its archived rows, views, and workflow groups. Active tables return unchanged without a new audit event. Name conflicts may change the returned `name`. Find archived tables with List Tables and `scope=archived`.

        OAuth scope: `api:write`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        workspace_id : str
            Unique workspace identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2RestoreTableResponse
            The restored table.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.restore_table(
                table_id="tableId",
                workspace_id="a91c4b2e-6d3f-4e8a-b5c7-0d9e2f1a8c64",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.restore_table(
            table_id, workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    async def bulk_update_table_rows(
        self,
        table_id: str,
        *,
        workspace_id: str,
        updates: typing.Sequence[BulkUpdateTableRowsRequestUpdatesItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2BulkUpdateTableRowsResponse:
        """
        Apply separate partial patches to up to 1,000 rows, preserving omitted columns. A row outside the table rejects the entire request with `400` and lists missing IDs. Use Update Rows by Filter to apply one patch to every matching row.

        OAuth scope: `api:write`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        workspace_id : str
            Workspace that owns the table.

        updates : typing.Sequence[BulkUpdateTableRowsRequestUpdatesItem]
            One merge patch per row. Each row identifier may appear at most once.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2BulkUpdateTableRowsResponse
            The bulk update result.

        Examples
        --------
        import asyncio

        from fern.tables import BulkUpdateTableRowsRequestUpdatesItem

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.bulk_update_table_rows(
                table_id="tableId",
                workspace_id="a91c4b2e-6d3f-4e8a-b5c7-0d9e2f1a8c64",
                updates=[
                    BulkUpdateTableRowsRequestUpdatesItem(
                        row_id="row_1f3e5d7c9b8a4c2d806e4a6b8d0f2e93",
                        data={"status": "active"},
                    ),
                    BulkUpdateTableRowsRequestUpdatesItem(
                        row_id="row_2b4d6f8a0c1e3759b8d0f2a4c6e80193",
                        data={"status": "churned"},
                    ),
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.bulk_update_table_rows(
            table_id, workspace_id=workspace_id, updates=updates, request_options=request_options
        )
        return _response.data

    async def get_table_dispatch(
        self,
        table_id: str,
        dispatch_id: str,
        *,
        workspace_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2TableRunDispatchResponse:
        """
        Get a dispatch's current state. Poll until `complete` or `canceled`; use row reads with `includeRunState` for per-cell outcomes.

        OAuth scope: `api:read`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        dispatch_id : str
            Unique table run-dispatch identifier.

        workspace_id : str
            Workspace that owns the transfer resource.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2TableRunDispatchResponse
            The requested run dispatch.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.get_table_dispatch(
                table_id="tableId",
                dispatch_id="dispatchId",
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_table_dispatch(
            table_id, dispatch_id, workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    async def cancel_table_dispatch(
        self,
        table_id: str,
        dispatch_id: str,
        *,
        workspace_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2CancelTableDispatchResponse:
        """
        Stop a dispatch from scheduling more cells. Already queued or running cells continue; use Cancel Column Runs to stop them. Completed or canceled dispatches return unchanged.

        OAuth scope: `api:write`.

        Parameters
        ----------
        table_id : str
            Unique table identifier.

        dispatch_id : str
            Unique table run-dispatch identifier.

        workspace_id : str
            Workspace that owns the transfer resource.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2CancelTableDispatchResponse
            The dispatch in its post-cancellation state.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.cancel_table_dispatch(
                table_id="tableId",
                dispatch_id="dispatchId",
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cancel_table_dispatch(
            table_id, dispatch_id, workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    async def move_tables(
        self,
        *,
        workspace_id: str,
        table_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        folder_paths: typing.Optional[typing.Sequence[FolderPathInput]] = OMIT,
        target_folder_path: typing.Optional[FolderPathInput] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2MoveTablesResponse:
        """
        Move up to 100 tables and folders to one destination. Items succeed or fail independently: covered tables are `skipped`, missing items are `notFound`, and lock or cycle failures include reasons in `failed`. An invalid destination rejects the request before any move.

        OAuth scope: `api:write`.

        Parameters
        ----------
        workspace_id : str
            Workspace that owns every selected item.

        table_ids : typing.Optional[typing.Sequence[str]]
            Tables to move, by identifier.

        folder_paths : typing.Optional[typing.Sequence[FolderPathInput]]
            Table folders to re-parent, by canonical path.

        target_folder_path : typing.Optional[FolderPathInput]
            Destination folder path. Omit to move the selection to the workspace root.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2MoveTablesResponse
            Per-item outcome of the bulk move.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.move_tables(
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.move_tables(
            workspace_id=workspace_id,
            table_ids=table_ids,
            folder_paths=folder_paths,
            target_folder_path=target_folder_path,
            request_options=request_options,
        )
        return _response.data

    async def bulk_delete_tables(
        self,
        *,
        workspace_id: str,
        table_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        folder_paths: typing.Optional[typing.Sequence[FolderPathInput]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2BulkDeleteTablesResponse:
        """
        Archive up to 100 selected tables and folders, including folder contents. Items succeed or fail independently, with `skipped`, `notFound`, and `failed` outcomes. `deletedItems` includes all descendants. Use Restore Table or Restore Folder to recover archived items.

        OAuth scope: `api:write`.

        Parameters
        ----------
        workspace_id : str
            Workspace that owns every selected item.

        table_ids : typing.Optional[typing.Sequence[str]]
            Tables to archive, by identifier.

        folder_paths : typing.Optional[typing.Sequence[FolderPathInput]]
            Table folders to delete, by canonical path. Each cascades to everything inside it.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2BulkDeleteTablesResponse
            Per-item outcome of the bulk delete.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.bulk_delete_tables(
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.bulk_delete_tables(
            workspace_id=workspace_id, table_ids=table_ids, folder_paths=folder_paths, request_options=request_options
        )
        return _response.data
