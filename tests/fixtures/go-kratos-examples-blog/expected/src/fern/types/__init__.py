



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .article import Article
    from .create_article_reply import CreateArticleReply
    from .delete_article_reply import DeleteArticleReply
    from .get_article_reply import GetArticleReply
    from .google_protobuf_any import GoogleProtobufAny
    from .list_article_reply import ListArticleReply
    from .status import Status
    from .update_article_reply import UpdateArticleReply
_dynamic_imports: typing.Dict[str, str] = {
    "Article": ".article",
    "CreateArticleReply": ".create_article_reply",
    "DeleteArticleReply": ".delete_article_reply",
    "GetArticleReply": ".get_article_reply",
    "GoogleProtobufAny": ".google_protobuf_any",
    "ListArticleReply": ".list_article_reply",
    "Status": ".status",
    "UpdateArticleReply": ".update_article_reply",
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
    "CreateArticleReply",
    "DeleteArticleReply",
    "GetArticleReply",
    "GoogleProtobufAny",
    "ListArticleReply",
    "Status",
    "UpdateArticleReply",
]
