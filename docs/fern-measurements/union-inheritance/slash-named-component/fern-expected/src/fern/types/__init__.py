



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .notebooks_list_response import NotebooksListResponse
    from .notebooks_list_response_notebooks_item import NotebooksListResponseNotebooksItem
    from .pages_request_response import PagesRequestResponse
    from .pages_request_response_page import PagesRequestResponsePage
    from .pages_request_response_page_content import PagesRequestResponsePageContent
    from .pages_request_response_page_one import PagesRequestResponsePageOne
    from .pages_request_response_page_two import PagesRequestResponsePageTwo
_dynamic_imports: typing.Dict[str, str] = {
    "NotebooksListResponse": ".notebooks_list_response",
    "NotebooksListResponseNotebooksItem": ".notebooks_list_response_notebooks_item",
    "PagesRequestResponse": ".pages_request_response",
    "PagesRequestResponsePage": ".pages_request_response_page",
    "PagesRequestResponsePageContent": ".pages_request_response_page_content",
    "PagesRequestResponsePageOne": ".pages_request_response_page_one",
    "PagesRequestResponsePageTwo": ".pages_request_response_page_two",
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
    "NotebooksListResponse",
    "NotebooksListResponseNotebooksItem",
    "PagesRequestResponse",
    "PagesRequestResponsePage",
    "PagesRequestResponsePageContent",
    "PagesRequestResponsePageOne",
    "PagesRequestResponsePageTwo",
]
