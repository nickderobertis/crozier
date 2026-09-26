



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .marimo_accordion_data import MarimoAccordionData
    from .marimo_anywidget_data import MarimoAnywidgetData
    from .marimo_button_data import MarimoButtonData
    from .marimo_button_data_kind import MarimoButtonDataKind
    from .marimo_callout_output_data import MarimoCalloutOutputData
    from .marimo_callout_output_data_kind import MarimoCalloutOutputDataKind
    from .marimo_carousel_data import MarimoCarouselData
    from .marimo_carousel_data_height import MarimoCarouselDataHeight
    from .marimo_chatbot_cancel_prompt_input import MarimoChatbotCancelPromptInput
    from .marimo_chatbot_cancel_prompt_output import MarimoChatbotCancelPromptOutput
    from .marimo_chatbot_data import MarimoChatbotData
    from .marimo_chatbot_data_allow_attachments import MarimoChatbotDataAllowAttachments
    from .marimo_chatbot_data_config import MarimoChatbotDataConfig
    from .marimo_chatbot_delete_chat_history_input import MarimoChatbotDeleteChatHistoryInput
    from .marimo_chatbot_delete_chat_history_output import MarimoChatbotDeleteChatHistoryOutput
    from .marimo_chatbot_delete_chat_message_input import MarimoChatbotDeleteChatMessageInput
    from .marimo_chatbot_delete_chat_message_output import MarimoChatbotDeleteChatMessageOutput
    from .marimo_chatbot_get_chat_history_input import MarimoChatbotGetChatHistoryInput
    from .marimo_chatbot_get_chat_history_output import MarimoChatbotGetChatHistoryOutput
    from .marimo_chatbot_get_chat_history_output_messages_item import MarimoChatbotGetChatHistoryOutputMessagesItem
    from .marimo_chatbot_get_chat_history_output_messages_item_role import (
        MarimoChatbotGetChatHistoryOutputMessagesItemRole,
    )
    from .marimo_chatbot_send_prompt_input import MarimoChatbotSendPromptInput
    from .marimo_chatbot_send_prompt_input_config import MarimoChatbotSendPromptInputConfig
    from .marimo_chatbot_send_prompt_input_messages_item import MarimoChatbotSendPromptInputMessagesItem
    from .marimo_chatbot_send_prompt_input_messages_item_role import MarimoChatbotSendPromptInputMessagesItemRole
    from .marimo_chatbot_send_prompt_output import MarimoChatbotSendPromptOutput
    from .marimo_checkbox_data import MarimoCheckboxData
    from .marimo_code_editor_data import MarimoCodeEditorData
    from .marimo_code_editor_data_debounce import MarimoCodeEditorDataDebounce
    from .marimo_code_editor_data_theme import MarimoCodeEditorDataTheme
    from .marimo_data_editor_data import MarimoDataEditorData
    from .marimo_data_editor_data_column_sizing_mode import MarimoDataEditorDataColumnSizingMode
    from .marimo_data_editor_data_data import MarimoDataEditorDataData
    from .marimo_data_editor_data_editable_columns import MarimoDataEditorDataEditableColumns
    from .marimo_data_editor_data_editable_columns_one import MarimoDataEditorDataEditableColumnsOne
    from .marimo_data_editor_data_initial_value import MarimoDataEditorDataInitialValue
    from .marimo_data_editor_data_initial_value_edits_item import MarimoDataEditorDataInitialValueEditsItem
    from .marimo_data_explorer_data import MarimoDataExplorerData
    from .marimo_dataframe_data import MarimoDataframeData
    from .marimo_dataframe_download_as_input import MarimoDataframeDownloadAsInput
    from .marimo_dataframe_download_as_input_format import MarimoDataframeDownloadAsInputFormat
    from .marimo_dataframe_download_as_output import MarimoDataframeDownloadAsOutput
    from .marimo_dataframe_get_column_values_input import MarimoDataframeGetColumnValuesInput
    from .marimo_dataframe_get_column_values_output import MarimoDataframeGetColumnValuesOutput
    from .marimo_dataframe_get_dataframe_input import MarimoDataframeGetDataframeInput
    from .marimo_dataframe_get_dataframe_output import MarimoDataframeGetDataframeOutput
    from .marimo_dataframe_get_size_bytes_input import MarimoDataframeGetSizeBytesInput
    from .marimo_dataframe_get_size_bytes_output import MarimoDataframeGetSizeBytesOutput
    from .marimo_dataframe_search_input import MarimoDataframeSearchInput
    from .marimo_dataframe_search_input_def_schema0 import MarimoDataframeSearchInputDefSchema0
    from .marimo_dataframe_search_input_def_schema0children_item import (
        MarimoDataframeSearchInputDefSchema0ChildrenItem,
        MarimoDataframeSearchInputDefSchema0ChildrenItem_Condition,
        MarimoDataframeSearchInputDefSchema0ChildrenItem_Group,
    )
    from .marimo_dataframe_search_input_def_schema0children_item_condition import (
        MarimoDataframeSearchInputDefSchema0ChildrenItemCondition,
    )
    from .marimo_dataframe_search_input_def_schema0children_item_condition_column_id import (
        MarimoDataframeSearchInputDefSchema0ChildrenItemConditionColumnId,
    )
    from .marimo_dataframe_search_input_def_schema0children_item_condition_operator import (
        MarimoDataframeSearchInputDefSchema0ChildrenItemConditionOperator,
    )
    from .marimo_dataframe_search_input_def_schema0operator import MarimoDataframeSearchInputDefSchema0Operator
    from .marimo_dataframe_search_input_def_schema0type import MarimoDataframeSearchInputDefSchema0Type
    from .marimo_dataframe_search_input_sort_item import MarimoDataframeSearchInputSortItem
    from .marimo_dataframe_search_output import MarimoDataframeSearchOutput
    from .marimo_dataframe_search_output_data import MarimoDataframeSearchOutputData
    from .marimo_date_data import MarimoDateData
    from .marimo_date_range_data import MarimoDateRangeData
    from .marimo_datetime_data import MarimoDatetimeData
    from .marimo_datetime_data_precision import MarimoDatetimeDataPrecision
    from .marimo_dict_data import MarimoDictData
    from .marimo_download_data import MarimoDownloadData
    from .marimo_download_load_input import MarimoDownloadLoadInput
    from .marimo_download_load_output import MarimoDownloadLoadOutput
    from .marimo_dropdown_data import MarimoDropdownData
    from .marimo_file_browser_data import MarimoFileBrowserData
    from .marimo_file_browser_list_directory_input import MarimoFileBrowserListDirectoryInput
    from .marimo_file_browser_list_directory_output import MarimoFileBrowserListDirectoryOutput
    from .marimo_file_browser_list_directory_output_files_item import MarimoFileBrowserListDirectoryOutputFilesItem
    from .marimo_file_data import MarimoFileData
    from .marimo_file_data_kind import MarimoFileDataKind
    from .marimo_form_data import MarimoFormData
    from .marimo_form_validate_input import MarimoFormValidateInput
    from .marimo_form_validate_output import MarimoFormValidateOutput
    from .marimo_image_comparison_data import MarimoImageComparisonData
    from .marimo_image_comparison_data_direction import MarimoImageComparisonDataDirection
    from .marimo_json_output_data import MarimoJsonOutputData
    from .marimo_json_output_data_value_types import MarimoJsonOutputDataValueTypes
    from .marimo_lazy_data import MarimoLazyData
    from .marimo_lazy_load_input import MarimoLazyLoadInput
    from .marimo_lazy_load_output import MarimoLazyLoadOutput
    from .marimo_matplotlib_data import MarimoMatplotlibData
    from .marimo_matplotlib_data_x_scale import MarimoMatplotlibDataXScale
    from .marimo_matplotlib_data_y_scale import MarimoMatplotlibDataYScale
    from .marimo_matrix_data import MarimoMatrixData
    from .marimo_mermaid_data import MarimoMermaidData
    from .marimo_microphone_data import MarimoMicrophoneData
    from .marimo_mime_renderer_data import MarimoMimeRendererData
    from .marimo_mime_renderer_data_data import MarimoMimeRendererDataData
    from .marimo_mpl_interactive_data import MarimoMplInteractiveData
    from .marimo_multiselect_data import MarimoMultiselectData
    from .marimo_nav_menu_data import MarimoNavMenuData
    from .marimo_nav_menu_data_items_item import MarimoNavMenuDataItemsItem
    from .marimo_nav_menu_data_items_item_description import MarimoNavMenuDataItemsItemDescription
    from .marimo_nav_menu_data_items_item_items import MarimoNavMenuDataItemsItemItems
    from .marimo_nav_menu_data_items_item_items_items_item import MarimoNavMenuDataItemsItemItemsItemsItem
    from .marimo_nav_menu_data_orientation import MarimoNavMenuDataOrientation
    from .marimo_number_data import MarimoNumberData
    from .marimo_outline_data import MarimoOutlineData
    from .marimo_panel_data import MarimoPanelData
    from .marimo_panel_data_render_json import MarimoPanelDataRenderJson
    from .marimo_panel_send_to_widget_input import MarimoPanelSendToWidgetInput
    from .marimo_panel_send_to_widget_output import MarimoPanelSendToWidgetOutput
    from .marimo_plotly_data import MarimoPlotlyData
    from .marimo_progress_data import MarimoProgressData
    from .marimo_progress_data_progress import MarimoProgressDataProgress
    from .marimo_radio_data import MarimoRadioData
    from .marimo_range_slider_data import MarimoRangeSliderData
    from .marimo_range_slider_data_orientation import MarimoRangeSliderDataOrientation
    from .marimo_refresh_data import MarimoRefreshData
    from .marimo_refresh_data_default_interval import MarimoRefreshDataDefaultInterval
    from .marimo_refresh_data_options_item import MarimoRefreshDataOptionsItem
    from .marimo_routes_data import MarimoRoutesData
    from .marimo_slider_data import MarimoSliderData
    from .marimo_slider_data_orientation import MarimoSliderDataOrientation
    from .marimo_stat_data import MarimoStatData
    from .marimo_stat_data_direction import MarimoStatDataDirection
    from .marimo_stat_data_target_direction import MarimoStatDataTargetDirection
    from .marimo_stat_data_value import MarimoStatDataValue
    from .marimo_switch_data import MarimoSwitchData
    from .marimo_table_calculate_top_k_rows_input import MarimoTableCalculateTopKRowsInput
    from .marimo_table_calculate_top_k_rows_output import MarimoTableCalculateTopKRowsOutput
    from .marimo_table_data import MarimoTableData
    from .marimo_table_data_data import MarimoTableDataData
    from .marimo_table_data_initial_value import MarimoTableDataInitialValue
    from .marimo_table_data_initial_value_one_item import MarimoTableDataInitialValueOneItem
    from .marimo_table_data_max_columns import MarimoTableDataMaxColumns
    from .marimo_table_data_max_columns_one import MarimoTableDataMaxColumnsOne
    from .marimo_table_data_raw_data import MarimoTableDataRawData
    from .marimo_table_data_selection import MarimoTableDataSelection
    from .marimo_table_data_show_column_summaries import MarimoTableDataShowColumnSummaries
    from .marimo_table_data_show_column_summaries_one import MarimoTableDataShowColumnSummariesOne
    from .marimo_table_data_text_justify_columns_value import MarimoTableDataTextJustifyColumnsValue
    from .marimo_table_data_total_rows import MarimoTableDataTotalRows
    from .marimo_table_data_total_rows_one import MarimoTableDataTotalRowsOne
    from .marimo_table_download_as_input import MarimoTableDownloadAsInput
    from .marimo_table_download_as_input_format import MarimoTableDownloadAsInputFormat
    from .marimo_table_download_as_output import MarimoTableDownloadAsOutput
    from .marimo_table_get_column_summaries_input import MarimoTableGetColumnSummariesInput
    from .marimo_table_get_column_summaries_output import MarimoTableGetColumnSummariesOutput
    from .marimo_table_get_column_summaries_output_bin_values_value_item import (
        MarimoTableGetColumnSummariesOutputBinValuesValueItem,
    )
    from .marimo_table_get_column_summaries_output_bin_values_value_item_bin_end import (
        MarimoTableGetColumnSummariesOutputBinValuesValueItemBinEnd,
    )
    from .marimo_table_get_column_summaries_output_bin_values_value_item_bin_start import (
        MarimoTableGetColumnSummariesOutputBinValuesValueItemBinStart,
    )
    from .marimo_table_get_column_summaries_output_data import MarimoTableGetColumnSummariesOutputData
    from .marimo_table_get_column_summaries_output_stats_value import MarimoTableGetColumnSummariesOutputStatsValue
    from .marimo_table_get_column_summaries_output_stats_value_max import (
        MarimoTableGetColumnSummariesOutputStatsValueMax,
    )
    from .marimo_table_get_column_summaries_output_stats_value_mean import (
        MarimoTableGetColumnSummariesOutputStatsValueMean,
    )
    from .marimo_table_get_column_summaries_output_stats_value_median import (
        MarimoTableGetColumnSummariesOutputStatsValueMedian,
    )
    from .marimo_table_get_column_summaries_output_stats_value_min import (
        MarimoTableGetColumnSummariesOutputStatsValueMin,
    )
    from .marimo_table_get_column_summaries_output_stats_value_p25 import (
        MarimoTableGetColumnSummariesOutputStatsValueP25,
    )
    from .marimo_table_get_column_summaries_output_stats_value_p5 import MarimoTableGetColumnSummariesOutputStatsValueP5
    from .marimo_table_get_column_summaries_output_stats_value_p75 import (
        MarimoTableGetColumnSummariesOutputStatsValueP75,
    )
    from .marimo_table_get_column_summaries_output_stats_value_p95 import (
        MarimoTableGetColumnSummariesOutputStatsValueP95,
    )
    from .marimo_table_get_column_summaries_output_stats_value_std import (
        MarimoTableGetColumnSummariesOutputStatsValueStd,
    )
    from .marimo_table_get_column_summaries_output_value_counts_value_item import (
        MarimoTableGetColumnSummariesOutputValueCountsValueItem,
    )
    from .marimo_table_get_data_url_input import MarimoTableGetDataUrlInput
    from .marimo_table_get_data_url_output import MarimoTableGetDataUrlOutput
    from .marimo_table_get_data_url_output_data_url import MarimoTableGetDataUrlOutputDataUrl
    from .marimo_table_get_data_url_output_format import MarimoTableGetDataUrlOutputFormat
    from .marimo_table_get_row_ids_input import MarimoTableGetRowIdsInput
    from .marimo_table_get_row_ids_output import MarimoTableGetRowIdsOutput
    from .marimo_table_get_size_bytes_input import MarimoTableGetSizeBytesInput
    from .marimo_table_get_size_bytes_output import MarimoTableGetSizeBytesOutput
    from .marimo_table_preview_column_input import MarimoTablePreviewColumnInput
    from .marimo_table_preview_column_output import MarimoTablePreviewColumnOutput
    from .marimo_table_preview_column_output_stats import MarimoTablePreviewColumnOutputStats
    from .marimo_table_preview_column_output_stats_max import MarimoTablePreviewColumnOutputStatsMax
    from .marimo_table_preview_column_output_stats_mean import MarimoTablePreviewColumnOutputStatsMean
    from .marimo_table_preview_column_output_stats_median import MarimoTablePreviewColumnOutputStatsMedian
    from .marimo_table_preview_column_output_stats_min import MarimoTablePreviewColumnOutputStatsMin
    from .marimo_table_preview_column_output_stats_p25 import MarimoTablePreviewColumnOutputStatsP25
    from .marimo_table_preview_column_output_stats_p5 import MarimoTablePreviewColumnOutputStatsP5
    from .marimo_table_preview_column_output_stats_p75 import MarimoTablePreviewColumnOutputStatsP75
    from .marimo_table_preview_column_output_stats_p95 import MarimoTablePreviewColumnOutputStatsP95
    from .marimo_table_preview_column_output_stats_std import MarimoTablePreviewColumnOutputStatsStd
    from .marimo_table_search_input import MarimoTableSearchInput
    from .marimo_table_search_input_def_schema0 import MarimoTableSearchInputDefSchema0
    from .marimo_table_search_input_def_schema0children_item import (
        MarimoTableSearchInputDefSchema0ChildrenItem,
        MarimoTableSearchInputDefSchema0ChildrenItem_Condition,
        MarimoTableSearchInputDefSchema0ChildrenItem_Group,
    )
    from .marimo_table_search_input_def_schema0children_item_condition import (
        MarimoTableSearchInputDefSchema0ChildrenItemCondition,
    )
    from .marimo_table_search_input_def_schema0children_item_condition_column_id import (
        MarimoTableSearchInputDefSchema0ChildrenItemConditionColumnId,
    )
    from .marimo_table_search_input_def_schema0children_item_condition_operator import (
        MarimoTableSearchInputDefSchema0ChildrenItemConditionOperator,
    )
    from .marimo_table_search_input_def_schema0operator import MarimoTableSearchInputDefSchema0Operator
    from .marimo_table_search_input_def_schema0type import MarimoTableSearchInputDefSchema0Type
    from .marimo_table_search_input_sort_item import MarimoTableSearchInputSortItem
    from .marimo_table_search_output import MarimoTableSearchOutput
    from .marimo_table_search_output_data import MarimoTableSearchOutputData
    from .marimo_table_search_output_raw_data import MarimoTableSearchOutputRawData
    from .marimo_table_search_output_total_rows import MarimoTableSearchOutputTotalRows
    from .marimo_table_search_output_total_rows_one import MarimoTableSearchOutputTotalRowsOne
    from .marimo_tabs_data import MarimoTabsData
    from .marimo_tabs_data_orientation import MarimoTabsDataOrientation
    from .marimo_tex_data import MarimoTexData
    from .marimo_text_area_data import MarimoTextAreaData
    from .marimo_text_area_data_debounce import MarimoTextAreaDataDebounce
    from .marimo_text_data import MarimoTextData
    from .marimo_text_data_debounce import MarimoTextDataDebounce
    from .marimo_text_data_kind import MarimoTextDataKind
    from .marimo_vega_data import MarimoVegaData
    from .marimo_vega_data_chart_selection import MarimoVegaDataChartSelection
    from .marimo_vega_data_chart_selection_one import MarimoVegaDataChartSelectionOne
    from .marimo_vega_data_chart_selection_two import MarimoVegaDataChartSelectionTwo
    from .marimo_vega_data_field_selection import MarimoVegaDataFieldSelection
