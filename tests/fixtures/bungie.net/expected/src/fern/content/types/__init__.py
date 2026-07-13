



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .content_get_content_by_id_response import ContentGetContentByIdResponse
    from .content_get_content_by_tag_and_type_response import ContentGetContentByTagAndTypeResponse
    from .content_get_content_type_response import ContentGetContentTypeResponse
    from .content_rss_news_articles_response import ContentRssNewsArticlesResponse
    from .content_search_content_by_tag_and_type_response import ContentSearchContentByTagAndTypeResponse
    from .content_search_content_with_text_response import ContentSearchContentWithTextResponse
    from .content_search_help_articles_response import ContentSearchHelpArticlesResponse
_dynamic_imports: typing.Dict[str, str] = {
    "ContentGetContentByIdResponse": ".content_get_content_by_id_response",
    "ContentGetContentByTagAndTypeResponse": ".content_get_content_by_tag_and_type_response",
    "ContentGetContentTypeResponse": ".content_get_content_type_response",
    "ContentRssNewsArticlesResponse": ".content_rss_news_articles_response",
    "ContentSearchContentByTagAndTypeResponse": ".content_search_content_by_tag_and_type_response",
    "ContentSearchContentWithTextResponse": ".content_search_content_with_text_response",
    "ContentSearchHelpArticlesResponse": ".content_search_help_articles_response",
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
    "ContentGetContentByIdResponse",
    "ContentGetContentByTagAndTypeResponse",
    "ContentGetContentTypeResponse",
    "ContentRssNewsArticlesResponse",
    "ContentSearchContentByTagAndTypeResponse",
    "ContentSearchContentWithTextResponse",
    "ContentSearchHelpArticlesResponse",
]
