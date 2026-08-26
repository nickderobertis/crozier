

import typing

from .clear_cache_command import ClearCacheCommand
from .code_completion_command import CodeCompletionCommand
from .create_notebook_command import CreateNotebookCommand
from .debug_cell_command import DebugCellCommand
from .delete_cell_command import DeleteCellCommand
from .discover_data_sources_command import DiscoverDataSourcesCommand
from .execute_cells_command import ExecuteCellsCommand
from .execute_scratchpad_command import ExecuteScratchpadCommand
from .execute_stale_cells_command import ExecuteStaleCellsCommand
from .get_cache_info_command import GetCacheInfoCommand
from .install_packages_command import InstallPackagesCommand
from .invoke_function_command import InvokeFunctionCommand
from .list_data_source_connection_command import ListDataSourceConnectionCommand
from .list_secret_keys_command import ListSecretKeysCommand
from .list_sql_schemas_command import ListSqlSchemasCommand
from .list_sql_tables_command import ListSqlTablesCommand
from .model_command import ModelCommand
from .preview_dataset_column_command import PreviewDatasetColumnCommand
from .preview_sql_table_command import PreviewSqlTableCommand
from .refresh_secrets_command import RefreshSecretsCommand
from .rename_notebook_command import RenameNotebookCommand
from .set_breakpoints_command import SetBreakpointsCommand
from .stop_kernel_command import StopKernelCommand
from .storage_download_command import StorageDownloadCommand
from .storage_list_entries_command import StorageListEntriesCommand
from .sync_graph_command import SyncGraphCommand
from .update_cell_config_command import UpdateCellConfigCommand
from .update_ui_element_command import UpdateUiElementCommand
from .update_user_config_command import UpdateUserConfigCommand
from .validate_sql_command import ValidateSqlCommand

KnownUnionsCommand = typing.Union[
    CreateNotebookCommand,
    RenameNotebookCommand,
    CodeCompletionCommand,
    ExecuteCellsCommand,
    ExecuteScratchpadCommand,
    ExecuteStaleCellsCommand,
    DebugCellCommand,
    SetBreakpointsCommand,
    DeleteCellCommand,
    SyncGraphCommand,
    UpdateCellConfigCommand,
    InstallPackagesCommand,
    UpdateUiElementCommand,
    ModelCommand,
    InvokeFunctionCommand,
    UpdateUserConfigCommand,
    PreviewDatasetColumnCommand,
    PreviewSqlTableCommand,
    ListSqlTablesCommand,
    ListSqlSchemasCommand,
    ValidateSqlCommand,
    ListDataSourceConnectionCommand,
    DiscoverDataSourcesCommand,
    StorageListEntriesCommand,
    StorageDownloadCommand,
    ListSecretKeysCommand,
    RefreshSecretsCommand,
    ClearCacheCommand,
    GetCacheInfoCommand,
    StopKernelCommand,
]
