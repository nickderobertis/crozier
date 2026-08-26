

import contextlib
import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.jsonable_encoder import encode_path_param
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from .core.serialization import convert_and_respect_annotation_metadata
from .errors.bad_request_error import BadRequestError
from .errors.forbidden_error import ForbiddenError
from .errors.internal_server_error import InternalServerError
from .errors.not_found_error import NotFoundError
from .types.ai_completion_context import AiCompletionContext
from .types.ai_completion_request_language import AiCompletionRequestLanguage
from .types.ai_inline_completion_request_language import AiInlineCompletionRequestLanguage
from .types.base64string import Base64String
from .types.base_response import BaseResponse
from .types.cell_config import CellConfig
from .types.cell_id import CellId
from .types.cell_outputs import CellOutputs
from .types.chat_options import ChatOptions
from .types.chat_request_variables_item import ChatRequestVariablesItem
from .types.create_secret_request_provider import CreateSecretRequestProvider
from .types.dependency_tree_response import DependencyTreeResponse
from .types.export_as_ipynb_request_sort_mode import ExportAsIpynbRequestSortMode
from .types.export_as_markdown_request_flavor import ExportAsMarkdownRequestFlavor
from .types.export_as_pdf_request_preset import ExportAsPdfRequestPreset
from .types.export_availability_response import ExportAvailabilityResponse
from .types.file_copy_response import FileCopyResponse
from .types.file_create_response import FileCreateResponse
from .types.file_delete_response import FileDeleteResponse
from .types.file_details_response import FileDetailsResponse
from .types.file_list_response import FileListResponse
from .types.file_move_response import FileMoveResponse
from .types.file_search_response import FileSearchResponse
from .types.file_update_response import FileUpdateResponse
from .types.format_response import FormatResponse
from .types.get_api_environment_response import GetApiEnvironmentResponse
from .types.get_api_status_connections_response import GetApiStatusConnectionsResponse
from .types.get_api_status_response import GetApiStatusResponse
from .types.get_api_usage_response import GetApiUsageResponse
from .types.http_request import HttpRequest
from .types.install_export_requirements_request_format import InstallExportRequirementsRequestFormat
from .types.install_packages_request_source import InstallPackagesRequestSource
from .types.invoke_ai_tool_response import InvokeAiToolResponse
from .types.kernel_status_response import KernelStatusResponse
from .types.list_packages_response import ListPackagesResponse
from .types.list_secret_keys_response import ListSecretKeysResponse
from .types.lsp_health_response import LspHealthResponse
from .types.lsp_restart_response import LspRestartResponse
from .types.marimo_file import MarimoFile
from .types.mcp_refresh_response import McpRefreshResponse
from .types.mcp_status_response import McpStatusResponse
from .types.model_request_message import ModelRequestMessage
from .types.notebook_cell import NotebookCell
from .types.notebook_document_transaction_request_changes_item import NotebookDocumentTransactionRequestChangesItem
from .types.open_tutorial_request_tutorial_id import OpenTutorialRequestTutorialId
from .types.package_operation_response import PackageOperationResponse
from .types.post_api_files_create_request_type import PostApiFilesCreateRequestType
from .types.post_api_kernel_takeover_response import PostApiKernelTakeoverResponse
from .types.preview_dataset_column_request_source_type import PreviewDatasetColumnRequestSourceType
from .types.read_code_response import ReadCodeResponse
from .types.recent_files_response import RecentFilesResponse
from .types.request_id import RequestId
from .types.running_notebooks_response import RunningNotebooksResponse
from .types.session_id import SessionId
from .types.snippets import Snippets
from .types.success_response import SuccessResponse
from .types.tool_definition import ToolDefinition
from .types.ui_element_id import UiElementId
from .types.widget_model_id import WidgetModelId
from .types.workspace_files_response import WorkspaceFilesResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    @contextlib.contextmanager
    def get_file_filename_and_length(
        self, filename_and_length: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        Parameters
        ----------
        filename_and_length : str
            The filename and byte length of the virtual file

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            Get a virtual file
        """
        with self._client_wrapper.httpx_client.stream(
            f"@file/{encode_path_param(filename_and_length)}",
            method="GET",
            request_options=request_options,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return HttpResponse(
                            response=_response, data=(_chunk for _chunk in _response.iter_bytes(chunk_size=_chunk_size))
                        )
                    _response.read()
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Any,
                                parse_obj_as(
                                    type_=typing.Any,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()

    def post_api_ai_chat(
        self,
        *,
        marimo_session_id: str,
        include_other_code: str,
        ui_messages: typing.Sequence[typing.Dict[str, typing.Any]],
        model: typing.Optional[str] = OMIT,
        options: typing.Optional[ChatOptions] = OMIT,
        tools: typing.Optional[typing.Sequence[ToolDefinition]] = OMIT,
        variables: typing.Optional[typing.Sequence[ChatRequestVariablesItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        marimo_session_id : str

        include_other_code : str

        ui_messages : typing.Sequence[typing.Dict[str, typing.Any]]

        model : typing.Optional[str]

        options : typing.Optional[ChatOptions]

        tools : typing.Optional[typing.Sequence[ToolDefinition]]

        variables : typing.Optional[typing.Sequence[ChatRequestVariablesItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/ai/chat",
            method="POST",
            json={
                "includeOtherCode": include_other_code,
                "model": model,
                "options": convert_and_respect_annotation_metadata(
                    object_=options, annotation=ChatOptions, direction="write"
                ),
                "tools": convert_and_respect_annotation_metadata(
                    object_=tools, annotation=typing.Optional[typing.Sequence[ToolDefinition]], direction="write"
                ),
                "uiMessages": ui_messages,
                "variables": convert_and_respect_annotation_metadata(
                    object_=variables,
                    annotation=typing.Optional[typing.Sequence[ChatRequestVariablesItem]],
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_ai_completion(
        self,
        *,
        marimo_session_id: str,
        code: str,
        include_other_code: str,
        prompt: str,
        context: typing.Optional[AiCompletionContext] = OMIT,
        language: typing.Optional[AiCompletionRequestLanguage] = OMIT,
        selected_text: typing.Optional[str] = OMIT,
        ui_messages: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        marimo_session_id : str

        code : str

        include_other_code : str

        prompt : str

        context : typing.Optional[AiCompletionContext]

        language : typing.Optional[AiCompletionRequestLanguage]

        selected_text : typing.Optional[str]

        ui_messages : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            Get AI completion for a prompt
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/ai/completion",
            method="POST",
            json={
                "code": code,
                "context": convert_and_respect_annotation_metadata(
                    object_=context, annotation=typing.Optional[AiCompletionContext], direction="write"
                ),
                "includeOtherCode": include_other_code,
                "language": language,
                "prompt": prompt,
                "selectedText": selected_text,
                "uiMessages": ui_messages,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_ai_inline_completion(
        self,
        *,
        marimo_session_id: str,
        prefix: str,
        suffix: str,
        language: typing.Optional[AiInlineCompletionRequestLanguage] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Parameters
        ----------
        marimo_session_id : str

        prefix : str

        suffix : str

        language : typing.Optional[AiInlineCompletionRequestLanguage]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Get AI inline completion for code
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/ai/inline_completion",
            method="POST",
            json={
                "language": language,
                "prefix": prefix,
                "suffix": suffix,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_ai_invoke_tool(
        self,
        *,
        marimo_session_id: str,
        arguments: typing.Dict[str, typing.Any],
        tool_name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[InvokeAiToolResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        arguments : typing.Dict[str, typing.Any]

        tool_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InvokeAiToolResponse]
            Tool invocation result
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/ai/invoke_tool",
            method="POST",
            json={
                "arguments": arguments,
                "toolName": tool_name,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InvokeAiToolResponse,
                    parse_obj_as(
                        type_=InvokeAiToolResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_ai_mcp_refresh(
        self, *, marimo_session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[McpRefreshResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[McpRefreshResponse]
            Refresh MCP server configuration
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/ai/mcp/refresh",
            method="POST",
            headers={
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    McpRefreshResponse,
                    parse_obj_as(
                        type_=McpRefreshResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_api_ai_mcp_status(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[McpStatusResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[McpStatusResponse]
            Get MCP server status
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/ai/mcp/status",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    McpStatusResponse,
                    parse_obj_as(
                        type_=McpStatusResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_cache_clear(
        self, *, marimo_session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SuccessResponse]
            Clear all caches
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/cache/clear",
            method="POST",
            json={},
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_cache_info(
        self, *, marimo_session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SuccessResponse]
            Get cache statistics
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/cache/info",
            method="POST",
            json={},
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_datasources_discover(
        self, *, marimo_session_id: str, request_id: RequestId, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        request_id : RequestId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SuccessResponse]
            Discover datasource connections
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/datasources/discover",
            method="POST",
            json={
                "requestId": request_id,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_datasources_preview_column(
        self,
        *,
        marimo_session_id: str,
        column_name: str,
        source: str,
        source_type: PreviewDatasetColumnRequestSourceType,
        table_name: str,
        fully_qualified_table_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        column_name : str

        source : str

        source_type : PreviewDatasetColumnRequestSourceType

        table_name : str

        fully_qualified_table_name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SuccessResponse]
            Preview a column in a dataset
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/datasources/preview_column",
            method="POST",
            json={
                "columnName": column_name,
                "fullyQualifiedTableName": fully_qualified_table_name,
                "source": source,
                "sourceType": source_type,
                "tableName": table_name,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_datasources_preview_datasource_connection(
        self, *, marimo_session_id: str, engine: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        engine : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SuccessResponse]
            Broadcasts a datasource connection
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/datasources/preview_datasource_connection",
            method="POST",
            json={
                "engine": engine,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_datasources_preview_sql_schema_list(
        self,
        *,
        marimo_session_id: str,
        database: str,
        engine: str,
        request_id: RequestId,
        schema_path: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        database : str

        engine : str

        request_id : RequestId

        schema_path : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SuccessResponse]
            Preview a list of schemas in an SQL database
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/datasources/preview_sql_schema_list",
            method="POST",
            json={
                "database": database,
                "engine": engine,
                "requestId": request_id,
                "schemaPath": schema_path,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_datasources_preview_sql_table(
        self,
        *,
        marimo_session_id: str,
        database: str,
        engine: str,
        request_id: RequestId,
        schema: str,
        table_name: str,
        schema_path: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        database : str

        engine : str

        request_id : RequestId

        schema : str

        table_name : str

        schema_path : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SuccessResponse]
            Preview a SQL table
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/datasources/preview_sql_table",
            method="POST",
            json={
                "database": database,
                "engine": engine,
                "requestId": request_id,
                "schema": schema,
                "schemaPath": schema_path,
                "tableName": table_name,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_datasources_preview_sql_table_list(
        self,
        *,
        marimo_session_id: str,
        database: str,
        engine: str,
        request_id: RequestId,
        schema: str,
        schema_path: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        database : str

        engine : str

        request_id : RequestId

        schema : str

        schema_path : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SuccessResponse]
            Preview a list of tables in an SQL schema
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/datasources/preview_sql_table_list",
            method="POST",
            json={
                "database": database,
                "engine": engine,
                "requestId": request_id,
                "schema": schema,
                "schemaPath": schema_path,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_document_transaction(
        self,
        *,
        marimo_session_id: str,
        changes: typing.Sequence[NotebookDocumentTransactionRequestChangesItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        changes : typing.Sequence[NotebookDocumentTransactionRequestChangesItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SuccessResponse]
            Apply a document transaction
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/document/transaction",
            method="POST",
            json={
                "changes": convert_and_respect_annotation_metadata(
                    object_=changes,
                    annotation=typing.Sequence[NotebookDocumentTransactionRequestChangesItem],
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_api_documentation_snippets(
        self, *, marimo_session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Snippets]:
        """
        Parameters
        ----------
        marimo_session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Snippets]
            Load the snippets for the documentation page
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/documentation/snippets",
            method="GET",
            headers={
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Snippets,
                    parse_obj_as(
                        type_=Snippets,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_api_environment(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetApiEnvironmentResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetApiEnvironmentResponse]
            Environment information for issue reporting
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/environment",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetApiEnvironmentResponse,
                    parse_obj_as(
                        type_=GetApiEnvironmentResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_export_auto_export_html(
        self,
        *,
        marimo_session_id: str,
        download: bool,
        files: typing.Sequence[str],
        include_code: bool,
        asset_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        download : bool

        files : typing.Sequence[str]

        include_code : bool

        asset_url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SuccessResponse]
            Export the notebook as HTML
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/export/auto_export/html",
            method="POST",
            json={
                "assetUrl": asset_url,
                "download": download,
                "files": files,
                "includeCode": include_code,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def post_api_export_auto_export_ipynb(
        self, *, marimo_session_id: str, download: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        download : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SuccessResponse]
            Export the notebook as IPYNB
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/export/auto_export/ipynb",
            method="POST",
            json={
                "download": download,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def post_api_export_auto_export_markdown(
        self, *, marimo_session_id: str, download: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        download : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SuccessResponse]
            Export the notebook as a markdown
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/export/auto_export/markdown",
            method="POST",
            json={
                "download": download,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def get_api_export_availability(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ExportAvailabilityResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ExportAvailabilityResponse]
            Readiness for server-backed exports
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/export/availability",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExportAvailabilityResponse,
                    parse_obj_as(
                        type_=ExportAvailabilityResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_export_html(
        self,
        *,
        marimo_session_id: str,
        download: bool,
        files: typing.Sequence[str],
        include_code: bool,
        asset_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Parameters
        ----------
        marimo_session_id : str

        download : bool

        files : typing.Sequence[str]

        include_code : bool

        asset_url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Export the notebook as HTML
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/export/html",
            method="POST",
            json={
                "assetUrl": asset_url,
                "download": download,
                "files": files,
                "includeCode": include_code,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def post_api_export_ipynb(
        self,
        *,
        marimo_session_id: str,
        download: bool,
        include_outputs: typing.Optional[bool] = OMIT,
        sort_mode: typing.Optional[ExportAsIpynbRequestSortMode] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Parameters
        ----------
        marimo_session_id : str

        download : bool

        include_outputs : typing.Optional[bool]

        sort_mode : typing.Optional[ExportAsIpynbRequestSortMode]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Export the notebook as IPYNB
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/export/ipynb",
            method="POST",
            json={
                "download": download,
                "includeOutputs": include_outputs,
                "sortMode": sort_mode,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def post_api_export_markdown(
        self,
        *,
        marimo_session_id: str,
        download: bool,
        flavor: typing.Optional[ExportAsMarkdownRequestFlavor] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Parameters
        ----------
        marimo_session_id : str

        download : bool

        flavor : typing.Optional[ExportAsMarkdownRequestFlavor]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Export the notebook as a markdown
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/export/markdown",
            method="POST",
            json={
                "download": download,
                "flavor": flavor,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    @contextlib.contextmanager
    def post_api_export_pdf(
        self,
        *,
        marimo_session_id: str,
        webpdf: bool,
        include_inputs: typing.Optional[bool] = OMIT,
        include_outputs: typing.Optional[bool] = OMIT,
        preset: typing.Optional[ExportAsPdfRequestPreset] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        Parameters
        ----------
        marimo_session_id : str

        webpdf : bool

        include_inputs : typing.Optional[bool]

        include_outputs : typing.Optional[bool]

        preset : typing.Optional[ExportAsPdfRequestPreset]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            Export the notebook as a PDF
        """
        with self._client_wrapper.httpx_client.stream(
            "api/export/pdf",
            method="POST",
            json={
                "includeInputs": include_inputs,
                "includeOutputs": include_outputs,
                "preset": preset,
                "webpdf": webpdf,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return HttpResponse(
                            response=_response, data=(_chunk for _chunk in _response.iter_bytes(chunk_size=_chunk_size))
                        )
                    _response.read()
                    if _response.status_code == 400:
                        raise BadRequestError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Any,
                                parse_obj_as(
                                    type_=typing.Any,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 500:
                        raise InternalServerError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Any,
                                parse_obj_as(
                                    type_=typing.Any,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()

    def post_api_export_requirements_install(
        self,
        *,
        marimo_session_id: str,
        format: InstallExportRequirementsRequestFormat,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ExportAvailabilityResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        format : InstallExportRequirementsRequestFormat

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ExportAvailabilityResponse]
            Updated readiness for server-backed exports
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/export/requirements/install",
            method="POST",
            json={
                "format": format,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExportAvailabilityResponse,
                    parse_obj_as(
                        type_=ExportAvailabilityResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_export_script(
        self, *, marimo_session_id: str, download: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[str]:
        """
        Parameters
        ----------
        marimo_session_id : str

        download : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Export the notebook as a script
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/export/script",
            method="POST",
            json={
                "download": download,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def post_api_export_update_cell_outputs(
        self,
        *,
        marimo_session_id: str,
        cell_ids_to_output: typing.Dict[str, typing.Sequence[typing.Any]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        cell_ids_to_output : typing.Dict[str, typing.Sequence[typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SuccessResponse]
            Update the cell outputs
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/export/update_cell_outputs",
            method="POST",
            json={
                "cellIdsToOutput": cell_ids_to_output,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def post_api_files_copy(
        self, *, new_path: str, path: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[FileCopyResponse]:
        """
        Parameters
        ----------
        new_path : str

        path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FileCopyResponse]
            Copy a file or directory
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/files/copy",
            method="POST",
            json={
                "newPath": new_path,
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
                    FileCopyResponse,
                    parse_obj_as(
                        type_=FileCopyResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_files_create(
        self,
        *,
        name: str,
        path: str,
        type: PostApiFilesCreateRequestType,
        file: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FileCreateResponse]:
        """
        Parameters
        ----------
        name : str

        path : str

        type : PostApiFilesCreateRequestType

        file : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FileCreateResponse]
            Create a new file or directory
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/files/create",
            method="POST",
            data={
                "file": file,
                "name": name,
                "path": path,
                "type": type,
            },
            files={},
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FileCreateResponse,
                    parse_obj_as(
                        type_=FileCreateResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_files_delete(
        self, *, path: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[FileDeleteResponse]:
        """
        Parameters
        ----------
        path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FileDeleteResponse]
            Delete a file or directory
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/files/delete",
            method="POST",
            json={
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
                    FileDeleteResponse,
                    parse_obj_as(
                        type_=FileDeleteResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    @contextlib.contextmanager
    def get_api_files_download(
        self, *, path: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        Parameters
        ----------
        path : str
            Path of the file to download

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            Stream the file as an attachment
        """
        with self._client_wrapper.httpx_client.stream(
            "api/files/download",
            method="GET",
            params={
                "path": path,
            },
            request_options=request_options,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return HttpResponse(
                            response=_response, data=(_chunk for _chunk in _response.iter_bytes(chunk_size=_chunk_size))
                        )
                    _response.read()
                    if _response.status_code == 400:
                        raise BadRequestError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Any,
                                parse_obj_as(
                                    type_=typing.Any,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 403:
                        raise ForbiddenError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Any,
                                parse_obj_as(
                                    type_=typing.Any,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Any,
                                parse_obj_as(
                                    type_=typing.Any,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()

    def post_api_files_file_details(
        self,
        *,
        path: str,
        max_bytes: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FileDetailsResponse]:
        """
        Parameters
        ----------
        path : str

        max_bytes : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FileDetailsResponse]
            Get details of a specific file or directory
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/files/file_details",
            method="POST",
            json={
                "maxBytes": max_bytes,
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
                    FileDetailsResponse,
                    parse_obj_as(
                        type_=FileDetailsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_files_list_files(
        self, *, path: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[FileListResponse]:
        """
        Parameters
        ----------
        path : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FileListResponse]
            List files and directories in a given path
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/files/list_files",
            method="POST",
            json={
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
                    FileListResponse,
                    parse_obj_as(
                        type_=FileListResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_files_move(
        self, *, new_path: str, path: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[FileMoveResponse]:
        """
        Parameters
        ----------
        new_path : str

        path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FileMoveResponse]
            Move a file or directory
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/files/move",
            method="POST",
            json={
                "newPath": new_path,
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
                    FileMoveResponse,
                    parse_obj_as(
                        type_=FileMoveResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_files_open(
        self,
        *,
        path: str,
        line_number: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BaseResponse]:
        """
        Parameters
        ----------
        path : str

        line_number : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BaseResponse]
            Open a file in the system editor
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/files/open",
            method="POST",
            json={
                "lineNumber": line_number,
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
                    BaseResponse,
                    parse_obj_as(
                        type_=BaseResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_files_search(
        self,
        *,
        query: str,
        depth: typing.Optional[int] = OMIT,
        include_directories: typing.Optional[bool] = OMIT,
        include_files: typing.Optional[bool] = OMIT,
        limit: typing.Optional[int] = OMIT,
        path: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FileSearchResponse]:
        """
        Parameters
        ----------
        query : str

        depth : typing.Optional[int]

        include_directories : typing.Optional[bool]

        include_files : typing.Optional[bool]

        limit : typing.Optional[int]

        path : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FileSearchResponse]
            Search for files and directories matching a query
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/files/search",
            method="POST",
            json={
                "depth": depth,
                "includeDirectories": include_directories,
                "includeFiles": include_files,
                "limit": limit,
                "path": path,
                "query": query,
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
                    FileSearchResponse,
                    parse_obj_as(
                        type_=FileSearchResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_files_update(
        self, *, contents: str, path: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[FileUpdateResponse]:
        """
        Parameters
        ----------
        contents : str

        path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FileUpdateResponse]
            Update a file or directory
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/files/update",
            method="POST",
            json={
                "contents": contents,
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
                    FileUpdateResponse,
                    parse_obj_as(
                        type_=FileUpdateResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_home_recent_files(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RecentFilesResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RecentFilesResponse]
            Get the recent files
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/home/recent_files",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RecentFilesResponse,
                    parse_obj_as(
                        type_=RecentFilesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_home_running_notebooks(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RunningNotebooksResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RunningNotebooksResponse]
            Get the running files
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/home/running_notebooks",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RunningNotebooksResponse,
                    parse_obj_as(
                        type_=RunningNotebooksResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_home_shutdown_session(
        self, *, session_id: SessionId, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RunningNotebooksResponse]:
        """
        Parameters
        ----------
        session_id : SessionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RunningNotebooksResponse]
            Shutdown the current session
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/home/shutdown_session",
            method="POST",
            json={
                "sessionId": session_id,
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
                    RunningNotebooksResponse,
                    parse_obj_as(
                        type_=RunningNotebooksResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_home_tutorial_open(
        self, *, tutorial_id: OpenTutorialRequestTutorialId, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoFile]:
        """
        Parameters
        ----------
        tutorial_id : OpenTutorialRequestTutorialId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoFile]
            Open a new tutorial
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/home/tutorial/open",
            method="POST",
            json={
                "tutorialId": convert_and_respect_annotation_metadata(
                    object_=tutorial_id, annotation=OpenTutorialRequestTutorialId, direction="write"
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
                    MarimoFile,
                    parse_obj_as(
                        type_=MarimoFile,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_home_workspace_files(
        self, *, include_markdown: typing.Optional[bool] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WorkspaceFilesResponse]:
        """
        Parameters
        ----------
        include_markdown : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WorkspaceFilesResponse]
            Get the files in the workspace
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/home/workspace_files",
            method="POST",
            json={
                "includeMarkdown": include_markdown,
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
                    WorkspaceFilesResponse,
                    parse_obj_as(
                        type_=WorkspaceFilesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_kernel_code_autocomplete(
        self,
        *,
        marimo_session_id: str,
        cell_id: CellId,
        document: str,
        id: RequestId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        cell_id : CellId

        document : str

        id : RequestId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SuccessResponse]
            Complete a code fragment
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/kernel/code_autocomplete",
            method="POST",
            json={
                "cellId": cell_id,
                "document": document,
                "id": id,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_kernel_copy(
        self,
        *,
        marimo_session_id: str,
        destination: str,
        source: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Parameters
        ----------
        marimo_session_id : str

        destination : str

        source : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Copy notebook
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/kernel/copy",
            method="POST",
            json={
                "destination": destination,
                "source": source,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_kernel_delete(
        self, *, marimo_session_id: str, cell_id: CellId, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        cell_id : CellId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SuccessResponse]
            Delete a cell
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/kernel/delete",
            method="POST",
            json={
                "cellId": cell_id,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_kernel_focus_cell(
        self, *, marimo_session_id: str, cell_id: CellId, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        cell_id : CellId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SuccessResponse]
            Focus a cell in kiosk-mode consumers
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/kernel/focus_cell",
            method="POST",
            json={
                "cellId": cell_id,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_kernel_format(
        self, *, codes: typing.Dict[str, str], line_length: int, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[FormatResponse]:
        """
        Parameters
        ----------
        codes : typing.Dict[str, str]

        line_length : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FormatResponse]
            Format code
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/kernel/format",
            method="POST",
            json={
                "codes": codes,
                "lineLength": line_length,
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
                    FormatResponse,
                    parse_obj_as(
                        type_=FormatResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_kernel_function_call(
        self,
        *,
        marimo_session_id: str,
        args: typing.Dict[str, typing.Any],
        function_call_id: RequestId,
        function_name: str,
        namespace: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        args : typing.Dict[str, typing.Any]

        function_call_id : RequestId

        function_name : str

        namespace : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SuccessResponse]
            Invoke an RPC
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/kernel/function_call",
            method="POST",
            json={
                "args": args,
                "functionCallId": function_call_id,
                "functionName": function_name,
                "namespace": namespace,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_kernel_install_missing_packages(
        self,
        *,
        marimo_session_id: str,
        manager: str,
        versions: typing.Dict[str, str],
        source: typing.Optional[InstallPackagesRequestSource] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        manager : str

        versions : typing.Dict[str, str]

        source : typing.Optional[InstallPackagesRequestSource]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SuccessResponse]
            Install missing packages
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/kernel/install_missing_packages",
            method="POST",
            json={
                "manager": manager,
                "source": source,
                "versions": versions,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_kernel_instantiate(
        self,
        *,
        marimo_session_id: str,
        object_ids: typing.Sequence[UiElementId],
        values: typing.Sequence[typing.Any],
        auto_run: typing.Optional[bool] = OMIT,
        codes: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        object_ids : typing.Sequence[UiElementId]

        values : typing.Sequence[typing.Any]

        auto_run : typing.Optional[bool]

        codes : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SuccessResponse]
            Instantiate a component. Only allowed in edit mode; in run mode, instantiation happens server-side automatically.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/kernel/instantiate",
            method="POST",
            json={
                "autoRun": auto_run,
                "codes": codes,
                "objectIds": object_ids,
                "values": values,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_kernel_interrupt(
        self, *, marimo_session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SuccessResponse]
            Interrupt the kernel's execution
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/kernel/interrupt",
            method="POST",
            headers={
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_kernel_pdb_breakpoints(
        self,
        *,
        marimo_session_id: str,
        breakpoints: typing.Dict[str, typing.Sequence[int]],
        request: typing.Optional[HttpRequest] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        breakpoints : typing.Dict[str, typing.Sequence[int]]

        request : typing.Optional[HttpRequest]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SuccessResponse]
            Set the live debugger's breakpoints for the session.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/kernel/pdb/breakpoints",
            method="POST",
            json={
                "breakpoints": breakpoints,
                "request": convert_and_respect_annotation_metadata(
                    object_=request, annotation=typing.Optional[HttpRequest], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_kernel_pdb_pm(
        self,
        *,
        marimo_session_id: str,
        cell_id: CellId,
        request: typing.Optional[HttpRequest] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        cell_id : CellId

        request : typing.Optional[HttpRequest]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SuccessResponse]
            Run a post mortem on the most recent failed cell.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/kernel/pdb/pm",
            method="POST",
            json={
                "cellId": cell_id,
                "request": convert_and_respect_annotation_metadata(
                    object_=request, annotation=typing.Optional[HttpRequest], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_kernel_read_code(
        self, *, marimo_session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ReadCodeResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ReadCodeResponse]
            Read the code from the server
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/kernel/read_code",
            method="POST",
            headers={
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ReadCodeResponse,
                    parse_obj_as(
                        type_=ReadCodeResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def post_api_kernel_rename(
        self, *, marimo_session_id: str, filename: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        filename : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SuccessResponse]
            Rename the current app
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/kernel/rename",
            method="POST",
            json={
                "filename": filename,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_kernel_restart_session(
        self, *, marimo_session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SuccessResponse]
            Restart the current session without affecting other sessions.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/kernel/restart_session",
            method="POST",
            headers={
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_kernel_run(
        self,
        *,
        marimo_session_id: str,
        cell_ids: typing.Sequence[CellId],
        codes: typing.Sequence[str],
        request: typing.Optional[HttpRequest] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        cell_ids : typing.Sequence[CellId]

        codes : typing.Sequence[str]

        request : typing.Optional[HttpRequest]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SuccessResponse]
            Run a cell. Updates cell code in the kernel if needed; registers new cells for unseen cell IDs. Only allowed in edit mode.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/kernel/run",
            method="POST",
            json={
                "cellIds": cell_ids,
                "codes": codes,
                "request": convert_and_respect_annotation_metadata(
                    object_=request, annotation=typing.Optional[HttpRequest], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_kernel_save(
        self,
        *,
        marimo_session_id: str,
        cell_ids: typing.Sequence[CellId],
        codes: typing.Sequence[str],
        configs: typing.Sequence[CellConfig],
        filename: str,
        names: typing.Sequence[str],
        layout: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        persist: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Parameters
        ----------
        marimo_session_id : str

        cell_ids : typing.Sequence[CellId]

        codes : typing.Sequence[str]

        configs : typing.Sequence[CellConfig]

        filename : str

        names : typing.Sequence[str]

        layout : typing.Optional[typing.Dict[str, typing.Any]]

        persist : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Save the current app
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/kernel/save",
            method="POST",
            json={
                "cellIds": cell_ids,
                "codes": codes,
                "configs": convert_and_respect_annotation_metadata(
                    object_=configs, annotation=typing.Sequence[CellConfig], direction="write"
                ),
                "filename": filename,
                "layout": layout,
                "names": names,
                "persist": persist,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_kernel_save_app_config(
        self,
        *,
        marimo_session_id: str,
        config: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Parameters
        ----------
        marimo_session_id : str

        config : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Save the app configuration
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/kernel/save_app_config",
            method="POST",
            json={
                "config": config,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_kernel_save_user_config(
        self,
        *,
        config: typing.Dict[str, typing.Any],
        marimo_session_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        config : typing.Dict[str, typing.Any]

        marimo_session_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SuccessResponse]
            Update the user config on disk and in the kernel. Only allowed in edit mode.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/kernel/save_user_config",
            method="POST",
            json={
                "config": config,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_kernel_scratchpad_run(
        self,
        *,
        marimo_session_id: str,
        code: str,
        cell_outputs: typing.Optional[CellOutputs] = OMIT,
        notebook_cells: typing.Optional[typing.Sequence[NotebookCell]] = OMIT,
        request: typing.Optional[HttpRequest] = OMIT,
        run_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        code : str

        cell_outputs : typing.Optional[CellOutputs]

        notebook_cells : typing.Optional[typing.Sequence[NotebookCell]]

        request : typing.Optional[HttpRequest]

        run_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SuccessResponse]
            Run the scratchpad
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/kernel/scratchpad/run",
            method="POST",
            json={
                "cellOutputs": convert_and_respect_annotation_metadata(
                    object_=cell_outputs, annotation=typing.Optional[CellOutputs], direction="write"
                ),
                "code": code,
                "notebookCells": convert_and_respect_annotation_metadata(
                    object_=notebook_cells, annotation=typing.Optional[typing.Sequence[NotebookCell]], direction="write"
                ),
                "request": convert_and_respect_annotation_metadata(
                    object_=request, annotation=typing.Optional[HttpRequest], direction="write"
                ),
                "runId": run_id,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_kernel_set_cell_config(
        self,
        *,
        marimo_session_id: str,
        configs: typing.Dict[str, typing.Dict[str, typing.Any]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        configs : typing.Dict[str, typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SuccessResponse]
            Set the configuration of a cell
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/kernel/set_cell_config",
            method="POST",
            json={
                "configs": configs,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_kernel_set_model_value(
        self,
        *,
        marimo_session_id: str,
        buffers: typing.Sequence[Base64String],
        message: ModelRequestMessage,
        model_id: WidgetModelId,
        token: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        buffers : typing.Sequence[Base64String]

        message : ModelRequestMessage

        model_id : WidgetModelId

        token : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SuccessResponse]
            Set model value
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/kernel/set_model_value",
            method="POST",
            json={
                "buffers": buffers,
                "message": convert_and_respect_annotation_metadata(
                    object_=message, annotation=ModelRequestMessage, direction="write"
                ),
                "modelId": model_id,
                "token": token,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_kernel_set_ui_element_value(
        self,
        *,
        marimo_session_id: str,
        object_ids: typing.Sequence[UiElementId],
        values: typing.Sequence[typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        object_ids : typing.Sequence[UiElementId]

        values : typing.Sequence[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SuccessResponse]
            Set UI element values
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/kernel/set_ui_element_value",
            method="POST",
            json={
                "objectIds": object_ids,
                "values": values,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_kernel_shutdown(
        self, *, marimo_session_id: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SuccessResponse]
            Shutdown the kernel
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/kernel/shutdown",
            method="POST",
            headers={
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_api_kernel_status(
        self, *, marimo_session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[KernelStatusResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[KernelStatusResponse]
            Report whether the kernel is currently executing. `running` means at least one cell is queued or running; `idle` means the kernel is alive but not executing; `stopped` means the kernel process is not running.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/kernel/status",
            method="GET",
            headers={
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    KernelStatusResponse,
                    parse_obj_as(
                        type_=KernelStatusResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_kernel_stdin(
        self, *, marimo_session_id: str, text: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        text : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SuccessResponse]
            Send input to the stdin stream
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/kernel/stdin",
            method="POST",
            json={
                "text": text,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_kernel_takeover(
        self, *, marimo_session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PostApiKernelTakeoverResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostApiKernelTakeoverResponse]
            Successfully closed existing sessions
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/kernel/takeover",
            method="POST",
            headers={
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostApiKernelTakeoverResponse,
                    parse_obj_as(
                        type_=PostApiKernelTakeoverResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_api_lsp_health(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[LspHealthResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[LspHealthResponse]
            Get health status of all LSP servers
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/lsp/health",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LspHealthResponse,
                    parse_obj_as(
                        type_=LspHealthResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_lsp_restart(
        self,
        *,
        server_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[LspRestartResponse]:
        """
        Parameters
        ----------
        server_ids : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[LspRestartResponse]
            Restart LSP servers
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/lsp/restart",
            method="POST",
            json={
                "serverIds": server_ids,
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
                    LspRestartResponse,
                    parse_obj_as(
                        type_=LspRestartResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_packages_add(
        self,
        *,
        package: str,
        group: typing.Optional[str] = OMIT,
        upgrade: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PackageOperationResponse]:
        """
        Parameters
        ----------
        package : str

        group : typing.Optional[str]

        upgrade : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PackageOperationResponse]
            Install package
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/packages/add",
            method="POST",
            json={
                "group": group,
                "package": package,
                "upgrade": upgrade,
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
                    PackageOperationResponse,
                    parse_obj_as(
                        type_=PackageOperationResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_api_packages_list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListPackagesResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListPackagesResponse]
            List installed packages
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/packages/list",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListPackagesResponse,
                    parse_obj_as(
                        type_=ListPackagesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_packages_remove(
        self,
        *,
        package: str,
        group: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PackageOperationResponse]:
        """
        Parameters
        ----------
        package : str

        group : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PackageOperationResponse]
            Uninstall package
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/packages/remove",
            method="POST",
            json={
                "group": group,
                "package": package,
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
                    PackageOperationResponse,
                    parse_obj_as(
                        type_=PackageOperationResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_api_packages_tree(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DependencyTreeResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DependencyTreeResponse]
            List dependency tree
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/packages/tree",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DependencyTreeResponse,
                    parse_obj_as(
                        type_=DependencyTreeResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_secrets_create(
        self,
        *,
        marimo_session_id: str,
        key: str,
        name: str,
        provider: CreateSecretRequestProvider,
        value: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BaseResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        key : str

        name : str

        provider : CreateSecretRequestProvider

        value : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BaseResponse]
            Create a secret
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/secrets/create",
            method="POST",
            json={
                "key": key,
                "name": name,
                "provider": provider,
                "value": value,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BaseResponse,
                    parse_obj_as(
                        type_=BaseResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_secrets_delete(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[BaseResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BaseResponse]
            Delete a secret
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/secrets/delete",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BaseResponse,
                    parse_obj_as(
                        type_=BaseResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_secrets_keys(
        self, *, marimo_session_id: str, request_id: RequestId, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListSecretKeysResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        request_id : RequestId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListSecretKeysResponse]
            List all secret keys
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/secrets/keys",
            method="POST",
            json={
                "requestId": request_id,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListSecretKeysResponse,
                    parse_obj_as(
                        type_=ListSecretKeysResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_sql_validate(
        self,
        *,
        marimo_session_id: str,
        only_parse: bool,
        query: str,
        request_id: RequestId,
        dialect: typing.Optional[str] = OMIT,
        engine: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        only_parse : bool

        query : str

        request_id : RequestId

        dialect : typing.Optional[str]

        engine : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SuccessResponse]
            Validate an SQL query
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/sql/validate",
            method="POST",
            json={
                "dialect": dialect,
                "engine": engine,
                "onlyParse": only_parse,
                "query": query,
                "requestId": request_id,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_api_status(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetApiStatusResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetApiStatusResponse]
            Get the status of the application
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/status",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetApiStatusResponse,
                    parse_obj_as(
                        type_=GetApiStatusResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_api_status_connections(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetApiStatusConnectionsResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetApiStatusConnectionsResponse]
            Get the number of active websocket connections
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/status/connections",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetApiStatusConnectionsResponse,
                    parse_obj_as(
                        type_=GetApiStatusConnectionsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_storage_download(
        self,
        *,
        marimo_session_id: str,
        namespace: str,
        path: str,
        request_id: RequestId,
        preview: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        namespace : str

        path : str

        request_id : RequestId

        preview : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SuccessResponse]
            Download a storage entry
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/storage/download",
            method="POST",
            json={
                "namespace": namespace,
                "path": path,
                "preview": preview,
                "requestId": request_id,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_storage_list_entries(
        self,
        *,
        marimo_session_id: str,
        limit: int,
        namespace: str,
        request_id: RequestId,
        page_token: typing.Optional[str] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        limit : int

        namespace : str

        request_id : RequestId

        page_token : typing.Optional[str]

        prefix : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SuccessResponse]
            List storage entries at a prefix
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/storage/list_entries",
            method="POST",
            json={
                "limit": limit,
                "namespace": namespace,
                "pageToken": page_token,
                "prefix": prefix,
                "requestId": request_id,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_api_usage(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetApiUsageResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetApiUsageResponse]
            Get the current memory and CPU usage of the application
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/usage",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetApiUsageResponse,
                    parse_obj_as(
                        type_=GetApiUsageResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_api_version(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Get the version of the application
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/version",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawFernApi:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    @contextlib.asynccontextmanager
    async def get_file_filename_and_length(
        self, filename_and_length: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        Parameters
        ----------
        filename_and_length : str
            The filename and byte length of the virtual file

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            Get a virtual file
        """
        async with self._client_wrapper.httpx_client.stream(
            f"@file/{encode_path_param(filename_and_length)}",
            method="GET",
            request_options=request_options,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return AsyncHttpResponse(
                            response=_response,
                            data=(_chunk async for _chunk in _response.aiter_bytes(chunk_size=_chunk_size)),
                        )
                    await _response.aread()
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Any,
                                parse_obj_as(
                                    type_=typing.Any,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()

    async def post_api_ai_chat(
        self,
        *,
        marimo_session_id: str,
        include_other_code: str,
        ui_messages: typing.Sequence[typing.Dict[str, typing.Any]],
        model: typing.Optional[str] = OMIT,
        options: typing.Optional[ChatOptions] = OMIT,
        tools: typing.Optional[typing.Sequence[ToolDefinition]] = OMIT,
        variables: typing.Optional[typing.Sequence[ChatRequestVariablesItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        marimo_session_id : str

        include_other_code : str

        ui_messages : typing.Sequence[typing.Dict[str, typing.Any]]

        model : typing.Optional[str]

        options : typing.Optional[ChatOptions]

        tools : typing.Optional[typing.Sequence[ToolDefinition]]

        variables : typing.Optional[typing.Sequence[ChatRequestVariablesItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/ai/chat",
            method="POST",
            json={
                "includeOtherCode": include_other_code,
                "model": model,
                "options": convert_and_respect_annotation_metadata(
                    object_=options, annotation=ChatOptions, direction="write"
                ),
                "tools": convert_and_respect_annotation_metadata(
                    object_=tools, annotation=typing.Optional[typing.Sequence[ToolDefinition]], direction="write"
                ),
                "uiMessages": ui_messages,
                "variables": convert_and_respect_annotation_metadata(
                    object_=variables,
                    annotation=typing.Optional[typing.Sequence[ChatRequestVariablesItem]],
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_ai_completion(
        self,
        *,
        marimo_session_id: str,
        code: str,
        include_other_code: str,
        prompt: str,
        context: typing.Optional[AiCompletionContext] = OMIT,
        language: typing.Optional[AiCompletionRequestLanguage] = OMIT,
        selected_text: typing.Optional[str] = OMIT,
        ui_messages: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        marimo_session_id : str

        code : str

        include_other_code : str

        prompt : str

        context : typing.Optional[AiCompletionContext]

        language : typing.Optional[AiCompletionRequestLanguage]

        selected_text : typing.Optional[str]

        ui_messages : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            Get AI completion for a prompt
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/ai/completion",
            method="POST",
            json={
                "code": code,
                "context": convert_and_respect_annotation_metadata(
                    object_=context, annotation=typing.Optional[AiCompletionContext], direction="write"
                ),
                "includeOtherCode": include_other_code,
                "language": language,
                "prompt": prompt,
                "selectedText": selected_text,
                "uiMessages": ui_messages,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_ai_inline_completion(
        self,
        *,
        marimo_session_id: str,
        prefix: str,
        suffix: str,
        language: typing.Optional[AiInlineCompletionRequestLanguage] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Parameters
        ----------
        marimo_session_id : str

        prefix : str

        suffix : str

        language : typing.Optional[AiInlineCompletionRequestLanguage]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Get AI inline completion for code
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/ai/inline_completion",
            method="POST",
            json={
                "language": language,
                "prefix": prefix,
                "suffix": suffix,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_ai_invoke_tool(
        self,
        *,
        marimo_session_id: str,
        arguments: typing.Dict[str, typing.Any],
        tool_name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[InvokeAiToolResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        arguments : typing.Dict[str, typing.Any]

        tool_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InvokeAiToolResponse]
            Tool invocation result
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/ai/invoke_tool",
            method="POST",
            json={
                "arguments": arguments,
                "toolName": tool_name,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InvokeAiToolResponse,
                    parse_obj_as(
                        type_=InvokeAiToolResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_ai_mcp_refresh(
        self, *, marimo_session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[McpRefreshResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[McpRefreshResponse]
            Refresh MCP server configuration
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/ai/mcp/refresh",
            method="POST",
            headers={
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    McpRefreshResponse,
                    parse_obj_as(
                        type_=McpRefreshResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_api_ai_mcp_status(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[McpStatusResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[McpStatusResponse]
            Get MCP server status
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/ai/mcp/status",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    McpStatusResponse,
                    parse_obj_as(
                        type_=McpStatusResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_cache_clear(
        self, *, marimo_session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SuccessResponse]
            Clear all caches
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/cache/clear",
            method="POST",
            json={},
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_cache_info(
        self, *, marimo_session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SuccessResponse]
            Get cache statistics
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/cache/info",
            method="POST",
            json={},
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_datasources_discover(
        self, *, marimo_session_id: str, request_id: RequestId, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        request_id : RequestId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SuccessResponse]
            Discover datasource connections
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/datasources/discover",
            method="POST",
            json={
                "requestId": request_id,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_datasources_preview_column(
        self,
        *,
        marimo_session_id: str,
        column_name: str,
        source: str,
        source_type: PreviewDatasetColumnRequestSourceType,
        table_name: str,
        fully_qualified_table_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        column_name : str

        source : str

        source_type : PreviewDatasetColumnRequestSourceType

        table_name : str

        fully_qualified_table_name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SuccessResponse]
            Preview a column in a dataset
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/datasources/preview_column",
            method="POST",
            json={
                "columnName": column_name,
                "fullyQualifiedTableName": fully_qualified_table_name,
                "source": source,
                "sourceType": source_type,
                "tableName": table_name,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_datasources_preview_datasource_connection(
        self, *, marimo_session_id: str, engine: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        engine : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SuccessResponse]
            Broadcasts a datasource connection
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/datasources/preview_datasource_connection",
            method="POST",
            json={
                "engine": engine,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_datasources_preview_sql_schema_list(
        self,
        *,
        marimo_session_id: str,
        database: str,
        engine: str,
        request_id: RequestId,
        schema_path: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        database : str

        engine : str

        request_id : RequestId

        schema_path : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SuccessResponse]
            Preview a list of schemas in an SQL database
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/datasources/preview_sql_schema_list",
            method="POST",
            json={
                "database": database,
                "engine": engine,
                "requestId": request_id,
                "schemaPath": schema_path,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_datasources_preview_sql_table(
        self,
        *,
        marimo_session_id: str,
        database: str,
        engine: str,
        request_id: RequestId,
        schema: str,
        table_name: str,
        schema_path: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        database : str

        engine : str

        request_id : RequestId

        schema : str

        table_name : str

        schema_path : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SuccessResponse]
            Preview a SQL table
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/datasources/preview_sql_table",
            method="POST",
            json={
                "database": database,
                "engine": engine,
                "requestId": request_id,
                "schema": schema,
                "schemaPath": schema_path,
                "tableName": table_name,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_datasources_preview_sql_table_list(
        self,
        *,
        marimo_session_id: str,
        database: str,
        engine: str,
        request_id: RequestId,
        schema: str,
        schema_path: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        database : str

        engine : str

        request_id : RequestId

        schema : str

        schema_path : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SuccessResponse]
            Preview a list of tables in an SQL schema
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/datasources/preview_sql_table_list",
            method="POST",
            json={
                "database": database,
                "engine": engine,
                "requestId": request_id,
                "schema": schema,
                "schemaPath": schema_path,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_document_transaction(
        self,
        *,
        marimo_session_id: str,
        changes: typing.Sequence[NotebookDocumentTransactionRequestChangesItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        changes : typing.Sequence[NotebookDocumentTransactionRequestChangesItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SuccessResponse]
            Apply a document transaction
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/document/transaction",
            method="POST",
            json={
                "changes": convert_and_respect_annotation_metadata(
                    object_=changes,
                    annotation=typing.Sequence[NotebookDocumentTransactionRequestChangesItem],
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_api_documentation_snippets(
        self, *, marimo_session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Snippets]:
        """
        Parameters
        ----------
        marimo_session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Snippets]
            Load the snippets for the documentation page
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/documentation/snippets",
            method="GET",
            headers={
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Snippets,
                    parse_obj_as(
                        type_=Snippets,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_api_environment(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetApiEnvironmentResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetApiEnvironmentResponse]
            Environment information for issue reporting
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/environment",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetApiEnvironmentResponse,
                    parse_obj_as(
                        type_=GetApiEnvironmentResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_export_auto_export_html(
        self,
        *,
        marimo_session_id: str,
        download: bool,
        files: typing.Sequence[str],
        include_code: bool,
        asset_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        download : bool

        files : typing.Sequence[str]

        include_code : bool

        asset_url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SuccessResponse]
            Export the notebook as HTML
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/export/auto_export/html",
            method="POST",
            json={
                "assetUrl": asset_url,
                "download": download,
                "files": files,
                "includeCode": include_code,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def post_api_export_auto_export_ipynb(
        self, *, marimo_session_id: str, download: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        download : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SuccessResponse]
            Export the notebook as IPYNB
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/export/auto_export/ipynb",
            method="POST",
            json={
                "download": download,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def post_api_export_auto_export_markdown(
        self, *, marimo_session_id: str, download: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        download : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SuccessResponse]
            Export the notebook as a markdown
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/export/auto_export/markdown",
            method="POST",
            json={
                "download": download,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def get_api_export_availability(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ExportAvailabilityResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ExportAvailabilityResponse]
            Readiness for server-backed exports
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/export/availability",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExportAvailabilityResponse,
                    parse_obj_as(
                        type_=ExportAvailabilityResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_export_html(
        self,
        *,
        marimo_session_id: str,
        download: bool,
        files: typing.Sequence[str],
        include_code: bool,
        asset_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Parameters
        ----------
        marimo_session_id : str

        download : bool

        files : typing.Sequence[str]

        include_code : bool

        asset_url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Export the notebook as HTML
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/export/html",
            method="POST",
            json={
                "assetUrl": asset_url,
                "download": download,
                "files": files,
                "includeCode": include_code,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def post_api_export_ipynb(
        self,
        *,
        marimo_session_id: str,
        download: bool,
        include_outputs: typing.Optional[bool] = OMIT,
        sort_mode: typing.Optional[ExportAsIpynbRequestSortMode] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Parameters
        ----------
        marimo_session_id : str

        download : bool

        include_outputs : typing.Optional[bool]

        sort_mode : typing.Optional[ExportAsIpynbRequestSortMode]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Export the notebook as IPYNB
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/export/ipynb",
            method="POST",
            json={
                "download": download,
                "includeOutputs": include_outputs,
                "sortMode": sort_mode,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def post_api_export_markdown(
        self,
        *,
        marimo_session_id: str,
        download: bool,
        flavor: typing.Optional[ExportAsMarkdownRequestFlavor] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Parameters
        ----------
        marimo_session_id : str

        download : bool

        flavor : typing.Optional[ExportAsMarkdownRequestFlavor]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Export the notebook as a markdown
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/export/markdown",
            method="POST",
            json={
                "download": download,
                "flavor": flavor,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    @contextlib.asynccontextmanager
    async def post_api_export_pdf(
        self,
        *,
        marimo_session_id: str,
        webpdf: bool,
        include_inputs: typing.Optional[bool] = OMIT,
        include_outputs: typing.Optional[bool] = OMIT,
        preset: typing.Optional[ExportAsPdfRequestPreset] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        Parameters
        ----------
        marimo_session_id : str

        webpdf : bool

        include_inputs : typing.Optional[bool]

        include_outputs : typing.Optional[bool]

        preset : typing.Optional[ExportAsPdfRequestPreset]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            Export the notebook as a PDF
        """
        async with self._client_wrapper.httpx_client.stream(
            "api/export/pdf",
            method="POST",
            json={
                "includeInputs": include_inputs,
                "includeOutputs": include_outputs,
                "preset": preset,
                "webpdf": webpdf,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return AsyncHttpResponse(
                            response=_response,
                            data=(_chunk async for _chunk in _response.aiter_bytes(chunk_size=_chunk_size)),
                        )
                    await _response.aread()
                    if _response.status_code == 400:
                        raise BadRequestError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Any,
                                parse_obj_as(
                                    type_=typing.Any,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 500:
                        raise InternalServerError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Any,
                                parse_obj_as(
                                    type_=typing.Any,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()

    async def post_api_export_requirements_install(
        self,
        *,
        marimo_session_id: str,
        format: InstallExportRequirementsRequestFormat,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ExportAvailabilityResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        format : InstallExportRequirementsRequestFormat

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ExportAvailabilityResponse]
            Updated readiness for server-backed exports
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/export/requirements/install",
            method="POST",
            json={
                "format": format,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExportAvailabilityResponse,
                    parse_obj_as(
                        type_=ExportAvailabilityResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_export_script(
        self, *, marimo_session_id: str, download: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[str]:
        """
        Parameters
        ----------
        marimo_session_id : str

        download : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Export the notebook as a script
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/export/script",
            method="POST",
            json={
                "download": download,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def post_api_export_update_cell_outputs(
        self,
        *,
        marimo_session_id: str,
        cell_ids_to_output: typing.Dict[str, typing.Sequence[typing.Any]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        cell_ids_to_output : typing.Dict[str, typing.Sequence[typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SuccessResponse]
            Update the cell outputs
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/export/update_cell_outputs",
            method="POST",
            json={
                "cellIdsToOutput": cell_ids_to_output,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def post_api_files_copy(
        self, *, new_path: str, path: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[FileCopyResponse]:
        """
        Parameters
        ----------
        new_path : str

        path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FileCopyResponse]
            Copy a file or directory
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/files/copy",
            method="POST",
            json={
                "newPath": new_path,
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
                    FileCopyResponse,
                    parse_obj_as(
                        type_=FileCopyResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_files_create(
        self,
        *,
        name: str,
        path: str,
        type: PostApiFilesCreateRequestType,
        file: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FileCreateResponse]:
        """
        Parameters
        ----------
        name : str

        path : str

        type : PostApiFilesCreateRequestType

        file : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FileCreateResponse]
            Create a new file or directory
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/files/create",
            method="POST",
            data={
                "file": file,
                "name": name,
                "path": path,
                "type": type,
            },
            files={},
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FileCreateResponse,
                    parse_obj_as(
                        type_=FileCreateResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_files_delete(
        self, *, path: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[FileDeleteResponse]:
        """
        Parameters
        ----------
        path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FileDeleteResponse]
            Delete a file or directory
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/files/delete",
            method="POST",
            json={
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
                    FileDeleteResponse,
                    parse_obj_as(
                        type_=FileDeleteResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    @contextlib.asynccontextmanager
    async def get_api_files_download(
        self, *, path: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        Parameters
        ----------
        path : str
            Path of the file to download

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            Stream the file as an attachment
        """
        async with self._client_wrapper.httpx_client.stream(
            "api/files/download",
            method="GET",
            params={
                "path": path,
            },
            request_options=request_options,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return AsyncHttpResponse(
                            response=_response,
                            data=(_chunk async for _chunk in _response.aiter_bytes(chunk_size=_chunk_size)),
                        )
                    await _response.aread()
                    if _response.status_code == 400:
                        raise BadRequestError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Any,
                                parse_obj_as(
                                    type_=typing.Any,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 403:
                        raise ForbiddenError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Any,
                                parse_obj_as(
                                    type_=typing.Any,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Any,
                                parse_obj_as(
                                    type_=typing.Any,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()

    async def post_api_files_file_details(
        self,
        *,
        path: str,
        max_bytes: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FileDetailsResponse]:
        """
        Parameters
        ----------
        path : str

        max_bytes : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FileDetailsResponse]
            Get details of a specific file or directory
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/files/file_details",
            method="POST",
            json={
                "maxBytes": max_bytes,
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
                    FileDetailsResponse,
                    parse_obj_as(
                        type_=FileDetailsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_files_list_files(
        self, *, path: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[FileListResponse]:
        """
        Parameters
        ----------
        path : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FileListResponse]
            List files and directories in a given path
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/files/list_files",
            method="POST",
            json={
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
                    FileListResponse,
                    parse_obj_as(
                        type_=FileListResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_files_move(
        self, *, new_path: str, path: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[FileMoveResponse]:
        """
        Parameters
        ----------
        new_path : str

        path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FileMoveResponse]
            Move a file or directory
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/files/move",
            method="POST",
            json={
                "newPath": new_path,
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
                    FileMoveResponse,
                    parse_obj_as(
                        type_=FileMoveResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_files_open(
        self,
        *,
        path: str,
        line_number: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BaseResponse]:
        """
        Parameters
        ----------
        path : str

        line_number : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BaseResponse]
            Open a file in the system editor
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/files/open",
            method="POST",
            json={
                "lineNumber": line_number,
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
                    BaseResponse,
                    parse_obj_as(
                        type_=BaseResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_files_search(
        self,
        *,
        query: str,
        depth: typing.Optional[int] = OMIT,
        include_directories: typing.Optional[bool] = OMIT,
        include_files: typing.Optional[bool] = OMIT,
        limit: typing.Optional[int] = OMIT,
        path: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FileSearchResponse]:
        """
        Parameters
        ----------
        query : str

        depth : typing.Optional[int]

        include_directories : typing.Optional[bool]

        include_files : typing.Optional[bool]

        limit : typing.Optional[int]

        path : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FileSearchResponse]
            Search for files and directories matching a query
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/files/search",
            method="POST",
            json={
                "depth": depth,
                "includeDirectories": include_directories,
                "includeFiles": include_files,
                "limit": limit,
                "path": path,
                "query": query,
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
                    FileSearchResponse,
                    parse_obj_as(
                        type_=FileSearchResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_files_update(
        self, *, contents: str, path: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[FileUpdateResponse]:
        """
        Parameters
        ----------
        contents : str

        path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FileUpdateResponse]
            Update a file or directory
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/files/update",
            method="POST",
            json={
                "contents": contents,
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
                    FileUpdateResponse,
                    parse_obj_as(
                        type_=FileUpdateResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_home_recent_files(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RecentFilesResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RecentFilesResponse]
            Get the recent files
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/home/recent_files",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RecentFilesResponse,
                    parse_obj_as(
                        type_=RecentFilesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_home_running_notebooks(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RunningNotebooksResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RunningNotebooksResponse]
            Get the running files
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/home/running_notebooks",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RunningNotebooksResponse,
                    parse_obj_as(
                        type_=RunningNotebooksResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_home_shutdown_session(
        self, *, session_id: SessionId, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RunningNotebooksResponse]:
        """
        Parameters
        ----------
        session_id : SessionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RunningNotebooksResponse]
            Shutdown the current session
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/home/shutdown_session",
            method="POST",
            json={
                "sessionId": session_id,
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
                    RunningNotebooksResponse,
                    parse_obj_as(
                        type_=RunningNotebooksResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_home_tutorial_open(
        self, *, tutorial_id: OpenTutorialRequestTutorialId, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoFile]:
        """
        Parameters
        ----------
        tutorial_id : OpenTutorialRequestTutorialId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoFile]
            Open a new tutorial
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/home/tutorial/open",
            method="POST",
            json={
                "tutorialId": convert_and_respect_annotation_metadata(
                    object_=tutorial_id, annotation=OpenTutorialRequestTutorialId, direction="write"
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
                    MarimoFile,
                    parse_obj_as(
                        type_=MarimoFile,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_home_workspace_files(
        self, *, include_markdown: typing.Optional[bool] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WorkspaceFilesResponse]:
        """
        Parameters
        ----------
        include_markdown : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WorkspaceFilesResponse]
            Get the files in the workspace
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/home/workspace_files",
            method="POST",
            json={
                "includeMarkdown": include_markdown,
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
                    WorkspaceFilesResponse,
                    parse_obj_as(
                        type_=WorkspaceFilesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_kernel_code_autocomplete(
        self,
        *,
        marimo_session_id: str,
        cell_id: CellId,
        document: str,
        id: RequestId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        cell_id : CellId

        document : str

        id : RequestId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SuccessResponse]
            Complete a code fragment
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/kernel/code_autocomplete",
            method="POST",
            json={
                "cellId": cell_id,
                "document": document,
                "id": id,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_kernel_copy(
        self,
        *,
        marimo_session_id: str,
        destination: str,
        source: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Parameters
        ----------
        marimo_session_id : str

        destination : str

        source : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Copy notebook
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/kernel/copy",
            method="POST",
            json={
                "destination": destination,
                "source": source,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_kernel_delete(
        self, *, marimo_session_id: str, cell_id: CellId, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        cell_id : CellId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SuccessResponse]
            Delete a cell
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/kernel/delete",
            method="POST",
            json={
                "cellId": cell_id,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_kernel_focus_cell(
        self, *, marimo_session_id: str, cell_id: CellId, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        cell_id : CellId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SuccessResponse]
            Focus a cell in kiosk-mode consumers
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/kernel/focus_cell",
            method="POST",
            json={
                "cellId": cell_id,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_kernel_format(
        self, *, codes: typing.Dict[str, str], line_length: int, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[FormatResponse]:
        """
        Parameters
        ----------
        codes : typing.Dict[str, str]

        line_length : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FormatResponse]
            Format code
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/kernel/format",
            method="POST",
            json={
                "codes": codes,
                "lineLength": line_length,
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
                    FormatResponse,
                    parse_obj_as(
                        type_=FormatResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_kernel_function_call(
        self,
        *,
        marimo_session_id: str,
        args: typing.Dict[str, typing.Any],
        function_call_id: RequestId,
        function_name: str,
        namespace: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        args : typing.Dict[str, typing.Any]

        function_call_id : RequestId

        function_name : str

        namespace : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SuccessResponse]
            Invoke an RPC
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/kernel/function_call",
            method="POST",
            json={
                "args": args,
                "functionCallId": function_call_id,
                "functionName": function_name,
                "namespace": namespace,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_kernel_install_missing_packages(
        self,
        *,
        marimo_session_id: str,
        manager: str,
        versions: typing.Dict[str, str],
        source: typing.Optional[InstallPackagesRequestSource] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        manager : str

        versions : typing.Dict[str, str]

        source : typing.Optional[InstallPackagesRequestSource]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SuccessResponse]
            Install missing packages
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/kernel/install_missing_packages",
            method="POST",
            json={
                "manager": manager,
                "source": source,
                "versions": versions,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_kernel_instantiate(
        self,
        *,
        marimo_session_id: str,
        object_ids: typing.Sequence[UiElementId],
        values: typing.Sequence[typing.Any],
        auto_run: typing.Optional[bool] = OMIT,
        codes: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        object_ids : typing.Sequence[UiElementId]

        values : typing.Sequence[typing.Any]

        auto_run : typing.Optional[bool]

        codes : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SuccessResponse]
            Instantiate a component. Only allowed in edit mode; in run mode, instantiation happens server-side automatically.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/kernel/instantiate",
            method="POST",
            json={
                "autoRun": auto_run,
                "codes": codes,
                "objectIds": object_ids,
                "values": values,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_kernel_interrupt(
        self, *, marimo_session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SuccessResponse]
            Interrupt the kernel's execution
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/kernel/interrupt",
            method="POST",
            headers={
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_kernel_pdb_breakpoints(
        self,
        *,
        marimo_session_id: str,
        breakpoints: typing.Dict[str, typing.Sequence[int]],
        request: typing.Optional[HttpRequest] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        breakpoints : typing.Dict[str, typing.Sequence[int]]

        request : typing.Optional[HttpRequest]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SuccessResponse]
            Set the live debugger's breakpoints for the session.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/kernel/pdb/breakpoints",
            method="POST",
            json={
                "breakpoints": breakpoints,
                "request": convert_and_respect_annotation_metadata(
                    object_=request, annotation=typing.Optional[HttpRequest], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_kernel_pdb_pm(
        self,
        *,
        marimo_session_id: str,
        cell_id: CellId,
        request: typing.Optional[HttpRequest] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        cell_id : CellId

        request : typing.Optional[HttpRequest]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SuccessResponse]
            Run a post mortem on the most recent failed cell.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/kernel/pdb/pm",
            method="POST",
            json={
                "cellId": cell_id,
                "request": convert_and_respect_annotation_metadata(
                    object_=request, annotation=typing.Optional[HttpRequest], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_kernel_read_code(
        self, *, marimo_session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ReadCodeResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ReadCodeResponse]
            Read the code from the server
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/kernel/read_code",
            method="POST",
            headers={
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ReadCodeResponse,
                    parse_obj_as(
                        type_=ReadCodeResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def post_api_kernel_rename(
        self, *, marimo_session_id: str, filename: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        filename : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SuccessResponse]
            Rename the current app
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/kernel/rename",
            method="POST",
            json={
                "filename": filename,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_kernel_restart_session(
        self, *, marimo_session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SuccessResponse]
            Restart the current session without affecting other sessions.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/kernel/restart_session",
            method="POST",
            headers={
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_kernel_run(
        self,
        *,
        marimo_session_id: str,
        cell_ids: typing.Sequence[CellId],
        codes: typing.Sequence[str],
        request: typing.Optional[HttpRequest] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        cell_ids : typing.Sequence[CellId]

        codes : typing.Sequence[str]

        request : typing.Optional[HttpRequest]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SuccessResponse]
            Run a cell. Updates cell code in the kernel if needed; registers new cells for unseen cell IDs. Only allowed in edit mode.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/kernel/run",
            method="POST",
            json={
                "cellIds": cell_ids,
                "codes": codes,
                "request": convert_and_respect_annotation_metadata(
                    object_=request, annotation=typing.Optional[HttpRequest], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_kernel_save(
        self,
        *,
        marimo_session_id: str,
        cell_ids: typing.Sequence[CellId],
        codes: typing.Sequence[str],
        configs: typing.Sequence[CellConfig],
        filename: str,
        names: typing.Sequence[str],
        layout: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        persist: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Parameters
        ----------
        marimo_session_id : str

        cell_ids : typing.Sequence[CellId]

        codes : typing.Sequence[str]

        configs : typing.Sequence[CellConfig]

        filename : str

        names : typing.Sequence[str]

        layout : typing.Optional[typing.Dict[str, typing.Any]]

        persist : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Save the current app
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/kernel/save",
            method="POST",
            json={
                "cellIds": cell_ids,
                "codes": codes,
                "configs": convert_and_respect_annotation_metadata(
                    object_=configs, annotation=typing.Sequence[CellConfig], direction="write"
                ),
                "filename": filename,
                "layout": layout,
                "names": names,
                "persist": persist,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_kernel_save_app_config(
        self,
        *,
        marimo_session_id: str,
        config: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Parameters
        ----------
        marimo_session_id : str

        config : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Save the app configuration
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/kernel/save_app_config",
            method="POST",
            json={
                "config": config,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_kernel_save_user_config(
        self,
        *,
        config: typing.Dict[str, typing.Any],
        marimo_session_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        config : typing.Dict[str, typing.Any]

        marimo_session_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SuccessResponse]
            Update the user config on disk and in the kernel. Only allowed in edit mode.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/kernel/save_user_config",
            method="POST",
            json={
                "config": config,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_kernel_scratchpad_run(
        self,
        *,
        marimo_session_id: str,
        code: str,
        cell_outputs: typing.Optional[CellOutputs] = OMIT,
        notebook_cells: typing.Optional[typing.Sequence[NotebookCell]] = OMIT,
        request: typing.Optional[HttpRequest] = OMIT,
        run_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        code : str

        cell_outputs : typing.Optional[CellOutputs]

        notebook_cells : typing.Optional[typing.Sequence[NotebookCell]]

        request : typing.Optional[HttpRequest]

        run_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SuccessResponse]
            Run the scratchpad
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/kernel/scratchpad/run",
            method="POST",
            json={
                "cellOutputs": convert_and_respect_annotation_metadata(
                    object_=cell_outputs, annotation=typing.Optional[CellOutputs], direction="write"
                ),
                "code": code,
                "notebookCells": convert_and_respect_annotation_metadata(
                    object_=notebook_cells, annotation=typing.Optional[typing.Sequence[NotebookCell]], direction="write"
                ),
                "request": convert_and_respect_annotation_metadata(
                    object_=request, annotation=typing.Optional[HttpRequest], direction="write"
                ),
                "runId": run_id,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_kernel_set_cell_config(
        self,
        *,
        marimo_session_id: str,
        configs: typing.Dict[str, typing.Dict[str, typing.Any]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        configs : typing.Dict[str, typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SuccessResponse]
            Set the configuration of a cell
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/kernel/set_cell_config",
            method="POST",
            json={
                "configs": configs,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_kernel_set_model_value(
        self,
        *,
        marimo_session_id: str,
        buffers: typing.Sequence[Base64String],
        message: ModelRequestMessage,
        model_id: WidgetModelId,
        token: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        buffers : typing.Sequence[Base64String]

        message : ModelRequestMessage

        model_id : WidgetModelId

        token : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SuccessResponse]
            Set model value
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/kernel/set_model_value",
            method="POST",
            json={
                "buffers": buffers,
                "message": convert_and_respect_annotation_metadata(
                    object_=message, annotation=ModelRequestMessage, direction="write"
                ),
                "modelId": model_id,
                "token": token,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_kernel_set_ui_element_value(
        self,
        *,
        marimo_session_id: str,
        object_ids: typing.Sequence[UiElementId],
        values: typing.Sequence[typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        object_ids : typing.Sequence[UiElementId]

        values : typing.Sequence[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SuccessResponse]
            Set UI element values
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/kernel/set_ui_element_value",
            method="POST",
            json={
                "objectIds": object_ids,
                "values": values,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_kernel_shutdown(
        self, *, marimo_session_id: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SuccessResponse]
            Shutdown the kernel
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/kernel/shutdown",
            method="POST",
            headers={
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_api_kernel_status(
        self, *, marimo_session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[KernelStatusResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[KernelStatusResponse]
            Report whether the kernel is currently executing. `running` means at least one cell is queued or running; `idle` means the kernel is alive but not executing; `stopped` means the kernel process is not running.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/kernel/status",
            method="GET",
            headers={
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    KernelStatusResponse,
                    parse_obj_as(
                        type_=KernelStatusResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_kernel_stdin(
        self, *, marimo_session_id: str, text: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        text : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SuccessResponse]
            Send input to the stdin stream
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/kernel/stdin",
            method="POST",
            json={
                "text": text,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_kernel_takeover(
        self, *, marimo_session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PostApiKernelTakeoverResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostApiKernelTakeoverResponse]
            Successfully closed existing sessions
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/kernel/takeover",
            method="POST",
            headers={
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostApiKernelTakeoverResponse,
                    parse_obj_as(
                        type_=PostApiKernelTakeoverResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_api_lsp_health(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[LspHealthResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[LspHealthResponse]
            Get health status of all LSP servers
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/lsp/health",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LspHealthResponse,
                    parse_obj_as(
                        type_=LspHealthResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_lsp_restart(
        self,
        *,
        server_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[LspRestartResponse]:
        """
        Parameters
        ----------
        server_ids : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[LspRestartResponse]
            Restart LSP servers
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/lsp/restart",
            method="POST",
            json={
                "serverIds": server_ids,
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
                    LspRestartResponse,
                    parse_obj_as(
                        type_=LspRestartResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_packages_add(
        self,
        *,
        package: str,
        group: typing.Optional[str] = OMIT,
        upgrade: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PackageOperationResponse]:
        """
        Parameters
        ----------
        package : str

        group : typing.Optional[str]

        upgrade : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PackageOperationResponse]
            Install package
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/packages/add",
            method="POST",
            json={
                "group": group,
                "package": package,
                "upgrade": upgrade,
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
                    PackageOperationResponse,
                    parse_obj_as(
                        type_=PackageOperationResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_api_packages_list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListPackagesResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListPackagesResponse]
            List installed packages
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/packages/list",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListPackagesResponse,
                    parse_obj_as(
                        type_=ListPackagesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_packages_remove(
        self,
        *,
        package: str,
        group: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PackageOperationResponse]:
        """
        Parameters
        ----------
        package : str

        group : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PackageOperationResponse]
            Uninstall package
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/packages/remove",
            method="POST",
            json={
                "group": group,
                "package": package,
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
                    PackageOperationResponse,
                    parse_obj_as(
                        type_=PackageOperationResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_api_packages_tree(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DependencyTreeResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DependencyTreeResponse]
            List dependency tree
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/packages/tree",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DependencyTreeResponse,
                    parse_obj_as(
                        type_=DependencyTreeResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_secrets_create(
        self,
        *,
        marimo_session_id: str,
        key: str,
        name: str,
        provider: CreateSecretRequestProvider,
        value: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BaseResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        key : str

        name : str

        provider : CreateSecretRequestProvider

        value : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BaseResponse]
            Create a secret
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/secrets/create",
            method="POST",
            json={
                "key": key,
                "name": name,
                "provider": provider,
                "value": value,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BaseResponse,
                    parse_obj_as(
                        type_=BaseResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_secrets_delete(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[BaseResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BaseResponse]
            Delete a secret
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/secrets/delete",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BaseResponse,
                    parse_obj_as(
                        type_=BaseResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_secrets_keys(
        self, *, marimo_session_id: str, request_id: RequestId, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListSecretKeysResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        request_id : RequestId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListSecretKeysResponse]
            List all secret keys
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/secrets/keys",
            method="POST",
            json={
                "requestId": request_id,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListSecretKeysResponse,
                    parse_obj_as(
                        type_=ListSecretKeysResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_sql_validate(
        self,
        *,
        marimo_session_id: str,
        only_parse: bool,
        query: str,
        request_id: RequestId,
        dialect: typing.Optional[str] = OMIT,
        engine: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        only_parse : bool

        query : str

        request_id : RequestId

        dialect : typing.Optional[str]

        engine : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SuccessResponse]
            Validate an SQL query
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/sql/validate",
            method="POST",
            json={
                "dialect": dialect,
                "engine": engine,
                "onlyParse": only_parse,
                "query": query,
                "requestId": request_id,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_api_status(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetApiStatusResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetApiStatusResponse]
            Get the status of the application
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/status",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetApiStatusResponse,
                    parse_obj_as(
                        type_=GetApiStatusResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_api_status_connections(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetApiStatusConnectionsResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetApiStatusConnectionsResponse]
            Get the number of active websocket connections
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/status/connections",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetApiStatusConnectionsResponse,
                    parse_obj_as(
                        type_=GetApiStatusConnectionsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_storage_download(
        self,
        *,
        marimo_session_id: str,
        namespace: str,
        path: str,
        request_id: RequestId,
        preview: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        namespace : str

        path : str

        request_id : RequestId

        preview : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SuccessResponse]
            Download a storage entry
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/storage/download",
            method="POST",
            json={
                "namespace": namespace,
                "path": path,
                "preview": preview,
                "requestId": request_id,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_storage_list_entries(
        self,
        *,
        marimo_session_id: str,
        limit: int,
        namespace: str,
        request_id: RequestId,
        page_token: typing.Optional[str] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SuccessResponse]:
        """
        Parameters
        ----------
        marimo_session_id : str

        limit : int

        namespace : str

        request_id : RequestId

        page_token : typing.Optional[str]

        prefix : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SuccessResponse]
            List storage entries at a prefix
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/storage/list_entries",
            method="POST",
            json={
                "limit": limit,
                "namespace": namespace,
                "pageToken": page_token,
                "prefix": prefix,
                "requestId": request_id,
            },
            headers={
                "content-type": "application/json",
                "Marimo-Session-Id": str(marimo_session_id) if marimo_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_api_usage(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetApiUsageResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetApiUsageResponse]
            Get the current memory and CPU usage of the application
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/usage",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetApiUsageResponse,
                    parse_obj_as(
                        type_=GetApiUsageResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_api_version(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Get the version of the application
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/version",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
