



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_billing_account_balance_history_response import GetBillingAccountBalanceHistoryResponse
    from .get_billing_account_balance_history_response_data_item import GetBillingAccountBalanceHistoryResponseDataItem
    from .get_billing_account_response import GetBillingAccountResponse
    from .get_billing_account_response_plan import GetBillingAccountResponsePlan
    from .get_billing_account_response_plan_type import GetBillingAccountResponsePlanType
    from .get_billing_accounts_response import GetBillingAccountsResponse
_dynamic_imports: typing.Dict[str, str] = {
    "GetBillingAccountBalanceHistoryResponse": ".get_billing_account_balance_history_response",
    "GetBillingAccountBalanceHistoryResponseDataItem": ".get_billing_account_balance_history_response_data_item",
    "GetBillingAccountResponse": ".get_billing_account_response",
    "GetBillingAccountResponsePlan": ".get_billing_account_response_plan",
    "GetBillingAccountResponsePlanType": ".get_billing_account_response_plan_type",
    "GetBillingAccountsResponse": ".get_billing_accounts_response",
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
    "GetBillingAccountBalanceHistoryResponse",
    "GetBillingAccountBalanceHistoryResponseDataItem",
    "GetBillingAccountResponse",
    "GetBillingAccountResponsePlan",
    "GetBillingAccountResponsePlanType",
    "GetBillingAccountsResponse",
]
