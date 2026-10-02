

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.marimo_chatbot_cancel_prompt_input import MarimoChatbotCancelPromptInput
from ..types.marimo_chatbot_delete_chat_history_input import MarimoChatbotDeleteChatHistoryInput
from ..types.marimo_chatbot_delete_chat_message_input import MarimoChatbotDeleteChatMessageInput
from ..types.marimo_chatbot_get_chat_history_input import MarimoChatbotGetChatHistoryInput
from ..types.marimo_chatbot_send_prompt_input import MarimoChatbotSendPromptInput
from ..types.marimo_chatbot_send_prompt_input_config import MarimoChatbotSendPromptInputConfig
from ..types.marimo_chatbot_send_prompt_input_messages_item import MarimoChatbotSendPromptInputMessagesItem
from ..types.marimo_dataframe_download_as_input import MarimoDataframeDownloadAsInput
from ..types.marimo_dataframe_download_as_input_format import MarimoDataframeDownloadAsInputFormat
from ..types.marimo_dataframe_get_column_values_input import MarimoDataframeGetColumnValuesInput
from ..types.marimo_dataframe_get_dataframe_input import MarimoDataframeGetDataframeInput
from ..types.marimo_dataframe_get_size_bytes_input import MarimoDataframeGetSizeBytesInput
from ..types.marimo_dataframe_search_input import MarimoDataframeSearchInput
from ..types.marimo_dataframe_search_input_def_schema0 import MarimoDataframeSearchInputDefSchema0
from ..types.marimo_dataframe_search_input_sort_item import MarimoDataframeSearchInputSortItem
from ..types.marimo_download_load_input import MarimoDownloadLoadInput
from ..types.marimo_file_browser_list_directory_input import MarimoFileBrowserListDirectoryInput
from ..types.marimo_form_validate_input import MarimoFormValidateInput
from ..types.marimo_lazy_load_input import MarimoLazyLoadInput
from ..types.marimo_panel_send_to_widget_input import MarimoPanelSendToWidgetInput
from ..types.marimo_table_calculate_top_k_rows_input import MarimoTableCalculateTopKRowsInput
from ..types.marimo_table_download_as_input import MarimoTableDownloadAsInput
from ..types.marimo_table_download_as_input_format import MarimoTableDownloadAsInputFormat
from ..types.marimo_table_get_column_summaries_input import MarimoTableGetColumnSummariesInput
from ..types.marimo_table_get_data_url_input import MarimoTableGetDataUrlInput
from ..types.marimo_table_get_row_ids_input import MarimoTableGetRowIdsInput
from ..types.marimo_table_get_size_bytes_input import MarimoTableGetSizeBytesInput
from ..types.marimo_table_preview_column_input import MarimoTablePreviewColumnInput
from ..types.marimo_table_search_input import MarimoTableSearchInput
from ..types.marimo_table_search_input_def_schema0 import MarimoTableSearchInputDefSchema0
from ..types.marimo_table_search_input_sort_item import MarimoTableSearchInputSortItem
from .raw_client import AsyncRawRpcInputClient, RawRpcInputClient


OMIT = typing.cast(typing.Any, ...)


class RpcInputClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRpcInputClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRpcInputClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRpcInputClient
        """
        return self._raw_client

    def read_marimo_chatbot_cancel_prompt_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoChatbotCancelPromptInput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoChatbotCancelPromptInput
            marimo-chatbot cancel_prompt input accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rpc_input.read_marimo_chatbot_cancel_prompt_input()
        """
        _response = self._raw_client.read_marimo_chatbot_cancel_prompt_input(request_options=request_options)
        return _response.data

    def write_marimo_chatbot_cancel_prompt_input(
        self, *, request_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request_id : str

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
        client.rpc_input.write_marimo_chatbot_cancel_prompt_input(
            request_id="request_id",
        )
        """
        _response = self._raw_client.write_marimo_chatbot_cancel_prompt_input(
            request_id=request_id, request_options=request_options
        )
        return _response.data

    def read_marimo_chatbot_delete_chat_history_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoChatbotDeleteChatHistoryInput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoChatbotDeleteChatHistoryInput
            marimo-chatbot delete_chat_history input accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rpc_input.read_marimo_chatbot_delete_chat_history_input()
        """
        _response = self._raw_client.read_marimo_chatbot_delete_chat_history_input(request_options=request_options)
        return _response.data

    def write_marimo_chatbot_delete_chat_history_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
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
        client.rpc_input.write_marimo_chatbot_delete_chat_history_input()
        """
        _response = self._raw_client.write_marimo_chatbot_delete_chat_history_input(request_options=request_options)
        return _response.data

    def read_marimo_chatbot_delete_chat_message_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoChatbotDeleteChatMessageInput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoChatbotDeleteChatMessageInput
            marimo-chatbot delete_chat_message input accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rpc_input.read_marimo_chatbot_delete_chat_message_input()
        """
        _response = self._raw_client.read_marimo_chatbot_delete_chat_message_input(request_options=request_options)
        return _response.data

    def write_marimo_chatbot_delete_chat_message_input(
        self, *, index: float, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        index : float

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
        client.rpc_input.write_marimo_chatbot_delete_chat_message_input(
            index=1.1,
        )
        """
        _response = self._raw_client.write_marimo_chatbot_delete_chat_message_input(
            index=index, request_options=request_options
        )
        return _response.data

    def read_marimo_chatbot_get_chat_history_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoChatbotGetChatHistoryInput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoChatbotGetChatHistoryInput
            marimo-chatbot get_chat_history input accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rpc_input.read_marimo_chatbot_get_chat_history_input()
        """
        _response = self._raw_client.read_marimo_chatbot_get_chat_history_input(request_options=request_options)
        return _response.data

    def write_marimo_chatbot_get_chat_history_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
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
        client.rpc_input.write_marimo_chatbot_get_chat_history_input()
        """
        _response = self._raw_client.write_marimo_chatbot_get_chat_history_input(request_options=request_options)
        return _response.data

    def read_marimo_chatbot_send_prompt_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoChatbotSendPromptInput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoChatbotSendPromptInput
            marimo-chatbot send_prompt input accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rpc_input.read_marimo_chatbot_send_prompt_input()
        """
        _response = self._raw_client.read_marimo_chatbot_send_prompt_input(request_options=request_options)
        return _response.data

    def write_marimo_chatbot_send_prompt_input(
        self,
        *,
        request_id: str,
        messages: typing.Sequence[MarimoChatbotSendPromptInputMessagesItem],
        config: MarimoChatbotSendPromptInputConfig,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        request_id : str

        messages : typing.Sequence[MarimoChatbotSendPromptInputMessagesItem]

        config : MarimoChatbotSendPromptInputConfig

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import (
            FernApi,
            MarimoChatbotSendPromptInputConfig,
            MarimoChatbotSendPromptInputMessagesItem,
        )

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rpc_input.write_marimo_chatbot_send_prompt_input(
            request_id="request_id",
            messages=[
                MarimoChatbotSendPromptInputMessagesItem(
                    id="id",
                    role="system",
                    parts=[],
                )
            ],
            config=MarimoChatbotSendPromptInputConfig(),
        )
        """
        _response = self._raw_client.write_marimo_chatbot_send_prompt_input(
            request_id=request_id, messages=messages, config=config, request_options=request_options
        )
        return _response.data

    def read_marimo_dataframe_download_as_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoDataframeDownloadAsInput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoDataframeDownloadAsInput
            marimo-dataframe download_as input accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rpc_input.read_marimo_dataframe_download_as_input()
        """
        _response = self._raw_client.read_marimo_dataframe_download_as_input(request_options=request_options)
        return _response.data

    def write_marimo_dataframe_download_as_input(
        self, *, format: MarimoDataframeDownloadAsInputFormat, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        format : MarimoDataframeDownloadAsInputFormat

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
        client.rpc_input.write_marimo_dataframe_download_as_input(
            format="csv",
        )
        """
        _response = self._raw_client.write_marimo_dataframe_download_as_input(
            format=format, request_options=request_options
        )
        return _response.data

    def read_marimo_dataframe_get_column_values_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoDataframeGetColumnValuesInput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoDataframeGetColumnValuesInput
            marimo-dataframe get_column_values input accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rpc_input.read_marimo_dataframe_get_column_values_input()
        """
        _response = self._raw_client.read_marimo_dataframe_get_column_values_input(request_options=request_options)
        return _response.data

    def write_marimo_dataframe_get_column_values_input(
        self, *, column: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        column : str

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
        client.rpc_input.write_marimo_dataframe_get_column_values_input(
            column="column",
        )
        """
        _response = self._raw_client.write_marimo_dataframe_get_column_values_input(
            column=column, request_options=request_options
        )
        return _response.data

    def read_marimo_dataframe_get_dataframe_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoDataframeGetDataframeInput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoDataframeGetDataframeInput
            marimo-dataframe get_dataframe input accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rpc_input.read_marimo_dataframe_get_dataframe_input()
        """
        _response = self._raw_client.read_marimo_dataframe_get_dataframe_input(request_options=request_options)
        return _response.data

    def write_marimo_dataframe_get_dataframe_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
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
        client.rpc_input.write_marimo_dataframe_get_dataframe_input()
        """
        _response = self._raw_client.write_marimo_dataframe_get_dataframe_input(request_options=request_options)
        return _response.data

    def read_marimo_dataframe_get_size_bytes_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoDataframeGetSizeBytesInput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoDataframeGetSizeBytesInput
            marimo-dataframe get_size_bytes input accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rpc_input.read_marimo_dataframe_get_size_bytes_input()
        """
        _response = self._raw_client.read_marimo_dataframe_get_size_bytes_input(request_options=request_options)
        return _response.data

    def write_marimo_dataframe_get_size_bytes_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
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
        client.rpc_input.write_marimo_dataframe_get_size_bytes_input()
        """
        _response = self._raw_client.write_marimo_dataframe_get_size_bytes_input(request_options=request_options)
        return _response.data

    def read_marimo_dataframe_search_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoDataframeSearchInput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoDataframeSearchInput
            marimo-dataframe search input accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rpc_input.read_marimo_dataframe_search_input()
        """
        _response = self._raw_client.read_marimo_dataframe_search_input(request_options=request_options)
        return _response.data

    def write_marimo_dataframe_search_input(
        self,
        *,
        page_number: float,
        page_size: float,
        sort: typing.Optional[typing.Sequence[MarimoDataframeSearchInputSortItem]] = OMIT,
        query: typing.Optional[str] = OMIT,
        filters: typing.Optional[MarimoDataframeSearchInputDefSchema0] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        page_number : float

        page_size : float

        sort : typing.Optional[typing.Sequence[MarimoDataframeSearchInputSortItem]]

        query : typing.Optional[str]

        filters : typing.Optional[MarimoDataframeSearchInputDefSchema0]

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
        client.rpc_input.write_marimo_dataframe_search_input(
            page_number=1.1,
            page_size=1.1,
        )
        """
        _response = self._raw_client.write_marimo_dataframe_search_input(
            page_number=page_number,
            page_size=page_size,
            sort=sort,
            query=query,
            filters=filters,
            request_options=request_options,
        )
        return _response.data

    def read_marimo_download_load_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoDownloadLoadInput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoDownloadLoadInput
            marimo-download load input accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rpc_input.read_marimo_download_load_input()
        """
        _response = self._raw_client.read_marimo_download_load_input(request_options=request_options)
        return _response.data

    def write_marimo_download_load_input(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
        client.rpc_input.write_marimo_download_load_input()
        """
        _response = self._raw_client.write_marimo_download_load_input(request_options=request_options)
        return _response.data

    def read_marimo_file_browser_list_directory_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoFileBrowserListDirectoryInput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoFileBrowserListDirectoryInput
            marimo-file-browser list_directory input accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rpc_input.read_marimo_file_browser_list_directory_input()
        """
        _response = self._raw_client.read_marimo_file_browser_list_directory_input(request_options=request_options)
        return _response.data

    def write_marimo_file_browser_list_directory_input(
        self, *, path: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        path : str

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
        client.rpc_input.write_marimo_file_browser_list_directory_input(
            path="path",
        )
        """
        _response = self._raw_client.write_marimo_file_browser_list_directory_input(
            path=path, request_options=request_options
        )
        return _response.data

    def read_marimo_form_validate_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoFormValidateInput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoFormValidateInput
            marimo-form validate input accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rpc_input.read_marimo_form_validate_input()
        """
        _response = self._raw_client.read_marimo_form_validate_input(request_options=request_options)
        return _response.data

    def write_marimo_form_validate_input(
        self, *, value: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        value : typing.Any

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
        client.rpc_input.write_marimo_form_validate_input(
            value={"key": "value"},
        )
        """
        _response = self._raw_client.write_marimo_form_validate_input(value=value, request_options=request_options)
        return _response.data

    def read_marimo_lazy_load_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoLazyLoadInput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoLazyLoadInput
            marimo-lazy load input accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rpc_input.read_marimo_lazy_load_input()
        """
        _response = self._raw_client.read_marimo_lazy_load_input(request_options=request_options)
        return _response.data

    def write_marimo_lazy_load_input(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
        client.rpc_input.write_marimo_lazy_load_input()
        """
        _response = self._raw_client.write_marimo_lazy_load_input(request_options=request_options)
        return _response.data

    def read_marimo_panel_send_to_widget_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoPanelSendToWidgetInput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoPanelSendToWidgetInput
            marimo-panel send_to_widget input accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rpc_input.read_marimo_panel_send_to_widget_input()
        """
        _response = self._raw_client.read_marimo_panel_send_to_widget_input(request_options=request_options)
        return _response.data

    def write_marimo_panel_send_to_widget_input(
        self,
        *,
        message: typing.Any,
        buffers: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        message : typing.Any

        buffers : typing.Sequence[str]

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
        client.rpc_input.write_marimo_panel_send_to_widget_input(
            message={"key": "value"},
            buffers=["buffers", "buffers"],
        )
        """
        _response = self._raw_client.write_marimo_panel_send_to_widget_input(
            message=message, buffers=buffers, request_options=request_options
        )
        return _response.data

    def read_marimo_table_calculate_top_k_rows_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoTableCalculateTopKRowsInput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoTableCalculateTopKRowsInput
            marimo-table calculate_top_k_rows input accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rpc_input.read_marimo_table_calculate_top_k_rows_input()
        """
        _response = self._raw_client.read_marimo_table_calculate_top_k_rows_input(request_options=request_options)
        return _response.data

    def write_marimo_table_calculate_top_k_rows_input(
        self, *, column: str, k: float, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        column : str

        k : float

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
        client.rpc_input.write_marimo_table_calculate_top_k_rows_input(
            column="column",
            k=1.1,
        )
        """
        _response = self._raw_client.write_marimo_table_calculate_top_k_rows_input(
            column=column, k=k, request_options=request_options
        )
        return _response.data

    def read_marimo_table_download_as_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoTableDownloadAsInput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoTableDownloadAsInput
            marimo-table download_as input accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rpc_input.read_marimo_table_download_as_input()
        """
        _response = self._raw_client.read_marimo_table_download_as_input(request_options=request_options)
        return _response.data

    def write_marimo_table_download_as_input(
        self, *, format: MarimoTableDownloadAsInputFormat, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        format : MarimoTableDownloadAsInputFormat

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
        client.rpc_input.write_marimo_table_download_as_input(
            format="csv",
        )
        """
        _response = self._raw_client.write_marimo_table_download_as_input(
            format=format, request_options=request_options
        )
        return _response.data

    def read_marimo_table_get_column_summaries_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoTableGetColumnSummariesInput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoTableGetColumnSummariesInput
            marimo-table get_column_summaries input accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rpc_input.read_marimo_table_get_column_summaries_input()
        """
        _response = self._raw_client.read_marimo_table_get_column_summaries_input(request_options=request_options)
        return _response.data

    def write_marimo_table_get_column_summaries_input(
        self, *, request: MarimoTableGetColumnSummariesInput, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : MarimoTableGetColumnSummariesInput

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
        client.rpc_input.write_marimo_table_get_column_summaries_input(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.write_marimo_table_get_column_summaries_input(
            request=request, request_options=request_options
        )
        return _response.data

    def read_marimo_table_get_data_url_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoTableGetDataUrlInput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoTableGetDataUrlInput
            marimo-table get_data_url input accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rpc_input.read_marimo_table_get_data_url_input()
        """
        _response = self._raw_client.read_marimo_table_get_data_url_input(request_options=request_options)
        return _response.data

    def write_marimo_table_get_data_url_input(
        self, *, request: MarimoTableGetDataUrlInput, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : MarimoTableGetDataUrlInput

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
        client.rpc_input.write_marimo_table_get_data_url_input(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.write_marimo_table_get_data_url_input(
            request=request, request_options=request_options
        )
        return _response.data

    def read_marimo_table_get_row_ids_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoTableGetRowIdsInput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoTableGetRowIdsInput
            marimo-table get_row_ids input accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rpc_input.read_marimo_table_get_row_ids_input()
        """
        _response = self._raw_client.read_marimo_table_get_row_ids_input(request_options=request_options)
        return _response.data

    def write_marimo_table_get_row_ids_input(
        self, *, request: MarimoTableGetRowIdsInput, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : MarimoTableGetRowIdsInput

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
        client.rpc_input.write_marimo_table_get_row_ids_input(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.write_marimo_table_get_row_ids_input(
            request=request, request_options=request_options
        )
        return _response.data

    def read_marimo_table_get_size_bytes_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoTableGetSizeBytesInput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoTableGetSizeBytesInput
            marimo-table get_size_bytes input accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rpc_input.read_marimo_table_get_size_bytes_input()
        """
        _response = self._raw_client.read_marimo_table_get_size_bytes_input(request_options=request_options)
        return _response.data

    def write_marimo_table_get_size_bytes_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
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
        client.rpc_input.write_marimo_table_get_size_bytes_input()
        """
        _response = self._raw_client.write_marimo_table_get_size_bytes_input(request_options=request_options)
        return _response.data

    def read_marimo_table_preview_column_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoTablePreviewColumnInput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoTablePreviewColumnInput
            marimo-table preview_column input accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rpc_input.read_marimo_table_preview_column_input()
        """
        _response = self._raw_client.read_marimo_table_preview_column_input(request_options=request_options)
        return _response.data

    def write_marimo_table_preview_column_input(
        self, *, column: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        column : str

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
        client.rpc_input.write_marimo_table_preview_column_input(
            column="column",
        )
        """
        _response = self._raw_client.write_marimo_table_preview_column_input(
            column=column, request_options=request_options
        )
        return _response.data

    def read_marimo_table_search_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoTableSearchInput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoTableSearchInput
            marimo-table search input accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rpc_input.read_marimo_table_search_input()
        """
        _response = self._raw_client.read_marimo_table_search_input(request_options=request_options)
        return _response.data

    def write_marimo_table_search_input(
        self,
        *,
        page_number: float,
        page_size: float,
        sort: typing.Optional[typing.Sequence[MarimoTableSearchInputSortItem]] = OMIT,
        query: typing.Optional[str] = OMIT,
        filters: typing.Optional[MarimoTableSearchInputDefSchema0] = OMIT,
        max_columns: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        page_number : float

        page_size : float

        sort : typing.Optional[typing.Sequence[MarimoTableSearchInputSortItem]]

        query : typing.Optional[str]

        filters : typing.Optional[MarimoTableSearchInputDefSchema0]

        max_columns : typing.Optional[float]

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
        client.rpc_input.write_marimo_table_search_input(
            page_number=1.1,
            page_size=1.1,
        )
        """
        _response = self._raw_client.write_marimo_table_search_input(
            page_number=page_number,
            page_size=page_size,
            sort=sort,
            query=query,
            filters=filters,
            max_columns=max_columns,
            request_options=request_options,
        )
        return _response.data


class AsyncRpcInputClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRpcInputClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRpcInputClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRpcInputClient
        """
        return self._raw_client

    async def read_marimo_chatbot_cancel_prompt_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoChatbotCancelPromptInput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoChatbotCancelPromptInput
            marimo-chatbot cancel_prompt input accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rpc_input.read_marimo_chatbot_cancel_prompt_input()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_chatbot_cancel_prompt_input(request_options=request_options)
        return _response.data

    async def write_marimo_chatbot_cancel_prompt_input(
        self, *, request_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request_id : str

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
            await client.rpc_input.write_marimo_chatbot_cancel_prompt_input(
                request_id="request_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_chatbot_cancel_prompt_input(
            request_id=request_id, request_options=request_options
        )
        return _response.data

    async def read_marimo_chatbot_delete_chat_history_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoChatbotDeleteChatHistoryInput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoChatbotDeleteChatHistoryInput
            marimo-chatbot delete_chat_history input accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rpc_input.read_marimo_chatbot_delete_chat_history_input()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_chatbot_delete_chat_history_input(
            request_options=request_options
        )
        return _response.data

    async def write_marimo_chatbot_delete_chat_history_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
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
            await client.rpc_input.write_marimo_chatbot_delete_chat_history_input()


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_chatbot_delete_chat_history_input(
            request_options=request_options
        )
        return _response.data

    async def read_marimo_chatbot_delete_chat_message_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoChatbotDeleteChatMessageInput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoChatbotDeleteChatMessageInput
            marimo-chatbot delete_chat_message input accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rpc_input.read_marimo_chatbot_delete_chat_message_input()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_chatbot_delete_chat_message_input(
            request_options=request_options
        )
        return _response.data

    async def write_marimo_chatbot_delete_chat_message_input(
        self, *, index: float, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        index : float

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
            await client.rpc_input.write_marimo_chatbot_delete_chat_message_input(
                index=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_chatbot_delete_chat_message_input(
            index=index, request_options=request_options
        )
        return _response.data

    async def read_marimo_chatbot_get_chat_history_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoChatbotGetChatHistoryInput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoChatbotGetChatHistoryInput
            marimo-chatbot get_chat_history input accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rpc_input.read_marimo_chatbot_get_chat_history_input()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_chatbot_get_chat_history_input(request_options=request_options)
        return _response.data

    async def write_marimo_chatbot_get_chat_history_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
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
            await client.rpc_input.write_marimo_chatbot_get_chat_history_input()


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_chatbot_get_chat_history_input(request_options=request_options)
        return _response.data

    async def read_marimo_chatbot_send_prompt_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoChatbotSendPromptInput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoChatbotSendPromptInput
            marimo-chatbot send_prompt input accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rpc_input.read_marimo_chatbot_send_prompt_input()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_chatbot_send_prompt_input(request_options=request_options)
        return _response.data

    async def write_marimo_chatbot_send_prompt_input(
        self,
        *,
        request_id: str,
        messages: typing.Sequence[MarimoChatbotSendPromptInputMessagesItem],
        config: MarimoChatbotSendPromptInputConfig,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        request_id : str

        messages : typing.Sequence[MarimoChatbotSendPromptInputMessagesItem]

        config : MarimoChatbotSendPromptInputConfig

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
            MarimoChatbotSendPromptInputConfig,
            MarimoChatbotSendPromptInputMessagesItem,
        )

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rpc_input.write_marimo_chatbot_send_prompt_input(
                request_id="request_id",
                messages=[
                    MarimoChatbotSendPromptInputMessagesItem(
                        id="id",
                        role="system",
                        parts=[],
                    )
                ],
                config=MarimoChatbotSendPromptInputConfig(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_chatbot_send_prompt_input(
            request_id=request_id, messages=messages, config=config, request_options=request_options
        )
        return _response.data

    async def read_marimo_dataframe_download_as_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoDataframeDownloadAsInput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoDataframeDownloadAsInput
            marimo-dataframe download_as input accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rpc_input.read_marimo_dataframe_download_as_input()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_dataframe_download_as_input(request_options=request_options)
        return _response.data

    async def write_marimo_dataframe_download_as_input(
        self, *, format: MarimoDataframeDownloadAsInputFormat, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        format : MarimoDataframeDownloadAsInputFormat

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
            await client.rpc_input.write_marimo_dataframe_download_as_input(
                format="csv",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_dataframe_download_as_input(
            format=format, request_options=request_options
        )
        return _response.data

    async def read_marimo_dataframe_get_column_values_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoDataframeGetColumnValuesInput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoDataframeGetColumnValuesInput
            marimo-dataframe get_column_values input accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rpc_input.read_marimo_dataframe_get_column_values_input()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_dataframe_get_column_values_input(
            request_options=request_options
        )
        return _response.data

    async def write_marimo_dataframe_get_column_values_input(
        self, *, column: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        column : str

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
            await client.rpc_input.write_marimo_dataframe_get_column_values_input(
                column="column",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_dataframe_get_column_values_input(
            column=column, request_options=request_options
        )
        return _response.data

    async def read_marimo_dataframe_get_dataframe_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoDataframeGetDataframeInput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoDataframeGetDataframeInput
            marimo-dataframe get_dataframe input accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rpc_input.read_marimo_dataframe_get_dataframe_input()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_dataframe_get_dataframe_input(request_options=request_options)
        return _response.data

    async def write_marimo_dataframe_get_dataframe_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
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
            await client.rpc_input.write_marimo_dataframe_get_dataframe_input()


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_dataframe_get_dataframe_input(request_options=request_options)
        return _response.data

    async def read_marimo_dataframe_get_size_bytes_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoDataframeGetSizeBytesInput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoDataframeGetSizeBytesInput
            marimo-dataframe get_size_bytes input accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rpc_input.read_marimo_dataframe_get_size_bytes_input()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_dataframe_get_size_bytes_input(request_options=request_options)
        return _response.data

    async def write_marimo_dataframe_get_size_bytes_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
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
            await client.rpc_input.write_marimo_dataframe_get_size_bytes_input()


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_dataframe_get_size_bytes_input(request_options=request_options)
        return _response.data

    async def read_marimo_dataframe_search_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoDataframeSearchInput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoDataframeSearchInput
            marimo-dataframe search input accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rpc_input.read_marimo_dataframe_search_input()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_dataframe_search_input(request_options=request_options)
        return _response.data

    async def write_marimo_dataframe_search_input(
        self,
        *,
        page_number: float,
        page_size: float,
        sort: typing.Optional[typing.Sequence[MarimoDataframeSearchInputSortItem]] = OMIT,
        query: typing.Optional[str] = OMIT,
        filters: typing.Optional[MarimoDataframeSearchInputDefSchema0] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        page_number : float

        page_size : float

        sort : typing.Optional[typing.Sequence[MarimoDataframeSearchInputSortItem]]

        query : typing.Optional[str]

        filters : typing.Optional[MarimoDataframeSearchInputDefSchema0]

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
            await client.rpc_input.write_marimo_dataframe_search_input(
                page_number=1.1,
                page_size=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_dataframe_search_input(
            page_number=page_number,
            page_size=page_size,
            sort=sort,
            query=query,
            filters=filters,
            request_options=request_options,
        )
        return _response.data

    async def read_marimo_download_load_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoDownloadLoadInput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoDownloadLoadInput
            marimo-download load input accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rpc_input.read_marimo_download_load_input()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_download_load_input(request_options=request_options)
        return _response.data

    async def write_marimo_download_load_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
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
            await client.rpc_input.write_marimo_download_load_input()


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_download_load_input(request_options=request_options)
        return _response.data

    async def read_marimo_file_browser_list_directory_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoFileBrowserListDirectoryInput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoFileBrowserListDirectoryInput
            marimo-file-browser list_directory input accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rpc_input.read_marimo_file_browser_list_directory_input()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_file_browser_list_directory_input(
            request_options=request_options
        )
        return _response.data

    async def write_marimo_file_browser_list_directory_input(
        self, *, path: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        path : str

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
            await client.rpc_input.write_marimo_file_browser_list_directory_input(
                path="path",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_file_browser_list_directory_input(
            path=path, request_options=request_options
        )
        return _response.data

    async def read_marimo_form_validate_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoFormValidateInput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoFormValidateInput
            marimo-form validate input accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rpc_input.read_marimo_form_validate_input()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_form_validate_input(request_options=request_options)
        return _response.data

    async def write_marimo_form_validate_input(
        self, *, value: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        value : typing.Any

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
            await client.rpc_input.write_marimo_form_validate_input(
                value={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_form_validate_input(
            value=value, request_options=request_options
        )
        return _response.data

    async def read_marimo_lazy_load_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoLazyLoadInput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoLazyLoadInput
            marimo-lazy load input accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rpc_input.read_marimo_lazy_load_input()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_lazy_load_input(request_options=request_options)
        return _response.data

    async def write_marimo_lazy_load_input(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            await client.rpc_input.write_marimo_lazy_load_input()


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_lazy_load_input(request_options=request_options)
        return _response.data

    async def read_marimo_panel_send_to_widget_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoPanelSendToWidgetInput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoPanelSendToWidgetInput
            marimo-panel send_to_widget input accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rpc_input.read_marimo_panel_send_to_widget_input()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_panel_send_to_widget_input(request_options=request_options)
        return _response.data

    async def write_marimo_panel_send_to_widget_input(
        self,
        *,
        message: typing.Any,
        buffers: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        message : typing.Any

        buffers : typing.Sequence[str]

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
            await client.rpc_input.write_marimo_panel_send_to_widget_input(
                message={"key": "value"},
                buffers=["buffers", "buffers"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_panel_send_to_widget_input(
            message=message, buffers=buffers, request_options=request_options
        )
        return _response.data

    async def read_marimo_table_calculate_top_k_rows_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoTableCalculateTopKRowsInput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoTableCalculateTopKRowsInput
            marimo-table calculate_top_k_rows input accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rpc_input.read_marimo_table_calculate_top_k_rows_input()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_table_calculate_top_k_rows_input(request_options=request_options)
        return _response.data

    async def write_marimo_table_calculate_top_k_rows_input(
        self, *, column: str, k: float, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        column : str

        k : float

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
            await client.rpc_input.write_marimo_table_calculate_top_k_rows_input(
                column="column",
                k=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_table_calculate_top_k_rows_input(
            column=column, k=k, request_options=request_options
        )
        return _response.data

    async def read_marimo_table_download_as_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoTableDownloadAsInput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoTableDownloadAsInput
            marimo-table download_as input accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rpc_input.read_marimo_table_download_as_input()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_table_download_as_input(request_options=request_options)
        return _response.data

    async def write_marimo_table_download_as_input(
        self, *, format: MarimoTableDownloadAsInputFormat, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        format : MarimoTableDownloadAsInputFormat

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
            await client.rpc_input.write_marimo_table_download_as_input(
                format="csv",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_table_download_as_input(
            format=format, request_options=request_options
        )
        return _response.data

    async def read_marimo_table_get_column_summaries_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoTableGetColumnSummariesInput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoTableGetColumnSummariesInput
            marimo-table get_column_summaries input accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rpc_input.read_marimo_table_get_column_summaries_input()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_table_get_column_summaries_input(request_options=request_options)
        return _response.data

    async def write_marimo_table_get_column_summaries_input(
        self, *, request: MarimoTableGetColumnSummariesInput, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : MarimoTableGetColumnSummariesInput

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
            await client.rpc_input.write_marimo_table_get_column_summaries_input(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_table_get_column_summaries_input(
            request=request, request_options=request_options
        )
        return _response.data

    async def read_marimo_table_get_data_url_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoTableGetDataUrlInput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoTableGetDataUrlInput
            marimo-table get_data_url input accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rpc_input.read_marimo_table_get_data_url_input()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_table_get_data_url_input(request_options=request_options)
        return _response.data

    async def write_marimo_table_get_data_url_input(
        self, *, request: MarimoTableGetDataUrlInput, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : MarimoTableGetDataUrlInput

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
            await client.rpc_input.write_marimo_table_get_data_url_input(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_table_get_data_url_input(
            request=request, request_options=request_options
        )
        return _response.data

    async def read_marimo_table_get_row_ids_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoTableGetRowIdsInput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoTableGetRowIdsInput
            marimo-table get_row_ids input accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rpc_input.read_marimo_table_get_row_ids_input()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_table_get_row_ids_input(request_options=request_options)
        return _response.data

    async def write_marimo_table_get_row_ids_input(
        self, *, request: MarimoTableGetRowIdsInput, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : MarimoTableGetRowIdsInput

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
            await client.rpc_input.write_marimo_table_get_row_ids_input(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_table_get_row_ids_input(
            request=request, request_options=request_options
        )
        return _response.data

    async def read_marimo_table_get_size_bytes_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoTableGetSizeBytesInput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoTableGetSizeBytesInput
            marimo-table get_size_bytes input accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rpc_input.read_marimo_table_get_size_bytes_input()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_table_get_size_bytes_input(request_options=request_options)
        return _response.data

    async def write_marimo_table_get_size_bytes_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
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
            await client.rpc_input.write_marimo_table_get_size_bytes_input()


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_table_get_size_bytes_input(request_options=request_options)
        return _response.data

    async def read_marimo_table_preview_column_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoTablePreviewColumnInput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoTablePreviewColumnInput
            marimo-table preview_column input accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rpc_input.read_marimo_table_preview_column_input()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_table_preview_column_input(request_options=request_options)
        return _response.data

    async def write_marimo_table_preview_column_input(
        self, *, column: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        column : str

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
            await client.rpc_input.write_marimo_table_preview_column_input(
                column="column",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_table_preview_column_input(
            column=column, request_options=request_options
        )
        return _response.data

    async def read_marimo_table_search_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoTableSearchInput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoTableSearchInput
            marimo-table search input accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rpc_input.read_marimo_table_search_input()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_table_search_input(request_options=request_options)
        return _response.data

    async def write_marimo_table_search_input(
        self,
        *,
        page_number: float,
        page_size: float,
        sort: typing.Optional[typing.Sequence[MarimoTableSearchInputSortItem]] = OMIT,
        query: typing.Optional[str] = OMIT,
        filters: typing.Optional[MarimoTableSearchInputDefSchema0] = OMIT,
        max_columns: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        page_number : float

        page_size : float

        sort : typing.Optional[typing.Sequence[MarimoTableSearchInputSortItem]]

        query : typing.Optional[str]

        filters : typing.Optional[MarimoTableSearchInputDefSchema0]

        max_columns : typing.Optional[float]

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
            await client.rpc_input.write_marimo_table_search_input(
                page_number=1.1,
                page_size=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_table_search_input(
            page_number=page_number,
            page_size=page_size,
            sort=sort,
            query=query,
            filters=filters,
            max_columns=max_columns,
            request_options=request_options,
        )
        return _response.data
