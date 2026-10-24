



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .circuit import Circuit
    from .condition import Condition
    from .condition_value_item import ConditionValueItem
    from .data import Data
    from .data_type import DataType
    from .data_type_result import DataTypeResult
    from .data_types import DataTypes
    from .field import Field
    from .field_def import FieldDef
    from .field_template import FieldTemplate
    from .field_value import FieldValue
    from .global_ import Global
    from .message import Message
    from .message_condition import MessageCondition
    from .message_id import MessageId
    from .raw_message import RawMessage
    from .raw_messages import RawMessages
    from .seconds import Seconds
    from .symbol import Symbol
    from .symbols import Symbols
    from .templates import Templates
    from .templates_item import TemplatesItem
    from .templates_item_name import TemplatesItemName
_dynamic_imports: typing.Dict[str, str] = {
    "Circuit": ".circuit",
    "Condition": ".condition",
    "ConditionValueItem": ".condition_value_item",
    "Data": ".data",
    "DataType": ".data_type",
    "DataTypeResult": ".data_type_result",
    "DataTypes": ".data_types",
    "Field": ".field",
    "FieldDef": ".field_def",
    "FieldTemplate": ".field_template",
    "FieldValue": ".field_value",
    "Global": ".global_",
    "Message": ".message",
    "MessageCondition": ".message_condition",
    "MessageId": ".message_id",
    "RawMessage": ".raw_message",
    "RawMessages": ".raw_messages",
    "Seconds": ".seconds",
    "Symbol": ".symbol",
    "Symbols": ".symbols",
    "Templates": ".templates",
    "TemplatesItem": ".templates_item",
    "TemplatesItemName": ".templates_item_name",
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
    "Circuit",
    "Condition",
    "ConditionValueItem",
    "Data",
    "DataType",
    "DataTypeResult",
    "DataTypes",
    "Field",
    "FieldDef",
    "FieldTemplate",
    "FieldValue",
    "Global",
    "Message",
    "MessageCondition",
    "MessageId",
    "RawMessage",
    "RawMessages",
    "Seconds",
    "Symbol",
    "Symbols",
    "Templates",
    "TemplatesItem",
    "TemplatesItemName",
]
