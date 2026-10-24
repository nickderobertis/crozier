



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        Circuit,
        Condition,
        ConditionValueItem,
        Data,
        DataType,
        DataTypeResult,
        DataTypes,
        Field,
        FieldDef,
        FieldTemplate,
        FieldValue,
        Global,
        Message,
        MessageCondition,
        MessageId,
        RawMessage,
        RawMessages,
        Seconds,
        Symbol,
        Symbols,
        Templates,
        TemplatesItem,
        TemplatesItemName,
    )
    from .errors import BadRequestError, ForbiddenError, InternalServerError, NotFoundError
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "Circuit": ".types",
    "Condition": ".types",
    "ConditionValueItem": ".types",
    "Data": ".types",
    "DataType": ".types",
    "DataTypeResult": ".types",
    "DataTypes": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "Field": ".types",
    "FieldDef": ".types",
    "FieldTemplate": ".types",
    "FieldValue": ".types",
    "ForbiddenError": ".errors",
    "Global": ".types",
    "InternalServerError": ".errors",
    "Message": ".types",
    "MessageCondition": ".types",
    "MessageId": ".types",
    "NotFoundError": ".errors",
    "RawMessage": ".types",
    "RawMessages": ".types",
    "Seconds": ".types",
    "Symbol": ".types",
    "Symbols": ".types",
    "Templates": ".types",
    "TemplatesItem": ".types",
    "TemplatesItemName": ".types",
    "__version__": ".version",
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
    "AsyncFernApi",
    "BadRequestError",
    "Circuit",
    "Condition",
    "ConditionValueItem",
    "Data",
    "DataType",
    "DataTypeResult",
    "DataTypes",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FernApi",
    "FernApiEnvironment",
    "Field",
    "FieldDef",
    "FieldTemplate",
    "FieldValue",
    "ForbiddenError",
    "Global",
    "InternalServerError",
    "Message",
    "MessageCondition",
    "MessageId",
    "NotFoundError",
    "RawMessage",
    "RawMessages",
    "Seconds",
    "Symbol",
    "Symbols",
    "Templates",
    "TemplatesItem",
    "TemplatesItemName",
    "__version__",
]
