



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .kvdb_compact_status_get_response import KvdbCompactStatusGetResponse
    from .kvdb_csched_get_response_item import KvdbCschedGetResponseItem
    from .kvdb_media_class_get_response import KvdbMediaClassGetResponse
    from .kvdb_param_get_response import KvdbParamGetResponse
    from .kvdb_param_set_request_body import KvdbParamSetRequestBody
    from .kvdb_params_get_response import KvdbParamsGetResponse
_dynamic_imports: typing.Dict[str, str] = {
    "KvdbCompactStatusGetResponse": ".kvdb_compact_status_get_response",
    "KvdbCschedGetResponseItem": ".kvdb_csched_get_response_item",
    "KvdbMediaClassGetResponse": ".kvdb_media_class_get_response",
    "KvdbParamGetResponse": ".kvdb_param_get_response",
    "KvdbParamSetRequestBody": ".kvdb_param_set_request_body",
    "KvdbParamsGetResponse": ".kvdb_params_get_response",
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
    "KvdbCompactStatusGetResponse",
    "KvdbCschedGetResponseItem",
    "KvdbMediaClassGetResponse",
    "KvdbParamGetResponse",
    "KvdbParamSetRequestBody",
    "KvdbParamsGetResponse",
]
