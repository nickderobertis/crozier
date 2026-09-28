

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.marimo_accordion_data import MarimoAccordionData
from ..types.marimo_anywidget_data import MarimoAnywidgetData
from ..types.marimo_button_data import MarimoButtonData
from ..types.marimo_button_data_kind import MarimoButtonDataKind
from ..types.marimo_callout_output_data import MarimoCalloutOutputData
from ..types.marimo_callout_output_data_kind import MarimoCalloutOutputDataKind
from ..types.marimo_carousel_data import MarimoCarouselData
from ..types.marimo_carousel_data_height import MarimoCarouselDataHeight
from ..types.marimo_chatbot_data import MarimoChatbotData
from ..types.marimo_chatbot_data_allow_attachments import MarimoChatbotDataAllowAttachments
from ..types.marimo_chatbot_data_config import MarimoChatbotDataConfig
from ..types.marimo_checkbox_data import MarimoCheckboxData
from ..types.marimo_code_editor_data import MarimoCodeEditorData
from ..types.marimo_code_editor_data_debounce import MarimoCodeEditorDataDebounce
from ..types.marimo_code_editor_data_theme import MarimoCodeEditorDataTheme
from ..types.marimo_data_editor_data import MarimoDataEditorData
from ..types.marimo_data_editor_data_column_sizing_mode import MarimoDataEditorDataColumnSizingMode
from ..types.marimo_data_editor_data_data import MarimoDataEditorDataData
from ..types.marimo_data_editor_data_editable_columns import MarimoDataEditorDataEditableColumns
from ..types.marimo_data_editor_data_initial_value import MarimoDataEditorDataInitialValue
from ..types.marimo_data_explorer_data import MarimoDataExplorerData
from ..types.marimo_dataframe_data import MarimoDataframeData
from ..types.marimo_date_data import MarimoDateData
from ..types.marimo_date_range_data import MarimoDateRangeData
from ..types.marimo_datetime_data import MarimoDatetimeData
from ..types.marimo_datetime_data_precision import MarimoDatetimeDataPrecision
from ..types.marimo_dict_data import MarimoDictData
from ..types.marimo_download_data import MarimoDownloadData
from ..types.marimo_dropdown_data import MarimoDropdownData
from ..types.marimo_file_browser_data import MarimoFileBrowserData
from ..types.marimo_file_data import MarimoFileData
from ..types.marimo_file_data_kind import MarimoFileDataKind
from ..types.marimo_form_data import MarimoFormData
from ..types.marimo_image_comparison_data import MarimoImageComparisonData
from ..types.marimo_image_comparison_data_direction import MarimoImageComparisonDataDirection
from ..types.marimo_json_output_data import MarimoJsonOutputData
from ..types.marimo_json_output_data_value_types import MarimoJsonOutputDataValueTypes
from ..types.marimo_lazy_data import MarimoLazyData
from ..types.marimo_matplotlib_data import MarimoMatplotlibData
from ..types.marimo_matplotlib_data_x_scale import MarimoMatplotlibDataXScale
from ..types.marimo_matplotlib_data_y_scale import MarimoMatplotlibDataYScale
from ..types.marimo_matrix_data import MarimoMatrixData
from ..types.marimo_mermaid_data import MarimoMermaidData
from ..types.marimo_microphone_data import MarimoMicrophoneData
from ..types.marimo_mime_renderer_data import MarimoMimeRendererData
from ..types.marimo_mime_renderer_data_data import MarimoMimeRendererDataData
from ..types.marimo_mpl_interactive_data import MarimoMplInteractiveData
from ..types.marimo_multiselect_data import MarimoMultiselectData
from ..types.marimo_nav_menu_data import MarimoNavMenuData
from ..types.marimo_nav_menu_data_items_item import MarimoNavMenuDataItemsItem
from ..types.marimo_nav_menu_data_orientation import MarimoNavMenuDataOrientation
from ..types.marimo_number_data import MarimoNumberData
from ..types.marimo_outline_data import MarimoOutlineData
from ..types.marimo_panel_data import MarimoPanelData
from ..types.marimo_panel_data_render_json import MarimoPanelDataRenderJson
from ..types.marimo_plotly_data import MarimoPlotlyData
from ..types.marimo_progress_data import MarimoProgressData
from ..types.marimo_progress_data_progress import MarimoProgressDataProgress
from ..types.marimo_radio_data import MarimoRadioData
from ..types.marimo_range_slider_data import MarimoRangeSliderData
from ..types.marimo_range_slider_data_orientation import MarimoRangeSliderDataOrientation
from ..types.marimo_refresh_data import MarimoRefreshData
from ..types.marimo_refresh_data_default_interval import MarimoRefreshDataDefaultInterval
from ..types.marimo_refresh_data_options_item import MarimoRefreshDataOptionsItem
from ..types.marimo_routes_data import MarimoRoutesData
from ..types.marimo_slider_data import MarimoSliderData
from ..types.marimo_slider_data_orientation import MarimoSliderDataOrientation
from ..types.marimo_stat_data import MarimoStatData
from ..types.marimo_stat_data_direction import MarimoStatDataDirection
from ..types.marimo_stat_data_target_direction import MarimoStatDataTargetDirection
from ..types.marimo_stat_data_value import MarimoStatDataValue
from ..types.marimo_switch_data import MarimoSwitchData
from ..types.marimo_table_data import MarimoTableData
from ..types.marimo_table_data_data import MarimoTableDataData
from ..types.marimo_table_data_initial_value import MarimoTableDataInitialValue
from ..types.marimo_table_data_max_columns import MarimoTableDataMaxColumns
from ..types.marimo_table_data_raw_data import MarimoTableDataRawData
from ..types.marimo_table_data_selection import MarimoTableDataSelection
from ..types.marimo_table_data_show_column_summaries import MarimoTableDataShowColumnSummaries
from ..types.marimo_table_data_text_justify_columns_value import MarimoTableDataTextJustifyColumnsValue
from ..types.marimo_table_data_total_rows import MarimoTableDataTotalRows
from ..types.marimo_tabs_data import MarimoTabsData
from ..types.marimo_tabs_data_orientation import MarimoTabsDataOrientation
from ..types.marimo_tex_data import MarimoTexData
from ..types.marimo_text_area_data import MarimoTextAreaData
from ..types.marimo_text_area_data_debounce import MarimoTextAreaDataDebounce
from ..types.marimo_text_data import MarimoTextData
from ..types.marimo_text_data_debounce import MarimoTextDataDebounce
from ..types.marimo_text_data_kind import MarimoTextDataKind
from ..types.marimo_vega_data import MarimoVegaData
from ..types.marimo_vega_data_chart_selection import MarimoVegaDataChartSelection
from ..types.marimo_vega_data_field_selection import MarimoVegaDataFieldSelection
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPluginDataClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def read_marimo_accordion_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoAccordionData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoAccordionData]
            marimo-accordion data accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-accordion/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoAccordionData,
                    parse_obj_as(
                        type_=MarimoAccordionData,
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

    def write_marimo_accordion_data(
        self,
        *,
        labels: typing.Sequence[str],
        multiple: bool,
        expanded: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        labels : typing.Sequence[str]

        multiple : bool

        expanded : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-accordion/data",
            method="PUT",
            json={
                "labels": labels,
                "multiple": multiple,
                "expanded": expanded,
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

    def read_marimo_anywidget_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoAnywidgetData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoAnywidgetData]
            marimo-anywidget data accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-anywidget/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoAnywidgetData,
                    parse_obj_as(
                        type_=MarimoAnywidgetData,
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

    def write_marimo_anywidget_data(
        self, *, model_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        model_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-anywidget/data",
            method="PUT",
            json={
                "modelId": model_id,
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

    def read_marimo_button_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoButtonData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoButtonData]
            marimo-button data accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-button/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoButtonData,
                    parse_obj_as(
                        type_=MarimoButtonData,
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

    def write_marimo_button_data(
        self,
        *,
        label: str,
        kind: typing.Optional[MarimoButtonDataKind] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        full_width: typing.Optional[bool] = OMIT,
        tooltip: typing.Optional[str] = OMIT,
        keyboard_shortcut: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        label : str

        kind : typing.Optional[MarimoButtonDataKind]

        disabled : typing.Optional[bool]

        full_width : typing.Optional[bool]

        tooltip : typing.Optional[str]

        keyboard_shortcut : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-button/data",
            method="PUT",
            json={
                "label": label,
                "kind": kind,
                "disabled": disabled,
                "fullWidth": full_width,
                "tooltip": tooltip,
                "keyboardShortcut": keyboard_shortcut,
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

    def read_marimo_callout_output_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoCalloutOutputData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoCalloutOutputData]
            marimo-callout-output data accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-callout-output/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoCalloutOutputData,
                    parse_obj_as(
                        type_=MarimoCalloutOutputData,
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

    def write_marimo_callout_output_data(
        self,
        *,
        html: str,
        kind: typing.Optional[MarimoCalloutOutputDataKind] = OMIT,
        title: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        html : str

        kind : typing.Optional[MarimoCalloutOutputDataKind]

        title : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-callout-output/data",
            method="PUT",
            json={
                "html": html,
                "kind": kind,
                "title": title,
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

    def read_marimo_carousel_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoCarouselData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoCarouselData]
            marimo-carousel data accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-carousel/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoCarouselData,
                    parse_obj_as(
                        type_=MarimoCarouselData,
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

    def write_marimo_carousel_data(
        self,
        *,
        index: typing.Optional[str] = OMIT,
        height: typing.Optional[MarimoCarouselDataHeight] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        index : typing.Optional[str]

        height : typing.Optional[MarimoCarouselDataHeight]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-carousel/data",
            method="PUT",
            json={
                "index": index,
                "height": convert_and_respect_annotation_metadata(
                    object_=height, annotation=typing.Optional[MarimoCarouselDataHeight], direction="write"
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

    def read_marimo_chatbot_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoChatbotData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoChatbotData]
            marimo-chatbot data accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-chatbot/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoChatbotData,
                    parse_obj_as(
                        type_=MarimoChatbotData,
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

    def write_marimo_chatbot_data(
        self,
        *,
        show_configuration_controls: bool,
        config: MarimoChatbotDataConfig,
        allow_attachments: MarimoChatbotDataAllowAttachments,
        prompts: typing.Optional[typing.Sequence[str]] = OMIT,
        max_height: typing.Optional[float] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        show_configuration_controls : bool

        config : MarimoChatbotDataConfig

        allow_attachments : MarimoChatbotDataAllowAttachments

        prompts : typing.Optional[typing.Sequence[str]]

        max_height : typing.Optional[float]

        disabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-chatbot/data",
            method="PUT",
            json={
                "prompts": prompts,
                "showConfigurationControls": show_configuration_controls,
                "maxHeight": max_height,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=MarimoChatbotDataConfig, direction="write"
                ),
                "allowAttachments": convert_and_respect_annotation_metadata(
                    object_=allow_attachments, annotation=MarimoChatbotDataAllowAttachments, direction="write"
                ),
                "disabled": disabled,
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

    def read_marimo_checkbox_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoCheckboxData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoCheckboxData]
            marimo-checkbox data accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-checkbox/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoCheckboxData,
                    parse_obj_as(
                        type_=MarimoCheckboxData,
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

    def write_marimo_checkbox_data(
        self,
        *,
        initial_value: bool,
        label: typing.Optional[str] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        initial_value : bool

        label : typing.Optional[str]

        disabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-checkbox/data",
            method="PUT",
            json={
                "initialValue": initial_value,
                "label": label,
                "disabled": disabled,
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

    def read_marimo_code_editor_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoCodeEditorData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoCodeEditorData]
            marimo-code-editor data accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-code-editor/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoCodeEditorData,
                    parse_obj_as(
                        type_=MarimoCodeEditorData,
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

    def write_marimo_code_editor_data(
        self,
        *,
        initial_value: str,
        placeholder: str,
        language: typing.Optional[str] = OMIT,
        theme: typing.Optional[MarimoCodeEditorDataTheme] = OMIT,
        label: typing.Optional[str] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        min_height: typing.Optional[float] = OMIT,
        max_height: typing.Optional[float] = OMIT,
        show_copy_button: typing.Optional[bool] = OMIT,
        debounce: typing.Optional[MarimoCodeEditorDataDebounce] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        initial_value : str

        placeholder : str

        language : typing.Optional[str]

        theme : typing.Optional[MarimoCodeEditorDataTheme]

        label : typing.Optional[str]

        disabled : typing.Optional[bool]

        min_height : typing.Optional[float]

        max_height : typing.Optional[float]

        show_copy_button : typing.Optional[bool]

        debounce : typing.Optional[MarimoCodeEditorDataDebounce]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-code-editor/data",
            method="PUT",
            json={
                "initialValue": initial_value,
                "language": language,
                "placeholder": placeholder,
                "theme": theme,
                "label": label,
                "disabled": disabled,
                "minHeight": min_height,
                "maxHeight": max_height,
                "showCopyButton": show_copy_button,
                "debounce": convert_and_respect_annotation_metadata(
                    object_=debounce, annotation=MarimoCodeEditorDataDebounce, direction="write"
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

    def read_marimo_data_editor_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoDataEditorData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoDataEditorData]
            marimo-data-editor data accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-data-editor/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoDataEditorData,
                    parse_obj_as(
                        type_=MarimoDataEditorData,
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

    def write_marimo_data_editor_data(
        self,
        *,
        initial_value: MarimoDataEditorDataInitialValue,
        data: MarimoDataEditorDataData,
        editable_columns: MarimoDataEditorDataEditableColumns,
        label: typing.Optional[str] = OMIT,
        field_types: typing.Optional[typing.Sequence[typing.Sequence[typing.Any]]] = OMIT,
        column_names: typing.Optional[typing.Sequence[str]] = OMIT,
        column_sizing_mode: typing.Optional[MarimoDataEditorDataColumnSizingMode] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        initial_value : MarimoDataEditorDataInitialValue

        data : MarimoDataEditorDataData

        editable_columns : MarimoDataEditorDataEditableColumns

        label : typing.Optional[str]

        field_types : typing.Optional[typing.Sequence[typing.Sequence[typing.Any]]]

        column_names : typing.Optional[typing.Sequence[str]]

        column_sizing_mode : typing.Optional[MarimoDataEditorDataColumnSizingMode]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-data-editor/data",
            method="PUT",
            json={
                "initialValue": convert_and_respect_annotation_metadata(
                    object_=initial_value, annotation=MarimoDataEditorDataInitialValue, direction="write"
                ),
                "label": label,
                "data": convert_and_respect_annotation_metadata(
                    object_=data, annotation=MarimoDataEditorDataData, direction="write"
                ),
                "fieldTypes": field_types,
                "columnNames": column_names,
                "editableColumns": convert_and_respect_annotation_metadata(
                    object_=editable_columns, annotation=MarimoDataEditorDataEditableColumns, direction="write"
                ),
                "columnSizingMode": column_sizing_mode,
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

    def read_marimo_data_explorer_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoDataExplorerData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoDataExplorerData]
            marimo-data-explorer data accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-data-explorer/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoDataExplorerData,
                    parse_obj_as(
                        type_=MarimoDataExplorerData,
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

    def write_marimo_data_explorer_data(
        self, *, data: str, label: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        data : str

        label : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-data-explorer/data",
            method="PUT",
            json={
                "label": label,
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

    def read_marimo_dataframe_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoDataframeData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoDataframeData]
            marimo-dataframe data accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-dataframe/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoDataframeData,
                    parse_obj_as(
                        type_=MarimoDataframeData,
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

    def write_marimo_dataframe_data(
        self,
        *,
        columns: typing.Sequence[typing.Sequence[typing.Any]],
        label: typing.Optional[str] = OMIT,
        page_size: typing.Optional[float] = OMIT,
        show_download: typing.Optional[bool] = OMIT,
        dataframe_name: typing.Optional[str] = OMIT,
        lazy: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        columns : typing.Sequence[typing.Sequence[typing.Any]]

        label : typing.Optional[str]

        page_size : typing.Optional[float]

        show_download : typing.Optional[bool]

        dataframe_name : typing.Optional[str]

        lazy : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-dataframe/data",
            method="PUT",
            json={
                "label": label,
                "pageSize": page_size,
                "showDownload": show_download,
                "dataframeName": dataframe_name,
                "columns": columns,
                "lazy": lazy,
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

    def read_marimo_date_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoDateData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoDateData]
            marimo-date data accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-date/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoDateData,
                    parse_obj_as(
                        type_=MarimoDateData,
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

    def write_marimo_date_data(
        self,
        *,
        initial_value: str,
        start: str,
        stop: str,
        label: typing.Optional[str] = OMIT,
        step: typing.Optional[str] = OMIT,
        full_width: typing.Optional[bool] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        initial_value : str

        start : str

        stop : str

        label : typing.Optional[str]

        step : typing.Optional[str]

        full_width : typing.Optional[bool]

        disabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-date/data",
            method="PUT",
            json={
                "initialValue": initial_value,
                "label": label,
                "start": start,
                "stop": stop,
                "step": step,
                "fullWidth": full_width,
                "disabled": disabled,
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

    def read_marimo_date_range_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoDateRangeData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoDateRangeData]
            marimo-date-range data accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-date-range/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoDateRangeData,
                    parse_obj_as(
                        type_=MarimoDateRangeData,
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

    def write_marimo_date_range_data(
        self,
        *,
        initial_value: typing.Sequence[typing.Any],
        start: str,
        stop: str,
        label: typing.Optional[str] = OMIT,
        step: typing.Optional[str] = OMIT,
        full_width: typing.Optional[bool] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        initial_value : typing.Sequence[typing.Any]

        start : str

        stop : str

        label : typing.Optional[str]

        step : typing.Optional[str]

        full_width : typing.Optional[bool]

        disabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-date-range/data",
            method="PUT",
            json={
                "initialValue": initial_value,
                "label": label,
                "start": start,
                "stop": stop,
                "step": step,
                "fullWidth": full_width,
                "disabled": disabled,
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

    def read_marimo_datetime_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoDatetimeData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoDatetimeData]
            marimo-datetime data accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-datetime/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoDatetimeData,
                    parse_obj_as(
                        type_=MarimoDatetimeData,
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

    def write_marimo_datetime_data(
        self,
        *,
        initial_value: str,
        start: str,
        stop: str,
        label: typing.Optional[str] = OMIT,
        step: typing.Optional[str] = OMIT,
        precision: typing.Optional[MarimoDatetimeDataPrecision] = OMIT,
        full_width: typing.Optional[bool] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        initial_value : str

        start : str

        stop : str

        label : typing.Optional[str]

        step : typing.Optional[str]

        precision : typing.Optional[MarimoDatetimeDataPrecision]

        full_width : typing.Optional[bool]

        disabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-datetime/data",
            method="PUT",
            json={
                "initialValue": initial_value,
                "label": label,
                "start": start,
                "stop": stop,
                "step": step,
                "precision": precision,
                "fullWidth": full_width,
                "disabled": disabled,
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

    def read_marimo_dict_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoDictData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoDictData]
            marimo-dict data accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-dict/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoDictData,
                    parse_obj_as(
                        type_=MarimoDictData,
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

    def write_marimo_dict_data(
        self,
        *,
        element_ids: typing.Dict[str, str],
        label: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        element_ids : typing.Dict[str, str]

        label : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-dict/data",
            method="PUT",
            json={
                "label": label,
                "elementIds": element_ids,
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

    def read_marimo_download_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoDownloadData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoDownloadData]
            marimo-download data accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-download/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoDownloadData,
                    parse_obj_as(
                        type_=MarimoDownloadData,
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

    def write_marimo_download_data(
        self,
        *,
        data: str,
        disabled: typing.Optional[bool] = OMIT,
        filename: typing.Optional[str] = OMIT,
        label: typing.Optional[str] = OMIT,
        lazy: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        data : str

        disabled : typing.Optional[bool]

        filename : typing.Optional[str]

        label : typing.Optional[str]

        lazy : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-download/data",
            method="PUT",
            json={
                "data": data,
                "disabled": disabled,
                "filename": filename,
                "label": label,
                "lazy": lazy,
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

    def read_marimo_dropdown_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoDropdownData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoDropdownData]
            marimo-dropdown data accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-dropdown/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoDropdownData,
                    parse_obj_as(
                        type_=MarimoDropdownData,
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

    def write_marimo_dropdown_data(
        self,
        *,
        initial_value: typing.Sequence[str],
        options: typing.Sequence[str],
        allow_select_none: bool,
        label: typing.Optional[str] = OMIT,
        full_width: typing.Optional[bool] = OMIT,
        searchable: typing.Optional[bool] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        initial_value : typing.Sequence[str]

        options : typing.Sequence[str]

        allow_select_none : bool

        label : typing.Optional[str]

        full_width : typing.Optional[bool]

        searchable : typing.Optional[bool]

        disabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-dropdown/data",
            method="PUT",
            json={
                "initialValue": initial_value,
                "label": label,
                "options": options,
                "allowSelectNone": allow_select_none,
                "fullWidth": full_width,
                "searchable": searchable,
                "disabled": disabled,
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

    def read_marimo_file_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoFileData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoFileData]
            marimo-file data accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-file/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoFileData,
                    parse_obj_as(
                        type_=MarimoFileData,
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

    def write_marimo_file_data(
        self,
        *,
        filetypes: typing.Sequence[str],
        multiple: bool,
        kind: MarimoFileDataKind,
        max_size: float,
        label: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        filetypes : typing.Sequence[str]

        multiple : bool

        kind : MarimoFileDataKind

        max_size : float

        label : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-file/data",
            method="PUT",
            json={
                "filetypes": filetypes,
                "multiple": multiple,
                "kind": kind,
                "label": label,
                "max_size": max_size,
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

    def read_marimo_file_browser_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoFileBrowserData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoFileBrowserData]
            marimo-file-browser data accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-file-browser/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoFileBrowserData,
                    parse_obj_as(
                        type_=MarimoFileBrowserData,
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

    def write_marimo_file_browser_data(
        self,
        *,
        initial_path: str,
        filetypes: typing.Sequence[str],
        selection_mode: str,
        multiple: bool,
        restrict_navigation: bool,
        label: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        initial_path : str

        filetypes : typing.Sequence[str]

        selection_mode : str

        multiple : bool

        restrict_navigation : bool

        label : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-file-browser/data",
            method="PUT",
            json={
                "initialPath": initial_path,
                "filetypes": filetypes,
                "selectionMode": selection_mode,
                "multiple": multiple,
                "label": label,
                "restrictNavigation": restrict_navigation,
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

    def read_marimo_form_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoFormData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoFormData]
            marimo-form data accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-form/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoFormData,
                    parse_obj_as(
                        type_=MarimoFormData,
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

    def write_marimo_form_data(
        self,
        *,
        element_id: str,
        label: typing.Optional[str] = OMIT,
        bordered: typing.Optional[bool] = OMIT,
        loading: typing.Optional[bool] = OMIT,
        submit_button_label: typing.Optional[str] = OMIT,
        submit_button_tooltip: typing.Optional[str] = OMIT,
        submit_button_disabled: typing.Optional[bool] = OMIT,
        clear_on_submit: typing.Optional[bool] = OMIT,
        show_clear_button: typing.Optional[bool] = OMIT,
        clear_button_label: typing.Optional[str] = OMIT,
        clear_button_tooltip: typing.Optional[str] = OMIT,
        should_validate: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        element_id : str

        label : typing.Optional[str]

        bordered : typing.Optional[bool]

        loading : typing.Optional[bool]

        submit_button_label : typing.Optional[str]

        submit_button_tooltip : typing.Optional[str]

        submit_button_disabled : typing.Optional[bool]

        clear_on_submit : typing.Optional[bool]

        show_clear_button : typing.Optional[bool]

        clear_button_label : typing.Optional[str]

        clear_button_tooltip : typing.Optional[str]

        should_validate : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-form/data",
            method="PUT",
            json={
                "label": label,
                "elementId": element_id,
                "bordered": bordered,
                "loading": loading,
                "submitButtonLabel": submit_button_label,
                "submitButtonTooltip": submit_button_tooltip,
                "submitButtonDisabled": submit_button_disabled,
                "clearOnSubmit": clear_on_submit,
                "showClearButton": show_clear_button,
                "clearButtonLabel": clear_button_label,
                "clearButtonTooltip": clear_button_tooltip,
                "shouldValidate": should_validate,
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

    def read_marimo_image_comparison_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoImageComparisonData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoImageComparisonData]
            marimo-image-comparison data accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-image-comparison/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoImageComparisonData,
                    parse_obj_as(
                        type_=MarimoImageComparisonData,
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

    def write_marimo_image_comparison_data(
        self,
        *,
        before_src: str,
        after_src: str,
        value: typing.Optional[float] = OMIT,
        direction: typing.Optional[MarimoImageComparisonDataDirection] = OMIT,
        width: typing.Optional[str] = OMIT,
        height: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        before_src : str

        after_src : str

        value : typing.Optional[float]

        direction : typing.Optional[MarimoImageComparisonDataDirection]

        width : typing.Optional[str]

        height : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-image-comparison/data",
            method="PUT",
            json={
                "beforeSrc": before_src,
                "afterSrc": after_src,
                "value": value,
                "direction": direction,
                "width": width,
                "height": height,
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

    def read_marimo_json_output_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoJsonOutputData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoJsonOutputData]
            marimo-json-output data accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-json-output/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoJsonOutputData,
                    parse_obj_as(
                        type_=MarimoJsonOutputData,
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

    def write_marimo_json_output_data(
        self,
        *,
        json_data: typing.Any,
        name: typing.Optional[str] = OMIT,
        value_types: typing.Optional[MarimoJsonOutputDataValueTypes] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        json_data : typing.Any

        name : typing.Optional[str]

        value_types : typing.Optional[MarimoJsonOutputDataValueTypes]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-json-output/data",
            method="PUT",
            json={
                "name": name,
                "jsonData": json_data,
                "valueTypes": value_types,
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

    def read_marimo_lazy_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoLazyData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoLazyData]
            marimo-lazy data accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-lazy/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoLazyData,
                    parse_obj_as(
                        type_=MarimoLazyData,
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

    def write_marimo_lazy_data(
        self,
        *,
        show_loading_indicator: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        show_loading_indicator : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-lazy/data",
            method="PUT",
            json={
                "showLoadingIndicator": show_loading_indicator,
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

    def read_marimo_matplotlib_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoMatplotlibData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoMatplotlibData]
            marimo-matplotlib data accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-matplotlib/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoMatplotlibData,
                    parse_obj_as(
                        type_=MarimoMatplotlibData,
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

    def write_marimo_matplotlib_data(
        self,
        *,
        chart_base64: str,
        x_bounds: typing.Sequence[typing.Any],
        y_bounds: typing.Sequence[typing.Any],
        axes_pixel_bounds: typing.Sequence[typing.Any],
        width: float,
        height: float,
        debounce: bool,
        selection_color: typing.Optional[str] = OMIT,
        selection_opacity: typing.Optional[float] = OMIT,
        stroke_width: typing.Optional[float] = OMIT,
        x_scale: typing.Optional[MarimoMatplotlibDataXScale] = OMIT,
        y_scale: typing.Optional[MarimoMatplotlibDataYScale] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        chart_base64 : str

        x_bounds : typing.Sequence[typing.Any]

        y_bounds : typing.Sequence[typing.Any]

        axes_pixel_bounds : typing.Sequence[typing.Any]

        width : float

        height : float

        debounce : bool

        selection_color : typing.Optional[str]

        selection_opacity : typing.Optional[float]

        stroke_width : typing.Optional[float]

        x_scale : typing.Optional[MarimoMatplotlibDataXScale]

        y_scale : typing.Optional[MarimoMatplotlibDataYScale]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-matplotlib/data",
            method="PUT",
            json={
                "chartBase64": chart_base64,
                "xBounds": x_bounds,
                "yBounds": y_bounds,
                "axesPixelBounds": axes_pixel_bounds,
                "width": width,
                "height": height,
                "selectionColor": selection_color,
                "selectionOpacity": selection_opacity,
                "strokeWidth": stroke_width,
                "debounce": debounce,
                "xScale": x_scale,
                "yScale": y_scale,
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

    def read_marimo_matrix_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoMatrixData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoMatrixData]
            marimo-matrix data accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-matrix/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoMatrixData,
                    parse_obj_as(
                        type_=MarimoMatrixData,
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

    def write_marimo_matrix_data(
        self,
        *,
        initial_value: typing.Sequence[typing.Sequence[float]],
        step: typing.Sequence[typing.Sequence[float]],
        precision: float,
        symmetric: bool,
        scientific: bool,
        disabled: typing.Sequence[typing.Sequence[bool]],
        label: typing.Optional[str] = OMIT,
        min_value: typing.Optional[typing.Sequence[typing.Sequence[float]]] = OMIT,
        max_value: typing.Optional[typing.Sequence[typing.Sequence[float]]] = OMIT,
        row_labels: typing.Optional[typing.Sequence[str]] = OMIT,
        column_labels: typing.Optional[typing.Sequence[str]] = OMIT,
        debounce: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        initial_value : typing.Sequence[typing.Sequence[float]]

        step : typing.Sequence[typing.Sequence[float]]

        precision : float

        symmetric : bool

        scientific : bool

        disabled : typing.Sequence[typing.Sequence[bool]]

        label : typing.Optional[str]

        min_value : typing.Optional[typing.Sequence[typing.Sequence[float]]]

        max_value : typing.Optional[typing.Sequence[typing.Sequence[float]]]

        row_labels : typing.Optional[typing.Sequence[str]]

        column_labels : typing.Optional[typing.Sequence[str]]

        debounce : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-matrix/data",
            method="PUT",
            json={
                "initialValue": initial_value,
                "label": label,
                "minValue": min_value,
                "maxValue": max_value,
                "step": step,
                "precision": precision,
                "rowLabels": row_labels,
                "columnLabels": column_labels,
                "symmetric": symmetric,
                "debounce": debounce,
                "scientific": scientific,
                "disabled": disabled,
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

    def read_marimo_mermaid_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoMermaidData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoMermaidData]
            marimo-mermaid data accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-mermaid/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoMermaidData,
                    parse_obj_as(
                        type_=MarimoMermaidData,
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

    def write_marimo_mermaid_data(
        self,
        *,
        diagram: str,
        theme: typing.Optional[str] = OMIT,
        theme_variables: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        diagram : str

        theme : typing.Optional[str]

        theme_variables : typing.Optional[typing.Dict[str, str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-mermaid/data",
            method="PUT",
            json={
                "diagram": diagram,
                "theme": theme,
                "theme_variables": theme_variables,
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

    def read_marimo_microphone_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoMicrophoneData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoMicrophoneData]
            marimo-microphone data accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-microphone/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoMicrophoneData,
                    parse_obj_as(
                        type_=MarimoMicrophoneData,
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

    def write_marimo_microphone_data(
        self, *, label: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        label : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-microphone/data",
            method="PUT",
            json={
                "label": label,
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

    def read_marimo_mime_renderer_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoMimeRendererData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoMimeRendererData]
            marimo-mime-renderer data accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-mime-renderer/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoMimeRendererData,
                    parse_obj_as(
                        type_=MarimoMimeRendererData,
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

    def write_marimo_mime_renderer_data(
        self,
        *,
        mime: str,
        data: typing.Optional[MarimoMimeRendererDataData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        mime : str

        data : typing.Optional[MarimoMimeRendererDataData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-mime-renderer/data",
            method="PUT",
            json={
                "mime": mime,
                "data": convert_and_respect_annotation_metadata(
                    object_=data, annotation=typing.Optional[MarimoMimeRendererDataData], direction="write"
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

    def read_marimo_mpl_interactive_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoMplInteractiveData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoMplInteractiveData]
            marimo-mpl-interactive data accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-mpl-interactive/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoMplInteractiveData,
                    parse_obj_as(
                        type_=MarimoMplInteractiveData,
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

    def write_marimo_mpl_interactive_data(
        self,
        *,
        mpl_js_url: str,
        css_url: str,
        toolbar_images: typing.Dict[str, str],
        width: float,
        height: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        mpl_js_url : str

        css_url : str

        toolbar_images : typing.Dict[str, str]

        width : float

        height : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-mpl-interactive/data",
            method="PUT",
            json={
                "mplJsUrl": mpl_js_url,
                "cssUrl": css_url,
                "toolbarImages": toolbar_images,
                "width": width,
                "height": height,
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

    def read_marimo_multiselect_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoMultiselectData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoMultiselectData]
            marimo-multiselect data accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-multiselect/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoMultiselectData,
                    parse_obj_as(
                        type_=MarimoMultiselectData,
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

    def write_marimo_multiselect_data(
        self,
        *,
        initial_value: typing.Sequence[str],
        options: typing.Sequence[str],
        label: typing.Optional[str] = OMIT,
        full_width: typing.Optional[bool] = OMIT,
        max_selections: typing.Optional[float] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        initial_value : typing.Sequence[str]

        options : typing.Sequence[str]

        label : typing.Optional[str]

        full_width : typing.Optional[bool]

        max_selections : typing.Optional[float]

        disabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-multiselect/data",
            method="PUT",
            json={
                "initialValue": initial_value,
                "label": label,
                "options": options,
                "fullWidth": full_width,
                "maxSelections": max_selections,
                "disabled": disabled,
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

    def read_marimo_nav_menu_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoNavMenuData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoNavMenuData]
            marimo-nav-menu data accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-nav-menu/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoNavMenuData,
                    parse_obj_as(
                        type_=MarimoNavMenuData,
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

    def write_marimo_nav_menu_data(
        self,
        *,
        items: typing.Sequence[MarimoNavMenuDataItemsItem],
        orientation: MarimoNavMenuDataOrientation,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        items : typing.Sequence[MarimoNavMenuDataItemsItem]

        orientation : MarimoNavMenuDataOrientation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-nav-menu/data",
            method="PUT",
            json={
                "items": convert_and_respect_annotation_metadata(
                    object_=items, annotation=typing.Sequence[MarimoNavMenuDataItemsItem], direction="write"
                ),
                "orientation": orientation,
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

    def read_marimo_number_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoNumberData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoNumberData]
            marimo-number data accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-number/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoNumberData,
                    parse_obj_as(
                        type_=MarimoNumberData,
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

    def write_marimo_number_data(
        self,
        *,
        initial_value: typing.Optional[float] = OMIT,
        label: typing.Optional[str] = OMIT,
        start: typing.Optional[float] = OMIT,
        stop: typing.Optional[float] = OMIT,
        step: typing.Optional[float] = OMIT,
        debounce: typing.Optional[bool] = OMIT,
        full_width: typing.Optional[bool] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        initial_value : typing.Optional[float]

        label : typing.Optional[str]

        start : typing.Optional[float]

        stop : typing.Optional[float]

        step : typing.Optional[float]

        debounce : typing.Optional[bool]

        full_width : typing.Optional[bool]

        disabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-number/data",
            method="PUT",
            json={
                "initialValue": initial_value,
                "label": label,
                "start": start,
                "stop": stop,
                "step": step,
                "debounce": debounce,
                "fullWidth": full_width,
                "disabled": disabled,
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

    def read_marimo_outline_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoOutlineData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoOutlineData]
            marimo-outline data accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-outline/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoOutlineData,
                    parse_obj_as(
                        type_=MarimoOutlineData,
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

    def write_marimo_outline_data(
        self, *, label: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        label : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-outline/data",
            method="PUT",
            json={
                "label": label,
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

    def read_marimo_panel_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoPanelData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoPanelData]
            marimo-panel data accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-panel/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoPanelData,
                    parse_obj_as(
                        type_=MarimoPanelData,
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

    def write_marimo_panel_data(
        self,
        *,
        docs_json: typing.Dict[str, typing.Any],
        render_json: MarimoPanelDataRenderJson,
        extension_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        docs_json : typing.Dict[str, typing.Any]

        render_json : MarimoPanelDataRenderJson

        extension_url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-panel/data",
            method="PUT",
            json={
                "extensionUrl": extension_url,
                "docs_json": docs_json,
                "render_json": convert_and_respect_annotation_metadata(
                    object_=render_json, annotation=MarimoPanelDataRenderJson, direction="write"
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

    def read_marimo_plotly_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoPlotlyData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoPlotlyData]
            marimo-plotly data accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-plotly/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoPlotlyData,
                    parse_obj_as(
                        type_=MarimoPlotlyData,
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

    def write_marimo_plotly_data(
        self,
        *,
        figure: typing.Dict[str, typing.Any],
        config: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        figure : typing.Dict[str, typing.Any]

        config : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-plotly/data",
            method="PUT",
            json={
                "figure": figure,
                "config": config,
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

    def read_marimo_progress_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoProgressData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoProgressData]
            marimo-progress data accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-progress/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoProgressData,
                    parse_obj_as(
                        type_=MarimoProgressData,
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

    def write_marimo_progress_data(
        self,
        *,
        progress: MarimoProgressDataProgress,
        title: typing.Optional[str] = OMIT,
        subtitle: typing.Optional[str] = OMIT,
        total: typing.Optional[float] = OMIT,
        eta: typing.Optional[float] = OMIT,
        rate: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        progress : MarimoProgressDataProgress

        title : typing.Optional[str]

        subtitle : typing.Optional[str]

        total : typing.Optional[float]

        eta : typing.Optional[float]

        rate : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-progress/data",
            method="PUT",
            json={
                "title": title,
                "subtitle": subtitle,
                "progress": convert_and_respect_annotation_metadata(
                    object_=progress, annotation=MarimoProgressDataProgress, direction="write"
                ),
                "total": total,
                "eta": eta,
                "rate": rate,
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

    def read_marimo_radio_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoRadioData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoRadioData]
            marimo-radio data accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-radio/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoRadioData,
                    parse_obj_as(
                        type_=MarimoRadioData,
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

    def write_marimo_radio_data(
        self,
        *,
        options: typing.Sequence[str],
        initial_value: typing.Optional[str] = OMIT,
        inline: typing.Optional[bool] = OMIT,
        label: typing.Optional[str] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        options : typing.Sequence[str]

        initial_value : typing.Optional[str]

        inline : typing.Optional[bool]

        label : typing.Optional[str]

        disabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-radio/data",
            method="PUT",
            json={
                "initialValue": initial_value,
                "inline": inline,
                "label": label,
                "options": options,
                "disabled": disabled,
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

    def read_marimo_range_slider_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoRangeSliderData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoRangeSliderData]
            marimo-range-slider data accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-range-slider/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoRangeSliderData,
                    parse_obj_as(
                        type_=MarimoRangeSliderData,
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

    def write_marimo_range_slider_data(
        self,
        *,
        initial_value: typing.Sequence[float],
        start: float,
        stop: float,
        label: typing.Optional[str] = OMIT,
        step: typing.Optional[float] = OMIT,
        steps: typing.Optional[typing.Sequence[float]] = OMIT,
        debounce: typing.Optional[bool] = OMIT,
        orientation: typing.Optional[MarimoRangeSliderDataOrientation] = OMIT,
        show_value: typing.Optional[bool] = OMIT,
        full_width: typing.Optional[bool] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        initial_value : typing.Sequence[float]

        start : float

        stop : float

        label : typing.Optional[str]

        step : typing.Optional[float]

        steps : typing.Optional[typing.Sequence[float]]

        debounce : typing.Optional[bool]

        orientation : typing.Optional[MarimoRangeSliderDataOrientation]

        show_value : typing.Optional[bool]

        full_width : typing.Optional[bool]

        disabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-range-slider/data",
            method="PUT",
            json={
                "initialValue": initial_value,
                "label": label,
                "start": start,
                "stop": stop,
                "step": step,
                "steps": steps,
                "debounce": debounce,
                "orientation": orientation,
                "showValue": show_value,
                "fullWidth": full_width,
                "disabled": disabled,
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

    def read_marimo_refresh_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoRefreshData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoRefreshData]
            marimo-refresh data accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-refresh/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoRefreshData,
                    parse_obj_as(
                        type_=MarimoRefreshData,
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

    def write_marimo_refresh_data(
        self,
        *,
        options: typing.Optional[typing.Sequence[MarimoRefreshDataOptionsItem]] = OMIT,
        default_interval: typing.Optional[MarimoRefreshDataDefaultInterval] = OMIT,
        label: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        options : typing.Optional[typing.Sequence[MarimoRefreshDataOptionsItem]]

        default_interval : typing.Optional[MarimoRefreshDataDefaultInterval]

        label : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-refresh/data",
            method="PUT",
            json={
                "options": convert_and_respect_annotation_metadata(
                    object_=options, annotation=typing.Sequence[MarimoRefreshDataOptionsItem], direction="write"
                ),
                "defaultInterval": convert_and_respect_annotation_metadata(
                    object_=default_interval, annotation=MarimoRefreshDataDefaultInterval, direction="write"
                ),
                "label": label,
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

    def read_marimo_routes_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoRoutesData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoRoutesData]
            marimo-routes data accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-routes/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoRoutesData,
                    parse_obj_as(
                        type_=MarimoRoutesData,
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

    def write_marimo_routes_data(
        self, *, routes: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        routes : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-routes/data",
            method="PUT",
            json={
                "routes": routes,
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

    def read_marimo_slider_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoSliderData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoSliderData]
            marimo-slider data accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-slider/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoSliderData,
                    parse_obj_as(
                        type_=MarimoSliderData,
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

    def write_marimo_slider_data(
        self,
        *,
        initial_value: float,
        start: float,
        stop: float,
        label: typing.Optional[str] = OMIT,
        step: typing.Optional[float] = OMIT,
        steps: typing.Optional[typing.Sequence[float]] = OMIT,
        debounce: typing.Optional[bool] = OMIT,
        orientation: typing.Optional[MarimoSliderDataOrientation] = OMIT,
        show_value: typing.Optional[bool] = OMIT,
        full_width: typing.Optional[bool] = OMIT,
        include_input: typing.Optional[bool] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        initial_value : float

        start : float

        stop : float

        label : typing.Optional[str]

        step : typing.Optional[float]

        steps : typing.Optional[typing.Sequence[float]]

        debounce : typing.Optional[bool]

        orientation : typing.Optional[MarimoSliderDataOrientation]

        show_value : typing.Optional[bool]

        full_width : typing.Optional[bool]

        include_input : typing.Optional[bool]

        disabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-slider/data",
            method="PUT",
            json={
                "initialValue": initial_value,
                "label": label,
                "start": start,
                "stop": stop,
                "step": step,
                "steps": steps,
                "debounce": debounce,
                "orientation": orientation,
                "showValue": show_value,
                "fullWidth": full_width,
                "includeInput": include_input,
                "disabled": disabled,
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

    def read_marimo_stat_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoStatData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoStatData]
            marimo-stat data accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-stat/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoStatData,
                    parse_obj_as(
                        type_=MarimoStatData,
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

    def write_marimo_stat_data(
        self,
        *,
        value: typing.Optional[MarimoStatDataValue] = OMIT,
        label: typing.Optional[str] = OMIT,
        caption: typing.Optional[str] = OMIT,
        bordered: typing.Optional[bool] = OMIT,
        direction: typing.Optional[MarimoStatDataDirection] = OMIT,
        target_direction: typing.Optional[MarimoStatDataTargetDirection] = OMIT,
        slot: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        value : typing.Optional[MarimoStatDataValue]

        label : typing.Optional[str]

        caption : typing.Optional[str]

        bordered : typing.Optional[bool]

        direction : typing.Optional[MarimoStatDataDirection]

        target_direction : typing.Optional[MarimoStatDataTargetDirection]

        slot : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-stat/data",
            method="PUT",
            json={
                "value": convert_and_respect_annotation_metadata(
                    object_=value, annotation=MarimoStatDataValue, direction="write"
                ),
                "label": label,
                "caption": caption,
                "bordered": bordered,
                "direction": direction,
                "target_direction": target_direction,
                "slot": slot,
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

    def read_marimo_switch_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoSwitchData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoSwitchData]
            marimo-switch data accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-switch/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoSwitchData,
                    parse_obj_as(
                        type_=MarimoSwitchData,
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

    def write_marimo_switch_data(
        self,
        *,
        initial_value: bool,
        label: typing.Optional[str] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        initial_value : bool

        label : typing.Optional[str]

        disabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-switch/data",
            method="PUT",
            json={
                "initialValue": initial_value,
                "label": label,
                "disabled": disabled,
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

    def read_marimo_table_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoTableData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoTableData]
            marimo-table data accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoTableData,
                    parse_obj_as(
                        type_=MarimoTableData,
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

    def write_marimo_table_data(
        self,
        *,
        initial_value: MarimoTableDataInitialValue,
        data: MarimoTableDataData,
        total_rows: MarimoTableDataTotalRows,
        row_headers: typing.Sequence[typing.Sequence[typing.Any]],
        total_columns: float,
        label: typing.Optional[str] = OMIT,
        raw_data: typing.Optional[MarimoTableDataRawData] = OMIT,
        pagination: typing.Optional[bool] = OMIT,
        page_size: typing.Optional[float] = OMIT,
        selection: typing.Optional[MarimoTableDataSelection] = OMIT,
        show_download: typing.Optional[bool] = OMIT,
        show_filters: typing.Optional[bool] = OMIT,
        show_column_summaries: typing.Optional[MarimoTableDataShowColumnSummaries] = OMIT,
        show_data_types: typing.Optional[bool] = OMIT,
        show_page_size_selector: typing.Optional[bool] = OMIT,
        show_column_explorer: typing.Optional[bool] = OMIT,
        show_row_explorer: typing.Optional[bool] = OMIT,
        show_chart_builder: typing.Optional[bool] = OMIT,
        show_search: typing.Optional[bool] = OMIT,
        freeze_columns_left: typing.Optional[typing.Sequence[str]] = OMIT,
        freeze_columns_right: typing.Optional[typing.Sequence[str]] = OMIT,
        hidden_columns: typing.Optional[typing.Sequence[str]] = OMIT,
        text_justify_columns: typing.Optional[typing.Dict[str, MarimoTableDataTextJustifyColumnsValue]] = OMIT,
        wrapped_columns: typing.Optional[typing.Sequence[str]] = OMIT,
        column_widths: typing.Optional[typing.Dict[str, int]] = OMIT,
        header_tooltip: typing.Optional[typing.Dict[str, str]] = OMIT,
        field_types: typing.Optional[typing.Sequence[typing.Sequence[typing.Any]]] = OMIT,
        max_columns: typing.Optional[MarimoTableDataMaxColumns] = OMIT,
        has_stable_row_id: typing.Optional[bool] = OMIT,
        max_height: typing.Optional[float] = OMIT,
        cell_styles: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Dict[str, typing.Any]]]] = OMIT,
        hover_template: typing.Optional[str] = OMIT,
        cell_hover_texts: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Optional[str]]]] = OMIT,
        lazy: typing.Optional[bool] = OMIT,
        preload: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        initial_value : MarimoTableDataInitialValue

        data : MarimoTableDataData

        total_rows : MarimoTableDataTotalRows

        row_headers : typing.Sequence[typing.Sequence[typing.Any]]

        total_columns : float

        label : typing.Optional[str]

        raw_data : typing.Optional[MarimoTableDataRawData]

        pagination : typing.Optional[bool]

        page_size : typing.Optional[float]

        selection : typing.Optional[MarimoTableDataSelection]

        show_download : typing.Optional[bool]

        show_filters : typing.Optional[bool]

        show_column_summaries : typing.Optional[MarimoTableDataShowColumnSummaries]

        show_data_types : typing.Optional[bool]

        show_page_size_selector : typing.Optional[bool]

        show_column_explorer : typing.Optional[bool]

        show_row_explorer : typing.Optional[bool]

        show_chart_builder : typing.Optional[bool]

        show_search : typing.Optional[bool]

        freeze_columns_left : typing.Optional[typing.Sequence[str]]

        freeze_columns_right : typing.Optional[typing.Sequence[str]]

        hidden_columns : typing.Optional[typing.Sequence[str]]

        text_justify_columns : typing.Optional[typing.Dict[str, MarimoTableDataTextJustifyColumnsValue]]

        wrapped_columns : typing.Optional[typing.Sequence[str]]

        column_widths : typing.Optional[typing.Dict[str, int]]

        header_tooltip : typing.Optional[typing.Dict[str, str]]

        field_types : typing.Optional[typing.Sequence[typing.Sequence[typing.Any]]]

        max_columns : typing.Optional[MarimoTableDataMaxColumns]

        has_stable_row_id : typing.Optional[bool]

        max_height : typing.Optional[float]

        cell_styles : typing.Optional[typing.Dict[str, typing.Dict[str, typing.Dict[str, typing.Any]]]]

        hover_template : typing.Optional[str]

        cell_hover_texts : typing.Optional[typing.Dict[str, typing.Dict[str, typing.Optional[str]]]]

        lazy : typing.Optional[bool]

        preload : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/data",
            method="PUT",
            json={
                "initialValue": convert_and_respect_annotation_metadata(
                    object_=initial_value, annotation=MarimoTableDataInitialValue, direction="write"
                ),
                "label": label,
                "data": convert_and_respect_annotation_metadata(
                    object_=data, annotation=MarimoTableDataData, direction="write"
                ),
                "rawData": convert_and_respect_annotation_metadata(
                    object_=raw_data, annotation=typing.Optional[MarimoTableDataRawData], direction="write"
                ),
                "totalRows": convert_and_respect_annotation_metadata(
                    object_=total_rows, annotation=MarimoTableDataTotalRows, direction="write"
                ),
                "pagination": pagination,
                "pageSize": page_size,
                "selection": selection,
                "showDownload": show_download,
                "showFilters": show_filters,
                "showColumnSummaries": convert_and_respect_annotation_metadata(
                    object_=show_column_summaries, annotation=MarimoTableDataShowColumnSummaries, direction="write"
                ),
                "showDataTypes": show_data_types,
                "showPageSizeSelector": show_page_size_selector,
                "showColumnExplorer": show_column_explorer,
                "showRowExplorer": show_row_explorer,
                "showChartBuilder": show_chart_builder,
                "showSearch": show_search,
                "rowHeaders": row_headers,
                "freezeColumnsLeft": freeze_columns_left,
                "freezeColumnsRight": freeze_columns_right,
                "hiddenColumns": hidden_columns,
                "textJustifyColumns": text_justify_columns,
                "wrappedColumns": wrapped_columns,
                "columnWidths": column_widths,
                "headerTooltip": header_tooltip,
                "fieldTypes": field_types,
                "totalColumns": total_columns,
                "maxColumns": convert_and_respect_annotation_metadata(
                    object_=max_columns, annotation=MarimoTableDataMaxColumns, direction="write"
                ),
                "hasStableRowId": has_stable_row_id,
                "maxHeight": max_height,
                "cellStyles": cell_styles,
                "hoverTemplate": hover_template,
                "cellHoverTexts": cell_hover_texts,
                "lazy": lazy,
                "preload": preload,
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

    def read_marimo_tabs_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoTabsData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoTabsData]
            marimo-tabs data accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-tabs/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoTabsData,
                    parse_obj_as(
                        type_=MarimoTabsData,
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

    def write_marimo_tabs_data(
        self,
        *,
        tabs: typing.Sequence[str],
        label: typing.Optional[str] = OMIT,
        orientation: typing.Optional[MarimoTabsDataOrientation] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        tabs : typing.Sequence[str]

        label : typing.Optional[str]

        orientation : typing.Optional[MarimoTabsDataOrientation]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-tabs/data",
            method="PUT",
            json={
                "tabs": tabs,
                "label": label,
                "orientation": orientation,
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

    def read_marimo_tex_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoTexData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoTexData]
            marimo-tex data accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-tex/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoTexData,
                    parse_obj_as(
                        type_=MarimoTexData,
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

    def write_marimo_tex_data(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
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
            "plugins/marimo-tex/data",
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

    def read_marimo_text_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoTextData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoTextData]
            marimo-text data accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-text/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoTextData,
                    parse_obj_as(
                        type_=MarimoTextData,
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

    def write_marimo_text_data(
        self,
        *,
        initial_value: str,
        placeholder: str,
        label: typing.Optional[str] = OMIT,
        kind: typing.Optional[MarimoTextDataKind] = OMIT,
        max_length: typing.Optional[float] = OMIT,
        min_length: typing.Optional[float] = OMIT,
        full_width: typing.Optional[bool] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        debounce: typing.Optional[MarimoTextDataDebounce] = OMIT,
        password_has_value: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        initial_value : str

        placeholder : str

        label : typing.Optional[str]

        kind : typing.Optional[MarimoTextDataKind]

        max_length : typing.Optional[float]

        min_length : typing.Optional[float]

        full_width : typing.Optional[bool]

        disabled : typing.Optional[bool]

        debounce : typing.Optional[MarimoTextDataDebounce]

        password_has_value : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-text/data",
            method="PUT",
            json={
                "initialValue": initial_value,
                "placeholder": placeholder,
                "label": label,
                "kind": kind,
                "maxLength": max_length,
                "minLength": min_length,
                "fullWidth": full_width,
                "disabled": disabled,
                "debounce": convert_and_respect_annotation_metadata(
                    object_=debounce, annotation=MarimoTextDataDebounce, direction="write"
                ),
                "passwordHasValue": password_has_value,
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

    def read_marimo_text_area_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoTextAreaData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoTextAreaData]
            marimo-text-area data accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-text-area/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoTextAreaData,
                    parse_obj_as(
                        type_=MarimoTextAreaData,
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

    def write_marimo_text_area_data(
        self,
        *,
        initial_value: str,
        placeholder: str,
        label: typing.Optional[str] = OMIT,
        max_length: typing.Optional[float] = OMIT,
        min_length: typing.Optional[float] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        debounce: typing.Optional[MarimoTextAreaDataDebounce] = OMIT,
        rows: typing.Optional[float] = OMIT,
        full_width: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        initial_value : str

        placeholder : str

        label : typing.Optional[str]

        max_length : typing.Optional[float]

        min_length : typing.Optional[float]

        disabled : typing.Optional[bool]

        debounce : typing.Optional[MarimoTextAreaDataDebounce]

        rows : typing.Optional[float]

        full_width : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-text-area/data",
            method="PUT",
            json={
                "initialValue": initial_value,
                "placeholder": placeholder,
                "label": label,
                "maxLength": max_length,
                "minLength": min_length,
                "disabled": disabled,
                "debounce": convert_and_respect_annotation_metadata(
                    object_=debounce, annotation=MarimoTextAreaDataDebounce, direction="write"
                ),
                "rows": rows,
                "fullWidth": full_width,
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

    def read_marimo_vega_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarimoVegaData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarimoVegaData]
            marimo-vega data accepted by a plugin consumer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-vega/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoVegaData,
                    parse_obj_as(
                        type_=MarimoVegaData,
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

    def write_marimo_vega_data(
        self,
        *,
        spec: typing.Dict[str, typing.Any],
        chart_selection: typing.Optional[MarimoVegaDataChartSelection] = OMIT,
        field_selection: typing.Optional[MarimoVegaDataFieldSelection] = OMIT,
        embed_options: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        spec : typing.Dict[str, typing.Any]

        chart_selection : typing.Optional[MarimoVegaDataChartSelection]

        field_selection : typing.Optional[MarimoVegaDataFieldSelection]

        embed_options : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugins/marimo-vega/data",
            method="PUT",
            json={
                "spec": spec,
                "chartSelection": convert_and_respect_annotation_metadata(
                    object_=chart_selection, annotation=MarimoVegaDataChartSelection, direction="write"
                ),
                "fieldSelection": convert_and_respect_annotation_metadata(
                    object_=field_selection, annotation=MarimoVegaDataFieldSelection, direction="write"
                ),
                "embedOptions": embed_options,
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


class AsyncRawPluginDataClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def read_marimo_accordion_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoAccordionData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoAccordionData]
            marimo-accordion data accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-accordion/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoAccordionData,
                    parse_obj_as(
                        type_=MarimoAccordionData,
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

    async def write_marimo_accordion_data(
        self,
        *,
        labels: typing.Sequence[str],
        multiple: bool,
        expanded: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        labels : typing.Sequence[str]

        multiple : bool

        expanded : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-accordion/data",
            method="PUT",
            json={
                "labels": labels,
                "multiple": multiple,
                "expanded": expanded,
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

    async def read_marimo_anywidget_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoAnywidgetData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoAnywidgetData]
            marimo-anywidget data accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-anywidget/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoAnywidgetData,
                    parse_obj_as(
                        type_=MarimoAnywidgetData,
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

    async def write_marimo_anywidget_data(
        self, *, model_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        model_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-anywidget/data",
            method="PUT",
            json={
                "modelId": model_id,
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

    async def read_marimo_button_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoButtonData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoButtonData]
            marimo-button data accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-button/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoButtonData,
                    parse_obj_as(
                        type_=MarimoButtonData,
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

    async def write_marimo_button_data(
        self,
        *,
        label: str,
        kind: typing.Optional[MarimoButtonDataKind] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        full_width: typing.Optional[bool] = OMIT,
        tooltip: typing.Optional[str] = OMIT,
        keyboard_shortcut: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        label : str

        kind : typing.Optional[MarimoButtonDataKind]

        disabled : typing.Optional[bool]

        full_width : typing.Optional[bool]

        tooltip : typing.Optional[str]

        keyboard_shortcut : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-button/data",
            method="PUT",
            json={
                "label": label,
                "kind": kind,
                "disabled": disabled,
                "fullWidth": full_width,
                "tooltip": tooltip,
                "keyboardShortcut": keyboard_shortcut,
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

    async def read_marimo_callout_output_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoCalloutOutputData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoCalloutOutputData]
            marimo-callout-output data accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-callout-output/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoCalloutOutputData,
                    parse_obj_as(
                        type_=MarimoCalloutOutputData,
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

    async def write_marimo_callout_output_data(
        self,
        *,
        html: str,
        kind: typing.Optional[MarimoCalloutOutputDataKind] = OMIT,
        title: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        html : str

        kind : typing.Optional[MarimoCalloutOutputDataKind]

        title : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-callout-output/data",
            method="PUT",
            json={
                "html": html,
                "kind": kind,
                "title": title,
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

    async def read_marimo_carousel_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoCarouselData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoCarouselData]
            marimo-carousel data accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-carousel/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoCarouselData,
                    parse_obj_as(
                        type_=MarimoCarouselData,
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

    async def write_marimo_carousel_data(
        self,
        *,
        index: typing.Optional[str] = OMIT,
        height: typing.Optional[MarimoCarouselDataHeight] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        index : typing.Optional[str]

        height : typing.Optional[MarimoCarouselDataHeight]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-carousel/data",
            method="PUT",
            json={
                "index": index,
                "height": convert_and_respect_annotation_metadata(
                    object_=height, annotation=typing.Optional[MarimoCarouselDataHeight], direction="write"
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

    async def read_marimo_chatbot_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoChatbotData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoChatbotData]
            marimo-chatbot data accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-chatbot/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoChatbotData,
                    parse_obj_as(
                        type_=MarimoChatbotData,
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

    async def write_marimo_chatbot_data(
        self,
        *,
        show_configuration_controls: bool,
        config: MarimoChatbotDataConfig,
        allow_attachments: MarimoChatbotDataAllowAttachments,
        prompts: typing.Optional[typing.Sequence[str]] = OMIT,
        max_height: typing.Optional[float] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        show_configuration_controls : bool

        config : MarimoChatbotDataConfig

        allow_attachments : MarimoChatbotDataAllowAttachments

        prompts : typing.Optional[typing.Sequence[str]]

        max_height : typing.Optional[float]

        disabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-chatbot/data",
            method="PUT",
            json={
                "prompts": prompts,
                "showConfigurationControls": show_configuration_controls,
                "maxHeight": max_height,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=MarimoChatbotDataConfig, direction="write"
                ),
                "allowAttachments": convert_and_respect_annotation_metadata(
                    object_=allow_attachments, annotation=MarimoChatbotDataAllowAttachments, direction="write"
                ),
                "disabled": disabled,
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

    async def read_marimo_checkbox_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoCheckboxData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoCheckboxData]
            marimo-checkbox data accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-checkbox/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoCheckboxData,
                    parse_obj_as(
                        type_=MarimoCheckboxData,
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

    async def write_marimo_checkbox_data(
        self,
        *,
        initial_value: bool,
        label: typing.Optional[str] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        initial_value : bool

        label : typing.Optional[str]

        disabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-checkbox/data",
            method="PUT",
            json={
                "initialValue": initial_value,
                "label": label,
                "disabled": disabled,
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

    async def read_marimo_code_editor_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoCodeEditorData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoCodeEditorData]
            marimo-code-editor data accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-code-editor/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoCodeEditorData,
                    parse_obj_as(
                        type_=MarimoCodeEditorData,
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

    async def write_marimo_code_editor_data(
        self,
        *,
        initial_value: str,
        placeholder: str,
        language: typing.Optional[str] = OMIT,
        theme: typing.Optional[MarimoCodeEditorDataTheme] = OMIT,
        label: typing.Optional[str] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        min_height: typing.Optional[float] = OMIT,
        max_height: typing.Optional[float] = OMIT,
        show_copy_button: typing.Optional[bool] = OMIT,
        debounce: typing.Optional[MarimoCodeEditorDataDebounce] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        initial_value : str

        placeholder : str

        language : typing.Optional[str]

        theme : typing.Optional[MarimoCodeEditorDataTheme]

        label : typing.Optional[str]

        disabled : typing.Optional[bool]

        min_height : typing.Optional[float]

        max_height : typing.Optional[float]

        show_copy_button : typing.Optional[bool]

        debounce : typing.Optional[MarimoCodeEditorDataDebounce]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-code-editor/data",
            method="PUT",
            json={
                "initialValue": initial_value,
                "language": language,
                "placeholder": placeholder,
                "theme": theme,
                "label": label,
                "disabled": disabled,
                "minHeight": min_height,
                "maxHeight": max_height,
                "showCopyButton": show_copy_button,
                "debounce": convert_and_respect_annotation_metadata(
                    object_=debounce, annotation=MarimoCodeEditorDataDebounce, direction="write"
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

    async def read_marimo_data_editor_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoDataEditorData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoDataEditorData]
            marimo-data-editor data accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-data-editor/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoDataEditorData,
                    parse_obj_as(
                        type_=MarimoDataEditorData,
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

    async def write_marimo_data_editor_data(
        self,
        *,
        initial_value: MarimoDataEditorDataInitialValue,
        data: MarimoDataEditorDataData,
        editable_columns: MarimoDataEditorDataEditableColumns,
        label: typing.Optional[str] = OMIT,
        field_types: typing.Optional[typing.Sequence[typing.Sequence[typing.Any]]] = OMIT,
        column_names: typing.Optional[typing.Sequence[str]] = OMIT,
        column_sizing_mode: typing.Optional[MarimoDataEditorDataColumnSizingMode] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        initial_value : MarimoDataEditorDataInitialValue

        data : MarimoDataEditorDataData

        editable_columns : MarimoDataEditorDataEditableColumns

        label : typing.Optional[str]

        field_types : typing.Optional[typing.Sequence[typing.Sequence[typing.Any]]]

        column_names : typing.Optional[typing.Sequence[str]]

        column_sizing_mode : typing.Optional[MarimoDataEditorDataColumnSizingMode]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-data-editor/data",
            method="PUT",
            json={
                "initialValue": convert_and_respect_annotation_metadata(
                    object_=initial_value, annotation=MarimoDataEditorDataInitialValue, direction="write"
                ),
                "label": label,
                "data": convert_and_respect_annotation_metadata(
                    object_=data, annotation=MarimoDataEditorDataData, direction="write"
                ),
                "fieldTypes": field_types,
                "columnNames": column_names,
                "editableColumns": convert_and_respect_annotation_metadata(
                    object_=editable_columns, annotation=MarimoDataEditorDataEditableColumns, direction="write"
                ),
                "columnSizingMode": column_sizing_mode,
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

    async def read_marimo_data_explorer_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoDataExplorerData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoDataExplorerData]
            marimo-data-explorer data accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-data-explorer/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoDataExplorerData,
                    parse_obj_as(
                        type_=MarimoDataExplorerData,
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

    async def write_marimo_data_explorer_data(
        self, *, data: str, label: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        data : str

        label : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-data-explorer/data",
            method="PUT",
            json={
                "label": label,
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

    async def read_marimo_dataframe_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoDataframeData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoDataframeData]
            marimo-dataframe data accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-dataframe/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoDataframeData,
                    parse_obj_as(
                        type_=MarimoDataframeData,
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

    async def write_marimo_dataframe_data(
        self,
        *,
        columns: typing.Sequence[typing.Sequence[typing.Any]],
        label: typing.Optional[str] = OMIT,
        page_size: typing.Optional[float] = OMIT,
        show_download: typing.Optional[bool] = OMIT,
        dataframe_name: typing.Optional[str] = OMIT,
        lazy: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        columns : typing.Sequence[typing.Sequence[typing.Any]]

        label : typing.Optional[str]

        page_size : typing.Optional[float]

        show_download : typing.Optional[bool]

        dataframe_name : typing.Optional[str]

        lazy : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-dataframe/data",
            method="PUT",
            json={
                "label": label,
                "pageSize": page_size,
                "showDownload": show_download,
                "dataframeName": dataframe_name,
                "columns": columns,
                "lazy": lazy,
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

    async def read_marimo_date_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoDateData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoDateData]
            marimo-date data accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-date/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoDateData,
                    parse_obj_as(
                        type_=MarimoDateData,
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

    async def write_marimo_date_data(
        self,
        *,
        initial_value: str,
        start: str,
        stop: str,
        label: typing.Optional[str] = OMIT,
        step: typing.Optional[str] = OMIT,
        full_width: typing.Optional[bool] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        initial_value : str

        start : str

        stop : str

        label : typing.Optional[str]

        step : typing.Optional[str]

        full_width : typing.Optional[bool]

        disabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-date/data",
            method="PUT",
            json={
                "initialValue": initial_value,
                "label": label,
                "start": start,
                "stop": stop,
                "step": step,
                "fullWidth": full_width,
                "disabled": disabled,
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

    async def read_marimo_date_range_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoDateRangeData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoDateRangeData]
            marimo-date-range data accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-date-range/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoDateRangeData,
                    parse_obj_as(
                        type_=MarimoDateRangeData,
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

    async def write_marimo_date_range_data(
        self,
        *,
        initial_value: typing.Sequence[typing.Any],
        start: str,
        stop: str,
        label: typing.Optional[str] = OMIT,
        step: typing.Optional[str] = OMIT,
        full_width: typing.Optional[bool] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        initial_value : typing.Sequence[typing.Any]

        start : str

        stop : str

        label : typing.Optional[str]

        step : typing.Optional[str]

        full_width : typing.Optional[bool]

        disabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-date-range/data",
            method="PUT",
            json={
                "initialValue": initial_value,
                "label": label,
                "start": start,
                "stop": stop,
                "step": step,
                "fullWidth": full_width,
                "disabled": disabled,
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

    async def read_marimo_datetime_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoDatetimeData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoDatetimeData]
            marimo-datetime data accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-datetime/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoDatetimeData,
                    parse_obj_as(
                        type_=MarimoDatetimeData,
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

    async def write_marimo_datetime_data(
        self,
        *,
        initial_value: str,
        start: str,
        stop: str,
        label: typing.Optional[str] = OMIT,
        step: typing.Optional[str] = OMIT,
        precision: typing.Optional[MarimoDatetimeDataPrecision] = OMIT,
        full_width: typing.Optional[bool] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        initial_value : str

        start : str

        stop : str

        label : typing.Optional[str]

        step : typing.Optional[str]

        precision : typing.Optional[MarimoDatetimeDataPrecision]

        full_width : typing.Optional[bool]

        disabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-datetime/data",
            method="PUT",
            json={
                "initialValue": initial_value,
                "label": label,
                "start": start,
                "stop": stop,
                "step": step,
                "precision": precision,
                "fullWidth": full_width,
                "disabled": disabled,
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

    async def read_marimo_dict_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoDictData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoDictData]
            marimo-dict data accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-dict/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoDictData,
                    parse_obj_as(
                        type_=MarimoDictData,
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

    async def write_marimo_dict_data(
        self,
        *,
        element_ids: typing.Dict[str, str],
        label: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        element_ids : typing.Dict[str, str]

        label : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-dict/data",
            method="PUT",
            json={
                "label": label,
                "elementIds": element_ids,
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

    async def read_marimo_download_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoDownloadData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoDownloadData]
            marimo-download data accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-download/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoDownloadData,
                    parse_obj_as(
                        type_=MarimoDownloadData,
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

    async def write_marimo_download_data(
        self,
        *,
        data: str,
        disabled: typing.Optional[bool] = OMIT,
        filename: typing.Optional[str] = OMIT,
        label: typing.Optional[str] = OMIT,
        lazy: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        data : str

        disabled : typing.Optional[bool]

        filename : typing.Optional[str]

        label : typing.Optional[str]

        lazy : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-download/data",
            method="PUT",
            json={
                "data": data,
                "disabled": disabled,
                "filename": filename,
                "label": label,
                "lazy": lazy,
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

    async def read_marimo_dropdown_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoDropdownData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoDropdownData]
            marimo-dropdown data accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-dropdown/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoDropdownData,
                    parse_obj_as(
                        type_=MarimoDropdownData,
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

    async def write_marimo_dropdown_data(
        self,
        *,
        initial_value: typing.Sequence[str],
        options: typing.Sequence[str],
        allow_select_none: bool,
        label: typing.Optional[str] = OMIT,
        full_width: typing.Optional[bool] = OMIT,
        searchable: typing.Optional[bool] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        initial_value : typing.Sequence[str]

        options : typing.Sequence[str]

        allow_select_none : bool

        label : typing.Optional[str]

        full_width : typing.Optional[bool]

        searchable : typing.Optional[bool]

        disabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-dropdown/data",
            method="PUT",
            json={
                "initialValue": initial_value,
                "label": label,
                "options": options,
                "allowSelectNone": allow_select_none,
                "fullWidth": full_width,
                "searchable": searchable,
                "disabled": disabled,
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

    async def read_marimo_file_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoFileData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoFileData]
            marimo-file data accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-file/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoFileData,
                    parse_obj_as(
                        type_=MarimoFileData,
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

    async def write_marimo_file_data(
        self,
        *,
        filetypes: typing.Sequence[str],
        multiple: bool,
        kind: MarimoFileDataKind,
        max_size: float,
        label: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        filetypes : typing.Sequence[str]

        multiple : bool

        kind : MarimoFileDataKind

        max_size : float

        label : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-file/data",
            method="PUT",
            json={
                "filetypes": filetypes,
                "multiple": multiple,
                "kind": kind,
                "label": label,
                "max_size": max_size,
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

    async def read_marimo_file_browser_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoFileBrowserData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoFileBrowserData]
            marimo-file-browser data accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-file-browser/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoFileBrowserData,
                    parse_obj_as(
                        type_=MarimoFileBrowserData,
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

    async def write_marimo_file_browser_data(
        self,
        *,
        initial_path: str,
        filetypes: typing.Sequence[str],
        selection_mode: str,
        multiple: bool,
        restrict_navigation: bool,
        label: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        initial_path : str

        filetypes : typing.Sequence[str]

        selection_mode : str

        multiple : bool

        restrict_navigation : bool

        label : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-file-browser/data",
            method="PUT",
            json={
                "initialPath": initial_path,
                "filetypes": filetypes,
                "selectionMode": selection_mode,
                "multiple": multiple,
                "label": label,
                "restrictNavigation": restrict_navigation,
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

    async def read_marimo_form_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoFormData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoFormData]
            marimo-form data accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-form/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoFormData,
                    parse_obj_as(
                        type_=MarimoFormData,
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

    async def write_marimo_form_data(
        self,
        *,
        element_id: str,
        label: typing.Optional[str] = OMIT,
        bordered: typing.Optional[bool] = OMIT,
        loading: typing.Optional[bool] = OMIT,
        submit_button_label: typing.Optional[str] = OMIT,
        submit_button_tooltip: typing.Optional[str] = OMIT,
        submit_button_disabled: typing.Optional[bool] = OMIT,
        clear_on_submit: typing.Optional[bool] = OMIT,
        show_clear_button: typing.Optional[bool] = OMIT,
        clear_button_label: typing.Optional[str] = OMIT,
        clear_button_tooltip: typing.Optional[str] = OMIT,
        should_validate: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        element_id : str

        label : typing.Optional[str]

        bordered : typing.Optional[bool]

        loading : typing.Optional[bool]

        submit_button_label : typing.Optional[str]

        submit_button_tooltip : typing.Optional[str]

        submit_button_disabled : typing.Optional[bool]

        clear_on_submit : typing.Optional[bool]

        show_clear_button : typing.Optional[bool]

        clear_button_label : typing.Optional[str]

        clear_button_tooltip : typing.Optional[str]

        should_validate : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-form/data",
            method="PUT",
            json={
                "label": label,
                "elementId": element_id,
                "bordered": bordered,
                "loading": loading,
                "submitButtonLabel": submit_button_label,
                "submitButtonTooltip": submit_button_tooltip,
                "submitButtonDisabled": submit_button_disabled,
                "clearOnSubmit": clear_on_submit,
                "showClearButton": show_clear_button,
                "clearButtonLabel": clear_button_label,
                "clearButtonTooltip": clear_button_tooltip,
                "shouldValidate": should_validate,
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

    async def read_marimo_image_comparison_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoImageComparisonData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoImageComparisonData]
            marimo-image-comparison data accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-image-comparison/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoImageComparisonData,
                    parse_obj_as(
                        type_=MarimoImageComparisonData,
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

    async def write_marimo_image_comparison_data(
        self,
        *,
        before_src: str,
        after_src: str,
        value: typing.Optional[float] = OMIT,
        direction: typing.Optional[MarimoImageComparisonDataDirection] = OMIT,
        width: typing.Optional[str] = OMIT,
        height: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        before_src : str

        after_src : str

        value : typing.Optional[float]

        direction : typing.Optional[MarimoImageComparisonDataDirection]

        width : typing.Optional[str]

        height : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-image-comparison/data",
            method="PUT",
            json={
                "beforeSrc": before_src,
                "afterSrc": after_src,
                "value": value,
                "direction": direction,
                "width": width,
                "height": height,
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

    async def read_marimo_json_output_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoJsonOutputData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoJsonOutputData]
            marimo-json-output data accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-json-output/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoJsonOutputData,
                    parse_obj_as(
                        type_=MarimoJsonOutputData,
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

    async def write_marimo_json_output_data(
        self,
        *,
        json_data: typing.Any,
        name: typing.Optional[str] = OMIT,
        value_types: typing.Optional[MarimoJsonOutputDataValueTypes] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        json_data : typing.Any

        name : typing.Optional[str]

        value_types : typing.Optional[MarimoJsonOutputDataValueTypes]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-json-output/data",
            method="PUT",
            json={
                "name": name,
                "jsonData": json_data,
                "valueTypes": value_types,
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

    async def read_marimo_lazy_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoLazyData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoLazyData]
            marimo-lazy data accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-lazy/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoLazyData,
                    parse_obj_as(
                        type_=MarimoLazyData,
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

    async def write_marimo_lazy_data(
        self,
        *,
        show_loading_indicator: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        show_loading_indicator : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-lazy/data",
            method="PUT",
            json={
                "showLoadingIndicator": show_loading_indicator,
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

    async def read_marimo_matplotlib_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoMatplotlibData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoMatplotlibData]
            marimo-matplotlib data accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-matplotlib/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoMatplotlibData,
                    parse_obj_as(
                        type_=MarimoMatplotlibData,
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

    async def write_marimo_matplotlib_data(
        self,
        *,
        chart_base64: str,
        x_bounds: typing.Sequence[typing.Any],
        y_bounds: typing.Sequence[typing.Any],
        axes_pixel_bounds: typing.Sequence[typing.Any],
        width: float,
        height: float,
        debounce: bool,
        selection_color: typing.Optional[str] = OMIT,
        selection_opacity: typing.Optional[float] = OMIT,
        stroke_width: typing.Optional[float] = OMIT,
        x_scale: typing.Optional[MarimoMatplotlibDataXScale] = OMIT,
        y_scale: typing.Optional[MarimoMatplotlibDataYScale] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        chart_base64 : str

        x_bounds : typing.Sequence[typing.Any]

        y_bounds : typing.Sequence[typing.Any]

        axes_pixel_bounds : typing.Sequence[typing.Any]

        width : float

        height : float

        debounce : bool

        selection_color : typing.Optional[str]

        selection_opacity : typing.Optional[float]

        stroke_width : typing.Optional[float]

        x_scale : typing.Optional[MarimoMatplotlibDataXScale]

        y_scale : typing.Optional[MarimoMatplotlibDataYScale]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-matplotlib/data",
            method="PUT",
            json={
                "chartBase64": chart_base64,
                "xBounds": x_bounds,
                "yBounds": y_bounds,
                "axesPixelBounds": axes_pixel_bounds,
                "width": width,
                "height": height,
                "selectionColor": selection_color,
                "selectionOpacity": selection_opacity,
                "strokeWidth": stroke_width,
                "debounce": debounce,
                "xScale": x_scale,
                "yScale": y_scale,
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

    async def read_marimo_matrix_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoMatrixData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoMatrixData]
            marimo-matrix data accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-matrix/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoMatrixData,
                    parse_obj_as(
                        type_=MarimoMatrixData,
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

    async def write_marimo_matrix_data(
        self,
        *,
        initial_value: typing.Sequence[typing.Sequence[float]],
        step: typing.Sequence[typing.Sequence[float]],
        precision: float,
        symmetric: bool,
        scientific: bool,
        disabled: typing.Sequence[typing.Sequence[bool]],
        label: typing.Optional[str] = OMIT,
        min_value: typing.Optional[typing.Sequence[typing.Sequence[float]]] = OMIT,
        max_value: typing.Optional[typing.Sequence[typing.Sequence[float]]] = OMIT,
        row_labels: typing.Optional[typing.Sequence[str]] = OMIT,
        column_labels: typing.Optional[typing.Sequence[str]] = OMIT,
        debounce: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        initial_value : typing.Sequence[typing.Sequence[float]]

        step : typing.Sequence[typing.Sequence[float]]

        precision : float

        symmetric : bool

        scientific : bool

        disabled : typing.Sequence[typing.Sequence[bool]]

        label : typing.Optional[str]

        min_value : typing.Optional[typing.Sequence[typing.Sequence[float]]]

        max_value : typing.Optional[typing.Sequence[typing.Sequence[float]]]

        row_labels : typing.Optional[typing.Sequence[str]]

        column_labels : typing.Optional[typing.Sequence[str]]

        debounce : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-matrix/data",
            method="PUT",
            json={
                "initialValue": initial_value,
                "label": label,
                "minValue": min_value,
                "maxValue": max_value,
                "step": step,
                "precision": precision,
                "rowLabels": row_labels,
                "columnLabels": column_labels,
                "symmetric": symmetric,
                "debounce": debounce,
                "scientific": scientific,
                "disabled": disabled,
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

    async def read_marimo_mermaid_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoMermaidData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoMermaidData]
            marimo-mermaid data accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-mermaid/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoMermaidData,
                    parse_obj_as(
                        type_=MarimoMermaidData,
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

    async def write_marimo_mermaid_data(
        self,
        *,
        diagram: str,
        theme: typing.Optional[str] = OMIT,
        theme_variables: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        diagram : str

        theme : typing.Optional[str]

        theme_variables : typing.Optional[typing.Dict[str, str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-mermaid/data",
            method="PUT",
            json={
                "diagram": diagram,
                "theme": theme,
                "theme_variables": theme_variables,
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

    async def read_marimo_microphone_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoMicrophoneData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoMicrophoneData]
            marimo-microphone data accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-microphone/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoMicrophoneData,
                    parse_obj_as(
                        type_=MarimoMicrophoneData,
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

    async def write_marimo_microphone_data(
        self, *, label: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        label : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-microphone/data",
            method="PUT",
            json={
                "label": label,
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

    async def read_marimo_mime_renderer_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoMimeRendererData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoMimeRendererData]
            marimo-mime-renderer data accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-mime-renderer/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoMimeRendererData,
                    parse_obj_as(
                        type_=MarimoMimeRendererData,
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

    async def write_marimo_mime_renderer_data(
        self,
        *,
        mime: str,
        data: typing.Optional[MarimoMimeRendererDataData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        mime : str

        data : typing.Optional[MarimoMimeRendererDataData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-mime-renderer/data",
            method="PUT",
            json={
                "mime": mime,
                "data": convert_and_respect_annotation_metadata(
                    object_=data, annotation=typing.Optional[MarimoMimeRendererDataData], direction="write"
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

    async def read_marimo_mpl_interactive_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoMplInteractiveData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoMplInteractiveData]
            marimo-mpl-interactive data accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-mpl-interactive/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoMplInteractiveData,
                    parse_obj_as(
                        type_=MarimoMplInteractiveData,
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

    async def write_marimo_mpl_interactive_data(
        self,
        *,
        mpl_js_url: str,
        css_url: str,
        toolbar_images: typing.Dict[str, str],
        width: float,
        height: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        mpl_js_url : str

        css_url : str

        toolbar_images : typing.Dict[str, str]

        width : float

        height : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-mpl-interactive/data",
            method="PUT",
            json={
                "mplJsUrl": mpl_js_url,
                "cssUrl": css_url,
                "toolbarImages": toolbar_images,
                "width": width,
                "height": height,
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

    async def read_marimo_multiselect_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoMultiselectData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoMultiselectData]
            marimo-multiselect data accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-multiselect/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoMultiselectData,
                    parse_obj_as(
                        type_=MarimoMultiselectData,
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

    async def write_marimo_multiselect_data(
        self,
        *,
        initial_value: typing.Sequence[str],
        options: typing.Sequence[str],
        label: typing.Optional[str] = OMIT,
        full_width: typing.Optional[bool] = OMIT,
        max_selections: typing.Optional[float] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        initial_value : typing.Sequence[str]

        options : typing.Sequence[str]

        label : typing.Optional[str]

        full_width : typing.Optional[bool]

        max_selections : typing.Optional[float]

        disabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-multiselect/data",
            method="PUT",
            json={
                "initialValue": initial_value,
                "label": label,
                "options": options,
                "fullWidth": full_width,
                "maxSelections": max_selections,
                "disabled": disabled,
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

    async def read_marimo_nav_menu_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoNavMenuData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoNavMenuData]
            marimo-nav-menu data accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-nav-menu/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoNavMenuData,
                    parse_obj_as(
                        type_=MarimoNavMenuData,
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

    async def write_marimo_nav_menu_data(
        self,
        *,
        items: typing.Sequence[MarimoNavMenuDataItemsItem],
        orientation: MarimoNavMenuDataOrientation,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        items : typing.Sequence[MarimoNavMenuDataItemsItem]

        orientation : MarimoNavMenuDataOrientation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-nav-menu/data",
            method="PUT",
            json={
                "items": convert_and_respect_annotation_metadata(
                    object_=items, annotation=typing.Sequence[MarimoNavMenuDataItemsItem], direction="write"
                ),
                "orientation": orientation,
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

    async def read_marimo_number_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoNumberData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoNumberData]
            marimo-number data accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-number/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoNumberData,
                    parse_obj_as(
                        type_=MarimoNumberData,
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

    async def write_marimo_number_data(
        self,
        *,
        initial_value: typing.Optional[float] = OMIT,
        label: typing.Optional[str] = OMIT,
        start: typing.Optional[float] = OMIT,
        stop: typing.Optional[float] = OMIT,
        step: typing.Optional[float] = OMIT,
        debounce: typing.Optional[bool] = OMIT,
        full_width: typing.Optional[bool] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        initial_value : typing.Optional[float]

        label : typing.Optional[str]

        start : typing.Optional[float]

        stop : typing.Optional[float]

        step : typing.Optional[float]

        debounce : typing.Optional[bool]

        full_width : typing.Optional[bool]

        disabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-number/data",
            method="PUT",
            json={
                "initialValue": initial_value,
                "label": label,
                "start": start,
                "stop": stop,
                "step": step,
                "debounce": debounce,
                "fullWidth": full_width,
                "disabled": disabled,
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

    async def read_marimo_outline_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoOutlineData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoOutlineData]
            marimo-outline data accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-outline/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoOutlineData,
                    parse_obj_as(
                        type_=MarimoOutlineData,
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

    async def write_marimo_outline_data(
        self, *, label: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        label : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-outline/data",
            method="PUT",
            json={
                "label": label,
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

    async def read_marimo_panel_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoPanelData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoPanelData]
            marimo-panel data accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-panel/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoPanelData,
                    parse_obj_as(
                        type_=MarimoPanelData,
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

    async def write_marimo_panel_data(
        self,
        *,
        docs_json: typing.Dict[str, typing.Any],
        render_json: MarimoPanelDataRenderJson,
        extension_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        docs_json : typing.Dict[str, typing.Any]

        render_json : MarimoPanelDataRenderJson

        extension_url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-panel/data",
            method="PUT",
            json={
                "extensionUrl": extension_url,
                "docs_json": docs_json,
                "render_json": convert_and_respect_annotation_metadata(
                    object_=render_json, annotation=MarimoPanelDataRenderJson, direction="write"
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

    async def read_marimo_plotly_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoPlotlyData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoPlotlyData]
            marimo-plotly data accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-plotly/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoPlotlyData,
                    parse_obj_as(
                        type_=MarimoPlotlyData,
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

    async def write_marimo_plotly_data(
        self,
        *,
        figure: typing.Dict[str, typing.Any],
        config: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        figure : typing.Dict[str, typing.Any]

        config : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-plotly/data",
            method="PUT",
            json={
                "figure": figure,
                "config": config,
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

    async def read_marimo_progress_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoProgressData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoProgressData]
            marimo-progress data accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-progress/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoProgressData,
                    parse_obj_as(
                        type_=MarimoProgressData,
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

    async def write_marimo_progress_data(
        self,
        *,
        progress: MarimoProgressDataProgress,
        title: typing.Optional[str] = OMIT,
        subtitle: typing.Optional[str] = OMIT,
        total: typing.Optional[float] = OMIT,
        eta: typing.Optional[float] = OMIT,
        rate: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        progress : MarimoProgressDataProgress

        title : typing.Optional[str]

        subtitle : typing.Optional[str]

        total : typing.Optional[float]

        eta : typing.Optional[float]

        rate : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-progress/data",
            method="PUT",
            json={
                "title": title,
                "subtitle": subtitle,
                "progress": convert_and_respect_annotation_metadata(
                    object_=progress, annotation=MarimoProgressDataProgress, direction="write"
                ),
                "total": total,
                "eta": eta,
                "rate": rate,
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

    async def read_marimo_radio_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoRadioData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoRadioData]
            marimo-radio data accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-radio/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoRadioData,
                    parse_obj_as(
                        type_=MarimoRadioData,
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

    async def write_marimo_radio_data(
        self,
        *,
        options: typing.Sequence[str],
        initial_value: typing.Optional[str] = OMIT,
        inline: typing.Optional[bool] = OMIT,
        label: typing.Optional[str] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        options : typing.Sequence[str]

        initial_value : typing.Optional[str]

        inline : typing.Optional[bool]

        label : typing.Optional[str]

        disabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-radio/data",
            method="PUT",
            json={
                "initialValue": initial_value,
                "inline": inline,
                "label": label,
                "options": options,
                "disabled": disabled,
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

    async def read_marimo_range_slider_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoRangeSliderData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoRangeSliderData]
            marimo-range-slider data accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-range-slider/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoRangeSliderData,
                    parse_obj_as(
                        type_=MarimoRangeSliderData,
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

    async def write_marimo_range_slider_data(
        self,
        *,
        initial_value: typing.Sequence[float],
        start: float,
        stop: float,
        label: typing.Optional[str] = OMIT,
        step: typing.Optional[float] = OMIT,
        steps: typing.Optional[typing.Sequence[float]] = OMIT,
        debounce: typing.Optional[bool] = OMIT,
        orientation: typing.Optional[MarimoRangeSliderDataOrientation] = OMIT,
        show_value: typing.Optional[bool] = OMIT,
        full_width: typing.Optional[bool] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        initial_value : typing.Sequence[float]

        start : float

        stop : float

        label : typing.Optional[str]

        step : typing.Optional[float]

        steps : typing.Optional[typing.Sequence[float]]

        debounce : typing.Optional[bool]

        orientation : typing.Optional[MarimoRangeSliderDataOrientation]

        show_value : typing.Optional[bool]

        full_width : typing.Optional[bool]

        disabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-range-slider/data",
            method="PUT",
            json={
                "initialValue": initial_value,
                "label": label,
                "start": start,
                "stop": stop,
                "step": step,
                "steps": steps,
                "debounce": debounce,
                "orientation": orientation,
                "showValue": show_value,
                "fullWidth": full_width,
                "disabled": disabled,
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

    async def read_marimo_refresh_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoRefreshData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoRefreshData]
            marimo-refresh data accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-refresh/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoRefreshData,
                    parse_obj_as(
                        type_=MarimoRefreshData,
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

    async def write_marimo_refresh_data(
        self,
        *,
        options: typing.Optional[typing.Sequence[MarimoRefreshDataOptionsItem]] = OMIT,
        default_interval: typing.Optional[MarimoRefreshDataDefaultInterval] = OMIT,
        label: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        options : typing.Optional[typing.Sequence[MarimoRefreshDataOptionsItem]]

        default_interval : typing.Optional[MarimoRefreshDataDefaultInterval]

        label : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-refresh/data",
            method="PUT",
            json={
                "options": convert_and_respect_annotation_metadata(
                    object_=options, annotation=typing.Sequence[MarimoRefreshDataOptionsItem], direction="write"
                ),
                "defaultInterval": convert_and_respect_annotation_metadata(
                    object_=default_interval, annotation=MarimoRefreshDataDefaultInterval, direction="write"
                ),
                "label": label,
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

    async def read_marimo_routes_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoRoutesData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoRoutesData]
            marimo-routes data accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-routes/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoRoutesData,
                    parse_obj_as(
                        type_=MarimoRoutesData,
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

    async def write_marimo_routes_data(
        self, *, routes: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        routes : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-routes/data",
            method="PUT",
            json={
                "routes": routes,
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

    async def read_marimo_slider_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoSliderData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoSliderData]
            marimo-slider data accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-slider/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoSliderData,
                    parse_obj_as(
                        type_=MarimoSliderData,
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

    async def write_marimo_slider_data(
        self,
        *,
        initial_value: float,
        start: float,
        stop: float,
        label: typing.Optional[str] = OMIT,
        step: typing.Optional[float] = OMIT,
        steps: typing.Optional[typing.Sequence[float]] = OMIT,
        debounce: typing.Optional[bool] = OMIT,
        orientation: typing.Optional[MarimoSliderDataOrientation] = OMIT,
        show_value: typing.Optional[bool] = OMIT,
        full_width: typing.Optional[bool] = OMIT,
        include_input: typing.Optional[bool] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        initial_value : float

        start : float

        stop : float

        label : typing.Optional[str]

        step : typing.Optional[float]

        steps : typing.Optional[typing.Sequence[float]]

        debounce : typing.Optional[bool]

        orientation : typing.Optional[MarimoSliderDataOrientation]

        show_value : typing.Optional[bool]

        full_width : typing.Optional[bool]

        include_input : typing.Optional[bool]

        disabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-slider/data",
            method="PUT",
            json={
                "initialValue": initial_value,
                "label": label,
                "start": start,
                "stop": stop,
                "step": step,
                "steps": steps,
                "debounce": debounce,
                "orientation": orientation,
                "showValue": show_value,
                "fullWidth": full_width,
                "includeInput": include_input,
                "disabled": disabled,
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

    async def read_marimo_stat_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoStatData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoStatData]
            marimo-stat data accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-stat/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoStatData,
                    parse_obj_as(
                        type_=MarimoStatData,
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

    async def write_marimo_stat_data(
        self,
        *,
        value: typing.Optional[MarimoStatDataValue] = OMIT,
        label: typing.Optional[str] = OMIT,
        caption: typing.Optional[str] = OMIT,
        bordered: typing.Optional[bool] = OMIT,
        direction: typing.Optional[MarimoStatDataDirection] = OMIT,
        target_direction: typing.Optional[MarimoStatDataTargetDirection] = OMIT,
        slot: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        value : typing.Optional[MarimoStatDataValue]

        label : typing.Optional[str]

        caption : typing.Optional[str]

        bordered : typing.Optional[bool]

        direction : typing.Optional[MarimoStatDataDirection]

        target_direction : typing.Optional[MarimoStatDataTargetDirection]

        slot : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-stat/data",
            method="PUT",
            json={
                "value": convert_and_respect_annotation_metadata(
                    object_=value, annotation=MarimoStatDataValue, direction="write"
                ),
                "label": label,
                "caption": caption,
                "bordered": bordered,
                "direction": direction,
                "target_direction": target_direction,
                "slot": slot,
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

    async def read_marimo_switch_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoSwitchData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoSwitchData]
            marimo-switch data accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-switch/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoSwitchData,
                    parse_obj_as(
                        type_=MarimoSwitchData,
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

    async def write_marimo_switch_data(
        self,
        *,
        initial_value: bool,
        label: typing.Optional[str] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        initial_value : bool

        label : typing.Optional[str]

        disabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-switch/data",
            method="PUT",
            json={
                "initialValue": initial_value,
                "label": label,
                "disabled": disabled,
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

    async def read_marimo_table_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoTableData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoTableData]
            marimo-table data accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoTableData,
                    parse_obj_as(
                        type_=MarimoTableData,
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

    async def write_marimo_table_data(
        self,
        *,
        initial_value: MarimoTableDataInitialValue,
        data: MarimoTableDataData,
        total_rows: MarimoTableDataTotalRows,
        row_headers: typing.Sequence[typing.Sequence[typing.Any]],
        total_columns: float,
        label: typing.Optional[str] = OMIT,
        raw_data: typing.Optional[MarimoTableDataRawData] = OMIT,
        pagination: typing.Optional[bool] = OMIT,
        page_size: typing.Optional[float] = OMIT,
        selection: typing.Optional[MarimoTableDataSelection] = OMIT,
        show_download: typing.Optional[bool] = OMIT,
        show_filters: typing.Optional[bool] = OMIT,
        show_column_summaries: typing.Optional[MarimoTableDataShowColumnSummaries] = OMIT,
        show_data_types: typing.Optional[bool] = OMIT,
        show_page_size_selector: typing.Optional[bool] = OMIT,
        show_column_explorer: typing.Optional[bool] = OMIT,
        show_row_explorer: typing.Optional[bool] = OMIT,
        show_chart_builder: typing.Optional[bool] = OMIT,
        show_search: typing.Optional[bool] = OMIT,
        freeze_columns_left: typing.Optional[typing.Sequence[str]] = OMIT,
        freeze_columns_right: typing.Optional[typing.Sequence[str]] = OMIT,
        hidden_columns: typing.Optional[typing.Sequence[str]] = OMIT,
        text_justify_columns: typing.Optional[typing.Dict[str, MarimoTableDataTextJustifyColumnsValue]] = OMIT,
        wrapped_columns: typing.Optional[typing.Sequence[str]] = OMIT,
        column_widths: typing.Optional[typing.Dict[str, int]] = OMIT,
        header_tooltip: typing.Optional[typing.Dict[str, str]] = OMIT,
        field_types: typing.Optional[typing.Sequence[typing.Sequence[typing.Any]]] = OMIT,
        max_columns: typing.Optional[MarimoTableDataMaxColumns] = OMIT,
        has_stable_row_id: typing.Optional[bool] = OMIT,
        max_height: typing.Optional[float] = OMIT,
        cell_styles: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Dict[str, typing.Any]]]] = OMIT,
        hover_template: typing.Optional[str] = OMIT,
        cell_hover_texts: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Optional[str]]]] = OMIT,
        lazy: typing.Optional[bool] = OMIT,
        preload: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        initial_value : MarimoTableDataInitialValue

        data : MarimoTableDataData

        total_rows : MarimoTableDataTotalRows

        row_headers : typing.Sequence[typing.Sequence[typing.Any]]

        total_columns : float

        label : typing.Optional[str]

        raw_data : typing.Optional[MarimoTableDataRawData]

        pagination : typing.Optional[bool]

        page_size : typing.Optional[float]

        selection : typing.Optional[MarimoTableDataSelection]

        show_download : typing.Optional[bool]

        show_filters : typing.Optional[bool]

        show_column_summaries : typing.Optional[MarimoTableDataShowColumnSummaries]

        show_data_types : typing.Optional[bool]

        show_page_size_selector : typing.Optional[bool]

        show_column_explorer : typing.Optional[bool]

        show_row_explorer : typing.Optional[bool]

        show_chart_builder : typing.Optional[bool]

        show_search : typing.Optional[bool]

        freeze_columns_left : typing.Optional[typing.Sequence[str]]

        freeze_columns_right : typing.Optional[typing.Sequence[str]]

        hidden_columns : typing.Optional[typing.Sequence[str]]

        text_justify_columns : typing.Optional[typing.Dict[str, MarimoTableDataTextJustifyColumnsValue]]

        wrapped_columns : typing.Optional[typing.Sequence[str]]

        column_widths : typing.Optional[typing.Dict[str, int]]

        header_tooltip : typing.Optional[typing.Dict[str, str]]

        field_types : typing.Optional[typing.Sequence[typing.Sequence[typing.Any]]]

        max_columns : typing.Optional[MarimoTableDataMaxColumns]

        has_stable_row_id : typing.Optional[bool]

        max_height : typing.Optional[float]

        cell_styles : typing.Optional[typing.Dict[str, typing.Dict[str, typing.Dict[str, typing.Any]]]]

        hover_template : typing.Optional[str]

        cell_hover_texts : typing.Optional[typing.Dict[str, typing.Dict[str, typing.Optional[str]]]]

        lazy : typing.Optional[bool]

        preload : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-table/data",
            method="PUT",
            json={
                "initialValue": convert_and_respect_annotation_metadata(
                    object_=initial_value, annotation=MarimoTableDataInitialValue, direction="write"
                ),
                "label": label,
                "data": convert_and_respect_annotation_metadata(
                    object_=data, annotation=MarimoTableDataData, direction="write"
                ),
                "rawData": convert_and_respect_annotation_metadata(
                    object_=raw_data, annotation=typing.Optional[MarimoTableDataRawData], direction="write"
                ),
                "totalRows": convert_and_respect_annotation_metadata(
                    object_=total_rows, annotation=MarimoTableDataTotalRows, direction="write"
                ),
                "pagination": pagination,
                "pageSize": page_size,
                "selection": selection,
                "showDownload": show_download,
                "showFilters": show_filters,
                "showColumnSummaries": convert_and_respect_annotation_metadata(
                    object_=show_column_summaries, annotation=MarimoTableDataShowColumnSummaries, direction="write"
                ),
                "showDataTypes": show_data_types,
                "showPageSizeSelector": show_page_size_selector,
                "showColumnExplorer": show_column_explorer,
                "showRowExplorer": show_row_explorer,
                "showChartBuilder": show_chart_builder,
                "showSearch": show_search,
                "rowHeaders": row_headers,
                "freezeColumnsLeft": freeze_columns_left,
                "freezeColumnsRight": freeze_columns_right,
                "hiddenColumns": hidden_columns,
                "textJustifyColumns": text_justify_columns,
                "wrappedColumns": wrapped_columns,
                "columnWidths": column_widths,
                "headerTooltip": header_tooltip,
                "fieldTypes": field_types,
                "totalColumns": total_columns,
                "maxColumns": convert_and_respect_annotation_metadata(
                    object_=max_columns, annotation=MarimoTableDataMaxColumns, direction="write"
                ),
                "hasStableRowId": has_stable_row_id,
                "maxHeight": max_height,
                "cellStyles": cell_styles,
                "hoverTemplate": hover_template,
                "cellHoverTexts": cell_hover_texts,
                "lazy": lazy,
                "preload": preload,
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

    async def read_marimo_tabs_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoTabsData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoTabsData]
            marimo-tabs data accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-tabs/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoTabsData,
                    parse_obj_as(
                        type_=MarimoTabsData,
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

    async def write_marimo_tabs_data(
        self,
        *,
        tabs: typing.Sequence[str],
        label: typing.Optional[str] = OMIT,
        orientation: typing.Optional[MarimoTabsDataOrientation] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        tabs : typing.Sequence[str]

        label : typing.Optional[str]

        orientation : typing.Optional[MarimoTabsDataOrientation]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-tabs/data",
            method="PUT",
            json={
                "tabs": tabs,
                "label": label,
                "orientation": orientation,
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

    async def read_marimo_tex_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoTexData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoTexData]
            marimo-tex data accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-tex/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoTexData,
                    parse_obj_as(
                        type_=MarimoTexData,
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

    async def write_marimo_tex_data(
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
            "plugins/marimo-tex/data",
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

    async def read_marimo_text_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoTextData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoTextData]
            marimo-text data accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-text/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoTextData,
                    parse_obj_as(
                        type_=MarimoTextData,
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

    async def write_marimo_text_data(
        self,
        *,
        initial_value: str,
        placeholder: str,
        label: typing.Optional[str] = OMIT,
        kind: typing.Optional[MarimoTextDataKind] = OMIT,
        max_length: typing.Optional[float] = OMIT,
        min_length: typing.Optional[float] = OMIT,
        full_width: typing.Optional[bool] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        debounce: typing.Optional[MarimoTextDataDebounce] = OMIT,
        password_has_value: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        initial_value : str

        placeholder : str

        label : typing.Optional[str]

        kind : typing.Optional[MarimoTextDataKind]

        max_length : typing.Optional[float]

        min_length : typing.Optional[float]

        full_width : typing.Optional[bool]

        disabled : typing.Optional[bool]

        debounce : typing.Optional[MarimoTextDataDebounce]

        password_has_value : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-text/data",
            method="PUT",
            json={
                "initialValue": initial_value,
                "placeholder": placeholder,
                "label": label,
                "kind": kind,
                "maxLength": max_length,
                "minLength": min_length,
                "fullWidth": full_width,
                "disabled": disabled,
                "debounce": convert_and_respect_annotation_metadata(
                    object_=debounce, annotation=MarimoTextDataDebounce, direction="write"
                ),
                "passwordHasValue": password_has_value,
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

    async def read_marimo_text_area_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoTextAreaData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoTextAreaData]
            marimo-text-area data accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-text-area/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoTextAreaData,
                    parse_obj_as(
                        type_=MarimoTextAreaData,
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

    async def write_marimo_text_area_data(
        self,
        *,
        initial_value: str,
        placeholder: str,
        label: typing.Optional[str] = OMIT,
        max_length: typing.Optional[float] = OMIT,
        min_length: typing.Optional[float] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        debounce: typing.Optional[MarimoTextAreaDataDebounce] = OMIT,
        rows: typing.Optional[float] = OMIT,
        full_width: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        initial_value : str

        placeholder : str

        label : typing.Optional[str]

        max_length : typing.Optional[float]

        min_length : typing.Optional[float]

        disabled : typing.Optional[bool]

        debounce : typing.Optional[MarimoTextAreaDataDebounce]

        rows : typing.Optional[float]

        full_width : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-text-area/data",
            method="PUT",
            json={
                "initialValue": initial_value,
                "placeholder": placeholder,
                "label": label,
                "maxLength": max_length,
                "minLength": min_length,
                "disabled": disabled,
                "debounce": convert_and_respect_annotation_metadata(
                    object_=debounce, annotation=MarimoTextAreaDataDebounce, direction="write"
                ),
                "rows": rows,
                "fullWidth": full_width,
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

    async def read_marimo_vega_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarimoVegaData]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarimoVegaData]
            marimo-vega data accepted by a plugin consumer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-vega/data",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarimoVegaData,
                    parse_obj_as(
                        type_=MarimoVegaData,
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

    async def write_marimo_vega_data(
        self,
        *,
        spec: typing.Dict[str, typing.Any],
        chart_selection: typing.Optional[MarimoVegaDataChartSelection] = OMIT,
        field_selection: typing.Optional[MarimoVegaDataFieldSelection] = OMIT,
        embed_options: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        spec : typing.Dict[str, typing.Any]

        chart_selection : typing.Optional[MarimoVegaDataChartSelection]

        field_selection : typing.Optional[MarimoVegaDataFieldSelection]

        embed_options : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugins/marimo-vega/data",
            method="PUT",
            json={
                "spec": spec,
                "chartSelection": convert_and_respect_annotation_metadata(
                    object_=chart_selection, annotation=MarimoVegaDataChartSelection, direction="write"
                ),
                "fieldSelection": convert_and_respect_annotation_metadata(
                    object_=field_selection, annotation=MarimoVegaDataFieldSelection, direction="write"
                ),
                "embedOptions": embed_options,
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
