

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
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
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawRpcOutputClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def read_marimo_chatbot_cancel_prompt_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[MarimoChatbotCancelPromptOutput]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[MarimoChatbotCancelPromptOutput]]
            marimo-chatbot cancel_prompt output accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-chatbot/functions/cancel_prompt/output",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[MarimoChatbotCancelPromptOutput],
                    parse_obj_as(
                        type_=typing.Optional[MarimoChatbotCancelPromptOutput],
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

    def write_marimo_chatbot_cancel_prompt_output(
        self,
        *,
        request: typing.Optional[MarimoChatbotCancelPromptOutput] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        request : typing.Optional[MarimoChatbotCancelPromptOutput]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-chatbot/functions/cancel_prompt/output",
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

    def read_marimo_chatbot_delete_chat_history_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[MarimoChatbotDeleteChatHistoryOutput]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[MarimoChatbotDeleteChatHistoryOutput]]
            marimo-chatbot delete_chat_history output accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-chatbot/functions/delete_chat_history/output",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[MarimoChatbotDeleteChatHistoryOutput],
                    parse_obj_as(
                        type_=typing.Optional[MarimoChatbotDeleteChatHistoryOutput],
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

    def write_marimo_chatbot_delete_chat_history_output(
        self,
        *,
        request: typing.Optional[MarimoChatbotDeleteChatHistoryOutput] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        request : typing.Optional[MarimoChatbotDeleteChatHistoryOutput]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-chatbot/functions/delete_chat_history/output",
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

    def read_marimo_chatbot_delete_chat_message_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[MarimoChatbotDeleteChatMessageOutput]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[MarimoChatbotDeleteChatMessageOutput]]
            marimo-chatbot delete_chat_message output accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-chatbot/functions/delete_chat_message/output",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[MarimoChatbotDeleteChatMessageOutput],
                    parse_obj_as(
                        type_=typing.Optional[MarimoChatbotDeleteChatMessageOutput],
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

    def write_marimo_chatbot_delete_chat_message_output(
        self,
        *,
        request: typing.Optional[MarimoChatbotDeleteChatMessageOutput] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        request : typing.Optional[MarimoChatbotDeleteChatMessageOutput]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-chatbot/functions/delete_chat_message/output",
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

    def read_marimo_chatbot_get_chat_history_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoChatbotGetChatHistoryOutput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoChatbotGetChatHistoryOutput]
            marimo-chatbot get_chat_history output accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-chatbot/functions/get_chat_history/output",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoChatbotGetChatHistoryOutput,
                    parse_obj_as(
                        type_=MarimoChatbotGetChatHistoryOutput,
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

    def write_marimo_chatbot_get_chat_history_output(
        self,
        *,
        messages: typing.Sequence[MarimoChatbotGetChatHistoryOutputMessagesItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        messages : typing.Sequence[MarimoChatbotGetChatHistoryOutputMessagesItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-chatbot/functions/get_chat_history/output",
            method="PUT",
            json={
                "messages": convert_and_respect_annotation_metadata(
                    object_=messages,
                    annotation=typing.Sequence[MarimoChatbotGetChatHistoryOutputMessagesItem],
                    direction="write",
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

    def read_marimo_chatbot_send_prompt_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoChatbotSendPromptOutput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoChatbotSendPromptOutput]
            marimo-chatbot send_prompt output accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-chatbot/functions/send_prompt/output",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoChatbotSendPromptOutput,
                    parse_obj_as(
                        type_=MarimoChatbotSendPromptOutput,
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

    def write_marimo_chatbot_send_prompt_output(
        self, *, request: MarimoChatbotSendPromptOutput, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        request : MarimoChatbotSendPromptOutput

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-chatbot/functions/send_prompt/output",
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

    def read_marimo_dataframe_download_as_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoDataframeDownloadAsOutput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoDataframeDownloadAsOutput]
            marimo-dataframe download_as output accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-dataframe/functions/download_as/output",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoDataframeDownloadAsOutput,
                    parse_obj_as(
                        type_=MarimoDataframeDownloadAsOutput,
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

    def write_marimo_dataframe_download_as_output(
        self,
        *,
        url: str,
        filename: str,
        error: typing.Optional[str] = OMIT,
        missing_packages: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-dataframe/functions/download_as/output",
            method="PUT",
            json={
                "url": url,
                "filename": filename,
                "error": error,
                "missing_packages": missing_packages,
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

    def read_marimo_dataframe_get_column_values_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoDataframeGetColumnValuesOutput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoDataframeGetColumnValuesOutput]
            marimo-dataframe get_column_values output accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-dataframe/functions/get_column_values/output",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoDataframeGetColumnValuesOutput,
                    parse_obj_as(
                        type_=MarimoDataframeGetColumnValuesOutput,
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

    def write_marimo_dataframe_get_column_values_output(
        self,
        *,
        values: typing.Sequence[typing.Any],
        too_many_values: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        values : typing.Sequence[typing.Any]

        too_many_values : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-dataframe/functions/get_column_values/output",
            method="PUT",
            json={
                "values": values,
                "too_many_values": too_many_values,
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

    def read_marimo_dataframe_get_dataframe_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoDataframeGetDataframeOutput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoDataframeGetDataframeOutput]
            marimo-dataframe get_dataframe output accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-dataframe/functions/get_dataframe/output",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoDataframeGetDataframeOutput,
                    parse_obj_as(
                        type_=MarimoDataframeGetDataframeOutput,
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
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-dataframe/functions/get_dataframe/output",
            method="PUT",
            json={
                "url": url,
                "total_rows": total_rows,
                "row_headers": row_headers,
                "field_types": field_types,
                "column_types_per_step": column_types_per_step,
                "python_code": python_code,
                "sql_code": sql_code,
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

    def read_marimo_dataframe_get_size_bytes_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoDataframeGetSizeBytesOutput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoDataframeGetSizeBytesOutput]
            marimo-dataframe get_size_bytes output accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-dataframe/functions/get_size_bytes/output",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoDataframeGetSizeBytesOutput,
                    parse_obj_as(
                        type_=MarimoDataframeGetSizeBytesOutput,
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

    def write_marimo_dataframe_get_size_bytes_output(
        self, *, size_bytes: typing.Optional[float] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        size_bytes : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-dataframe/functions/get_size_bytes/output",
            method="PUT",
            json={
                "size_bytes": size_bytes,
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

    def read_marimo_dataframe_search_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoDataframeSearchOutput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoDataframeSearchOutput]
            marimo-dataframe search output accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-dataframe/functions/search/output",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoDataframeSearchOutput,
                    parse_obj_as(
                        type_=MarimoDataframeSearchOutput,
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

    def write_marimo_dataframe_search_output(
        self,
        *,
        data: MarimoDataframeSearchOutputData,
        total_rows: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        data : MarimoDataframeSearchOutputData

        total_rows : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-dataframe/functions/search/output",
            method="PUT",
            json={
                "data": convert_and_respect_annotation_metadata(
                    object_=data, annotation=MarimoDataframeSearchOutputData, direction="write"
                ),
                "total_rows": total_rows,
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

    def read_marimo_download_load_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoDownloadLoadOutput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoDownloadLoadOutput]
            marimo-download load output accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-download/functions/load/output",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoDownloadLoadOutput,
                    parse_obj_as(
                        type_=MarimoDownloadLoadOutput,
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

    def write_marimo_download_load_output(
        self,
        *,
        data: str,
        filename: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        data : str

        filename : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-download/functions/load/output",
            method="PUT",
            json={
                "data": data,
                "filename": filename,
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

    def read_marimo_file_browser_list_directory_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoFileBrowserListDirectoryOutput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoFileBrowserListDirectoryOutput]
            marimo-file-browser list_directory output accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-file-browser/functions/list_directory/output",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoFileBrowserListDirectoryOutput,
                    parse_obj_as(
                        type_=MarimoFileBrowserListDirectoryOutput,
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

    def write_marimo_file_browser_list_directory_output(
        self,
        *,
        files: typing.Sequence[MarimoFileBrowserListDirectoryOutputFilesItem],
        total_count: float,
        is_truncated: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-file-browser/functions/list_directory/output",
            method="PUT",
            json={
                "files": convert_and_respect_annotation_metadata(
                    object_=files,
                    annotation=typing.Sequence[MarimoFileBrowserListDirectoryOutputFilesItem],
                    direction="write",
                ),
                "total_count": total_count,
                "is_truncated": is_truncated,
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

    def read_marimo_form_validate_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[MarimoFormValidateOutput]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[MarimoFormValidateOutput]]
            marimo-form validate output accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-form/functions/validate/output",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[MarimoFormValidateOutput],
                    parse_obj_as(
                        type_=typing.Optional[MarimoFormValidateOutput],
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

    def write_marimo_form_validate_output(
        self,
        *,
        request: typing.Optional[MarimoFormValidateOutput] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        request : typing.Optional[MarimoFormValidateOutput]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-form/functions/validate/output",
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

    def read_marimo_lazy_load_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoLazyLoadOutput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoLazyLoadOutput]
            marimo-lazy load output accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-lazy/functions/load/output",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoLazyLoadOutput,
                    parse_obj_as(
                        type_=MarimoLazyLoadOutput,
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

    def write_marimo_lazy_load_output(
        self, *, html: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        html : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-lazy/functions/load/output",
            method="PUT",
            json={
                "html": html,
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

    def read_marimo_panel_send_to_widget_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[MarimoPanelSendToWidgetOutput]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[MarimoPanelSendToWidgetOutput]]
            marimo-panel send_to_widget output accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-panel/functions/send_to_widget/output",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[MarimoPanelSendToWidgetOutput],
                    parse_obj_as(
                        type_=typing.Optional[MarimoPanelSendToWidgetOutput],
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

    def write_marimo_panel_send_to_widget_output(
        self,
        *,
        request: typing.Optional[MarimoPanelSendToWidgetOutput] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        request : typing.Optional[MarimoPanelSendToWidgetOutput]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-panel/functions/send_to_widget/output",
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

    def read_marimo_table_calculate_top_k_rows_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoTableCalculateTopKRowsOutput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoTableCalculateTopKRowsOutput]
            marimo-table calculate_top_k_rows output accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/calculate_top_k_rows/output",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoTableCalculateTopKRowsOutput,
                    parse_obj_as(
                        type_=MarimoTableCalculateTopKRowsOutput,
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

    def write_marimo_table_calculate_top_k_rows_output(
        self,
        *,
        data: typing.Sequence[typing.Sequence[typing.Any]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        data : typing.Sequence[typing.Sequence[typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/calculate_top_k_rows/output",
            method="PUT",
            json={
                "data": data,
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

    def read_marimo_table_download_as_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoTableDownloadAsOutput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoTableDownloadAsOutput]
            marimo-table download_as output accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/download_as/output",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoTableDownloadAsOutput,
                    parse_obj_as(
                        type_=MarimoTableDownloadAsOutput,
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

    def write_marimo_table_download_as_output(
        self,
        *,
        url: str,
        filename: str,
        error: typing.Optional[str] = OMIT,
        missing_packages: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/download_as/output",
            method="PUT",
            json={
                "url": url,
                "filename": filename,
                "error": error,
                "missing_packages": missing_packages,
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

    def read_marimo_table_get_column_summaries_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoTableGetColumnSummariesOutput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoTableGetColumnSummariesOutput]
            marimo-table get_column_summaries output accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/get_column_summaries/output",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoTableGetColumnSummariesOutput,
                    parse_obj_as(
                        type_=MarimoTableGetColumnSummariesOutput,
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
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/get_column_summaries/output",
            method="PUT",
            json={
                "data": convert_and_respect_annotation_metadata(
                    object_=data, annotation=typing.Optional[MarimoTableGetColumnSummariesOutputData], direction="write"
                ),
                "stats": convert_and_respect_annotation_metadata(
                    object_=stats,
                    annotation=typing.Dict[str, MarimoTableGetColumnSummariesOutputStatsValue],
                    direction="write",
                ),
                "bin_values": convert_and_respect_annotation_metadata(
                    object_=bin_values,
                    annotation=typing.Dict[str, typing.Sequence[MarimoTableGetColumnSummariesOutputBinValuesValueItem]],
                    direction="write",
                ),
                "value_counts": convert_and_respect_annotation_metadata(
                    object_=value_counts,
                    annotation=typing.Dict[
                        str, typing.Sequence[MarimoTableGetColumnSummariesOutputValueCountsValueItem]
                    ],
                    direction="write",
                ),
                "show_charts": show_charts,
                "is_disabled": is_disabled,
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

    def read_marimo_table_get_data_url_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoTableGetDataUrlOutput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoTableGetDataUrlOutput]
            marimo-table get_data_url output accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/get_data_url/output",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoTableGetDataUrlOutput,
                    parse_obj_as(
                        type_=MarimoTableGetDataUrlOutput,
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

    def write_marimo_table_get_data_url_output(
        self,
        *,
        data_url: MarimoTableGetDataUrlOutputDataUrl,
        format: MarimoTableGetDataUrlOutputFormat,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        data_url : MarimoTableGetDataUrlOutputDataUrl

        format : MarimoTableGetDataUrlOutputFormat

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/get_data_url/output",
            method="PUT",
            json={
                "data_url": convert_and_respect_annotation_metadata(
                    object_=data_url, annotation=MarimoTableGetDataUrlOutputDataUrl, direction="write"
                ),
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

    def read_marimo_table_get_row_ids_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoTableGetRowIdsOutput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoTableGetRowIdsOutput]
            marimo-table get_row_ids output accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/get_row_ids/output",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoTableGetRowIdsOutput,
                    parse_obj_as(
                        type_=MarimoTableGetRowIdsOutput,
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

    def write_marimo_table_get_row_ids_output(
        self,
        *,
        row_ids: typing.Sequence[float],
        all_rows: bool,
        error: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/get_row_ids/output",
            method="PUT",
            json={
                "row_ids": row_ids,
                "all_rows": all_rows,
                "error": error,
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

    def read_marimo_table_get_size_bytes_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoTableGetSizeBytesOutput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoTableGetSizeBytesOutput]
            marimo-table get_size_bytes output accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/get_size_bytes/output",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoTableGetSizeBytesOutput,
                    parse_obj_as(
                        type_=MarimoTableGetSizeBytesOutput,
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

    def write_marimo_table_get_size_bytes_output(
        self, *, size_bytes: typing.Optional[float] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        size_bytes : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/get_size_bytes/output",
            method="PUT",
            json={
                "size_bytes": size_bytes,
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

    def read_marimo_table_preview_column_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoTablePreviewColumnOutput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoTablePreviewColumnOutput]
            marimo-table preview_column output accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/preview_column/output",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoTablePreviewColumnOutput,
                    parse_obj_as(
                        type_=MarimoTablePreviewColumnOutput,
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

    def write_marimo_table_preview_column_output(
        self,
        *,
        chart_spec: typing.Optional[str] = OMIT,
        chart_code: typing.Optional[str] = OMIT,
        error: typing.Optional[str] = OMIT,
        missing_packages: typing.Optional[typing.Sequence[str]] = OMIT,
        stats: typing.Optional[MarimoTablePreviewColumnOutputStats] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/preview_column/output",
            method="PUT",
            json={
                "chart_spec": chart_spec,
                "chart_code": chart_code,
                "error": error,
                "missing_packages": missing_packages,
                "stats": convert_and_respect_annotation_metadata(
                    object_=stats, annotation=typing.Optional[MarimoTablePreviewColumnOutputStats], direction="write"
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

    def read_marimo_table_search_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoTableSearchOutput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoTableSearchOutput]
            marimo-table search output accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/search/output",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoTableSearchOutput,
                    parse_obj_as(
                        type_=MarimoTableSearchOutput,
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
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/search/output",
            method="PUT",
            json={
                "data": convert_and_respect_annotation_metadata(
                    object_=data, annotation=MarimoTableSearchOutputData, direction="write"
                ),
                "total_rows": convert_and_respect_annotation_metadata(
                    object_=total_rows, annotation=MarimoTableSearchOutputTotalRows, direction="write"
                ),
                "cell_styles": cell_styles,
                "cell_hover_texts": cell_hover_texts,
                "raw_data": convert_and_respect_annotation_metadata(
                    object_=raw_data, annotation=typing.Optional[MarimoTableSearchOutputRawData], direction="write"
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


class AsyncRawRpcOutputClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def read_marimo_chatbot_cancel_prompt_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[MarimoChatbotCancelPromptOutput]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[MarimoChatbotCancelPromptOutput]]
            marimo-chatbot cancel_prompt output accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-chatbot/functions/cancel_prompt/output",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[MarimoChatbotCancelPromptOutput],
                    parse_obj_as(
                        type_=typing.Optional[MarimoChatbotCancelPromptOutput],
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

    async def write_marimo_chatbot_cancel_prompt_output(
        self,
        *,
        request: typing.Optional[MarimoChatbotCancelPromptOutput] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        request : typing.Optional[MarimoChatbotCancelPromptOutput]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-chatbot/functions/cancel_prompt/output",
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

    async def read_marimo_chatbot_delete_chat_history_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[MarimoChatbotDeleteChatHistoryOutput]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[MarimoChatbotDeleteChatHistoryOutput]]
            marimo-chatbot delete_chat_history output accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-chatbot/functions/delete_chat_history/output",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[MarimoChatbotDeleteChatHistoryOutput],
                    parse_obj_as(
                        type_=typing.Optional[MarimoChatbotDeleteChatHistoryOutput],
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

    async def write_marimo_chatbot_delete_chat_history_output(
        self,
        *,
        request: typing.Optional[MarimoChatbotDeleteChatHistoryOutput] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        request : typing.Optional[MarimoChatbotDeleteChatHistoryOutput]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-chatbot/functions/delete_chat_history/output",
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

    async def read_marimo_chatbot_delete_chat_message_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[MarimoChatbotDeleteChatMessageOutput]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[MarimoChatbotDeleteChatMessageOutput]]
            marimo-chatbot delete_chat_message output accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-chatbot/functions/delete_chat_message/output",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[MarimoChatbotDeleteChatMessageOutput],
                    parse_obj_as(
                        type_=typing.Optional[MarimoChatbotDeleteChatMessageOutput],
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

    async def write_marimo_chatbot_delete_chat_message_output(
        self,
        *,
        request: typing.Optional[MarimoChatbotDeleteChatMessageOutput] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        request : typing.Optional[MarimoChatbotDeleteChatMessageOutput]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-chatbot/functions/delete_chat_message/output",
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

    async def read_marimo_chatbot_get_chat_history_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoChatbotGetChatHistoryOutput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoChatbotGetChatHistoryOutput]
            marimo-chatbot get_chat_history output accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-chatbot/functions/get_chat_history/output",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoChatbotGetChatHistoryOutput,
                    parse_obj_as(
                        type_=MarimoChatbotGetChatHistoryOutput,
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

    async def write_marimo_chatbot_get_chat_history_output(
        self,
        *,
        messages: typing.Sequence[MarimoChatbotGetChatHistoryOutputMessagesItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        messages : typing.Sequence[MarimoChatbotGetChatHistoryOutputMessagesItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-chatbot/functions/get_chat_history/output",
            method="PUT",
            json={
                "messages": convert_and_respect_annotation_metadata(
                    object_=messages,
                    annotation=typing.Sequence[MarimoChatbotGetChatHistoryOutputMessagesItem],
                    direction="write",
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

    async def read_marimo_chatbot_send_prompt_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoChatbotSendPromptOutput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoChatbotSendPromptOutput]
            marimo-chatbot send_prompt output accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-chatbot/functions/send_prompt/output",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoChatbotSendPromptOutput,
                    parse_obj_as(
                        type_=MarimoChatbotSendPromptOutput,
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

    async def write_marimo_chatbot_send_prompt_output(
        self, *, request: MarimoChatbotSendPromptOutput, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        request : MarimoChatbotSendPromptOutput

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-chatbot/functions/send_prompt/output",
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

    async def read_marimo_dataframe_download_as_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoDataframeDownloadAsOutput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoDataframeDownloadAsOutput]
            marimo-dataframe download_as output accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-dataframe/functions/download_as/output",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoDataframeDownloadAsOutput,
                    parse_obj_as(
                        type_=MarimoDataframeDownloadAsOutput,
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

    async def write_marimo_dataframe_download_as_output(
        self,
        *,
        url: str,
        filename: str,
        error: typing.Optional[str] = OMIT,
        missing_packages: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-dataframe/functions/download_as/output",
            method="PUT",
            json={
                "url": url,
                "filename": filename,
                "error": error,
                "missing_packages": missing_packages,
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

    async def read_marimo_dataframe_get_column_values_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoDataframeGetColumnValuesOutput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoDataframeGetColumnValuesOutput]
            marimo-dataframe get_column_values output accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-dataframe/functions/get_column_values/output",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoDataframeGetColumnValuesOutput,
                    parse_obj_as(
                        type_=MarimoDataframeGetColumnValuesOutput,
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

    async def write_marimo_dataframe_get_column_values_output(
        self,
        *,
        values: typing.Sequence[typing.Any],
        too_many_values: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        values : typing.Sequence[typing.Any]

        too_many_values : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-dataframe/functions/get_column_values/output",
            method="PUT",
            json={
                "values": values,
                "too_many_values": too_many_values,
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

    async def read_marimo_dataframe_get_dataframe_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoDataframeGetDataframeOutput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoDataframeGetDataframeOutput]
            marimo-dataframe get_dataframe output accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-dataframe/functions/get_dataframe/output",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoDataframeGetDataframeOutput,
                    parse_obj_as(
                        type_=MarimoDataframeGetDataframeOutput,
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
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-dataframe/functions/get_dataframe/output",
            method="PUT",
            json={
                "url": url,
                "total_rows": total_rows,
                "row_headers": row_headers,
                "field_types": field_types,
                "column_types_per_step": column_types_per_step,
                "python_code": python_code,
                "sql_code": sql_code,
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

    async def read_marimo_dataframe_get_size_bytes_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoDataframeGetSizeBytesOutput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoDataframeGetSizeBytesOutput]
            marimo-dataframe get_size_bytes output accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-dataframe/functions/get_size_bytes/output",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoDataframeGetSizeBytesOutput,
                    parse_obj_as(
                        type_=MarimoDataframeGetSizeBytesOutput,
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

    async def write_marimo_dataframe_get_size_bytes_output(
        self, *, size_bytes: typing.Optional[float] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        size_bytes : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-dataframe/functions/get_size_bytes/output",
            method="PUT",
            json={
                "size_bytes": size_bytes,
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

    async def read_marimo_dataframe_search_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoDataframeSearchOutput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoDataframeSearchOutput]
            marimo-dataframe search output accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-dataframe/functions/search/output",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoDataframeSearchOutput,
                    parse_obj_as(
                        type_=MarimoDataframeSearchOutput,
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

    async def write_marimo_dataframe_search_output(
        self,
        *,
        data: MarimoDataframeSearchOutputData,
        total_rows: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        data : MarimoDataframeSearchOutputData

        total_rows : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-dataframe/functions/search/output",
            method="PUT",
            json={
                "data": convert_and_respect_annotation_metadata(
                    object_=data, annotation=MarimoDataframeSearchOutputData, direction="write"
                ),
                "total_rows": total_rows,
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

    async def read_marimo_download_load_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoDownloadLoadOutput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoDownloadLoadOutput]
            marimo-download load output accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-download/functions/load/output",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoDownloadLoadOutput,
                    parse_obj_as(
                        type_=MarimoDownloadLoadOutput,
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

    async def write_marimo_download_load_output(
        self,
        *,
        data: str,
        filename: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        data : str

        filename : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-download/functions/load/output",
            method="PUT",
            json={
                "data": data,
                "filename": filename,
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

    async def read_marimo_file_browser_list_directory_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoFileBrowserListDirectoryOutput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoFileBrowserListDirectoryOutput]
            marimo-file-browser list_directory output accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-file-browser/functions/list_directory/output",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoFileBrowserListDirectoryOutput,
                    parse_obj_as(
                        type_=MarimoFileBrowserListDirectoryOutput,
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

    async def write_marimo_file_browser_list_directory_output(
        self,
        *,
        files: typing.Sequence[MarimoFileBrowserListDirectoryOutputFilesItem],
        total_count: float,
        is_truncated: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-file-browser/functions/list_directory/output",
            method="PUT",
            json={
                "files": convert_and_respect_annotation_metadata(
                    object_=files,
                    annotation=typing.Sequence[MarimoFileBrowserListDirectoryOutputFilesItem],
                    direction="write",
                ),
                "total_count": total_count,
                "is_truncated": is_truncated,
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

    async def read_marimo_form_validate_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[MarimoFormValidateOutput]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[MarimoFormValidateOutput]]
            marimo-form validate output accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-form/functions/validate/output",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[MarimoFormValidateOutput],
                    parse_obj_as(
                        type_=typing.Optional[MarimoFormValidateOutput],
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

    async def write_marimo_form_validate_output(
        self,
        *,
        request: typing.Optional[MarimoFormValidateOutput] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        request : typing.Optional[MarimoFormValidateOutput]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-form/functions/validate/output",
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

    async def read_marimo_lazy_load_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoLazyLoadOutput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoLazyLoadOutput]
            marimo-lazy load output accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-lazy/functions/load/output",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoLazyLoadOutput,
                    parse_obj_as(
                        type_=MarimoLazyLoadOutput,
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

    async def write_marimo_lazy_load_output(
        self, *, html: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        html : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-lazy/functions/load/output",
            method="PUT",
            json={
                "html": html,
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

    async def read_marimo_panel_send_to_widget_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[MarimoPanelSendToWidgetOutput]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[MarimoPanelSendToWidgetOutput]]
            marimo-panel send_to_widget output accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-panel/functions/send_to_widget/output",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[MarimoPanelSendToWidgetOutput],
                    parse_obj_as(
                        type_=typing.Optional[MarimoPanelSendToWidgetOutput],
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

    async def write_marimo_panel_send_to_widget_output(
        self,
        *,
        request: typing.Optional[MarimoPanelSendToWidgetOutput] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        request : typing.Optional[MarimoPanelSendToWidgetOutput]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-panel/functions/send_to_widget/output",
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

    async def read_marimo_table_calculate_top_k_rows_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoTableCalculateTopKRowsOutput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoTableCalculateTopKRowsOutput]
            marimo-table calculate_top_k_rows output accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/calculate_top_k_rows/output",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoTableCalculateTopKRowsOutput,
                    parse_obj_as(
                        type_=MarimoTableCalculateTopKRowsOutput,
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

    async def write_marimo_table_calculate_top_k_rows_output(
        self,
        *,
        data: typing.Sequence[typing.Sequence[typing.Any]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        data : typing.Sequence[typing.Sequence[typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/calculate_top_k_rows/output",
            method="PUT",
            json={
                "data": data,
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

    async def read_marimo_table_download_as_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoTableDownloadAsOutput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoTableDownloadAsOutput]
            marimo-table download_as output accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/download_as/output",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoTableDownloadAsOutput,
                    parse_obj_as(
                        type_=MarimoTableDownloadAsOutput,
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

    async def write_marimo_table_download_as_output(
        self,
        *,
        url: str,
        filename: str,
        error: typing.Optional[str] = OMIT,
        missing_packages: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/download_as/output",
            method="PUT",
            json={
                "url": url,
                "filename": filename,
                "error": error,
                "missing_packages": missing_packages,
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

    async def read_marimo_table_get_column_summaries_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoTableGetColumnSummariesOutput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoTableGetColumnSummariesOutput]
            marimo-table get_column_summaries output accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/get_column_summaries/output",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoTableGetColumnSummariesOutput,
                    parse_obj_as(
                        type_=MarimoTableGetColumnSummariesOutput,
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
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/get_column_summaries/output",
            method="PUT",
            json={
                "data": convert_and_respect_annotation_metadata(
                    object_=data, annotation=typing.Optional[MarimoTableGetColumnSummariesOutputData], direction="write"
                ),
                "stats": convert_and_respect_annotation_metadata(
                    object_=stats,
                    annotation=typing.Dict[str, MarimoTableGetColumnSummariesOutputStatsValue],
                    direction="write",
                ),
                "bin_values": convert_and_respect_annotation_metadata(
                    object_=bin_values,
                    annotation=typing.Dict[str, typing.Sequence[MarimoTableGetColumnSummariesOutputBinValuesValueItem]],
                    direction="write",
                ),
                "value_counts": convert_and_respect_annotation_metadata(
                    object_=value_counts,
                    annotation=typing.Dict[
                        str, typing.Sequence[MarimoTableGetColumnSummariesOutputValueCountsValueItem]
                    ],
                    direction="write",
                ),
                "show_charts": show_charts,
                "is_disabled": is_disabled,
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

    async def read_marimo_table_get_data_url_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoTableGetDataUrlOutput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoTableGetDataUrlOutput]
            marimo-table get_data_url output accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/get_data_url/output",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoTableGetDataUrlOutput,
                    parse_obj_as(
                        type_=MarimoTableGetDataUrlOutput,
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

    async def write_marimo_table_get_data_url_output(
        self,
        *,
        data_url: MarimoTableGetDataUrlOutputDataUrl,
        format: MarimoTableGetDataUrlOutputFormat,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        data_url : MarimoTableGetDataUrlOutputDataUrl

        format : MarimoTableGetDataUrlOutputFormat

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/get_data_url/output",
            method="PUT",
            json={
                "data_url": convert_and_respect_annotation_metadata(
                    object_=data_url, annotation=MarimoTableGetDataUrlOutputDataUrl, direction="write"
                ),
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

    async def read_marimo_table_get_row_ids_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoTableGetRowIdsOutput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoTableGetRowIdsOutput]
            marimo-table get_row_ids output accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/get_row_ids/output",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoTableGetRowIdsOutput,
                    parse_obj_as(
                        type_=MarimoTableGetRowIdsOutput,
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

    async def write_marimo_table_get_row_ids_output(
        self,
        *,
        row_ids: typing.Sequence[float],
        all_rows: bool,
        error: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/get_row_ids/output",
            method="PUT",
            json={
                "row_ids": row_ids,
                "all_rows": all_rows,
                "error": error,
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

    async def read_marimo_table_get_size_bytes_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoTableGetSizeBytesOutput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoTableGetSizeBytesOutput]
            marimo-table get_size_bytes output accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/get_size_bytes/output",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoTableGetSizeBytesOutput,
                    parse_obj_as(
                        type_=MarimoTableGetSizeBytesOutput,
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

    async def write_marimo_table_get_size_bytes_output(
        self, *, size_bytes: typing.Optional[float] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        size_bytes : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/get_size_bytes/output",
            method="PUT",
            json={
                "size_bytes": size_bytes,
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

    async def read_marimo_table_preview_column_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoTablePreviewColumnOutput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoTablePreviewColumnOutput]
            marimo-table preview_column output accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/preview_column/output",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoTablePreviewColumnOutput,
                    parse_obj_as(
                        type_=MarimoTablePreviewColumnOutput,
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

    async def write_marimo_table_preview_column_output(
        self,
        *,
        chart_spec: typing.Optional[str] = OMIT,
        chart_code: typing.Optional[str] = OMIT,
        error: typing.Optional[str] = OMIT,
        missing_packages: typing.Optional[typing.Sequence[str]] = OMIT,
        stats: typing.Optional[MarimoTablePreviewColumnOutputStats] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/preview_column/output",
            method="PUT",
            json={
                "chart_spec": chart_spec,
                "chart_code": chart_code,
                "error": error,
                "missing_packages": missing_packages,
                "stats": convert_and_respect_annotation_metadata(
                    object_=stats, annotation=typing.Optional[MarimoTablePreviewColumnOutputStats], direction="write"
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

    async def read_marimo_table_search_output(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoTableSearchOutput]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoTableSearchOutput]
            marimo-table search output accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/search/output",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoTableSearchOutput,
                    parse_obj_as(
                        type_=MarimoTableSearchOutput,
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
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/functions/search/output",
            method="PUT",
            json={
                "data": convert_and_respect_annotation_metadata(
                    object_=data, annotation=MarimoTableSearchOutputData, direction="write"
                ),
                "total_rows": convert_and_respect_annotation_metadata(
                    object_=total_rows, annotation=MarimoTableSearchOutputTotalRows, direction="write"
                ),
                "cell_styles": cell_styles,
                "cell_hover_texts": cell_hover_texts,
                "raw_data": convert_and_respect_annotation_metadata(
                    object_=raw_data, annotation=typing.Optional[MarimoTableSearchOutputRawData], direction="write"
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
