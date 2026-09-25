



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_drafts_response import CreateDraftsResponse
    from .create_saved_snippet_response import CreateSavedSnippetResponse
    from .edit_draft_request_draft import EditDraftRequestDraft
    from .edit_draft_request_draft_type import EditDraftRequestDraftType
    from .get_drafts_response import GetDraftsResponse
    from .get_saved_snippets_response import GetSavedSnippetsResponse
_dynamic_imports: typing.Dict[str, str] = {
    "CreateDraftsResponse": ".create_drafts_response",
    "CreateSavedSnippetResponse": ".create_saved_snippet_response",
    "EditDraftRequestDraft": ".edit_draft_request_draft",
    "EditDraftRequestDraftType": ".edit_draft_request_draft_type",
    "GetDraftsResponse": ".get_drafts_response",
    "GetSavedSnippetsResponse": ".get_saved_snippets_response",
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
    "CreateDraftsResponse",
    "CreateSavedSnippetResponse",
    "EditDraftRequestDraft",
    "EditDraftRequestDraftType",
    "GetDraftsResponse",
    "GetSavedSnippetsResponse",
]
