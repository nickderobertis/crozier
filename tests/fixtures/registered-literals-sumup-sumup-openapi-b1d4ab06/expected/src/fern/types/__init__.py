



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .address import Address
    from .address_legacy import AddressLegacy
    from .affiliate import Affiliate
    from .amount import Amount
    from .attributes import Attributes
    from .bad_request import BadRequest
    from .bad_request_error_body import BadRequestErrorBody
    from .bad_request_error_body_error_code import BadRequestErrorBodyErrorCode
    from .bad_request_errors import BadRequestErrors
    from .bad_request_errors_type import BadRequestErrorsType
    from .base_person import BasePerson
    from .branding import Branding
    from .business_profile import BusinessProfile
    from .card import Card
    from .card_response import CardResponse
    from .card_type import CardType
    from .change_status import ChangeStatus
    from .checkout import Checkout
    from .checkout_accepted import CheckoutAccepted
    from .checkout_accepted_next_step import CheckoutAcceptedNextStep
    from .checkout_accepted_next_step_mechanism_item import CheckoutAcceptedNextStepMechanismItem
    from .checkout_status import CheckoutStatus
    from .checkout_success import CheckoutSuccess
    from .checkout_success_payment_instrument import CheckoutSuccessPaymentInstrument
    from .checkout_transactions_item import CheckoutTransactionsItem
    from .classic_merchant_identifiers import ClassicMerchantIdentifiers
    from .company import Company
    from .company_identifier import CompanyIdentifier
    from .company_identifiers import CompanyIdentifiers
    from .country_code import CountryCode
    from .create_reader_checkout_error import CreateReaderCheckoutError
    from .create_reader_checkout_error_errors import CreateReaderCheckoutErrorErrors
    from .create_reader_checkout_response import CreateReaderCheckoutResponse
    from .create_reader_checkout_response_data import CreateReaderCheckoutResponseData
    from .create_reader_checkout_unprocessable_entity import CreateReaderCheckoutUnprocessableEntity
    from .create_reader_terminate_error import CreateReaderTerminateError
    from .create_reader_terminate_error_errors import CreateReaderTerminateErrorErrors
    from .create_reader_terminate_unprocessable_entity import CreateReaderTerminateUnprocessableEntity
    from .currency import Currency
    from .customer import Customer
    from .details_error import DetailsError
    from .details_error_failed_constraints_item import DetailsErrorFailedConstraintsItem
    from .device import Device
    from .elv_card_account import ElvCardAccount
    from .entry_mode import EntryMode
    from .error import Error
    from .error_extended import ErrorExtended
    from .error_forbidden import ErrorForbidden
    from .event import Event
    from .financial_payout import FinancialPayout
    from .financial_payout_status import FinancialPayoutStatus
    from .financial_payout_type import FinancialPayoutType
    from .financial_payouts import FinancialPayouts
    from .get_reader_checkout_response import GetReaderCheckoutResponse
    from .get_reader_checkout_response_data import GetReaderCheckoutResponseData
    from .get_reader_checkout_response_data_card_type import GetReaderCheckoutResponseDataCardType
    from .get_reader_checkout_response_data_payment_type import GetReaderCheckoutResponseDataPaymentType
    from .get_reader_checkout_response_data_status import GetReaderCheckoutResponseDataStatus
    from .get_reader_checkout_response_data_total_amount import GetReaderCheckoutResponseDataTotalAmount
    from .horizontal_accuracy import HorizontalAccuracy
    from .hosted_checkout import HostedCheckout
    from .invite import Invite
    from .lat import Lat
    from .legal_type import LegalType
    from .link import Link
    from .list_persons_response_body import ListPersonsResponseBody
    from .lon import Lon
    from .mandate_payload import MandatePayload
    from .mandate_payload_type import MandatePayloadType
    from .mandate_response import MandateResponse
    from .mandate_response_status import MandateResponseStatus
    from .member import Member
    from .membership import Membership
    from .membership_resource import MembershipResource
    from .membership_status import MembershipStatus
    from .membership_user import MembershipUser
    from .membership_user_classic import MembershipUserClassic
    from .merchant import Merchant
    from .meta import Meta
    from .metadata import Metadata
    from .not_found import NotFound
    from .not_found_errors import NotFoundErrors
    from .oauth_scope import OauthScope
    from .ownership import Ownership
    from .payment_instrument_response import PaymentInstrumentResponse
    from .payment_instrument_response_card import PaymentInstrumentResponseCard
    from .payment_instrument_response_type import PaymentInstrumentResponseType
    from .payment_type import PaymentType
    from .person import Person
    from .personal_details import PersonalDetails
    from .personal_identifier import PersonalIdentifier
    from .personal_identifiers import PersonalIdentifiers
    from .phone_number import PhoneNumber
    from .problem import Problem
    from .product import Product
    from .reader import Reader
    from .reader_checkout_status_change import ReaderCheckoutStatusChange
    from .reader_checkout_status_change_payload import ReaderCheckoutStatusChangePayload
    from .reader_checkout_status_change_payload_status import ReaderCheckoutStatusChangePayloadStatus
    from .reader_device import ReaderDevice
    from .reader_device_model import ReaderDeviceModel
    from .reader_id import ReaderId
    from .reader_name import ReaderName
    from .reader_pairing_code import ReaderPairingCode
    from .reader_payment_response import ReaderPaymentResponse
    from .reader_payment_response_data import ReaderPaymentResponseData
    from .reader_status import ReaderStatus
    from .receipt import Receipt
    from .receipt_acquirer_data import ReceiptAcquirerData
    from .receipt_card import ReceiptCard
    from .receipt_event import ReceiptEvent
    from .receipt_merchant_data import ReceiptMerchantData
    from .receipt_merchant_data_merchant_profile import ReceiptMerchantDataMerchantProfile
    from .receipt_merchant_data_merchant_profile_address import ReceiptMerchantDataMerchantProfileAddress
    from .receipt_reader import ReceiptReader
    from .receipt_transaction import ReceiptTransaction
    from .receipt_transaction_process_as import ReceiptTransactionProcessAs
    from .receipt_transaction_products_item import ReceiptTransactionProductsItem
    from .receipt_transaction_vat_rates_item import ReceiptTransactionVatRatesItem
    from .resource_type import ResourceType
    from .role import Role
    from .status_response import StatusResponse
    from .status_response_data import StatusResponseData
    from .status_response_data_connection_type import StatusResponseDataConnectionType
    from .status_response_data_state import StatusResponseDataState
    from .status_response_data_status import StatusResponseDataStatus
    from .timestamps import Timestamps
    from .transaction_base import TransactionBase
    from .transaction_checkout_info import TransactionCheckoutInfo
    from .transaction_event import TransactionEvent
    from .transaction_event_id import TransactionEventId
    from .transaction_event_status import TransactionEventStatus
    from .transaction_event_type import TransactionEventType
    from .transaction_full import TransactionFull
    from .transaction_full_location import TransactionFullLocation
    from .transaction_full_payout_type import TransactionFullPayoutType
    from .transaction_full_process_as import TransactionFullProcessAs
    from .transaction_full_simple_payment_type import TransactionFullSimplePaymentType
    from .transaction_full_simple_status import TransactionFullSimpleStatus
    from .transaction_full_vat_rates_item import TransactionFullVatRatesItem
    from .transaction_full_verification_method import TransactionFullVerificationMethod
    from .transaction_history import TransactionHistory
    from .transaction_history_payout_type import TransactionHistoryPayoutType
    from .transaction_history_type import TransactionHistoryType
    from .transaction_id import TransactionId
    from .transaction_mixin_history import TransactionMixinHistory
    from .transaction_mixin_history_payout_plan import TransactionMixinHistoryPayoutPlan
    from .transaction_status import TransactionStatus
    from .transactions_history_link import TransactionsHistoryLink
    from .unauthorized import Unauthorized
    from .unauthorized_errors import UnauthorizedErrors
    from .unauthorized_errors_type import UnauthorizedErrorsType
    from .user_type import UserType
    from .version import Version
