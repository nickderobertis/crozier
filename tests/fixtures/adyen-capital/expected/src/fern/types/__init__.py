



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .action import Action
    from .additional_bank_identification import AdditionalBankIdentification
    from .additional_bank_identification_type import AdditionalBankIdentificationType
    from .amount import Amount
    from .au_local_account_identification import AuLocalAccountIdentification
    from .balance import Balance
    from .bank_account_identification import (
        BankAccountIdentification,
        BankAccountIdentification_AuLocal,
        BankAccountIdentification_BrLocal,
        BankAccountIdentification_CaLocal,
        BankAccountIdentification_CzLocal,
        BankAccountIdentification_DkLocal,
        BankAccountIdentification_HkLocal,
        BankAccountIdentification_HuLocal,
        BankAccountIdentification_Iban,
        BankAccountIdentification_NoLocal,
        BankAccountIdentification_NumberAndBic,
        BankAccountIdentification_NzLocal,
        BankAccountIdentification_PlLocal,
        BankAccountIdentification_SeLocal,
        BankAccountIdentification_SgLocal,
        BankAccountIdentification_UkLocal,
        BankAccountIdentification_UsLocal,
    )
    from .br_local_account_identification import BrLocalAccountIdentification
    from .ca_local_account_identification import CaLocalAccountIdentification
    from .ca_local_bank_account_type import CaLocalBankAccountType
    from .calculated_grant_offer import CalculatedGrantOffer
    from .calculated_grant_offer_contract_type import CalculatedGrantOfferContractType
    from .cz_local_account_identification import CzLocalAccountIdentification
    from .default_error_response_entity import DefaultErrorResponseEntity
    from .disbursement import Disbursement
    from .disbursement_repayment import DisbursementRepayment
    from .disbursement_repayment_info_update import DisbursementRepaymentInfoUpdate
    from .disbursements import Disbursements
    from .dk_local_account_identification import DkLocalAccountIdentification
    from .dynamic_offer import DynamicOffer
    from .dynamic_offer_contract_type import DynamicOfferContractType
    from .dynamic_offer_repayment import DynamicOfferRepayment
    from .fee import Fee
    from .financing_type import FinancingType
    from .funds_collection import FundsCollection
    from .funds_collection_type import FundsCollectionType
    from .get_dynamic_offers_response import GetDynamicOffersResponse
    from .grant import Grant
    from .grant_account import GrantAccount
    from .grant_counterparty import GrantCounterparty
    from .grant_info_counterparty import GrantInfoCounterparty
    from .grant_limit import GrantLimit
    from .grant_offer import GrantOffer
    from .grant_offer_contract_type import GrantOfferContractType
    from .grant_offer_fee import GrantOfferFee
    from .grant_offers import GrantOffers
    from .grants import Grants
    from .hk_local_account_identification import HkLocalAccountIdentification
    from .hu_local_account_identification import HuLocalAccountIdentification
    from .iban_account_identification import IbanAccountIdentification
    from .invalid_field import InvalidField
    from .no_local_account_identification import NoLocalAccountIdentification
    from .number_and_bic_account_identification import NumberAndBicAccountIdentification
    from .nz_local_account_identification import NzLocalAccountIdentification
    from .pl_local_account_identification import PlLocalAccountIdentification
    from .repayment import Repayment
    from .repayment_term import RepaymentTerm
    from .se_local_account_identification import SeLocalAccountIdentification
    from .sg_local_account_identification import SgLocalAccountIdentification
    from .status import Status
    from .status_code import StatusCode
    from .threshold_repayment import ThresholdRepayment
    from .uk_local_account_identification import UkLocalAccountIdentification
    from .us_local_account_identification import UsLocalAccountIdentification
    from .us_local_bank_account_type import UsLocalBankAccountType
