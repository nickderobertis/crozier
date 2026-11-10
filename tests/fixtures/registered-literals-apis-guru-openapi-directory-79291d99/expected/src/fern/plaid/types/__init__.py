



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .deposit_switch_alt_create_request_country_code import DepositSwitchAltCreateRequestCountryCode
    from .deposit_switch_create_request_country_code import DepositSwitchCreateRequestCountryCode
    from .processor_token_create_request_processor import ProcessorTokenCreateRequestProcessor
    from .sandbox_income_fire_webhook_request_verification_status import (
        SandboxIncomeFireWebhookRequestVerificationStatus,
    )
    from .sandbox_item_fire_webhook_request_webhook_code import SandboxItemFireWebhookRequestWebhookCode
    from .sandbox_item_set_verification_status_request_verification_status import (
        SandboxItemSetVerificationStatusRequestVerificationStatus,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "DepositSwitchAltCreateRequestCountryCode": ".deposit_switch_alt_create_request_country_code",
    "DepositSwitchCreateRequestCountryCode": ".deposit_switch_create_request_country_code",
    "ProcessorTokenCreateRequestProcessor": ".processor_token_create_request_processor",
    "SandboxIncomeFireWebhookRequestVerificationStatus": ".sandbox_income_fire_webhook_request_verification_status",
    "SandboxItemFireWebhookRequestWebhookCode": ".sandbox_item_fire_webhook_request_webhook_code",
    "SandboxItemSetVerificationStatusRequestVerificationStatus": ".sandbox_item_set_verification_status_request_verification_status",
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
    "DepositSwitchAltCreateRequestCountryCode",
    "DepositSwitchCreateRequestCountryCode",
    "ProcessorTokenCreateRequestProcessor",
    "SandboxIncomeFireWebhookRequestVerificationStatus",
    "SandboxItemFireWebhookRequestWebhookCode",
    "SandboxItemSetVerificationStatusRequestVerificationStatus",
]
