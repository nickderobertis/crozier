

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.marimo_chatbot_cancel_prompt_output import MarimoChatbotCancelPromptOutput
from ..types.marimo_chatbot_delete_chat_history_output import MarimoChatbotDeleteChatHistoryOutput
from ..types.marimo_chatbot_delete_chat_message_output import MarimoChatbotDeleteChatMessageOutput
from ..types.marimo_chatbot_get_chat_history_output import MarimoChatbotGetChatHistoryOutput
from ..types.marimo_chatbot_get_chat_history_output_messages_item import MarimoChatbotGetChatHistoryOutputMessagesItem
from ..types.marimo_chatbot_send_prompt_output import MarimoChatbotSendPromptOutput
from ..types.marimo_dataframe_download_as_output import MarimoDataframeDownloadAsOutput
from ..types.marimo_dataframe_get_column_values_output import MarimoDataframeGetColumnValuesOutput
from ..types.marimo_dataframe_get_dataframe_output import MarimoDataframeGetDataframeOutput
from ..types.marimo_dataframe_get_size_bytes_output import MarimoDataframeGetSizeBytesOutput
from ..types.marimo_dataframe_search_output import MarimoDataframeSearchOutput
from ..types.marimo_dataframe_search_output_data import MarimoDataframeSearchOutputData
from ..types.marimo_download_load_output import MarimoDownloadLoadOutput
from ..types.marimo_file_browser_list_directory_output import MarimoFileBrowserListDirectoryOutput
from ..types.marimo_file_browser_list_directory_output_files_item import MarimoFileBrowserListDirectoryOutputFilesItem
from ..types.marimo_form_validate_output import MarimoFormValidateOutput
from ..types.marimo_lazy_load_output import MarimoLazyLoadOutput
from ..types.marimo_panel_send_to_widget_output import MarimoPanelSendToWidgetOutput
from ..types.marimo_table_calculate_top_k_rows_output import MarimoTableCalculateTopKRowsOutput
from ..types.marimo_table_download_as_output import MarimoTableDownloadAsOutput
from ..types.marimo_table_get_column_summaries_output import MarimoTableGetColumnSummariesOutput
from ..types.marimo_table_get_column_summaries_output_bin_values_value_item import (
    MarimoTableGetColumnSummariesOutputBinValuesValueItem,
)
from ..types.marimo_table_get_column_summaries_output_data import MarimoTableGetColumnSummariesOutputData
from ..types.marimo_table_get_column_summaries_output_stats_value import MarimoTableGetColumnSummariesOutputStatsValue
from ..types.marimo_table_get_column_summaries_output_value_counts_value_item import (
    MarimoTableGetColumnSummariesOutputValueCountsValueItem,
)
from ..types.marimo_table_get_data_url_output import MarimoTableGetDataUrlOutput
from ..types.marimo_table_get_data_url_output_data_url import MarimoTableGetDataUrlOutputDataUrl
from ..types.marimo_table_get_data_url_output_format import MarimoTableGetDataUrlOutputFormat
from ..types.marimo_table_get_row_ids_output import MarimoTableGetRowIdsOutput
from ..types.marimo_table_get_size_bytes_output import MarimoTableGetSizeBytesOutput
from ..types.marimo_table_preview_column_output import MarimoTablePreviewColumnOutput
from ..types.marimo_table_preview_column_output_stats import MarimoTablePreviewColumnOutputStats
from ..types.marimo_table_search_output import MarimoTableSearchOutput
from ..types.marimo_table_search_output_data import MarimoTableSearchOutputData
from ..types.marimo_table_search_output_raw_data import MarimoTableSearchOutputRawData
from ..types.marimo_table_search_output_total_rows import MarimoTableSearchOutputTotalRows
from .raw_client import AsyncRawRpcOutputClient, RawRpcOutputClient


OMIT = typing.cast(typing.Any, ...)


class RpcOutputClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRpcOutputClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRpcOutputClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRpcOutputClient
        """
        return self._raw_client

    def read_marimo_chatbot_cancel_prompt_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[MarimoChatbotCancelPromptOutput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[MarimoChatbotCancelPromptOutput]
            marimo-chatbot cancel_prompt output accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rpc_output.read_marimo_chatbot_cancel_prompt_output()
        """
        _response = self._raw_client.read_marimo_chatbot_cancel_prompt_output(request_options=request_options)
        return _response.data

    def write_marimo_chatbot_cancel_prompt_output(
        self,
        *,
        request: typing.Optional[MarimoChatbotCancelPromptOutput] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        request : typing.Optional[MarimoChatbotCancelPromptOutput]

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
        client.rpc_output.write_marimo_chatbot_cancel_prompt_output()
        """
        _response = self._raw_client.write_marimo_chatbot_cancel_prompt_output(
            request=request, request_options=request_options
        )
        return _response.data

    def read_marimo_chatbot_delete_chat_history_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[MarimoChatbotDeleteChatHistoryOutput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[MarimoChatbotDeleteChatHistoryOutput]
            marimo-chatbot delete_chat_history output accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rpc_output.read_marimo_chatbot_delete_chat_history_output()
        """
        _response = self._raw_client.read_marimo_chatbot_delete_chat_history_output(request_options=request_options)
        return _response.data

    def write_marimo_chatbot_delete_chat_history_output(
        self,
        *,
        request: typing.Optional[MarimoChatbotDeleteChatHistoryOutput] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        request : typing.Optional[MarimoChatbotDeleteChatHistoryOutput]

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
        client.rpc_output.write_marimo_chatbot_delete_chat_history_output()
        """
        _response = self._raw_client.write_marimo_chatbot_delete_chat_history_output(
            request=request, request_options=request_options
        )
        return _response.data

    def read_marimo_chatbot_delete_chat_message_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[MarimoChatbotDeleteChatMessageOutput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[MarimoChatbotDeleteChatMessageOutput]
            marimo-chatbot delete_chat_message output accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rpc_output.read_marimo_chatbot_delete_chat_message_output()
        """
        _response = self._raw_client.read_marimo_chatbot_delete_chat_message_output(request_options=request_options)
        return _response.data

    def write_marimo_chatbot_delete_chat_message_output(
        self,
        *,
        request: typing.Optional[MarimoChatbotDeleteChatMessageOutput] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        request : typing.Optional[MarimoChatbotDeleteChatMessageOutput]

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
        client.rpc_output.write_marimo_chatbot_delete_chat_message_output()
        """
        _response = self._raw_client.write_marimo_chatbot_delete_chat_message_output(
            request=request, request_options=request_options
        )
        return _response.data

    def read_marimo_chatbot_get_chat_history_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoChatbotGetChatHistoryOutput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoChatbotGetChatHistoryOutput
            marimo-chatbot get_chat_history output accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rpc_output.read_marimo_chatbot_get_chat_history_output()
        """
        _response = self._raw_client.read_marimo_chatbot_get_chat_history_output(request_options=request_options)
        return _response.data

    def write_marimo_chatbot_get_chat_history_output(
        self,
        *,
        messages: typing.Sequence[MarimoChatbotGetChatHistoryOutputMessagesItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        messages : typing.Sequence[MarimoChatbotGetChatHistoryOutputMessagesItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, MarimoChatbotGetChatHistoryOutputMessagesItem

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rpc_output.write_marimo_chatbot_get_chat_history_output(
            messages=[
                MarimoChatbotGetChatHistoryOutputMessagesItem(
                    id="id",
                    role="system",
                    parts=[],
                )
            ],
        )
        """
        _response = self._raw_client.write_marimo_chatbot_get_chat_history_output(
            messages=messages, request_options=request_options
        )
        return _response.data

    def read_marimo_chatbot_send_prompt_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoChatbotSendPromptOutput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoChatbotSendPromptOutput
            marimo-chatbot send_prompt output accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rpc_output.read_marimo_chatbot_send_prompt_output()
        """
        _response = self._raw_client.read_marimo_chatbot_send_prompt_output(request_options=request_options)
        return _response.data

    def write_marimo_chatbot_send_prompt_output(
        self, *, request: MarimoChatbotSendPromptOutput, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : MarimoChatbotSendPromptOutput

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
        client.rpc_output.write_marimo_chatbot_send_prompt_output(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.write_marimo_chatbot_send_prompt_output(
            request=request, request_options=request_options
        )
        return _response.data

    def read_marimo_dataframe_download_as_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoDataframeDownloadAsOutput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoDataframeDownloadAsOutput
            marimo-dataframe download_as output accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rpc_output.read_marimo_dataframe_download_as_output()
        """
        _response = self._raw_client.read_marimo_dataframe_download_as_output(request_options=request_options)
        return _response.data

    def write_marimo_dataframe_download_as_output(
        self,
        *,
        url: str,
        filename: str,
        error: typing.Optional[str] = OMIT,
        missing_packages: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        url : str

        filename : str

        error : typing.Optional[str]

        missing_packages : typing.Optional[typing.Sequence[str]]

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
        client.rpc_output.write_marimo_dataframe_download_as_output(
            url="url",
            filename="filename",
        )
        """
        _response = self._raw_client.write_marimo_dataframe_download_as_output(
            url=url, filename=filename, error=error, missing_packages=missing_packages, request_options=request_options
        )
        return _response.data

    def read_marimo_dataframe_get_column_values_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoDataframeGetColumnValuesOutput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoDataframeGetColumnValuesOutput
            marimo-dataframe get_column_values output accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rpc_output.read_marimo_dataframe_get_column_values_output()
        """
        _response = self._raw_client.read_marimo_dataframe_get_column_values_output(request_options=request_options)
        return _response.data

    def write_marimo_dataframe_get_column_values_output(
        self,
        *,
        values: typing.Sequence[typing.Any],
        too_many_values: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        values : typing.Sequence[typing.Any]

        too_many_values : bool

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
        client.rpc_output.write_marimo_dataframe_get_column_values_output(
            values=[],
            too_many_values=True,
        )
        """
        _response = self._raw_client.write_marimo_dataframe_get_column_values_output(
            values=values, too_many_values=too_many_values, request_options=request_options
        )
        return _response.data

    def read_marimo_dataframe_get_dataframe_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoDataframeGetDataframeOutput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoDataframeGetDataframeOutput
            marimo-dataframe get_dataframe output accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rpc_output.read_marimo_dataframe_get_dataframe_output()
        """
        _response = self._raw_client.read_marimo_dataframe_get_dataframe_output(request_options=request_options)
        return _response.data

    def write_marimo_dataframe_get_dataframe_output(
        self,
        *,
        url: str,
        total_rows: float,
        row_headers: typing.Sequence[typing.Sequence[typing.Any]],
        field_types: typing.Sequence[typing.Sequence[typing.Any]],
        column_types_per_step: typing.Sequence[typing.Sequence[typing.Sequence[typing.Any]]],
        python_code: typing.Optional[str] = OMIT,
        sql_code: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        url : str

        total_rows : float

        row_headers : typing.Sequence[typing.Sequence[typing.Any]]

        field_types : typing.Sequence[typing.Sequence[typing.Any]]

        column_types_per_step : typing.Sequence[typing.Sequence[typing.Sequence[typing.Any]]]

        python_code : typing.Optional[str]

        sql_code : typing.Optional[str]

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
        client.rpc_output.write_marimo_dataframe_get_dataframe_output(
            url="url",
            total_rows=1.1,
            row_headers=[[]],
            field_types=[[]],
            column_types_per_step=[[[]]],
        )
        """
        _response = self._raw_client.write_marimo_dataframe_get_dataframe_output(
            url=url,
            total_rows=total_rows,
            row_headers=row_headers,
            field_types=field_types,
            column_types_per_step=column_types_per_step,
            python_code=python_code,
            sql_code=sql_code,
            request_options=request_options,
        )
        return _response.data

    def read_marimo_dataframe_get_size_bytes_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoDataframeGetSizeBytesOutput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoDataframeGetSizeBytesOutput
            marimo-dataframe get_size_bytes output accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rpc_output.read_marimo_dataframe_get_size_bytes_output()
        """
        _response = self._raw_client.read_marimo_dataframe_get_size_bytes_output(request_options=request_options)
        return _response.data

    def write_marimo_dataframe_get_size_bytes_output(
        self, *, size_bytes: typing.Optional[float] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        size_bytes : typing.Optional[float]

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
        client.rpc_output.write_marimo_dataframe_get_size_bytes_output()
        """
        _response = self._raw_client.write_marimo_dataframe_get_size_bytes_output(
            size_bytes=size_bytes, request_options=request_options
        )
        return _response.data

    def read_marimo_dataframe_search_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoDataframeSearchOutput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoDataframeSearchOutput
            marimo-dataframe search output accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rpc_output.read_marimo_dataframe_search_output()
        """
        _response = self._raw_client.read_marimo_dataframe_search_output(request_options=request_options)
        return _response.data

    def write_marimo_dataframe_search_output(
        self,
        *,
        data: MarimoDataframeSearchOutputData,
        total_rows: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        data : MarimoDataframeSearchOutputData

        total_rows : float

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
        client.rpc_output.write_marimo_dataframe_search_output(
            data="data",
            total_rows=1.1,
        )
        """
        _response = self._raw_client.write_marimo_dataframe_search_output(
            data=data, total_rows=total_rows, request_options=request_options
        )
        return _response.data

    def read_marimo_download_load_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoDownloadLoadOutput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoDownloadLoadOutput
            marimo-download load output accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rpc_output.read_marimo_download_load_output()
        """
        _response = self._raw_client.read_marimo_download_load_output(request_options=request_options)
        return _response.data

    def write_marimo_download_load_output(
        self,
        *,
        data: str,
        filename: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        data : str

        filename : typing.Optional[str]

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
        client.rpc_output.write_marimo_download_load_output(
            data="data",
        )
        """
        _response = self._raw_client.write_marimo_download_load_output(
            data=data, filename=filename, request_options=request_options
        )
        return _response.data

    def read_marimo_file_browser_list_directory_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoFileBrowserListDirectoryOutput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoFileBrowserListDirectoryOutput
            marimo-file-browser list_directory output accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rpc_output.read_marimo_file_browser_list_directory_output()
        """
        _response = self._raw_client.read_marimo_file_browser_list_directory_output(request_options=request_options)
        return _response.data

    def write_marimo_file_browser_list_directory_output(
        self,
        *,
        files: typing.Sequence[MarimoFileBrowserListDirectoryOutputFilesItem],
        total_count: float,
        is_truncated: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        files : typing.Sequence[MarimoFileBrowserListDirectoryOutputFilesItem]

        total_count : float

        is_truncated : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, MarimoFileBrowserListDirectoryOutputFilesItem

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rpc_output.write_marimo_file_browser_list_directory_output(
            files=[
                MarimoFileBrowserListDirectoryOutputFilesItem(
                    id="id",
                    path="path",
                    name="name",
                    is_directory=True,
                )
            ],
            total_count=1.1,
            is_truncated=True,
        )
        """
        _response = self._raw_client.write_marimo_file_browser_list_directory_output(
            files=files, total_count=total_count, is_truncated=is_truncated, request_options=request_options
        )
        return _response.data

    def read_marimo_form_validate_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[MarimoFormValidateOutput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[MarimoFormValidateOutput]
            marimo-form validate output accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rpc_output.read_marimo_form_validate_output()
        """
        _response = self._raw_client.read_marimo_form_validate_output(request_options=request_options)
        return _response.data

    def write_marimo_form_validate_output(
        self,
        *,
        request: typing.Optional[MarimoFormValidateOutput] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        request : typing.Optional[MarimoFormValidateOutput]

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
        client.rpc_output.write_marimo_form_validate_output(
            request="string",
        )
        """
        _response = self._raw_client.write_marimo_form_validate_output(request=request, request_options=request_options)
        return _response.data

    def read_marimo_lazy_load_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoLazyLoadOutput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoLazyLoadOutput
            marimo-lazy load output accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rpc_output.read_marimo_lazy_load_output()
        """
        _response = self._raw_client.read_marimo_lazy_load_output(request_options=request_options)
        return _response.data

    def write_marimo_lazy_load_output(
        self, *, html: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        html : str

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
        client.rpc_output.write_marimo_lazy_load_output(
            html="html",
        )
        """
        _response = self._raw_client.write_marimo_lazy_load_output(html=html, request_options=request_options)
        return _response.data

    def read_marimo_panel_send_to_widget_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[MarimoPanelSendToWidgetOutput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[MarimoPanelSendToWidgetOutput]
            marimo-panel send_to_widget output accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rpc_output.read_marimo_panel_send_to_widget_output()
        """
        _response = self._raw_client.read_marimo_panel_send_to_widget_output(request_options=request_options)
        return _response.data

    def write_marimo_panel_send_to_widget_output(
        self,
        *,
        request: typing.Optional[MarimoPanelSendToWidgetOutput] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        request : typing.Optional[MarimoPanelSendToWidgetOutput]

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
        client.rpc_output.write_marimo_panel_send_to_widget_output()
        """
        _response = self._raw_client.write_marimo_panel_send_to_widget_output(
            request=request, request_options=request_options
        )
        return _response.data

    def read_marimo_table_calculate_top_k_rows_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoTableCalculateTopKRowsOutput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoTableCalculateTopKRowsOutput
            marimo-table calculate_top_k_rows output accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rpc_output.read_marimo_table_calculate_top_k_rows_output()
        """
        _response = self._raw_client.read_marimo_table_calculate_top_k_rows_output(request_options=request_options)
        return _response.data

    def write_marimo_table_calculate_top_k_rows_output(
        self,
        *,
        data: typing.Sequence[typing.Sequence[typing.Any]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        data : typing.Sequence[typing.Sequence[typing.Any]]

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
        client.rpc_output.write_marimo_table_calculate_top_k_rows_output(
            data=[[]],
        )
        """
        _response = self._raw_client.write_marimo_table_calculate_top_k_rows_output(
            data=data, request_options=request_options
        )
        return _response.data

    def read_marimo_table_download_as_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoTableDownloadAsOutput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoTableDownloadAsOutput
            marimo-table download_as output accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rpc_output.read_marimo_table_download_as_output()
        """
        _response = self._raw_client.read_marimo_table_download_as_output(request_options=request_options)
        return _response.data

    def write_marimo_table_download_as_output(
        self,
        *,
        url: str,
        filename: str,
        error: typing.Optional[str] = OMIT,
        missing_packages: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        url : str

        filename : str

        error : typing.Optional[str]

        missing_packages : typing.Optional[typing.Sequence[str]]

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
        client.rpc_output.write_marimo_table_download_as_output(
            url="url",
            filename="filename",
        )
        """
        _response = self._raw_client.write_marimo_table_download_as_output(
            url=url, filename=filename, error=error, missing_packages=missing_packages, request_options=request_options
        )
        return _response.data

    def read_marimo_table_get_column_summaries_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoTableGetColumnSummariesOutput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoTableGetColumnSummariesOutput
            marimo-table get_column_summaries output accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rpc_output.read_marimo_table_get_column_summaries_output()
        """
        _response = self._raw_client.read_marimo_table_get_column_summaries_output(request_options=request_options)
        return _response.data

    def write_marimo_table_get_column_summaries_output(
        self,
        *,
        stats: typing.Dict[str, MarimoTableGetColumnSummariesOutputStatsValue],
        bin_values: typing.Dict[str, typing.Sequence[MarimoTableGetColumnSummariesOutputBinValuesValueItem]],
        value_counts: typing.Dict[str, typing.Sequence[MarimoTableGetColumnSummariesOutputValueCountsValueItem]],
        show_charts: bool,
        data: typing.Optional[MarimoTableGetColumnSummariesOutputData] = OMIT,
        is_disabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        stats : typing.Dict[str, MarimoTableGetColumnSummariesOutputStatsValue]

        bin_values : typing.Dict[str, typing.Sequence[MarimoTableGetColumnSummariesOutputBinValuesValueItem]]

        value_counts : typing.Dict[str, typing.Sequence[MarimoTableGetColumnSummariesOutputValueCountsValueItem]]

        show_charts : bool

        data : typing.Optional[MarimoTableGetColumnSummariesOutputData]

        is_disabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import (
            FernApi,
            MarimoTableGetColumnSummariesOutputBinValuesValueItem,
            MarimoTableGetColumnSummariesOutputStatsValue,
            MarimoTableGetColumnSummariesOutputValueCountsValueItem,
        )

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rpc_output.write_marimo_table_get_column_summaries_output(
            stats={"key": MarimoTableGetColumnSummariesOutputStatsValue()},
            bin_values={
                "key": [
                    MarimoTableGetColumnSummariesOutputBinValuesValueItem(
                        bin_start=1.1,
                        bin_end=1.1,
                        count=1.1,
                    )
                ]
            },
            value_counts={
                "key": [
                    MarimoTableGetColumnSummariesOutputValueCountsValueItem(
                        value="value",
                        count=1.1,
                    )
                ]
            },
            show_charts=True,
        )
        """
        _response = self._raw_client.write_marimo_table_get_column_summaries_output(
            stats=stats,
            bin_values=bin_values,
            value_counts=value_counts,
            show_charts=show_charts,
            data=data,
            is_disabled=is_disabled,
            request_options=request_options,
        )
        return _response.data

    def read_marimo_table_get_data_url_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoTableGetDataUrlOutput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoTableGetDataUrlOutput
            marimo-table get_data_url output accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rpc_output.read_marimo_table_get_data_url_output()
        """
        _response = self._raw_client.read_marimo_table_get_data_url_output(request_options=request_options)
        return _response.data

    def write_marimo_table_get_data_url_output(
        self,
        *,
        data_url: MarimoTableGetDataUrlOutputDataUrl,
        format: MarimoTableGetDataUrlOutputFormat,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        data_url : MarimoTableGetDataUrlOutputDataUrl

        format : MarimoTableGetDataUrlOutputFormat

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
        client.rpc_output.write_marimo_table_get_data_url_output(
            data_url="data_url",
            format="csv",
        )
        """
        _response = self._raw_client.write_marimo_table_get_data_url_output(
            data_url=data_url, format=format, request_options=request_options
        )
        return _response.data

    def read_marimo_table_get_row_ids_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoTableGetRowIdsOutput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoTableGetRowIdsOutput
            marimo-table get_row_ids output accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rpc_output.read_marimo_table_get_row_ids_output()
        """
        _response = self._raw_client.read_marimo_table_get_row_ids_output(request_options=request_options)
        return _response.data

    def write_marimo_table_get_row_ids_output(
        self,
        *,
        row_ids: typing.Sequence[float],
        all_rows: bool,
        error: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        row_ids : typing.Sequence[float]

        all_rows : bool

        error : typing.Optional[str]

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
        client.rpc_output.write_marimo_table_get_row_ids_output(
            row_ids=[1.1],
            all_rows=True,
        )
        """
        _response = self._raw_client.write_marimo_table_get_row_ids_output(
            row_ids=row_ids, all_rows=all_rows, error=error, request_options=request_options
        )
        return _response.data

    def read_marimo_table_get_size_bytes_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoTableGetSizeBytesOutput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoTableGetSizeBytesOutput
            marimo-table get_size_bytes output accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rpc_output.read_marimo_table_get_size_bytes_output()
        """
        _response = self._raw_client.read_marimo_table_get_size_bytes_output(request_options=request_options)
        return _response.data

    def write_marimo_table_get_size_bytes_output(
        self, *, size_bytes: typing.Optional[float] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        size_bytes : typing.Optional[float]

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
        client.rpc_output.write_marimo_table_get_size_bytes_output()
        """
        _response = self._raw_client.write_marimo_table_get_size_bytes_output(
            size_bytes=size_bytes, request_options=request_options
        )
        return _response.data

    def read_marimo_table_preview_column_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoTablePreviewColumnOutput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoTablePreviewColumnOutput
            marimo-table preview_column output accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rpc_output.read_marimo_table_preview_column_output()
        """
        _response = self._raw_client.read_marimo_table_preview_column_output(request_options=request_options)
        return _response.data

    def write_marimo_table_preview_column_output(
        self,
        *,
        chart_spec: typing.Optional[str] = OMIT,
        chart_code: typing.Optional[str] = OMIT,
        error: typing.Optional[str] = OMIT,
        missing_packages: typing.Optional[typing.Sequence[str]] = OMIT,
        stats: typing.Optional[MarimoTablePreviewColumnOutputStats] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        chart_spec : typing.Optional[str]

        chart_code : typing.Optional[str]

        error : typing.Optional[str]

        missing_packages : typing.Optional[typing.Sequence[str]]

        stats : typing.Optional[MarimoTablePreviewColumnOutputStats]

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
        client.rpc_output.write_marimo_table_preview_column_output()
        """
        _response = self._raw_client.write_marimo_table_preview_column_output(
            chart_spec=chart_spec,
            chart_code=chart_code,
            error=error,
            missing_packages=missing_packages,
            stats=stats,
            request_options=request_options,
        )
        return _response.data

    def read_marimo_table_search_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoTableSearchOutput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoTableSearchOutput
            marimo-table search output accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rpc_output.read_marimo_table_search_output()
        """
        _response = self._raw_client.read_marimo_table_search_output(request_options=request_options)
        return _response.data

    def write_marimo_table_search_output(
        self,
        *,
        data: MarimoTableSearchOutputData,
        total_rows: MarimoTableSearchOutputTotalRows,
        cell_styles: typing.Optional[
            typing.Dict[str, typing.Optional[typing.Dict[str, typing.Optional[typing.Dict[str, typing.Any]]]]]
        ] = OMIT,
        cell_hover_texts: typing.Optional[
            typing.Dict[str, typing.Optional[typing.Dict[str, typing.Optional[str]]]]
        ] = OMIT,
        raw_data: typing.Optional[MarimoTableSearchOutputRawData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        data : MarimoTableSearchOutputData

        total_rows : MarimoTableSearchOutputTotalRows

        cell_styles : typing.Optional[typing.Dict[str, typing.Optional[typing.Dict[str, typing.Optional[typing.Dict[str, typing.Any]]]]]]

        cell_hover_texts : typing.Optional[typing.Dict[str, typing.Optional[typing.Dict[str, typing.Optional[str]]]]]

        raw_data : typing.Optional[MarimoTableSearchOutputRawData]

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
        client.rpc_output.write_marimo_table_search_output(
            data="data",
            total_rows="too_many",
        )
        """
        _response = self._raw_client.write_marimo_table_search_output(
            data=data,
            total_rows=total_rows,
            cell_styles=cell_styles,
            cell_hover_texts=cell_hover_texts,
            raw_data=raw_data,
            request_options=request_options,
        )
        return _response.data


class AsyncRpcOutputClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRpcOutputClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRpcOutputClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRpcOutputClient
        """
        return self._raw_client

    async def read_marimo_chatbot_cancel_prompt_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[MarimoChatbotCancelPromptOutput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[MarimoChatbotCancelPromptOutput]
            marimo-chatbot cancel_prompt output accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rpc_output.read_marimo_chatbot_cancel_prompt_output()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_chatbot_cancel_prompt_output(request_options=request_options)
        return _response.data

    async def write_marimo_chatbot_cancel_prompt_output(
        self,
        *,
        request: typing.Optional[MarimoChatbotCancelPromptOutput] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        request : typing.Optional[MarimoChatbotCancelPromptOutput]

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
            await client.rpc_output.write_marimo_chatbot_cancel_prompt_output()


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_chatbot_cancel_prompt_output(
            request=request, request_options=request_options
        )
        return _response.data

    async def read_marimo_chatbot_delete_chat_history_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[MarimoChatbotDeleteChatHistoryOutput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[MarimoChatbotDeleteChatHistoryOutput]
            marimo-chatbot delete_chat_history output accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rpc_output.read_marimo_chatbot_delete_chat_history_output()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_chatbot_delete_chat_history_output(
            request_options=request_options
        )
        return _response.data

    async def write_marimo_chatbot_delete_chat_history_output(
        self,
        *,
        request: typing.Optional[MarimoChatbotDeleteChatHistoryOutput] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        request : typing.Optional[MarimoChatbotDeleteChatHistoryOutput]

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
            await client.rpc_output.write_marimo_chatbot_delete_chat_history_output()


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_chatbot_delete_chat_history_output(
            request=request, request_options=request_options
        )
        return _response.data

    async def read_marimo_chatbot_delete_chat_message_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[MarimoChatbotDeleteChatMessageOutput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[MarimoChatbotDeleteChatMessageOutput]
            marimo-chatbot delete_chat_message output accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rpc_output.read_marimo_chatbot_delete_chat_message_output()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_chatbot_delete_chat_message_output(
            request_options=request_options
        )
        return _response.data

    async def write_marimo_chatbot_delete_chat_message_output(
        self,
        *,
        request: typing.Optional[MarimoChatbotDeleteChatMessageOutput] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        request : typing.Optional[MarimoChatbotDeleteChatMessageOutput]

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
            await client.rpc_output.write_marimo_chatbot_delete_chat_message_output()


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_chatbot_delete_chat_message_output(
            request=request, request_options=request_options
        )
        return _response.data

    async def read_marimo_chatbot_get_chat_history_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoChatbotGetChatHistoryOutput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoChatbotGetChatHistoryOutput
            marimo-chatbot get_chat_history output accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rpc_output.read_marimo_chatbot_get_chat_history_output()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_chatbot_get_chat_history_output(request_options=request_options)
        return _response.data

    async def write_marimo_chatbot_get_chat_history_output(
        self,
        *,
        messages: typing.Sequence[MarimoChatbotGetChatHistoryOutputMessagesItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        messages : typing.Sequence[MarimoChatbotGetChatHistoryOutputMessagesItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, MarimoChatbotGetChatHistoryOutputMessagesItem

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rpc_output.write_marimo_chatbot_get_chat_history_output(
                messages=[
                    MarimoChatbotGetChatHistoryOutputMessagesItem(
                        id="id",
                        role="system",
                        parts=[],
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_chatbot_get_chat_history_output(
            messages=messages, request_options=request_options
        )
        return _response.data

    async def read_marimo_chatbot_send_prompt_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoChatbotSendPromptOutput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoChatbotSendPromptOutput
            marimo-chatbot send_prompt output accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rpc_output.read_marimo_chatbot_send_prompt_output()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_chatbot_send_prompt_output(request_options=request_options)
        return _response.data

    async def write_marimo_chatbot_send_prompt_output(
        self, *, request: MarimoChatbotSendPromptOutput, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : MarimoChatbotSendPromptOutput

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
            await client.rpc_output.write_marimo_chatbot_send_prompt_output(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_chatbot_send_prompt_output(
            request=request, request_options=request_options
        )
        return _response.data

    async def read_marimo_dataframe_download_as_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoDataframeDownloadAsOutput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoDataframeDownloadAsOutput
            marimo-dataframe download_as output accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rpc_output.read_marimo_dataframe_download_as_output()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_dataframe_download_as_output(request_options=request_options)
        return _response.data

    async def write_marimo_dataframe_download_as_output(
        self,
        *,
        url: str,
        filename: str,
        error: typing.Optional[str] = OMIT,
        missing_packages: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        url : str

        filename : str

        error : typing.Optional[str]

        missing_packages : typing.Optional[typing.Sequence[str]]

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
            await client.rpc_output.write_marimo_dataframe_download_as_output(
                url="url",
                filename="filename",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_dataframe_download_as_output(
            url=url, filename=filename, error=error, missing_packages=missing_packages, request_options=request_options
        )
        return _response.data

    async def read_marimo_dataframe_get_column_values_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoDataframeGetColumnValuesOutput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoDataframeGetColumnValuesOutput
            marimo-dataframe get_column_values output accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rpc_output.read_marimo_dataframe_get_column_values_output()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_dataframe_get_column_values_output(
            request_options=request_options
        )
        return _response.data

    async def write_marimo_dataframe_get_column_values_output(
        self,
        *,
        values: typing.Sequence[typing.Any],
        too_many_values: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        values : typing.Sequence[typing.Any]

        too_many_values : bool

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
            await client.rpc_output.write_marimo_dataframe_get_column_values_output(
                values=[],
                too_many_values=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_dataframe_get_column_values_output(
            values=values, too_many_values=too_many_values, request_options=request_options
        )
        return _response.data

    async def read_marimo_dataframe_get_dataframe_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoDataframeGetDataframeOutput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoDataframeGetDataframeOutput
            marimo-dataframe get_dataframe output accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rpc_output.read_marimo_dataframe_get_dataframe_output()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_dataframe_get_dataframe_output(request_options=request_options)
        return _response.data

    async def write_marimo_dataframe_get_dataframe_output(
        self,
        *,
        url: str,
        total_rows: float,
        row_headers: typing.Sequence[typing.Sequence[typing.Any]],
        field_types: typing.Sequence[typing.Sequence[typing.Any]],
        column_types_per_step: typing.Sequence[typing.Sequence[typing.Sequence[typing.Any]]],
        python_code: typing.Optional[str] = OMIT,
        sql_code: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        url : str

        total_rows : float

        row_headers : typing.Sequence[typing.Sequence[typing.Any]]

        field_types : typing.Sequence[typing.Sequence[typing.Any]]

        column_types_per_step : typing.Sequence[typing.Sequence[typing.Sequence[typing.Any]]]

        python_code : typing.Optional[str]

        sql_code : typing.Optional[str]

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
            await client.rpc_output.write_marimo_dataframe_get_dataframe_output(
                url="url",
                total_rows=1.1,
                row_headers=[[]],
                field_types=[[]],
                column_types_per_step=[[[]]],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_dataframe_get_dataframe_output(
            url=url,
            total_rows=total_rows,
            row_headers=row_headers,
            field_types=field_types,
            column_types_per_step=column_types_per_step,
            python_code=python_code,
            sql_code=sql_code,
            request_options=request_options,
        )
        return _response.data

    async def read_marimo_dataframe_get_size_bytes_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoDataframeGetSizeBytesOutput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoDataframeGetSizeBytesOutput
            marimo-dataframe get_size_bytes output accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rpc_output.read_marimo_dataframe_get_size_bytes_output()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_dataframe_get_size_bytes_output(request_options=request_options)
        return _response.data

    async def write_marimo_dataframe_get_size_bytes_output(
        self, *, size_bytes: typing.Optional[float] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        size_bytes : typing.Optional[float]

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
            await client.rpc_output.write_marimo_dataframe_get_size_bytes_output()


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_dataframe_get_size_bytes_output(
            size_bytes=size_bytes, request_options=request_options
        )
        return _response.data

    async def read_marimo_dataframe_search_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoDataframeSearchOutput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoDataframeSearchOutput
            marimo-dataframe search output accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rpc_output.read_marimo_dataframe_search_output()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_dataframe_search_output(request_options=request_options)
        return _response.data

    async def write_marimo_dataframe_search_output(
        self,
        *,
        data: MarimoDataframeSearchOutputData,
        total_rows: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        data : MarimoDataframeSearchOutputData

        total_rows : float

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
            await client.rpc_output.write_marimo_dataframe_search_output(
                data="data",
                total_rows=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_dataframe_search_output(
            data=data, total_rows=total_rows, request_options=request_options
        )
        return _response.data

    async def read_marimo_download_load_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoDownloadLoadOutput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoDownloadLoadOutput
            marimo-download load output accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rpc_output.read_marimo_download_load_output()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_download_load_output(request_options=request_options)
        return _response.data

    async def write_marimo_download_load_output(
        self,
        *,
        data: str,
        filename: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        data : str

        filename : typing.Optional[str]

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
            await client.rpc_output.write_marimo_download_load_output(
                data="data",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_download_load_output(
            data=data, filename=filename, request_options=request_options
        )
        return _response.data

    async def read_marimo_file_browser_list_directory_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoFileBrowserListDirectoryOutput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoFileBrowserListDirectoryOutput
            marimo-file-browser list_directory output accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rpc_output.read_marimo_file_browser_list_directory_output()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_file_browser_list_directory_output(
            request_options=request_options
        )
        return _response.data

    async def write_marimo_file_browser_list_directory_output(
        self,
        *,
        files: typing.Sequence[MarimoFileBrowserListDirectoryOutputFilesItem],
        total_count: float,
        is_truncated: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        files : typing.Sequence[MarimoFileBrowserListDirectoryOutputFilesItem]

        total_count : float

        is_truncated : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, MarimoFileBrowserListDirectoryOutputFilesItem

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rpc_output.write_marimo_file_browser_list_directory_output(
                files=[
                    MarimoFileBrowserListDirectoryOutputFilesItem(
                        id="id",
                        path="path",
                        name="name",
                        is_directory=True,
                    )
                ],
                total_count=1.1,
                is_truncated=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_file_browser_list_directory_output(
            files=files, total_count=total_count, is_truncated=is_truncated, request_options=request_options
        )
        return _response.data

    async def read_marimo_form_validate_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[MarimoFormValidateOutput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[MarimoFormValidateOutput]
            marimo-form validate output accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rpc_output.read_marimo_form_validate_output()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_form_validate_output(request_options=request_options)
        return _response.data

    async def write_marimo_form_validate_output(
        self,
        *,
        request: typing.Optional[MarimoFormValidateOutput] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        request : typing.Optional[MarimoFormValidateOutput]

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
            await client.rpc_output.write_marimo_form_validate_output(
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_form_validate_output(
            request=request, request_options=request_options
        )
        return _response.data

    async def read_marimo_lazy_load_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoLazyLoadOutput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoLazyLoadOutput
            marimo-lazy load output accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rpc_output.read_marimo_lazy_load_output()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_lazy_load_output(request_options=request_options)
        return _response.data

    async def write_marimo_lazy_load_output(
        self, *, html: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        html : str

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
            await client.rpc_output.write_marimo_lazy_load_output(
                html="html",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_lazy_load_output(html=html, request_options=request_options)
        return _response.data

    async def read_marimo_panel_send_to_widget_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[MarimoPanelSendToWidgetOutput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[MarimoPanelSendToWidgetOutput]
            marimo-panel send_to_widget output accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rpc_output.read_marimo_panel_send_to_widget_output()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_panel_send_to_widget_output(request_options=request_options)
        return _response.data

    async def write_marimo_panel_send_to_widget_output(
        self,
        *,
        request: typing.Optional[MarimoPanelSendToWidgetOutput] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        request : typing.Optional[MarimoPanelSendToWidgetOutput]

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
            await client.rpc_output.write_marimo_panel_send_to_widget_output()


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_panel_send_to_widget_output(
            request=request, request_options=request_options
        )
        return _response.data

    async def read_marimo_table_calculate_top_k_rows_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoTableCalculateTopKRowsOutput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoTableCalculateTopKRowsOutput
            marimo-table calculate_top_k_rows output accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rpc_output.read_marimo_table_calculate_top_k_rows_output()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_table_calculate_top_k_rows_output(
            request_options=request_options
        )
        return _response.data

    async def write_marimo_table_calculate_top_k_rows_output(
        self,
        *,
        data: typing.Sequence[typing.Sequence[typing.Any]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        data : typing.Sequence[typing.Sequence[typing.Any]]

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
            await client.rpc_output.write_marimo_table_calculate_top_k_rows_output(
                data=[[]],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_table_calculate_top_k_rows_output(
            data=data, request_options=request_options
        )
        return _response.data

    async def read_marimo_table_download_as_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoTableDownloadAsOutput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoTableDownloadAsOutput
            marimo-table download_as output accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rpc_output.read_marimo_table_download_as_output()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_table_download_as_output(request_options=request_options)
        return _response.data

    async def write_marimo_table_download_as_output(
        self,
        *,
        url: str,
        filename: str,
        error: typing.Optional[str] = OMIT,
        missing_packages: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        url : str

        filename : str

        error : typing.Optional[str]

        missing_packages : typing.Optional[typing.Sequence[str]]

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
            await client.rpc_output.write_marimo_table_download_as_output(
                url="url",
                filename="filename",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_table_download_as_output(
            url=url, filename=filename, error=error, missing_packages=missing_packages, request_options=request_options
        )
        return _response.data

    async def read_marimo_table_get_column_summaries_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoTableGetColumnSummariesOutput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoTableGetColumnSummariesOutput
            marimo-table get_column_summaries output accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rpc_output.read_marimo_table_get_column_summaries_output()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_table_get_column_summaries_output(
            request_options=request_options
        )
        return _response.data

    async def write_marimo_table_get_column_summaries_output(
        self,
        *,
        stats: typing.Dict[str, MarimoTableGetColumnSummariesOutputStatsValue],
        bin_values: typing.Dict[str, typing.Sequence[MarimoTableGetColumnSummariesOutputBinValuesValueItem]],
        value_counts: typing.Dict[str, typing.Sequence[MarimoTableGetColumnSummariesOutputValueCountsValueItem]],
        show_charts: bool,
        data: typing.Optional[MarimoTableGetColumnSummariesOutputData] = OMIT,
        is_disabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        stats : typing.Dict[str, MarimoTableGetColumnSummariesOutputStatsValue]

        bin_values : typing.Dict[str, typing.Sequence[MarimoTableGetColumnSummariesOutputBinValuesValueItem]]

        value_counts : typing.Dict[str, typing.Sequence[MarimoTableGetColumnSummariesOutputValueCountsValueItem]]

        show_charts : bool

        data : typing.Optional[MarimoTableGetColumnSummariesOutputData]

        is_disabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            MarimoTableGetColumnSummariesOutputBinValuesValueItem,
            MarimoTableGetColumnSummariesOutputStatsValue,
            MarimoTableGetColumnSummariesOutputValueCountsValueItem,
        )

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rpc_output.write_marimo_table_get_column_summaries_output(
                stats={"key": MarimoTableGetColumnSummariesOutputStatsValue()},
                bin_values={
                    "key": [
                        MarimoTableGetColumnSummariesOutputBinValuesValueItem(
                            bin_start=1.1,
                            bin_end=1.1,
                            count=1.1,
                        )
                    ]
                },
                value_counts={
                    "key": [
                        MarimoTableGetColumnSummariesOutputValueCountsValueItem(
                            value="value",
                            count=1.1,
                        )
                    ]
                },
                show_charts=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_table_get_column_summaries_output(
            stats=stats,
            bin_values=bin_values,
            value_counts=value_counts,
            show_charts=show_charts,
            data=data,
            is_disabled=is_disabled,
            request_options=request_options,
        )
        return _response.data

    async def read_marimo_table_get_data_url_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoTableGetDataUrlOutput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoTableGetDataUrlOutput
            marimo-table get_data_url output accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rpc_output.read_marimo_table_get_data_url_output()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_table_get_data_url_output(request_options=request_options)
        return _response.data

    async def write_marimo_table_get_data_url_output(
        self,
        *,
        data_url: MarimoTableGetDataUrlOutputDataUrl,
        format: MarimoTableGetDataUrlOutputFormat,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        data_url : MarimoTableGetDataUrlOutputDataUrl

        format : MarimoTableGetDataUrlOutputFormat

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
            await client.rpc_output.write_marimo_table_get_data_url_output(
                data_url="data_url",
                format="csv",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_table_get_data_url_output(
            data_url=data_url, format=format, request_options=request_options
        )
        return _response.data

    async def read_marimo_table_get_row_ids_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoTableGetRowIdsOutput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoTableGetRowIdsOutput
            marimo-table get_row_ids output accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rpc_output.read_marimo_table_get_row_ids_output()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_table_get_row_ids_output(request_options=request_options)
        return _response.data

    async def write_marimo_table_get_row_ids_output(
        self,
        *,
        row_ids: typing.Sequence[float],
        all_rows: bool,
        error: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        row_ids : typing.Sequence[float]

        all_rows : bool

        error : typing.Optional[str]

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
            await client.rpc_output.write_marimo_table_get_row_ids_output(
                row_ids=[1.1],
                all_rows=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_table_get_row_ids_output(
            row_ids=row_ids, all_rows=all_rows, error=error, request_options=request_options
        )
        return _response.data

    async def read_marimo_table_get_size_bytes_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoTableGetSizeBytesOutput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoTableGetSizeBytesOutput
            marimo-table get_size_bytes output accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rpc_output.read_marimo_table_get_size_bytes_output()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_table_get_size_bytes_output(request_options=request_options)
        return _response.data

    async def write_marimo_table_get_size_bytes_output(
        self, *, size_bytes: typing.Optional[float] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        size_bytes : typing.Optional[float]

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
            await client.rpc_output.write_marimo_table_get_size_bytes_output()


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_table_get_size_bytes_output(
            size_bytes=size_bytes, request_options=request_options
        )
        return _response.data

    async def read_marimo_table_preview_column_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoTablePreviewColumnOutput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoTablePreviewColumnOutput
            marimo-table preview_column output accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rpc_output.read_marimo_table_preview_column_output()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_table_preview_column_output(request_options=request_options)
        return _response.data

    async def write_marimo_table_preview_column_output(
        self,
        *,
        chart_spec: typing.Optional[str] = OMIT,
        chart_code: typing.Optional[str] = OMIT,
        error: typing.Optional[str] = OMIT,
        missing_packages: typing.Optional[typing.Sequence[str]] = OMIT,
        stats: typing.Optional[MarimoTablePreviewColumnOutputStats] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        chart_spec : typing.Optional[str]

        chart_code : typing.Optional[str]

        error : typing.Optional[str]

        missing_packages : typing.Optional[typing.Sequence[str]]

        stats : typing.Optional[MarimoTablePreviewColumnOutputStats]

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
            await client.rpc_output.write_marimo_table_preview_column_output()


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_table_preview_column_output(
            chart_spec=chart_spec,
            chart_code=chart_code,
            error=error,
            missing_packages=missing_packages,
            stats=stats,
            request_options=request_options,
        )
        return _response.data

    async def read_marimo_table_search_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoTableSearchOutput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoTableSearchOutput
            marimo-table search output accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rpc_output.read_marimo_table_search_output()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_table_search_output(request_options=request_options)
        return _response.data

    async def write_marimo_table_search_output(
        self,
        *,
        data: MarimoTableSearchOutputData,
        total_rows: MarimoTableSearchOutputTotalRows,
        cell_styles: typing.Optional[
            typing.Dict[str, typing.Optional[typing.Dict[str, typing.Optional[typing.Dict[str, typing.Any]]]]]
        ] = OMIT,
        cell_hover_texts: typing.Optional[
            typing.Dict[str, typing.Optional[typing.Dict[str, typing.Optional[str]]]]
        ] = OMIT,
        raw_data: typing.Optional[MarimoTableSearchOutputRawData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        data : MarimoTableSearchOutputData

        total_rows : MarimoTableSearchOutputTotalRows

        cell_styles : typing.Optional[typing.Dict[str, typing.Optional[typing.Dict[str, typing.Optional[typing.Dict[str, typing.Any]]]]]]

        cell_hover_texts : typing.Optional[typing.Dict[str, typing.Optional[typing.Dict[str, typing.Optional[str]]]]]

        raw_data : typing.Optional[MarimoTableSearchOutputRawData]

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
            await client.rpc_output.write_marimo_table_search_output(
                data="data",
                total_rows="too_many",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_table_search_output(
            data=data,
            total_rows=total_rows,
            cell_styles=cell_styles,
            cell_hover_texts=cell_hover_texts,
            raw_data=raw_data,
            request_options=request_options,
        )
        return _response.data
