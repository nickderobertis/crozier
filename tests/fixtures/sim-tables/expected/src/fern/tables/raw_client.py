

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.conflict_error import ConflictError
from ..errors.content_too_large_error import ContentTooLargeError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.locked_error import LockedError
from ..errors.not_found_error import NotFoundError
from ..errors.service_unavailable_error import ServiceUnavailableError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unsupported_media_type_error import UnsupportedMediaTypeError
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
from ..types.v2error import V2Error
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
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawTablesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> HttpResponse[V2TableListResponse]:
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
        HttpResponse[V2TableListResponse]
            A page of tables in the workspace.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/tables",
            method="GET",
            params={
                "workspaceId": workspace_id,
                "scope": scope,
                "folderPath": folder_path,
                "search": search,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "limit": limit,
                "cursor": cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2TableListResponse,
                    parse_obj_as(
                        type_=V2TableListResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_table(
        self,
        *,
        name: str,
        workspace_id: str,
        schema: CreateTableRequestSchema,
        description: typing.Optional[str] = OMIT,
        folder_path: typing.Optional[FolderPathInput] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V2CreateTableResponse]:
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
        HttpResponse[V2CreateTableResponse]
            The created table.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/tables",
            method="POST",
            json={
                "name": name,
                "description": description,
                "workspaceId": workspace_id,
                "schema": convert_and_respect_annotation_metadata(
                    object_=schema, annotation=CreateTableRequestSchema, direction="write"
                ),
                "folderPath": folder_path,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2CreateTableResponse,
                    parse_obj_as(
                        type_=V2CreateTableResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_table(
        self, table_id: str, *, workspace_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[V2TableResponse]:
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
        HttpResponse[V2TableResponse]
            The requested table.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}",
            method="GET",
            params={
                "workspaceId": workspace_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2TableResponse,
                    parse_obj_as(
                        type_=V2TableResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_table(
        self, table_id: str, *, workspace_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[V2DeleteTableResponse]:
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
        HttpResponse[V2DeleteTableResponse]
            Table deletion acknowledgement.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}",
            method="DELETE",
            params={
                "workspaceId": workspace_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2DeleteTableResponse,
                    parse_obj_as(
                        type_=V2DeleteTableResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 423:
                raise LockedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_table(
        self,
        table_id: str,
        *,
        workspace_id: str,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        folder_path: typing.Optional[FolderPathInput] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V2UpdateTableResponse]:
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
        HttpResponse[V2UpdateTableResponse]
            The updated table.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}",
            method="PATCH",
            json={
                "workspaceId": workspace_id,
                "name": name,
                "description": description,
                "folderPath": folder_path,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2UpdateTableResponse,
                    parse_obj_as(
                        type_=V2UpdateTableResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def add_table_column(
        self,
        table_id: str,
        *,
        workspace_id: str,
        column: AddTableColumnRequestColumn,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V2TableColumnsResponse]:
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
        HttpResponse[V2TableColumnsResponse]
            The updated table columns.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/columns",
            method="POST",
            json={
                "workspaceId": workspace_id,
                "column": convert_and_respect_annotation_metadata(
                    object_=column, annotation=AddTableColumnRequestColumn, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2TableColumnsResponse,
                    parse_obj_as(
                        type_=V2TableColumnsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 423:
                raise LockedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_table_column(
        self,
        table_id: str,
        *,
        workspace_id: str,
        column_name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V2TableColumnsResponse]:
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
        HttpResponse[V2TableColumnsResponse]
            The surviving table columns.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/columns",
            method="DELETE",
            json={
                "workspaceId": workspace_id,
                "columnName": column_name,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2TableColumnsResponse,
                    parse_obj_as(
                        type_=V2TableColumnsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 423:
                raise LockedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_table_column(
        self,
        table_id: str,
        *,
        workspace_id: str,
        column_name: str,
        updates: UpdateTableColumnRequestUpdates,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V2TableColumnsResponse]:
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
        HttpResponse[V2TableColumnsResponse]
            The updated table columns.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/columns",
            method="PATCH",
            json={
                "workspaceId": workspace_id,
                "columnName": column_name,
                "updates": convert_and_respect_annotation_metadata(
                    object_=updates, annotation=UpdateTableColumnRequestUpdates, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2TableColumnsResponse,
                    parse_obj_as(
                        type_=V2TableColumnsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 423:
                raise LockedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_table_rows(
        self,
        table_id: str,
        *,
        workspace_id: str,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        include_run_state: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V2TableRowListResponse]:
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
        HttpResponse[V2TableRowListResponse]
            A page of table rows.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/rows",
            method="GET",
            params={
                "workspaceId": workspace_id,
                "limit": limit,
                "cursor": cursor,
                "includeRunState": include_run_state,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2TableRowListResponse,
                    parse_obj_as(
                        type_=V2TableRowListResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_table_rows(
        self, table_id: str, *, request: CreateTableRowsRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[V2CreateTableRowsResponse]:
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
        HttpResponse[V2CreateTableRowsResponse]
            The inserted row or rows.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/rows",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=CreateTableRowsRequest, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2CreateTableRowsResponse,
                    parse_obj_as(
                        type_=V2CreateTableRowsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 423:
                raise LockedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_table_rows(
        self,
        table_id: str,
        *,
        workspace_id: str,
        filter: typing.Optional[TablePredicate] = OMIT,
        limit: typing.Optional[int] = OMIT,
        row_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V2DeleteTableRowsResponse]:
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
        HttpResponse[V2DeleteTableRowsResponse]
            The bulk deletion result.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/rows",
            method="DELETE",
            json={
                "workspaceId": workspace_id,
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=TablePredicate, direction="write"
                ),
                "limit": limit,
                "rowIds": row_ids,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2DeleteTableRowsResponse,
                    parse_obj_as(
                        type_=V2DeleteTableRowsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 423:
                raise LockedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_table_rows(
        self,
        table_id: str,
        *,
        workspace_id: str,
        filter: TablePredicate,
        data: V2TableRowData,
        limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V2UpdateTableRowsResponse]:
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
        HttpResponse[V2UpdateTableRowsResponse]
            The bulk update result.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/rows",
            method="PATCH",
            json={
                "workspaceId": workspace_id,
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=TablePredicate, direction="write"
                ),
                "data": data,
                "limit": limit,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2UpdateTableRowsResponse,
                    parse_obj_as(
                        type_=V2UpdateTableRowsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 423:
                raise LockedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_table_row(
        self,
        table_id: str,
        row_id: str,
        *,
        workspace_id: str,
        include_run_state: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V2TableRowResponse]:
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
        HttpResponse[V2TableRowResponse]
            The requested table row.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/rows/{encode_path_param(row_id)}",
            method="GET",
            params={
                "workspaceId": workspace_id,
                "includeRunState": include_run_state,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2TableRowResponse,
                    parse_obj_as(
                        type_=V2TableRowResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_table_row(
        self, table_id: str, row_id: str, *, workspace_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[V2DeleteTableRowResponse]:
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
        HttpResponse[V2DeleteTableRowResponse]
            The row deletion result.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/rows/{encode_path_param(row_id)}",
            method="DELETE",
            params={
                "workspaceId": workspace_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2DeleteTableRowResponse,
                    parse_obj_as(
                        type_=V2DeleteTableRowResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 423:
                raise LockedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_table_row(
        self,
        table_id: str,
        row_id: str,
        *,
        workspace_id: str,
        data: V2TableRowData,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V2TableRowResponse]:
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
        HttpResponse[V2TableRowResponse]
            The updated table row.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/rows/{encode_path_param(row_id)}",
            method="PATCH",
            json={
                "workspaceId": workspace_id,
                "data": data,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2TableRowResponse,
                    parse_obj_as(
                        type_=V2TableRowResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 423:
                raise LockedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def upsert_table_row(
        self,
        table_id: str,
        *,
        workspace_id: str,
        data: V2TableRowData,
        conflict_target: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V2UpsertTableRowResponse]:
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
        HttpResponse[V2UpsertTableRowResponse]
            The upserted row and operation performed.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/rows/upsert",
            method="POST",
            json={
                "workspaceId": workspace_id,
                "data": data,
                "conflictTarget": conflict_target,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2UpsertTableRowResponse,
                    parse_obj_as(
                        type_=V2UpsertTableRowResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 423:
                raise LockedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[V2QueryTableRowsResponse]:
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
        HttpResponse[V2QueryTableRowsResponse]
            A page of matching table rows.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/query",
            method="POST",
            json={
                "workspaceId": workspace_id,
                "predicate": convert_and_respect_annotation_metadata(
                    object_=predicate, annotation=TablePredicateInput, direction="write"
                ),
                "sort": convert_and_respect_annotation_metadata(
                    object_=sort, annotation=typing.Sequence[QueryTableRowsRequestSortItem], direction="write"
                ),
                "limit": limit,
                "cursor": cursor,
                "includeRunState": include_run_state,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2QueryTableRowsResponse,
                    parse_obj_as(
                        type_=V2QueryTableRowsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def count_table_rows(
        self,
        table_id: str,
        *,
        workspace_id: str,
        predicate: typing.Optional[TablePredicateInput] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V2CountTableRowsResponse]:
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
        HttpResponse[V2CountTableRowsResponse]
            The number of matching table rows.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/query/count",
            method="POST",
            json={
                "workspaceId": workspace_id,
                "predicate": convert_and_respect_annotation_metadata(
                    object_=predicate, annotation=TablePredicateInput, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2CountTableRowsResponse,
                    parse_obj_as(
                        type_=V2CountTableRowsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_table_views(
        self, table_id: str, *, workspace_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[V2TableViewListResponse]:
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
        HttpResponse[V2TableViewListResponse]
            The saved table views.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/views",
            method="GET",
            params={
                "workspaceId": workspace_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2TableViewListResponse,
                    parse_obj_as(
                        type_=V2TableViewListResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_table_view(
        self,
        table_id: str,
        *,
        workspace_id: str,
        name: str,
        config: CreateTableViewRequestConfig,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V2CreateTableViewResponse]:
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
        HttpResponse[V2CreateTableViewResponse]
            The created table view.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/views",
            method="POST",
            json={
                "workspaceId": workspace_id,
                "name": name,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=CreateTableViewRequestConfig, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2CreateTableViewResponse,
                    parse_obj_as(
                        type_=V2CreateTableViewResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_table_view(
        self, table_id: str, view_id: str, *, workspace_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[V2TableViewResponse]:
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
        HttpResponse[V2TableViewResponse]
            The requested table view.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/views/{encode_path_param(view_id)}",
            method="GET",
            params={
                "workspaceId": workspace_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2TableViewResponse,
                    parse_obj_as(
                        type_=V2TableViewResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_table_view(
        self, table_id: str, view_id: str, *, workspace_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[V2DeleteTableViewResponse]:
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
        HttpResponse[V2DeleteTableViewResponse]
            Table view deletion acknowledgement.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/views/{encode_path_param(view_id)}",
            method="DELETE",
            params={
                "workspaceId": workspace_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2DeleteTableViewResponse,
                    parse_obj_as(
                        type_=V2DeleteTableViewResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[V2TableViewResponse]:
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
        HttpResponse[V2TableViewResponse]
            The updated table view.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/views/{encode_path_param(view_id)}",
            method="PATCH",
            json={
                "workspaceId": workspace_id,
                "name": name,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=UpdateTableViewRequestConfig, direction="write"
                ),
                "configPatch": convert_and_respect_annotation_metadata(
                    object_=config_patch, annotation=UpdateTableViewRequestConfigPatch, direction="write"
                ),
                "isDefault": is_default,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2TableViewResponse,
                    parse_obj_as(
                        type_=V2TableViewResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_table_workflow_groups(
        self, table_id: str, *, workspace_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[V2TableWorkflowGroupListResponse]:
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
        HttpResponse[V2TableWorkflowGroupListResponse]
            The table workflow groups.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/groups",
            method="GET",
            params={
                "workspaceId": workspace_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2TableWorkflowGroupListResponse,
                    parse_obj_as(
                        type_=V2TableWorkflowGroupListResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def add_table_workflow_group(
        self,
        table_id: str,
        *,
        workspace_id: str,
        group: AddTableWorkflowGroupRequestGroup,
        output_columns: typing.Sequence[AddTableWorkflowGroupRequestOutputColumnsItem],
        auto_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V2AddTableWorkflowGroupResponse]:
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
        HttpResponse[V2AddTableWorkflowGroupResponse]
            The created workflow group and resulting columns.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/groups",
            method="POST",
            json={
                "workspaceId": workspace_id,
                "group": convert_and_respect_annotation_metadata(
                    object_=group, annotation=AddTableWorkflowGroupRequestGroup, direction="write"
                ),
                "outputColumns": convert_and_respect_annotation_metadata(
                    object_=output_columns,
                    annotation=typing.Sequence[AddTableWorkflowGroupRequestOutputColumnsItem],
                    direction="write",
                ),
                "autoRun": auto_run,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2AddTableWorkflowGroupResponse,
                    parse_obj_as(
                        type_=V2AddTableWorkflowGroupResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 423:
                raise LockedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_table_workflow_group(
        self,
        table_id: str,
        *,
        workspace_id: str,
        group_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V2DeleteTableWorkflowGroupResponse]:
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
        HttpResponse[V2DeleteTableWorkflowGroupResponse]
            Workflow-group deletion acknowledgement and surviving columns.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/groups",
            method="DELETE",
            json={
                "workspaceId": workspace_id,
                "groupId": group_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2DeleteTableWorkflowGroupResponse,
                    parse_obj_as(
                        type_=V2DeleteTableWorkflowGroupResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 423:
                raise LockedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[V2UpdateTableWorkflowGroupResponse]:
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
        HttpResponse[V2UpdateTableWorkflowGroupResponse]
            The updated workflow group and resulting columns.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/groups",
            method="PATCH",
            json={
                "workspaceId": workspace_id,
                "groupId": group_id,
                "workflowId": workflow_id,
                "name": name,
                "dependencies": convert_and_respect_annotation_metadata(
                    object_=dependencies, annotation=UpdateTableWorkflowGroupRequestDependencies, direction="write"
                ),
                "outputs": convert_and_respect_annotation_metadata(
                    object_=outputs,
                    annotation=typing.Sequence[UpdateTableWorkflowGroupRequestOutputsItem],
                    direction="write",
                ),
                "newOutputColumns": convert_and_respect_annotation_metadata(
                    object_=new_output_columns,
                    annotation=typing.Sequence[UpdateTableWorkflowGroupRequestNewOutputColumnsItem],
                    direction="write",
                ),
                "mappingUpdates": convert_and_respect_annotation_metadata(
                    object_=mapping_updates,
                    annotation=typing.Sequence[UpdateTableWorkflowGroupRequestMappingUpdatesItem],
                    direction="write",
                ),
                "inputMappings": convert_and_respect_annotation_metadata(
                    object_=input_mappings,
                    annotation=typing.Sequence[UpdateTableWorkflowGroupRequestInputMappingsItem],
                    direction="write",
                ),
                "deploymentMode": deployment_mode,
                "type": type,
                "autoRun": auto_run,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2UpdateTableWorkflowGroupResponse,
                    parse_obj_as(
                        type_=V2UpdateTableWorkflowGroupResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 423:
                raise LockedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_table_dispatches(
        self, table_id: str, *, workspace_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[V2TableRunDispatchListResponse]:
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
        HttpResponse[V2TableRunDispatchListResponse]
            The table's active run dispatches.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/dispatches",
            method="GET",
            params={
                "workspaceId": workspace_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2TableRunDispatchListResponse,
                    parse_obj_as(
                        type_=V2TableRunDispatchListResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[V2CreateTableDispatchResponse]:
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
        HttpResponse[V2CreateTableDispatchResponse]
            The accepted run dispatch.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/dispatches",
            method="POST",
            json={
                "workspaceId": workspace_id,
                "groupIds": group_ids,
                "runMode": run_mode,
                "rowIds": row_ids,
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=TablePredicate, direction="write"
                ),
                "excludeRowIds": exclude_row_ids,
                "limit": convert_and_respect_annotation_metadata(
                    object_=limit, annotation=CreateTableDispatchRequestLimit, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2CreateTableDispatchResponse,
                    parse_obj_as(
                        type_=V2CreateTableDispatchResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_row_enrichment(
        self,
        table_id: str,
        row_id: str,
        group_id: str,
        *,
        workspace_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V2RowEnrichmentResponse]:
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
        HttpResponse[V2RowEnrichmentResponse]
            The enrichment run detail, or null when none was recorded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/rows/{encode_path_param(row_id)}/enrichment/{encode_path_param(group_id)}",
            method="GET",
            params={
                "workspaceId": workspace_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2RowEnrichmentResponse,
                    parse_obj_as(
                        type_=V2RowEnrichmentResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def run_row_enrichment(
        self,
        table_id: str,
        row_id: str,
        group_id: str,
        *,
        workspace_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V2RunRowEnrichmentResponse]:
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
        HttpResponse[V2RunRowEnrichmentResponse]
            The accepted row enrichment dispatch.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/rows/{encode_path_param(row_id)}/enrichment/{encode_path_param(group_id)}",
            method="POST",
            json={
                "workspaceId": workspace_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2RunRowEnrichmentResponse,
                    parse_obj_as(
                        type_=V2RunRowEnrichmentResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def search_table_rows(
        self,
        table_id: str,
        *,
        workspace_id: str,
        q: str,
        predicate: typing.Optional[TablePredicate] = OMIT,
        sort: typing.Optional[typing.Sequence[SearchTableRowsRequestSortItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V2SearchTableRowsResponse]:
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
        HttpResponse[V2SearchTableRowsResponse]
            The matching table cells.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/rows/search",
            method="POST",
            json={
                "workspaceId": workspace_id,
                "q": q,
                "predicate": convert_and_respect_annotation_metadata(
                    object_=predicate, annotation=TablePredicate, direction="write"
                ),
                "sort": convert_and_respect_annotation_metadata(
                    object_=sort, annotation=typing.Sequence[SearchTableRowsRequestSortItem], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2SearchTableRowsResponse,
                    parse_obj_as(
                        type_=V2SearchTableRowsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[V2CreateTableImportResponse]:
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
        HttpResponse[V2CreateTableImportResponse]
            The created table import and optional transfer instructions.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/tables/imports",
            method="POST",
            json={
                "workspaceId": workspace_id,
                "source": convert_and_respect_annotation_metadata(
                    object_=source, annotation=CreateTableImportRequestSource, direction="write"
                ),
                "target": convert_and_respect_annotation_metadata(
                    object_=target, annotation=CreateTableImportRequestTarget, direction="write"
                ),
                "mapping": mapping,
                "createColumns": create_columns,
                "timezone": timezone,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2CreateTableImportResponse,
                    parse_obj_as(
                        type_=V2CreateTableImportResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 423:
                raise LockedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_table_import(
        self,
        import_id: str,
        *,
        workspace_id: str,
        upload_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V2TableImportResponse]:
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
        HttpResponse[V2TableImportResponse]
            The requested table import.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/tables/imports/{encode_path_param(import_id)}",
            method="GET",
            params={
                "workspaceId": workspace_id,
            },
            headers={
                "upload-token": str(upload_token) if upload_token is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2TableImportResponse,
                    parse_obj_as(
                        type_=V2TableImportResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def cancel_table_import(
        self,
        import_id: str,
        *,
        workspace_id: str,
        upload_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V2CancelTableImportResponse]:
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
        HttpResponse[V2CancelTableImportResponse]
            The canceled table import.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/tables/imports/{encode_path_param(import_id)}",
            method="DELETE",
            params={
                "workspaceId": workspace_id,
            },
            headers={
                "upload-token": str(upload_token) if upload_token is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2CancelTableImportResponse,
                    parse_obj_as(
                        type_=V2CancelTableImportResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_table_import_part_urls(
        self,
        import_id: str,
        *,
        workspace_id: str,
        upload_token: str,
        part_numbers: typing.Sequence[int],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V2CreateTableImportPartUrlsResponse]:
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
        HttpResponse[V2CreateTableImportPartUrlsResponse]
            The signed multipart upload URLs.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/tables/imports/{encode_path_param(import_id)}/parts",
            method="POST",
            params={
                "workspaceId": workspace_id,
            },
            json={
                "partNumbers": part_numbers,
            },
            headers={
                "content-type": "application/json",
                "upload-token": str(upload_token) if upload_token is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2CreateTableImportPartUrlsResponse,
                    parse_obj_as(
                        type_=V2CreateTableImportPartUrlsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def complete_table_import_upload(
        self,
        import_id: str,
        *,
        workspace_id: str,
        upload_token: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V2CompleteTableImportUploadResponse]:
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
        HttpResponse[V2CompleteTableImportUploadResponse]
            The table import after upload completion.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/tables/imports/{encode_path_param(import_id)}/complete",
            method="POST",
            params={
                "workspaceId": workspace_id,
            },
            headers={
                "upload-token": str(upload_token) if upload_token is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2CompleteTableImportUploadResponse,
                    parse_obj_as(
                        type_=V2CompleteTableImportUploadResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 423:
                raise LockedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_table_export(
        self,
        table_id: str,
        *,
        workspace_id: str,
        format: typing.Optional[CreateTableExportRequestFormat] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V2CreateTableExportResponse]:
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
        HttpResponse[V2CreateTableExportResponse]
            The created table export.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/exports",
            method="POST",
            json={
                "workspaceId": workspace_id,
                "format": format,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2CreateTableExportResponse,
                    parse_obj_as(
                        type_=V2CreateTableExportResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_table_export(
        self,
        table_id: str,
        export_id: str,
        *,
        workspace_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V2TableExportResponse]:
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
        HttpResponse[V2TableExportResponse]
            The requested table export.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/exports/{encode_path_param(export_id)}",
            method="GET",
            params={
                "workspaceId": workspace_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2TableExportResponse,
                    parse_obj_as(
                        type_=V2TableExportResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def cancel_table_export(
        self,
        table_id: str,
        export_id: str,
        *,
        workspace_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V2CancelTableExportResponse]:
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
        HttpResponse[V2CancelTableExportResponse]
            The canceled table export.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/exports/{encode_path_param(export_id)}",
            method="DELETE",
            params={
                "workspaceId": workspace_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2CancelTableExportResponse,
                    parse_obj_as(
                        type_=V2CancelTableExportResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def download_table_export(
        self,
        table_id: str,
        export_id: str,
        *,
        workspace_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V2DownloadTableExportResponse]:
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
        HttpResponse[V2DownloadTableExportResponse]
            Signed table-export download information.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/exports/{encode_path_param(export_id)}/download",
            method="GET",
            params={
                "workspaceId": workspace_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2DownloadTableExportResponse,
                    parse_obj_as(
                        type_=V2DownloadTableExportResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[V2CancelTableRunsResponse]:
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
        HttpResponse[V2CancelTableRunsResponse]
            The number of canceled cell runs.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/cancel-runs",
            method="POST",
            json={
                "workspaceId": workspace_id,
                "scope": scope,
                "rowId": row_id,
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=TablePredicate, direction="write"
                ),
                "excludeRowIds": exclude_row_ids,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2CancelTableRunsResponse,
                    parse_obj_as(
                        type_=V2CancelTableRunsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_tables_folders(
        self,
        *,
        workspace_id: str,
        parent_path: typing.Optional[FolderPathInput] = None,
        search: typing.Optional[str] = None,
        sort_by: typing.Optional[ListTablesFoldersRequestSortBy] = None,
        sort_order: typing.Optional[ListTablesFoldersRequestSortOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V2TableFolderListResponse]:
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
        HttpResponse[V2TableFolderListResponse]
            The table folders.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/tables/folders",
            method="GET",
            params={
                "workspaceId": workspace_id,
                "parentPath": parent_path,
                "search": search,
                "sortBy": sort_by,
                "sortOrder": sort_order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2TableFolderListResponse,
                    parse_obj_as(
                        type_=V2TableFolderListResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_tables_folder(
        self,
        *,
        workspace_id: str,
        path: NonRootFolderPathInput,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V2CreateTableFolderResponse]:
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
        HttpResponse[V2CreateTableFolderResponse]
            The created table folder.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/tables/folders",
            method="POST",
            json={
                "workspaceId": workspace_id,
                "path": path,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2CreateTableFolderResponse,
                    parse_obj_as(
                        type_=V2CreateTableFolderResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_tables_folder(
        self,
        *,
        workspace_id: str,
        path: NonRootFolderPathInput,
        recursive: typing.Optional[DeleteTablesFolderRequestRecursive] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V2DeleteTableFolderResponse]:
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
        HttpResponse[V2DeleteTableFolderResponse]
            Table-folder deletion acknowledgement.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/tables/folders",
            method="DELETE",
            params={
                "workspaceId": workspace_id,
                "path": path,
                "recursive": recursive,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2DeleteTableFolderResponse,
                    parse_obj_as(
                        type_=V2DeleteTableFolderResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 423:
                raise LockedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def relocate_tables_folder(
        self,
        *,
        workspace_id: str,
        path: NonRootFolderPathInput,
        destination_path: NonRootFolderPathInput,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V2RelocateTableFolderResponse]:
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
        HttpResponse[V2RelocateTableFolderResponse]
            The relocated table folder.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/tables/folders",
            method="PATCH",
            json={
                "workspaceId": workspace_id,
                "path": path,
                "destinationPath": destination_path,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2RelocateTableFolderResponse,
                    parse_obj_as(
                        type_=V2RelocateTableFolderResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def restore_tables_folder(
        self,
        *,
        workspace_id: str,
        path: NonRootFolderPathInput,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V2RestoreTableFolderResponse]:
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
        HttpResponse[V2RestoreTableFolderResponse]
            The restored table folder and what it brought back.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/tables/folders/restore",
            method="POST",
            json={
                "workspaceId": workspace_id,
                "path": path,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2RestoreTableFolderResponse,
                    parse_obj_as(
                        type_=V2RestoreTableFolderResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def restore_table(
        self, table_id: str, *, workspace_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[V2RestoreTableResponse]:
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
        HttpResponse[V2RestoreTableResponse]
            The restored table.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/restore",
            method="POST",
            json={
                "workspaceId": workspace_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2RestoreTableResponse,
                    parse_obj_as(
                        type_=V2RestoreTableResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def bulk_update_table_rows(
        self,
        table_id: str,
        *,
        workspace_id: str,
        updates: typing.Sequence[BulkUpdateTableRowsRequestUpdatesItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V2BulkUpdateTableRowsResponse]:
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
        HttpResponse[V2BulkUpdateTableRowsResponse]
            The bulk update result.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/rows/bulk-update",
            method="POST",
            json={
                "workspaceId": workspace_id,
                "updates": convert_and_respect_annotation_metadata(
                    object_=updates,
                    annotation=typing.Sequence[BulkUpdateTableRowsRequestUpdatesItem],
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2BulkUpdateTableRowsResponse,
                    parse_obj_as(
                        type_=V2BulkUpdateTableRowsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 423:
                raise LockedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_table_dispatch(
        self,
        table_id: str,
        dispatch_id: str,
        *,
        workspace_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V2TableRunDispatchResponse]:
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
        HttpResponse[V2TableRunDispatchResponse]
            The requested run dispatch.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/dispatches/{encode_path_param(dispatch_id)}",
            method="GET",
            params={
                "workspaceId": workspace_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2TableRunDispatchResponse,
                    parse_obj_as(
                        type_=V2TableRunDispatchResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def cancel_table_dispatch(
        self,
        table_id: str,
        dispatch_id: str,
        *,
        workspace_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V2CancelTableDispatchResponse]:
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
        HttpResponse[V2CancelTableDispatchResponse]
            The dispatch in its post-cancellation state.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/dispatches/{encode_path_param(dispatch_id)}",
            method="DELETE",
            params={
                "workspaceId": workspace_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2CancelTableDispatchResponse,
                    parse_obj_as(
                        type_=V2CancelTableDispatchResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def move_tables(
        self,
        *,
        workspace_id: str,
        table_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        folder_paths: typing.Optional[typing.Sequence[FolderPathInput]] = OMIT,
        target_folder_path: typing.Optional[FolderPathInput] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V2MoveTablesResponse]:
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
        HttpResponse[V2MoveTablesResponse]
            Per-item outcome of the bulk move.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/tables/move",
            method="POST",
            json={
                "workspaceId": workspace_id,
                "tableIds": table_ids,
                "folderPaths": folder_paths,
                "targetFolderPath": target_folder_path,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2MoveTablesResponse,
                    parse_obj_as(
                        type_=V2MoveTablesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def bulk_delete_tables(
        self,
        *,
        workspace_id: str,
        table_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        folder_paths: typing.Optional[typing.Sequence[FolderPathInput]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V2BulkDeleteTablesResponse]:
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
        HttpResponse[V2BulkDeleteTablesResponse]
            Per-item outcome of the bulk delete.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/tables/bulk-delete",
            method="POST",
            json={
                "workspaceId": workspace_id,
                "tableIds": table_ids,
                "folderPaths": folder_paths,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2BulkDeleteTablesResponse,
                    parse_obj_as(
                        type_=V2BulkDeleteTablesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 423:
                raise LockedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawTablesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> AsyncHttpResponse[V2TableListResponse]:
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
        AsyncHttpResponse[V2TableListResponse]
            A page of tables in the workspace.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/tables",
            method="GET",
            params={
                "workspaceId": workspace_id,
                "scope": scope,
                "folderPath": folder_path,
                "search": search,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "limit": limit,
                "cursor": cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2TableListResponse,
                    parse_obj_as(
                        type_=V2TableListResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_table(
        self,
        *,
        name: str,
        workspace_id: str,
        schema: CreateTableRequestSchema,
        description: typing.Optional[str] = OMIT,
        folder_path: typing.Optional[FolderPathInput] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V2CreateTableResponse]:
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
        AsyncHttpResponse[V2CreateTableResponse]
            The created table.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/tables",
            method="POST",
            json={
                "name": name,
                "description": description,
                "workspaceId": workspace_id,
                "schema": convert_and_respect_annotation_metadata(
                    object_=schema, annotation=CreateTableRequestSchema, direction="write"
                ),
                "folderPath": folder_path,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2CreateTableResponse,
                    parse_obj_as(
                        type_=V2CreateTableResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_table(
        self, table_id: str, *, workspace_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[V2TableResponse]:
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
        AsyncHttpResponse[V2TableResponse]
            The requested table.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}",
            method="GET",
            params={
                "workspaceId": workspace_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2TableResponse,
                    parse_obj_as(
                        type_=V2TableResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_table(
        self, table_id: str, *, workspace_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[V2DeleteTableResponse]:
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
        AsyncHttpResponse[V2DeleteTableResponse]
            Table deletion acknowledgement.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}",
            method="DELETE",
            params={
                "workspaceId": workspace_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2DeleteTableResponse,
                    parse_obj_as(
                        type_=V2DeleteTableResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 423:
                raise LockedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_table(
        self,
        table_id: str,
        *,
        workspace_id: str,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        folder_path: typing.Optional[FolderPathInput] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V2UpdateTableResponse]:
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
        AsyncHttpResponse[V2UpdateTableResponse]
            The updated table.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}",
            method="PATCH",
            json={
                "workspaceId": workspace_id,
                "name": name,
                "description": description,
                "folderPath": folder_path,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2UpdateTableResponse,
                    parse_obj_as(
                        type_=V2UpdateTableResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def add_table_column(
        self,
        table_id: str,
        *,
        workspace_id: str,
        column: AddTableColumnRequestColumn,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V2TableColumnsResponse]:
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
        AsyncHttpResponse[V2TableColumnsResponse]
            The updated table columns.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/columns",
            method="POST",
            json={
                "workspaceId": workspace_id,
                "column": convert_and_respect_annotation_metadata(
                    object_=column, annotation=AddTableColumnRequestColumn, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2TableColumnsResponse,
                    parse_obj_as(
                        type_=V2TableColumnsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 423:
                raise LockedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_table_column(
        self,
        table_id: str,
        *,
        workspace_id: str,
        column_name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V2TableColumnsResponse]:
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
        AsyncHttpResponse[V2TableColumnsResponse]
            The surviving table columns.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/columns",
            method="DELETE",
            json={
                "workspaceId": workspace_id,
                "columnName": column_name,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2TableColumnsResponse,
                    parse_obj_as(
                        type_=V2TableColumnsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 423:
                raise LockedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_table_column(
        self,
        table_id: str,
        *,
        workspace_id: str,
        column_name: str,
        updates: UpdateTableColumnRequestUpdates,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V2TableColumnsResponse]:
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
        AsyncHttpResponse[V2TableColumnsResponse]
            The updated table columns.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/columns",
            method="PATCH",
            json={
                "workspaceId": workspace_id,
                "columnName": column_name,
                "updates": convert_and_respect_annotation_metadata(
                    object_=updates, annotation=UpdateTableColumnRequestUpdates, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2TableColumnsResponse,
                    parse_obj_as(
                        type_=V2TableColumnsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 423:
                raise LockedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_table_rows(
        self,
        table_id: str,
        *,
        workspace_id: str,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        include_run_state: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V2TableRowListResponse]:
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
        AsyncHttpResponse[V2TableRowListResponse]
            A page of table rows.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/rows",
            method="GET",
            params={
                "workspaceId": workspace_id,
                "limit": limit,
                "cursor": cursor,
                "includeRunState": include_run_state,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2TableRowListResponse,
                    parse_obj_as(
                        type_=V2TableRowListResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_table_rows(
        self, table_id: str, *, request: CreateTableRowsRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[V2CreateTableRowsResponse]:
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
        AsyncHttpResponse[V2CreateTableRowsResponse]
            The inserted row or rows.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/rows",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=CreateTableRowsRequest, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2CreateTableRowsResponse,
                    parse_obj_as(
                        type_=V2CreateTableRowsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 423:
                raise LockedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_table_rows(
        self,
        table_id: str,
        *,
        workspace_id: str,
        filter: typing.Optional[TablePredicate] = OMIT,
        limit: typing.Optional[int] = OMIT,
        row_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V2DeleteTableRowsResponse]:
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
        AsyncHttpResponse[V2DeleteTableRowsResponse]
            The bulk deletion result.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/rows",
            method="DELETE",
            json={
                "workspaceId": workspace_id,
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=TablePredicate, direction="write"
                ),
                "limit": limit,
                "rowIds": row_ids,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2DeleteTableRowsResponse,
                    parse_obj_as(
                        type_=V2DeleteTableRowsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 423:
                raise LockedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_table_rows(
        self,
        table_id: str,
        *,
        workspace_id: str,
        filter: TablePredicate,
        data: V2TableRowData,
        limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V2UpdateTableRowsResponse]:
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
        AsyncHttpResponse[V2UpdateTableRowsResponse]
            The bulk update result.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/rows",
            method="PATCH",
            json={
                "workspaceId": workspace_id,
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=TablePredicate, direction="write"
                ),
                "data": data,
                "limit": limit,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2UpdateTableRowsResponse,
                    parse_obj_as(
                        type_=V2UpdateTableRowsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 423:
                raise LockedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_table_row(
        self,
        table_id: str,
        row_id: str,
        *,
        workspace_id: str,
        include_run_state: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V2TableRowResponse]:
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
        AsyncHttpResponse[V2TableRowResponse]
            The requested table row.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/rows/{encode_path_param(row_id)}",
            method="GET",
            params={
                "workspaceId": workspace_id,
                "includeRunState": include_run_state,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2TableRowResponse,
                    parse_obj_as(
                        type_=V2TableRowResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_table_row(
        self, table_id: str, row_id: str, *, workspace_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[V2DeleteTableRowResponse]:
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
        AsyncHttpResponse[V2DeleteTableRowResponse]
            The row deletion result.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/rows/{encode_path_param(row_id)}",
            method="DELETE",
            params={
                "workspaceId": workspace_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2DeleteTableRowResponse,
                    parse_obj_as(
                        type_=V2DeleteTableRowResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 423:
                raise LockedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_table_row(
        self,
        table_id: str,
        row_id: str,
        *,
        workspace_id: str,
        data: V2TableRowData,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V2TableRowResponse]:
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
        AsyncHttpResponse[V2TableRowResponse]
            The updated table row.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/rows/{encode_path_param(row_id)}",
            method="PATCH",
            json={
                "workspaceId": workspace_id,
                "data": data,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2TableRowResponse,
                    parse_obj_as(
                        type_=V2TableRowResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 423:
                raise LockedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def upsert_table_row(
        self,
        table_id: str,
        *,
        workspace_id: str,
        data: V2TableRowData,
        conflict_target: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V2UpsertTableRowResponse]:
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
        AsyncHttpResponse[V2UpsertTableRowResponse]
            The upserted row and operation performed.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/rows/upsert",
            method="POST",
            json={
                "workspaceId": workspace_id,
                "data": data,
                "conflictTarget": conflict_target,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2UpsertTableRowResponse,
                    parse_obj_as(
                        type_=V2UpsertTableRowResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 423:
                raise LockedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[V2QueryTableRowsResponse]:
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
        AsyncHttpResponse[V2QueryTableRowsResponse]
            A page of matching table rows.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/query",
            method="POST",
            json={
                "workspaceId": workspace_id,
                "predicate": convert_and_respect_annotation_metadata(
                    object_=predicate, annotation=TablePredicateInput, direction="write"
                ),
                "sort": convert_and_respect_annotation_metadata(
                    object_=sort, annotation=typing.Sequence[QueryTableRowsRequestSortItem], direction="write"
                ),
                "limit": limit,
                "cursor": cursor,
                "includeRunState": include_run_state,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2QueryTableRowsResponse,
                    parse_obj_as(
                        type_=V2QueryTableRowsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def count_table_rows(
        self,
        table_id: str,
        *,
        workspace_id: str,
        predicate: typing.Optional[TablePredicateInput] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V2CountTableRowsResponse]:
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
        AsyncHttpResponse[V2CountTableRowsResponse]
            The number of matching table rows.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/query/count",
            method="POST",
            json={
                "workspaceId": workspace_id,
                "predicate": convert_and_respect_annotation_metadata(
                    object_=predicate, annotation=TablePredicateInput, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2CountTableRowsResponse,
                    parse_obj_as(
                        type_=V2CountTableRowsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_table_views(
        self, table_id: str, *, workspace_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[V2TableViewListResponse]:
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
        AsyncHttpResponse[V2TableViewListResponse]
            The saved table views.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/views",
            method="GET",
            params={
                "workspaceId": workspace_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2TableViewListResponse,
                    parse_obj_as(
                        type_=V2TableViewListResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_table_view(
        self,
        table_id: str,
        *,
        workspace_id: str,
        name: str,
        config: CreateTableViewRequestConfig,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V2CreateTableViewResponse]:
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
        AsyncHttpResponse[V2CreateTableViewResponse]
            The created table view.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/views",
            method="POST",
            json={
                "workspaceId": workspace_id,
                "name": name,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=CreateTableViewRequestConfig, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2CreateTableViewResponse,
                    parse_obj_as(
                        type_=V2CreateTableViewResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_table_view(
        self, table_id: str, view_id: str, *, workspace_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[V2TableViewResponse]:
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
        AsyncHttpResponse[V2TableViewResponse]
            The requested table view.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/views/{encode_path_param(view_id)}",
            method="GET",
            params={
                "workspaceId": workspace_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2TableViewResponse,
                    parse_obj_as(
                        type_=V2TableViewResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_table_view(
        self, table_id: str, view_id: str, *, workspace_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[V2DeleteTableViewResponse]:
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
        AsyncHttpResponse[V2DeleteTableViewResponse]
            Table view deletion acknowledgement.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/views/{encode_path_param(view_id)}",
            method="DELETE",
            params={
                "workspaceId": workspace_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2DeleteTableViewResponse,
                    parse_obj_as(
                        type_=V2DeleteTableViewResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[V2TableViewResponse]:
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
        AsyncHttpResponse[V2TableViewResponse]
            The updated table view.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/views/{encode_path_param(view_id)}",
            method="PATCH",
            json={
                "workspaceId": workspace_id,
                "name": name,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=UpdateTableViewRequestConfig, direction="write"
                ),
                "configPatch": convert_and_respect_annotation_metadata(
                    object_=config_patch, annotation=UpdateTableViewRequestConfigPatch, direction="write"
                ),
                "isDefault": is_default,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2TableViewResponse,
                    parse_obj_as(
                        type_=V2TableViewResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_table_workflow_groups(
        self, table_id: str, *, workspace_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[V2TableWorkflowGroupListResponse]:
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
        AsyncHttpResponse[V2TableWorkflowGroupListResponse]
            The table workflow groups.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/groups",
            method="GET",
            params={
                "workspaceId": workspace_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2TableWorkflowGroupListResponse,
                    parse_obj_as(
                        type_=V2TableWorkflowGroupListResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def add_table_workflow_group(
        self,
        table_id: str,
        *,
        workspace_id: str,
        group: AddTableWorkflowGroupRequestGroup,
        output_columns: typing.Sequence[AddTableWorkflowGroupRequestOutputColumnsItem],
        auto_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V2AddTableWorkflowGroupResponse]:
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
        AsyncHttpResponse[V2AddTableWorkflowGroupResponse]
            The created workflow group and resulting columns.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/groups",
            method="POST",
            json={
                "workspaceId": workspace_id,
                "group": convert_and_respect_annotation_metadata(
                    object_=group, annotation=AddTableWorkflowGroupRequestGroup, direction="write"
                ),
                "outputColumns": convert_and_respect_annotation_metadata(
                    object_=output_columns,
                    annotation=typing.Sequence[AddTableWorkflowGroupRequestOutputColumnsItem],
                    direction="write",
                ),
                "autoRun": auto_run,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2AddTableWorkflowGroupResponse,
                    parse_obj_as(
                        type_=V2AddTableWorkflowGroupResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 423:
                raise LockedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_table_workflow_group(
        self,
        table_id: str,
        *,
        workspace_id: str,
        group_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V2DeleteTableWorkflowGroupResponse]:
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
        AsyncHttpResponse[V2DeleteTableWorkflowGroupResponse]
            Workflow-group deletion acknowledgement and surviving columns.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/groups",
            method="DELETE",
            json={
                "workspaceId": workspace_id,
                "groupId": group_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2DeleteTableWorkflowGroupResponse,
                    parse_obj_as(
                        type_=V2DeleteTableWorkflowGroupResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 423:
                raise LockedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[V2UpdateTableWorkflowGroupResponse]:
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
        AsyncHttpResponse[V2UpdateTableWorkflowGroupResponse]
            The updated workflow group and resulting columns.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/groups",
            method="PATCH",
            json={
                "workspaceId": workspace_id,
                "groupId": group_id,
                "workflowId": workflow_id,
                "name": name,
                "dependencies": convert_and_respect_annotation_metadata(
                    object_=dependencies, annotation=UpdateTableWorkflowGroupRequestDependencies, direction="write"
                ),
                "outputs": convert_and_respect_annotation_metadata(
                    object_=outputs,
                    annotation=typing.Sequence[UpdateTableWorkflowGroupRequestOutputsItem],
                    direction="write",
                ),
                "newOutputColumns": convert_and_respect_annotation_metadata(
                    object_=new_output_columns,
                    annotation=typing.Sequence[UpdateTableWorkflowGroupRequestNewOutputColumnsItem],
                    direction="write",
                ),
                "mappingUpdates": convert_and_respect_annotation_metadata(
                    object_=mapping_updates,
                    annotation=typing.Sequence[UpdateTableWorkflowGroupRequestMappingUpdatesItem],
                    direction="write",
                ),
                "inputMappings": convert_and_respect_annotation_metadata(
                    object_=input_mappings,
                    annotation=typing.Sequence[UpdateTableWorkflowGroupRequestInputMappingsItem],
                    direction="write",
                ),
                "deploymentMode": deployment_mode,
                "type": type,
                "autoRun": auto_run,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2UpdateTableWorkflowGroupResponse,
                    parse_obj_as(
                        type_=V2UpdateTableWorkflowGroupResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 423:
                raise LockedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_table_dispatches(
        self, table_id: str, *, workspace_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[V2TableRunDispatchListResponse]:
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
        AsyncHttpResponse[V2TableRunDispatchListResponse]
            The table's active run dispatches.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/dispatches",
            method="GET",
            params={
                "workspaceId": workspace_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2TableRunDispatchListResponse,
                    parse_obj_as(
                        type_=V2TableRunDispatchListResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[V2CreateTableDispatchResponse]:
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
        AsyncHttpResponse[V2CreateTableDispatchResponse]
            The accepted run dispatch.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/dispatches",
            method="POST",
            json={
                "workspaceId": workspace_id,
                "groupIds": group_ids,
                "runMode": run_mode,
                "rowIds": row_ids,
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=TablePredicate, direction="write"
                ),
                "excludeRowIds": exclude_row_ids,
                "limit": convert_and_respect_annotation_metadata(
                    object_=limit, annotation=CreateTableDispatchRequestLimit, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2CreateTableDispatchResponse,
                    parse_obj_as(
                        type_=V2CreateTableDispatchResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_row_enrichment(
        self,
        table_id: str,
        row_id: str,
        group_id: str,
        *,
        workspace_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V2RowEnrichmentResponse]:
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
        AsyncHttpResponse[V2RowEnrichmentResponse]
            The enrichment run detail, or null when none was recorded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/rows/{encode_path_param(row_id)}/enrichment/{encode_path_param(group_id)}",
            method="GET",
            params={
                "workspaceId": workspace_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2RowEnrichmentResponse,
                    parse_obj_as(
                        type_=V2RowEnrichmentResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def run_row_enrichment(
        self,
        table_id: str,
        row_id: str,
        group_id: str,
        *,
        workspace_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V2RunRowEnrichmentResponse]:
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
        AsyncHttpResponse[V2RunRowEnrichmentResponse]
            The accepted row enrichment dispatch.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/rows/{encode_path_param(row_id)}/enrichment/{encode_path_param(group_id)}",
            method="POST",
            json={
                "workspaceId": workspace_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2RunRowEnrichmentResponse,
                    parse_obj_as(
                        type_=V2RunRowEnrichmentResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def search_table_rows(
        self,
        table_id: str,
        *,
        workspace_id: str,
        q: str,
        predicate: typing.Optional[TablePredicate] = OMIT,
        sort: typing.Optional[typing.Sequence[SearchTableRowsRequestSortItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V2SearchTableRowsResponse]:
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
        AsyncHttpResponse[V2SearchTableRowsResponse]
            The matching table cells.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/rows/search",
            method="POST",
            json={
                "workspaceId": workspace_id,
                "q": q,
                "predicate": convert_and_respect_annotation_metadata(
                    object_=predicate, annotation=TablePredicate, direction="write"
                ),
                "sort": convert_and_respect_annotation_metadata(
                    object_=sort, annotation=typing.Sequence[SearchTableRowsRequestSortItem], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2SearchTableRowsResponse,
                    parse_obj_as(
                        type_=V2SearchTableRowsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[V2CreateTableImportResponse]:
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
        AsyncHttpResponse[V2CreateTableImportResponse]
            The created table import and optional transfer instructions.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/tables/imports",
            method="POST",
            json={
                "workspaceId": workspace_id,
                "source": convert_and_respect_annotation_metadata(
                    object_=source, annotation=CreateTableImportRequestSource, direction="write"
                ),
                "target": convert_and_respect_annotation_metadata(
                    object_=target, annotation=CreateTableImportRequestTarget, direction="write"
                ),
                "mapping": mapping,
                "createColumns": create_columns,
                "timezone": timezone,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2CreateTableImportResponse,
                    parse_obj_as(
                        type_=V2CreateTableImportResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 423:
                raise LockedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_table_import(
        self,
        import_id: str,
        *,
        workspace_id: str,
        upload_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V2TableImportResponse]:
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
        AsyncHttpResponse[V2TableImportResponse]
            The requested table import.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/tables/imports/{encode_path_param(import_id)}",
            method="GET",
            params={
                "workspaceId": workspace_id,
            },
            headers={
                "upload-token": str(upload_token) if upload_token is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2TableImportResponse,
                    parse_obj_as(
                        type_=V2TableImportResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def cancel_table_import(
        self,
        import_id: str,
        *,
        workspace_id: str,
        upload_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V2CancelTableImportResponse]:
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
        AsyncHttpResponse[V2CancelTableImportResponse]
            The canceled table import.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/tables/imports/{encode_path_param(import_id)}",
            method="DELETE",
            params={
                "workspaceId": workspace_id,
            },
            headers={
                "upload-token": str(upload_token) if upload_token is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2CancelTableImportResponse,
                    parse_obj_as(
                        type_=V2CancelTableImportResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_table_import_part_urls(
        self,
        import_id: str,
        *,
        workspace_id: str,
        upload_token: str,
        part_numbers: typing.Sequence[int],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V2CreateTableImportPartUrlsResponse]:
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
        AsyncHttpResponse[V2CreateTableImportPartUrlsResponse]
            The signed multipart upload URLs.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/tables/imports/{encode_path_param(import_id)}/parts",
            method="POST",
            params={
                "workspaceId": workspace_id,
            },
            json={
                "partNumbers": part_numbers,
            },
            headers={
                "content-type": "application/json",
                "upload-token": str(upload_token) if upload_token is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2CreateTableImportPartUrlsResponse,
                    parse_obj_as(
                        type_=V2CreateTableImportPartUrlsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def complete_table_import_upload(
        self,
        import_id: str,
        *,
        workspace_id: str,
        upload_token: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V2CompleteTableImportUploadResponse]:
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
        AsyncHttpResponse[V2CompleteTableImportUploadResponse]
            The table import after upload completion.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/tables/imports/{encode_path_param(import_id)}/complete",
            method="POST",
            params={
                "workspaceId": workspace_id,
            },
            headers={
                "upload-token": str(upload_token) if upload_token is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2CompleteTableImportUploadResponse,
                    parse_obj_as(
                        type_=V2CompleteTableImportUploadResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 423:
                raise LockedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_table_export(
        self,
        table_id: str,
        *,
        workspace_id: str,
        format: typing.Optional[CreateTableExportRequestFormat] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V2CreateTableExportResponse]:
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
        AsyncHttpResponse[V2CreateTableExportResponse]
            The created table export.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/exports",
            method="POST",
            json={
                "workspaceId": workspace_id,
                "format": format,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2CreateTableExportResponse,
                    parse_obj_as(
                        type_=V2CreateTableExportResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_table_export(
        self,
        table_id: str,
        export_id: str,
        *,
        workspace_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V2TableExportResponse]:
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
        AsyncHttpResponse[V2TableExportResponse]
            The requested table export.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/exports/{encode_path_param(export_id)}",
            method="GET",
            params={
                "workspaceId": workspace_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2TableExportResponse,
                    parse_obj_as(
                        type_=V2TableExportResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def cancel_table_export(
        self,
        table_id: str,
        export_id: str,
        *,
        workspace_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V2CancelTableExportResponse]:
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
        AsyncHttpResponse[V2CancelTableExportResponse]
            The canceled table export.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/exports/{encode_path_param(export_id)}",
            method="DELETE",
            params={
                "workspaceId": workspace_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2CancelTableExportResponse,
                    parse_obj_as(
                        type_=V2CancelTableExportResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def download_table_export(
        self,
        table_id: str,
        export_id: str,
        *,
        workspace_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V2DownloadTableExportResponse]:
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
        AsyncHttpResponse[V2DownloadTableExportResponse]
            Signed table-export download information.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/exports/{encode_path_param(export_id)}/download",
            method="GET",
            params={
                "workspaceId": workspace_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2DownloadTableExportResponse,
                    parse_obj_as(
                        type_=V2DownloadTableExportResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[V2CancelTableRunsResponse]:
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
        AsyncHttpResponse[V2CancelTableRunsResponse]
            The number of canceled cell runs.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/cancel-runs",
            method="POST",
            json={
                "workspaceId": workspace_id,
                "scope": scope,
                "rowId": row_id,
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=TablePredicate, direction="write"
                ),
                "excludeRowIds": exclude_row_ids,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2CancelTableRunsResponse,
                    parse_obj_as(
                        type_=V2CancelTableRunsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_tables_folders(
        self,
        *,
        workspace_id: str,
        parent_path: typing.Optional[FolderPathInput] = None,
        search: typing.Optional[str] = None,
        sort_by: typing.Optional[ListTablesFoldersRequestSortBy] = None,
        sort_order: typing.Optional[ListTablesFoldersRequestSortOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V2TableFolderListResponse]:
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
        AsyncHttpResponse[V2TableFolderListResponse]
            The table folders.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/tables/folders",
            method="GET",
            params={
                "workspaceId": workspace_id,
                "parentPath": parent_path,
                "search": search,
                "sortBy": sort_by,
                "sortOrder": sort_order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2TableFolderListResponse,
                    parse_obj_as(
                        type_=V2TableFolderListResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_tables_folder(
        self,
        *,
        workspace_id: str,
        path: NonRootFolderPathInput,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V2CreateTableFolderResponse]:
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
        AsyncHttpResponse[V2CreateTableFolderResponse]
            The created table folder.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/tables/folders",
            method="POST",
            json={
                "workspaceId": workspace_id,
                "path": path,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2CreateTableFolderResponse,
                    parse_obj_as(
                        type_=V2CreateTableFolderResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_tables_folder(
        self,
        *,
        workspace_id: str,
        path: NonRootFolderPathInput,
        recursive: typing.Optional[DeleteTablesFolderRequestRecursive] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V2DeleteTableFolderResponse]:
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
        AsyncHttpResponse[V2DeleteTableFolderResponse]
            Table-folder deletion acknowledgement.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/tables/folders",
            method="DELETE",
            params={
                "workspaceId": workspace_id,
                "path": path,
                "recursive": recursive,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2DeleteTableFolderResponse,
                    parse_obj_as(
                        type_=V2DeleteTableFolderResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 423:
                raise LockedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def relocate_tables_folder(
        self,
        *,
        workspace_id: str,
        path: NonRootFolderPathInput,
        destination_path: NonRootFolderPathInput,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V2RelocateTableFolderResponse]:
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
        AsyncHttpResponse[V2RelocateTableFolderResponse]
            The relocated table folder.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/tables/folders",
            method="PATCH",
            json={
                "workspaceId": workspace_id,
                "path": path,
                "destinationPath": destination_path,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2RelocateTableFolderResponse,
                    parse_obj_as(
                        type_=V2RelocateTableFolderResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def restore_tables_folder(
        self,
        *,
        workspace_id: str,
        path: NonRootFolderPathInput,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V2RestoreTableFolderResponse]:
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
        AsyncHttpResponse[V2RestoreTableFolderResponse]
            The restored table folder and what it brought back.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/tables/folders/restore",
            method="POST",
            json={
                "workspaceId": workspace_id,
                "path": path,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2RestoreTableFolderResponse,
                    parse_obj_as(
                        type_=V2RestoreTableFolderResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def restore_table(
        self, table_id: str, *, workspace_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[V2RestoreTableResponse]:
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
        AsyncHttpResponse[V2RestoreTableResponse]
            The restored table.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/restore",
            method="POST",
            json={
                "workspaceId": workspace_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2RestoreTableResponse,
                    parse_obj_as(
                        type_=V2RestoreTableResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def bulk_update_table_rows(
        self,
        table_id: str,
        *,
        workspace_id: str,
        updates: typing.Sequence[BulkUpdateTableRowsRequestUpdatesItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V2BulkUpdateTableRowsResponse]:
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
        AsyncHttpResponse[V2BulkUpdateTableRowsResponse]
            The bulk update result.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/rows/bulk-update",
            method="POST",
            json={
                "workspaceId": workspace_id,
                "updates": convert_and_respect_annotation_metadata(
                    object_=updates,
                    annotation=typing.Sequence[BulkUpdateTableRowsRequestUpdatesItem],
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2BulkUpdateTableRowsResponse,
                    parse_obj_as(
                        type_=V2BulkUpdateTableRowsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 423:
                raise LockedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_table_dispatch(
        self,
        table_id: str,
        dispatch_id: str,
        *,
        workspace_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V2TableRunDispatchResponse]:
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
        AsyncHttpResponse[V2TableRunDispatchResponse]
            The requested run dispatch.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/dispatches/{encode_path_param(dispatch_id)}",
            method="GET",
            params={
                "workspaceId": workspace_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2TableRunDispatchResponse,
                    parse_obj_as(
                        type_=V2TableRunDispatchResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def cancel_table_dispatch(
        self,
        table_id: str,
        dispatch_id: str,
        *,
        workspace_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V2CancelTableDispatchResponse]:
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
        AsyncHttpResponse[V2CancelTableDispatchResponse]
            The dispatch in its post-cancellation state.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/tables/{encode_path_param(table_id)}/dispatches/{encode_path_param(dispatch_id)}",
            method="DELETE",
            params={
                "workspaceId": workspace_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2CancelTableDispatchResponse,
                    parse_obj_as(
                        type_=V2CancelTableDispatchResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def move_tables(
        self,
        *,
        workspace_id: str,
        table_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        folder_paths: typing.Optional[typing.Sequence[FolderPathInput]] = OMIT,
        target_folder_path: typing.Optional[FolderPathInput] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V2MoveTablesResponse]:
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
        AsyncHttpResponse[V2MoveTablesResponse]
            Per-item outcome of the bulk move.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/tables/move",
            method="POST",
            json={
                "workspaceId": workspace_id,
                "tableIds": table_ids,
                "folderPaths": folder_paths,
                "targetFolderPath": target_folder_path,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2MoveTablesResponse,
                    parse_obj_as(
                        type_=V2MoveTablesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def bulk_delete_tables(
        self,
        *,
        workspace_id: str,
        table_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        folder_paths: typing.Optional[typing.Sequence[FolderPathInput]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V2BulkDeleteTablesResponse]:
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
        AsyncHttpResponse[V2BulkDeleteTablesResponse]
            Per-item outcome of the bulk delete.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/tables/bulk-delete",
            method="POST",
            json={
                "workspaceId": workspace_id,
                "tableIds": table_ids,
                "folderPaths": folder_paths,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2BulkDeleteTablesResponse,
                    parse_obj_as(
                        type_=V2BulkDeleteTablesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 423:
                raise LockedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
