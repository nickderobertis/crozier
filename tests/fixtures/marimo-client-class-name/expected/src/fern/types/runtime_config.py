

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .runtime_config_auto_reload import RuntimeConfigAutoReload
from .runtime_config_default_auto_download_item import RuntimeConfigDefaultAutoDownloadItem
from .runtime_config_default_sql_output import RuntimeConfigDefaultSqlOutput
from .runtime_config_on_cell_change import RuntimeConfigOnCellChange
from .runtime_config_watcher_on_save import RuntimeConfigWatcherOnSave


class RuntimeConfig(UniversalBaseModel):
    """
    Configuration for runtime.

        **Keys.**

        - `auto_instantiate`: if `False`, cells won't automatically
            run on startup. This only applies when editing a notebook,
            and not when running as an application.
            The default is `True`.
        - `auto_reload`: if `lazy`, cells importing modified modules will marked
          as stale; if `autorun`, affected cells will be automatically run. similar
          to IPython's %autoreload extension but with more code intelligence.
        - `reactive_tests`: if `True`, marimo will automatically run pytest on cells containing only test functions and test classes.
          execution.
        - `on_cell_change`: if `lazy`, cells will be marked stale when their
          ancestors run but won't autorun; if `autorun`, cells will automatically
          run when their ancestors run.
        - `execution_type`: if `relaxed`, marimo will not clone cell declarations;
          if `strict` marimo will clone cell declarations by default, avoiding
          hidden potential state build up.
        - `watcher_on_save`: how to handle file changes when saving. `"lazy"` marks
            affected cells as stale, `"autorun"` automatically runs affected cells.
        - `output_max_bytes`: the maximum size in bytes of cell outputs; larger
            values may affect frontend performance
        - `serve_cached_sessions_in_apps`: if `True`, initialize applications with session cache.
            The default is `False`.
        - `std_stream_max_bytes`: the maximum size in bytes of console outputs;
          larger values may affect frontend performance
        - `pythonpath`: a list of directories to add to the Python search path.
            Directories will be added to the head of sys.path. Similar to the
            `PYTHONPATH` environment variable, the directories will be included in
            where Python will look for imported modules.
        - `dotenv`: a list of paths to `.env` files to load.
            If the file does not exist, it will be silently ignored.
            The default is `[".env"]` if a pyproject.toml is found, otherwise `[]`.
        - `default_sql_output`: the default output format for SQL queries. Can be one of:
            `"auto"`, `"native"`, `"polars"`, `"lazy-polars"`, or `"pandas"`.
            The default is `"auto"`.
        - `default_auto_download`: an Optional list of export types to automatically snapshot your notebook as:
           `html`, `markdown`, `ipynb`.
           The default is None.
        - `default_csv_encoding`: the default encoding for CSV exports.
            The default is `"utf-8"`.
        - `show_tracebacks`: if `True`, show detailed error tracebacks in run mode.
            When enabled, exceptions will display a clickable toast that opens a modal with the full traceback.
            The default is `False`.
    """

    auto_instantiate: bool
    auto_reload: RuntimeConfigAutoReload
    default_auto_download: typing.Optional[typing.List[RuntimeConfigDefaultAutoDownloadItem]] = None
    default_csv_encoding: typing.Optional[str] = None
    default_sql_output: RuntimeConfigDefaultSqlOutput
    dotenv: typing.Optional[typing.List[str]] = None
    on_cell_change: RuntimeConfigOnCellChange
    output_max_bytes: int
    pythonpath: typing.Optional[typing.List[str]] = None
    reactive_tests: bool
    serve_cached_sessions_in_apps: typing.Optional[bool] = None
    show_tracebacks: typing.Optional[bool] = None
    std_stream_max_bytes: int
    watcher_on_save: RuntimeConfigWatcherOnSave

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
