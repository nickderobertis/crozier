

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .raw_client import AsyncRawFernApi, RawFernApi
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

if typing.TYPE_CHECKING:
    from .auth.client import AsyncAuthClient, AuthClient

OMIT = typing.cast(typing.Any, ...)


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : str
        The base url to use for requests from the client.

    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    max_retries : typing.Optional[int]
        The default maximum number of retries for failed requests. Defaults to 2. Per-request `max_retries` in `request_options` takes precedence over this value.

    stream_reconnection_enabled : typing.Optional[bool]
        Whether to automatically reconnect on stream disconnection for resumable streaming endpoints. Defaults to True. Per-request `stream_reconnection_enabled` in `request_options` takes precedence over this value.

    max_stream_reconnection_attempts : typing.Optional[int]
        The maximum number of reconnection attempts for resumable streaming endpoints. Defaults to no limit. Per-request `max_stream_reconnection_attempts` in `request_options` takes precedence over this value.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    logging : typing.Optional[typing.Union[LogConfig, Logger]]
        Configure logging for the SDK. Accepts a LogConfig dict with 'level' (debug/info/warn/error), 'logger' (custom logger implementation), and 'silent' (boolean, defaults to True) fields. You can also pass a pre-configured Logger instance.

    Examples
    --------
    from fern import FernApi

    client = FernApi(
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        _defaulted_max_retries = max_retries if max_retries is not None else 2
        self._client_wrapper = SyncClientWrapper(
            base_url=base_url,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
            max_retries=_defaulted_max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
        )
        self._raw_client = RawFernApi(client_wrapper=self._client_wrapper)
        self._auth: typing.Optional[AuthClient] = None

    @property
    def with_raw_response(self) -> RawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFernApi
        """
        return self._raw_client

    def get_file_filename_and_length(
        self, filename_and_length: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        filename_and_length : str
            The filename and byte length of the virtual file

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Get a virtual file

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_file_filename_and_length(
            filename_and_length="filename_and_length",
        )
        """
        with self._raw_client.get_file_filename_and_length(filename_and_length, request_options=request_options) as r:
            yield from r.data

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
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_ai_chat(
            marimo_session_id="Marimo-Session-Id",
            include_other_code="includeOtherCode",
            ui_messages=[{"key": "value"}],
        )
        """
        _response = self._raw_client.post_api_ai_chat(
            marimo_session_id=marimo_session_id,
            include_other_code=include_other_code,
            ui_messages=ui_messages,
            model=model,
            options=options,
            tools=tools,
            variables=variables,
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.Dict[str, typing.Any]:
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
        typing.Dict[str, typing.Any]
            Get AI completion for a prompt

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_ai_completion(
            marimo_session_id="Marimo-Session-Id",
            code="code",
            include_other_code="includeOtherCode",
            prompt="prompt",
        )
        """
        _response = self._raw_client.post_api_ai_completion(
            marimo_session_id=marimo_session_id,
            code=code,
            include_other_code=include_other_code,
            prompt=prompt,
            context=context,
            language=language,
            selected_text=selected_text,
            ui_messages=ui_messages,
            request_options=request_options,
        )
        return _response.data

    def post_api_ai_inline_completion(
        self,
        *,
        marimo_session_id: str,
        prefix: str,
        suffix: str,
        language: typing.Optional[AiInlineCompletionRequestLanguage] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
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
        str
            Get AI inline completion for code

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_ai_inline_completion(
            marimo_session_id="marimoSessionId",
            prefix="prefix",
            suffix="suffix",
        )
        """
        _response = self._raw_client.post_api_ai_inline_completion(
            marimo_session_id=marimo_session_id,
            prefix=prefix,
            suffix=suffix,
            language=language,
            request_options=request_options,
        )
        return _response.data

    def post_api_ai_invoke_tool(
        self,
        *,
        marimo_session_id: str,
        arguments: typing.Dict[str, typing.Any],
        tool_name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InvokeAiToolResponse:
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
        InvokeAiToolResponse
            Tool invocation result

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_ai_invoke_tool(
            marimo_session_id="Marimo-Session-Id",
            arguments={"key": "value"},
            tool_name="toolName",
        )
        """
        _response = self._raw_client.post_api_ai_invoke_tool(
            marimo_session_id=marimo_session_id,
            arguments=arguments,
            tool_name=tool_name,
            request_options=request_options,
        )
        return _response.data

    def post_api_ai_mcp_refresh(
        self, *, marimo_session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> McpRefreshResponse:
        """
        Parameters
        ----------
        marimo_session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        McpRefreshResponse
            Refresh MCP server configuration

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_ai_mcp_refresh(
            marimo_session_id="Marimo-Session-Id",
        )
        """
        _response = self._raw_client.post_api_ai_mcp_refresh(
            marimo_session_id=marimo_session_id, request_options=request_options
        )
        return _response.data

    def get_api_ai_mcp_status(self, *, request_options: typing.Optional[RequestOptions] = None) -> McpStatusResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        McpStatusResponse
            Get MCP server status

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_api_ai_mcp_status()
        """
        _response = self._raw_client.get_api_ai_mcp_status(request_options=request_options)
        return _response.data

    def post_api_cache_clear(
        self, *, marimo_session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SuccessResponse:
        """
        Parameters
        ----------
        marimo_session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Clear all caches

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_cache_clear(
            marimo_session_id="Marimo-Session-Id",
        )
        """
        _response = self._raw_client.post_api_cache_clear(
            marimo_session_id=marimo_session_id, request_options=request_options
        )
        return _response.data

    def post_api_cache_info(
        self, *, marimo_session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SuccessResponse:
        """
        Parameters
        ----------
        marimo_session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Get cache statistics

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_cache_info(
            marimo_session_id="Marimo-Session-Id",
        )
        """
        _response = self._raw_client.post_api_cache_info(
            marimo_session_id=marimo_session_id, request_options=request_options
        )
        return _response.data

    def post_api_datasources_discover(
        self, *, marimo_session_id: str, request_id: RequestId, request_options: typing.Optional[RequestOptions] = None
    ) -> SuccessResponse:
        """
        Parameters
        ----------
        marimo_session_id : str

        request_id : RequestId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Discover datasource connections

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_datasources_discover(
            marimo_session_id="Marimo-Session-Id",
            request_id="requestId",
        )
        """
        _response = self._raw_client.post_api_datasources_discover(
            marimo_session_id=marimo_session_id, request_id=request_id, request_options=request_options
        )
        return _response.data

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
    ) -> SuccessResponse:
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
        SuccessResponse
            Preview a column in a dataset

        Examples
        --------
        from fern import FernApi, PreviewDatasetColumnRequestSourceType

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_datasources_preview_column(
            marimo_session_id="Marimo-Session-Id",
            column_name="columnName",
            source="source",
            source_type=PreviewDatasetColumnRequestSourceType.CATALOG,
            table_name="tableName",
        )
        """
        _response = self._raw_client.post_api_datasources_preview_column(
            marimo_session_id=marimo_session_id,
            column_name=column_name,
            source=source,
            source_type=source_type,
            table_name=table_name,
            fully_qualified_table_name=fully_qualified_table_name,
            request_options=request_options,
        )
        return _response.data

    def post_api_datasources_preview_datasource_connection(
        self, *, marimo_session_id: str, engine: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SuccessResponse:
        """
        Parameters
        ----------
        marimo_session_id : str

        engine : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Broadcasts a datasource connection

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_datasources_preview_datasource_connection(
            marimo_session_id="Marimo-Session-Id",
            engine="engine",
        )
        """
        _response = self._raw_client.post_api_datasources_preview_datasource_connection(
            marimo_session_id=marimo_session_id, engine=engine, request_options=request_options
        )
        return _response.data

    def post_api_datasources_preview_sql_schema_list(
        self,
        *,
        marimo_session_id: str,
        database: str,
        engine: str,
        request_id: RequestId,
        schema_path: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SuccessResponse:
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
        SuccessResponse
            Preview a list of schemas in an SQL database

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_datasources_preview_sql_schema_list(
            marimo_session_id="Marimo-Session-Id",
            database="database",
            engine="engine",
            request_id="requestId",
        )
        """
        _response = self._raw_client.post_api_datasources_preview_sql_schema_list(
            marimo_session_id=marimo_session_id,
            database=database,
            engine=engine,
            request_id=request_id,
            schema_path=schema_path,
            request_options=request_options,
        )
        return _response.data

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
    ) -> SuccessResponse:
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
        SuccessResponse
            Preview a SQL table

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_datasources_preview_sql_table(
            marimo_session_id="Marimo-Session-Id",
            database="database",
            engine="engine",
            request_id="requestId",
            schema="schema",
            table_name="tableName",
        )
        """
        _response = self._raw_client.post_api_datasources_preview_sql_table(
            marimo_session_id=marimo_session_id,
            database=database,
            engine=engine,
            request_id=request_id,
            schema=schema,
            table_name=table_name,
            schema_path=schema_path,
            request_options=request_options,
        )
        return _response.data

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
    ) -> SuccessResponse:
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
        SuccessResponse
            Preview a list of tables in an SQL schema

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_datasources_preview_sql_table_list(
            marimo_session_id="Marimo-Session-Id",
            database="database",
            engine="engine",
            request_id="requestId",
            schema="schema",
        )
        """
        _response = self._raw_client.post_api_datasources_preview_sql_table_list(
            marimo_session_id=marimo_session_id,
            database=database,
            engine=engine,
            request_id=request_id,
            schema=schema,
            schema_path=schema_path,
            request_options=request_options,
        )
        return _response.data

    def post_api_document_transaction(
        self,
        *,
        marimo_session_id: str,
        changes: typing.Sequence[NotebookDocumentTransactionRequestChangesItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SuccessResponse:
        """
        Parameters
        ----------
        marimo_session_id : str

        changes : typing.Sequence[NotebookDocumentTransactionRequestChangesItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Apply a document transaction

        Examples
        --------
        from fern import CellConfig, CreateCell, CreateCellType, FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_document_transaction(
            marimo_session_id="Marimo-Session-Id",
            changes=[
                CreateCell(
                    cell_id="cellId",
                    code="code",
                    config=CellConfig(),
                    name="name",
                    type=CreateCellType.CREATE_CELL,
                )
            ],
        )
        """
        _response = self._raw_client.post_api_document_transaction(
            marimo_session_id=marimo_session_id, changes=changes, request_options=request_options
        )
        return _response.data

    def get_api_documentation_snippets(
        self, *, marimo_session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Snippets:
        """
        Parameters
        ----------
        marimo_session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Snippets
            Load the snippets for the documentation page

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_api_documentation_snippets(
            marimo_session_id="Marimo-Session-Id",
        )
        """
        _response = self._raw_client.get_api_documentation_snippets(
            marimo_session_id=marimo_session_id, request_options=request_options
        )
        return _response.data

    def get_api_environment(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetApiEnvironmentResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApiEnvironmentResponse
            Environment information for issue reporting

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_api_environment()
        """
        _response = self._raw_client.get_api_environment(request_options=request_options)
        return _response.data

    def post_api_export_auto_export_html(
        self,
        *,
        marimo_session_id: str,
        download: bool,
        files: typing.Sequence[str],
        include_code: bool,
        asset_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SuccessResponse:
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
        SuccessResponse
            Export the notebook as HTML

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_export_auto_export_html(
            marimo_session_id="Marimo-Session-Id",
            download=True,
            files=["files"],
            include_code=True,
        )
        """
        _response = self._raw_client.post_api_export_auto_export_html(
            marimo_session_id=marimo_session_id,
            download=download,
            files=files,
            include_code=include_code,
            asset_url=asset_url,
            request_options=request_options,
        )
        return _response.data

    def post_api_export_auto_export_ipynb(
        self, *, marimo_session_id: str, download: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> SuccessResponse:
        """
        Parameters
        ----------
        marimo_session_id : str

        download : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Export the notebook as IPYNB

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_export_auto_export_ipynb(
            marimo_session_id="Marimo-Session-Id",
            download=True,
        )
        """
        _response = self._raw_client.post_api_export_auto_export_ipynb(
            marimo_session_id=marimo_session_id, download=download, request_options=request_options
        )
        return _response.data

    def post_api_export_auto_export_markdown(
        self, *, marimo_session_id: str, download: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> SuccessResponse:
        """
        Parameters
        ----------
        marimo_session_id : str

        download : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Export the notebook as a markdown

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_export_auto_export_markdown(
            marimo_session_id="Marimo-Session-Id",
            download=True,
        )
        """
        _response = self._raw_client.post_api_export_auto_export_markdown(
            marimo_session_id=marimo_session_id, download=download, request_options=request_options
        )
        return _response.data

    def get_api_export_availability(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ExportAvailabilityResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportAvailabilityResponse
            Readiness for server-backed exports

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_api_export_availability()
        """
        _response = self._raw_client.get_api_export_availability(request_options=request_options)
        return _response.data

    def post_api_export_html(
        self,
        *,
        marimo_session_id: str,
        download: bool,
        files: typing.Sequence[str],
        include_code: bool,
        asset_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
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
        str
            Export the notebook as HTML

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_export_html(
            marimo_session_id="marimoSessionId",
            download=True,
            files=["files", "files"],
            include_code=True,
        )
        """
        _response = self._raw_client.post_api_export_html(
            marimo_session_id=marimo_session_id,
            download=download,
            files=files,
            include_code=include_code,
            asset_url=asset_url,
            request_options=request_options,
        )
        return _response.data

    def post_api_export_ipynb(
        self,
        *,
        marimo_session_id: str,
        download: bool,
        include_outputs: typing.Optional[bool] = OMIT,
        sort_mode: typing.Optional[ExportAsIpynbRequestSortMode] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
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
        str
            Export the notebook as IPYNB

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_export_ipynb(
            marimo_session_id="marimoSessionId",
            download=True,
        )
        """
        _response = self._raw_client.post_api_export_ipynb(
            marimo_session_id=marimo_session_id,
            download=download,
            include_outputs=include_outputs,
            sort_mode=sort_mode,
            request_options=request_options,
        )
        return _response.data

    def post_api_export_markdown(
        self,
        *,
        marimo_session_id: str,
        download: bool,
        flavor: typing.Optional[ExportAsMarkdownRequestFlavor] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
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
        str
            Export the notebook as a markdown

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_export_markdown(
            marimo_session_id="marimoSessionId",
            download=True,
        )
        """
        _response = self._raw_client.post_api_export_markdown(
            marimo_session_id=marimo_session_id, download=download, flavor=flavor, request_options=request_options
        )
        return _response.data

    def post_api_export_pdf(
        self,
        *,
        marimo_session_id: str,
        webpdf: bool,
        include_inputs: typing.Optional[bool] = OMIT,
        include_outputs: typing.Optional[bool] = OMIT,
        preset: typing.Optional[ExportAsPdfRequestPreset] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
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
        typing.Iterator[bytes]
            Export the notebook as a PDF

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_export_pdf(
            marimo_session_id="marimoSessionId",
            webpdf=True,
        )
        """
        with self._raw_client.post_api_export_pdf(
            marimo_session_id=marimo_session_id,
            webpdf=webpdf,
            include_inputs=include_inputs,
            include_outputs=include_outputs,
            preset=preset,
            request_options=request_options,
        ) as r:
            yield from r.data

    def post_api_export_requirements_install(
        self,
        *,
        marimo_session_id: str,
        format: InstallExportRequirementsRequestFormat,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExportAvailabilityResponse:
        """
        Parameters
        ----------
        marimo_session_id : str

        format : InstallExportRequirementsRequestFormat

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportAvailabilityResponse
            Updated readiness for server-backed exports

        Examples
        --------
        from fern import FernApi, InstallExportRequirementsRequestFormat

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_export_requirements_install(
            marimo_session_id="Marimo-Session-Id",
            format=InstallExportRequirementsRequestFormat.HTML,
        )
        """
        _response = self._raw_client.post_api_export_requirements_install(
            marimo_session_id=marimo_session_id, format=format, request_options=request_options
        )
        return _response.data

    def post_api_export_script(
        self, *, marimo_session_id: str, download: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        marimo_session_id : str

        download : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Export the notebook as a script

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_export_script(
            marimo_session_id="marimoSessionId",
            download=True,
        )
        """
        _response = self._raw_client.post_api_export_script(
            marimo_session_id=marimo_session_id, download=download, request_options=request_options
        )
        return _response.data

    def post_api_export_update_cell_outputs(
        self,
        *,
        marimo_session_id: str,
        cell_ids_to_output: typing.Dict[str, typing.Sequence[typing.Any]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SuccessResponse:
        """
        Parameters
        ----------
        marimo_session_id : str

        cell_ids_to_output : typing.Dict[str, typing.Sequence[typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Update the cell outputs

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_export_update_cell_outputs(
            marimo_session_id="Marimo-Session-Id",
            cell_ids_to_output={"key": []},
        )
        """
        _response = self._raw_client.post_api_export_update_cell_outputs(
            marimo_session_id=marimo_session_id, cell_ids_to_output=cell_ids_to_output, request_options=request_options
        )
        return _response.data

    def post_api_files_copy(
        self, *, new_path: str, path: str, request_options: typing.Optional[RequestOptions] = None
    ) -> FileCopyResponse:
        """
        Parameters
        ----------
        new_path : str

        path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileCopyResponse
            Copy a file or directory

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_files_copy(
            new_path="newPath",
            path="path",
        )
        """
        _response = self._raw_client.post_api_files_copy(new_path=new_path, path=path, request_options=request_options)
        return _response.data

    def post_api_files_create(
        self,
        *,
        name: str,
        path: str,
        type: PostApiFilesCreateRequestType,
        file: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FileCreateResponse:
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
        FileCreateResponse
            Create a new file or directory

        Examples
        --------
        from fern import FernApi, PostApiFilesCreateRequestType

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_files_create(
            name="name",
            path="path",
            type=PostApiFilesCreateRequestType.DIRECTORY,
        )
        """
        _response = self._raw_client.post_api_files_create(
            name=name, path=path, type=type, file=file, request_options=request_options
        )
        return _response.data

    def post_api_files_delete(
        self, *, path: str, request_options: typing.Optional[RequestOptions] = None
    ) -> FileDeleteResponse:
        """
        Parameters
        ----------
        path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileDeleteResponse
            Delete a file or directory

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_files_delete(
            path="path",
        )
        """
        _response = self._raw_client.post_api_files_delete(path=path, request_options=request_options)
        return _response.data

    def get_api_files_download(
        self, *, path: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        path : str
            Path of the file to download

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Stream the file as an attachment

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_api_files_download(
            path="path",
        )
        """
        with self._raw_client.get_api_files_download(path=path, request_options=request_options) as r:
            yield from r.data

    def post_api_files_file_details(
        self,
        *,
        path: str,
        max_bytes: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FileDetailsResponse:
        """
        Parameters
        ----------
        path : str

        max_bytes : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileDetailsResponse
            Get details of a specific file or directory

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_files_file_details(
            path="path",
        )
        """
        _response = self._raw_client.post_api_files_file_details(
            path=path, max_bytes=max_bytes, request_options=request_options
        )
        return _response.data

    def post_api_files_list_files(
        self, *, path: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> FileListResponse:
        """
        Parameters
        ----------
        path : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileListResponse
            List files and directories in a given path

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_files_list_files()
        """
        _response = self._raw_client.post_api_files_list_files(path=path, request_options=request_options)
        return _response.data

    def post_api_files_move(
        self, *, new_path: str, path: str, request_options: typing.Optional[RequestOptions] = None
    ) -> FileMoveResponse:
        """
        Parameters
        ----------
        new_path : str

        path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileMoveResponse
            Move a file or directory

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_files_move(
            new_path="newPath",
            path="path",
        )
        """
        _response = self._raw_client.post_api_files_move(new_path=new_path, path=path, request_options=request_options)
        return _response.data

    def post_api_files_open(
        self,
        *,
        path: str,
        line_number: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BaseResponse:
        """
        Parameters
        ----------
        path : str

        line_number : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseResponse
            Open a file in the system editor

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_files_open(
            path="path",
        )
        """
        _response = self._raw_client.post_api_files_open(
            path=path, line_number=line_number, request_options=request_options
        )
        return _response.data

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
    ) -> FileSearchResponse:
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
        FileSearchResponse
            Search for files and directories matching a query

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_files_search(
            query="query",
        )
        """
        _response = self._raw_client.post_api_files_search(
            query=query,
            depth=depth,
            include_directories=include_directories,
            include_files=include_files,
            limit=limit,
            path=path,
            request_options=request_options,
        )
        return _response.data

    def post_api_files_update(
        self, *, contents: str, path: str, request_options: typing.Optional[RequestOptions] = None
    ) -> FileUpdateResponse:
        """
        Parameters
        ----------
        contents : str

        path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileUpdateResponse
            Update a file or directory

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_files_update(
            contents="contents",
            path="path",
        )
        """
        _response = self._raw_client.post_api_files_update(
            contents=contents, path=path, request_options=request_options
        )
        return _response.data

    def post_api_home_recent_files(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RecentFilesResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecentFilesResponse
            Get the recent files

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_home_recent_files()
        """
        _response = self._raw_client.post_api_home_recent_files(request_options=request_options)
        return _response.data

    def post_api_home_running_notebooks(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RunningNotebooksResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RunningNotebooksResponse
            Get the running files

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_home_running_notebooks()
        """
        _response = self._raw_client.post_api_home_running_notebooks(request_options=request_options)
        return _response.data

    def post_api_home_shutdown_session(
        self, *, session_id: SessionId, request_options: typing.Optional[RequestOptions] = None
    ) -> RunningNotebooksResponse:
        """
        Parameters
        ----------
        session_id : SessionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RunningNotebooksResponse
            Shutdown the current session

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_home_shutdown_session(
            session_id="sessionId",
        )
        """
        _response = self._raw_client.post_api_home_shutdown_session(
            session_id=session_id, request_options=request_options
        )
        return _response.data

    def post_api_home_tutorial_open(
        self, *, tutorial_id: OpenTutorialRequestTutorialId, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoFile:
        """
        Parameters
        ----------
        tutorial_id : OpenTutorialRequestTutorialId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoFile
            Open a new tutorial

        Examples
        --------
        from fern import FernApi, OpenTutorialRequestTutorialIdZero

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_home_tutorial_open(
            tutorial_id=OpenTutorialRequestTutorialIdZero.DATAFLOW,
        )
        """
        _response = self._raw_client.post_api_home_tutorial_open(
            tutorial_id=tutorial_id, request_options=request_options
        )
        return _response.data

    def post_api_home_workspace_files(
        self, *, include_markdown: typing.Optional[bool] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkspaceFilesResponse:
        """
        Parameters
        ----------
        include_markdown : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceFilesResponse
            Get the files in the workspace

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_home_workspace_files()
        """
        _response = self._raw_client.post_api_home_workspace_files(
            include_markdown=include_markdown, request_options=request_options
        )
        return _response.data

    def post_api_kernel_code_autocomplete(
        self,
        *,
        marimo_session_id: str,
        cell_id: CellId,
        document: str,
        id: RequestId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SuccessResponse:
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
        SuccessResponse
            Complete a code fragment

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_kernel_code_autocomplete(
            marimo_session_id="Marimo-Session-Id",
            cell_id="cellId",
            document="document",
            id="id",
        )
        """
        _response = self._raw_client.post_api_kernel_code_autocomplete(
            marimo_session_id=marimo_session_id,
            cell_id=cell_id,
            document=document,
            id=id,
            request_options=request_options,
        )
        return _response.data

    def post_api_kernel_copy(
        self,
        *,
        marimo_session_id: str,
        destination: str,
        source: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
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
        str
            Copy notebook

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_kernel_copy(
            marimo_session_id="marimoSessionId",
            destination="destination",
            source="source",
        )
        """
        _response = self._raw_client.post_api_kernel_copy(
            marimo_session_id=marimo_session_id, destination=destination, source=source, request_options=request_options
        )
        return _response.data

    def post_api_kernel_delete(
        self, *, marimo_session_id: str, cell_id: CellId, request_options: typing.Optional[RequestOptions] = None
    ) -> SuccessResponse:
        """
        Parameters
        ----------
        marimo_session_id : str

        cell_id : CellId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Delete a cell

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_kernel_delete(
            marimo_session_id="Marimo-Session-Id",
            cell_id="cellId",
        )
        """
        _response = self._raw_client.post_api_kernel_delete(
            marimo_session_id=marimo_session_id, cell_id=cell_id, request_options=request_options
        )
        return _response.data

    def post_api_kernel_focus_cell(
        self, *, marimo_session_id: str, cell_id: CellId, request_options: typing.Optional[RequestOptions] = None
    ) -> SuccessResponse:
        """
        Parameters
        ----------
        marimo_session_id : str

        cell_id : CellId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Focus a cell in kiosk-mode consumers

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_kernel_focus_cell(
            marimo_session_id="Marimo-Session-Id",
            cell_id="cellId",
        )
        """
        _response = self._raw_client.post_api_kernel_focus_cell(
            marimo_session_id=marimo_session_id, cell_id=cell_id, request_options=request_options
        )
        return _response.data

    def post_api_kernel_format(
        self, *, codes: typing.Dict[str, str], line_length: int, request_options: typing.Optional[RequestOptions] = None
    ) -> FormatResponse:
        """
        Parameters
        ----------
        codes : typing.Dict[str, str]

        line_length : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FormatResponse
            Format code

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_kernel_format(
            codes={"key": "value"},
            line_length=1,
        )
        """
        _response = self._raw_client.post_api_kernel_format(
            codes=codes, line_length=line_length, request_options=request_options
        )
        return _response.data

    def post_api_kernel_function_call(
        self,
        *,
        marimo_session_id: str,
        args: typing.Dict[str, typing.Any],
        function_call_id: RequestId,
        function_name: str,
        namespace: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SuccessResponse:
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
        SuccessResponse
            Invoke an RPC

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_kernel_function_call(
            marimo_session_id="Marimo-Session-Id",
            args={"key": "value"},
            function_call_id="functionCallId",
            function_name="functionName",
            namespace="namespace",
        )
        """
        _response = self._raw_client.post_api_kernel_function_call(
            marimo_session_id=marimo_session_id,
            args=args,
            function_call_id=function_call_id,
            function_name=function_name,
            namespace=namespace,
            request_options=request_options,
        )
        return _response.data

    def post_api_kernel_install_missing_packages(
        self,
        *,
        marimo_session_id: str,
        manager: str,
        versions: typing.Dict[str, str],
        source: typing.Optional[InstallPackagesRequestSource] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SuccessResponse:
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
        SuccessResponse
            Install missing packages

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_kernel_install_missing_packages(
            marimo_session_id="Marimo-Session-Id",
            manager="manager",
            versions={"key": "value"},
        )
        """
        _response = self._raw_client.post_api_kernel_install_missing_packages(
            marimo_session_id=marimo_session_id,
            manager=manager,
            versions=versions,
            source=source,
            request_options=request_options,
        )
        return _response.data

    def post_api_kernel_instantiate(
        self,
        *,
        marimo_session_id: str,
        object_ids: typing.Sequence[UiElementId],
        values: typing.Sequence[typing.Any],
        auto_run: typing.Optional[bool] = OMIT,
        codes: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SuccessResponse:
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
        SuccessResponse
            Instantiate a component. Only allowed in edit mode; in run mode, instantiation happens server-side automatically.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_kernel_instantiate(
            marimo_session_id="Marimo-Session-Id",
            object_ids=["objectIds"],
            values=[],
        )
        """
        _response = self._raw_client.post_api_kernel_instantiate(
            marimo_session_id=marimo_session_id,
            object_ids=object_ids,
            values=values,
            auto_run=auto_run,
            codes=codes,
            request_options=request_options,
        )
        return _response.data

    def post_api_kernel_interrupt(
        self, *, marimo_session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SuccessResponse:
        """
        Parameters
        ----------
        marimo_session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Interrupt the kernel's execution

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_kernel_interrupt(
            marimo_session_id="Marimo-Session-Id",
        )
        """
        _response = self._raw_client.post_api_kernel_interrupt(
            marimo_session_id=marimo_session_id, request_options=request_options
        )
        return _response.data

    def post_api_kernel_pdb_breakpoints(
        self,
        *,
        marimo_session_id: str,
        breakpoints: typing.Dict[str, typing.Sequence[int]],
        request: typing.Optional[HttpRequest] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SuccessResponse:
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
        SuccessResponse
            Set the live debugger's breakpoints for the session.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_kernel_pdb_breakpoints(
            marimo_session_id="Marimo-Session-Id",
            breakpoints={"key": [1]},
        )
        """
        _response = self._raw_client.post_api_kernel_pdb_breakpoints(
            marimo_session_id=marimo_session_id,
            breakpoints=breakpoints,
            request=request,
            request_options=request_options,
        )
        return _response.data

    def post_api_kernel_pdb_pm(
        self,
        *,
        marimo_session_id: str,
        cell_id: CellId,
        request: typing.Optional[HttpRequest] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SuccessResponse:
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
        SuccessResponse
            Run a post mortem on the most recent failed cell.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_kernel_pdb_pm(
            marimo_session_id="Marimo-Session-Id",
            cell_id="cellId",
        )
        """
        _response = self._raw_client.post_api_kernel_pdb_pm(
            marimo_session_id=marimo_session_id, cell_id=cell_id, request=request, request_options=request_options
        )
        return _response.data

    def post_api_kernel_read_code(
        self, *, marimo_session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ReadCodeResponse:
        """
        Parameters
        ----------
        marimo_session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReadCodeResponse
            Read the code from the server

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_kernel_read_code(
            marimo_session_id="Marimo-Session-Id",
        )
        """
        _response = self._raw_client.post_api_kernel_read_code(
            marimo_session_id=marimo_session_id, request_options=request_options
        )
        return _response.data

    def post_api_kernel_rename(
        self, *, marimo_session_id: str, filename: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SuccessResponse:
        """
        Parameters
        ----------
        marimo_session_id : str

        filename : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Rename the current app

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_kernel_rename(
            marimo_session_id="Marimo-Session-Id",
            filename="filename",
        )
        """
        _response = self._raw_client.post_api_kernel_rename(
            marimo_session_id=marimo_session_id, filename=filename, request_options=request_options
        )
        return _response.data

    def post_api_kernel_restart_session(
        self, *, marimo_session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SuccessResponse:
        """
        Parameters
        ----------
        marimo_session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Restart the current session without affecting other sessions.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_kernel_restart_session(
            marimo_session_id="Marimo-Session-Id",
        )
        """
        _response = self._raw_client.post_api_kernel_restart_session(
            marimo_session_id=marimo_session_id, request_options=request_options
        )
        return _response.data

    def post_api_kernel_run(
        self,
        *,
        marimo_session_id: str,
        cell_ids: typing.Sequence[CellId],
        codes: typing.Sequence[str],
        request: typing.Optional[HttpRequest] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SuccessResponse:
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
        SuccessResponse
            Run a cell. Updates cell code in the kernel if needed; registers new cells for unseen cell IDs. Only allowed in edit mode.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_kernel_run(
            marimo_session_id="Marimo-Session-Id",
            cell_ids=["cellIds"],
            codes=["codes"],
        )
        """
        _response = self._raw_client.post_api_kernel_run(
            marimo_session_id=marimo_session_id,
            cell_ids=cell_ids,
            codes=codes,
            request=request,
            request_options=request_options,
        )
        return _response.data

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
    ) -> str:
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
        str
            Save the current app

        Examples
        --------
        from fern import CellConfig, FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_kernel_save(
            marimo_session_id="marimoSessionId",
            cell_ids=["cellIds", "cellIds"],
            codes=["codes", "codes"],
            configs=[CellConfig(), CellConfig()],
            filename="filename",
            names=["names", "names"],
        )
        """
        _response = self._raw_client.post_api_kernel_save(
            marimo_session_id=marimo_session_id,
            cell_ids=cell_ids,
            codes=codes,
            configs=configs,
            filename=filename,
            names=names,
            layout=layout,
            persist=persist,
            request_options=request_options,
        )
        return _response.data

    def post_api_kernel_save_app_config(
        self,
        *,
        marimo_session_id: str,
        config: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Parameters
        ----------
        marimo_session_id : str

        config : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Save the app configuration

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_kernel_save_app_config(
            marimo_session_id="marimoSessionId",
            config={"config": {"key": "value"}},
        )
        """
        _response = self._raw_client.post_api_kernel_save_app_config(
            marimo_session_id=marimo_session_id, config=config, request_options=request_options
        )
        return _response.data

    def post_api_kernel_save_user_config(
        self,
        *,
        config: typing.Dict[str, typing.Any],
        marimo_session_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SuccessResponse:
        """
        Parameters
        ----------
        config : typing.Dict[str, typing.Any]

        marimo_session_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Update the user config on disk and in the kernel. Only allowed in edit mode.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_kernel_save_user_config(
            config={"key": "value"},
        )
        """
        _response = self._raw_client.post_api_kernel_save_user_config(
            config=config, marimo_session_id=marimo_session_id, request_options=request_options
        )
        return _response.data

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
    ) -> SuccessResponse:
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
        SuccessResponse
            Run the scratchpad

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_kernel_scratchpad_run(
            marimo_session_id="Marimo-Session-Id",
            code="code",
        )
        """
        _response = self._raw_client.post_api_kernel_scratchpad_run(
            marimo_session_id=marimo_session_id,
            code=code,
            cell_outputs=cell_outputs,
            notebook_cells=notebook_cells,
            request=request,
            run_id=run_id,
            request_options=request_options,
        )
        return _response.data

    def post_api_kernel_set_cell_config(
        self,
        *,
        marimo_session_id: str,
        configs: typing.Dict[str, typing.Dict[str, typing.Any]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SuccessResponse:
        """
        Parameters
        ----------
        marimo_session_id : str

        configs : typing.Dict[str, typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Set the configuration of a cell

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_kernel_set_cell_config(
            marimo_session_id="Marimo-Session-Id",
            configs={"key": {"key": "value"}},
        )
        """
        _response = self._raw_client.post_api_kernel_set_cell_config(
            marimo_session_id=marimo_session_id, configs=configs, request_options=request_options
        )
        return _response.data

    def post_api_kernel_set_model_value(
        self,
        *,
        marimo_session_id: str,
        buffers: typing.Sequence[Base64String],
        message: ModelRequestMessage,
        model_id: WidgetModelId,
        token: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SuccessResponse:
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
        SuccessResponse
            Set model value

        Examples
        --------
        from fern import FernApi, ModelUpdateMessage, ModelUpdateMessageMethod

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_kernel_set_model_value(
            marimo_session_id="Marimo-Session-Id",
            buffers=["buffers"],
            message=ModelUpdateMessage(
                buffer_paths=[["bufferPaths"]],
                method=ModelUpdateMessageMethod.UPDATE,
                state={"key": "value"},
            ),
            model_id="modelId",
        )
        """
        _response = self._raw_client.post_api_kernel_set_model_value(
            marimo_session_id=marimo_session_id,
            buffers=buffers,
            message=message,
            model_id=model_id,
            token=token,
            request_options=request_options,
        )
        return _response.data

    def post_api_kernel_set_ui_element_value(
        self,
        *,
        marimo_session_id: str,
        object_ids: typing.Sequence[UiElementId],
        values: typing.Sequence[typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SuccessResponse:
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
        SuccessResponse
            Set UI element values

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_kernel_set_ui_element_value(
            marimo_session_id="Marimo-Session-Id",
            object_ids=["objectIds"],
            values=[],
        )
        """
        _response = self._raw_client.post_api_kernel_set_ui_element_value(
            marimo_session_id=marimo_session_id, object_ids=object_ids, values=values, request_options=request_options
        )
        return _response.data

    def post_api_kernel_shutdown(
        self, *, marimo_session_id: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> SuccessResponse:
        """
        Parameters
        ----------
        marimo_session_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Shutdown the kernel

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_kernel_shutdown()
        """
        _response = self._raw_client.post_api_kernel_shutdown(
            marimo_session_id=marimo_session_id, request_options=request_options
        )
        return _response.data

    def get_api_kernel_status(
        self, *, marimo_session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> KernelStatusResponse:
        """
        Parameters
        ----------
        marimo_session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KernelStatusResponse
            Report whether the kernel is currently executing. `running` means at least one cell is queued or running; `idle` means the kernel is alive but not executing; `stopped` means the kernel process is not running.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_api_kernel_status(
            marimo_session_id="Marimo-Session-Id",
        )
        """
        _response = self._raw_client.get_api_kernel_status(
            marimo_session_id=marimo_session_id, request_options=request_options
        )
        return _response.data

    def post_api_kernel_stdin(
        self, *, marimo_session_id: str, text: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SuccessResponse:
        """
        Parameters
        ----------
        marimo_session_id : str

        text : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Send input to the stdin stream

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_kernel_stdin(
            marimo_session_id="Marimo-Session-Id",
            text="text",
        )
        """
        _response = self._raw_client.post_api_kernel_stdin(
            marimo_session_id=marimo_session_id, text=text, request_options=request_options
        )
        return _response.data

    def post_api_kernel_takeover(
        self, *, marimo_session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PostApiKernelTakeoverResponse:
        """
        Parameters
        ----------
        marimo_session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostApiKernelTakeoverResponse
            Successfully closed existing sessions

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_kernel_takeover(
            marimo_session_id="Marimo-Session-Id",
        )
        """
        _response = self._raw_client.post_api_kernel_takeover(
            marimo_session_id=marimo_session_id, request_options=request_options
        )
        return _response.data

    def get_api_lsp_health(self, *, request_options: typing.Optional[RequestOptions] = None) -> LspHealthResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LspHealthResponse
            Get health status of all LSP servers

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_api_lsp_health()
        """
        _response = self._raw_client.get_api_lsp_health(request_options=request_options)
        return _response.data

    def post_api_lsp_restart(
        self,
        *,
        server_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LspRestartResponse:
        """
        Parameters
        ----------
        server_ids : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LspRestartResponse
            Restart LSP servers

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_lsp_restart()
        """
        _response = self._raw_client.post_api_lsp_restart(server_ids=server_ids, request_options=request_options)
        return _response.data

    def post_api_packages_add(
        self,
        *,
        package: str,
        group: typing.Optional[str] = OMIT,
        upgrade: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PackageOperationResponse:
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
        PackageOperationResponse
            Install package

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_packages_add(
            package="package",
        )
        """
        _response = self._raw_client.post_api_packages_add(
            package=package, group=group, upgrade=upgrade, request_options=request_options
        )
        return _response.data

    def get_api_packages_list(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListPackagesResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListPackagesResponse
            List installed packages

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_api_packages_list()
        """
        _response = self._raw_client.get_api_packages_list(request_options=request_options)
        return _response.data

    def post_api_packages_remove(
        self,
        *,
        package: str,
        group: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PackageOperationResponse:
        """
        Parameters
        ----------
        package : str

        group : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PackageOperationResponse
            Uninstall package

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_packages_remove(
            package="package",
        )
        """
        _response = self._raw_client.post_api_packages_remove(
            package=package, group=group, request_options=request_options
        )
        return _response.data

    def get_api_packages_tree(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DependencyTreeResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DependencyTreeResponse
            List dependency tree

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_api_packages_tree()
        """
        _response = self._raw_client.get_api_packages_tree(request_options=request_options)
        return _response.data

    def post_api_secrets_create(
        self,
        *,
        marimo_session_id: str,
        key: str,
        name: str,
        provider: CreateSecretRequestProvider,
        value: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BaseResponse:
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
        BaseResponse
            Create a secret

        Examples
        --------
        from fern import CreateSecretRequestProvider, FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_secrets_create(
            marimo_session_id="Marimo-Session-Id",
            key="key",
            name="name",
            provider=CreateSecretRequestProvider.DOTENV,
            value="value",
        )
        """
        _response = self._raw_client.post_api_secrets_create(
            marimo_session_id=marimo_session_id,
            key=key,
            name=name,
            provider=provider,
            value=value,
            request_options=request_options,
        )
        return _response.data

    def post_api_secrets_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> BaseResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseResponse
            Delete a secret

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_secrets_delete()
        """
        _response = self._raw_client.post_api_secrets_delete(request_options=request_options)
        return _response.data

    def post_api_secrets_keys(
        self, *, marimo_session_id: str, request_id: RequestId, request_options: typing.Optional[RequestOptions] = None
    ) -> ListSecretKeysResponse:
        """
        Parameters
        ----------
        marimo_session_id : str

        request_id : RequestId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListSecretKeysResponse
            List all secret keys

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_secrets_keys(
            marimo_session_id="Marimo-Session-Id",
            request_id="requestId",
        )
        """
        _response = self._raw_client.post_api_secrets_keys(
            marimo_session_id=marimo_session_id, request_id=request_id, request_options=request_options
        )
        return _response.data

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
    ) -> SuccessResponse:
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
        SuccessResponse
            Validate an SQL query

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_sql_validate(
            marimo_session_id="Marimo-Session-Id",
            only_parse=True,
            query="query",
            request_id="requestId",
        )
        """
        _response = self._raw_client.post_api_sql_validate(
            marimo_session_id=marimo_session_id,
            only_parse=only_parse,
            query=query,
            request_id=request_id,
            dialect=dialect,
            engine=engine,
            request_options=request_options,
        )
        return _response.data

    def get_api_status(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetApiStatusResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApiStatusResponse
            Get the status of the application

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_api_status()
        """
        _response = self._raw_client.get_api_status(request_options=request_options)
        return _response.data

    def get_api_status_connections(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetApiStatusConnectionsResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApiStatusConnectionsResponse
            Get the number of active websocket connections

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_api_status_connections()
        """
        _response = self._raw_client.get_api_status_connections(request_options=request_options)
        return _response.data

    def post_api_storage_download(
        self,
        *,
        marimo_session_id: str,
        namespace: str,
        path: str,
        request_id: RequestId,
        preview: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SuccessResponse:
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
        SuccessResponse
            Download a storage entry

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_storage_download(
            marimo_session_id="Marimo-Session-Id",
            namespace="namespace",
            path="path",
            request_id="requestId",
        )
        """
        _response = self._raw_client.post_api_storage_download(
            marimo_session_id=marimo_session_id,
            namespace=namespace,
            path=path,
            request_id=request_id,
            preview=preview,
            request_options=request_options,
        )
        return _response.data

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
    ) -> SuccessResponse:
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
        SuccessResponse
            List storage entries at a prefix

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_api_storage_list_entries(
            marimo_session_id="Marimo-Session-Id",
            limit=1,
            namespace="namespace",
            request_id="requestId",
        )
        """
        _response = self._raw_client.post_api_storage_list_entries(
            marimo_session_id=marimo_session_id,
            limit=limit,
            namespace=namespace,
            request_id=request_id,
            page_token=page_token,
            prefix=prefix,
            request_options=request_options,
        )
        return _response.data

    def get_api_usage(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetApiUsageResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApiUsageResponse
            Get the current memory and CPU usage of the application

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_api_usage()
        """
        _response = self._raw_client.get_api_usage(request_options=request_options)
        return _response.data

    def get_api_version(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Get the version of the application

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_api_version()
        """
        _response = self._raw_client.get_api_version(request_options=request_options)
        return _response.data

    @property
    def auth(self):
        if self._auth is None:
            from .auth.client import AuthClient

            self._auth = AuthClient(client_wrapper=self._client_wrapper)
        return self._auth


def _make_default_async_client(
    timeout: typing.Optional[float],
    follow_redirects: typing.Optional[bool],
) -> httpx.AsyncClient:
    try:
        import httpx_aiohttp
    except ImportError:
        pass
    else:
        if follow_redirects is not None:
            return httpx_aiohttp.HttpxAiohttpClient(timeout=timeout, follow_redirects=follow_redirects)
        return httpx_aiohttp.HttpxAiohttpClient(timeout=timeout)

    if follow_redirects is not None:
        return httpx.AsyncClient(timeout=timeout, follow_redirects=follow_redirects)
    return httpx.AsyncClient(timeout=timeout)


class AsyncFernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : str
        The base url to use for requests from the client.

    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    max_retries : typing.Optional[int]
        The default maximum number of retries for failed requests. Defaults to 2. Per-request `max_retries` in `request_options` takes precedence over this value.

    stream_reconnection_enabled : typing.Optional[bool]
        Whether to automatically reconnect on stream disconnection for resumable streaming endpoints. Defaults to True. Per-request `stream_reconnection_enabled` in `request_options` takes precedence over this value.

    max_stream_reconnection_attempts : typing.Optional[int]
        The maximum number of reconnection attempts for resumable streaming endpoints. Defaults to no limit. Per-request `max_stream_reconnection_attempts` in `request_options` takes precedence over this value.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    logging : typing.Optional[typing.Union[LogConfig, Logger]]
        Configure logging for the SDK. Accepts a LogConfig dict with 'level' (debug/info/warn/error), 'logger' (custom logger implementation), and 'silent' (boolean, defaults to True) fields. You can also pass a pre-configured Logger instance.

    Examples
    --------
    from fern import AsyncFernApi

    client = AsyncFernApi(
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        _defaulted_max_retries = max_retries if max_retries is not None else 2
        self._client_wrapper = AsyncClientWrapper(
            base_url=base_url,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else _make_default_async_client(timeout=_defaulted_timeout, follow_redirects=follow_redirects),
            timeout=_defaulted_timeout,
            max_retries=_defaulted_max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
        )
        self._raw_client = AsyncRawFernApi(client_wrapper=self._client_wrapper)
        self._auth: typing.Optional[AsyncAuthClient] = None

    @property
    def with_raw_response(self) -> AsyncRawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFernApi
        """
        return self._raw_client

    async def get_file_filename_and_length(
        self, filename_and_length: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        filename_and_length : str
            The filename and byte length of the virtual file

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Get a virtual file

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_file_filename_and_length(
                filename_and_length="filename_and_length",
            )


        asyncio.run(main())
        """
        async with self._raw_client.get_file_filename_and_length(
            filename_and_length, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

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
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_ai_chat(
                marimo_session_id="Marimo-Session-Id",
                include_other_code="includeOtherCode",
                ui_messages=[{"key": "value"}],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_ai_chat(
            marimo_session_id=marimo_session_id,
            include_other_code=include_other_code,
            ui_messages=ui_messages,
            model=model,
            options=options,
            tools=tools,
            variables=variables,
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.Dict[str, typing.Any]:
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
        typing.Dict[str, typing.Any]
            Get AI completion for a prompt

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_ai_completion(
                marimo_session_id="Marimo-Session-Id",
                code="code",
                include_other_code="includeOtherCode",
                prompt="prompt",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_ai_completion(
            marimo_session_id=marimo_session_id,
            code=code,
            include_other_code=include_other_code,
            prompt=prompt,
            context=context,
            language=language,
            selected_text=selected_text,
            ui_messages=ui_messages,
            request_options=request_options,
        )
        return _response.data

    async def post_api_ai_inline_completion(
        self,
        *,
        marimo_session_id: str,
        prefix: str,
        suffix: str,
        language: typing.Optional[AiInlineCompletionRequestLanguage] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
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
        str
            Get AI inline completion for code

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_ai_inline_completion(
                marimo_session_id="marimoSessionId",
                prefix="prefix",
                suffix="suffix",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_ai_inline_completion(
            marimo_session_id=marimo_session_id,
            prefix=prefix,
            suffix=suffix,
            language=language,
            request_options=request_options,
        )
        return _response.data

    async def post_api_ai_invoke_tool(
        self,
        *,
        marimo_session_id: str,
        arguments: typing.Dict[str, typing.Any],
        tool_name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InvokeAiToolResponse:
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
        InvokeAiToolResponse
            Tool invocation result

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_ai_invoke_tool(
                marimo_session_id="Marimo-Session-Id",
                arguments={"key": "value"},
                tool_name="toolName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_ai_invoke_tool(
            marimo_session_id=marimo_session_id,
            arguments=arguments,
            tool_name=tool_name,
            request_options=request_options,
        )
        return _response.data

    async def post_api_ai_mcp_refresh(
        self, *, marimo_session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> McpRefreshResponse:
        """
        Parameters
        ----------
        marimo_session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        McpRefreshResponse
            Refresh MCP server configuration

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_ai_mcp_refresh(
                marimo_session_id="Marimo-Session-Id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_ai_mcp_refresh(
            marimo_session_id=marimo_session_id, request_options=request_options
        )
        return _response.data

    async def get_api_ai_mcp_status(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> McpStatusResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        McpStatusResponse
            Get MCP server status

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_api_ai_mcp_status()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_ai_mcp_status(request_options=request_options)
        return _response.data

    async def post_api_cache_clear(
        self, *, marimo_session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SuccessResponse:
        """
        Parameters
        ----------
        marimo_session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Clear all caches

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_cache_clear(
                marimo_session_id="Marimo-Session-Id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_cache_clear(
            marimo_session_id=marimo_session_id, request_options=request_options
        )
        return _response.data

    async def post_api_cache_info(
        self, *, marimo_session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SuccessResponse:
        """
        Parameters
        ----------
        marimo_session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Get cache statistics

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_cache_info(
                marimo_session_id="Marimo-Session-Id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_cache_info(
            marimo_session_id=marimo_session_id, request_options=request_options
        )
        return _response.data

    async def post_api_datasources_discover(
        self, *, marimo_session_id: str, request_id: RequestId, request_options: typing.Optional[RequestOptions] = None
    ) -> SuccessResponse:
        """
        Parameters
        ----------
        marimo_session_id : str

        request_id : RequestId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Discover datasource connections

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_datasources_discover(
                marimo_session_id="Marimo-Session-Id",
                request_id="requestId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_datasources_discover(
            marimo_session_id=marimo_session_id, request_id=request_id, request_options=request_options
        )
        return _response.data

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
    ) -> SuccessResponse:
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
        SuccessResponse
            Preview a column in a dataset

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, PreviewDatasetColumnRequestSourceType

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_datasources_preview_column(
                marimo_session_id="Marimo-Session-Id",
                column_name="columnName",
                source="source",
                source_type=PreviewDatasetColumnRequestSourceType.CATALOG,
                table_name="tableName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_datasources_preview_column(
            marimo_session_id=marimo_session_id,
            column_name=column_name,
            source=source,
            source_type=source_type,
            table_name=table_name,
            fully_qualified_table_name=fully_qualified_table_name,
            request_options=request_options,
        )
        return _response.data

    async def post_api_datasources_preview_datasource_connection(
        self, *, marimo_session_id: str, engine: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SuccessResponse:
        """
        Parameters
        ----------
        marimo_session_id : str

        engine : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Broadcasts a datasource connection

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_datasources_preview_datasource_connection(
                marimo_session_id="Marimo-Session-Id",
                engine="engine",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_datasources_preview_datasource_connection(
            marimo_session_id=marimo_session_id, engine=engine, request_options=request_options
        )
        return _response.data

    async def post_api_datasources_preview_sql_schema_list(
        self,
        *,
        marimo_session_id: str,
        database: str,
        engine: str,
        request_id: RequestId,
        schema_path: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SuccessResponse:
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
        SuccessResponse
            Preview a list of schemas in an SQL database

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_datasources_preview_sql_schema_list(
                marimo_session_id="Marimo-Session-Id",
                database="database",
                engine="engine",
                request_id="requestId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_datasources_preview_sql_schema_list(
            marimo_session_id=marimo_session_id,
            database=database,
            engine=engine,
            request_id=request_id,
            schema_path=schema_path,
            request_options=request_options,
        )
        return _response.data

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
    ) -> SuccessResponse:
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
        SuccessResponse
            Preview a SQL table

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_datasources_preview_sql_table(
                marimo_session_id="Marimo-Session-Id",
                database="database",
                engine="engine",
                request_id="requestId",
                schema="schema",
                table_name="tableName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_datasources_preview_sql_table(
            marimo_session_id=marimo_session_id,
            database=database,
            engine=engine,
            request_id=request_id,
            schema=schema,
            table_name=table_name,
            schema_path=schema_path,
            request_options=request_options,
        )
        return _response.data

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
    ) -> SuccessResponse:
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
        SuccessResponse
            Preview a list of tables in an SQL schema

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_datasources_preview_sql_table_list(
                marimo_session_id="Marimo-Session-Id",
                database="database",
                engine="engine",
                request_id="requestId",
                schema="schema",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_datasources_preview_sql_table_list(
            marimo_session_id=marimo_session_id,
            database=database,
            engine=engine,
            request_id=request_id,
            schema=schema,
            schema_path=schema_path,
            request_options=request_options,
        )
        return _response.data

    async def post_api_document_transaction(
        self,
        *,
        marimo_session_id: str,
        changes: typing.Sequence[NotebookDocumentTransactionRequestChangesItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SuccessResponse:
        """
        Parameters
        ----------
        marimo_session_id : str

        changes : typing.Sequence[NotebookDocumentTransactionRequestChangesItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Apply a document transaction

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, CellConfig, CreateCell, CreateCellType

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_document_transaction(
                marimo_session_id="Marimo-Session-Id",
                changes=[
                    CreateCell(
                        cell_id="cellId",
                        code="code",
                        config=CellConfig(),
                        name="name",
                        type=CreateCellType.CREATE_CELL,
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_document_transaction(
            marimo_session_id=marimo_session_id, changes=changes, request_options=request_options
        )
        return _response.data

    async def get_api_documentation_snippets(
        self, *, marimo_session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Snippets:
        """
        Parameters
        ----------
        marimo_session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Snippets
            Load the snippets for the documentation page

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_api_documentation_snippets(
                marimo_session_id="Marimo-Session-Id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_documentation_snippets(
            marimo_session_id=marimo_session_id, request_options=request_options
        )
        return _response.data

    async def get_api_environment(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetApiEnvironmentResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApiEnvironmentResponse
            Environment information for issue reporting

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_api_environment()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_environment(request_options=request_options)
        return _response.data

    async def post_api_export_auto_export_html(
        self,
        *,
        marimo_session_id: str,
        download: bool,
        files: typing.Sequence[str],
        include_code: bool,
        asset_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SuccessResponse:
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
        SuccessResponse
            Export the notebook as HTML

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_export_auto_export_html(
                marimo_session_id="Marimo-Session-Id",
                download=True,
                files=["files"],
                include_code=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_export_auto_export_html(
            marimo_session_id=marimo_session_id,
            download=download,
            files=files,
            include_code=include_code,
            asset_url=asset_url,
            request_options=request_options,
        )
        return _response.data

    async def post_api_export_auto_export_ipynb(
        self, *, marimo_session_id: str, download: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> SuccessResponse:
        """
        Parameters
        ----------
        marimo_session_id : str

        download : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Export the notebook as IPYNB

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_export_auto_export_ipynb(
                marimo_session_id="Marimo-Session-Id",
                download=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_export_auto_export_ipynb(
            marimo_session_id=marimo_session_id, download=download, request_options=request_options
        )
        return _response.data

    async def post_api_export_auto_export_markdown(
        self, *, marimo_session_id: str, download: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> SuccessResponse:
        """
        Parameters
        ----------
        marimo_session_id : str

        download : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Export the notebook as a markdown

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_export_auto_export_markdown(
                marimo_session_id="Marimo-Session-Id",
                download=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_export_auto_export_markdown(
            marimo_session_id=marimo_session_id, download=download, request_options=request_options
        )
        return _response.data

    async def get_api_export_availability(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ExportAvailabilityResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportAvailabilityResponse
            Readiness for server-backed exports

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_api_export_availability()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_export_availability(request_options=request_options)
        return _response.data

    async def post_api_export_html(
        self,
        *,
        marimo_session_id: str,
        download: bool,
        files: typing.Sequence[str],
        include_code: bool,
        asset_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
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
        str
            Export the notebook as HTML

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_export_html(
                marimo_session_id="marimoSessionId",
                download=True,
                files=["files", "files"],
                include_code=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_export_html(
            marimo_session_id=marimo_session_id,
            download=download,
            files=files,
            include_code=include_code,
            asset_url=asset_url,
            request_options=request_options,
        )
        return _response.data

    async def post_api_export_ipynb(
        self,
        *,
        marimo_session_id: str,
        download: bool,
        include_outputs: typing.Optional[bool] = OMIT,
        sort_mode: typing.Optional[ExportAsIpynbRequestSortMode] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
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
        str
            Export the notebook as IPYNB

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_export_ipynb(
                marimo_session_id="marimoSessionId",
                download=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_export_ipynb(
            marimo_session_id=marimo_session_id,
            download=download,
            include_outputs=include_outputs,
            sort_mode=sort_mode,
            request_options=request_options,
        )
        return _response.data

    async def post_api_export_markdown(
        self,
        *,
        marimo_session_id: str,
        download: bool,
        flavor: typing.Optional[ExportAsMarkdownRequestFlavor] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
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
        str
            Export the notebook as a markdown

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_export_markdown(
                marimo_session_id="marimoSessionId",
                download=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_export_markdown(
            marimo_session_id=marimo_session_id, download=download, flavor=flavor, request_options=request_options
        )
        return _response.data

    async def post_api_export_pdf(
        self,
        *,
        marimo_session_id: str,
        webpdf: bool,
        include_inputs: typing.Optional[bool] = OMIT,
        include_outputs: typing.Optional[bool] = OMIT,
        preset: typing.Optional[ExportAsPdfRequestPreset] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
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
        typing.AsyncIterator[bytes]
            Export the notebook as a PDF

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_export_pdf(
                marimo_session_id="marimoSessionId",
                webpdf=True,
            )


        asyncio.run(main())
        """
        async with self._raw_client.post_api_export_pdf(
            marimo_session_id=marimo_session_id,
            webpdf=webpdf,
            include_inputs=include_inputs,
            include_outputs=include_outputs,
            preset=preset,
            request_options=request_options,
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def post_api_export_requirements_install(
        self,
        *,
        marimo_session_id: str,
        format: InstallExportRequirementsRequestFormat,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExportAvailabilityResponse:
        """
        Parameters
        ----------
        marimo_session_id : str

        format : InstallExportRequirementsRequestFormat

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportAvailabilityResponse
            Updated readiness for server-backed exports

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, InstallExportRequirementsRequestFormat

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_export_requirements_install(
                marimo_session_id="Marimo-Session-Id",
                format=InstallExportRequirementsRequestFormat.HTML,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_export_requirements_install(
            marimo_session_id=marimo_session_id, format=format, request_options=request_options
        )
        return _response.data

    async def post_api_export_script(
        self, *, marimo_session_id: str, download: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        marimo_session_id : str

        download : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Export the notebook as a script

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_export_script(
                marimo_session_id="marimoSessionId",
                download=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_export_script(
            marimo_session_id=marimo_session_id, download=download, request_options=request_options
        )
        return _response.data

    async def post_api_export_update_cell_outputs(
        self,
        *,
        marimo_session_id: str,
        cell_ids_to_output: typing.Dict[str, typing.Sequence[typing.Any]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SuccessResponse:
        """
        Parameters
        ----------
        marimo_session_id : str

        cell_ids_to_output : typing.Dict[str, typing.Sequence[typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Update the cell outputs

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_export_update_cell_outputs(
                marimo_session_id="Marimo-Session-Id",
                cell_ids_to_output={"key": []},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_export_update_cell_outputs(
            marimo_session_id=marimo_session_id, cell_ids_to_output=cell_ids_to_output, request_options=request_options
        )
        return _response.data

    async def post_api_files_copy(
        self, *, new_path: str, path: str, request_options: typing.Optional[RequestOptions] = None
    ) -> FileCopyResponse:
        """
        Parameters
        ----------
        new_path : str

        path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileCopyResponse
            Copy a file or directory

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_files_copy(
                new_path="newPath",
                path="path",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_files_copy(
            new_path=new_path, path=path, request_options=request_options
        )
        return _response.data

    async def post_api_files_create(
        self,
        *,
        name: str,
        path: str,
        type: PostApiFilesCreateRequestType,
        file: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FileCreateResponse:
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
        FileCreateResponse
            Create a new file or directory

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, PostApiFilesCreateRequestType

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_files_create(
                name="name",
                path="path",
                type=PostApiFilesCreateRequestType.DIRECTORY,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_files_create(
            name=name, path=path, type=type, file=file, request_options=request_options
        )
        return _response.data

    async def post_api_files_delete(
        self, *, path: str, request_options: typing.Optional[RequestOptions] = None
    ) -> FileDeleteResponse:
        """
        Parameters
        ----------
        path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileDeleteResponse
            Delete a file or directory

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_files_delete(
                path="path",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_files_delete(path=path, request_options=request_options)
        return _response.data

    async def get_api_files_download(
        self, *, path: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        path : str
            Path of the file to download

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Stream the file as an attachment

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_api_files_download(
                path="path",
            )


        asyncio.run(main())
        """
        async with self._raw_client.get_api_files_download(path=path, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def post_api_files_file_details(
        self,
        *,
        path: str,
        max_bytes: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FileDetailsResponse:
        """
        Parameters
        ----------
        path : str

        max_bytes : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileDetailsResponse
            Get details of a specific file or directory

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_files_file_details(
                path="path",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_files_file_details(
            path=path, max_bytes=max_bytes, request_options=request_options
        )
        return _response.data

    async def post_api_files_list_files(
        self, *, path: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> FileListResponse:
        """
        Parameters
        ----------
        path : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileListResponse
            List files and directories in a given path

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_files_list_files()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_files_list_files(path=path, request_options=request_options)
        return _response.data

    async def post_api_files_move(
        self, *, new_path: str, path: str, request_options: typing.Optional[RequestOptions] = None
    ) -> FileMoveResponse:
        """
        Parameters
        ----------
        new_path : str

        path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileMoveResponse
            Move a file or directory

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_files_move(
                new_path="newPath",
                path="path",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_files_move(
            new_path=new_path, path=path, request_options=request_options
        )
        return _response.data

    async def post_api_files_open(
        self,
        *,
        path: str,
        line_number: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BaseResponse:
        """
        Parameters
        ----------
        path : str

        line_number : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseResponse
            Open a file in the system editor

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_files_open(
                path="path",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_files_open(
            path=path, line_number=line_number, request_options=request_options
        )
        return _response.data

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
    ) -> FileSearchResponse:
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
        FileSearchResponse
            Search for files and directories matching a query

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_files_search(
                query="query",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_files_search(
            query=query,
            depth=depth,
            include_directories=include_directories,
            include_files=include_files,
            limit=limit,
            path=path,
            request_options=request_options,
        )
        return _response.data

    async def post_api_files_update(
        self, *, contents: str, path: str, request_options: typing.Optional[RequestOptions] = None
    ) -> FileUpdateResponse:
        """
        Parameters
        ----------
        contents : str

        path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileUpdateResponse
            Update a file or directory

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_files_update(
                contents="contents",
                path="path",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_files_update(
            contents=contents, path=path, request_options=request_options
        )
        return _response.data

    async def post_api_home_recent_files(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RecentFilesResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecentFilesResponse
            Get the recent files

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_home_recent_files()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_home_recent_files(request_options=request_options)
        return _response.data

    async def post_api_home_running_notebooks(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RunningNotebooksResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RunningNotebooksResponse
            Get the running files

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_home_running_notebooks()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_home_running_notebooks(request_options=request_options)
        return _response.data

    async def post_api_home_shutdown_session(
        self, *, session_id: SessionId, request_options: typing.Optional[RequestOptions] = None
    ) -> RunningNotebooksResponse:
        """
        Parameters
        ----------
        session_id : SessionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RunningNotebooksResponse
            Shutdown the current session

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_home_shutdown_session(
                session_id="sessionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_home_shutdown_session(
            session_id=session_id, request_options=request_options
        )
        return _response.data

    async def post_api_home_tutorial_open(
        self, *, tutorial_id: OpenTutorialRequestTutorialId, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoFile:
        """
        Parameters
        ----------
        tutorial_id : OpenTutorialRequestTutorialId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoFile
            Open a new tutorial

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, OpenTutorialRequestTutorialIdZero

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_home_tutorial_open(
                tutorial_id=OpenTutorialRequestTutorialIdZero.DATAFLOW,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_home_tutorial_open(
            tutorial_id=tutorial_id, request_options=request_options
        )
        return _response.data

    async def post_api_home_workspace_files(
        self, *, include_markdown: typing.Optional[bool] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkspaceFilesResponse:
        """
        Parameters
        ----------
        include_markdown : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceFilesResponse
            Get the files in the workspace

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_home_workspace_files()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_home_workspace_files(
            include_markdown=include_markdown, request_options=request_options
        )
        return _response.data

    async def post_api_kernel_code_autocomplete(
        self,
        *,
        marimo_session_id: str,
        cell_id: CellId,
        document: str,
        id: RequestId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SuccessResponse:
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
        SuccessResponse
            Complete a code fragment

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_kernel_code_autocomplete(
                marimo_session_id="Marimo-Session-Id",
                cell_id="cellId",
                document="document",
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_kernel_code_autocomplete(
            marimo_session_id=marimo_session_id,
            cell_id=cell_id,
            document=document,
            id=id,
            request_options=request_options,
        )
        return _response.data

    async def post_api_kernel_copy(
        self,
        *,
        marimo_session_id: str,
        destination: str,
        source: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
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
        str
            Copy notebook

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_kernel_copy(
                marimo_session_id="marimoSessionId",
                destination="destination",
                source="source",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_kernel_copy(
            marimo_session_id=marimo_session_id, destination=destination, source=source, request_options=request_options
        )
        return _response.data

    async def post_api_kernel_delete(
        self, *, marimo_session_id: str, cell_id: CellId, request_options: typing.Optional[RequestOptions] = None
    ) -> SuccessResponse:
        """
        Parameters
        ----------
        marimo_session_id : str

        cell_id : CellId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Delete a cell

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_kernel_delete(
                marimo_session_id="Marimo-Session-Id",
                cell_id="cellId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_kernel_delete(
            marimo_session_id=marimo_session_id, cell_id=cell_id, request_options=request_options
        )
        return _response.data

    async def post_api_kernel_focus_cell(
        self, *, marimo_session_id: str, cell_id: CellId, request_options: typing.Optional[RequestOptions] = None
    ) -> SuccessResponse:
        """
        Parameters
        ----------
        marimo_session_id : str

        cell_id : CellId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Focus a cell in kiosk-mode consumers

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_kernel_focus_cell(
                marimo_session_id="Marimo-Session-Id",
                cell_id="cellId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_kernel_focus_cell(
            marimo_session_id=marimo_session_id, cell_id=cell_id, request_options=request_options
        )
        return _response.data

    async def post_api_kernel_format(
        self, *, codes: typing.Dict[str, str], line_length: int, request_options: typing.Optional[RequestOptions] = None
    ) -> FormatResponse:
        """
        Parameters
        ----------
        codes : typing.Dict[str, str]

        line_length : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FormatResponse
            Format code

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_kernel_format(
                codes={"key": "value"},
                line_length=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_kernel_format(
            codes=codes, line_length=line_length, request_options=request_options
        )
        return _response.data

    async def post_api_kernel_function_call(
        self,
        *,
        marimo_session_id: str,
        args: typing.Dict[str, typing.Any],
        function_call_id: RequestId,
        function_name: str,
        namespace: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SuccessResponse:
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
        SuccessResponse
            Invoke an RPC

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_kernel_function_call(
                marimo_session_id="Marimo-Session-Id",
                args={"key": "value"},
                function_call_id="functionCallId",
                function_name="functionName",
                namespace="namespace",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_kernel_function_call(
            marimo_session_id=marimo_session_id,
            args=args,
            function_call_id=function_call_id,
            function_name=function_name,
            namespace=namespace,
            request_options=request_options,
        )
        return _response.data

    async def post_api_kernel_install_missing_packages(
        self,
        *,
        marimo_session_id: str,
        manager: str,
        versions: typing.Dict[str, str],
        source: typing.Optional[InstallPackagesRequestSource] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SuccessResponse:
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
        SuccessResponse
            Install missing packages

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_kernel_install_missing_packages(
                marimo_session_id="Marimo-Session-Id",
                manager="manager",
                versions={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_kernel_install_missing_packages(
            marimo_session_id=marimo_session_id,
            manager=manager,
            versions=versions,
            source=source,
            request_options=request_options,
        )
        return _response.data

    async def post_api_kernel_instantiate(
        self,
        *,
        marimo_session_id: str,
        object_ids: typing.Sequence[UiElementId],
        values: typing.Sequence[typing.Any],
        auto_run: typing.Optional[bool] = OMIT,
        codes: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SuccessResponse:
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
        SuccessResponse
            Instantiate a component. Only allowed in edit mode; in run mode, instantiation happens server-side automatically.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_kernel_instantiate(
                marimo_session_id="Marimo-Session-Id",
                object_ids=["objectIds"],
                values=[],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_kernel_instantiate(
            marimo_session_id=marimo_session_id,
            object_ids=object_ids,
            values=values,
            auto_run=auto_run,
            codes=codes,
            request_options=request_options,
        )
        return _response.data

    async def post_api_kernel_interrupt(
        self, *, marimo_session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SuccessResponse:
        """
        Parameters
        ----------
        marimo_session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Interrupt the kernel's execution

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_kernel_interrupt(
                marimo_session_id="Marimo-Session-Id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_kernel_interrupt(
            marimo_session_id=marimo_session_id, request_options=request_options
        )
        return _response.data

    async def post_api_kernel_pdb_breakpoints(
        self,
        *,
        marimo_session_id: str,
        breakpoints: typing.Dict[str, typing.Sequence[int]],
        request: typing.Optional[HttpRequest] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SuccessResponse:
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
        SuccessResponse
            Set the live debugger's breakpoints for the session.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_kernel_pdb_breakpoints(
                marimo_session_id="Marimo-Session-Id",
                breakpoints={"key": [1]},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_kernel_pdb_breakpoints(
            marimo_session_id=marimo_session_id,
            breakpoints=breakpoints,
            request=request,
            request_options=request_options,
        )
        return _response.data

    async def post_api_kernel_pdb_pm(
        self,
        *,
        marimo_session_id: str,
        cell_id: CellId,
        request: typing.Optional[HttpRequest] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SuccessResponse:
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
        SuccessResponse
            Run a post mortem on the most recent failed cell.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_kernel_pdb_pm(
                marimo_session_id="Marimo-Session-Id",
                cell_id="cellId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_kernel_pdb_pm(
            marimo_session_id=marimo_session_id, cell_id=cell_id, request=request, request_options=request_options
        )
        return _response.data

    async def post_api_kernel_read_code(
        self, *, marimo_session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ReadCodeResponse:
        """
        Parameters
        ----------
        marimo_session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReadCodeResponse
            Read the code from the server

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_kernel_read_code(
                marimo_session_id="Marimo-Session-Id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_kernel_read_code(
            marimo_session_id=marimo_session_id, request_options=request_options
        )
        return _response.data

    async def post_api_kernel_rename(
        self, *, marimo_session_id: str, filename: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SuccessResponse:
        """
        Parameters
        ----------
        marimo_session_id : str

        filename : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Rename the current app

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_kernel_rename(
                marimo_session_id="Marimo-Session-Id",
                filename="filename",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_kernel_rename(
            marimo_session_id=marimo_session_id, filename=filename, request_options=request_options
        )
        return _response.data

    async def post_api_kernel_restart_session(
        self, *, marimo_session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SuccessResponse:
        """
        Parameters
        ----------
        marimo_session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Restart the current session without affecting other sessions.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_kernel_restart_session(
                marimo_session_id="Marimo-Session-Id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_kernel_restart_session(
            marimo_session_id=marimo_session_id, request_options=request_options
        )
        return _response.data

    async def post_api_kernel_run(
        self,
        *,
        marimo_session_id: str,
        cell_ids: typing.Sequence[CellId],
        codes: typing.Sequence[str],
        request: typing.Optional[HttpRequest] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SuccessResponse:
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
        SuccessResponse
            Run a cell. Updates cell code in the kernel if needed; registers new cells for unseen cell IDs. Only allowed in edit mode.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_kernel_run(
                marimo_session_id="Marimo-Session-Id",
                cell_ids=["cellIds"],
                codes=["codes"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_kernel_run(
            marimo_session_id=marimo_session_id,
            cell_ids=cell_ids,
            codes=codes,
            request=request,
            request_options=request_options,
        )
        return _response.data

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
    ) -> str:
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
        str
            Save the current app

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, CellConfig

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_kernel_save(
                marimo_session_id="marimoSessionId",
                cell_ids=["cellIds", "cellIds"],
                codes=["codes", "codes"],
                configs=[CellConfig(), CellConfig()],
                filename="filename",
                names=["names", "names"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_kernel_save(
            marimo_session_id=marimo_session_id,
            cell_ids=cell_ids,
            codes=codes,
            configs=configs,
            filename=filename,
            names=names,
            layout=layout,
            persist=persist,
            request_options=request_options,
        )
        return _response.data

    async def post_api_kernel_save_app_config(
        self,
        *,
        marimo_session_id: str,
        config: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Parameters
        ----------
        marimo_session_id : str

        config : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Save the app configuration

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_kernel_save_app_config(
                marimo_session_id="marimoSessionId",
                config={"config": {"key": "value"}},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_kernel_save_app_config(
            marimo_session_id=marimo_session_id, config=config, request_options=request_options
        )
        return _response.data

    async def post_api_kernel_save_user_config(
        self,
        *,
        config: typing.Dict[str, typing.Any],
        marimo_session_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SuccessResponse:
        """
        Parameters
        ----------
        config : typing.Dict[str, typing.Any]

        marimo_session_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Update the user config on disk and in the kernel. Only allowed in edit mode.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_kernel_save_user_config(
                config={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_kernel_save_user_config(
            config=config, marimo_session_id=marimo_session_id, request_options=request_options
        )
        return _response.data

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
    ) -> SuccessResponse:
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
        SuccessResponse
            Run the scratchpad

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_kernel_scratchpad_run(
                marimo_session_id="Marimo-Session-Id",
                code="code",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_kernel_scratchpad_run(
            marimo_session_id=marimo_session_id,
            code=code,
            cell_outputs=cell_outputs,
            notebook_cells=notebook_cells,
            request=request,
            run_id=run_id,
            request_options=request_options,
        )
        return _response.data

    async def post_api_kernel_set_cell_config(
        self,
        *,
        marimo_session_id: str,
        configs: typing.Dict[str, typing.Dict[str, typing.Any]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SuccessResponse:
        """
        Parameters
        ----------
        marimo_session_id : str

        configs : typing.Dict[str, typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Set the configuration of a cell

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_kernel_set_cell_config(
                marimo_session_id="Marimo-Session-Id",
                configs={"key": {"key": "value"}},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_kernel_set_cell_config(
            marimo_session_id=marimo_session_id, configs=configs, request_options=request_options
        )
        return _response.data

    async def post_api_kernel_set_model_value(
        self,
        *,
        marimo_session_id: str,
        buffers: typing.Sequence[Base64String],
        message: ModelRequestMessage,
        model_id: WidgetModelId,
        token: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SuccessResponse:
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
        SuccessResponse
            Set model value

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ModelUpdateMessage, ModelUpdateMessageMethod

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_kernel_set_model_value(
                marimo_session_id="Marimo-Session-Id",
                buffers=["buffers"],
                message=ModelUpdateMessage(
                    buffer_paths=[["bufferPaths"]],
                    method=ModelUpdateMessageMethod.UPDATE,
                    state={"key": "value"},
                ),
                model_id="modelId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_kernel_set_model_value(
            marimo_session_id=marimo_session_id,
            buffers=buffers,
            message=message,
            model_id=model_id,
            token=token,
            request_options=request_options,
        )
        return _response.data

    async def post_api_kernel_set_ui_element_value(
        self,
        *,
        marimo_session_id: str,
        object_ids: typing.Sequence[UiElementId],
        values: typing.Sequence[typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SuccessResponse:
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
        SuccessResponse
            Set UI element values

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_kernel_set_ui_element_value(
                marimo_session_id="Marimo-Session-Id",
                object_ids=["objectIds"],
                values=[],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_kernel_set_ui_element_value(
            marimo_session_id=marimo_session_id, object_ids=object_ids, values=values, request_options=request_options
        )
        return _response.data

    async def post_api_kernel_shutdown(
        self, *, marimo_session_id: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> SuccessResponse:
        """
        Parameters
        ----------
        marimo_session_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Shutdown the kernel

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_kernel_shutdown()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_kernel_shutdown(
            marimo_session_id=marimo_session_id, request_options=request_options
        )
        return _response.data

    async def get_api_kernel_status(
        self, *, marimo_session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> KernelStatusResponse:
        """
        Parameters
        ----------
        marimo_session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KernelStatusResponse
            Report whether the kernel is currently executing. `running` means at least one cell is queued or running; `idle` means the kernel is alive but not executing; `stopped` means the kernel process is not running.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_api_kernel_status(
                marimo_session_id="Marimo-Session-Id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_kernel_status(
            marimo_session_id=marimo_session_id, request_options=request_options
        )
        return _response.data

    async def post_api_kernel_stdin(
        self, *, marimo_session_id: str, text: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SuccessResponse:
        """
        Parameters
        ----------
        marimo_session_id : str

        text : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Send input to the stdin stream

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_kernel_stdin(
                marimo_session_id="Marimo-Session-Id",
                text="text",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_kernel_stdin(
            marimo_session_id=marimo_session_id, text=text, request_options=request_options
        )
        return _response.data

    async def post_api_kernel_takeover(
        self, *, marimo_session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PostApiKernelTakeoverResponse:
        """
        Parameters
        ----------
        marimo_session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostApiKernelTakeoverResponse
            Successfully closed existing sessions

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_kernel_takeover(
                marimo_session_id="Marimo-Session-Id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_kernel_takeover(
            marimo_session_id=marimo_session_id, request_options=request_options
        )
        return _response.data

    async def get_api_lsp_health(self, *, request_options: typing.Optional[RequestOptions] = None) -> LspHealthResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LspHealthResponse
            Get health status of all LSP servers

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_api_lsp_health()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_lsp_health(request_options=request_options)
        return _response.data

    async def post_api_lsp_restart(
        self,
        *,
        server_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LspRestartResponse:
        """
        Parameters
        ----------
        server_ids : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LspRestartResponse
            Restart LSP servers

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_lsp_restart()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_lsp_restart(server_ids=server_ids, request_options=request_options)
        return _response.data

    async def post_api_packages_add(
        self,
        *,
        package: str,
        group: typing.Optional[str] = OMIT,
        upgrade: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PackageOperationResponse:
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
        PackageOperationResponse
            Install package

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_packages_add(
                package="package",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_packages_add(
            package=package, group=group, upgrade=upgrade, request_options=request_options
        )
        return _response.data

    async def get_api_packages_list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListPackagesResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListPackagesResponse
            List installed packages

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_api_packages_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_packages_list(request_options=request_options)
        return _response.data

    async def post_api_packages_remove(
        self,
        *,
        package: str,
        group: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PackageOperationResponse:
        """
        Parameters
        ----------
        package : str

        group : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PackageOperationResponse
            Uninstall package

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_packages_remove(
                package="package",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_packages_remove(
            package=package, group=group, request_options=request_options
        )
        return _response.data

    async def get_api_packages_tree(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DependencyTreeResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DependencyTreeResponse
            List dependency tree

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_api_packages_tree()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_packages_tree(request_options=request_options)
        return _response.data

    async def post_api_secrets_create(
        self,
        *,
        marimo_session_id: str,
        key: str,
        name: str,
        provider: CreateSecretRequestProvider,
        value: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BaseResponse:
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
        BaseResponse
            Create a secret

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, CreateSecretRequestProvider

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_secrets_create(
                marimo_session_id="Marimo-Session-Id",
                key="key",
                name="name",
                provider=CreateSecretRequestProvider.DOTENV,
                value="value",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_secrets_create(
            marimo_session_id=marimo_session_id,
            key=key,
            name=name,
            provider=provider,
            value=value,
            request_options=request_options,
        )
        return _response.data

    async def post_api_secrets_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> BaseResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseResponse
            Delete a secret

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_secrets_delete()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_secrets_delete(request_options=request_options)
        return _response.data

    async def post_api_secrets_keys(
        self, *, marimo_session_id: str, request_id: RequestId, request_options: typing.Optional[RequestOptions] = None
    ) -> ListSecretKeysResponse:
        """
        Parameters
        ----------
        marimo_session_id : str

        request_id : RequestId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListSecretKeysResponse
            List all secret keys

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_secrets_keys(
                marimo_session_id="Marimo-Session-Id",
                request_id="requestId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_secrets_keys(
            marimo_session_id=marimo_session_id, request_id=request_id, request_options=request_options
        )
        return _response.data

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
    ) -> SuccessResponse:
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
        SuccessResponse
            Validate an SQL query

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_sql_validate(
                marimo_session_id="Marimo-Session-Id",
                only_parse=True,
                query="query",
                request_id="requestId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_sql_validate(
            marimo_session_id=marimo_session_id,
            only_parse=only_parse,
            query=query,
            request_id=request_id,
            dialect=dialect,
            engine=engine,
            request_options=request_options,
        )
        return _response.data

    async def get_api_status(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetApiStatusResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApiStatusResponse
            Get the status of the application

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_api_status()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_status(request_options=request_options)
        return _response.data

    async def get_api_status_connections(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetApiStatusConnectionsResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApiStatusConnectionsResponse
            Get the number of active websocket connections

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_api_status_connections()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_status_connections(request_options=request_options)
        return _response.data

    async def post_api_storage_download(
        self,
        *,
        marimo_session_id: str,
        namespace: str,
        path: str,
        request_id: RequestId,
        preview: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SuccessResponse:
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
        SuccessResponse
            Download a storage entry

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_storage_download(
                marimo_session_id="Marimo-Session-Id",
                namespace="namespace",
                path="path",
                request_id="requestId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_storage_download(
            marimo_session_id=marimo_session_id,
            namespace=namespace,
            path=path,
            request_id=request_id,
            preview=preview,
            request_options=request_options,
        )
        return _response.data

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
    ) -> SuccessResponse:
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
        SuccessResponse
            List storage entries at a prefix

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_api_storage_list_entries(
                marimo_session_id="Marimo-Session-Id",
                limit=1,
                namespace="namespace",
                request_id="requestId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_storage_list_entries(
            marimo_session_id=marimo_session_id,
            limit=limit,
            namespace=namespace,
            request_id=request_id,
            page_token=page_token,
            prefix=prefix,
            request_options=request_options,
        )
        return _response.data

    async def get_api_usage(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetApiUsageResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApiUsageResponse
            Get the current memory and CPU usage of the application

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_api_usage()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_usage(request_options=request_options)
        return _response.data

    async def get_api_version(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Get the version of the application

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_api_version()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_version(request_options=request_options)
        return _response.data

    @property
    def auth(self):
        if self._auth is None:
            from .auth.client import AsyncAuthClient

            self._auth = AsyncAuthClient(client_wrapper=self._client_wrapper)
        return self._auth
