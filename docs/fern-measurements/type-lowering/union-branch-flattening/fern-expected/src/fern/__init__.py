



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        AchInstruction,
        BridgeProperties,
        BridgePropertiesDirection,
        ChainSource,
        CommonRampProperties,
        FiatSource,
        IbanInstruction,
        InstructedOffRampProperties,
        InstructedOffRampPropertiesPaymentInstructions,
        OffRampProperties,
        OffRampPropertiesDirection,
        OnRampProperties,
        OnRampPropertiesDirection,
        PaymentInstruction,
        Ramp,
        RampDirection,
        RampMethod,
        RampMethodDirection,
        Ticket,
        TicketFare,
    )
    from . import ramps
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .ramps import RampRequestDirection, RampRequestPaymentInstructions
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AchInstruction": ".types",
    "AsyncFernApi": ".client",
    "BridgeProperties": ".types",
    "BridgePropertiesDirection": ".types",
    "ChainSource": ".types",
    "CommonRampProperties": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "FiatSource": ".types",
    "IbanInstruction": ".types",
    "InstructedOffRampProperties": ".types",
    "InstructedOffRampPropertiesPaymentInstructions": ".types",
    "OffRampProperties": ".types",
    "OffRampPropertiesDirection": ".types",
    "OnRampProperties": ".types",
    "OnRampPropertiesDirection": ".types",
    "PaymentInstruction": ".types",
    "Ramp": ".types",
    "RampDirection": ".types",
    "RampMethod": ".types",
    "RampMethodDirection": ".types",
    "RampRequestDirection": ".ramps",
    "RampRequestPaymentInstructions": ".ramps",
    "Ticket": ".types",
    "TicketFare": ".types",
    "__version__": ".version",
    "ramps": ".ramps",
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
    "AchInstruction",
    "AsyncFernApi",
    "BridgeProperties",
    "BridgePropertiesDirection",
    "ChainSource",
    "CommonRampProperties",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FernApi",
    "FiatSource",
    "IbanInstruction",
    "InstructedOffRampProperties",
    "InstructedOffRampPropertiesPaymentInstructions",
    "OffRampProperties",
    "OffRampPropertiesDirection",
    "OnRampProperties",
    "OnRampPropertiesDirection",
    "PaymentInstruction",
    "Ramp",
    "RampDirection",
    "RampMethod",
    "RampMethodDirection",
    "RampRequestDirection",
    "RampRequestPaymentInstructions",
    "Ticket",
    "TicketFare",
    "__version__",
    "ramps",
]
