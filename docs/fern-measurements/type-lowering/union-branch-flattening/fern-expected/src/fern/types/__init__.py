



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .ach_instruction import AchInstruction
    from .bridge_properties import BridgeProperties
    from .bridge_properties_direction import BridgePropertiesDirection
    from .chain_source import ChainSource
    from .common_ramp_properties import CommonRampProperties
    from .fiat_source import FiatSource
    from .iban_instruction import IbanInstruction
    from .instructed_off_ramp_properties import InstructedOffRampProperties
    from .instructed_off_ramp_properties_payment_instructions import InstructedOffRampPropertiesPaymentInstructions
    from .off_ramp_properties import OffRampProperties
    from .off_ramp_properties_direction import OffRampPropertiesDirection
    from .on_ramp_properties import OnRampProperties
    from .on_ramp_properties_direction import OnRampPropertiesDirection
    from .payment_instruction import PaymentInstruction
    from .ramp import Ramp
    from .ramp_direction import RampDirection
    from .ramp_method import RampMethod
    from .ramp_method_direction import RampMethodDirection
    from .ticket import Ticket
    from .ticket_fare import TicketFare
_dynamic_imports: typing.Dict[str, str] = {
    "AchInstruction": ".ach_instruction",
    "BridgeProperties": ".bridge_properties",
    "BridgePropertiesDirection": ".bridge_properties_direction",
    "ChainSource": ".chain_source",
    "CommonRampProperties": ".common_ramp_properties",
    "FiatSource": ".fiat_source",
    "IbanInstruction": ".iban_instruction",
    "InstructedOffRampProperties": ".instructed_off_ramp_properties",
    "InstructedOffRampPropertiesPaymentInstructions": ".instructed_off_ramp_properties_payment_instructions",
    "OffRampProperties": ".off_ramp_properties",
    "OffRampPropertiesDirection": ".off_ramp_properties_direction",
    "OnRampProperties": ".on_ramp_properties",
    "OnRampPropertiesDirection": ".on_ramp_properties_direction",
    "PaymentInstruction": ".payment_instruction",
    "Ramp": ".ramp",
    "RampDirection": ".ramp_direction",
    "RampMethod": ".ramp_method",
    "RampMethodDirection": ".ramp_method_direction",
    "Ticket": ".ticket",
    "TicketFare": ".ticket_fare",
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
    "BridgeProperties",
    "BridgePropertiesDirection",
    "ChainSource",
    "CommonRampProperties",
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
    "Ticket",
    "TicketFare",
]
