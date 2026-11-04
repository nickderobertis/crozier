

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StatisticName(enum.StrEnum):
    SEARCH_SCENARIOS_BY_NAME = "SEARCH_SCENARIOS_BY_NAME"
    FILTER_SCENARIOS_BY_STATUS = "FILTER_SCENARIOS_BY_STATUS"
    FILTER_SCENARIOS_BY_PROCESSING_MODE = "FILTER_SCENARIOS_BY_PROCESSING_MODE"
    FILTER_SCENARIOS_BY_CATEGORY = "FILTER_SCENARIOS_BY_CATEGORY"
    FILTER_SCENARIOS_BY_AUTHOR = "FILTER_SCENARIOS_BY_AUTHOR"
    FILTER_SCENARIOS_BY_OTHER = "FILTER_SCENARIOS_BY_OTHER"
    SORT_SCENARIOS_BY_SORT_OPTION = "SORT_SCENARIOS_BY_SORT_OPTION"
    SEARCH_COMPONENTS_BY_NAME = "SEARCH_COMPONENTS_BY_NAME"
    FILTER_COMPONENTS_BY_GROUP = "FILTER_COMPONENTS_BY_GROUP"
    FILTER_COMPONENTS_BY_PROCESSING_MODE = "FILTER_COMPONENTS_BY_PROCESSING_MODE"
    FILTER_COMPONENTS_BY_CATEGORY = "FILTER_COMPONENTS_BY_CATEGORY"
    FILTER_COMPONENTS_BY_MULTIPLE_CATEGORIES = "FILTER_COMPONENTS_BY_MULTIPLE_CATEGORIES"
    FILTER_COMPONENTS_BY_USAGES = "FILTER_COMPONENTS_BY_USAGES"
    CLICK_COMPONENT_USAGES = "CLICK_COMPONENT_USAGES"
    SEARCH_COMPONENT_USAGES_BY_NAME = "SEARCH_COMPONENT_USAGES_BY_NAME"
    FILTER_COMPONENT_USAGES_BY_STATUS = "FILTER_COMPONENT_USAGES_BY_STATUS"
    FILTER_COMPONENT_USAGES_BY_CATEGORY = "FILTER_COMPONENT_USAGES_BY_CATEGORY"
    FILTER_COMPONENT_USAGES_BY_AUTHOR = "FILTER_COMPONENT_USAGES_BY_AUTHOR"
    FILTER_COMPONENT_USAGES_BY_OTHER = "FILTER_COMPONENT_USAGES_BY_OTHER"
    CLICK_SCENARIO_FROM_COMPONENT_USAGES = "CLICK_SCENARIO_FROM_COMPONENT_USAGES"
    CLICK_GLOBAL_METRICS_TAB = "CLICK_GLOBAL_METRICS_TAB"
    CLICK_ACTION_DEPLOY = "CLICK_ACTION_DEPLOY"
    CLICK_ACTION_METRICS = "CLICK_ACTION_METRICS"
    CLICK_VIEW_ZOOM_IN = "CLICK_VIEW_ZOOM_IN"
    CLICK_VIEW_ZOOM_OUT = "CLICK_VIEW_ZOOM_OUT"
    CLICK_VIEW_RESET = "CLICK_VIEW_RESET"
    CLICK_EDIT_UNDO = "CLICK_EDIT_UNDO"
    CLICK_EDIT_REDO = "CLICK_EDIT_REDO"
    CLICK_EDIT_COPY = "CLICK_EDIT_COPY"
    CLICK_EDIT_PASTE = "CLICK_EDIT_PASTE"
    CLICK_EDIT_DELETE = "CLICK_EDIT_DELETE"
    CLICK_EDIT_LAYOUT = "CLICK_EDIT_LAYOUT"
    CLICK_SCENARIO_PROPERTIES = "CLICK_SCENARIO_PROPERTIES"
    CLICK_SCENARIO_COMPARE = "CLICK_SCENARIO_COMPARE"
    CLICK_SCENARIO_MIGRATE = "CLICK_SCENARIO_MIGRATE"
    CLICK_SCENARIO_IMPORT = "CLICK_SCENARIO_IMPORT"
    CLICK_SCENARIO_EXPORT = "CLICK_SCENARIO_EXPORT"
    CLICK_SCENARIO_PDF = "CLICK_SCENARIO_PDF"
    CLICK_SCENARIO_ARCHIVE = "CLICK_SCENARIO_ARCHIVE"
    CLICK_TEST_GENERATED = "CLICK_TEST_GENERATED"
    CLICK_TEST_ADHOC = "CLICK_TEST_ADHOC"
    CLICK_SCENARIO_TEST = "CLICK_SCENARIO_TEST"
    CLICK_TEST_FROM_FILE = "CLICK_TEST_FROM_FILE"
    CLICK_TEST_GENERATE_FILE = "CLICK_TEST_GENERATE_FILE"
    CLICK_TEST_HIDE = "CLICK_TEST_HIDE"
    CLICK_MORE_SCENARIO_DETAILS = "CLICK_MORE_SCENARIO_DETAILS"
    CLICK_EXPAND_PANEL = "CLICK_EXPAND_PANEL"
    CLICK_COLLAPSE_PANEL = "CLICK_COLLAPSE_PANEL"
    CLICK_SCENARIO_ACTIVITIES_ADD_ATTACHMENT = "CLICK_SCENARIO_ACTIVITIES_ADD_ATTACHMENT"
    CLICK_SCENARIO_ACTIVITIES_ADD_COMMENT = "CLICK_SCENARIO_ACTIVITIES_ADD_COMMENT"
    CLICK_LIVE_DATA = "CLICK_LIVE_DATA"
    CLICK_SCENARIO_ACTIVITIES_ADD_COMMENT_TO_ACTIVITY = "CLICK_SCENARIO_ACTIVITIES_ADD_COMMENT_TO_ACTIVITY"
    CLICK_SCENARIO_ACTIVITIES_COMPARE = "CLICK_SCENARIO_ACTIVITIES_COMPARE"
    CLICK_SCENARIO_ACTIVITIES_DOWNLOAD_ATTACHMENT = "CLICK_SCENARIO_ACTIVITIES_DOWNLOAD_ATTACHMENT"
    CLICK_SCENARIO_ACTIVITIES_DELETE_ATTACHMENT = "CLICK_SCENARIO_ACTIVITIES_DELETE_ATTACHMENT"
    CLICK_SCENARIO_ACTIVITIES_DELETE_COMMENT = "CLICK_SCENARIO_ACTIVITIES_DELETE_COMMENT"
    CLICK_SCENARIO_ACTIVITIES_EDIT_COMMENT = "CLICK_SCENARIO_ACTIVITIES_EDIT_COMMENT"
    CLICK_SCENARIO_ACTIVITIES_OPEN_VERSION = "CLICK_SCENARIO_ACTIVITIES_OPEN_VERSION"
    MOVE_TOOLBAR_PANEL = "MOVE_TOOLBAR_PANEL"
    SEARCH_NODES_IN_SCENARIO = "SEARCH_NODES_IN_SCENARIO"
    SEARCH_COMPONENTS_IN_SCENARIO = "SEARCH_COMPONENTS_IN_SCENARIO"
    CLICK_OLDER_VERSION = "CLICK_OLDER_VERSION"
    CLICK_NEWER_VERSION = "CLICK_NEWER_VERSION"
    CLICK_NODE_DOCUMENTATION = "CLICK_NODE_DOCUMENTATION"
    CLICK_COMPONENTS_TAB = "CLICK_COMPONENTS_TAB"
    CLICK_SCENARIO_SAVE = "CLICK_SCENARIO_SAVE"
    CLICK_TEST_COUNTS = "CLICK_TEST_COUNTS"
    CLICK_SCENARIO_CANCEL = "CLICK_SCENARIO_CANCEL"
    CLICK_SCENARIO_ARCHIVE_TOGGLE = "CLICK_SCENARIO_ARCHIVE_TOGGLE"
    CLICK_SCENARIO_UNARCHIVE = "CLICK_SCENARIO_UNARCHIVE"
    CLICK_SCENARIO_CUSTOM_LINK = "CLICK_SCENARIO_CUSTOM_LINK"
    DOUBLE_CLICK_RANGE_SELECT_NODES = "DOUBLE_CLICK_RANGE_SELECT_NODES"
    KEYBOARD_AND_CLICK_RANGE_SELECT_NODES = "KEYBOARD_AND_CLICK_RANGE_SELECT_NODES"
    KEYBOARD_COPY_NODE = "KEYBOARD_COPY_NODE"
    KEYBOARD_PASTE_NODE = "KEYBOARD_PASTE_NODE"
    KEYBOARD_CUT_NODE = "KEYBOARD_CUT_NODE"
    KEYBOARD_SELECT_ALL_NODES = "KEYBOARD_SELECT_ALL_NODES"
    KEYBOARD_REDO_SCENARIO_CHANGES = "KEYBOARD_REDO_SCENARIO_CHANGES"
    KEYBOARD_UNDO_SCENARIO_CHANGES = "KEYBOARD_UNDO_SCENARIO_CHANGES"
    KEYBOARD_DELETE_NODES = "KEYBOARD_DELETE_NODES"
    KEYBOARD_DESELECT_ALL_NODES = "KEYBOARD_DESELECT_ALL_NODES"
    KEYBOARD_FOCUS_SEARCH_NODE_FIELD = "KEYBOARD_FOCUS_SEARCH_NODE_FIELD"

    def visit(
        self,
        search_scenarios_by_name: typing.Callable[[], T_Result],
        filter_scenarios_by_status: typing.Callable[[], T_Result],
        filter_scenarios_by_processing_mode: typing.Callable[[], T_Result],
        filter_scenarios_by_category: typing.Callable[[], T_Result],
        filter_scenarios_by_author: typing.Callable[[], T_Result],
        filter_scenarios_by_other: typing.Callable[[], T_Result],
        sort_scenarios_by_sort_option: typing.Callable[[], T_Result],
        search_components_by_name: typing.Callable[[], T_Result],
        filter_components_by_group: typing.Callable[[], T_Result],
        filter_components_by_processing_mode: typing.Callable[[], T_Result],
        filter_components_by_category: typing.Callable[[], T_Result],
        filter_components_by_multiple_categories: typing.Callable[[], T_Result],
        filter_components_by_usages: typing.Callable[[], T_Result],
        click_component_usages: typing.Callable[[], T_Result],
        search_component_usages_by_name: typing.Callable[[], T_Result],
        filter_component_usages_by_status: typing.Callable[[], T_Result],
        filter_component_usages_by_category: typing.Callable[[], T_Result],
        filter_component_usages_by_author: typing.Callable[[], T_Result],
        filter_component_usages_by_other: typing.Callable[[], T_Result],
        click_scenario_from_component_usages: typing.Callable[[], T_Result],
        click_global_metrics_tab: typing.Callable[[], T_Result],
        click_action_deploy: typing.Callable[[], T_Result],
        click_action_metrics: typing.Callable[[], T_Result],
        click_view_zoom_in: typing.Callable[[], T_Result],
        click_view_zoom_out: typing.Callable[[], T_Result],
        click_view_reset: typing.Callable[[], T_Result],
        click_edit_undo: typing.Callable[[], T_Result],
        click_edit_redo: typing.Callable[[], T_Result],
        click_edit_copy: typing.Callable[[], T_Result],
        click_edit_paste: typing.Callable[[], T_Result],
        click_edit_delete: typing.Callable[[], T_Result],
        click_edit_layout: typing.Callable[[], T_Result],
        click_scenario_properties: typing.Callable[[], T_Result],
        click_scenario_compare: typing.Callable[[], T_Result],
        click_scenario_migrate: typing.Callable[[], T_Result],
        click_scenario_import: typing.Callable[[], T_Result],
        click_scenario_export: typing.Callable[[], T_Result],
        click_scenario_pdf: typing.Callable[[], T_Result],
        click_scenario_archive: typing.Callable[[], T_Result],
        click_test_generated: typing.Callable[[], T_Result],
        click_test_adhoc: typing.Callable[[], T_Result],
        click_scenario_test: typing.Callable[[], T_Result],
        click_test_from_file: typing.Callable[[], T_Result],
        click_test_generate_file: typing.Callable[[], T_Result],
        click_test_hide: typing.Callable[[], T_Result],
        click_more_scenario_details: typing.Callable[[], T_Result],
        click_expand_panel: typing.Callable[[], T_Result],
        click_collapse_panel: typing.Callable[[], T_Result],
        click_scenario_activities_add_attachment: typing.Callable[[], T_Result],
        click_scenario_activities_add_comment: typing.Callable[[], T_Result],
        click_live_data: typing.Callable[[], T_Result],
        click_scenario_activities_add_comment_to_activity: typing.Callable[[], T_Result],
        click_scenario_activities_compare: typing.Callable[[], T_Result],
        click_scenario_activities_download_attachment: typing.Callable[[], T_Result],
        click_scenario_activities_delete_attachment: typing.Callable[[], T_Result],
        click_scenario_activities_delete_comment: typing.Callable[[], T_Result],
        click_scenario_activities_edit_comment: typing.Callable[[], T_Result],
        click_scenario_activities_open_version: typing.Callable[[], T_Result],
        move_toolbar_panel: typing.Callable[[], T_Result],
        search_nodes_in_scenario: typing.Callable[[], T_Result],
        search_components_in_scenario: typing.Callable[[], T_Result],
        click_older_version: typing.Callable[[], T_Result],
        click_newer_version: typing.Callable[[], T_Result],
        click_node_documentation: typing.Callable[[], T_Result],
        click_components_tab: typing.Callable[[], T_Result],
        click_scenario_save: typing.Callable[[], T_Result],
        click_test_counts: typing.Callable[[], T_Result],
        click_scenario_cancel: typing.Callable[[], T_Result],
        click_scenario_archive_toggle: typing.Callable[[], T_Result],
        click_scenario_unarchive: typing.Callable[[], T_Result],
        click_scenario_custom_link: typing.Callable[[], T_Result],
        double_click_range_select_nodes: typing.Callable[[], T_Result],
        keyboard_and_click_range_select_nodes: typing.Callable[[], T_Result],
        keyboard_copy_node: typing.Callable[[], T_Result],
        keyboard_paste_node: typing.Callable[[], T_Result],
        keyboard_cut_node: typing.Callable[[], T_Result],
        keyboard_select_all_nodes: typing.Callable[[], T_Result],
        keyboard_redo_scenario_changes: typing.Callable[[], T_Result],
        keyboard_undo_scenario_changes: typing.Callable[[], T_Result],
        keyboard_delete_nodes: typing.Callable[[], T_Result],
        keyboard_deselect_all_nodes: typing.Callable[[], T_Result],
        keyboard_focus_search_node_field: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StatisticName.SEARCH_SCENARIOS_BY_NAME:
            return search_scenarios_by_name()
        if self is StatisticName.FILTER_SCENARIOS_BY_STATUS:
            return filter_scenarios_by_status()
        if self is StatisticName.FILTER_SCENARIOS_BY_PROCESSING_MODE:
            return filter_scenarios_by_processing_mode()
        if self is StatisticName.FILTER_SCENARIOS_BY_CATEGORY:
            return filter_scenarios_by_category()
        if self is StatisticName.FILTER_SCENARIOS_BY_AUTHOR:
            return filter_scenarios_by_author()
        if self is StatisticName.FILTER_SCENARIOS_BY_OTHER:
            return filter_scenarios_by_other()
        if self is StatisticName.SORT_SCENARIOS_BY_SORT_OPTION:
            return sort_scenarios_by_sort_option()
        if self is StatisticName.SEARCH_COMPONENTS_BY_NAME:
            return search_components_by_name()
        if self is StatisticName.FILTER_COMPONENTS_BY_GROUP:
            return filter_components_by_group()
        if self is StatisticName.FILTER_COMPONENTS_BY_PROCESSING_MODE:
            return filter_components_by_processing_mode()
        if self is StatisticName.FILTER_COMPONENTS_BY_CATEGORY:
            return filter_components_by_category()
        if self is StatisticName.FILTER_COMPONENTS_BY_MULTIPLE_CATEGORIES:
            return filter_components_by_multiple_categories()
        if self is StatisticName.FILTER_COMPONENTS_BY_USAGES:
            return filter_components_by_usages()
        if self is StatisticName.CLICK_COMPONENT_USAGES:
            return click_component_usages()
        if self is StatisticName.SEARCH_COMPONENT_USAGES_BY_NAME:
            return search_component_usages_by_name()
        if self is StatisticName.FILTER_COMPONENT_USAGES_BY_STATUS:
            return filter_component_usages_by_status()
        if self is StatisticName.FILTER_COMPONENT_USAGES_BY_CATEGORY:
            return filter_component_usages_by_category()
        if self is StatisticName.FILTER_COMPONENT_USAGES_BY_AUTHOR:
            return filter_component_usages_by_author()
        if self is StatisticName.FILTER_COMPONENT_USAGES_BY_OTHER:
            return filter_component_usages_by_other()
        if self is StatisticName.CLICK_SCENARIO_FROM_COMPONENT_USAGES:
            return click_scenario_from_component_usages()
        if self is StatisticName.CLICK_GLOBAL_METRICS_TAB:
            return click_global_metrics_tab()
        if self is StatisticName.CLICK_ACTION_DEPLOY:
            return click_action_deploy()
        if self is StatisticName.CLICK_ACTION_METRICS:
            return click_action_metrics()
        if self is StatisticName.CLICK_VIEW_ZOOM_IN:
            return click_view_zoom_in()
        if self is StatisticName.CLICK_VIEW_ZOOM_OUT:
            return click_view_zoom_out()
        if self is StatisticName.CLICK_VIEW_RESET:
            return click_view_reset()
        if self is StatisticName.CLICK_EDIT_UNDO:
            return click_edit_undo()
        if self is StatisticName.CLICK_EDIT_REDO:
            return click_edit_redo()
        if self is StatisticName.CLICK_EDIT_COPY:
            return click_edit_copy()
        if self is StatisticName.CLICK_EDIT_PASTE:
            return click_edit_paste()
        if self is StatisticName.CLICK_EDIT_DELETE:
            return click_edit_delete()
        if self is StatisticName.CLICK_EDIT_LAYOUT:
            return click_edit_layout()
        if self is StatisticName.CLICK_SCENARIO_PROPERTIES:
            return click_scenario_properties()
        if self is StatisticName.CLICK_SCENARIO_COMPARE:
            return click_scenario_compare()
        if self is StatisticName.CLICK_SCENARIO_MIGRATE:
            return click_scenario_migrate()
        if self is StatisticName.CLICK_SCENARIO_IMPORT:
            return click_scenario_import()
        if self is StatisticName.CLICK_SCENARIO_EXPORT:
            return click_scenario_export()
        if self is StatisticName.CLICK_SCENARIO_PDF:
            return click_scenario_pdf()
        if self is StatisticName.CLICK_SCENARIO_ARCHIVE:
            return click_scenario_archive()
        if self is StatisticName.CLICK_TEST_GENERATED:
            return click_test_generated()
        if self is StatisticName.CLICK_TEST_ADHOC:
            return click_test_adhoc()
        if self is StatisticName.CLICK_SCENARIO_TEST:
            return click_scenario_test()
        if self is StatisticName.CLICK_TEST_FROM_FILE:
            return click_test_from_file()
        if self is StatisticName.CLICK_TEST_GENERATE_FILE:
            return click_test_generate_file()
        if self is StatisticName.CLICK_TEST_HIDE:
            return click_test_hide()
        if self is StatisticName.CLICK_MORE_SCENARIO_DETAILS:
            return click_more_scenario_details()
        if self is StatisticName.CLICK_EXPAND_PANEL:
            return click_expand_panel()
        if self is StatisticName.CLICK_COLLAPSE_PANEL:
            return click_collapse_panel()
        if self is StatisticName.CLICK_SCENARIO_ACTIVITIES_ADD_ATTACHMENT:
            return click_scenario_activities_add_attachment()
        if self is StatisticName.CLICK_SCENARIO_ACTIVITIES_ADD_COMMENT:
            return click_scenario_activities_add_comment()
        if self is StatisticName.CLICK_LIVE_DATA:
            return click_live_data()
        if self is StatisticName.CLICK_SCENARIO_ACTIVITIES_ADD_COMMENT_TO_ACTIVITY:
            return click_scenario_activities_add_comment_to_activity()
        if self is StatisticName.CLICK_SCENARIO_ACTIVITIES_COMPARE:
            return click_scenario_activities_compare()
        if self is StatisticName.CLICK_SCENARIO_ACTIVITIES_DOWNLOAD_ATTACHMENT:
            return click_scenario_activities_download_attachment()
        if self is StatisticName.CLICK_SCENARIO_ACTIVITIES_DELETE_ATTACHMENT:
            return click_scenario_activities_delete_attachment()
        if self is StatisticName.CLICK_SCENARIO_ACTIVITIES_DELETE_COMMENT:
            return click_scenario_activities_delete_comment()
        if self is StatisticName.CLICK_SCENARIO_ACTIVITIES_EDIT_COMMENT:
            return click_scenario_activities_edit_comment()
        if self is StatisticName.CLICK_SCENARIO_ACTIVITIES_OPEN_VERSION:
            return click_scenario_activities_open_version()
        if self is StatisticName.MOVE_TOOLBAR_PANEL:
            return move_toolbar_panel()
        if self is StatisticName.SEARCH_NODES_IN_SCENARIO:
            return search_nodes_in_scenario()
        if self is StatisticName.SEARCH_COMPONENTS_IN_SCENARIO:
            return search_components_in_scenario()
        if self is StatisticName.CLICK_OLDER_VERSION:
            return click_older_version()
        if self is StatisticName.CLICK_NEWER_VERSION:
            return click_newer_version()
        if self is StatisticName.CLICK_NODE_DOCUMENTATION:
            return click_node_documentation()
        if self is StatisticName.CLICK_COMPONENTS_TAB:
            return click_components_tab()
        if self is StatisticName.CLICK_SCENARIO_SAVE:
            return click_scenario_save()
        if self is StatisticName.CLICK_TEST_COUNTS:
            return click_test_counts()
        if self is StatisticName.CLICK_SCENARIO_CANCEL:
            return click_scenario_cancel()
        if self is StatisticName.CLICK_SCENARIO_ARCHIVE_TOGGLE:
            return click_scenario_archive_toggle()
        if self is StatisticName.CLICK_SCENARIO_UNARCHIVE:
            return click_scenario_unarchive()
        if self is StatisticName.CLICK_SCENARIO_CUSTOM_LINK:
            return click_scenario_custom_link()
        if self is StatisticName.DOUBLE_CLICK_RANGE_SELECT_NODES:
            return double_click_range_select_nodes()
        if self is StatisticName.KEYBOARD_AND_CLICK_RANGE_SELECT_NODES:
            return keyboard_and_click_range_select_nodes()
        if self is StatisticName.KEYBOARD_COPY_NODE:
            return keyboard_copy_node()
        if self is StatisticName.KEYBOARD_PASTE_NODE:
            return keyboard_paste_node()
        if self is StatisticName.KEYBOARD_CUT_NODE:
            return keyboard_cut_node()
        if self is StatisticName.KEYBOARD_SELECT_ALL_NODES:
            return keyboard_select_all_nodes()
        if self is StatisticName.KEYBOARD_REDO_SCENARIO_CHANGES:
            return keyboard_redo_scenario_changes()
        if self is StatisticName.KEYBOARD_UNDO_SCENARIO_CHANGES:
            return keyboard_undo_scenario_changes()
        if self is StatisticName.KEYBOARD_DELETE_NODES:
            return keyboard_delete_nodes()
        if self is StatisticName.KEYBOARD_DESELECT_ALL_NODES:
            return keyboard_deselect_all_nodes()
        if self is StatisticName.KEYBOARD_FOCUS_SEARCH_NODE_FIELD:
            return keyboard_focus_search_node_field()
