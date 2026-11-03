



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        CharmSeal,
        CopperBadge,
        CopperKind,
        EntryV1,
        EntryV2,
        PageV1,
        PageV2,
        PageV2Edition,
        StampSeal,
        TinBadge,
        TinKind,
        WaxSeal,
    )
    from . import seals
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .seals import (
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
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "CharmSeal": ".types",
    "CopperBadge": ".types",
    "CopperKind": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "EntryV1": ".types",
    "EntryV2": ".types",
    "FernApi": ".client",
    "InspectCharmRequestToken": ".seals",
    "InspectCharmRequestToken_Charm": ".seals",
    "InspectCharmRequestToken_Wax": ".seals",
    "PageV1": ".types",
    "PageV2": ".types",
    "PageV2Edition": ".types",
    "SealRegistrationSeal": ".seals",
    "SealRegistrationSeal_Stamp": ".seals",
    "SealRegistrationSeal_Wax": ".seals",
    "StampSeal": ".types",
    "StockShelfRequestShelfValue": ".seals",
    "StockShelfRequestShelfValue_Stamp": ".seals",
    "StockShelfRequestShelfValue_Wax": ".seals",
    "TinBadge": ".types",
    "TinKind": ".types",
    "VerifyBadgeRequestBadge": ".seals",
    "VerifyBadgeRequestBadge_Copper": ".seals",
    "VerifyBadgeRequestBadge_Tin": ".seals",
    "VerifyCharmRequestToken": ".seals",
    "VerifyCharmRequestToken_Charm": ".seals",
    "VerifyCharmRequestToken_Wax": ".seals",
    "VerifyLogbookRequestEntry": ".seals",
    "VerifyLogbookResponse": ".seals",
    "VerifySealRequestSeal": ".seals",
    "VerifySealRequestSeal_Stamp": ".seals",
    "VerifySealRequestSeal_Wax": ".seals",
    "VerifySealResponse": ".seals",
    "WaxSeal": ".types",
    "__version__": ".version",
    "seals": ".seals",
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
    "AsyncFernApi",
    "CharmSeal",
    "CopperBadge",
    "CopperKind",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "EntryV1",
    "EntryV2",
    "FernApi",
    "InspectCharmRequestToken",
    "InspectCharmRequestToken_Charm",
    "InspectCharmRequestToken_Wax",
    "PageV1",
    "PageV2",
    "PageV2Edition",
    "SealRegistrationSeal",
    "SealRegistrationSeal_Stamp",
    "SealRegistrationSeal_Wax",
    "StampSeal",
    "StockShelfRequestShelfValue",
    "StockShelfRequestShelfValue_Stamp",
    "StockShelfRequestShelfValue_Wax",
    "TinBadge",
    "TinKind",
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
    "WaxSeal",
    "__version__",
    "seals",
]