_dynamic_imports: typing.Dict[str, str] = {
    "Address": ".address",
    "AddressLegacy": ".address_legacy",
    "Affiliate": ".affiliate",
    "Amount": ".amount",
    "Attributes": ".attributes",
    "BadRequest": ".bad_request",
    "BadRequestErrorBody": ".bad_request_error_body",
    "BadRequestErrorBodyErrorCode": ".bad_request_error_body_error_code",
    "BadRequestErrors": ".bad_request_errors",
    "BadRequestErrorsType": ".bad_request_errors_type",
    "BasePerson": ".base_person",
    "Branding": ".branding",
    "BusinessProfile": ".business_profile",
    "Card": ".card",
    "CardResponse": ".card_response",
    "CardType": ".card_type",
    "ChangeStatus": ".change_status",
    "Checkout": ".checkout",
    "CheckoutAccepted": ".checkout_accepted",
    "CheckoutAcceptedNextStep": ".checkout_accepted_next_step",
    "CheckoutAcceptedNextStepMechanismItem": ".checkout_accepted_next_step_mechanism_item",
    "CheckoutStatus": ".checkout_status",
    "CheckoutSuccess": ".checkout_success",
    "CheckoutSuccessPaymentInstrument": ".checkout_success_payment_instrument",
    "CheckoutTransactionsItem": ".checkout_transactions_item",
    "ClassicMerchantIdentifiers": ".classic_merchant_identifiers",
    "Company": ".company",
    "CompanyIdentifier": ".company_identifier",
    "CompanyIdentifiers": ".company_identifiers",
    "CountryCode": ".country_code",
    "CreateReaderCheckoutError": ".create_reader_checkout_error",
    "CreateReaderCheckoutErrorErrors": ".create_reader_checkout_error_errors",
    "CreateReaderCheckoutResponse": ".create_reader_checkout_response",
    "CreateReaderCheckoutResponseData": ".create_reader_checkout_response_data",
    "CreateReaderCheckoutUnprocessableEntity": ".create_reader_checkout_unprocessable_entity",
    "CreateReaderTerminateError": ".create_reader_terminate_error",
    "CreateReaderTerminateErrorErrors": ".create_reader_terminate_error_errors",
    "CreateReaderTerminateUnprocessableEntity": ".create_reader_terminate_unprocessable_entity",
    "Currency": ".currency",
    "Customer": ".customer",
    "DetailsError": ".details_error",
    "DetailsErrorFailedConstraintsItem": ".details_error_failed_constraints_item",
    "Device": ".device",
    "ElvCardAccount": ".elv_card_account",
    "EntryMode": ".entry_mode",
    "Error": ".error",
    "ErrorExtended": ".error_extended",
    "ErrorForbidden": ".error_forbidden",
    "Event": ".event",
    "FinancialPayout": ".financial_payout",
    "FinancialPayoutStatus": ".financial_payout_status",
    "FinancialPayoutType": ".financial_payout_type",
    "FinancialPayouts": ".financial_payouts",
    "GetReaderCheckoutResponse": ".get_reader_checkout_response",
    "GetReaderCheckoutResponseData": ".get_reader_checkout_response_data",
    "GetReaderCheckoutResponseDataCardType": ".get_reader_checkout_response_data_card_type",
    "GetReaderCheckoutResponseDataPaymentType": ".get_reader_checkout_response_data_payment_type",
    "GetReaderCheckoutResponseDataStatus": ".get_reader_checkout_response_data_status",
    "GetReaderCheckoutResponseDataTotalAmount": ".get_reader_checkout_response_data_total_amount",
    "HorizontalAccuracy": ".horizontal_accuracy",
    "HostedCheckout": ".hosted_checkout",
    "Invite": ".invite",
    "Lat": ".lat",
    "LegalType": ".legal_type",
    "Link": ".link",
    "ListPersonsResponseBody": ".list_persons_response_body",
    "Lon": ".lon",
    "MandatePayload": ".mandate_payload",
    "MandatePayloadType": ".mandate_payload_type",
    "MandateResponse": ".mandate_response",
    "MandateResponseStatus": ".mandate_response_status",
    "Member": ".member",
    "Membership": ".membership",
    "MembershipResource": ".membership_resource",
    "MembershipStatus": ".membership_status",
    "MembershipUser": ".membership_user",
    "MembershipUserClassic": ".membership_user_classic",
    "Merchant": ".merchant",
    "Meta": ".meta",
    "Metadata": ".metadata",
    "NotFound": ".not_found",
    "NotFoundErrors": ".not_found_errors",
    "OauthScope": ".oauth_scope",
    "Ownership": ".ownership",
    "PaymentInstrumentResponse": ".payment_instrument_response",
    "PaymentInstrumentResponseCard": ".payment_instrument_response_card",
    "PaymentInstrumentResponseType": ".payment_instrument_response_type",
    "PaymentType": ".payment_type",
    "Person": ".person",
    "PersonalDetails": ".personal_details",
    "PersonalIdentifier": ".personal_identifier",
    "PersonalIdentifiers": ".personal_identifiers",
    "PhoneNumber": ".phone_number",
    "Problem": ".problem",
    "Product": ".product",
    "Reader": ".reader",
    "ReaderCheckoutStatusChange": ".reader_checkout_status_change",
    "ReaderCheckoutStatusChangePayload": ".reader_checkout_status_change_payload",
    "ReaderCheckoutStatusChangePayloadStatus": ".reader_checkout_status_change_payload_status",
    "ReaderDevice": ".reader_device",
    "ReaderDeviceModel": ".reader_device_model",
    "ReaderId": ".reader_id",
    "ReaderName": ".reader_name",
    "ReaderPairingCode": ".reader_pairing_code",
    "ReaderPaymentResponse": ".reader_payment_response",
    "ReaderPaymentResponseData": ".reader_payment_response_data",
    "ReaderStatus": ".reader_status",
    "Receipt": ".receipt",
    "ReceiptAcquirerData": ".receipt_acquirer_data",
    "ReceiptCard": ".receipt_card",
    "ReceiptEvent": ".receipt_event",
    "ReceiptMerchantData": ".receipt_merchant_data",
    "ReceiptMerchantDataMerchantProfile": ".receipt_merchant_data_merchant_profile",
    "ReceiptMerchantDataMerchantProfileAddress": ".receipt_merchant_data_merchant_profile_address",
    "ReceiptReader": ".receipt_reader",
    "ReceiptTransaction": ".receipt_transaction",
    "ReceiptTransactionProcessAs": ".receipt_transaction_process_as",
    "ReceiptTransactionProductsItem": ".receipt_transaction_products_item",
    "ReceiptTransactionVatRatesItem": ".receipt_transaction_vat_rates_item",
    "ResourceType": ".resource_type",
    "Role": ".role",
    "StatusResponse": ".status_response",
    "StatusResponseData": ".status_response_data",
    "StatusResponseDataConnectionType": ".status_response_data_connection_type",
    "StatusResponseDataState": ".status_response_data_state",
    "StatusResponseDataStatus": ".status_response_data_status",
    "Timestamps": ".timestamps",
    "TransactionBase": ".transaction_base",
    "TransactionCheckoutInfo": ".transaction_checkout_info",
    "TransactionEvent": ".transaction_event",
    "TransactionEventId": ".transaction_event_id",
    "TransactionEventStatus": ".transaction_event_status",
    "TransactionEventType": ".transaction_event_type",
    "TransactionFull": ".transaction_full",
    "TransactionFullLocation": ".transaction_full_location",
    "TransactionFullPayoutType": ".transaction_full_payout_type",
    "TransactionFullProcessAs": ".transaction_full_process_as",
    "TransactionFullSimplePaymentType": ".transaction_full_simple_payment_type",
    "TransactionFullSimpleStatus": ".transaction_full_simple_status",
    "TransactionFullVatRatesItem": ".transaction_full_vat_rates_item",
    "TransactionFullVerificationMethod": ".transaction_full_verification_method",
    "TransactionHistory": ".transaction_history",
    "TransactionHistoryPayoutType": ".transaction_history_payout_type",
    "TransactionHistoryType": ".transaction_history_type",
    "TransactionId": ".transaction_id",
    "TransactionMixinHistory": ".transaction_mixin_history",
    "TransactionMixinHistoryPayoutPlan": ".transaction_mixin_history_payout_plan",
    "TransactionStatus": ".transaction_status",
    "TransactionsHistoryLink": ".transactions_history_link",
    "Unauthorized": ".unauthorized",
    "UnauthorizedErrors": ".unauthorized_errors",
    "UnauthorizedErrorsType": ".unauthorized_errors_type",
    "UserType": ".user_type",
    "Version": ".version",
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
    "Address",
    "AddressLegacy",
    "Affiliate",
    "Amount",
    "Attributes",
    "BadRequest",
    "BadRequestErrorBody",
    "BadRequestErrorBodyErrorCode",
    "BadRequestErrors",
    "BadRequestErrorsType",
    "BasePerson",
    "Branding",
    "BusinessProfile",
    "Card",
    "CardResponse",
    "CardType",
    "ChangeStatus",
    "Checkout",
    "CheckoutAccepted",
    "CheckoutAcceptedNextStep",
    "CheckoutAcceptedNextStepMechanismItem",
    "CheckoutStatus",
    "CheckoutSuccess",
    "CheckoutSuccessPaymentInstrument",
    "CheckoutTransactionsItem",
    "ClassicMerchantIdentifiers",
    "Company",
    "CompanyIdentifier",
    "CompanyIdentifiers",
    "CountryCode",
    "CreateReaderCheckoutError",
    "CreateReaderCheckoutErrorErrors",
    "CreateReaderCheckoutResponse",
    "CreateReaderCheckoutResponseData",
    "CreateReaderCheckoutUnprocessableEntity",
    "CreateReaderTerminateError",
    "CreateReaderTerminateErrorErrors",
    "CreateReaderTerminateUnprocessableEntity",
    "Currency",
    "Customer",
    "DetailsError",
    "DetailsErrorFailedConstraintsItem",
    "Device",
    "ElvCardAccount",
    "EntryMode",
    "Error",
    "ErrorExtended",
    "ErrorForbidden",
    "Event",
    "FinancialPayout",
    "FinancialPayoutStatus",
    "FinancialPayoutType",
    "FinancialPayouts",
    "GetReaderCheckoutResponse",
    "GetReaderCheckoutResponseData",
    "GetReaderCheckoutResponseDataCardType",
    "GetReaderCheckoutResponseDataPaymentType",
    "GetReaderCheckoutResponseDataStatus",
    "GetReaderCheckoutResponseDataTotalAmount",
    "HorizontalAccuracy",
    "HostedCheckout",
    "Invite",
    "Lat",
    "LegalType",
    "Link",
    "ListPersonsResponseBody",
    "Lon",
    "MandatePayload",
    "MandatePayloadType",
    "MandateResponse",
    "MandateResponseStatus",
    "Member",
    "Membership",
    "MembershipResource",
    "MembershipStatus",
    "MembershipUser",
    "MembershipUserClassic",
    "Merchant",
    "Meta",
    "Metadata",
    "NotFound",
    "NotFoundErrors",
    "OauthScope",
    "Ownership",
    "PaymentInstrumentResponse",
    "PaymentInstrumentResponseCard",
    "PaymentInstrumentResponseType",
    "PaymentType",
    "Person",
    "PersonalDetails",
    "PersonalIdentifier",
    "PersonalIdentifiers",
    "PhoneNumber",
    "Problem",
    "Product",
    "Reader",
    "ReaderCheckoutStatusChange",
    "ReaderCheckoutStatusChangePayload",
    "ReaderCheckoutStatusChangePayloadStatus",
    "ReaderDevice",
    "ReaderDeviceModel",
    "ReaderId",
    "ReaderName",
    "ReaderPairingCode",
    "ReaderPaymentResponse",
    "ReaderPaymentResponseData",
    "ReaderStatus",
    "Receipt",
    "ReceiptAcquirerData",
    "ReceiptCard",
    "ReceiptEvent",
    "ReceiptMerchantData",
    "ReceiptMerchantDataMerchantProfile",
    "ReceiptMerchantDataMerchantProfileAddress",
    "ReceiptReader",
    "ReceiptTransaction",
    "ReceiptTransactionProcessAs",
    "ReceiptTransactionProductsItem",
    "ReceiptTransactionVatRatesItem",
    "ResourceType",
    "Role",
    "StatusResponse",
    "StatusResponseData",
    "StatusResponseDataConnectionType",
    "StatusResponseDataState",
    "StatusResponseDataStatus",
    "Timestamps",
    "TransactionBase",
    "TransactionCheckoutInfo",
    "TransactionEvent",
    "TransactionEventId",
    "TransactionEventStatus",
    "TransactionEventType",
    "TransactionFull",
    "TransactionFullLocation",
    "TransactionFullPayoutType",
    "TransactionFullProcessAs",
    "TransactionFullSimplePaymentType",
    "TransactionFullSimpleStatus",
    "TransactionFullVatRatesItem",
    "TransactionFullVerificationMethod",
    "TransactionHistory",
    "TransactionHistoryPayoutType",
    "TransactionHistoryType",
    "TransactionId",
    "TransactionMixinHistory",
    "TransactionMixinHistoryPayoutPlan",
    "TransactionStatus",
    "TransactionsHistoryLink",
    "Unauthorized",
    "UnauthorizedErrors",
    "UnauthorizedErrorsType",
    "UserType",
    "Version",
]
