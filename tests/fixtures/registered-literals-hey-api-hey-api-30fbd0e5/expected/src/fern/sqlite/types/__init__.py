



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .sqlite_batch_request_mode import SqliteBatchRequestMode
    from .sqlite_batch_request_statements_item import SqliteBatchRequestStatementsItem
    from .sqlite_batch_request_statements_item_args import SqliteBatchRequestStatementsItemArgs
    from .sqlite_batch_request_statements_item_args_args import SqliteBatchRequestStatementsItemArgsArgs
    from .sqlite_execute_request_statement import SqliteExecuteRequestStatement
    from .sqlite_execute_request_statement_args import SqliteExecuteRequestStatementArgs
    from .sqlite_execute_request_statement_args_args import SqliteExecuteRequestStatementArgsArgs
_dynamic_imports: typing.Dict[str, str] = {
    "SqliteBatchRequestMode": ".sqlite_batch_request_mode",
    "SqliteBatchRequestStatementsItem": ".sqlite_batch_request_statements_item",
    "SqliteBatchRequestStatementsItemArgs": ".sqlite_batch_request_statements_item_args",
    "SqliteBatchRequestStatementsItemArgsArgs": ".sqlite_batch_request_statements_item_args_args",
    "SqliteExecuteRequestStatement": ".sqlite_execute_request_statement",
    "SqliteExecuteRequestStatementArgs": ".sqlite_execute_request_statement_args",
    "SqliteExecuteRequestStatementArgsArgs": ".sqlite_execute_request_statement_args_args",
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
    "SqliteBatchRequestMode",
    "SqliteBatchRequestStatementsItem",
    "SqliteBatchRequestStatementsItemArgs",
    "SqliteBatchRequestStatementsItemArgsArgs",
    "SqliteExecuteRequestStatement",
    "SqliteExecuteRequestStatementArgs",
    "SqliteExecuteRequestStatementArgsArgs",
]
