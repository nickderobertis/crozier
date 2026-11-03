



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        InspectCharmRequestToken,
        InspectCharmRequestToken_Charm,
        InspectCharmRequestToken_Wax,
        SealRegistrationSeal,
        SealRegistrationSeal_Stamp,
        SealRegistrationSeal_Wax,
        StockShelfRequestShelfValue,
        StockShelfRequestShelfValue_Stamp,
        StockShelfRequestShelfValue_Wax,
        VerifyBadgeRequestBadge,
        VerifyBadgeRequestBadge_Copper,
        VerifyBadgeRequestBadge_Tin,
        VerifyCharmRequestToken,
        VerifyCharmRequestToken_Charm,
        VerifyCharmRequestToken_Wax,
        VerifyLogbookRequestEntry,
        VerifyLogbookResponse,
        VerifySealRequestSeal,
        VerifySealRequestSeal_Stamp,
        VerifySealRequestSeal_Wax,
        VerifySealResponse,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "InspectCharmRequestToken": ".types",
    "InspectCharmRequestToken_Charm": ".types",
    "InspectCharmRequestToken_Wax": ".types",
    "SealRegistrationSeal": ".types",
    "SealRegistrationSeal_Stamp": ".types",
    "SealRegistrationSeal_Wax": ".types",
    "StockShelfRequestShelfValue": ".types",
    "StockShelfRequestShelfValue_Stamp": ".types",
    "StockShelfRequestShelfValue_Wax": ".types",
    "VerifyBadgeRequestBadge": ".types",
    "VerifyBadgeRequestBadge_Copper": ".types",
    "VerifyBadgeRequestBadge_Tin": ".types",
    "VerifyCharmRequestToken": ".types",
    "VerifyCharmRequestToken_Charm": ".types",
    "VerifyCharmRequestToken_Wax": ".types",
    "VerifyLogbookRequestEntry": ".types",
    "VerifyLogbookResponse": ".types",
    "VerifySealRequestSeal": ".types",
    "VerifySealRequestSeal_Stamp": ".types",
    "VerifySealRequestSeal_Wax": ".types",
    "VerifySealResponse": ".types",
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
    "InspectCharmRequestToken",
    "InspectCharmRequestToken_Charm",
    "InspectCharmRequestToken_Wax",
    "SealRegistrationSeal",
    "SealRegistrationSeal_Stamp",
    "SealRegistrationSeal_Wax",
    "StockShelfRequestShelfValue",
    "StockShelfRequestShelfValue_Stamp",
    "StockShelfRequestShelfValue_Wax",
    "VerifyBadgeRequestBadge",
    "VerifyBadgeRequestBadge_Copper",
    "VerifyBadgeRequestBadge_Tin",
    "VerifyCharmRequestToken",
    "VerifyCharmRequestToken_Charm",
    "VerifyCharmRequestToken_Wax",
    "VerifyLogbookRequestEntry",
    "VerifyLogbookResponse",
    "VerifySealRequestSeal",
    "VerifySealRequestSeal_Stamp",
    "VerifySealRequestSeal_Wax",
    "VerifySealResponse",
]
