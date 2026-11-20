



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_params_default_object_query_request_filter import GetParamsDefaultObjectQueryRequestFilter
    from .get_params_default_object_query_response import GetParamsDefaultObjectQueryResponse
    from .get_params_default_object_query_response_filter import GetParamsDefaultObjectQueryResponseFilter
    from .get_params_mixed_query_request_statuses_item import GetParamsMixedQueryRequestStatusesItem
    from .get_params_mixed_query_response import GetParamsMixedQueryResponse
    from .get_params_simple_query_request_order_by import GetParamsSimpleQueryRequestOrderBy
    from .get_params_simple_query_response import GetParamsSimpleQueryResponse
    from .get_params_unexploded_object_query_request_filter import GetParamsUnexplodedObjectQueryRequestFilter
    from .get_params_unexploded_object_query_response import GetParamsUnexplodedObjectQueryResponse
    from .get_params_unexploded_object_query_response_filter import GetParamsUnexplodedObjectQueryResponseFilter
_dynamic_imports: typing.Dict[str, str] = {
    "GetParamsDefaultObjectQueryRequestFilter": ".get_params_default_object_query_request_filter",
    "GetParamsDefaultObjectQueryResponse": ".get_params_default_object_query_response",
    "GetParamsDefaultObjectQueryResponseFilter": ".get_params_default_object_query_response_filter",
    "GetParamsMixedQueryRequestStatusesItem": ".get_params_mixed_query_request_statuses_item",
    "GetParamsMixedQueryResponse": ".get_params_mixed_query_response",
    "GetParamsSimpleQueryRequestOrderBy": ".get_params_simple_query_request_order_by",
    "GetParamsSimpleQueryResponse": ".get_params_simple_query_response",
    "GetParamsUnexplodedObjectQueryRequestFilter": ".get_params_unexploded_object_query_request_filter",
    "GetParamsUnexplodedObjectQueryResponse": ".get_params_unexploded_object_query_response",
    "GetParamsUnexplodedObjectQueryResponseFilter": ".get_params_unexploded_object_query_response_filter",
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
    "GetParamsDefaultObjectQueryRequestFilter",
    "GetParamsDefaultObjectQueryResponse",
    "GetParamsDefaultObjectQueryResponseFilter",
    "GetParamsMixedQueryRequestStatusesItem",
    "GetParamsMixedQueryResponse",
    "GetParamsSimpleQueryRequestOrderBy",
    "GetParamsSimpleQueryResponse",
    "GetParamsUnexplodedObjectQueryRequestFilter",
    "GetParamsUnexplodedObjectQueryResponse",
    "GetParamsUnexplodedObjectQueryResponseFilter",
]
