



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .choice import Choice
    from .choice_code import ChoiceCode
    from .fixed import Fixed
    from .get_record_response import GetRecordResponse
    from .get_record_response_annotated import GetRecordResponseAnnotated
    from .get_record_response_annotated_code import GetRecordResponseAnnotatedCode
    from .get_record_response_closed import GetRecordResponseClosed
    from .get_record_response_fixed import GetRecordResponseFixed
    from .get_record_response_open import GetRecordResponseOpen
_dynamic_imports: typing.Dict[str, str] = {
    "Choice": ".choice",
    "ChoiceCode": ".choice_code",
    "Fixed": ".fixed",
    "GetRecordResponse": ".get_record_response",
    "GetRecordResponseAnnotated": ".get_record_response_annotated",
    "GetRecordResponseAnnotatedCode": ".get_record_response_annotated_code",
    "GetRecordResponseClosed": ".get_record_response_closed",
    "GetRecordResponseFixed": ".get_record_response_fixed",
    "GetRecordResponseOpen": ".get_record_response_open",
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
    "Choice",
    "ChoiceCode",
    "Fixed",
    "GetRecordResponse",
    "GetRecordResponseAnnotated",
    "GetRecordResponseAnnotatedCode",
    "GetRecordResponseClosed",
    "GetRecordResponseFixed",
    "GetRecordResponseOpen",
]
