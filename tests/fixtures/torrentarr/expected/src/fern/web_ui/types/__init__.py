



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .api_arr_open_item_request_kind import ApiArrOpenItemRequestKind
    from .api_log_content_request_format import ApiLogContentRequestFormat
    from .api_log_search_request_case import ApiLogSearchRequestCase
    from .api_log_search_request_include_rotated import ApiLogSearchRequestIncludeRotated
    from .api_log_search_request_regex import ApiLogSearchRequestRegex
    from .web_arr_open_item_request_kind import WebArrOpenItemRequestKind
    from .web_log_content_request_format import WebLogContentRequestFormat
    from .web_log_search_request_case import WebLogSearchRequestCase
    from .web_log_search_request_include_rotated import WebLogSearchRequestIncludeRotated
    from .web_log_search_request_regex import WebLogSearchRequestRegex
_dynamic_imports: typing.Dict[str, str] = {
    "ApiArrOpenItemRequestKind": ".api_arr_open_item_request_kind",
    "ApiLogContentRequestFormat": ".api_log_content_request_format",
    "ApiLogSearchRequestCase": ".api_log_search_request_case",
    "ApiLogSearchRequestIncludeRotated": ".api_log_search_request_include_rotated",
    "ApiLogSearchRequestRegex": ".api_log_search_request_regex",
    "WebArrOpenItemRequestKind": ".web_arr_open_item_request_kind",
    "WebLogContentRequestFormat": ".web_log_content_request_format",
    "WebLogSearchRequestCase": ".web_log_search_request_case",
    "WebLogSearchRequestIncludeRotated": ".web_log_search_request_include_rotated",
    "WebLogSearchRequestRegex": ".web_log_search_request_regex",
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
    "ApiArrOpenItemRequestKind",
    "ApiLogContentRequestFormat",
    "ApiLogSearchRequestCase",
    "ApiLogSearchRequestIncludeRotated",
    "ApiLogSearchRequestRegex",
    "WebArrOpenItemRequestKind",
    "WebLogContentRequestFormat",
    "WebLogSearchRequestCase",
    "WebLogSearchRequestIncludeRotated",
    "WebLogSearchRequestRegex",
]
