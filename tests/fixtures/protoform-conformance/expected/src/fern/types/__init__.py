



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .book_name import BookName
    from .connect_error_v1error import ConnectErrorV1Error
    from .protoform_conformance_v1book import ProtoformConformanceV1Book
    from .protoform_conformance_v1book_state import ProtoformConformanceV1BookState
    from .protoform_conformance_v1list_books_response import ProtoformConformanceV1ListBooksResponse
    from .publisher_name import PublisherName
_dynamic_imports: typing.Dict[str, str] = {
    "BookName": ".book_name",
    "ConnectErrorV1Error": ".connect_error_v1error",
    "ProtoformConformanceV1Book": ".protoform_conformance_v1book",
    "ProtoformConformanceV1BookState": ".protoform_conformance_v1book_state",
    "ProtoformConformanceV1ListBooksResponse": ".protoform_conformance_v1list_books_response",
    "PublisherName": ".publisher_name",
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
    "BookName",
    "ConnectErrorV1Error",
    "ProtoformConformanceV1Book",
    "ProtoformConformanceV1BookState",
    "ProtoformConformanceV1ListBooksResponse",
    "PublisherName",
]