_dynamic_imports: typing.Dict[str, str] = {
    "Action": ".action",
    "AdditionalBankIdentification": ".additional_bank_identification",
    "AdditionalBankIdentificationType": ".additional_bank_identification_type",
    "Amount": ".amount",
    "AuLocalAccountIdentification": ".au_local_account_identification",
    "Balance": ".balance",
    "BankAccountIdentification": ".bank_account_identification",
    "BankAccountIdentification_AuLocal": ".bank_account_identification",
    "BankAccountIdentification_BrLocal": ".bank_account_identification",
    "BankAccountIdentification_CaLocal": ".bank_account_identification",
    "BankAccountIdentification_CzLocal": ".bank_account_identification",
    "BankAccountIdentification_DkLocal": ".bank_account_identification",
    "BankAccountIdentification_HkLocal": ".bank_account_identification",
    "BankAccountIdentification_HuLocal": ".bank_account_identification",
    "BankAccountIdentification_Iban": ".bank_account_identification",
    "BankAccountIdentification_NoLocal": ".bank_account_identification",
    "BankAccountIdentification_NumberAndBic": ".bank_account_identification",
    "BankAccountIdentification_NzLocal": ".bank_account_identification",
    "BankAccountIdentification_PlLocal": ".bank_account_identification",
    "BankAccountIdentification_SeLocal": ".bank_account_identification",
    "BankAccountIdentification_SgLocal": ".bank_account_identification",
    "BankAccountIdentification_UkLocal": ".bank_account_identification",
    "BankAccountIdentification_UsLocal": ".bank_account_identification",
    "BrLocalAccountIdentification": ".br_local_account_identification",
    "CaLocalAccountIdentification": ".ca_local_account_identification",
    "CaLocalBankAccountType": ".ca_local_bank_account_type",
    "CalculatedGrantOffer": ".calculated_grant_offer",
    "CalculatedGrantOfferContractType": ".calculated_grant_offer_contract_type",
    "CzLocalAccountIdentification": ".cz_local_account_identification",
    "DefaultErrorResponseEntity": ".default_error_response_entity",
    "Disbursement": ".disbursement",
    "DisbursementRepayment": ".disbursement_repayment",
    "DisbursementRepaymentInfoUpdate": ".disbursement_repayment_info_update",
    "Disbursements": ".disbursements",
    "DkLocalAccountIdentification": ".dk_local_account_identification",
    "DynamicOffer": ".dynamic_offer",
    "DynamicOfferContractType": ".dynamic_offer_contract_type",
    "DynamicOfferRepayment": ".dynamic_offer_repayment",
    "Fee": ".fee",
    "FinancingType": ".financing_type",
    "FundsCollection": ".funds_collection",
    "FundsCollectionType": ".funds_collection_type",
    "GetDynamicOffersResponse": ".get_dynamic_offers_response",
    "Grant": ".grant",
    "GrantAccount": ".grant_account",
    "GrantCounterparty": ".grant_counterparty",
    "GrantInfoCounterparty": ".grant_info_counterparty",
    "GrantLimit": ".grant_limit",
    "GrantOffer": ".grant_offer",
    "GrantOfferContractType": ".grant_offer_contract_type",
    "GrantOfferFee": ".grant_offer_fee",
    "GrantOffers": ".grant_offers",
    "Grants": ".grants",
    "HkLocalAccountIdentification": ".hk_local_account_identification",
    "HuLocalAccountIdentification": ".hu_local_account_identification",
    "IbanAccountIdentification": ".iban_account_identification",
    "InvalidField": ".invalid_field",
    "NoLocalAccountIdentification": ".no_local_account_identification",
    "NumberAndBicAccountIdentification": ".number_and_bic_account_identification",
    "NzLocalAccountIdentification": ".nz_local_account_identification",
    "PlLocalAccountIdentification": ".pl_local_account_identification",
    "Repayment": ".repayment",
    "RepaymentTerm": ".repayment_term",
    "SeLocalAccountIdentification": ".se_local_account_identification",
    "SgLocalAccountIdentification": ".sg_local_account_identification",
    "Status": ".status",
    "StatusCode": ".status_code",
    "ThresholdRepayment": ".threshold_repayment",
    "UkLocalAccountIdentification": ".uk_local_account_identification",
    "UsLocalAccountIdentification": ".us_local_account_identification",
    "UsLocalBankAccountType": ".us_local_bank_account_type",
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
    "Action",
    "AdditionalBankIdentification",
    "AdditionalBankIdentificationType",
    "Amount",
    "AuLocalAccountIdentification",
    "Balance",
    "BankAccountIdentification",
    "BankAccountIdentification_AuLocal",
    "BankAccountIdentification_BrLocal",
    "BankAccountIdentification_CaLocal",
    "BankAccountIdentification_CzLocal",
    "BankAccountIdentification_DkLocal",
    "BankAccountIdentification_HkLocal",
    "BankAccountIdentification_HuLocal",
    "BankAccountIdentification_Iban",
    "BankAccountIdentification_NoLocal",
    "BankAccountIdentification_NumberAndBic",
    "BankAccountIdentification_NzLocal",
    "BankAccountIdentification_PlLocal",
    "BankAccountIdentification_SeLocal",
    "BankAccountIdentification_SgLocal",
    "BankAccountIdentification_UkLocal",
    "BankAccountIdentification_UsLocal",
    "BrLocalAccountIdentification",
    "CaLocalAccountIdentification",
    "CaLocalBankAccountType",
    "CalculatedGrantOffer",
    "CalculatedGrantOfferContractType",
    "CzLocalAccountIdentification",
    "DefaultErrorResponseEntity",
    "Disbursement",
    "DisbursementRepayment",
    "DisbursementRepaymentInfoUpdate",
    "Disbursements",
    "DkLocalAccountIdentification",
    "DynamicOffer",
    "DynamicOfferContractType",
    "DynamicOfferRepayment",
    "Fee",
    "FinancingType",
    "FundsCollection",
    "FundsCollectionType",
    "GetDynamicOffersResponse",
    "Grant",
    "GrantAccount",
    "GrantCounterparty",
    "GrantInfoCounterparty",
    "GrantLimit",
    "GrantOffer",
    "GrantOfferContractType",
    "GrantOfferFee",
    "GrantOffers",
    "Grants",
    "HkLocalAccountIdentification",
    "HuLocalAccountIdentification",
    "IbanAccountIdentification",
    "InvalidField",
    "NoLocalAccountIdentification",
    "NumberAndBicAccountIdentification",
    "NzLocalAccountIdentification",
    "PlLocalAccountIdentification",
    "Repayment",
    "RepaymentTerm",
    "SeLocalAccountIdentification",
    "SgLocalAccountIdentification",
    "Status",
    "StatusCode",
    "ThresholdRepayment",
    "UkLocalAccountIdentification",
    "UsLocalAccountIdentification",
    "UsLocalBankAccountType",
]
