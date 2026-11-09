



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .conflict_error_body import ConflictErrorBody
    from .forbidden_error_body import (
        ForbiddenErrorBody,
        ForbiddenErrorBody_HttpsDeveloperNexmoComApiErrorsSubaccountsInvalidNumberTransfer,
        ForbiddenErrorBody_HttpsDeveloperNexmoComApiErrorsUnprovisioned,
    )
    from .invalid_number_transfer_error_response import InvalidNumberTransferErrorResponse
    from .list_balance_transfers_response import ListBalanceTransfersResponse
    from .list_balance_transfers_response_embedded import ListBalanceTransfersResponseEmbedded
    from .list_credit_transfers_response import ListCreditTransfersResponse
    from .list_credit_transfers_response_embedded import ListCreditTransfersResponseEmbedded
    from .not_found_error_body import NotFoundErrorBody
    from .shortcode_not_found import ShortcodeNotFound
    from .subaccount_create_response import SubaccountCreateResponse
    from .subaccount_response import SubaccountResponse
    from .subaccounts_all_response import SubaccountsAllResponse
    from .subaccounts_all_response_embedded import SubaccountsAllResponseEmbedded
    from .transfer_balance_or_credit_request import TransferBalanceOrCreditRequest
    from .transfer_balance_response import TransferBalanceResponse
    from .transfer_credit_response import TransferCreditResponse
    from .transfer_number_response import TransferNumberResponse
    from .unauthorized_error_body import UnauthorizedErrorBody
    from .unprocessable_entity_error_body import UnprocessableEntityErrorBody
    from .unprocessable_entity_error_body_invalid_parameters_item import (
        UnprocessableEntityErrorBodyInvalidParametersItem,
    )
    from .unprovisioned_error_response import UnprovisionedErrorResponse
_dynamic_imports: typing.Dict[str, str] = {
    "ConflictErrorBody": ".conflict_error_body",
    "ForbiddenErrorBody": ".forbidden_error_body",
    "ForbiddenErrorBody_HttpsDeveloperNexmoComApiErrorsSubaccountsInvalidNumberTransfer": ".forbidden_error_body",
    "ForbiddenErrorBody_HttpsDeveloperNexmoComApiErrorsUnprovisioned": ".forbidden_error_body",
    "InvalidNumberTransferErrorResponse": ".invalid_number_transfer_error_response",
    "ListBalanceTransfersResponse": ".list_balance_transfers_response",
    "ListBalanceTransfersResponseEmbedded": ".list_balance_transfers_response_embedded",
    "ListCreditTransfersResponse": ".list_credit_transfers_response",
    "ListCreditTransfersResponseEmbedded": ".list_credit_transfers_response_embedded",
    "NotFoundErrorBody": ".not_found_error_body",
    "ShortcodeNotFound": ".shortcode_not_found",
    "SubaccountCreateResponse": ".subaccount_create_response",
    "SubaccountResponse": ".subaccount_response",
    "SubaccountsAllResponse": ".subaccounts_all_response",
    "SubaccountsAllResponseEmbedded": ".subaccounts_all_response_embedded",
    "TransferBalanceOrCreditRequest": ".transfer_balance_or_credit_request",
    "TransferBalanceResponse": ".transfer_balance_response",
    "TransferCreditResponse": ".transfer_credit_response",
    "TransferNumberResponse": ".transfer_number_response",
    "UnauthorizedErrorBody": ".unauthorized_error_body",
    "UnprocessableEntityErrorBody": ".unprocessable_entity_error_body",
    "UnprocessableEntityErrorBodyInvalidParametersItem": ".unprocessable_entity_error_body_invalid_parameters_item",
    "UnprovisionedErrorResponse": ".unprovisioned_error_response",
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
    "ConflictErrorBody",
    "ForbiddenErrorBody",
    "ForbiddenErrorBody_HttpsDeveloperNexmoComApiErrorsSubaccountsInvalidNumberTransfer",
    "ForbiddenErrorBody_HttpsDeveloperNexmoComApiErrorsUnprovisioned",
    "InvalidNumberTransferErrorResponse",
    "ListBalanceTransfersResponse",
    "ListBalanceTransfersResponseEmbedded",
    "ListCreditTransfersResponse",
    "ListCreditTransfersResponseEmbedded",
    "NotFoundErrorBody",
    "ShortcodeNotFound",
    "SubaccountCreateResponse",
    "SubaccountResponse",
    "SubaccountsAllResponse",
    "SubaccountsAllResponseEmbedded",
    "TransferBalanceOrCreditRequest",
    "TransferBalanceResponse",
    "TransferCreditResponse",
    "TransferNumberResponse",
    "UnauthorizedErrorBody",
    "UnprocessableEntityErrorBody",
    "UnprocessableEntityErrorBodyInvalidParametersItem",
    "UnprovisionedErrorResponse",
]
