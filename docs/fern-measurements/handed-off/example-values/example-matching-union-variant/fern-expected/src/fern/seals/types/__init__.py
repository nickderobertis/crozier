



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .verify_logbook_request_entry import VerifyLogbookRequestEntry
    from .verify_logbook_response import VerifyLogbookResponse
    from .verify_seal_request_seal import VerifySealRequestSeal, VerifySealRequestSeal_Stamp, VerifySealRequestSeal_Wax
    from .verify_seal_response import VerifySealResponse
_dynamic_imports: typing.Dict[str, str] = {
    "VerifyLogbookRequestEntry": ".verify_logbook_request_entry",
    "VerifyLogbookResponse": ".verify_logbook_response",
    "VerifySealRequestSeal": ".verify_seal_request_seal",
    "VerifySealRequestSeal_Stamp": ".verify_seal_request_seal",
    "VerifySealRequestSeal_Wax": ".verify_seal_request_seal",
    "VerifySealResponse": ".verify_seal_response",
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
    "VerifyLogbookRequestEntry",
    "VerifyLogbookResponse",
    "VerifySealRequestSeal",
    "VerifySealRequestSeal_Stamp",
    "VerifySealRequestSeal_Wax",
    "VerifySealResponse",
]
