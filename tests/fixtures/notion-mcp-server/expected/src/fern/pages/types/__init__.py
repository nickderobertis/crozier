



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .retrieve_page_markdown_response import RetrievePageMarkdownResponse
    from .update_page_markdown_request_insert_content import UpdatePageMarkdownRequestInsertContent
    from .update_page_markdown_request_insert_content_position import UpdatePageMarkdownRequestInsertContentPosition
    from .update_page_markdown_request_insert_content_position_type import (
        UpdatePageMarkdownRequestInsertContentPositionType,
    )
    from .update_page_markdown_request_replace_content import UpdatePageMarkdownRequestReplaceContent
    from .update_page_markdown_request_replace_content_range import UpdatePageMarkdownRequestReplaceContentRange
    from .update_page_markdown_request_type import UpdatePageMarkdownRequestType
    from .update_page_markdown_request_update_content import UpdatePageMarkdownRequestUpdateContent
    from .update_page_markdown_request_update_content_content_updates_item import (
        UpdatePageMarkdownRequestUpdateContentContentUpdatesItem,
    )
    from .update_page_markdown_response import UpdatePageMarkdownResponse
_dynamic_imports: typing.Dict[str, str] = {
    "RetrievePageMarkdownResponse": ".retrieve_page_markdown_response",
    "UpdatePageMarkdownRequestInsertContent": ".update_page_markdown_request_insert_content",
    "UpdatePageMarkdownRequestInsertContentPosition": ".update_page_markdown_request_insert_content_position",
    "UpdatePageMarkdownRequestInsertContentPositionType": ".update_page_markdown_request_insert_content_position_type",
    "UpdatePageMarkdownRequestReplaceContent": ".update_page_markdown_request_replace_content",
    "UpdatePageMarkdownRequestReplaceContentRange": ".update_page_markdown_request_replace_content_range",
    "UpdatePageMarkdownRequestType": ".update_page_markdown_request_type",
    "UpdatePageMarkdownRequestUpdateContent": ".update_page_markdown_request_update_content",
    "UpdatePageMarkdownRequestUpdateContentContentUpdatesItem": ".update_page_markdown_request_update_content_content_updates_item",
    "UpdatePageMarkdownResponse": ".update_page_markdown_response",
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
    "RetrievePageMarkdownResponse",
    "UpdatePageMarkdownRequestInsertContent",
    "UpdatePageMarkdownRequestInsertContentPosition",
    "UpdatePageMarkdownRequestInsertContentPositionType",
    "UpdatePageMarkdownRequestReplaceContent",
    "UpdatePageMarkdownRequestReplaceContentRange",
    "UpdatePageMarkdownRequestType",
    "UpdatePageMarkdownRequestUpdateContent",
    "UpdatePageMarkdownRequestUpdateContentContentUpdatesItem",
    "UpdatePageMarkdownResponse",
]
