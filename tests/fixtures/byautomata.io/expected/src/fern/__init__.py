



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        Article,
        ContentProCompany,
        ContentProSnippets,
        InputCompany,
        SimilarCompany,
        SimilarCompanySearch,
        Snippet,
    )
    from .errors import BadRequestError, ForbiddenError, NotImplementedError
    from . import contentpro_search, contentpro_similar_text, search, similar
    from .client import AsyncFernApi, FernApi
    from .contentpro_search import GetContentproSearchResponse, GetContentproSearchResponseDataItem
    from .contentpro_similar_text import PostContentproSimilarTextResponse, PostContentproSimilarTextResponseDataItem
    from .environment import FernApiEnvironment
    from .search import GetSearchResponse
    from .similar import GetSimilarResponse
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "Article": ".types",
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "ContentProCompany": ".types",
    "ContentProSnippets": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "ForbiddenError": ".errors",
    "GetContentproSearchResponse": ".contentpro_search",
    "GetContentproSearchResponseDataItem": ".contentpro_search",
    "GetSearchResponse": ".search",
    "GetSimilarResponse": ".similar",
    "InputCompany": ".types",
    "NotImplementedError": ".errors",
    "PostContentproSimilarTextResponse": ".contentpro_similar_text",
    "PostContentproSimilarTextResponseDataItem": ".contentpro_similar_text",
    "SimilarCompany": ".types",
    "SimilarCompanySearch": ".types",
    "Snippet": ".types",
    "__version__": ".version",
    "contentpro_search": ".contentpro_search",
    "contentpro_similar_text": ".contentpro_similar_text",
    "search": ".search",
    "similar": ".similar",
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
    "Article",
    "AsyncFernApi",
    "BadRequestError",
    "ContentProCompany",
    "ContentProSnippets",
    "FernApi",
    "FernApiEnvironment",
    "ForbiddenError",
    "GetContentproSearchResponse",
    "GetContentproSearchResponseDataItem",
    "GetSearchResponse",
    "GetSimilarResponse",
    "InputCompany",
    "NotImplementedError",
    "PostContentproSimilarTextResponse",
    "PostContentproSimilarTextResponseDataItem",
    "SimilarCompany",
    "SimilarCompanySearch",
    "Snippet",
    "__version__",
    "contentpro_search",
    "contentpro_similar_text",
    "search",
    "similar",
]
