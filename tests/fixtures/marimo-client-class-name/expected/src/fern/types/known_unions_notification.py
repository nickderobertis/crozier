

import typing

from .active_line_notification import ActiveLineNotification
from .alert_notification import AlertNotification
from .banner_notification import BannerNotification
from .cache_cleared_notification import CacheClearedNotification
from .cache_info_notification import CacheInfoNotification
from .cell_notification import CellNotification
from .completed_run_notification import CompletedRunNotification
from .completion_result_notification import CompletionResultNotification
from .consumer_capabilities_notification import ConsumerCapabilitiesNotification
from .data_column_preview_notification import DataColumnPreviewNotification
from .data_source_connections_notification import DataSourceConnectionsNotification
from .data_source_discovery_result_notification import DataSourceDiscoveryResultNotification
from .datasets_notification import DatasetsNotification
from .focus_cell_notification import FocusCellNotification
from .function_call_result_notification import FunctionCallResultNotification
from .installing_package_alert_notification import InstallingPackageAlertNotification
from .interrupted_notification import InterruptedNotification
from .kernel_ready_notification import KernelReadyNotification
from .kernel_startup_error_notification import KernelStartupErrorNotification
from .missing_package_alert_notification import MissingPackageAlertNotification
from .model_lifecycle_notification import ModelLifecycleNotification
from .notebook_document_transaction_notification import NotebookDocumentTransactionNotification
from .query_params_append_notification import QueryParamsAppendNotification
from .query_params_clear_notification import QueryParamsClearNotification
from .query_params_delete_notification import QueryParamsDeleteNotification
from .query_params_set_notification import QueryParamsSetNotification
from .reconnected_notification import ReconnectedNotification
from .reload_notification import ReloadNotification
from .remove_ui_elements_notification import RemoveUiElementsNotification
from .secret_keys_result_notification import SecretKeysResultNotification
from .sql_schema_list_preview_notification import SqlSchemaListPreviewNotification
from .sql_table_list_preview_notification import SqlTableListPreviewNotification
from .sql_table_preview_notification import SqlTablePreviewNotification
from .startup_logs_notification import StartupLogsNotification
from .storage_download_ready_notification import StorageDownloadReadyNotification
from .storage_entries_notification import StorageEntriesNotification
from .storage_namespaces_notification import StorageNamespacesNotification
from .ui_element_message_notification import UiElementMessageNotification
from .validate_sql_result_notification import ValidateSqlResultNotification
from .variable_values_notification import VariableValuesNotification
from .variables_notification import VariablesNotification

KnownUnionsNotification = typing.Union[
    CellNotification,
    FunctionCallResultNotification,
    UiElementMessageNotification,
    ModelLifecycleNotification,
    RemoveUiElementsNotification,
    ReloadNotification,
    ReconnectedNotification,
    InterruptedNotification,
    CompletedRunNotification,
    KernelReadyNotification,
    CompletionResultNotification,
    AlertNotification,
    BannerNotification,
    MissingPackageAlertNotification,
    InstallingPackageAlertNotification,
    StartupLogsNotification,
    KernelStartupErrorNotification,
    VariablesNotification,
    VariableValuesNotification,
    QueryParamsSetNotification,
    QueryParamsAppendNotification,
    QueryParamsDeleteNotification,
    QueryParamsClearNotification,
    DatasetsNotification,
    DataColumnPreviewNotification,
    SqlTablePreviewNotification,
    SqlTableListPreviewNotification,
    SqlSchemaListPreviewNotification,
    DataSourceConnectionsNotification,
    DataSourceDiscoveryResultNotification,
    ValidateSqlResultNotification,
    StorageNamespacesNotification,
    StorageEntriesNotification,
    StorageDownloadReadyNotification,
    SecretKeysResultNotification,
    CacheClearedNotification,
    CacheInfoNotification,
    FocusCellNotification,
    ActiveLineNotification,
    NotebookDocumentTransactionNotification,
    ConsumerCapabilitiesNotification,
]
