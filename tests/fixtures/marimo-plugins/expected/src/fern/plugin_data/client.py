

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
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
from .raw_client import AsyncRawPluginDataClient, RawPluginDataClient


OMIT = typing.cast(typing.Any, ...)


class PluginDataClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPluginDataClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPluginDataClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPluginDataClient
        """
        return self._raw_client

    def read_marimo_accordion_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoAccordionData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoAccordionData
            marimo-accordion data accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.read_marimo_accordion_data()
        """
        _response = self._raw_client.read_marimo_accordion_data(request_options=request_options)
        return _response.data

    def write_marimo_accordion_data(
        self,
        *,
        labels: typing.Sequence[str],
        multiple: bool,
        expanded: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.write_marimo_accordion_data(
            labels=["labels"],
            multiple=True,
        )
        """
        _response = self._raw_client.write_marimo_accordion_data(
            labels=labels, multiple=multiple, expanded=expanded, request_options=request_options
        )
        return _response.data

    def read_marimo_anywidget_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoAnywidgetData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoAnywidgetData
            marimo-anywidget data accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.read_marimo_anywidget_data()
        """
        _response = self._raw_client.read_marimo_anywidget_data(request_options=request_options)
        return _response.data

    def write_marimo_anywidget_data(
        self, *, model_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        model_id : str

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
        client.plugin_data.write_marimo_anywidget_data(
            model_id="modelId",
        )
        """
        _response = self._raw_client.write_marimo_anywidget_data(model_id=model_id, request_options=request_options)
        return _response.data

    def read_marimo_button_data(self, *, request_options: typing.Optional[RequestOptions] = None) -> MarimoButtonData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoButtonData
            marimo-button data accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.read_marimo_button_data()
        """
        _response = self._raw_client.read_marimo_button_data(request_options=request_options)
        return _response.data

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
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.write_marimo_button_data(
            label="label",
        )
        """
        _response = self._raw_client.write_marimo_button_data(
            label=label,
            kind=kind,
            disabled=disabled,
            full_width=full_width,
            tooltip=tooltip,
            keyboard_shortcut=keyboard_shortcut,
            request_options=request_options,
        )
        return _response.data

    def read_marimo_callout_output_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoCalloutOutputData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoCalloutOutputData
            marimo-callout-output data accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.read_marimo_callout_output_data()
        """
        _response = self._raw_client.read_marimo_callout_output_data(request_options=request_options)
        return _response.data

    def write_marimo_callout_output_data(
        self,
        *,
        html: str,
        kind: typing.Optional[MarimoCalloutOutputDataKind] = OMIT,
        title: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.write_marimo_callout_output_data(
            html="html",
        )
        """
        _response = self._raw_client.write_marimo_callout_output_data(
            html=html, kind=kind, title=title, request_options=request_options
        )
        return _response.data

    def read_marimo_carousel_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoCarouselData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoCarouselData
            marimo-carousel data accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.read_marimo_carousel_data()
        """
        _response = self._raw_client.read_marimo_carousel_data(request_options=request_options)
        return _response.data

    def write_marimo_carousel_data(
        self,
        *,
        index: typing.Optional[str] = OMIT,
        height: typing.Optional[MarimoCarouselDataHeight] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        index : typing.Optional[str]

        height : typing.Optional[MarimoCarouselDataHeight]

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
        client.plugin_data.write_marimo_carousel_data()
        """
        _response = self._raw_client.write_marimo_carousel_data(
            index=index, height=height, request_options=request_options
        )
        return _response.data

    def read_marimo_chatbot_data(self, *, request_options: typing.Optional[RequestOptions] = None) -> MarimoChatbotData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoChatbotData
            marimo-chatbot data accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.read_marimo_chatbot_data()
        """
        _response = self._raw_client.read_marimo_chatbot_data(request_options=request_options)
        return _response.data

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
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi, MarimoChatbotDataConfig

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.write_marimo_chatbot_data(
            show_configuration_controls=True,
            config=MarimoChatbotDataConfig(),
            allow_attachments=True,
        )
        """
        _response = self._raw_client.write_marimo_chatbot_data(
            show_configuration_controls=show_configuration_controls,
            config=config,
            allow_attachments=allow_attachments,
            prompts=prompts,
            max_height=max_height,
            disabled=disabled,
            request_options=request_options,
        )
        return _response.data

    def read_marimo_checkbox_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoCheckboxData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoCheckboxData
            marimo-checkbox data accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.read_marimo_checkbox_data()
        """
        _response = self._raw_client.read_marimo_checkbox_data(request_options=request_options)
        return _response.data

    def write_marimo_checkbox_data(
        self,
        *,
        initial_value: bool,
        label: typing.Optional[str] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.write_marimo_checkbox_data(
            initial_value=True,
        )
        """
        _response = self._raw_client.write_marimo_checkbox_data(
            initial_value=initial_value, label=label, disabled=disabled, request_options=request_options
        )
        return _response.data

    def read_marimo_code_editor_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoCodeEditorData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoCodeEditorData
            marimo-code-editor data accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.read_marimo_code_editor_data()
        """
        _response = self._raw_client.read_marimo_code_editor_data(request_options=request_options)
        return _response.data

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
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.write_marimo_code_editor_data(
            initial_value="initialValue",
            placeholder="placeholder",
        )
        """
        _response = self._raw_client.write_marimo_code_editor_data(
            initial_value=initial_value,
            placeholder=placeholder,
            language=language,
            theme=theme,
            label=label,
            disabled=disabled,
            min_height=min_height,
            max_height=max_height,
            show_copy_button=show_copy_button,
            debounce=debounce,
            request_options=request_options,
        )
        return _response.data

    def read_marimo_data_editor_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoDataEditorData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoDataEditorData
            marimo-data-editor data accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.read_marimo_data_editor_data()
        """
        _response = self._raw_client.read_marimo_data_editor_data(request_options=request_options)
        return _response.data

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
    ) -> None:
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
        None

        Examples
        --------
        from fern import (
            FernApi,
            MarimoDataEditorDataEditableColumnsOne,
            MarimoDataEditorDataInitialValue,
        )

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.write_marimo_data_editor_data(
            initial_value=MarimoDataEditorDataInitialValue(
                edits=[],
            ),
            data="data",
            editable_columns=MarimoDataEditorDataEditableColumnsOne.ALL,
        )
        """
        _response = self._raw_client.write_marimo_data_editor_data(
            initial_value=initial_value,
            data=data,
            editable_columns=editable_columns,
            label=label,
            field_types=field_types,
            column_names=column_names,
            column_sizing_mode=column_sizing_mode,
            request_options=request_options,
        )
        return _response.data

    def read_marimo_data_explorer_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoDataExplorerData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoDataExplorerData
            marimo-data-explorer data accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.read_marimo_data_explorer_data()
        """
        _response = self._raw_client.read_marimo_data_explorer_data(request_options=request_options)
        return _response.data

    def write_marimo_data_explorer_data(
        self, *, data: str, label: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        data : str

        label : typing.Optional[str]

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
        client.plugin_data.write_marimo_data_explorer_data(
            data="data",
        )
        """
        _response = self._raw_client.write_marimo_data_explorer_data(
            data=data, label=label, request_options=request_options
        )
        return _response.data

    def read_marimo_dataframe_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoDataframeData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoDataframeData
            marimo-dataframe data accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.read_marimo_dataframe_data()
        """
        _response = self._raw_client.read_marimo_dataframe_data(request_options=request_options)
        return _response.data

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
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.write_marimo_dataframe_data(
            columns=[[]],
        )
        """
        _response = self._raw_client.write_marimo_dataframe_data(
            columns=columns,
            label=label,
            page_size=page_size,
            show_download=show_download,
            dataframe_name=dataframe_name,
            lazy=lazy,
            request_options=request_options,
        )
        return _response.data

    def read_marimo_date_data(self, *, request_options: typing.Optional[RequestOptions] = None) -> MarimoDateData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoDateData
            marimo-date data accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.read_marimo_date_data()
        """
        _response = self._raw_client.read_marimo_date_data(request_options=request_options)
        return _response.data

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
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.write_marimo_date_data(
            initial_value="initialValue",
            start="start",
            stop="stop",
        )
        """
        _response = self._raw_client.write_marimo_date_data(
            initial_value=initial_value,
            start=start,
            stop=stop,
            label=label,
            step=step,
            full_width=full_width,
            disabled=disabled,
            request_options=request_options,
        )
        return _response.data

    def read_marimo_date_range_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoDateRangeData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoDateRangeData
            marimo-date-range data accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.read_marimo_date_range_data()
        """
        _response = self._raw_client.read_marimo_date_range_data(request_options=request_options)
        return _response.data

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
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.write_marimo_date_range_data(
            initial_value=[],
            start="start",
            stop="stop",
        )
        """
        _response = self._raw_client.write_marimo_date_range_data(
            initial_value=initial_value,
            start=start,
            stop=stop,
            label=label,
            step=step,
            full_width=full_width,
            disabled=disabled,
            request_options=request_options,
        )
        return _response.data

    def read_marimo_datetime_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoDatetimeData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoDatetimeData
            marimo-datetime data accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.read_marimo_datetime_data()
        """
        _response = self._raw_client.read_marimo_datetime_data(request_options=request_options)
        return _response.data

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
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.write_marimo_datetime_data(
            initial_value="initialValue",
            start="start",
            stop="stop",
        )
        """
        _response = self._raw_client.write_marimo_datetime_data(
            initial_value=initial_value,
            start=start,
            stop=stop,
            label=label,
            step=step,
            precision=precision,
            full_width=full_width,
            disabled=disabled,
            request_options=request_options,
        )
        return _response.data

    def read_marimo_dict_data(self, *, request_options: typing.Optional[RequestOptions] = None) -> MarimoDictData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoDictData
            marimo-dict data accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.read_marimo_dict_data()
        """
        _response = self._raw_client.read_marimo_dict_data(request_options=request_options)
        return _response.data

    def write_marimo_dict_data(
        self,
        *,
        element_ids: typing.Dict[str, str],
        label: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        element_ids : typing.Dict[str, str]

        label : typing.Optional[str]

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
        client.plugin_data.write_marimo_dict_data(
            element_ids={"key": "value"},
        )
        """
        _response = self._raw_client.write_marimo_dict_data(
            element_ids=element_ids, label=label, request_options=request_options
        )
        return _response.data

    def read_marimo_download_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoDownloadData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoDownloadData
            marimo-download data accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.read_marimo_download_data()
        """
        _response = self._raw_client.read_marimo_download_data(request_options=request_options)
        return _response.data

    def write_marimo_download_data(
        self,
        *,
        data: str,
        disabled: typing.Optional[bool] = OMIT,
        filename: typing.Optional[str] = OMIT,
        label: typing.Optional[str] = OMIT,
        lazy: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.write_marimo_download_data(
            data="data",
        )
        """
        _response = self._raw_client.write_marimo_download_data(
            data=data, disabled=disabled, filename=filename, label=label, lazy=lazy, request_options=request_options
        )
        return _response.data

    def read_marimo_dropdown_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoDropdownData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoDropdownData
            marimo-dropdown data accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.read_marimo_dropdown_data()
        """
        _response = self._raw_client.read_marimo_dropdown_data(request_options=request_options)
        return _response.data

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
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.write_marimo_dropdown_data(
            initial_value=["initialValue"],
            options=["options"],
            allow_select_none=True,
        )
        """
        _response = self._raw_client.write_marimo_dropdown_data(
            initial_value=initial_value,
            options=options,
            allow_select_none=allow_select_none,
            label=label,
            full_width=full_width,
            searchable=searchable,
            disabled=disabled,
            request_options=request_options,
        )
        return _response.data

    def read_marimo_file_data(self, *, request_options: typing.Optional[RequestOptions] = None) -> MarimoFileData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoFileData
            marimo-file data accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.read_marimo_file_data()
        """
        _response = self._raw_client.read_marimo_file_data(request_options=request_options)
        return _response.data

    def write_marimo_file_data(
        self,
        *,
        filetypes: typing.Sequence[str],
        multiple: bool,
        kind: MarimoFileDataKind,
        max_size: float,
        label: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi, MarimoFileDataKind

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.write_marimo_file_data(
            filetypes=["filetypes"],
            multiple=True,
            kind=MarimoFileDataKind.BUTTON,
            max_size=1.1,
        )
        """
        _response = self._raw_client.write_marimo_file_data(
            filetypes=filetypes,
            multiple=multiple,
            kind=kind,
            max_size=max_size,
            label=label,
            request_options=request_options,
        )
        return _response.data

    def read_marimo_file_browser_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoFileBrowserData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoFileBrowserData
            marimo-file-browser data accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.read_marimo_file_browser_data()
        """
        _response = self._raw_client.read_marimo_file_browser_data(request_options=request_options)
        return _response.data

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
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.write_marimo_file_browser_data(
            initial_path="initialPath",
            filetypes=["filetypes"],
            selection_mode="selectionMode",
            multiple=True,
            restrict_navigation=True,
        )
        """
        _response = self._raw_client.write_marimo_file_browser_data(
            initial_path=initial_path,
            filetypes=filetypes,
            selection_mode=selection_mode,
            multiple=multiple,
            restrict_navigation=restrict_navigation,
            label=label,
            request_options=request_options,
        )
        return _response.data

    def read_marimo_form_data(self, *, request_options: typing.Optional[RequestOptions] = None) -> MarimoFormData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoFormData
            marimo-form data accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.read_marimo_form_data()
        """
        _response = self._raw_client.read_marimo_form_data(request_options=request_options)
        return _response.data

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
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.write_marimo_form_data(
            element_id="elementId",
        )
        """
        _response = self._raw_client.write_marimo_form_data(
            element_id=element_id,
            label=label,
            bordered=bordered,
            loading=loading,
            submit_button_label=submit_button_label,
            submit_button_tooltip=submit_button_tooltip,
            submit_button_disabled=submit_button_disabled,
            clear_on_submit=clear_on_submit,
            show_clear_button=show_clear_button,
            clear_button_label=clear_button_label,
            clear_button_tooltip=clear_button_tooltip,
            should_validate=should_validate,
            request_options=request_options,
        )
        return _response.data

    def read_marimo_image_comparison_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoImageComparisonData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoImageComparisonData
            marimo-image-comparison data accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.read_marimo_image_comparison_data()
        """
        _response = self._raw_client.read_marimo_image_comparison_data(request_options=request_options)
        return _response.data

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
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.write_marimo_image_comparison_data(
            before_src="beforeSrc",
            after_src="afterSrc",
        )
        """
        _response = self._raw_client.write_marimo_image_comparison_data(
            before_src=before_src,
            after_src=after_src,
            value=value,
            direction=direction,
            width=width,
            height=height,
            request_options=request_options,
        )
        return _response.data

    def read_marimo_json_output_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoJsonOutputData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoJsonOutputData
            marimo-json-output data accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.read_marimo_json_output_data()
        """
        _response = self._raw_client.read_marimo_json_output_data(request_options=request_options)
        return _response.data

    def write_marimo_json_output_data(
        self,
        *,
        json_data: typing.Any,
        name: typing.Optional[str] = OMIT,
        value_types: typing.Optional[MarimoJsonOutputDataValueTypes] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.write_marimo_json_output_data(
            json_data={"key": "value"},
        )
        """
        _response = self._raw_client.write_marimo_json_output_data(
            json_data=json_data, name=name, value_types=value_types, request_options=request_options
        )
        return _response.data

    def read_marimo_lazy_data(self, *, request_options: typing.Optional[RequestOptions] = None) -> MarimoLazyData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoLazyData
            marimo-lazy data accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.read_marimo_lazy_data()
        """
        _response = self._raw_client.read_marimo_lazy_data(request_options=request_options)
        return _response.data

    def write_marimo_lazy_data(
        self,
        *,
        show_loading_indicator: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        show_loading_indicator : typing.Optional[bool]

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
        client.plugin_data.write_marimo_lazy_data()
        """
        _response = self._raw_client.write_marimo_lazy_data(
            show_loading_indicator=show_loading_indicator, request_options=request_options
        )
        return _response.data

    def read_marimo_matplotlib_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoMatplotlibData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoMatplotlibData
            marimo-matplotlib data accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.read_marimo_matplotlib_data()
        """
        _response = self._raw_client.read_marimo_matplotlib_data(request_options=request_options)
        return _response.data

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
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.write_marimo_matplotlib_data(
            chart_base64="chartBase64",
            x_bounds=[],
            y_bounds=[],
            axes_pixel_bounds=[],
            width=1.1,
            height=1.1,
            debounce=True,
        )
        """
        _response = self._raw_client.write_marimo_matplotlib_data(
            chart_base64=chart_base64,
            x_bounds=x_bounds,
            y_bounds=y_bounds,
            axes_pixel_bounds=axes_pixel_bounds,
            width=width,
            height=height,
            debounce=debounce,
            selection_color=selection_color,
            selection_opacity=selection_opacity,
            stroke_width=stroke_width,
            x_scale=x_scale,
            y_scale=y_scale,
            request_options=request_options,
        )
        return _response.data

    def read_marimo_matrix_data(self, *, request_options: typing.Optional[RequestOptions] = None) -> MarimoMatrixData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoMatrixData
            marimo-matrix data accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.read_marimo_matrix_data()
        """
        _response = self._raw_client.read_marimo_matrix_data(request_options=request_options)
        return _response.data

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
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.write_marimo_matrix_data(
            initial_value=[[1.1]],
            step=[[1.1]],
            precision=1.1,
            symmetric=True,
            scientific=True,
            disabled=[[True]],
        )
        """
        _response = self._raw_client.write_marimo_matrix_data(
            initial_value=initial_value,
            step=step,
            precision=precision,
            symmetric=symmetric,
            scientific=scientific,
            disabled=disabled,
            label=label,
            min_value=min_value,
            max_value=max_value,
            row_labels=row_labels,
            column_labels=column_labels,
            debounce=debounce,
            request_options=request_options,
        )
        return _response.data

    def read_marimo_mermaid_data(self, *, request_options: typing.Optional[RequestOptions] = None) -> MarimoMermaidData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoMermaidData
            marimo-mermaid data accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.read_marimo_mermaid_data()
        """
        _response = self._raw_client.read_marimo_mermaid_data(request_options=request_options)
        return _response.data

    def write_marimo_mermaid_data(
        self,
        *,
        diagram: str,
        theme: typing.Optional[str] = OMIT,
        theme_variables: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.write_marimo_mermaid_data(
            diagram="diagram",
        )
        """
        _response = self._raw_client.write_marimo_mermaid_data(
            diagram=diagram, theme=theme, theme_variables=theme_variables, request_options=request_options
        )
        return _response.data

    def read_marimo_microphone_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoMicrophoneData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoMicrophoneData
            marimo-microphone data accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.read_marimo_microphone_data()
        """
        _response = self._raw_client.read_marimo_microphone_data(request_options=request_options)
        return _response.data

    def write_marimo_microphone_data(
        self, *, label: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        label : typing.Optional[str]

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
        client.plugin_data.write_marimo_microphone_data()
        """
        _response = self._raw_client.write_marimo_microphone_data(label=label, request_options=request_options)
        return _response.data

    def read_marimo_mime_renderer_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoMimeRendererData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoMimeRendererData
            marimo-mime-renderer data accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.read_marimo_mime_renderer_data()
        """
        _response = self._raw_client.read_marimo_mime_renderer_data(request_options=request_options)
        return _response.data

    def write_marimo_mime_renderer_data(
        self,
        *,
        mime: str,
        data: typing.Optional[MarimoMimeRendererDataData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        mime : str

        data : typing.Optional[MarimoMimeRendererDataData]

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
        client.plugin_data.write_marimo_mime_renderer_data(
            mime="mime",
        )
        """
        _response = self._raw_client.write_marimo_mime_renderer_data(
            mime=mime, data=data, request_options=request_options
        )
        return _response.data

    def read_marimo_mpl_interactive_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoMplInteractiveData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoMplInteractiveData
            marimo-mpl-interactive data accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.read_marimo_mpl_interactive_data()
        """
        _response = self._raw_client.read_marimo_mpl_interactive_data(request_options=request_options)
        return _response.data

    def write_marimo_mpl_interactive_data(
        self,
        *,
        mpl_js_url: str,
        css_url: str,
        toolbar_images: typing.Dict[str, str],
        width: float,
        height: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.write_marimo_mpl_interactive_data(
            mpl_js_url="mplJsUrl",
            css_url="cssUrl",
            toolbar_images={"key": "value"},
            width=1.1,
            height=1.1,
        )
        """
        _response = self._raw_client.write_marimo_mpl_interactive_data(
            mpl_js_url=mpl_js_url,
            css_url=css_url,
            toolbar_images=toolbar_images,
            width=width,
            height=height,
            request_options=request_options,
        )
        return _response.data

    def read_marimo_multiselect_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoMultiselectData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoMultiselectData
            marimo-multiselect data accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.read_marimo_multiselect_data()
        """
        _response = self._raw_client.read_marimo_multiselect_data(request_options=request_options)
        return _response.data

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
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.write_marimo_multiselect_data(
            initial_value=["initialValue"],
            options=["options"],
        )
        """
        _response = self._raw_client.write_marimo_multiselect_data(
            initial_value=initial_value,
            options=options,
            label=label,
            full_width=full_width,
            max_selections=max_selections,
            disabled=disabled,
            request_options=request_options,
        )
        return _response.data

    def read_marimo_nav_menu_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoNavMenuData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoNavMenuData
            marimo-nav-menu data accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.read_marimo_nav_menu_data()
        """
        _response = self._raw_client.read_marimo_nav_menu_data(request_options=request_options)
        return _response.data

    def write_marimo_nav_menu_data(
        self,
        *,
        items: typing.Sequence[MarimoNavMenuDataItemsItem],
        orientation: MarimoNavMenuDataOrientation,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        items : typing.Sequence[MarimoNavMenuDataItemsItem]

        orientation : MarimoNavMenuDataOrientation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import (
            FernApi,
            MarimoNavMenuDataItemsItemDescription,
            MarimoNavMenuDataOrientation,
        )

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.write_marimo_nav_menu_data(
            items=[
                MarimoNavMenuDataItemsItemDescription(
                    label="label",
                    href="href",
                )
            ],
            orientation=MarimoNavMenuDataOrientation.HORIZONTAL,
        )
        """
        _response = self._raw_client.write_marimo_nav_menu_data(
            items=items, orientation=orientation, request_options=request_options
        )
        return _response.data

    def read_marimo_number_data(self, *, request_options: typing.Optional[RequestOptions] = None) -> MarimoNumberData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoNumberData
            marimo-number data accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.read_marimo_number_data()
        """
        _response = self._raw_client.read_marimo_number_data(request_options=request_options)
        return _response.data

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
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.write_marimo_number_data()
        """
        _response = self._raw_client.write_marimo_number_data(
            initial_value=initial_value,
            label=label,
            start=start,
            stop=stop,
            step=step,
            debounce=debounce,
            full_width=full_width,
            disabled=disabled,
            request_options=request_options,
        )
        return _response.data

    def read_marimo_outline_data(self, *, request_options: typing.Optional[RequestOptions] = None) -> MarimoOutlineData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoOutlineData
            marimo-outline data accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.read_marimo_outline_data()
        """
        _response = self._raw_client.read_marimo_outline_data(request_options=request_options)
        return _response.data

    def write_marimo_outline_data(
        self, *, label: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        label : typing.Optional[str]

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
        client.plugin_data.write_marimo_outline_data()
        """
        _response = self._raw_client.write_marimo_outline_data(label=label, request_options=request_options)
        return _response.data

    def read_marimo_panel_data(self, *, request_options: typing.Optional[RequestOptions] = None) -> MarimoPanelData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoPanelData
            marimo-panel data accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.read_marimo_panel_data()
        """
        _response = self._raw_client.read_marimo_panel_data(request_options=request_options)
        return _response.data

    def write_marimo_panel_data(
        self,
        *,
        docs_json: typing.Dict[str, typing.Any],
        render_json: MarimoPanelDataRenderJson,
        extension_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi, MarimoPanelDataRenderJson

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.write_marimo_panel_data(
            docs_json={"key": "value"},
            render_json=MarimoPanelDataRenderJson(
                roots={"key": "value"},
            ),
        )
        """
        _response = self._raw_client.write_marimo_panel_data(
            docs_json=docs_json, render_json=render_json, extension_url=extension_url, request_options=request_options
        )
        return _response.data

    def read_marimo_plotly_data(self, *, request_options: typing.Optional[RequestOptions] = None) -> MarimoPlotlyData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoPlotlyData
            marimo-plotly data accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.read_marimo_plotly_data()
        """
        _response = self._raw_client.read_marimo_plotly_data(request_options=request_options)
        return _response.data

    def write_marimo_plotly_data(
        self,
        *,
        figure: typing.Dict[str, typing.Any],
        config: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        figure : typing.Dict[str, typing.Any]

        config : typing.Dict[str, typing.Any]

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
        client.plugin_data.write_marimo_plotly_data(
            figure={"key": "value"},
            config={"key": "value"},
        )
        """
        _response = self._raw_client.write_marimo_plotly_data(
            figure=figure, config=config, request_options=request_options
        )
        return _response.data

    def read_marimo_progress_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoProgressData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoProgressData
            marimo-progress data accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.read_marimo_progress_data()
        """
        _response = self._raw_client.read_marimo_progress_data(request_options=request_options)
        return _response.data

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
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.write_marimo_progress_data(
            progress=1.1,
        )
        """
        _response = self._raw_client.write_marimo_progress_data(
            progress=progress,
            title=title,
            subtitle=subtitle,
            total=total,
            eta=eta,
            rate=rate,
            request_options=request_options,
        )
        return _response.data

    def read_marimo_radio_data(self, *, request_options: typing.Optional[RequestOptions] = None) -> MarimoRadioData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoRadioData
            marimo-radio data accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.read_marimo_radio_data()
        """
        _response = self._raw_client.read_marimo_radio_data(request_options=request_options)
        return _response.data

    def write_marimo_radio_data(
        self,
        *,
        options: typing.Sequence[str],
        initial_value: typing.Optional[str] = OMIT,
        inline: typing.Optional[bool] = OMIT,
        label: typing.Optional[str] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.write_marimo_radio_data(
            options=["options"],
        )
        """
        _response = self._raw_client.write_marimo_radio_data(
            options=options,
            initial_value=initial_value,
            inline=inline,
            label=label,
            disabled=disabled,
            request_options=request_options,
        )
        return _response.data

    def read_marimo_range_slider_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoRangeSliderData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoRangeSliderData
            marimo-range-slider data accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.read_marimo_range_slider_data()
        """
        _response = self._raw_client.read_marimo_range_slider_data(request_options=request_options)
        return _response.data

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
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.write_marimo_range_slider_data(
            initial_value=[1.1],
            start=1.1,
            stop=1.1,
        )
        """
        _response = self._raw_client.write_marimo_range_slider_data(
            initial_value=initial_value,
            start=start,
            stop=stop,
            label=label,
            step=step,
            steps=steps,
            debounce=debounce,
            orientation=orientation,
            show_value=show_value,
            full_width=full_width,
            disabled=disabled,
            request_options=request_options,
        )
        return _response.data

    def read_marimo_refresh_data(self, *, request_options: typing.Optional[RequestOptions] = None) -> MarimoRefreshData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoRefreshData
            marimo-refresh data accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.read_marimo_refresh_data()
        """
        _response = self._raw_client.read_marimo_refresh_data(request_options=request_options)
        return _response.data

    def write_marimo_refresh_data(
        self,
        *,
        options: typing.Optional[typing.Sequence[MarimoRefreshDataOptionsItem]] = OMIT,
        default_interval: typing.Optional[MarimoRefreshDataDefaultInterval] = OMIT,
        label: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.write_marimo_refresh_data()
        """
        _response = self._raw_client.write_marimo_refresh_data(
            options=options, default_interval=default_interval, label=label, request_options=request_options
        )
        return _response.data

    def read_marimo_routes_data(self, *, request_options: typing.Optional[RequestOptions] = None) -> MarimoRoutesData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoRoutesData
            marimo-routes data accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.read_marimo_routes_data()
        """
        _response = self._raw_client.read_marimo_routes_data(request_options=request_options)
        return _response.data

    def write_marimo_routes_data(
        self, *, routes: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        routes : typing.Sequence[str]

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
        client.plugin_data.write_marimo_routes_data(
            routes=["routes"],
        )
        """
        _response = self._raw_client.write_marimo_routes_data(routes=routes, request_options=request_options)
        return _response.data

    def read_marimo_slider_data(self, *, request_options: typing.Optional[RequestOptions] = None) -> MarimoSliderData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoSliderData
            marimo-slider data accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.read_marimo_slider_data()
        """
        _response = self._raw_client.read_marimo_slider_data(request_options=request_options)
        return _response.data

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
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.write_marimo_slider_data(
            initial_value=1.1,
            start=1.1,
            stop=1.1,
        )
        """
        _response = self._raw_client.write_marimo_slider_data(
            initial_value=initial_value,
            start=start,
            stop=stop,
            label=label,
            step=step,
            steps=steps,
            debounce=debounce,
            orientation=orientation,
            show_value=show_value,
            full_width=full_width,
            include_input=include_input,
            disabled=disabled,
            request_options=request_options,
        )
        return _response.data

    def read_marimo_stat_data(self, *, request_options: typing.Optional[RequestOptions] = None) -> MarimoStatData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoStatData
            marimo-stat data accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.read_marimo_stat_data()
        """
        _response = self._raw_client.read_marimo_stat_data(request_options=request_options)
        return _response.data

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
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.write_marimo_stat_data()
        """
        _response = self._raw_client.write_marimo_stat_data(
            value=value,
            label=label,
            caption=caption,
            bordered=bordered,
            direction=direction,
            target_direction=target_direction,
            slot=slot,
            request_options=request_options,
        )
        return _response.data

    def read_marimo_switch_data(self, *, request_options: typing.Optional[RequestOptions] = None) -> MarimoSwitchData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoSwitchData
            marimo-switch data accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.read_marimo_switch_data()
        """
        _response = self._raw_client.read_marimo_switch_data(request_options=request_options)
        return _response.data

    def write_marimo_switch_data(
        self,
        *,
        initial_value: bool,
        label: typing.Optional[str] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.write_marimo_switch_data(
            initial_value=True,
        )
        """
        _response = self._raw_client.write_marimo_switch_data(
            initial_value=initial_value, label=label, disabled=disabled, request_options=request_options
        )
        return _response.data

    def read_marimo_table_data(self, *, request_options: typing.Optional[RequestOptions] = None) -> MarimoTableData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoTableData
            marimo-table data accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.read_marimo_table_data()
        """
        _response = self._raw_client.read_marimo_table_data(request_options=request_options)
        return _response.data

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
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi, MarimoTableDataTotalRowsOne

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.write_marimo_table_data(
            initial_value=[1.1],
            data="data",
            total_rows=MarimoTableDataTotalRowsOne.TOO_MANY,
            row_headers=[[]],
            total_columns=1.1,
        )
        """
        _response = self._raw_client.write_marimo_table_data(
            initial_value=initial_value,
            data=data,
            total_rows=total_rows,
            row_headers=row_headers,
            total_columns=total_columns,
            label=label,
            raw_data=raw_data,
            pagination=pagination,
            page_size=page_size,
            selection=selection,
            show_download=show_download,
            show_filters=show_filters,
            show_column_summaries=show_column_summaries,
            show_data_types=show_data_types,
            show_page_size_selector=show_page_size_selector,
            show_column_explorer=show_column_explorer,
            show_row_explorer=show_row_explorer,
            show_chart_builder=show_chart_builder,
            show_search=show_search,
            freeze_columns_left=freeze_columns_left,
            freeze_columns_right=freeze_columns_right,
            hidden_columns=hidden_columns,
            text_justify_columns=text_justify_columns,
            wrapped_columns=wrapped_columns,
            column_widths=column_widths,
            header_tooltip=header_tooltip,
            field_types=field_types,
            max_columns=max_columns,
            has_stable_row_id=has_stable_row_id,
            max_height=max_height,
            cell_styles=cell_styles,
            hover_template=hover_template,
            cell_hover_texts=cell_hover_texts,
            lazy=lazy,
            preload=preload,
            request_options=request_options,
        )
        return _response.data

    def read_marimo_tabs_data(self, *, request_options: typing.Optional[RequestOptions] = None) -> MarimoTabsData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoTabsData
            marimo-tabs data accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.read_marimo_tabs_data()
        """
        _response = self._raw_client.read_marimo_tabs_data(request_options=request_options)
        return _response.data

    def write_marimo_tabs_data(
        self,
        *,
        tabs: typing.Sequence[str],
        label: typing.Optional[str] = OMIT,
        orientation: typing.Optional[MarimoTabsDataOrientation] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.write_marimo_tabs_data(
            tabs=["tabs"],
        )
        """
        _response = self._raw_client.write_marimo_tabs_data(
            tabs=tabs, label=label, orientation=orientation, request_options=request_options
        )
        return _response.data

    def read_marimo_tex_data(self, *, request_options: typing.Optional[RequestOptions] = None) -> MarimoTexData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoTexData
            marimo-tex data accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.read_marimo_tex_data()
        """
        _response = self._raw_client.read_marimo_tex_data(request_options=request_options)
        return _response.data

    def write_marimo_tex_data(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.plugin_data.write_marimo_tex_data()
        """
        _response = self._raw_client.write_marimo_tex_data(request_options=request_options)
        return _response.data

    def read_marimo_text_data(self, *, request_options: typing.Optional[RequestOptions] = None) -> MarimoTextData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoTextData
            marimo-text data accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.read_marimo_text_data()
        """
        _response = self._raw_client.read_marimo_text_data(request_options=request_options)
        return _response.data

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
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.write_marimo_text_data(
            initial_value="initialValue",
            placeholder="placeholder",
        )
        """
        _response = self._raw_client.write_marimo_text_data(
            initial_value=initial_value,
            placeholder=placeholder,
            label=label,
            kind=kind,
            max_length=max_length,
            min_length=min_length,
            full_width=full_width,
            disabled=disabled,
            debounce=debounce,
            password_has_value=password_has_value,
            request_options=request_options,
        )
        return _response.data

    def read_marimo_text_area_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoTextAreaData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoTextAreaData
            marimo-text-area data accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.read_marimo_text_area_data()
        """
        _response = self._raw_client.read_marimo_text_area_data(request_options=request_options)
        return _response.data

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
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.write_marimo_text_area_data(
            initial_value="initialValue",
            placeholder="placeholder",
        )
        """
        _response = self._raw_client.write_marimo_text_area_data(
            initial_value=initial_value,
            placeholder=placeholder,
            label=label,
            max_length=max_length,
            min_length=min_length,
            disabled=disabled,
            debounce=debounce,
            rows=rows,
            full_width=full_width,
            request_options=request_options,
        )
        return _response.data

    def read_marimo_vega_data(self, *, request_options: typing.Optional[RequestOptions] = None) -> MarimoVegaData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoVegaData
            marimo-vega data accepted by a plugin consumer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.read_marimo_vega_data()
        """
        _response = self._raw_client.read_marimo_vega_data(request_options=request_options)
        return _response.data

    def write_marimo_vega_data(
        self,
        *,
        spec: typing.Dict[str, typing.Any],
        chart_selection: typing.Optional[MarimoVegaDataChartSelection] = OMIT,
        field_selection: typing.Optional[MarimoVegaDataFieldSelection] = OMIT,
        embed_options: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugin_data.write_marimo_vega_data(
            spec={"key": "value"},
        )
        """
        _response = self._raw_client.write_marimo_vega_data(
            spec=spec,
            chart_selection=chart_selection,
            field_selection=field_selection,
            embed_options=embed_options,
            request_options=request_options,
        )
        return _response.data


class AsyncPluginDataClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPluginDataClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPluginDataClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPluginDataClient
        """
        return self._raw_client

    async def read_marimo_accordion_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoAccordionData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoAccordionData
            marimo-accordion data accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.read_marimo_accordion_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_accordion_data(request_options=request_options)
        return _response.data

    async def write_marimo_accordion_data(
        self,
        *,
        labels: typing.Sequence[str],
        multiple: bool,
        expanded: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.write_marimo_accordion_data(
                labels=["labels"],
                multiple=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_accordion_data(
            labels=labels, multiple=multiple, expanded=expanded, request_options=request_options
        )
        return _response.data

    async def read_marimo_anywidget_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoAnywidgetData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoAnywidgetData
            marimo-anywidget data accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.read_marimo_anywidget_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_anywidget_data(request_options=request_options)
        return _response.data

    async def write_marimo_anywidget_data(
        self, *, model_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        model_id : str

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
            await client.plugin_data.write_marimo_anywidget_data(
                model_id="modelId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_anywidget_data(
            model_id=model_id, request_options=request_options
        )
        return _response.data

    async def read_marimo_button_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoButtonData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoButtonData
            marimo-button data accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.read_marimo_button_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_button_data(request_options=request_options)
        return _response.data

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
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.write_marimo_button_data(
                label="label",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_button_data(
            label=label,
            kind=kind,
            disabled=disabled,
            full_width=full_width,
            tooltip=tooltip,
            keyboard_shortcut=keyboard_shortcut,
            request_options=request_options,
        )
        return _response.data

    async def read_marimo_callout_output_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoCalloutOutputData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoCalloutOutputData
            marimo-callout-output data accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.read_marimo_callout_output_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_callout_output_data(request_options=request_options)
        return _response.data

    async def write_marimo_callout_output_data(
        self,
        *,
        html: str,
        kind: typing.Optional[MarimoCalloutOutputDataKind] = OMIT,
        title: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.write_marimo_callout_output_data(
                html="html",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_callout_output_data(
            html=html, kind=kind, title=title, request_options=request_options
        )
        return _response.data

    async def read_marimo_carousel_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoCarouselData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoCarouselData
            marimo-carousel data accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.read_marimo_carousel_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_carousel_data(request_options=request_options)
        return _response.data

    async def write_marimo_carousel_data(
        self,
        *,
        index: typing.Optional[str] = OMIT,
        height: typing.Optional[MarimoCarouselDataHeight] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        index : typing.Optional[str]

        height : typing.Optional[MarimoCarouselDataHeight]

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
            await client.plugin_data.write_marimo_carousel_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_carousel_data(
            index=index, height=height, request_options=request_options
        )
        return _response.data

    async def read_marimo_chatbot_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoChatbotData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoChatbotData
            marimo-chatbot data accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.read_marimo_chatbot_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_chatbot_data(request_options=request_options)
        return _response.data

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
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, MarimoChatbotDataConfig

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.write_marimo_chatbot_data(
                show_configuration_controls=True,
                config=MarimoChatbotDataConfig(),
                allow_attachments=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_chatbot_data(
            show_configuration_controls=show_configuration_controls,
            config=config,
            allow_attachments=allow_attachments,
            prompts=prompts,
            max_height=max_height,
            disabled=disabled,
            request_options=request_options,
        )
        return _response.data

    async def read_marimo_checkbox_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoCheckboxData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoCheckboxData
            marimo-checkbox data accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.read_marimo_checkbox_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_checkbox_data(request_options=request_options)
        return _response.data

    async def write_marimo_checkbox_data(
        self,
        *,
        initial_value: bool,
        label: typing.Optional[str] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.write_marimo_checkbox_data(
                initial_value=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_checkbox_data(
            initial_value=initial_value, label=label, disabled=disabled, request_options=request_options
        )
        return _response.data

    async def read_marimo_code_editor_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoCodeEditorData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoCodeEditorData
            marimo-code-editor data accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.read_marimo_code_editor_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_code_editor_data(request_options=request_options)
        return _response.data

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
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.write_marimo_code_editor_data(
                initial_value="initialValue",
                placeholder="placeholder",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_code_editor_data(
            initial_value=initial_value,
            placeholder=placeholder,
            language=language,
            theme=theme,
            label=label,
            disabled=disabled,
            min_height=min_height,
            max_height=max_height,
            show_copy_button=show_copy_button,
            debounce=debounce,
            request_options=request_options,
        )
        return _response.data

    async def read_marimo_data_editor_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoDataEditorData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoDataEditorData
            marimo-data-editor data accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.read_marimo_data_editor_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_data_editor_data(request_options=request_options)
        return _response.data

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
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            MarimoDataEditorDataEditableColumnsOne,
            MarimoDataEditorDataInitialValue,
        )

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.write_marimo_data_editor_data(
                initial_value=MarimoDataEditorDataInitialValue(
                    edits=[],
                ),
                data="data",
                editable_columns=MarimoDataEditorDataEditableColumnsOne.ALL,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_data_editor_data(
            initial_value=initial_value,
            data=data,
            editable_columns=editable_columns,
            label=label,
            field_types=field_types,
            column_names=column_names,
            column_sizing_mode=column_sizing_mode,
            request_options=request_options,
        )
        return _response.data

    async def read_marimo_data_explorer_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoDataExplorerData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoDataExplorerData
            marimo-data-explorer data accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.read_marimo_data_explorer_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_data_explorer_data(request_options=request_options)
        return _response.data

    async def write_marimo_data_explorer_data(
        self, *, data: str, label: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        data : str

        label : typing.Optional[str]

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
            await client.plugin_data.write_marimo_data_explorer_data(
                data="data",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_data_explorer_data(
            data=data, label=label, request_options=request_options
        )
        return _response.data

    async def read_marimo_dataframe_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoDataframeData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoDataframeData
            marimo-dataframe data accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.read_marimo_dataframe_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_dataframe_data(request_options=request_options)
        return _response.data

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
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.write_marimo_dataframe_data(
                columns=[[]],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_dataframe_data(
            columns=columns,
            label=label,
            page_size=page_size,
            show_download=show_download,
            dataframe_name=dataframe_name,
            lazy=lazy,
            request_options=request_options,
        )
        return _response.data

    async def read_marimo_date_data(self, *, request_options: typing.Optional[RequestOptions] = None) -> MarimoDateData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoDateData
            marimo-date data accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.read_marimo_date_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_date_data(request_options=request_options)
        return _response.data

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
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.write_marimo_date_data(
                initial_value="initialValue",
                start="start",
                stop="stop",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_date_data(
            initial_value=initial_value,
            start=start,
            stop=stop,
            label=label,
            step=step,
            full_width=full_width,
            disabled=disabled,
            request_options=request_options,
        )
        return _response.data

    async def read_marimo_date_range_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoDateRangeData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoDateRangeData
            marimo-date-range data accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.read_marimo_date_range_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_date_range_data(request_options=request_options)
        return _response.data

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
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.write_marimo_date_range_data(
                initial_value=[],
                start="start",
                stop="stop",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_date_range_data(
            initial_value=initial_value,
            start=start,
            stop=stop,
            label=label,
            step=step,
            full_width=full_width,
            disabled=disabled,
            request_options=request_options,
        )
        return _response.data

    async def read_marimo_datetime_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoDatetimeData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoDatetimeData
            marimo-datetime data accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.read_marimo_datetime_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_datetime_data(request_options=request_options)
        return _response.data

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
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.write_marimo_datetime_data(
                initial_value="initialValue",
                start="start",
                stop="stop",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_datetime_data(
            initial_value=initial_value,
            start=start,
            stop=stop,
            label=label,
            step=step,
            precision=precision,
            full_width=full_width,
            disabled=disabled,
            request_options=request_options,
        )
        return _response.data

    async def read_marimo_dict_data(self, *, request_options: typing.Optional[RequestOptions] = None) -> MarimoDictData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoDictData
            marimo-dict data accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.read_marimo_dict_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_dict_data(request_options=request_options)
        return _response.data

    async def write_marimo_dict_data(
        self,
        *,
        element_ids: typing.Dict[str, str],
        label: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        element_ids : typing.Dict[str, str]

        label : typing.Optional[str]

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
            await client.plugin_data.write_marimo_dict_data(
                element_ids={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_dict_data(
            element_ids=element_ids, label=label, request_options=request_options
        )
        return _response.data

    async def read_marimo_download_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoDownloadData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoDownloadData
            marimo-download data accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.read_marimo_download_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_download_data(request_options=request_options)
        return _response.data

    async def write_marimo_download_data(
        self,
        *,
        data: str,
        disabled: typing.Optional[bool] = OMIT,
        filename: typing.Optional[str] = OMIT,
        label: typing.Optional[str] = OMIT,
        lazy: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.write_marimo_download_data(
                data="data",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_download_data(
            data=data, disabled=disabled, filename=filename, label=label, lazy=lazy, request_options=request_options
        )
        return _response.data

    async def read_marimo_dropdown_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoDropdownData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoDropdownData
            marimo-dropdown data accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.read_marimo_dropdown_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_dropdown_data(request_options=request_options)
        return _response.data

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
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.write_marimo_dropdown_data(
                initial_value=["initialValue"],
                options=["options"],
                allow_select_none=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_dropdown_data(
            initial_value=initial_value,
            options=options,
            allow_select_none=allow_select_none,
            label=label,
            full_width=full_width,
            searchable=searchable,
            disabled=disabled,
            request_options=request_options,
        )
        return _response.data

    async def read_marimo_file_data(self, *, request_options: typing.Optional[RequestOptions] = None) -> MarimoFileData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoFileData
            marimo-file data accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.read_marimo_file_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_file_data(request_options=request_options)
        return _response.data

    async def write_marimo_file_data(
        self,
        *,
        filetypes: typing.Sequence[str],
        multiple: bool,
        kind: MarimoFileDataKind,
        max_size: float,
        label: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, MarimoFileDataKind

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.write_marimo_file_data(
                filetypes=["filetypes"],
                multiple=True,
                kind=MarimoFileDataKind.BUTTON,
                max_size=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_file_data(
            filetypes=filetypes,
            multiple=multiple,
            kind=kind,
            max_size=max_size,
            label=label,
            request_options=request_options,
        )
        return _response.data

    async def read_marimo_file_browser_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoFileBrowserData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoFileBrowserData
            marimo-file-browser data accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.read_marimo_file_browser_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_file_browser_data(request_options=request_options)
        return _response.data

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
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.write_marimo_file_browser_data(
                initial_path="initialPath",
                filetypes=["filetypes"],
                selection_mode="selectionMode",
                multiple=True,
                restrict_navigation=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_file_browser_data(
            initial_path=initial_path,
            filetypes=filetypes,
            selection_mode=selection_mode,
            multiple=multiple,
            restrict_navigation=restrict_navigation,
            label=label,
            request_options=request_options,
        )
        return _response.data

    async def read_marimo_form_data(self, *, request_options: typing.Optional[RequestOptions] = None) -> MarimoFormData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoFormData
            marimo-form data accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.read_marimo_form_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_form_data(request_options=request_options)
        return _response.data

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
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.write_marimo_form_data(
                element_id="elementId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_form_data(
            element_id=element_id,
            label=label,
            bordered=bordered,
            loading=loading,
            submit_button_label=submit_button_label,
            submit_button_tooltip=submit_button_tooltip,
            submit_button_disabled=submit_button_disabled,
            clear_on_submit=clear_on_submit,
            show_clear_button=show_clear_button,
            clear_button_label=clear_button_label,
            clear_button_tooltip=clear_button_tooltip,
            should_validate=should_validate,
            request_options=request_options,
        )
        return _response.data

    async def read_marimo_image_comparison_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoImageComparisonData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoImageComparisonData
            marimo-image-comparison data accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.read_marimo_image_comparison_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_image_comparison_data(request_options=request_options)
        return _response.data

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
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.write_marimo_image_comparison_data(
                before_src="beforeSrc",
                after_src="afterSrc",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_image_comparison_data(
            before_src=before_src,
            after_src=after_src,
            value=value,
            direction=direction,
            width=width,
            height=height,
            request_options=request_options,
        )
        return _response.data

    async def read_marimo_json_output_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoJsonOutputData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoJsonOutputData
            marimo-json-output data accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.read_marimo_json_output_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_json_output_data(request_options=request_options)
        return _response.data

    async def write_marimo_json_output_data(
        self,
        *,
        json_data: typing.Any,
        name: typing.Optional[str] = OMIT,
        value_types: typing.Optional[MarimoJsonOutputDataValueTypes] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.write_marimo_json_output_data(
                json_data={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_json_output_data(
            json_data=json_data, name=name, value_types=value_types, request_options=request_options
        )
        return _response.data

    async def read_marimo_lazy_data(self, *, request_options: typing.Optional[RequestOptions] = None) -> MarimoLazyData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoLazyData
            marimo-lazy data accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.read_marimo_lazy_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_lazy_data(request_options=request_options)
        return _response.data

    async def write_marimo_lazy_data(
        self,
        *,
        show_loading_indicator: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        show_loading_indicator : typing.Optional[bool]

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
            await client.plugin_data.write_marimo_lazy_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_lazy_data(
            show_loading_indicator=show_loading_indicator, request_options=request_options
        )
        return _response.data

    async def read_marimo_matplotlib_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoMatplotlibData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoMatplotlibData
            marimo-matplotlib data accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.read_marimo_matplotlib_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_matplotlib_data(request_options=request_options)
        return _response.data

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
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.write_marimo_matplotlib_data(
                chart_base64="chartBase64",
                x_bounds=[],
                y_bounds=[],
                axes_pixel_bounds=[],
                width=1.1,
                height=1.1,
                debounce=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_matplotlib_data(
            chart_base64=chart_base64,
            x_bounds=x_bounds,
            y_bounds=y_bounds,
            axes_pixel_bounds=axes_pixel_bounds,
            width=width,
            height=height,
            debounce=debounce,
            selection_color=selection_color,
            selection_opacity=selection_opacity,
            stroke_width=stroke_width,
            x_scale=x_scale,
            y_scale=y_scale,
            request_options=request_options,
        )
        return _response.data

    async def read_marimo_matrix_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoMatrixData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoMatrixData
            marimo-matrix data accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.read_marimo_matrix_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_matrix_data(request_options=request_options)
        return _response.data

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
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.write_marimo_matrix_data(
                initial_value=[[1.1]],
                step=[[1.1]],
                precision=1.1,
                symmetric=True,
                scientific=True,
                disabled=[[True]],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_matrix_data(
            initial_value=initial_value,
            step=step,
            precision=precision,
            symmetric=symmetric,
            scientific=scientific,
            disabled=disabled,
            label=label,
            min_value=min_value,
            max_value=max_value,
            row_labels=row_labels,
            column_labels=column_labels,
            debounce=debounce,
            request_options=request_options,
        )
        return _response.data

    async def read_marimo_mermaid_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoMermaidData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoMermaidData
            marimo-mermaid data accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.read_marimo_mermaid_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_mermaid_data(request_options=request_options)
        return _response.data

    async def write_marimo_mermaid_data(
        self,
        *,
        diagram: str,
        theme: typing.Optional[str] = OMIT,
        theme_variables: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.write_marimo_mermaid_data(
                diagram="diagram",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_mermaid_data(
            diagram=diagram, theme=theme, theme_variables=theme_variables, request_options=request_options
        )
        return _response.data

    async def read_marimo_microphone_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoMicrophoneData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoMicrophoneData
            marimo-microphone data accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.read_marimo_microphone_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_microphone_data(request_options=request_options)
        return _response.data

    async def write_marimo_microphone_data(
        self, *, label: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        label : typing.Optional[str]

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
            await client.plugin_data.write_marimo_microphone_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_microphone_data(label=label, request_options=request_options)
        return _response.data

    async def read_marimo_mime_renderer_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoMimeRendererData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoMimeRendererData
            marimo-mime-renderer data accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.read_marimo_mime_renderer_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_mime_renderer_data(request_options=request_options)
        return _response.data

    async def write_marimo_mime_renderer_data(
        self,
        *,
        mime: str,
        data: typing.Optional[MarimoMimeRendererDataData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        mime : str

        data : typing.Optional[MarimoMimeRendererDataData]

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
            await client.plugin_data.write_marimo_mime_renderer_data(
                mime="mime",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_mime_renderer_data(
            mime=mime, data=data, request_options=request_options
        )
        return _response.data

    async def read_marimo_mpl_interactive_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoMplInteractiveData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoMplInteractiveData
            marimo-mpl-interactive data accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.read_marimo_mpl_interactive_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_mpl_interactive_data(request_options=request_options)
        return _response.data

    async def write_marimo_mpl_interactive_data(
        self,
        *,
        mpl_js_url: str,
        css_url: str,
        toolbar_images: typing.Dict[str, str],
        width: float,
        height: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.write_marimo_mpl_interactive_data(
                mpl_js_url="mplJsUrl",
                css_url="cssUrl",
                toolbar_images={"key": "value"},
                width=1.1,
                height=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_mpl_interactive_data(
            mpl_js_url=mpl_js_url,
            css_url=css_url,
            toolbar_images=toolbar_images,
            width=width,
            height=height,
            request_options=request_options,
        )
        return _response.data

    async def read_marimo_multiselect_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoMultiselectData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoMultiselectData
            marimo-multiselect data accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.read_marimo_multiselect_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_multiselect_data(request_options=request_options)
        return _response.data

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
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.write_marimo_multiselect_data(
                initial_value=["initialValue"],
                options=["options"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_multiselect_data(
            initial_value=initial_value,
            options=options,
            label=label,
            full_width=full_width,
            max_selections=max_selections,
            disabled=disabled,
            request_options=request_options,
        )
        return _response.data

    async def read_marimo_nav_menu_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoNavMenuData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoNavMenuData
            marimo-nav-menu data accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.read_marimo_nav_menu_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_nav_menu_data(request_options=request_options)
        return _response.data

    async def write_marimo_nav_menu_data(
        self,
        *,
        items: typing.Sequence[MarimoNavMenuDataItemsItem],
        orientation: MarimoNavMenuDataOrientation,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        items : typing.Sequence[MarimoNavMenuDataItemsItem]

        orientation : MarimoNavMenuDataOrientation

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
            MarimoNavMenuDataItemsItemDescription,
            MarimoNavMenuDataOrientation,
        )

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.write_marimo_nav_menu_data(
                items=[
                    MarimoNavMenuDataItemsItemDescription(
                        label="label",
                        href="href",
                    )
                ],
                orientation=MarimoNavMenuDataOrientation.HORIZONTAL,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_nav_menu_data(
            items=items, orientation=orientation, request_options=request_options
        )
        return _response.data

    async def read_marimo_number_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoNumberData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoNumberData
            marimo-number data accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.read_marimo_number_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_number_data(request_options=request_options)
        return _response.data

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
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.write_marimo_number_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_number_data(
            initial_value=initial_value,
            label=label,
            start=start,
            stop=stop,
            step=step,
            debounce=debounce,
            full_width=full_width,
            disabled=disabled,
            request_options=request_options,
        )
        return _response.data

    async def read_marimo_outline_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoOutlineData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoOutlineData
            marimo-outline data accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.read_marimo_outline_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_outline_data(request_options=request_options)
        return _response.data

    async def write_marimo_outline_data(
        self, *, label: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        label : typing.Optional[str]

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
            await client.plugin_data.write_marimo_outline_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_outline_data(label=label, request_options=request_options)
        return _response.data

    async def read_marimo_panel_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoPanelData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoPanelData
            marimo-panel data accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.read_marimo_panel_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_panel_data(request_options=request_options)
        return _response.data

    async def write_marimo_panel_data(
        self,
        *,
        docs_json: typing.Dict[str, typing.Any],
        render_json: MarimoPanelDataRenderJson,
        extension_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, MarimoPanelDataRenderJson

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.write_marimo_panel_data(
                docs_json={"key": "value"},
                render_json=MarimoPanelDataRenderJson(
                    roots={"key": "value"},
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_panel_data(
            docs_json=docs_json, render_json=render_json, extension_url=extension_url, request_options=request_options
        )
        return _response.data

    async def read_marimo_plotly_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoPlotlyData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoPlotlyData
            marimo-plotly data accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.read_marimo_plotly_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_plotly_data(request_options=request_options)
        return _response.data

    async def write_marimo_plotly_data(
        self,
        *,
        figure: typing.Dict[str, typing.Any],
        config: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        figure : typing.Dict[str, typing.Any]

        config : typing.Dict[str, typing.Any]

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
            await client.plugin_data.write_marimo_plotly_data(
                figure={"key": "value"},
                config={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_plotly_data(
            figure=figure, config=config, request_options=request_options
        )
        return _response.data

    async def read_marimo_progress_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoProgressData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoProgressData
            marimo-progress data accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.read_marimo_progress_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_progress_data(request_options=request_options)
        return _response.data

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
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.write_marimo_progress_data(
                progress=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_progress_data(
            progress=progress,
            title=title,
            subtitle=subtitle,
            total=total,
            eta=eta,
            rate=rate,
            request_options=request_options,
        )
        return _response.data

    async def read_marimo_radio_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoRadioData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoRadioData
            marimo-radio data accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.read_marimo_radio_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_radio_data(request_options=request_options)
        return _response.data

    async def write_marimo_radio_data(
        self,
        *,
        options: typing.Sequence[str],
        initial_value: typing.Optional[str] = OMIT,
        inline: typing.Optional[bool] = OMIT,
        label: typing.Optional[str] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.write_marimo_radio_data(
                options=["options"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_radio_data(
            options=options,
            initial_value=initial_value,
            inline=inline,
            label=label,
            disabled=disabled,
            request_options=request_options,
        )
        return _response.data

    async def read_marimo_range_slider_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoRangeSliderData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoRangeSliderData
            marimo-range-slider data accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.read_marimo_range_slider_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_range_slider_data(request_options=request_options)
        return _response.data

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
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.write_marimo_range_slider_data(
                initial_value=[1.1],
                start=1.1,
                stop=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_range_slider_data(
            initial_value=initial_value,
            start=start,
            stop=stop,
            label=label,
            step=step,
            steps=steps,
            debounce=debounce,
            orientation=orientation,
            show_value=show_value,
            full_width=full_width,
            disabled=disabled,
            request_options=request_options,
        )
        return _response.data

    async def read_marimo_refresh_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoRefreshData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoRefreshData
            marimo-refresh data accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.read_marimo_refresh_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_refresh_data(request_options=request_options)
        return _response.data

    async def write_marimo_refresh_data(
        self,
        *,
        options: typing.Optional[typing.Sequence[MarimoRefreshDataOptionsItem]] = OMIT,
        default_interval: typing.Optional[MarimoRefreshDataDefaultInterval] = OMIT,
        label: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.write_marimo_refresh_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_refresh_data(
            options=options, default_interval=default_interval, label=label, request_options=request_options
        )
        return _response.data

    async def read_marimo_routes_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoRoutesData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoRoutesData
            marimo-routes data accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.read_marimo_routes_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_routes_data(request_options=request_options)
        return _response.data

    async def write_marimo_routes_data(
        self, *, routes: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        routes : typing.Sequence[str]

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
            await client.plugin_data.write_marimo_routes_data(
                routes=["routes"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_routes_data(routes=routes, request_options=request_options)
        return _response.data

    async def read_marimo_slider_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoSliderData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoSliderData
            marimo-slider data accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.read_marimo_slider_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_slider_data(request_options=request_options)
        return _response.data

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
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.write_marimo_slider_data(
                initial_value=1.1,
                start=1.1,
                stop=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_slider_data(
            initial_value=initial_value,
            start=start,
            stop=stop,
            label=label,
            step=step,
            steps=steps,
            debounce=debounce,
            orientation=orientation,
            show_value=show_value,
            full_width=full_width,
            include_input=include_input,
            disabled=disabled,
            request_options=request_options,
        )
        return _response.data

    async def read_marimo_stat_data(self, *, request_options: typing.Optional[RequestOptions] = None) -> MarimoStatData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoStatData
            marimo-stat data accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.read_marimo_stat_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_stat_data(request_options=request_options)
        return _response.data

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
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.write_marimo_stat_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_stat_data(
            value=value,
            label=label,
            caption=caption,
            bordered=bordered,
            direction=direction,
            target_direction=target_direction,
            slot=slot,
            request_options=request_options,
        )
        return _response.data

    async def read_marimo_switch_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoSwitchData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoSwitchData
            marimo-switch data accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.read_marimo_switch_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_switch_data(request_options=request_options)
        return _response.data

    async def write_marimo_switch_data(
        self,
        *,
        initial_value: bool,
        label: typing.Optional[str] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.write_marimo_switch_data(
                initial_value=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_switch_data(
            initial_value=initial_value, label=label, disabled=disabled, request_options=request_options
        )
        return _response.data

    async def read_marimo_table_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoTableData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoTableData
            marimo-table data accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.read_marimo_table_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_table_data(request_options=request_options)
        return _response.data

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
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, MarimoTableDataTotalRowsOne

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.write_marimo_table_data(
                initial_value=[1.1],
                data="data",
                total_rows=MarimoTableDataTotalRowsOne.TOO_MANY,
                row_headers=[[]],
                total_columns=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_table_data(
            initial_value=initial_value,
            data=data,
            total_rows=total_rows,
            row_headers=row_headers,
            total_columns=total_columns,
            label=label,
            raw_data=raw_data,
            pagination=pagination,
            page_size=page_size,
            selection=selection,
            show_download=show_download,
            show_filters=show_filters,
            show_column_summaries=show_column_summaries,
            show_data_types=show_data_types,
            show_page_size_selector=show_page_size_selector,
            show_column_explorer=show_column_explorer,
            show_row_explorer=show_row_explorer,
            show_chart_builder=show_chart_builder,
            show_search=show_search,
            freeze_columns_left=freeze_columns_left,
            freeze_columns_right=freeze_columns_right,
            hidden_columns=hidden_columns,
            text_justify_columns=text_justify_columns,
            wrapped_columns=wrapped_columns,
            column_widths=column_widths,
            header_tooltip=header_tooltip,
            field_types=field_types,
            max_columns=max_columns,
            has_stable_row_id=has_stable_row_id,
            max_height=max_height,
            cell_styles=cell_styles,
            hover_template=hover_template,
            cell_hover_texts=cell_hover_texts,
            lazy=lazy,
            preload=preload,
            request_options=request_options,
        )
        return _response.data

    async def read_marimo_tabs_data(self, *, request_options: typing.Optional[RequestOptions] = None) -> MarimoTabsData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoTabsData
            marimo-tabs data accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.read_marimo_tabs_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_tabs_data(request_options=request_options)
        return _response.data

    async def write_marimo_tabs_data(
        self,
        *,
        tabs: typing.Sequence[str],
        label: typing.Optional[str] = OMIT,
        orientation: typing.Optional[MarimoTabsDataOrientation] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.write_marimo_tabs_data(
                tabs=["tabs"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_tabs_data(
            tabs=tabs, label=label, orientation=orientation, request_options=request_options
        )
        return _response.data

    async def read_marimo_tex_data(self, *, request_options: typing.Optional[RequestOptions] = None) -> MarimoTexData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoTexData
            marimo-tex data accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.read_marimo_tex_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_tex_data(request_options=request_options)
        return _response.data

    async def write_marimo_tex_data(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.plugin_data.write_marimo_tex_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_tex_data(request_options=request_options)
        return _response.data

    async def read_marimo_text_data(self, *, request_options: typing.Optional[RequestOptions] = None) -> MarimoTextData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoTextData
            marimo-text data accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.read_marimo_text_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_text_data(request_options=request_options)
        return _response.data

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
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.write_marimo_text_data(
                initial_value="initialValue",
                placeholder="placeholder",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_text_data(
            initial_value=initial_value,
            placeholder=placeholder,
            label=label,
            kind=kind,
            max_length=max_length,
            min_length=min_length,
            full_width=full_width,
            disabled=disabled,
            debounce=debounce,
            password_has_value=password_has_value,
            request_options=request_options,
        )
        return _response.data

    async def read_marimo_text_area_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarimoTextAreaData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoTextAreaData
            marimo-text-area data accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.read_marimo_text_area_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_text_area_data(request_options=request_options)
        return _response.data

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
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.write_marimo_text_area_data(
                initial_value="initialValue",
                placeholder="placeholder",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_text_area_data(
            initial_value=initial_value,
            placeholder=placeholder,
            label=label,
            max_length=max_length,
            min_length=min_length,
            disabled=disabled,
            debounce=debounce,
            rows=rows,
            full_width=full_width,
            request_options=request_options,
        )
        return _response.data

    async def read_marimo_vega_data(self, *, request_options: typing.Optional[RequestOptions] = None) -> MarimoVegaData:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarimoVegaData
            marimo-vega data accepted by a plugin consumer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.read_marimo_vega_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_marimo_vega_data(request_options=request_options)
        return _response.data

    async def write_marimo_vega_data(
        self,
        *,
        spec: typing.Dict[str, typing.Any],
        chart_selection: typing.Optional[MarimoVegaDataChartSelection] = OMIT,
        field_selection: typing.Optional[MarimoVegaDataFieldSelection] = OMIT,
        embed_options: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugin_data.write_marimo_vega_data(
                spec={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_marimo_vega_data(
            spec=spec,
            chart_selection=chart_selection,
            field_selection=field_selection,
            embed_options=embed_options,
            request_options=request_options,
        )
        return _response.data