_dynamic_imports: typing.Dict[str, str] = {
    "MarimoAccordionData": ".marimo_accordion_data",
    "MarimoAnywidgetData": ".marimo_anywidget_data",
    "MarimoButtonData": ".marimo_button_data",
    "MarimoButtonDataKind": ".marimo_button_data_kind",
    "MarimoCalloutOutputData": ".marimo_callout_output_data",
    "MarimoCalloutOutputDataKind": ".marimo_callout_output_data_kind",
    "MarimoCarouselData": ".marimo_carousel_data",
    "MarimoCarouselDataHeight": ".marimo_carousel_data_height",
    "MarimoChatbotCancelPromptInput": ".marimo_chatbot_cancel_prompt_input",
    "MarimoChatbotCancelPromptOutput": ".marimo_chatbot_cancel_prompt_output",
    "MarimoChatbotData": ".marimo_chatbot_data",
    "MarimoChatbotDataAllowAttachments": ".marimo_chatbot_data_allow_attachments",
    "MarimoChatbotDataConfig": ".marimo_chatbot_data_config",
    "MarimoChatbotDeleteChatHistoryInput": ".marimo_chatbot_delete_chat_history_input",
    "MarimoChatbotDeleteChatHistoryOutput": ".marimo_chatbot_delete_chat_history_output",
    "MarimoChatbotDeleteChatMessageInput": ".marimo_chatbot_delete_chat_message_input",
    "MarimoChatbotDeleteChatMessageOutput": ".marimo_chatbot_delete_chat_message_output",
    "MarimoChatbotGetChatHistoryInput": ".marimo_chatbot_get_chat_history_input",
    "MarimoChatbotGetChatHistoryOutput": ".marimo_chatbot_get_chat_history_output",
    "MarimoChatbotGetChatHistoryOutputMessagesItem": ".marimo_chatbot_get_chat_history_output_messages_item",
    "MarimoChatbotGetChatHistoryOutputMessagesItemRole": ".marimo_chatbot_get_chat_history_output_messages_item_role",
    "MarimoChatbotSendPromptInput": ".marimo_chatbot_send_prompt_input",
    "MarimoChatbotSendPromptInputConfig": ".marimo_chatbot_send_prompt_input_config",
    "MarimoChatbotSendPromptInputMessagesItem": ".marimo_chatbot_send_prompt_input_messages_item",
    "MarimoChatbotSendPromptInputMessagesItemRole": ".marimo_chatbot_send_prompt_input_messages_item_role",
    "MarimoChatbotSendPromptOutput": ".marimo_chatbot_send_prompt_output",
    "MarimoCheckboxData": ".marimo_checkbox_data",
    "MarimoCodeEditorData": ".marimo_code_editor_data",
    "MarimoCodeEditorDataDebounce": ".marimo_code_editor_data_debounce",
    "MarimoCodeEditorDataTheme": ".marimo_code_editor_data_theme",
    "MarimoDataEditorData": ".marimo_data_editor_data",
    "MarimoDataEditorDataColumnSizingMode": ".marimo_data_editor_data_column_sizing_mode",
    "MarimoDataEditorDataData": ".marimo_data_editor_data_data",
    "MarimoDataEditorDataEditableColumns": ".marimo_data_editor_data_editable_columns",
    "MarimoDataEditorDataEditableColumnsOne": ".marimo_data_editor_data_editable_columns_one",
    "MarimoDataEditorDataInitialValue": ".marimo_data_editor_data_initial_value",
    "MarimoDataEditorDataInitialValueEditsItem": ".marimo_data_editor_data_initial_value_edits_item",
    "MarimoDataExplorerData": ".marimo_data_explorer_data",
    "MarimoDataframeData": ".marimo_dataframe_data",
    "MarimoDataframeDownloadAsInput": ".marimo_dataframe_download_as_input",
    "MarimoDataframeDownloadAsInputFormat": ".marimo_dataframe_download_as_input_format",
    "MarimoDataframeDownloadAsOutput": ".marimo_dataframe_download_as_output",
    "MarimoDataframeGetColumnValuesInput": ".marimo_dataframe_get_column_values_input",
    "MarimoDataframeGetColumnValuesOutput": ".marimo_dataframe_get_column_values_output",
    "MarimoDataframeGetDataframeInput": ".marimo_dataframe_get_dataframe_input",
    "MarimoDataframeGetDataframeOutput": ".marimo_dataframe_get_dataframe_output",
    "MarimoDataframeGetSizeBytesInput": ".marimo_dataframe_get_size_bytes_input",
    "MarimoDataframeGetSizeBytesOutput": ".marimo_dataframe_get_size_bytes_output",
    "MarimoDataframeSearchInput": ".marimo_dataframe_search_input",
    "MarimoDataframeSearchInputDefSchema0": ".marimo_dataframe_search_input_def_schema0",
    "MarimoDataframeSearchInputDefSchema0ChildrenItem": ".marimo_dataframe_search_input_def_schema0children_item",
    "MarimoDataframeSearchInputDefSchema0ChildrenItemCondition": ".marimo_dataframe_search_input_def_schema0children_item_condition",
    "MarimoDataframeSearchInputDefSchema0ChildrenItemConditionColumnId": ".marimo_dataframe_search_input_def_schema0children_item_condition_column_id",
    "MarimoDataframeSearchInputDefSchema0ChildrenItemConditionOperator": ".marimo_dataframe_search_input_def_schema0children_item_condition_operator",
    "MarimoDataframeSearchInputDefSchema0ChildrenItem_Condition": ".marimo_dataframe_search_input_def_schema0children_item",
    "MarimoDataframeSearchInputDefSchema0ChildrenItem_Group": ".marimo_dataframe_search_input_def_schema0children_item",
    "MarimoDataframeSearchInputDefSchema0Operator": ".marimo_dataframe_search_input_def_schema0operator",
    "MarimoDataframeSearchInputDefSchema0Type": ".marimo_dataframe_search_input_def_schema0type",
    "MarimoDataframeSearchInputSortItem": ".marimo_dataframe_search_input_sort_item",
    "MarimoDataframeSearchOutput": ".marimo_dataframe_search_output",
    "MarimoDataframeSearchOutputData": ".marimo_dataframe_search_output_data",
    "MarimoDateData": ".marimo_date_data",
    "MarimoDateRangeData": ".marimo_date_range_data",
    "MarimoDatetimeData": ".marimo_datetime_data",
    "MarimoDatetimeDataPrecision": ".marimo_datetime_data_precision",
    "MarimoDictData": ".marimo_dict_data",
    "MarimoDownloadData": ".marimo_download_data",
    "MarimoDownloadLoadInput": ".marimo_download_load_input",
    "MarimoDownloadLoadOutput": ".marimo_download_load_output",
    "MarimoDropdownData": ".marimo_dropdown_data",
    "MarimoFileBrowserData": ".marimo_file_browser_data",
    "MarimoFileBrowserListDirectoryInput": ".marimo_file_browser_list_directory_input",
    "MarimoFileBrowserListDirectoryOutput": ".marimo_file_browser_list_directory_output",
    "MarimoFileBrowserListDirectoryOutputFilesItem": ".marimo_file_browser_list_directory_output_files_item",
    "MarimoFileData": ".marimo_file_data",
    "MarimoFileDataKind": ".marimo_file_data_kind",
    "MarimoFormData": ".marimo_form_data",
    "MarimoFormValidateInput": ".marimo_form_validate_input",
    "MarimoFormValidateOutput": ".marimo_form_validate_output",
    "MarimoImageComparisonData": ".marimo_image_comparison_data",
    "MarimoImageComparisonDataDirection": ".marimo_image_comparison_data_direction",
    "MarimoJsonOutputData": ".marimo_json_output_data",
    "MarimoJsonOutputDataValueTypes": ".marimo_json_output_data_value_types",
    "MarimoLazyData": ".marimo_lazy_data",
    "MarimoLazyLoadInput": ".marimo_lazy_load_input",
    "MarimoLazyLoadOutput": ".marimo_lazy_load_output",
    "MarimoMatplotlibData": ".marimo_matplotlib_data",
    "MarimoMatplotlibDataXScale": ".marimo_matplotlib_data_x_scale",
    "MarimoMatplotlibDataYScale": ".marimo_matplotlib_data_y_scale",
    "MarimoMatrixData": ".marimo_matrix_data",
    "MarimoMermaidData": ".marimo_mermaid_data",
    "MarimoMicrophoneData": ".marimo_microphone_data",
    "MarimoMimeRendererData": ".marimo_mime_renderer_data",
    "MarimoMimeRendererDataData": ".marimo_mime_renderer_data_data",
    "MarimoMplInteractiveData": ".marimo_mpl_interactive_data",
    "MarimoMultiselectData": ".marimo_multiselect_data",
    "MarimoNavMenuData": ".marimo_nav_menu_data",
    "MarimoNavMenuDataItemsItem": ".marimo_nav_menu_data_items_item",
    "MarimoNavMenuDataItemsItemDescription": ".marimo_nav_menu_data_items_item_description",
    "MarimoNavMenuDataItemsItemItems": ".marimo_nav_menu_data_items_item_items",
    "MarimoNavMenuDataItemsItemItemsItemsItem": ".marimo_nav_menu_data_items_item_items_items_item",
    "MarimoNavMenuDataOrientation": ".marimo_nav_menu_data_orientation",
    "MarimoNumberData": ".marimo_number_data",
    "MarimoOutlineData": ".marimo_outline_data",
    "MarimoPanelData": ".marimo_panel_data",
    "MarimoPanelDataRenderJson": ".marimo_panel_data_render_json",
    "MarimoPanelSendToWidgetInput": ".marimo_panel_send_to_widget_input",
    "MarimoPanelSendToWidgetOutput": ".marimo_panel_send_to_widget_output",
    "MarimoPlotlyData": ".marimo_plotly_data",
    "MarimoProgressData": ".marimo_progress_data",
    "MarimoProgressDataProgress": ".marimo_progress_data_progress",
    "MarimoRadioData": ".marimo_radio_data",
    "MarimoRangeSliderData": ".marimo_range_slider_data",
    "MarimoRangeSliderDataOrientation": ".marimo_range_slider_data_orientation",
    "MarimoRefreshData": ".marimo_refresh_data",
    "MarimoRefreshDataDefaultInterval": ".marimo_refresh_data_default_interval",
    "MarimoRefreshDataOptionsItem": ".marimo_refresh_data_options_item",
    "MarimoRoutesData": ".marimo_routes_data",
    "MarimoSliderData": ".marimo_slider_data",
    "MarimoSliderDataOrientation": ".marimo_slider_data_orientation",
    "MarimoStatData": ".marimo_stat_data",
    "MarimoStatDataDirection": ".marimo_stat_data_direction",
    "MarimoStatDataTargetDirection": ".marimo_stat_data_target_direction",
    "MarimoStatDataValue": ".marimo_stat_data_value",
    "MarimoSwitchData": ".marimo_switch_data",
    "MarimoTableCalculateTopKRowsInput": ".marimo_table_calculate_top_k_rows_input",
    "MarimoTableCalculateTopKRowsOutput": ".marimo_table_calculate_top_k_rows_output",
    "MarimoTableData": ".marimo_table_data",
    "MarimoTableDataData": ".marimo_table_data_data",
    "MarimoTableDataInitialValue": ".marimo_table_data_initial_value",
    "MarimoTableDataInitialValueOneItem": ".marimo_table_data_initial_value_one_item",
    "MarimoTableDataMaxColumns": ".marimo_table_data_max_columns",
    "MarimoTableDataMaxColumnsOne": ".marimo_table_data_max_columns_one",
    "MarimoTableDataRawData": ".marimo_table_data_raw_data",
    "MarimoTableDataSelection": ".marimo_table_data_selection",
    "MarimoTableDataShowColumnSummaries": ".marimo_table_data_show_column_summaries",
    "MarimoTableDataShowColumnSummariesOne": ".marimo_table_data_show_column_summaries_one",
    "MarimoTableDataTextJustifyColumnsValue": ".marimo_table_data_text_justify_columns_value",
    "MarimoTableDataTotalRows": ".marimo_table_data_total_rows",
    "MarimoTableDataTotalRowsOne": ".marimo_table_data_total_rows_one",
    "MarimoTableDownloadAsInput": ".marimo_table_download_as_input",
    "MarimoTableDownloadAsInputFormat": ".marimo_table_download_as_input_format",
    "MarimoTableDownloadAsOutput": ".marimo_table_download_as_output",
    "MarimoTableGetColumnSummariesInput": ".marimo_table_get_column_summaries_input",
    "MarimoTableGetColumnSummariesOutput": ".marimo_table_get_column_summaries_output",
    "MarimoTableGetColumnSummariesOutputBinValuesValueItem": ".marimo_table_get_column_summaries_output_bin_values_value_item",
    "MarimoTableGetColumnSummariesOutputBinValuesValueItemBinEnd": ".marimo_table_get_column_summaries_output_bin_values_value_item_bin_end",
    "MarimoTableGetColumnSummariesOutputBinValuesValueItemBinStart": ".marimo_table_get_column_summaries_output_bin_values_value_item_bin_start",
    "MarimoTableGetColumnSummariesOutputData": ".marimo_table_get_column_summaries_output_data",
    "MarimoTableGetColumnSummariesOutputStatsValue": ".marimo_table_get_column_summaries_output_stats_value",
    "MarimoTableGetColumnSummariesOutputStatsValueMax": ".marimo_table_get_column_summaries_output_stats_value_max",
    "MarimoTableGetColumnSummariesOutputStatsValueMean": ".marimo_table_get_column_summaries_output_stats_value_mean",
    "MarimoTableGetColumnSummariesOutputStatsValueMedian": ".marimo_table_get_column_summaries_output_stats_value_median",
    "MarimoTableGetColumnSummariesOutputStatsValueMin": ".marimo_table_get_column_summaries_output_stats_value_min",
    "MarimoTableGetColumnSummariesOutputStatsValueP25": ".marimo_table_get_column_summaries_output_stats_value_p25",
    "MarimoTableGetColumnSummariesOutputStatsValueP5": ".marimo_table_get_column_summaries_output_stats_value_p5",
    "MarimoTableGetColumnSummariesOutputStatsValueP75": ".marimo_table_get_column_summaries_output_stats_value_p75",
    "MarimoTableGetColumnSummariesOutputStatsValueP95": ".marimo_table_get_column_summaries_output_stats_value_p95",
    "MarimoTableGetColumnSummariesOutputStatsValueStd": ".marimo_table_get_column_summaries_output_stats_value_std",
    "MarimoTableGetColumnSummariesOutputValueCountsValueItem": ".marimo_table_get_column_summaries_output_value_counts_value_item",
    "MarimoTableGetDataUrlInput": ".marimo_table_get_data_url_input",
    "MarimoTableGetDataUrlOutput": ".marimo_table_get_data_url_output",
    "MarimoTableGetDataUrlOutputDataUrl": ".marimo_table_get_data_url_output_data_url",
    "MarimoTableGetDataUrlOutputFormat": ".marimo_table_get_data_url_output_format",
    "MarimoTableGetRowIdsInput": ".marimo_table_get_row_ids_input",
    "MarimoTableGetRowIdsOutput": ".marimo_table_get_row_ids_output",
    "MarimoTableGetSizeBytesInput": ".marimo_table_get_size_bytes_input",
    "MarimoTableGetSizeBytesOutput": ".marimo_table_get_size_bytes_output",
    "MarimoTablePreviewColumnInput": ".marimo_table_preview_column_input",
    "MarimoTablePreviewColumnOutput": ".marimo_table_preview_column_output",
    "MarimoTablePreviewColumnOutputStats": ".marimo_table_preview_column_output_stats",
    "MarimoTablePreviewColumnOutputStatsMax": ".marimo_table_preview_column_output_stats_max",
    "MarimoTablePreviewColumnOutputStatsMean": ".marimo_table_preview_column_output_stats_mean",
    "MarimoTablePreviewColumnOutputStatsMedian": ".marimo_table_preview_column_output_stats_median",
    "MarimoTablePreviewColumnOutputStatsMin": ".marimo_table_preview_column_output_stats_min",
    "MarimoTablePreviewColumnOutputStatsP25": ".marimo_table_preview_column_output_stats_p25",
    "MarimoTablePreviewColumnOutputStatsP5": ".marimo_table_preview_column_output_stats_p5",
    "MarimoTablePreviewColumnOutputStatsP75": ".marimo_table_preview_column_output_stats_p75",
    "MarimoTablePreviewColumnOutputStatsP95": ".marimo_table_preview_column_output_stats_p95",
    "MarimoTablePreviewColumnOutputStatsStd": ".marimo_table_preview_column_output_stats_std",
    "MarimoTableSearchInput": ".marimo_table_search_input",
    "MarimoTableSearchInputDefSchema0": ".marimo_table_search_input_def_schema0",
    "MarimoTableSearchInputDefSchema0ChildrenItem": ".marimo_table_search_input_def_schema0children_item",
    "MarimoTableSearchInputDefSchema0ChildrenItemCondition": ".marimo_table_search_input_def_schema0children_item_condition",
    "MarimoTableSearchInputDefSchema0ChildrenItemConditionColumnId": ".marimo_table_search_input_def_schema0children_item_condition_column_id",
    "MarimoTableSearchInputDefSchema0ChildrenItemConditionOperator": ".marimo_table_search_input_def_schema0children_item_condition_operator",
    "MarimoTableSearchInputDefSchema0ChildrenItem_Condition": ".marimo_table_search_input_def_schema0children_item",
    "MarimoTableSearchInputDefSchema0ChildrenItem_Group": ".marimo_table_search_input_def_schema0children_item",
    "MarimoTableSearchInputDefSchema0Operator": ".marimo_table_search_input_def_schema0operator",
    "MarimoTableSearchInputDefSchema0Type": ".marimo_table_search_input_def_schema0type",
    "MarimoTableSearchInputSortItem": ".marimo_table_search_input_sort_item",
    "MarimoTableSearchOutput": ".marimo_table_search_output",
    "MarimoTableSearchOutputData": ".marimo_table_search_output_data",
    "MarimoTableSearchOutputRawData": ".marimo_table_search_output_raw_data",
    "MarimoTableSearchOutputTotalRows": ".marimo_table_search_output_total_rows",
    "MarimoTableSearchOutputTotalRowsOne": ".marimo_table_search_output_total_rows_one",
    "MarimoTabsData": ".marimo_tabs_data",
    "MarimoTabsDataOrientation": ".marimo_tabs_data_orientation",
    "MarimoTexData": ".marimo_tex_data",
    "MarimoTextAreaData": ".marimo_text_area_data",
    "MarimoTextAreaDataDebounce": ".marimo_text_area_data_debounce",
    "MarimoTextData": ".marimo_text_data",
    "MarimoTextDataDebounce": ".marimo_text_data_debounce",
    "MarimoTextDataKind": ".marimo_text_data_kind",
    "MarimoVegaData": ".marimo_vega_data",
    "MarimoVegaDataChartSelection": ".marimo_vega_data_chart_selection",
    "MarimoVegaDataChartSelectionOne": ".marimo_vega_data_chart_selection_one",
    "MarimoVegaDataChartSelectionTwo": ".marimo_vega_data_chart_selection_two",
    "MarimoVegaDataFieldSelection": ".marimo_vega_data_field_selection",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "MarimoAccordionData",
    "MarimoAnywidgetData",
    "MarimoButtonData",
    "MarimoButtonDataKind",
    "MarimoCalloutOutputData",
    "MarimoCalloutOutputDataKind",
    "MarimoCarouselData",
    "MarimoCarouselDataHeight",
    "MarimoChatbotCancelPromptInput",
    "MarimoChatbotCancelPromptOutput",
    "MarimoChatbotData",
    "MarimoChatbotDataAllowAttachments",
    "MarimoChatbotDataConfig",
    "MarimoChatbotDeleteChatHistoryInput",
    "MarimoChatbotDeleteChatHistoryOutput",
    "MarimoChatbotDeleteChatMessageInput",
    "MarimoChatbotDeleteChatMessageOutput",
    "MarimoChatbotGetChatHistoryInput",
    "MarimoChatbotGetChatHistoryOutput",
    "MarimoChatbotGetChatHistoryOutputMessagesItem",
    "MarimoChatbotGetChatHistoryOutputMessagesItemRole",
    "MarimoChatbotSendPromptInput",
    "MarimoChatbotSendPromptInputConfig",
    "MarimoChatbotSendPromptInputMessagesItem",
    "MarimoChatbotSendPromptInputMessagesItemRole",
    "MarimoChatbotSendPromptOutput",
    "MarimoCheckboxData",
    "MarimoCodeEditorData",
    "MarimoCodeEditorDataDebounce",
    "MarimoCodeEditorDataTheme",
    "MarimoDataEditorData",
    "MarimoDataEditorDataColumnSizingMode",
    "MarimoDataEditorDataData",
    "MarimoDataEditorDataEditableColumns",
    "MarimoDataEditorDataEditableColumnsOne",
    "MarimoDataEditorDataInitialValue",
    "MarimoDataEditorDataInitialValueEditsItem",
    "MarimoDataExplorerData",
    "MarimoDataframeData",
    "MarimoDataframeDownloadAsInput",
    "MarimoDataframeDownloadAsInputFormat",
    "MarimoDataframeDownloadAsOutput",
    "MarimoDataframeGetColumnValuesInput",
    "MarimoDataframeGetColumnValuesOutput",
    "MarimoDataframeGetDataframeInput",
    "MarimoDataframeGetDataframeOutput",
    "MarimoDataframeGetSizeBytesInput",
    "MarimoDataframeGetSizeBytesOutput",
    "MarimoDataframeSearchInput",
    "MarimoDataframeSearchInputDefSchema0",
    "MarimoDataframeSearchInputDefSchema0ChildrenItem",
    "MarimoDataframeSearchInputDefSchema0ChildrenItemCondition",
    "MarimoDataframeSearchInputDefSchema0ChildrenItemConditionColumnId",
    "MarimoDataframeSearchInputDefSchema0ChildrenItemConditionOperator",
    "MarimoDataframeSearchInputDefSchema0ChildrenItem_Condition",
    "MarimoDataframeSearchInputDefSchema0ChildrenItem_Group",
    "MarimoDataframeSearchInputDefSchema0Operator",
    "MarimoDataframeSearchInputDefSchema0Type",
    "MarimoDataframeSearchInputSortItem",
    "MarimoDataframeSearchOutput",
    "MarimoDataframeSearchOutputData",
    "MarimoDateData",
    "MarimoDateRangeData",
    "MarimoDatetimeData",
    "MarimoDatetimeDataPrecision",
    "MarimoDictData",
    "MarimoDownloadData",
    "MarimoDownloadLoadInput",
    "MarimoDownloadLoadOutput",
    "MarimoDropdownData",
    "MarimoFileBrowserData",
    "MarimoFileBrowserListDirectoryInput",
    "MarimoFileBrowserListDirectoryOutput",
    "MarimoFileBrowserListDirectoryOutputFilesItem",
    "MarimoFileData",
    "MarimoFileDataKind",
    "MarimoFormData",
    "MarimoFormValidateInput",
    "MarimoFormValidateOutput",
    "MarimoImageComparisonData",
    "MarimoImageComparisonDataDirection",
    "MarimoJsonOutputData",
    "MarimoJsonOutputDataValueTypes",
    "MarimoLazyData",
    "MarimoLazyLoadInput",
    "MarimoLazyLoadOutput",
    "MarimoMatplotlibData",
    "MarimoMatplotlibDataXScale",
    "MarimoMatplotlibDataYScale",
    "MarimoMatrixData",
    "MarimoMermaidData",
    "MarimoMicrophoneData",
    "MarimoMimeRendererData",
    "MarimoMimeRendererDataData",
    "MarimoMplInteractiveData",
    "MarimoMultiselectData",
    "MarimoNavMenuData",
    "MarimoNavMenuDataItemsItem",
    "MarimoNavMenuDataItemsItemDescription",
    "MarimoNavMenuDataItemsItemItems",
    "MarimoNavMenuDataItemsItemItemsItemsItem",
    "MarimoNavMenuDataOrientation",
    "MarimoNumberData",
    "MarimoOutlineData",
    "MarimoPanelData",
    "MarimoPanelDataRenderJson",
    "MarimoPanelSendToWidgetInput",
    "MarimoPanelSendToWidgetOutput",
    "MarimoPlotlyData",
    "MarimoProgressData",
    "MarimoProgressDataProgress",
    "MarimoRadioData",
    "MarimoRangeSliderData",
    "MarimoRangeSliderDataOrientation",
    "MarimoRefreshData",
    "MarimoRefreshDataDefaultInterval",
    "MarimoRefreshDataOptionsItem",
    "MarimoRoutesData",
    "MarimoSliderData",
    "MarimoSliderDataOrientation",
    "MarimoStatData",
    "MarimoStatDataDirection",
    "MarimoStatDataTargetDirection",
    "MarimoStatDataValue",
    "MarimoSwitchData",
    "MarimoTableCalculateTopKRowsInput",
    "MarimoTableCalculateTopKRowsOutput",
    "MarimoTableData",
    "MarimoTableDataData",
    "MarimoTableDataInitialValue",
    "MarimoTableDataInitialValueOneItem",
    "MarimoTableDataMaxColumns",
    "MarimoTableDataMaxColumnsOne",
    "MarimoTableDataRawData",
    "MarimoTableDataSelection",
    "MarimoTableDataShowColumnSummaries",
    "MarimoTableDataShowColumnSummariesOne",
    "MarimoTableDataTextJustifyColumnsValue",
    "MarimoTableDataTotalRows",
    "MarimoTableDataTotalRowsOne",
    "MarimoTableDownloadAsInput",
    "MarimoTableDownloadAsInputFormat",
    "MarimoTableDownloadAsOutput",
    "MarimoTableGetColumnSummariesInput",
    "MarimoTableGetColumnSummariesOutput",
    "MarimoTableGetColumnSummariesOutputBinValuesValueItem",
    "MarimoTableGetColumnSummariesOutputBinValuesValueItemBinEnd",
    "MarimoTableGetColumnSummariesOutputBinValuesValueItemBinStart",
    "MarimoTableGetColumnSummariesOutputData",
    "MarimoTableGetColumnSummariesOutputStatsValue",
    "MarimoTableGetColumnSummariesOutputStatsValueMax",
    "MarimoTableGetColumnSummariesOutputStatsValueMean",
    "MarimoTableGetColumnSummariesOutputStatsValueMedian",
    "MarimoTableGetColumnSummariesOutputStatsValueMin",
    "MarimoTableGetColumnSummariesOutputStatsValueP25",
    "MarimoTableGetColumnSummariesOutputStatsValueP5",
    "MarimoTableGetColumnSummariesOutputStatsValueP75",
    "MarimoTableGetColumnSummariesOutputStatsValueP95",
    "MarimoTableGetColumnSummariesOutputStatsValueStd",
    "MarimoTableGetColumnSummariesOutputValueCountsValueItem",
    "MarimoTableGetDataUrlInput",
    "MarimoTableGetDataUrlOutput",
    "MarimoTableGetDataUrlOutputDataUrl",
    "MarimoTableGetDataUrlOutputFormat",
    "MarimoTableGetRowIdsInput",
    "MarimoTableGetRowIdsOutput",
    "MarimoTableGetSizeBytesInput",
    "MarimoTableGetSizeBytesOutput",
    "MarimoTablePreviewColumnInput",
    "MarimoTablePreviewColumnOutput",
    "MarimoTablePreviewColumnOutputStats",
    "MarimoTablePreviewColumnOutputStatsMax",
    "MarimoTablePreviewColumnOutputStatsMean",
    "MarimoTablePreviewColumnOutputStatsMedian",
    "MarimoTablePreviewColumnOutputStatsMin",
    "MarimoTablePreviewColumnOutputStatsP25",
    "MarimoTablePreviewColumnOutputStatsP5",
    "MarimoTablePreviewColumnOutputStatsP75",
    "MarimoTablePreviewColumnOutputStatsP95",
    "MarimoTablePreviewColumnOutputStatsStd",
    "MarimoTableSearchInput",
    "MarimoTableSearchInputDefSchema0",
    "MarimoTableSearchInputDefSchema0ChildrenItem",
    "MarimoTableSearchInputDefSchema0ChildrenItemCondition",
    "MarimoTableSearchInputDefSchema0ChildrenItemConditionColumnId",
    "MarimoTableSearchInputDefSchema0ChildrenItemConditionOperator",
    "MarimoTableSearchInputDefSchema0ChildrenItem_Condition",
    "MarimoTableSearchInputDefSchema0ChildrenItem_Group",
    "MarimoTableSearchInputDefSchema0Operator",
    "MarimoTableSearchInputDefSchema0Type",
    "MarimoTableSearchInputSortItem",
    "MarimoTableSearchOutput",
    "MarimoTableSearchOutputData",
    "MarimoTableSearchOutputRawData",
    "MarimoTableSearchOutputTotalRows",
    "MarimoTableSearchOutputTotalRowsOne",
    "MarimoTabsData",
    "MarimoTabsDataOrientation",
    "MarimoTexData",
    "MarimoTextAreaData",
    "MarimoTextAreaDataDebounce",
    "MarimoTextData",
    "MarimoTextDataDebounce",
    "MarimoTextDataKind",
    "MarimoVegaData",
    "MarimoVegaDataChartSelection",
    "MarimoVegaDataChartSelectionOne",
    "MarimoVegaDataChartSelectionTwo",
    "MarimoVegaDataFieldSelection",
]
