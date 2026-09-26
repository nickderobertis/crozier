

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
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
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawRpcInputClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def read_marimo_chatbot_cancel_prompt_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoChatbotCancelPromptInput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoChatbotCancelPromptInput]
            marimo-chatbot cancel_prompt input accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-chatbot/functions/cancel_prompt/input",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoChatbotCancelPromptInput,
                    parse_obj_as(
                        type_=MarimoChatbotCancelPromptInput,
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

    def write_marimo_chatbot_cancel_prompt_input(
        self, *, request_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        request_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-chatbot/functions/cancel_prompt/input",
            method="PUT",
            json={
                "request_id": request_id,
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

    def read_marimo_chatbot_delete_chat_history_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoChatbotDeleteChatHistoryInput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoChatbotDeleteChatHistoryInput]
            marimo-chatbot delete_chat_history input accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-chatbot/functions/delete_chat_history/input",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoChatbotDeleteChatHistoryInput,
                    parse_obj_as(
                        type_=MarimoChatbotDeleteChatHistoryInput,
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

    def write_marimo_chatbot_delete_chat_history_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-chatbot/functions/delete_chat_history/input",
            method="PUT",
            json={},
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

    def read_marimo_chatbot_delete_chat_message_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoChatbotDeleteChatMessageInput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoChatbotDeleteChatMessageInput]
            marimo-chatbot delete_chat_message input accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-chatbot/functions/delete_chat_message/input",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoChatbotDeleteChatMessageInput,
                    parse_obj_as(
                        type_=MarimoChatbotDeleteChatMessageInput,
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

    def write_marimo_chatbot_delete_chat_message_input(
        self, *, index: float, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        index : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-chatbot/functions/delete_chat_message/input",
            method="PUT",
            json={
                "index": index,
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

    def read_marimo_chatbot_get_chat_history_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoChatbotGetChatHistoryInput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoChatbotGetChatHistoryInput]
            marimo-chatbot get_chat_history input accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-chatbot/functions/get_chat_history/input",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoChatbotGetChatHistoryInput,
                    parse_obj_as(
                        type_=MarimoChatbotGetChatHistoryInput,
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

    def write_marimo_chatbot_get_chat_history_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-chatbot/functions/get_chat_history/input",
            method="PUT",
            json={},
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

    def read_marimo_chatbot_send_prompt_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoChatbotSendPromptInput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoChatbotSendPromptInput]
            marimo-chatbot send_prompt input accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-chatbot/functions/send_prompt/input",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoChatbotSendPromptInput,
                    parse_obj_as(
                        type_=MarimoChatbotSendPromptInput,
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

    def write_marimo_chatbot_send_prompt_input(
        self,
        *,
        request_id: str,
        messages: typing.Sequence[MarimoChatbotSendPromptInputMessagesItem],
        config: MarimoChatbotSendPromptInputConfig,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-chatbot/functions/send_prompt/input",
            method="PUT",
            json={
                "request_id": request_id,
                "messages": convert_and_respect_annotation_metadata(
                    object_=messages,
                    annotation=typing.Sequence[MarimoChatbotSendPromptInputMessagesItem],
                    direction="write",
                ),
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=MarimoChatbotSendPromptInputConfig, direction="write"
                ),
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

    def read_marimo_dataframe_download_as_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoDataframeDownloadAsInput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoDataframeDownloadAsInput]
            marimo-dataframe download_as input accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-dataframe/functions/download_as/input",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoDataframeDownloadAsInput,
                    parse_obj_as(
                        type_=MarimoDataframeDownloadAsInput,
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

    def write_marimo_dataframe_download_as_input(
        self, *, format: MarimoDataframeDownloadAsInputFormat, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        format : MarimoDataframeDownloadAsInputFormat

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-dataframe/functions/download_as/input",
            method="PUT",
            json={
                "format": format,
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

    def read_marimo_dataframe_get_column_values_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoDataframeGetColumnValuesInput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoDataframeGetColumnValuesInput]
            marimo-dataframe get_column_values input accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-dataframe/functions/get_column_values/input",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoDataframeGetColumnValuesInput,
                    parse_obj_as(
                        type_=MarimoDataframeGetColumnValuesInput,
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

    def write_marimo_dataframe_get_column_values_input(
        self, *, column: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        column : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-dataframe/functions/get_column_values/input",
            method="PUT",
            json={
                "column": column,
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

    def read_marimo_dataframe_get_dataframe_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoDataframeGetDataframeInput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoDataframeGetDataframeInput]
            marimo-dataframe get_dataframe input accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-dataframe/functions/get_dataframe/input",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoDataframeGetDataframeInput,
                    parse_obj_as(
                        type_=MarimoDataframeGetDataframeInput,
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

    def write_marimo_dataframe_get_dataframe_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-dataframe/functions/get_dataframe/input",
            method="PUT",
            json={},
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

    def read_marimo_dataframe_get_size_bytes_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoDataframeGetSizeBytesInput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoDataframeGetSizeBytesInput]
            marimo-dataframe get_size_bytes input accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-dataframe/functions/get_size_bytes/input",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoDataframeGetSizeBytesInput,
                    parse_obj_as(
                        type_=MarimoDataframeGetSizeBytesInput,
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

    def write_marimo_dataframe_get_size_bytes_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-dataframe/functions/get_size_bytes/input",
            method="PUT",
            json={},
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

    def read_marimo_dataframe_search_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoDataframeSearchInput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoDataframeSearchInput]
            marimo-dataframe search input accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-dataframe/functions/search/input",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoDataframeSearchInput,
                    parse_obj_as(
                        type_=MarimoDataframeSearchInput,
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

    def write_marimo_dataframe_search_input(
        self,
        *,
        page_number: float,
        page_size: float,
        sort: typing.Optional[typing.Sequence[MarimoDataframeSearchInputSortItem]] = OMIT,
        query: typing.Optional[str] = OMIT,
        filters: typing.Optional[MarimoDataframeSearchInputDefSchema0] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-dataframe/functions/search/input",
            method="PUT",
            json={
                "sort": convert_and_respect_annotation_metadata(
                    object_=sort, annotation=typing.Sequence[MarimoDataframeSearchInputSortItem], direction="write"
                ),
                "query": query,
                "filters": convert_and_respect_annotation_metadata(
                    object_=filters, annotation=MarimoDataframeSearchInputDefSchema0, direction="write"
                ),
                "page_number": page_number,
                "page_size": page_size,
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

    def read_marimo_download_load_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoDownloadLoadInput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoDownloadLoadInput]
            marimo-download load input accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-download/functions/load/input",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoDownloadLoadInput,
                    parse_obj_as(
                        type_=MarimoDownloadLoadInput,
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

    def write_marimo_download_load_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-download/functions/load/input",
            method="PUT",
            json={},
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

    def read_marimo_file_browser_list_directory_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoFileBrowserListDirectoryInput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoFileBrowserListDirectoryInput]
            marimo-file-browser list_directory input accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-file-browser/functions/list_directory/input",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoFileBrowserListDirectoryInput,
                    parse_obj_as(
                        type_=MarimoFileBrowserListDirectoryInput,
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

    def write_marimo_file_browser_list_directory_input(
        self, *, path: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-file-browser/functions/list_directory/input",
            method="PUT",
            json={
                "path": path,
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

    def read_marimo_form_validate_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoFormValidateInput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoFormValidateInput]
            marimo-form validate input accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-form/functions/validate/input",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoFormValidateInput,
                    parse_obj_as(
                        type_=MarimoFormValidateInput,
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

    def write_marimo_form_validate_input(
        self, *, value: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        value : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-form/functions/validate/input",
            method="PUT",
            json={
                "value": value,
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

    def read_marimo_lazy_load_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoLazyLoadInput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoLazyLoadInput]
            marimo-lazy load input accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-lazy/functions/load/input",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoLazyLoadInput,
                    parse_obj_as(
                        type_=MarimoLazyLoadInput,
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

    def write_marimo_lazy_load_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-lazy/functions/load/input",
            method="PUT",
            json={},
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

    def read_marimo_panel_send_to_widget_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoPanelSendToWidgetInput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoPanelSendToWidgetInput]
            marimo-panel send_to_widget input accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-panel/functions/send_to_widget/input",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoPanelSendToWidgetInput,
                    parse_obj_as(
                        type_=MarimoPanelSendToWidgetInput,
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

    def write_marimo_panel_send_to_widget_input(
        self,
        *,
        message: typing.Any,
        buffers: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        message : typing.Any

        buffers : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-panel/functions/send_to_widget/input",
            method="PUT",
            json={
                "message": message,
                "buffers": buffers,
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

    def read_marimo_table_calculate_top_k_rows_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoTableCalculateTopKRowsInput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoTableCalculateTopKRowsInput]
            marimo-table calculate_top_k_rows input accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/calculate_top_k_rows/input",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoTableCalculateTopKRowsInput,
                    parse_obj_as(
                        type_=MarimoTableCalculateTopKRowsInput,
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

    def write_marimo_table_calculate_top_k_rows_input(
        self, *, column: str, k: float, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        column : str

        k : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/calculate_top_k_rows/input",
            method="PUT",
            json={
                "column": column,
                "k": k,
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

    def read_marimo_table_download_as_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoTableDownloadAsInput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoTableDownloadAsInput]
            marimo-table download_as input accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/download_as/input",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoTableDownloadAsInput,
                    parse_obj_as(
                        type_=MarimoTableDownloadAsInput,
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

    def write_marimo_table_download_as_input(
        self, *, format: MarimoTableDownloadAsInputFormat, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        format : MarimoTableDownloadAsInputFormat

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/download_as/input",
            method="PUT",
            json={
                "format": format,
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

    def read_marimo_table_get_column_summaries_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoTableGetColumnSummariesInput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoTableGetColumnSummariesInput]
            marimo-table get_column_summaries input accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/get_column_summaries/input",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoTableGetColumnSummariesInput,
                    parse_obj_as(
                        type_=MarimoTableGetColumnSummariesInput,
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

    def write_marimo_table_get_column_summaries_input(
        self, *, request: MarimoTableGetColumnSummariesInput, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        request : MarimoTableGetColumnSummariesInput

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/get_column_summaries/input",
            method="PUT",
            json=request,
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

    def read_marimo_table_get_data_url_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoTableGetDataUrlInput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoTableGetDataUrlInput]
            marimo-table get_data_url input accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/get_data_url/input",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoTableGetDataUrlInput,
                    parse_obj_as(
                        type_=MarimoTableGetDataUrlInput,
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

    def write_marimo_table_get_data_url_input(
        self, *, request: MarimoTableGetDataUrlInput, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        request : MarimoTableGetDataUrlInput

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/get_data_url/input",
            method="PUT",
            json=request,
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

    def read_marimo_table_get_row_ids_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoTableGetRowIdsInput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoTableGetRowIdsInput]
            marimo-table get_row_ids input accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/get_row_ids/input",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoTableGetRowIdsInput,
                    parse_obj_as(
                        type_=MarimoTableGetRowIdsInput,
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

    def write_marimo_table_get_row_ids_input(
        self, *, request: MarimoTableGetRowIdsInput, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        request : MarimoTableGetRowIdsInput

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/get_row_ids/input",
            method="PUT",
            json=request,
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

    def read_marimo_table_get_size_bytes_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoTableGetSizeBytesInput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoTableGetSizeBytesInput]
            marimo-table get_size_bytes input accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/get_size_bytes/input",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoTableGetSizeBytesInput,
                    parse_obj_as(
                        type_=MarimoTableGetSizeBytesInput,
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

    def write_marimo_table_get_size_bytes_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/get_size_bytes/input",
            method="PUT",
            json={},
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

    def read_marimo_table_preview_column_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoTablePreviewColumnInput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoTablePreviewColumnInput]
            marimo-table preview_column input accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/preview_column/input",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoTablePreviewColumnInput,
                    parse_obj_as(
                        type_=MarimoTablePreviewColumnInput,
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

    def write_marimo_table_preview_column_input(
        self, *, column: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        column : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/preview_column/input",
            method="PUT",
            json={
                "column": column,
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

    def read_marimo_table_search_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoTableSearchInput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoTableSearchInput]
            marimo-table search input accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/search/input",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoTableSearchInput,
                    parse_obj_as(
                        type_=MarimoTableSearchInput,
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
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/search/input",
            method="PUT",
            json={
                "sort": convert_and_respect_annotation_metadata(
                    object_=sort, annotation=typing.Sequence[MarimoTableSearchInputSortItem], direction="write"
                ),
                "query": query,
                "filters": convert_and_respect_annotation_metadata(
                    object_=filters, annotation=MarimoTableSearchInputDefSchema0, direction="write"
                ),
                "page_number": page_number,
                "page_size": page_size,
                "max_columns": max_columns,
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


class AsyncRawRpcInputClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def read_marimo_chatbot_cancel_prompt_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoChatbotCancelPromptInput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoChatbotCancelPromptInput]
            marimo-chatbot cancel_prompt input accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-chatbot/functions/cancel_prompt/input",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoChatbotCancelPromptInput,
                    parse_obj_as(
                        type_=MarimoChatbotCancelPromptInput,
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

    async def write_marimo_chatbot_cancel_prompt_input(
        self, *, request_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        request_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-chatbot/functions/cancel_prompt/input",
            method="PUT",
            json={
                "request_id": request_id,
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

    async def read_marimo_chatbot_delete_chat_history_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoChatbotDeleteChatHistoryInput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoChatbotDeleteChatHistoryInput]
            marimo-chatbot delete_chat_history input accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-chatbot/functions/delete_chat_history/input",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoChatbotDeleteChatHistoryInput,
                    parse_obj_as(
                        type_=MarimoChatbotDeleteChatHistoryInput,
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

    async def write_marimo_chatbot_delete_chat_history_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-chatbot/functions/delete_chat_history/input",
            method="PUT",
            json={},
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

    async def read_marimo_chatbot_delete_chat_message_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoChatbotDeleteChatMessageInput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoChatbotDeleteChatMessageInput]
            marimo-chatbot delete_chat_message input accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-chatbot/functions/delete_chat_message/input",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoChatbotDeleteChatMessageInput,
                    parse_obj_as(
                        type_=MarimoChatbotDeleteChatMessageInput,
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

    async def write_marimo_chatbot_delete_chat_message_input(
        self, *, index: float, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        index : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-chatbot/functions/delete_chat_message/input",
            method="PUT",
            json={
                "index": index,
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

    async def read_marimo_chatbot_get_chat_history_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoChatbotGetChatHistoryInput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoChatbotGetChatHistoryInput]
            marimo-chatbot get_chat_history input accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-chatbot/functions/get_chat_history/input",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoChatbotGetChatHistoryInput,
                    parse_obj_as(
                        type_=MarimoChatbotGetChatHistoryInput,
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

    async def write_marimo_chatbot_get_chat_history_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-chatbot/functions/get_chat_history/input",
            method="PUT",
            json={},
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

    async def read_marimo_chatbot_send_prompt_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoChatbotSendPromptInput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoChatbotSendPromptInput]
            marimo-chatbot send_prompt input accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-chatbot/functions/send_prompt/input",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoChatbotSendPromptInput,
                    parse_obj_as(
                        type_=MarimoChatbotSendPromptInput,
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

    async def write_marimo_chatbot_send_prompt_input(
        self,
        *,
        request_id: str,
        messages: typing.Sequence[MarimoChatbotSendPromptInputMessagesItem],
        config: MarimoChatbotSendPromptInputConfig,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-chatbot/functions/send_prompt/input",
            method="PUT",
            json={
                "request_id": request_id,
                "messages": convert_and_respect_annotation_metadata(
                    object_=messages,
                    annotation=typing.Sequence[MarimoChatbotSendPromptInputMessagesItem],
                    direction="write",
                ),
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=MarimoChatbotSendPromptInputConfig, direction="write"
                ),
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

    async def read_marimo_dataframe_download_as_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoDataframeDownloadAsInput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoDataframeDownloadAsInput]
            marimo-dataframe download_as input accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-dataframe/functions/download_as/input",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoDataframeDownloadAsInput,
                    parse_obj_as(
                        type_=MarimoDataframeDownloadAsInput,
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

    async def write_marimo_dataframe_download_as_input(
        self, *, format: MarimoDataframeDownloadAsInputFormat, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        format : MarimoDataframeDownloadAsInputFormat

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-dataframe/functions/download_as/input",
            method="PUT",
            json={
                "format": format,
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

    async def read_marimo_dataframe_get_column_values_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoDataframeGetColumnValuesInput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoDataframeGetColumnValuesInput]
            marimo-dataframe get_column_values input accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-dataframe/functions/get_column_values/input",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoDataframeGetColumnValuesInput,
                    parse_obj_as(
                        type_=MarimoDataframeGetColumnValuesInput,
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

    async def write_marimo_dataframe_get_column_values_input(
        self, *, column: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        column : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-dataframe/functions/get_column_values/input",
            method="PUT",
            json={
                "column": column,
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

    async def read_marimo_dataframe_get_dataframe_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoDataframeGetDataframeInput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoDataframeGetDataframeInput]
            marimo-dataframe get_dataframe input accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-dataframe/functions/get_dataframe/input",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoDataframeGetDataframeInput,
                    parse_obj_as(
                        type_=MarimoDataframeGetDataframeInput,
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

    async def write_marimo_dataframe_get_dataframe_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-dataframe/functions/get_dataframe/input",
            method="PUT",
            json={},
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

    async def read_marimo_dataframe_get_size_bytes_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoDataframeGetSizeBytesInput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoDataframeGetSizeBytesInput]
            marimo-dataframe get_size_bytes input accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-dataframe/functions/get_size_bytes/input",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoDataframeGetSizeBytesInput,
                    parse_obj_as(
                        type_=MarimoDataframeGetSizeBytesInput,
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

    async def write_marimo_dataframe_get_size_bytes_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-dataframe/functions/get_size_bytes/input",
            method="PUT",
            json={},
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

    async def read_marimo_dataframe_search_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoDataframeSearchInput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoDataframeSearchInput]
            marimo-dataframe search input accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-dataframe/functions/search/input",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoDataframeSearchInput,
                    parse_obj_as(
                        type_=MarimoDataframeSearchInput,
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

    async def write_marimo_dataframe_search_input(
        self,
        *,
        page_number: float,
        page_size: float,
        sort: typing.Optional[typing.Sequence[MarimoDataframeSearchInputSortItem]] = OMIT,
        query: typing.Optional[str] = OMIT,
        filters: typing.Optional[MarimoDataframeSearchInputDefSchema0] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-dataframe/functions/search/input",
            method="PUT",
            json={
                "sort": convert_and_respect_annotation_metadata(
                    object_=sort, annotation=typing.Sequence[MarimoDataframeSearchInputSortItem], direction="write"
                ),
                "query": query,
                "filters": convert_and_respect_annotation_metadata(
                    object_=filters, annotation=MarimoDataframeSearchInputDefSchema0, direction="write"
                ),
                "page_number": page_number,
                "page_size": page_size,
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

    async def read_marimo_download_load_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoDownloadLoadInput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoDownloadLoadInput]
            marimo-download load input accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-download/functions/load/input",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoDownloadLoadInput,
                    parse_obj_as(
                        type_=MarimoDownloadLoadInput,
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

    async def write_marimo_download_load_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-download/functions/load/input",
            method="PUT",
            json={},
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

    async def read_marimo_file_browser_list_directory_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoFileBrowserListDirectoryInput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoFileBrowserListDirectoryInput]
            marimo-file-browser list_directory input accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-file-browser/functions/list_directory/input",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoFileBrowserListDirectoryInput,
                    parse_obj_as(
                        type_=MarimoFileBrowserListDirectoryInput,
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

    async def write_marimo_file_browser_list_directory_input(
        self, *, path: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-file-browser/functions/list_directory/input",
            method="PUT",
            json={
                "path": path,
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

    async def read_marimo_form_validate_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoFormValidateInput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoFormValidateInput]
            marimo-form validate input accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-form/functions/validate/input",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoFormValidateInput,
                    parse_obj_as(
                        type_=MarimoFormValidateInput,
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

    async def write_marimo_form_validate_input(
        self, *, value: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        value : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-form/functions/validate/input",
            method="PUT",
            json={
                "value": value,
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

    async def read_marimo_lazy_load_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoLazyLoadInput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoLazyLoadInput]
            marimo-lazy load input accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-lazy/functions/load/input",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoLazyLoadInput,
                    parse_obj_as(
                        type_=MarimoLazyLoadInput,
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

    async def write_marimo_lazy_load_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-lazy/functions/load/input",
            method="PUT",
            json={},
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

    async def read_marimo_panel_send_to_widget_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoPanelSendToWidgetInput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoPanelSendToWidgetInput]
            marimo-panel send_to_widget input accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-panel/functions/send_to_widget/input",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoPanelSendToWidgetInput,
                    parse_obj_as(
                        type_=MarimoPanelSendToWidgetInput,
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

    async def write_marimo_panel_send_to_widget_input(
        self,
        *,
        message: typing.Any,
        buffers: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        message : typing.Any

        buffers : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-panel/functions/send_to_widget/input",
            method="PUT",
            json={
                "message": message,
                "buffers": buffers,
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

    async def read_marimo_table_calculate_top_k_rows_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoTableCalculateTopKRowsInput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoTableCalculateTopKRowsInput]
            marimo-table calculate_top_k_rows input accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/calculate_top_k_rows/input",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoTableCalculateTopKRowsInput,
                    parse_obj_as(
                        type_=MarimoTableCalculateTopKRowsInput,
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

    async def write_marimo_table_calculate_top_k_rows_input(
        self, *, column: str, k: float, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        column : str

        k : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/calculate_top_k_rows/input",
            method="PUT",
            json={
                "column": column,
                "k": k,
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

    async def read_marimo_table_download_as_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoTableDownloadAsInput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoTableDownloadAsInput]
            marimo-table download_as input accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/download_as/input",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoTableDownloadAsInput,
                    parse_obj_as(
                        type_=MarimoTableDownloadAsInput,
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

    async def write_marimo_table_download_as_input(
        self, *, format: MarimoTableDownloadAsInputFormat, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        format : MarimoTableDownloadAsInputFormat

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/download_as/input",
            method="PUT",
            json={
                "format": format,
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

    async def read_marimo_table_get_column_summaries_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoTableGetColumnSummariesInput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoTableGetColumnSummariesInput]
            marimo-table get_column_summaries input accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/get_column_summaries/input",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoTableGetColumnSummariesInput,
                    parse_obj_as(
                        type_=MarimoTableGetColumnSummariesInput,
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

    async def write_marimo_table_get_column_summaries_input(
        self, *, request: MarimoTableGetColumnSummariesInput, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        request : MarimoTableGetColumnSummariesInput

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/get_column_summaries/input",
            method="PUT",
            json=request,
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

    async def read_marimo_table_get_data_url_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoTableGetDataUrlInput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoTableGetDataUrlInput]
            marimo-table get_data_url input accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/get_data_url/input",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoTableGetDataUrlInput,
                    parse_obj_as(
                        type_=MarimoTableGetDataUrlInput,
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

    async def write_marimo_table_get_data_url_input(
        self, *, request: MarimoTableGetDataUrlInput, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        request : MarimoTableGetDataUrlInput

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/get_data_url/input",
            method="PUT",
            json=request,
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

    async def read_marimo_table_get_row_ids_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoTableGetRowIdsInput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoTableGetRowIdsInput]
            marimo-table get_row_ids input accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/get_row_ids/input",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoTableGetRowIdsInput,
                    parse_obj_as(
                        type_=MarimoTableGetRowIdsInput,
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

    async def write_marimo_table_get_row_ids_input(
        self, *, request: MarimoTableGetRowIdsInput, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        request : MarimoTableGetRowIdsInput

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/get_row_ids/input",
            method="PUT",
            json=request,
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

    async def read_marimo_table_get_size_bytes_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoTableGetSizeBytesInput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoTableGetSizeBytesInput]
            marimo-table get_size_bytes input accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/get_size_bytes/input",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoTableGetSizeBytesInput,
                    parse_obj_as(
                        type_=MarimoTableGetSizeBytesInput,
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

    async def write_marimo_table_get_size_bytes_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/get_size_bytes/input",
            method="PUT",
            json={},
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

    async def read_marimo_table_preview_column_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoTablePreviewColumnInput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoTablePreviewColumnInput]
            marimo-table preview_column input accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/preview_column/input",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoTablePreviewColumnInput,
                    parse_obj_as(
                        type_=MarimoTablePreviewColumnInput,
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

    async def write_marimo_table_preview_column_input(
        self, *, column: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        column : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/preview_column/input",
            method="PUT",
            json={
                "column": column,
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

    async def read_marimo_table_search_input(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoTableSearchInput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoTableSearchInput]
            marimo-table search input accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/search/input",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoTableSearchInput,
                    parse_obj_as(
                        type_=MarimoTableSearchInput,
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
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/search/input",
            method="PUT",
            json={
                "sort": convert_and_respect_annotation_metadata(
                    object_=sort, annotation=typing.Sequence[MarimoTableSearchInputSortItem], direction="write"
                ),
                "query": query,
                "filters": convert_and_respect_annotation_metadata(
                    object_=filters, annotation=MarimoTableSearchInputDefSchema0, direction="write"
                ),
                "page_number": page_number,
                "page_size": page_size,
                "max_columns": max_columns,
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
