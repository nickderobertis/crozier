



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_all_accounts_request_provider import GetAllAccountsRequestProvider
    from .get_all_accounts_response import GetAllAccountsResponse
    from .get_all_accounts_response_links import GetAllAccountsResponseLinks
    from .get_all_accounts_response_links_first import GetAllAccountsResponseLinksFirst
    from .get_all_accounts_response_links_last import GetAllAccountsResponseLinksLast
    from .get_all_accounts_response_links_next import GetAllAccountsResponseLinksNext
    from .get_all_accounts_response_links_prev import GetAllAccountsResponseLinksPrev
    from .get_all_accounts_response_links_self import GetAllAccountsResponseLinksSelf
_dynamic_imports: typing.Dict[str, str] = {
    "GetAllAccountsRequestProvider": ".get_all_accounts_request_provider",
    "GetAllAccountsResponse": ".get_all_accounts_response",
    "GetAllAccountsResponseLinks": ".get_all_accounts_response_links",
    "GetAllAccountsResponseLinksFirst": ".get_all_accounts_response_links_first",
    "GetAllAccountsResponseLinksLast": ".get_all_accounts_response_links_last",
    "GetAllAccountsResponseLinksNext": ".get_all_accounts_response_links_next",
    "GetAllAccountsResponseLinksPrev": ".get_all_accounts_response_links_prev",
    "GetAllAccountsResponseLinksSelf": ".get_all_accounts_response_links_self",
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
    "GetAllAccountsRequestProvider",
    "GetAllAccountsResponse",
    "GetAllAccountsResponseLinks",
    "GetAllAccountsResponseLinksFirst",
    "GetAllAccountsResponseLinksLast",
    "GetAllAccountsResponseLinksNext",
    "GetAllAccountsResponseLinksPrev",
    "GetAllAccountsResponseLinksSelf",
]
