



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .double_nested_list_schema import DoubleNestedListSchema
    from .double_nested_map_schema import DoubleNestedMapSchema
    from .double_nested_set_schema import DoubleNestedSetSchema
    from .edgecase_provider import EdgecaseProvider
    from .get_map_test_response import GetMapTestResponse
    from .get_nested_collections_response import GetNestedCollectionsResponse
    from .get_obj_no_type_response import GetObjNoTypeResponse
    from .get_obj_no_type_response_nested_obj import GetObjNoTypeResponseNestedObj
    from .get_set_test_response import GetSetTestResponse
    from .map_allof_oneof_stringified import MapAllofOneofStringified
    from .mapnested_allof_oneof_nullable import MapnestedAllofOneofNullable
    from .mapnested_schema import MapnestedSchema
    from .mapnested_schema_value import MapnestedSchemaValue
    from .nullable_object import NullableObject
    from .setnested_schema import SetnestedSchema
    from .setnested_schema_item import SetnestedSchemaItem
    from .stringable_number import StringableNumber
    from .triple_nested_map_schema import TripleNestedMapSchema
    from .triple_nested_map_schema_item_item_value import TripleNestedMapSchemaItemItemValue
    from .triple_nested_map_schema_item_item_value_obj_prop import TripleNestedMapSchemaItemItemValueObjProp
_dynamic_imports: typing.Dict[str, str] = {
    "DoubleNestedListSchema": ".double_nested_list_schema",
    "DoubleNestedMapSchema": ".double_nested_map_schema",
    "DoubleNestedSetSchema": ".double_nested_set_schema",
    "EdgecaseProvider": ".edgecase_provider",
    "GetMapTestResponse": ".get_map_test_response",
    "GetNestedCollectionsResponse": ".get_nested_collections_response",
    "GetObjNoTypeResponse": ".get_obj_no_type_response",
    "GetObjNoTypeResponseNestedObj": ".get_obj_no_type_response_nested_obj",
    "GetSetTestResponse": ".get_set_test_response",
    "MapAllofOneofStringified": ".map_allof_oneof_stringified",
    "MapnestedAllofOneofNullable": ".mapnested_allof_oneof_nullable",
    "MapnestedSchema": ".mapnested_schema",
    "MapnestedSchemaValue": ".mapnested_schema_value",
    "NullableObject": ".nullable_object",
    "SetnestedSchema": ".setnested_schema",
    "SetnestedSchemaItem": ".setnested_schema_item",
    "StringableNumber": ".stringable_number",
    "TripleNestedMapSchema": ".triple_nested_map_schema",
    "TripleNestedMapSchemaItemItemValue": ".triple_nested_map_schema_item_item_value",
    "TripleNestedMapSchemaItemItemValueObjProp": ".triple_nested_map_schema_item_item_value_obj_prop",
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
    "DoubleNestedListSchema",
    "DoubleNestedMapSchema",
    "DoubleNestedSetSchema",
    "EdgecaseProvider",
    "GetMapTestResponse",
    "GetNestedCollectionsResponse",
    "GetObjNoTypeResponse",
    "GetObjNoTypeResponseNestedObj",
    "GetSetTestResponse",
    "MapAllofOneofStringified",
    "MapnestedAllofOneofNullable",
    "MapnestedSchema",
    "MapnestedSchemaValue",
    "NullableObject",
    "SetnestedSchema",
    "SetnestedSchemaItem",
    "StringableNumber",
    "TripleNestedMapSchema",
    "TripleNestedMapSchemaItemItemValue",
    "TripleNestedMapSchemaItemItemValueObjProp",
]
