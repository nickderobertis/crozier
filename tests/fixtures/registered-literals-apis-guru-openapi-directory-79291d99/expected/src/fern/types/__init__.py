



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .access_token import AccessToken
    from .access_token_nullable import AccessTokenNullable
    from .account_access import AccountAccess
    from .account_assets import AccountAssets
    from .account_balance import AccountBalance
    from .account_base import AccountBase
    from .account_base_verification_status import AccountBaseVerificationStatus
    from .account_filter import AccountFilter
    from .account_filter_subtypes import AccountFilterSubtypes
    from .account_filters_response import AccountFiltersResponse
    from .account_identity import AccountIdentity
    from .account_identity_match_score import AccountIdentityMatchScore
    from .account_ids_with_updated_identity import AccountIdsWithUpdatedIdentity
    from .account_product_access import AccountProductAccess
    from .account_product_access_nullable import AccountProductAccessNullable
    from .account_selection_cardinality import AccountSelectionCardinality
    from .account_subtype import AccountSubtype
    from .account_subtypes import AccountSubtypes
    from .account_type import AccountType
    from .accounts_balance_get_request_options import AccountsBalanceGetRequestOptions
    from .accounts_get_request_options import AccountsGetRequestOptions
    from .accounts_get_response import AccountsGetResponse
    from .ach_class import AchClass
    from .action_state import ActionState
    from .activity import Activity
    from .activity_type import ActivityType
    from .address import Address
    from .address_data import AddressData
    from .address_data_nullable import AddressDataNullable
    from .address_match_score import AddressMatchScore
    from .address_nullable import AddressNullable
    from .address_purpose_label import AddressPurposeLabel
    from .api_client_id import ApiClientId
    from .api_secret import ApiSecret
    from .application import Application
    from .application_get_response import ApplicationGetResponse
    from .application_id import ApplicationId
    from .apr import Apr
    from .apr_apr_type import AprAprType
    from .asset import Asset
    from .asset_detail import AssetDetail
    from .asset_holder import AssetHolder
    from .asset_holder_name import AssetHolderName
    from .asset_owner import AssetOwner
    from .asset_owners import AssetOwners
    from .asset_report import AssetReport
    from .asset_report_add_ons import AssetReportAddOns
    from .asset_report_audit_copy_create_response import AssetReportAuditCopyCreateResponse
    from .asset_report_audit_copy_remove_response import AssetReportAuditCopyRemoveResponse
    from .asset_report_create_request_options import AssetReportCreateRequestOptions
    from .asset_report_create_response import AssetReportCreateResponse
    from .asset_report_filter_response import AssetReportFilterResponse
    from .asset_report_freddie import AssetReportFreddie
    from .asset_report_freddie_get_response import AssetReportFreddieGetResponse
    from .asset_report_get_request_options import AssetReportGetRequestOptions
    from .asset_report_get_response import AssetReportGetResponse
    from .asset_report_id import AssetReportId
    from .asset_report_item import AssetReportItem
    from .asset_report_pdf_get_request_options import AssetReportPdfGetRequestOptions
    from .asset_report_pdf_get_response import AssetReportPdfGetResponse
    from .asset_report_refresh_asset_report_token import AssetReportRefreshAssetReportToken
    from .asset_report_refresh_request_options import AssetReportRefreshRequestOptions
    from .asset_report_refresh_response import AssetReportRefreshResponse
    from .asset_report_remove_response import AssetReportRemoveResponse
    from .asset_report_token import AssetReportToken
    from .asset_report_transaction import AssetReportTransaction
    from .asset_report_user import AssetReportUser
    from .asset_transaction import AssetTransaction
    from .asset_transaction_category_type import AssetTransactionCategoryType
    from .asset_transaction_description import AssetTransactionDescription
    from .asset_transaction_detail import AssetTransactionDetail
    from .asset_transaction_type import AssetTransactionType
    from .asset_transactions import AssetTransactions
    from .asset_type import AssetType
    from .assets import Assets
    from .assets_error_webhook import AssetsErrorWebhook
    from .assets_product_ready_webhook import AssetsProductReadyWebhook
    from .auth_get_numbers import AuthGetNumbers
    from .auth_get_request_options import AuthGetRequestOptions
    from .auth_get_response import AuthGetResponse
    from .auth_metadata import AuthMetadata
    from .auth_supported_methods import AuthSupportedMethods
    from .automatically_verified_webhook import AutomaticallyVerifiedWebhook
    from .bank_initiated_return_risk import BankInitiatedReturnRisk
    from .bank_initiated_risk_tier import BankInitiatedRiskTier
    from .bank_transfer import BankTransfer
    from .bank_transfer_access_token import BankTransferAccessToken
    from .bank_transfer_amount import BankTransferAmount
    from .bank_transfer_balance import BankTransferBalance
    from .bank_transfer_balance_get_response import BankTransferBalanceGetResponse
    from .bank_transfer_cancel_response import BankTransferCancelResponse
    from .bank_transfer_create_response import BankTransferCreateResponse
    from .bank_transfer_direction import BankTransferDirection
    from .bank_transfer_event import BankTransferEvent
    from .bank_transfer_event_list_bank_transfer_type import BankTransferEventListBankTransferType
    from .bank_transfer_event_list_direction import BankTransferEventListDirection
    from .bank_transfer_event_list_response import BankTransferEventListResponse
    from .bank_transfer_event_sync_response import BankTransferEventSyncResponse
    from .bank_transfer_event_type import BankTransferEventType
    from .bank_transfer_failure import BankTransferFailure
    from .bank_transfer_get_response import BankTransferGetResponse
    from .bank_transfer_id import BankTransferId
    from .bank_transfer_idempotency_key import BankTransferIdempotencyKey
    from .bank_transfer_list_response import BankTransferListResponse
    from .bank_transfer_metadata import BankTransferMetadata
    from .bank_transfer_migrate_account_response import BankTransferMigrateAccountResponse
    from .bank_transfer_network import BankTransferNetwork
    from .bank_transfer_status import BankTransferStatus
    from .bank_transfer_sweep import BankTransferSweep
    from .bank_transfer_sweep_get_response import BankTransferSweepGetResponse
    from .bank_transfer_sweep_list_response import BankTransferSweepListResponse
    from .bank_transfer_type import BankTransferType
    from .bank_transfer_user import BankTransferUser
    from .bank_transfers_events_update_webhook import BankTransfersEventsUpdateWebhook
    from .bank_transfers_events_update_webhook_for_auth import BankTransfersEventsUpdateWebhookForAuth
    from .categories_get_request import CategoriesGetRequest
    from .categories_get_response import CategoriesGetResponse
    from .category import Category
    from .cause import Cause
    from .city import City
    from .city_nullable import CityNullable
    from .client_provided_enhanced_transaction import ClientProvidedEnhancedTransaction
    from .client_provided_enriched_transaction import ClientProvidedEnrichedTransaction
    from .client_provided_raw_transaction import ClientProvidedRawTransaction
    from .client_provided_transaction import ClientProvidedTransaction
    from .client_provided_transaction_location import ClientProvidedTransactionLocation
    from .client_user_id import ClientUserId
    from .client_user_id_nullable import ClientUserIdNullable
    from .connected_application import ConnectedApplication
    from .consent_payment_idempotency_key import ConsentPaymentIdempotencyKey
    from .counterparty import Counterparty
    from .counterparty_type import CounterpartyType
    from .country_code import CountryCode
    from .credit1099 import Credit1099
    from .credit1099filer import Credit1099Filer
    from .credit1099payer import Credit1099Payer
    from .credit1099recipient import Credit1099Recipient
    from .credit_account import CreditAccount
    from .credit_account_subtype import CreditAccountSubtype
    from .credit_account_subtypes import CreditAccountSubtypes
    from .credit_amount_with_currency import CreditAmountWithCurrency
    from .credit_audit_copy_token_create_response import CreditAuditCopyTokenCreateResponse
    from .credit_audit_copy_token_remove_response import CreditAuditCopyTokenRemoveResponse
    from .credit_audit_copy_token_update_response import CreditAuditCopyTokenUpdateResponse
    from .credit_bank_employer import CreditBankEmployer
    from .credit_bank_employment import CreditBankEmployment
    from .credit_bank_employment_get_response import CreditBankEmploymentGetResponse
    from .credit_bank_employment_item import CreditBankEmploymentItem
    from .credit_bank_employment_report import CreditBankEmploymentReport
    from .credit_bank_employment_warning import CreditBankEmploymentWarning
    from .credit_bank_employment_warning_type import CreditBankEmploymentWarningType
    from .credit_bank_income import CreditBankIncome
    from .credit_bank_income_account import CreditBankIncomeAccount
    from .credit_bank_income_account_type import CreditBankIncomeAccountType
    from .credit_bank_income_category import CreditBankIncomeCategory
    from .credit_bank_income_cause import CreditBankIncomeCause
    from .credit_bank_income_error_type import CreditBankIncomeErrorType
    from .credit_bank_income_get_request_options import CreditBankIncomeGetRequestOptions
    from .credit_bank_income_get_response import CreditBankIncomeGetResponse
    from .credit_bank_income_historical_summary import CreditBankIncomeHistoricalSummary
    from .credit_bank_income_item import CreditBankIncomeItem
    from .credit_bank_income_pay_frequency import CreditBankIncomePayFrequency
    from .credit_bank_income_pdf_get_response import CreditBankIncomePdfGetResponse
    from .credit_bank_income_refresh_request_options import CreditBankIncomeRefreshRequestOptions
    from .credit_bank_income_refresh_response import CreditBankIncomeRefreshResponse
    from .credit_bank_income_source import CreditBankIncomeSource
    from .credit_bank_income_summary import CreditBankIncomeSummary
    from .credit_bank_income_transaction import CreditBankIncomeTransaction
    from .credit_bank_income_warning import CreditBankIncomeWarning
    from .credit_bank_income_warning_code import CreditBankIncomeWarningCode
    from .credit_bank_income_warning_type import CreditBankIncomeWarningType
    from .credit_card_liability import CreditCardLiability
    from .credit_category import CreditCategory
    from .credit_document_metadata import CreditDocumentMetadata
    from .credit_document_type import CreditDocumentType
    from .credit_employer_verification import CreditEmployerVerification
    from .credit_employment_employee_type import CreditEmploymentEmployeeType
    from .credit_employment_get_response import CreditEmploymentGetResponse
    from .credit_employment_item import CreditEmploymentItem
    from .credit_employment_verification import CreditEmploymentVerification
    from .credit_employment_verification_status import CreditEmploymentVerificationStatus
    from .credit_filter import CreditFilter
    from .credit_freddie_mac_asset_detail_voe25 import CreditFreddieMacAssetDetailVoe25
    from .credit_freddie_mac_asset_transaction_detail_voe25 import CreditFreddieMacAssetTransactionDetailVoe25
    from .credit_freddie_mac_asset_transaction_voa24 import CreditFreddieMacAssetTransactionVoa24
    from .credit_freddie_mac_asset_transaction_voe25 import CreditFreddieMacAssetTransactionVoe25
    from .credit_freddie_mac_asset_transactions_voa24 import CreditFreddieMacAssetTransactionsVoa24
    from .credit_freddie_mac_asset_transactions_voe25 import CreditFreddieMacAssetTransactionsVoe25
    from .credit_freddie_mac_asset_voa24 import CreditFreddieMacAssetVoa24
    from .credit_freddie_mac_asset_voe25 import CreditFreddieMacAssetVoe25
    from .credit_freddie_mac_assets_voa24 import CreditFreddieMacAssetsVoa24
    from .credit_freddie_mac_assets_voe25 import CreditFreddieMacAssetsVoe25
    from .credit_freddie_mac_individual_name_voa24 import CreditFreddieMacIndividualNameVoa24
    from .credit_freddie_mac_loan_identifiers_voa24 import CreditFreddieMacLoanIdentifiersVoa24
    from .credit_freddie_mac_loan_voa24 import CreditFreddieMacLoanVoa24
    from .credit_freddie_mac_loans_voa24 import CreditFreddieMacLoansVoa24
    from .credit_freddie_mac_parties_voa24 import CreditFreddieMacPartiesVoa24
    from .credit_freddie_mac_party_individual_voa24 import CreditFreddieMacPartyIndividualVoa24
    from .credit_freddie_mac_party_voa24 import CreditFreddieMacPartyVoa24
    from .credit_freddie_mac_reporting_information_voa24 import CreditFreddieMacReportingInformationVoa24
    from .credit_freddie_mac_reports_get_response import CreditFreddieMacReportsGetResponse
    from .credit_freddie_mac_service_voa24 import CreditFreddieMacServiceVoa24
    from .credit_freddie_mac_service_voe25 import CreditFreddieMacServiceVoe25
    from .credit_freddie_mac_services_voa24 import CreditFreddieMacServicesVoa24
    from .credit_freddie_mac_services_voe25 import CreditFreddieMacServicesVoe25
    from .credit_freddie_mac_verification_of_asset_response_voa24 import (
        CreditFreddieMacVerificationOfAssetResponseVoa24,
    )
    from .credit_freddie_mac_verification_of_asset_response_voe25 import (
        CreditFreddieMacVerificationOfAssetResponseVoe25,
    )
    from .credit_freddie_mac_verification_of_asset_voa24 import CreditFreddieMacVerificationOfAssetVoa24
    from .credit_freddie_mac_verification_of_asset_voe25 import CreditFreddieMacVerificationOfAssetVoe25
    from .credit_freddie_mac_verification_of_assets_deal_voa24 import CreditFreddieMacVerificationOfAssetsDealVoa24
    from .credit_freddie_mac_verification_of_assets_voa24 import CreditFreddieMacVerificationOfAssetsVoa24
    from .credit_freddie_verification_of_employment_deal_voe25 import CreditFreddieVerificationOfEmploymentDealVoe25
    from .credit_freddie_verification_of_employment_voe25 import CreditFreddieVerificationOfEmploymentVoe25
    from .credit_iso_currency_code import CreditIsoCurrencyCode
    from .credit_pay_stub import CreditPayStub
    from .credit_pay_stub_address import CreditPayStubAddress
    from .credit_pay_stub_deductions import CreditPayStubDeductions
    from .credit_pay_stub_earnings import CreditPayStubEarnings
    from .credit_pay_stub_employee import CreditPayStubEmployee
    from .credit_pay_stub_employer import CreditPayStubEmployer
    from .credit_pay_stub_net_pay import CreditPayStubNetPay
    from .credit_pay_stub_pay_basis_type import CreditPayStubPayBasisType
    from .credit_payroll_income_get_response import CreditPayrollIncomeGetResponse
    from .credit_payroll_income_precheck_response import CreditPayrollIncomePrecheckResponse
    from .credit_payroll_income_refresh_request_options import CreditPayrollIncomeRefreshRequestOptions
    from .credit_payroll_income_refresh_response import CreditPayrollIncomeRefreshResponse
    from .credit_payroll_income_refresh_status import CreditPayrollIncomeRefreshStatus
    from .credit_payroll_income_risk_signals_get_request import CreditPayrollIncomeRiskSignalsGetRequest
    from .credit_payroll_income_risk_signals_get_response import CreditPayrollIncomeRiskSignalsGetResponse
    from .credit_platform_ids import CreditPlatformIds
    from .credit_relay_create_response import CreditRelayCreateResponse
    from .credit_relay_refresh_response import CreditRelayRefreshResponse
    from .credit_relay_remove_response import CreditRelayRemoveResponse
    from .credit_session import CreditSession
    from .credit_session_bank_employment_result import CreditSessionBankEmploymentResult
    from .credit_session_bank_employment_status import CreditSessionBankEmploymentStatus
    from .credit_session_bank_income_result import CreditSessionBankIncomeResult
    from .credit_session_bank_income_status import CreditSessionBankIncomeStatus
    from .credit_session_document_income_result import CreditSessionDocumentIncomeResult
    from .credit_session_error import CreditSessionError
    from .credit_session_item_add_result import CreditSessionItemAddResult
    from .credit_session_payroll_income_result import CreditSessionPayrollIncomeResult
    from .credit_session_results import CreditSessionResults
    from .credit_sessions_get_response import CreditSessionsGetResponse
    from .credit_unofficial_currency_code import CreditUnofficialCurrencyCode
    from .credit_w2 import CreditW2
    from .cursor import Cursor
    from .customer_initiated_return_risk import CustomerInitiatedReturnRisk
    from .customer_initiated_risk_tier import CustomerInitiatedRiskTier
    from .dashboard_user import DashboardUser
    from .dashboard_user_get_response import DashboardUserGetResponse
    from .dashboard_user_id import DashboardUserId
    from .dashboard_user_id_nullable import DashboardUserIdNullable
    from .dashboard_user_list_response import DashboardUserListResponse
    from .dashboard_user_status import DashboardUserStatus
    from .date_range import DateRange
    from .deductions import Deductions
    from .deductions_breakdown import DeductionsBreakdown
    from .deductions_total import DeductionsTotal
    from .default_update_webhook import DefaultUpdateWebhook
    from .deposit_switch_address_data import DepositSwitchAddressData
    from .deposit_switch_alt_create_response import DepositSwitchAltCreateResponse
    from .deposit_switch_create_request_options import DepositSwitchCreateRequestOptions
    from .deposit_switch_create_response import DepositSwitchCreateResponse
    from .deposit_switch_get_response import DepositSwitchGetResponse
    from .deposit_switch_get_response_state import DepositSwitchGetResponseState
    from .deposit_switch_get_response_switch_method import DepositSwitchGetResponseSwitchMethod
    from .deposit_switch_state_update_webhook import DepositSwitchStateUpdateWebhook
    from .deposit_switch_target_account import DepositSwitchTargetAccount
    from .deposit_switch_target_account_account_subtype import DepositSwitchTargetAccountAccountSubtype
    from .deposit_switch_target_user import DepositSwitchTargetUser
    from .deposit_switch_token_create_response import DepositSwitchTokenCreateResponse
    from .depository_account import DepositoryAccount
    from .depository_account_subtype import DepositoryAccountSubtype
    from .depository_account_subtypes import DepositoryAccountSubtypes
    from .depository_filter import DepositoryFilter
    from .detailed_originator import DetailedOriginator
    from .distribution_breakdown import DistributionBreakdown
    from .doc_type import DocType
    from .document_analysis import DocumentAnalysis
    from .document_authenticity_match_code import DocumentAuthenticityMatchCode
    from .document_date_of_birth_match_code import DocumentDateOfBirthMatchCode
    from .document_image_back import DocumentImageBack
    from .document_image_cropped_back import DocumentImageCroppedBack
    from .document_image_cropped_front import DocumentImageCroppedFront
    from .document_image_face import DocumentImageFace
    from .document_image_front import DocumentImageFront
    from .document_metadata import DocumentMetadata
    from .document_name_match_code import DocumentNameMatchCode
    from .document_risk_signal import DocumentRiskSignal
    from .document_risk_signal_institution_metadata import DocumentRiskSignalInstitutionMetadata
    from .document_risk_signals_object import DocumentRiskSignalsObject
    from .document_risk_summary import DocumentRiskSummary
    from .document_status import DocumentStatus
    from .documentary_verification import DocumentaryVerification
    from .documentary_verification_document import DocumentaryVerificationDocument
    from .earnings import Earnings
    from .earnings_breakdown import EarningsBreakdown
    from .earnings_breakdown_canonical_description import EarningsBreakdownCanonicalDescription
    from .earnings_total import EarningsTotal
    from .email import Email
    from .email_address import EmailAddress
    from .email_address_match_score import EmailAddressMatchScore
    from .email_address_nullable import EmailAddressNullable
    from .email_type import EmailType
    from .employee import Employee
    from .employee_income_summary_field_string import EmployeeIncomeSummaryFieldString
    from .employer import Employer
    from .employer_income_summary_field_string import EmployerIncomeSummaryFieldString
    from .employer_verification import EmployerVerification
    from .employers_search_response import EmployersSearchResponse
    from .employment_details import EmploymentDetails
    from .employment_source_type import EmploymentSourceType
    from .employment_verification import EmploymentVerification
    from .employment_verification_get_response import EmploymentVerificationGetResponse
    from .employment_verification_status import EmploymentVerificationStatus
    from .enhancements import Enhancements
    from .enrich_transaction_direction import EnrichTransactionDirection
    from .enrichments import Enrichments
    from .entity_document import EntityDocument
    from .entity_document_type import EntityDocumentType
    from .entity_screening_hit_analysis import EntityScreeningHitAnalysis
    from .entity_screening_hit_data import EntityScreeningHitData
    from .entity_screening_hit_documents_items import EntityScreeningHitDocumentsItems
    from .entity_screening_hit_emails import EntityScreeningHitEmails
    from .entity_screening_hit_emails_items import EntityScreeningHitEmailsItems
    from .entity_screening_hit_names import EntityScreeningHitNames
    from .entity_screening_hit_names_items import EntityScreeningHitNamesItems
    from .entity_screening_hit_phone_numbers import EntityScreeningHitPhoneNumbers
    from .entity_screening_hit_urls import EntityScreeningHitUrls
    from .entity_screening_hit_urls_items import EntityScreeningHitUrlsItems
    from .entity_screening_hits_phone_number_items import EntityScreeningHitsPhoneNumberItems
    from .entity_screening_status_updated_webhook import EntityScreeningStatusUpdatedWebhook
    from .entity_watchlist_code import EntityWatchlistCode
    from .entity_watchlist_program import EntityWatchlistProgram
    from .entity_watchlist_program_id import EntityWatchlistProgramId
    from .entity_watchlist_screening import EntityWatchlistScreening
    from .entity_watchlist_screening_hit import EntityWatchlistScreeningHit
    from .entity_watchlist_screening_hit_id import EntityWatchlistScreeningHitId
    from .entity_watchlist_screening_id import EntityWatchlistScreeningId
    from .entity_watchlist_screening_name import EntityWatchlistScreeningName
    from .entity_watchlist_screening_program_name import EntityWatchlistScreeningProgramName
    from .entity_watchlist_screening_review import EntityWatchlistScreeningReview
    from .entity_watchlist_screening_review_id import EntityWatchlistScreeningReviewId
    from .entity_watchlist_screening_search_terms import EntityWatchlistScreeningSearchTerms
    from .entity_watchlist_search_terms import EntityWatchlistSearchTerms
    from .expiration_date import ExpirationDate
    from .external_payment_initiation_consent_options import ExternalPaymentInitiationConsentOptions
    from .external_payment_options import ExternalPaymentOptions
    from .external_payment_refund_details import ExternalPaymentRefundDetails
    from .external_payment_schedule_base import ExternalPaymentScheduleBase
    from .external_payment_schedule_get import ExternalPaymentScheduleGet
    from .external_payment_schedule_request import ExternalPaymentScheduleRequest
    from .fallback_auth_microdeposit_auto_verified_webhook import FallbackAuthMicrodepositAutoVerifiedWebhook
    from .fallback_auth_microdeposit_verification_expired_webhook import (
        FallbackAuthMicrodepositVerificationExpiredWebhook,
    )
    from .family_name_field import FamilyNameField
    from .fdx_content_types import FdxContentTypes
    from .fdx_fi_attribute import FdxFiAttribute
    from .fdx_hateoas_link import FdxHateoasLink
    from .fdx_hateoas_link_action import FdxHateoasLinkAction
    from .fdx_notification_category import FdxNotificationCategory
    from .fdx_notification_payload import FdxNotificationPayload
    from .fdx_notification_payload_id_type import FdxNotificationPayloadIdType
    from .fdx_notification_priority import FdxNotificationPriority
    from .fdx_notification_severity import FdxNotificationSeverity
    from .fdx_notification_type import FdxNotificationType
    from .fdx_party import FdxParty
    from .fdx_party_registry import FdxPartyRegistry
    from .fdx_party_type import FdxPartyType
    from .fdx_timestamp import FdxTimestamp
    from .form1099type import Form1099Type
    from .generic_country_code import GenericCountryCode
    from .generic_country_code_nullable import GenericCountryCodeNullable
    from .generic_screening_hit_location_items import GenericScreeningHitLocationItems
    from .given_name_field import GivenNameField
    from .health_incident import HealthIncident
    from .historical_balance import HistoricalBalance
    from .historical_update_webhook import HistoricalUpdateWebhook
    from .holding import Holding
    from .holdings_default_update_webhook import HoldingsDefaultUpdateWebhook
    from .holdings_override import HoldingsOverride
    from .id_number_type import IdNumberType
    from .id_number_value import IdNumberValue
    from .idempotency_flag import IdempotencyFlag
    from .identity_default_update_webhook import IdentityDefaultUpdateWebhook
    from .identity_get_request_options import IdentityGetRequestOptions
    from .identity_get_response import IdentityGetResponse
    from .identity_match_identity_verification_id import IdentityMatchIdentityVerificationId
    from .identity_match_request_options import IdentityMatchRequestOptions
    from .identity_match_response import IdentityMatchResponse
    from .identity_match_user import IdentityMatchUser
    from .identity_update_types import IdentityUpdateTypes
    from .identity_verification import IdentityVerification
    from .identity_verification_consent import IdentityVerificationConsent
    from .identity_verification_create_response import IdentityVerificationCreateResponse
    from .identity_verification_get_response import IdentityVerificationGetResponse
    from .identity_verification_id import IdentityVerificationId
    from .identity_verification_list_response import IdentityVerificationListResponse
    from .identity_verification_request_user import IdentityVerificationRequestUser
    from .identity_verification_request_user_name import IdentityVerificationRequestUserName
    from .identity_verification_response_user_name import IdentityVerificationResponseUserName
    from .identity_verification_retried_webhook import IdentityVerificationRetriedWebhook
    from .identity_verification_retry_request_steps_object import IdentityVerificationRetryRequestStepsObject
    from .identity_verification_retry_response import IdentityVerificationRetryResponse
    from .identity_verification_status import IdentityVerificationStatus
    from .identity_verification_status_updated_webhook import IdentityVerificationStatusUpdatedWebhook
    from .identity_verification_step_status import IdentityVerificationStepStatus
    from .identity_verification_step_summary import IdentityVerificationStepSummary
    from .identity_verification_step_updated_webhook import IdentityVerificationStepUpdatedWebhook
    from .identity_verification_template_id import IdentityVerificationTemplateId
    from .identity_verification_template_reference import IdentityVerificationTemplateReference
    from .identity_verification_template_version import IdentityVerificationTemplateVersion
    from .identity_verification_user_address import IdentityVerificationUserAddress
    from .identity_verification_user_data import IdentityVerificationUserData
    from .identity_verification_user_phone_number import IdentityVerificationUserPhoneNumber
    from .image_quality import ImageQuality
    from .incident_update import IncidentUpdate
    from .incident_update_status import IncidentUpdateStatus
    from .income_breakdown import IncomeBreakdown
    from .income_breakdown_type import IncomeBreakdownType
    from .income_override import IncomeOverride
    from .income_summary import IncomeSummary
    from .income_summary_field_number import IncomeSummaryFieldNumber
    from .income_summary_field_string import IncomeSummaryFieldString
    from .income_verification_create_request_options import IncomeVerificationCreateRequestOptions
    from .income_verification_create_response import IncomeVerificationCreateResponse
    from .income_verification_payroll_flow_type import IncomeVerificationPayrollFlowType
    from .income_verification_paystubs_get_response import IncomeVerificationPaystubsGetResponse
    from .income_verification_precheck_confidence import IncomeVerificationPrecheckConfidence
    from .income_verification_precheck_employer import IncomeVerificationPrecheckEmployer
    from .income_verification_precheck_employer_address import IncomeVerificationPrecheckEmployerAddress
    from .income_verification_precheck_employer_address_data import IncomeVerificationPrecheckEmployerAddressData
    from .income_verification_precheck_military_info import IncomeVerificationPrecheckMilitaryInfo
    from .income_verification_precheck_payroll_institution import IncomeVerificationPrecheckPayrollInstitution
    from .income_verification_precheck_response import IncomeVerificationPrecheckResponse
    from .income_verification_precheck_user import IncomeVerificationPrecheckUser
    from .income_verification_source_type import IncomeVerificationSourceType
    from .income_verification_status_webhook import IncomeVerificationStatusWebhook
    from .income_verification_taxforms_get_response import IncomeVerificationTaxformsGetResponse
    from .income_verification_webhook_status import IncomeVerificationWebhookStatus
    from .individual_name import IndividualName
    from .individual_screening_hit_names import IndividualScreeningHitNames
    from .individual_watchlist_code import IndividualWatchlistCode
    from .individual_watchlist_program import IndividualWatchlistProgram
    from .individual_watchlist_screening_program_name import IndividualWatchlistScreeningProgramName
    from .inflow_model import InflowModel
    from .initial_update_webhook import InitialUpdateWebhook
    from .institution import Institution
    from .institution_status import InstitutionStatus
    from .institution_supported_networks import InstitutionSupportedNetworks
    from .institutions_get_by_id_request_options import InstitutionsGetByIdRequestOptions
    from .institutions_get_by_id_response import InstitutionsGetByIdResponse
    from .institutions_get_request_options import InstitutionsGetRequestOptions
    from .institutions_get_response import InstitutionsGetResponse
    from .institutions_search_account_filter import InstitutionsSearchAccountFilter
    from .institutions_search_payment_initiation_options import InstitutionsSearchPaymentInitiationOptions
    from .institutions_search_request_options import InstitutionsSearchRequestOptions
    from .institutions_search_response import InstitutionsSearchResponse
    from .internal_uid import InternalUid
    from .investment_account_subtype import InvestmentAccountSubtype
    from .investment_account_subtype_standalone import InvestmentAccountSubtypeStandalone
    from .investment_account_subtypes import InvestmentAccountSubtypes
    from .investment_filter import InvestmentFilter
    from .investment_holdings_get_request_options import InvestmentHoldingsGetRequestOptions
    from .investment_transaction import InvestmentTransaction
    from .investment_transaction_subtype import InvestmentTransactionSubtype
    from .investment_transaction_type import InvestmentTransactionType
    from .investments_default_update_webhook import InvestmentsDefaultUpdateWebhook
    from .investments_holdings_get_response import InvestmentsHoldingsGetResponse
    from .investments_transactions_get_request_options import InvestmentsTransactionsGetRequestOptions
    from .investments_transactions_get_response import InvestmentsTransactionsGetResponse
    from .investments_transactions_override import InvestmentsTransactionsOverride
    from .ip_address import IpAddress
    from .iso8601date import Iso8601Date
    from .iso8601date_nullable import Iso8601DateNullable
    from .issuing_country import IssuingCountry
    from .item import Item
    from .item_access_token_invalidate_response import ItemAccessTokenInvalidateResponse
    from .item_activity_list_response import ItemActivityListResponse
    from .item_application_list_response import ItemApplicationListResponse
    from .item_application_list_user_auth import ItemApplicationListUserAuth
    from .item_application_scopes_update_response import ItemApplicationScopesUpdateResponse
    from .item_error_webhook import ItemErrorWebhook
    from .item_get_response import ItemGetResponse
    from .item_id import ItemId
    from .item_import_request_options import ItemImportRequestOptions
    from .item_import_request_user_auth import ItemImportRequestUserAuth
    from .item_import_response import ItemImportResponse
    from .item_login_repaired_webhook import ItemLoginRepairedWebhook
    from .item_product_ready_webhook import ItemProductReadyWebhook
    from .item_public_token_create_response import ItemPublicTokenCreateResponse
    from .item_public_token_exchange_response import ItemPublicTokenExchangeResponse
    from .item_remove_response import ItemRemoveResponse
    from .item_status import ItemStatus
    from .item_status_investments import ItemStatusInvestments
    from .item_status_last_webhook import ItemStatusLastWebhook
    from .item_status_nullable import ItemStatusNullable
    from .item_status_transactions import ItemStatusTransactions
    from .item_update_type import ItemUpdateType
    from .item_webhook_update_response import ItemWebhookUpdateResponse
    from .jwk_public_key import JwkPublicKey
    from .jwt_header import JwtHeader
    from .kyc_check_address_summary import KycCheckAddressSummary
    from .kyc_check_date_of_birth_summary import KycCheckDateOfBirthSummary
    from .kyc_check_details import KycCheckDetails
    from .kyc_check_id_number_summary import KycCheckIdNumberSummary
    from .kyc_check_name_summary import KycCheckNameSummary
    from .kyc_check_phone_summary import KycCheckPhoneSummary
    from .last_data_access_times import LastDataAccessTimes
    from .liabilities_account_ids_with_updated_liabilities import LiabilitiesAccountIdsWithUpdatedLiabilities
    from .liabilities_default_update_webhook import LiabilitiesDefaultUpdateWebhook
    from .liabilities_get_request_options import LiabilitiesGetRequestOptions
    from .liabilities_get_response import LiabilitiesGetResponse
    from .liabilities_object import LiabilitiesObject
    from .liability_override import LiabilityOverride
    from .link_callback_metadata import LinkCallbackMetadata
    from .link_delivery_account import LinkDeliveryAccount
    from .link_delivery_callback_webhook import LinkDeliveryCallbackWebhook
    from .link_delivery_communication_method import LinkDeliveryCommunicationMethod
    from .link_delivery_create_response import LinkDeliveryCreateResponse
    from .link_delivery_delivery_method import LinkDeliveryDeliveryMethod
    from .link_delivery_get_response import LinkDeliveryGetResponse
    from .link_delivery_institution import LinkDeliveryInstitution
    from .link_delivery_metadata import LinkDeliveryMetadata
    from .link_delivery_options import LinkDeliveryOptions
    from .link_delivery_recipient import LinkDeliveryRecipient
    from .link_delivery_session_status import LinkDeliverySessionStatus
    from .link_delivery_verification_status import LinkDeliveryVerificationStatus
    from .link_delivery_webhook_callback_type import LinkDeliveryWebhookCallbackType
    from .link_delivery_webhook_communication_method import LinkDeliveryWebhookCommunicationMethod
    from .link_delivery_webhook_delivery_status import LinkDeliveryWebhookDeliveryStatus
    from .link_event_name import LinkEventName
    from .link_o_auth_correlation_id_exchange_response import LinkOAuthCorrelationIdExchangeResponse
    from .link_token_account_filters import LinkTokenAccountFilters
    from .link_token_create_credit_filter import LinkTokenCreateCreditFilter
    from .link_token_create_depository_filter import LinkTokenCreateDepositoryFilter
    from .link_token_create_institution_data import LinkTokenCreateInstitutionData
    from .link_token_create_investment_filter import LinkTokenCreateInvestmentFilter
    from .link_token_create_loan_filter import LinkTokenCreateLoanFilter
    from .link_token_create_request_account_subtypes import LinkTokenCreateRequestAccountSubtypes
    from .link_token_create_request_auth import LinkTokenCreateRequestAuth
    from .link_token_create_request_auth_flow_type import LinkTokenCreateRequestAuthFlowType
    from .link_token_create_request_deposit_switch import LinkTokenCreateRequestDepositSwitch
    from .link_token_create_request_employment import LinkTokenCreateRequestEmployment
    from .link_token_create_request_employment_bank_income import LinkTokenCreateRequestEmploymentBankIncome
    from .link_token_create_request_identity_verification import LinkTokenCreateRequestIdentityVerification
    from .link_token_create_request_income_verification import LinkTokenCreateRequestIncomeVerification
    from .link_token_create_request_income_verification_bank_income import (
        LinkTokenCreateRequestIncomeVerificationBankIncome,
    )
    from .link_token_create_request_income_verification_payroll_income import (
        LinkTokenCreateRequestIncomeVerificationPayrollIncome,
    )
    from .link_token_create_request_payment_initiation import LinkTokenCreateRequestPaymentInitiation
    from .link_token_create_request_transfer import LinkTokenCreateRequestTransfer
    from .link_token_create_request_update import LinkTokenCreateRequestUpdate
    from .link_token_create_request_user import LinkTokenCreateRequestUser
    from .link_token_create_request_user_name import LinkTokenCreateRequestUserName
    from .link_token_create_request_user_stated_income_source import LinkTokenCreateRequestUserStatedIncomeSource
    from .link_token_create_response import LinkTokenCreateResponse
    from .link_token_eu_config import LinkTokenEuConfig
    from .link_token_get_metadata_response import LinkTokenGetMetadataResponse
    from .link_token_get_response import LinkTokenGetResponse
    from .link_token_investments import LinkTokenInvestments
    from .link_user_delivery_status_webhook import LinkUserDeliveryStatusWebhook
    from .loan import Loan
    from .loan_account import LoanAccount
    from .loan_account_subtype import LoanAccountSubtype
    from .loan_account_subtypes import LoanAccountSubtypes
    from .loan_filter import LoanFilter
    from .loan_identifier import LoanIdentifier
    from .loan_identifier_type import LoanIdentifierType
    from .loan_identifiers import LoanIdentifiers
    from .loans import Loans
    from .location import Location
    from .match_summary import MatchSummary
    from .match_summary_code import MatchSummaryCode
    from .meta import Meta
    from .mfa import Mfa
    from .min_last_updated_datetime import MinLastUpdatedDatetime
    from .mortgage_interest_rate import MortgageInterestRate
    from .mortgage_liability import MortgageLiability
    from .mortgage_property_address import MortgagePropertyAddress
    from .multi_document_risk_signal import MultiDocumentRiskSignal
    from .name_match_score import NameMatchScore
    from .net_pay import NetPay
    from .new_accounts_available_webhook import NewAccountsAvailableWebhook
    from .numbers import Numbers
    from .numbers_ach import NumbersAch
    from .numbers_ach_nullable import NumbersAchNullable
    from .numbers_bacs import NumbersBacs
    from .numbers_bacs_nullable import NumbersBacsNullable
    from .numbers_eft import NumbersEft
    from .numbers_eft_nullable import NumbersEftNullable
    from .numbers_iban import NumbersIban
    from .numbers_iban_nullable import NumbersIbanNullable
    from .numbers_international import NumbersInternational
    from .numbers_international_iban import NumbersInternationalIban
    from .numbers_international_nullable import NumbersInternationalNullable
    from .originator import Originator
    from .override_account_type import OverrideAccountType
    from .override_accounts import OverrideAccounts
    from .owner import Owner
    from .owner_override import OwnerOverride
    from .ownership_type import OwnershipType
    from .parties import Parties
    from .partner_customer_create_response import PartnerCustomerCreateResponse
    from .partner_customer_enable_response import PartnerCustomerEnableResponse
    from .partner_customer_get_response import PartnerCustomerGetResponse
    from .partner_customer_o_auth_institutions_get_response import PartnerCustomerOAuthInstitutionsGetResponse
    from .partner_customer_remove_response import PartnerCustomerRemoveResponse
    from .partner_end_customer import PartnerEndCustomer
    from .partner_end_customer_address import PartnerEndCustomerAddress
    from .partner_end_customer_assets_under_management import PartnerEndCustomerAssetsUnderManagement
    from .partner_end_customer_billing_contact import PartnerEndCustomerBillingContact
    from .partner_end_customer_customer_support_info import PartnerEndCustomerCustomerSupportInfo
    from .partner_end_customer_flowdown_status import PartnerEndCustomerFlowdownStatus
    from .partner_end_customer_o_auth_institution import PartnerEndCustomerOAuthInstitution
    from .partner_end_customer_o_auth_institution_application_status import (
        PartnerEndCustomerOAuthInstitutionApplicationStatus,
    )
    from .partner_end_customer_o_auth_institution_environments import PartnerEndCustomerOAuthInstitutionEnvironments
    from .partner_end_customer_o_auth_status_updated_values import PartnerEndCustomerOAuthStatusUpdatedValues
    from .partner_end_customer_o_auth_status_updated_webhook import PartnerEndCustomerOAuthStatusUpdatedWebhook
    from .partner_end_customer_questionnaire_status import PartnerEndCustomerQuestionnaireStatus
    from .partner_end_customer_secrets import PartnerEndCustomerSecrets
    from .partner_end_customer_status import PartnerEndCustomerStatus
    from .partner_end_customer_technical_contact import PartnerEndCustomerTechnicalContact
    from .partner_end_customer_with_secrets import PartnerEndCustomerWithSecrets
    from .party import Party
    from .party_individual import PartyIndividual
    from .party_role_type import PartyRoleType
    from .pay import Pay
    from .pay_frequency import PayFrequency
    from .pay_frequency_value import PayFrequencyValue
    from .pay_period_details import PayPeriodDetails
    from .pay_period_details_pay_frequency import PayPeriodDetailsPayFrequency
    from .pay_stub_deductions_breakdown import PayStubDeductionsBreakdown
    from .pay_stub_deductions_total import PayStubDeductionsTotal
    from .pay_stub_distribution_breakdown import PayStubDistributionBreakdown
    from .pay_stub_earnings_breakdown import PayStubEarningsBreakdown
    from .pay_stub_earnings_breakdown_canonical_description import PayStubEarningsBreakdownCanonicalDescription
    from .pay_stub_earnings_total import PayStubEarningsTotal
    from .pay_stub_pay_period_details import PayStubPayPeriodDetails
    from .pay_stub_taxpayer_id import PayStubTaxpayerId
    from .payment_amount import PaymentAmount
    from .payment_amount_currency import PaymentAmountCurrency
    from .payment_amount_nullable import PaymentAmountNullable
    from .payment_amount_refunded import PaymentAmountRefunded
    from .payment_amount_to_refund import PaymentAmountToRefund
    from .payment_channel import PaymentChannel
    from .payment_consent_max_payment_amount import PaymentConsentMaxPaymentAmount
    from .payment_consent_periodic_alignment import PaymentConsentPeriodicAlignment
    from .payment_consent_periodic_amount import PaymentConsentPeriodicAmount
    from .payment_consent_periodic_amount_amount import PaymentConsentPeriodicAmountAmount
    from .payment_consent_periodic_interval import PaymentConsentPeriodicInterval
    from .payment_consent_valid_date_time import PaymentConsentValidDateTime
    from .payment_initiation_address import PaymentInitiationAddress
    from .payment_initiation_consent import PaymentInitiationConsent
    from .payment_initiation_consent_constraints import PaymentInitiationConsentConstraints
    from .payment_initiation_consent_create_response import PaymentInitiationConsentCreateResponse
    from .payment_initiation_consent_get_response import PaymentInitiationConsentGetResponse
    from .payment_initiation_consent_payment_execute_response import PaymentInitiationConsentPaymentExecuteResponse
    from .payment_initiation_consent_revoke_response import PaymentInitiationConsentRevokeResponse
    from .payment_initiation_consent_scope import PaymentInitiationConsentScope
    from .payment_initiation_consent_status import PaymentInitiationConsentStatus
    from .payment_initiation_maximum_payment_amount import PaymentInitiationMaximumPaymentAmount
    from .payment_initiation_metadata import PaymentInitiationMetadata
    from .payment_initiation_optional_restriction_bacs import PaymentInitiationOptionalRestrictionBacs
    from .payment_initiation_payment import PaymentInitiationPayment
    from .payment_initiation_payment_create_response import PaymentInitiationPaymentCreateResponse
    from .payment_initiation_payment_create_status import PaymentInitiationPaymentCreateStatus
    from .payment_initiation_payment_get_response import PaymentInitiationPaymentGetResponse
    from .payment_initiation_payment_list_response import PaymentInitiationPaymentListResponse
    from .payment_initiation_payment_reverse_response import PaymentInitiationPaymentReverseResponse
    from .payment_initiation_payment_status import PaymentInitiationPaymentStatus
    from .payment_initiation_payment_token_create_response import PaymentInitiationPaymentTokenCreateResponse
    from .payment_initiation_recipient import PaymentInitiationRecipient
    from .payment_initiation_recipient_create_response import PaymentInitiationRecipientCreateResponse
    from .payment_initiation_recipient_get_response import PaymentInitiationRecipientGetResponse
    from .payment_initiation_recipient_list_response import PaymentInitiationRecipientListResponse
    from .payment_initiation_standing_order_metadata import PaymentInitiationStandingOrderMetadata
    from .payment_meta import PaymentMeta
    from .payment_profile_create_response import PaymentProfileCreateResponse
    from .payment_profile_get_response import PaymentProfileGetResponse
    from .payment_profile_remove_response import PaymentProfileRemoveResponse
    from .payment_profile_status import PaymentProfileStatus
    from .payment_profile_token import PaymentProfileToken
    from .payment_schedule_interval import PaymentScheduleInterval
    from .payment_scheme import PaymentScheme
    from .payment_status_update_webhook import PaymentStatusUpdateWebhook
    from .payroll_income_account_data import PayrollIncomeAccountData
    from .payroll_income_object import PayrollIncomeObject
    from .payroll_income_rate_of_pay import PayrollIncomeRateOfPay
    from .payroll_item import PayrollItem
    from .payroll_item_status import PayrollItemStatus
    from .payroll_risk_signals_item import PayrollRiskSignalsItem
    from .paystub import Paystub
    from .paystub_address import PaystubAddress
    from .paystub_deduction import PaystubDeduction
    from .paystub_details import PaystubDetails
    from .paystub_employer import PaystubEmployer
    from .paystub_override import PaystubOverride
    from .paystub_override_employee import PaystubOverrideEmployee
    from .paystub_override_employee_address import PaystubOverrideEmployeeAddress
    from .paystub_override_employer import PaystubOverrideEmployer
    from .paystub_pay_frequency import PaystubPayFrequency
    from .paystub_ytd_details import PaystubYtdDetails
    from .pending_expiration_webhook import PendingExpirationWebhook
    from .personal_finance_category import PersonalFinanceCategory
    from .phone_number import PhoneNumber
    from .phone_number_match_score import PhoneNumberMatchScore
    from .phone_number_type import PhoneNumberType
    from .phone_type import PhoneType
    from .physical_document_category import PhysicalDocumentCategory
    from .physical_document_extracted_data import PhysicalDocumentExtractedData
    from .physical_document_extracted_data_analysis import PhysicalDocumentExtractedDataAnalysis
    from .physical_document_id_number import PhysicalDocumentIdNumber
    from .physical_document_images import PhysicalDocumentImages
    from .plaid_error import PlaidError
    from .plaid_error_type import PlaidErrorType
    from .platform_ids import PlatformIds
    from .po_box_status import PoBoxStatus
    from .postal_code import PostalCode
    from .postal_code_nullable import PostalCodeNullable
    from .previous_identity_verification_attempt_id import PreviousIdentityVerificationAttemptId
    from .processor_auth_get_response import ProcessorAuthGetResponse
    from .processor_balance_get_request_options import ProcessorBalanceGetRequestOptions
    from .processor_balance_get_response import ProcessorBalanceGetResponse
    from .processor_bank_transfer_create_response import ProcessorBankTransferCreateResponse
    from .processor_identity_get_response import ProcessorIdentityGetResponse
    from .processor_number import ProcessorNumber
    from .processor_signal_decision_report_response import ProcessorSignalDecisionReportResponse
    from .processor_signal_evaluate_response import ProcessorSignalEvaluateResponse
    from .processor_signal_return_report_response import ProcessorSignalReturnReportResponse
    from .processor_stripe_bank_account_token_create_response import ProcessorStripeBankAccountTokenCreateResponse
    from .processor_token import ProcessorToken
    from .processor_token_create_response import ProcessorTokenCreateResponse
    from .product_access import ProductAccess
    from .product_status import ProductStatus
    from .product_status_breakdown import ProductStatusBreakdown
    from .product_status_breakdown_refresh_interval import ProductStatusBreakdownRefreshInterval
    from .product_status_status import ProductStatusStatus
    from .products import Products
    from .program_archived import ProgramArchived
    from .program_name_sensitivity import ProgramNameSensitivity
    from .projected_income_summary_field_number import ProjectedIncomeSummaryFieldNumber
    from .proxy_type import ProxyType
    from .pslf_status import PslfStatus
    from .recaptcha_required_error import RecaptchaRequiredError
    from .recipient_bacs import RecipientBacs
    from .recipient_bacs_nullable import RecipientBacsNullable
    from .recurrence import Recurrence
    from .recurring_cancelled_webhook import RecurringCancelledWebhook
    from .recurring_new_transfer_webhook import RecurringNewTransferWebhook
    from .recurring_transaction_frequency import RecurringTransactionFrequency
    from .recurring_transactions_update_webhook import RecurringTransactionsUpdateWebhook
    from .recurring_transfer import RecurringTransfer
    from .recurring_transfer_id import RecurringTransferId
    from .recurring_transfer_nullable import RecurringTransferNullable
    from .recurring_transfer_skipped_webhook import RecurringTransferSkippedWebhook
    from .region import Region
    from .region_nullable import RegionNullable
    from .removed_transaction import RemovedTransaction
    from .report_type import ReportType
    from .reporting_information import ReportingInformation
    from .request_id import RequestId
    from .review_comment import ReviewComment
    from .risk_check_behavior import RiskCheckBehavior
    from .risk_check_behavior_bot_detected_label import RiskCheckBehaviorBotDetectedLabel
    from .risk_check_behavior_fraud_ring_detected_label import RiskCheckBehaviorFraudRingDetectedLabel
    from .risk_check_behavior_user_interactions_label import RiskCheckBehaviorUserInteractionsLabel
    from .risk_check_details import RiskCheckDetails
    from .risk_check_device import RiskCheckDevice
    from .risk_check_email import RiskCheckEmail
    from .risk_check_email_domain_is_custom import RiskCheckEmailDomainIsCustom
    from .risk_check_email_domain_is_disposable import RiskCheckEmailDomainIsDisposable
    from .risk_check_email_domain_is_free_provider import RiskCheckEmailDomainIsFreeProvider
    from .risk_check_email_is_deliverable_status import RiskCheckEmailIsDeliverableStatus
    from .risk_check_email_top_level_domain_is_suspicious import RiskCheckEmailTopLevelDomainIsSuspicious
    from .risk_check_linked_service import RiskCheckLinkedService
    from .risk_check_phone import RiskCheckPhone
    from .risk_signal_document_reference import RiskSignalDocumentReference
    from .role import Role
    from .role_detail import RoleDetail
    from .roles import Roles
    from .sandbox_bank_transfer_fire_webhook_response import SandboxBankTransferFireWebhookResponse
    from .sandbox_bank_transfer_simulate_response import SandboxBankTransferSimulateResponse
    from .sandbox_income_fire_webhook_response import SandboxIncomeFireWebhookResponse
    from .sandbox_item_fire_webhook_response import SandboxItemFireWebhookResponse
    from .sandbox_item_reset_login_response import SandboxItemResetLoginResponse
    from .sandbox_item_set_verification_status_response import SandboxItemSetVerificationStatusResponse
    from .sandbox_oauth_select_accounts_response import SandboxOauthSelectAccountsResponse
    from .sandbox_override_password import SandboxOverridePassword
    from .sandbox_override_username import SandboxOverrideUsername
    from .sandbox_payment_profile_reset_login_response import SandboxPaymentProfileResetLoginResponse
    from .sandbox_processor_token_create_request_options import SandboxProcessorTokenCreateRequestOptions
    from .sandbox_processor_token_create_response import SandboxProcessorTokenCreateResponse
    from .sandbox_public_token_create_request_income_verification_bank_income import (
        SandboxPublicTokenCreateRequestIncomeVerificationBankIncome,
    )
    from .sandbox_public_token_create_request_options import SandboxPublicTokenCreateRequestOptions
    from .sandbox_public_token_create_request_options_income_verification import (
        SandboxPublicTokenCreateRequestOptionsIncomeVerification,
    )
    from .sandbox_public_token_create_request_options_transactions import (
        SandboxPublicTokenCreateRequestOptionsTransactions,
    )
    from .sandbox_public_token_create_response import SandboxPublicTokenCreateResponse
    from .sandbox_transfer_fire_webhook_response import SandboxTransferFireWebhookResponse
    from .sandbox_transfer_repayment_simulate_response import SandboxTransferRepaymentSimulateResponse
    from .sandbox_transfer_simulate_response import SandboxTransferSimulateResponse
    from .sandbox_transfer_sweep_simulate_response import SandboxTransferSweepSimulateResponse
    from .sandbox_transfer_test_clock_advance_response import SandboxTransferTestClockAdvanceResponse
    from .sandbox_transfer_test_clock_create_response import SandboxTransferTestClockCreateResponse
    from .sandbox_transfer_test_clock_get_response import SandboxTransferTestClockGetResponse
    from .sandbox_transfer_test_clock_list_response import SandboxTransferTestClockListResponse
    from .scopes import Scopes
    from .scopes_context import ScopesContext
    from .scopes_nullable import ScopesNullable
    from .scopes_state import ScopesState
    from .screening_hit_analysis import ScreeningHitAnalysis
    from .screening_hit_data import ScreeningHitData
    from .screening_hit_date_of_birth_item import ScreeningHitDateOfBirthItem
    from .screening_hit_documents_items import ScreeningHitDocumentsItems
    from .screening_hit_names_items import ScreeningHitNamesItems
    from .screening_status_updated_webhook import ScreeningStatusUpdatedWebhook
    from .security import Security
    from .security_override import SecurityOverride
    from .sender_bacs_nullable import SenderBacsNullable
    from .service import Service
    from .service_product_fulfillment import ServiceProductFulfillment
    from .service_product_fulfillment_detail import ServiceProductFulfillmentDetail
    from .service_product_fulfillment_identifier import ServiceProductFulfillmentIdentifier
    from .servicer_address_data import ServicerAddressData
    from .services import Services
    from .shareable_url import ShareableUrl
    from .signal_address_data import SignalAddressData
    from .signal_decision_outcome import SignalDecisionOutcome
    from .signal_decision_report_response import SignalDecisionReportResponse
    from .signal_device import SignalDevice
    from .signal_evaluate_core_attributes import SignalEvaluateCoreAttributes
    from .signal_evaluate_response import SignalEvaluateResponse
    from .signal_payment_method import SignalPaymentMethod
    from .signal_person_name import SignalPersonName
    from .signal_prepare_response import SignalPrepareResponse
    from .signal_return_report_response import SignalReturnReportResponse
    from .signal_score import SignalScore
    from .signal_scores import SignalScores
    from .signal_user import SignalUser
    from .signal_warning import SignalWarning
    from .simulated_transfer_sweep import SimulatedTransferSweep
    from .single_document_risk_signal import SingleDocumentRiskSignal
    from .source import Source
    from .source_uid import SourceUid
    from .standalone_account_type import StandaloneAccountType
    from .standalone_currency_code_list import StandaloneCurrencyCodeList
    from .standalone_investment_transaction_buy_type import StandaloneInvestmentTransactionBuyType
    from .standalone_investment_transaction_cash_type import StandaloneInvestmentTransactionCashType
    from .standalone_investment_transaction_fee_type import StandaloneInvestmentTransactionFeeType
    from .standalone_investment_transaction_sell_type import StandaloneInvestmentTransactionSellType
    from .standalone_investment_transaction_transfer_type import StandaloneInvestmentTransactionTransferType
    from .standalone_investment_transaction_type import StandaloneInvestmentTransactionType
    from .status import Status
    from .statuses import Statuses
    from .strategy import Strategy
    from .street import Street
    from .street2 import Street2
    from .street_nullable import StreetNullable
    from .student_loan import StudentLoan
    from .student_loan_repayment_model import StudentLoanRepaymentModel
    from .student_loan_status import StudentLoanStatus
    from .student_loan_status_type import StudentLoanStatusType
    from .student_repayment_plan import StudentRepaymentPlan
    from .student_repayment_plan_type import StudentRepaymentPlanType
    from .sync_updates_available_webhook import SyncUpdatesAvailableWebhook
    from .taxform import Taxform
    from .taxpayer_id import TaxpayerId
    from .taxpayer_identifier import TaxpayerIdentifier
    from .taxpayer_identifier_type import TaxpayerIdentifierType
    from .taxpayer_identifiers import TaxpayerIdentifiers
    from .timestamp import Timestamp
    from .timestamp_nullable import TimestampNullable
    from .total import Total
    from .total_canonical_description import TotalCanonicalDescription
    from .transaction import Transaction
    from .transaction_base import TransactionBase
    from .transaction_base_transaction_type import TransactionBaseTransactionType
    from .transaction_code import TransactionCode
    from .transaction_counterparty import TransactionCounterparty
    from .transaction_data import TransactionData
    from .transaction_override import TransactionOverride
    from .transaction_payment_channel import TransactionPaymentChannel
    from .transaction_stream import TransactionStream
    from .transaction_stream_amount import TransactionStreamAmount
    from .transaction_stream_status import TransactionStreamStatus
    from .transactions_category_rule import TransactionsCategoryRule
    from .transactions_enhance_get_response import TransactionsEnhanceGetResponse
    from .transactions_enrich_get_response import TransactionsEnrichGetResponse
    from .transactions_enrich_request_options import TransactionsEnrichRequestOptions
    from .transactions_get_request_options import TransactionsGetRequestOptions
    from .transactions_get_response import TransactionsGetResponse
    from .transactions_recurring_get_request_options import TransactionsRecurringGetRequestOptions
    from .transactions_recurring_get_response import TransactionsRecurringGetResponse
    from .transactions_refresh_response import TransactionsRefreshResponse
    from .transactions_removed_webhook import TransactionsRemovedWebhook
    from .transactions_rule_details import TransactionsRuleDetails
    from .transactions_rule_field import TransactionsRuleField
    from .transactions_rule_type import TransactionsRuleType
    from .transactions_rules_create_response import TransactionsRulesCreateResponse
    from .transactions_rules_list_response import TransactionsRulesListResponse
    from .transactions_rules_remove_response import TransactionsRulesRemoveResponse
    from .transactions_sync_request_options import TransactionsSyncRequestOptions
    from .transactions_sync_response import TransactionsSyncResponse
    from .transfer import Transfer
    from .transfer_access_token import TransferAccessToken
    from .transfer_account_id import TransferAccountId
    from .transfer_amount import TransferAmount
    from .transfer_authorization import TransferAuthorization
    from .transfer_authorization_create_response import TransferAuthorizationCreateResponse
    from .transfer_authorization_decision import TransferAuthorizationDecision
    from .transfer_authorization_decision_rationale import TransferAuthorizationDecisionRationale
    from .transfer_authorization_decision_rationale_code import TransferAuthorizationDecisionRationaleCode
    from .transfer_authorization_device import TransferAuthorizationDevice
    from .transfer_authorization_guarantee_decision import TransferAuthorizationGuaranteeDecision
    from .transfer_authorization_guarantee_decision_rationale import TransferAuthorizationGuaranteeDecisionRationale
    from .transfer_authorization_guarantee_decision_rationale_code import (
        TransferAuthorizationGuaranteeDecisionRationaleCode,
    )
    from .transfer_authorization_id import TransferAuthorizationId
    from .transfer_authorization_idempotency_key import TransferAuthorizationIdempotencyKey
    from .transfer_authorization_proposed_transfer import TransferAuthorizationProposedTransfer
    from .transfer_authorization_user_in_request import TransferAuthorizationUserInRequest
    from .transfer_cancel_response import TransferCancelResponse
    from .transfer_capabilities_get_response import TransferCapabilitiesGetResponse
    from .transfer_capabilities_get_rtp import TransferCapabilitiesGetRtp
    from .transfer_configuration_get_response import TransferConfigurationGetResponse
    from .transfer_create_idempotency_key import TransferCreateIdempotencyKey
    from .transfer_create_response import TransferCreateResponse
    from .transfer_device import TransferDevice
    from .transfer_diligence_status import TransferDiligenceStatus
    from .transfer_event import TransferEvent
    from .transfer_event_list_response import TransferEventListResponse
    from .transfer_event_list_transfer_type import TransferEventListTransferType
    from .transfer_event_sync_response import TransferEventSyncResponse
    from .transfer_event_type import TransferEventType
    from .transfer_events_update_webhook import TransferEventsUpdateWebhook
    from .transfer_expected_settlement_schedule_item import TransferExpectedSettlementScheduleItem
    from .transfer_failure import TransferFailure
    from .transfer_funding_account_id_request import TransferFundingAccountIdRequest
    from .transfer_funding_account_id_response import TransferFundingAccountIdResponse
    from .transfer_get_response import TransferGetResponse
    from .transfer_id import TransferId
    from .transfer_id_for_refund import TransferIdForRefund
    from .transfer_intent_authorization_decision import TransferIntentAuthorizationDecision
    from .transfer_intent_create import TransferIntentCreate
    from .transfer_intent_create_mode import TransferIntentCreateMode
    from .transfer_intent_create_network import TransferIntentCreateNetwork
    from .transfer_intent_create_response import TransferIntentCreateResponse
    from .transfer_intent_get import TransferIntentGet
    from .transfer_intent_get_failure_reason import TransferIntentGetFailureReason
    from .transfer_intent_get_response import TransferIntentGetResponse
    from .transfer_intent_status import TransferIntentStatus
    from .transfer_list_response import TransferListResponse
    from .transfer_metadata import TransferMetadata
    from .transfer_metrics_get_response import TransferMetricsGetResponse
    from .transfer_migrate_account_response import TransferMigrateAccountResponse
    from .transfer_network import TransferNetwork
    from .transfer_originator_create_response import TransferOriginatorCreateResponse
    from .transfer_originator_get_response import TransferOriginatorGetResponse
    from .transfer_originator_list_response import TransferOriginatorListResponse
    from .transfer_payment_profile_token import TransferPaymentProfileToken
    from .transfer_questionnaire_create_response import TransferQuestionnaireCreateResponse
    from .transfer_recurring_cancel_response import TransferRecurringCancelResponse
    from .transfer_recurring_create_response import TransferRecurringCreateResponse
    from .transfer_recurring_get_response import TransferRecurringGetResponse
    from .transfer_recurring_idempotency_key import TransferRecurringIdempotencyKey
    from .transfer_recurring_list_response import TransferRecurringListResponse
    from .transfer_recurring_schedule import TransferRecurringSchedule
    from .transfer_recurring_status import TransferRecurringStatus
    from .transfer_refund import TransferRefund
    from .transfer_refund_amount import TransferRefundAmount
    from .transfer_refund_cancel_response import TransferRefundCancelResponse
    from .transfer_refund_create_response import TransferRefundCreateResponse
    from .transfer_refund_get_response import TransferRefundGetResponse
    from .transfer_refund_id import TransferRefundId
    from .transfer_refund_idempotency_key import TransferRefundIdempotencyKey
    from .transfer_refund_status import TransferRefundStatus
    from .transfer_repayment import TransferRepayment
    from .transfer_repayment_list_response import TransferRepaymentListResponse
    from .transfer_repayment_return import TransferRepaymentReturn
    from .transfer_repayment_return_list_response import TransferRepaymentReturnListResponse
    from .transfer_schedule_interval_count import TransferScheduleIntervalCount
    from .transfer_schedule_interval_unit import TransferScheduleIntervalUnit
    from .transfer_status import TransferStatus
    from .transfer_sweep import TransferSweep
    from .transfer_sweep_amount import TransferSweepAmount
    from .transfer_sweep_get_response import TransferSweepGetResponse
    from .transfer_sweep_id import TransferSweepId
    from .transfer_sweep_list_response import TransferSweepListResponse
    from .transfer_sweep_status import TransferSweepStatus
    from .transfer_test_clock import TransferTestClock
    from .transfer_test_clock_id import TransferTestClockId
    from .transfer_type import TransferType
    from .transfer_user_address_in_request import TransferUserAddressInRequest
    from .transfer_user_address_in_response import TransferUserAddressInResponse
    from .transfer_user_in_request import TransferUserInRequest
    from .transfer_user_in_request_deprecated import TransferUserInRequestDeprecated
    from .transfer_user_in_response import TransferUserInResponse
    from .unofficial_currency_code_list import UnofficialCurrencyCodeList
    from .update_entity_screening_request_search_terms import UpdateEntityScreeningRequestSearchTerms
    from .update_individual_screening_request_search_terms import UpdateIndividualScreeningRequestSearchTerms
    from .url import Url
    from .url_nullable import UrlNullable
    from .user_address import UserAddress
    from .user_create_response import UserCreateResponse
    from .user_custom_password import UserCustomPassword
    from .user_id import UserId
    from .user_id_number import UserIdNumber
    from .user_permission_revoked_webhook import UserPermissionRevokedWebhook
    from .user_stated_income_source_category import UserStatedIncomeSourceCategory
    from .user_stated_income_source_frequency import UserStatedIncomeSourceFrequency
    from .user_stated_income_source_pay_type import UserStatedIncomeSourcePayType
    from .user_token import UserToken
    from .utc_offset import UtcOffset
    from .validation_source import ValidationSource
    from .validation_sources import ValidationSources
    from .verification_expired_webhook import VerificationExpiredWebhook
    from .verification_of_asset import VerificationOfAsset
    from .verification_of_asset_response import VerificationOfAssetResponse
    from .verification_refresh_status import VerificationRefreshStatus
    from .verification_status import VerificationStatus
    from .virtual_time import VirtualTime
    from .w2 import W2
    from .w2box12 import W2Box12
    from .w2state_and_local_wages import W2StateAndLocalWages
    from .wallet import Wallet
    from .wallet_balance import WalletBalance
    from .wallet_create_response import WalletCreateResponse
    from .wallet_get_response import WalletGetResponse
    from .wallet_iso_currency_code import WalletIsoCurrencyCode
    from .wallet_list_response import WalletListResponse
    from .wallet_numbers import WalletNumbers
    from .wallet_status import WalletStatus
    from .wallet_transaction import WalletTransaction
    from .wallet_transaction_amount import WalletTransactionAmount
    from .wallet_transaction_counterparty import WalletTransactionCounterparty
    from .wallet_transaction_counterparty_bacs import WalletTransactionCounterpartyBacs
    from .wallet_transaction_counterparty_international import WalletTransactionCounterpartyInternational
    from .wallet_transaction_counterparty_numbers import WalletTransactionCounterpartyNumbers
    from .wallet_transaction_execute_response import WalletTransactionExecuteResponse
    from .wallet_transaction_get_response import WalletTransactionGetResponse
    from .wallet_transaction_idempotency_key import WalletTransactionIdempotencyKey
    from .wallet_transaction_list_request_options import WalletTransactionListRequestOptions
    from .wallet_transaction_list_response import WalletTransactionListResponse
    from .wallet_transaction_status import WalletTransactionStatus
    from .wallet_transaction_status_update_webhook import WalletTransactionStatusUpdateWebhook
    from .wallet_transaction_type import WalletTransactionType
    from .wallet_transactions_list_request import WalletTransactionsListRequest
    from .warning import Warning
    from .warning_warning_code import WarningWarningCode
    from .watchlist_program_id import WatchlistProgramId
    from .watchlist_screening_audit_trail import WatchlistScreeningAuditTrail
    from .watchlist_screening_document import WatchlistScreeningDocument
    from .watchlist_screening_document_type import WatchlistScreeningDocumentType
    from .watchlist_screening_document_value import WatchlistScreeningDocumentValue
    from .watchlist_screening_document_value_nullable import WatchlistScreeningDocumentValueNullable
    from .watchlist_screening_entity_create_response import WatchlistScreeningEntityCreateResponse
    from .watchlist_screening_entity_get_response import WatchlistScreeningEntityGetResponse
    from .watchlist_screening_entity_history_list_response import WatchlistScreeningEntityHistoryListResponse
    from .watchlist_screening_entity_hit_list_response import WatchlistScreeningEntityHitListResponse
    from .watchlist_screening_entity_list_response import WatchlistScreeningEntityListResponse
    from .watchlist_screening_entity_program_get_response import WatchlistScreeningEntityProgramGetResponse
    from .watchlist_screening_entity_program_list_response import WatchlistScreeningEntityProgramListResponse
    from .watchlist_screening_entity_review_create_response import WatchlistScreeningEntityReviewCreateResponse
    from .watchlist_screening_entity_review_list_response import WatchlistScreeningEntityReviewListResponse
    from .watchlist_screening_entity_update_request_resettable_field import (
        WatchlistScreeningEntityUpdateRequestResettableField,
    )
    from .watchlist_screening_entity_update_request_resettable_field_list import (
        WatchlistScreeningEntityUpdateRequestResettableFieldList,
    )
    from .watchlist_screening_entity_update_response import WatchlistScreeningEntityUpdateResponse
    from .watchlist_screening_hit import WatchlistScreeningHit
    from .watchlist_screening_hit_id import WatchlistScreeningHitId
    from .watchlist_screening_hit_locations import WatchlistScreeningHitLocations
    from .watchlist_screening_hit_status import WatchlistScreeningHitStatus
    from .watchlist_screening_individual import WatchlistScreeningIndividual
    from .watchlist_screening_individual_create_response import WatchlistScreeningIndividualCreateResponse
    from .watchlist_screening_individual_get_response import WatchlistScreeningIndividualGetResponse
    from .watchlist_screening_individual_history_list_response import WatchlistScreeningIndividualHistoryListResponse
    from .watchlist_screening_individual_hit_list_response import WatchlistScreeningIndividualHitListResponse
    from .watchlist_screening_individual_id import WatchlistScreeningIndividualId
    from .watchlist_screening_individual_id_nullable import WatchlistScreeningIndividualIdNullable
    from .watchlist_screening_individual_list_response import WatchlistScreeningIndividualListResponse
    from .watchlist_screening_individual_name import WatchlistScreeningIndividualName
    from .watchlist_screening_individual_program_get_response import WatchlistScreeningIndividualProgramGetResponse
    from .watchlist_screening_individual_program_list_response import WatchlistScreeningIndividualProgramListResponse
    from .watchlist_screening_individual_review_create_response import WatchlistScreeningIndividualReviewCreateResponse
    from .watchlist_screening_individual_review_list_response import WatchlistScreeningIndividualReviewListResponse
    from .watchlist_screening_individual_update_request_resettable_field import (
        WatchlistScreeningIndividualUpdateRequestResettableField,
    )
    from .watchlist_screening_individual_update_request_resettable_field_list import (
        WatchlistScreeningIndividualUpdateRequestResettableFieldList,
    )
    from .watchlist_screening_individual_update_response import WatchlistScreeningIndividualUpdateResponse
    from .watchlist_screening_phone_number import WatchlistScreeningPhoneNumber
    from .watchlist_screening_phone_number_nullable import WatchlistScreeningPhoneNumberNullable
    from .watchlist_screening_request_search_terms import WatchlistScreeningRequestSearchTerms
    from .watchlist_screening_review import WatchlistScreeningReview
    from .watchlist_screening_review_id import WatchlistScreeningReviewId
    from .watchlist_screening_search_terms import WatchlistScreeningSearchTerms
    from .watchlist_screening_status import WatchlistScreeningStatus
    from .weak_alias_determination import WeakAliasDetermination
    from .webhook_environment_values import WebhookEnvironmentValues
    from .webhook_type import WebhookType
    from .webhook_update_acknowledged_webhook import WebhookUpdateAcknowledgedWebhook
    from .webhook_verification_key_get_response import WebhookVerificationKeyGetResponse
    from .ytd_gross_income_summary_field_number import YtdGrossIncomeSummaryFieldNumber
    from .ytd_net_income_summary_field_number import YtdNetIncomeSummaryFieldNumber
_dynamic_imports: typing.Dict[str, str] = {
    "AccessToken": ".access_token",
    "AccessTokenNullable": ".access_token_nullable",
    "AccountAccess": ".account_access",
    "AccountAssets": ".account_assets",
    "AccountBalance": ".account_balance",
    "AccountBase": ".account_base",
    "AccountBaseVerificationStatus": ".account_base_verification_status",
    "AccountFilter": ".account_filter",
    "AccountFilterSubtypes": ".account_filter_subtypes",
    "AccountFiltersResponse": ".account_filters_response",
    "AccountIdentity": ".account_identity",
    "AccountIdentityMatchScore": ".account_identity_match_score",
    "AccountIdsWithUpdatedIdentity": ".account_ids_with_updated_identity",
    "AccountProductAccess": ".account_product_access",
    "AccountProductAccessNullable": ".account_product_access_nullable",
    "AccountSelectionCardinality": ".account_selection_cardinality",
    "AccountSubtype": ".account_subtype",
    "AccountSubtypes": ".account_subtypes",
    "AccountType": ".account_type",
    "AccountsBalanceGetRequestOptions": ".accounts_balance_get_request_options",
    "AccountsGetRequestOptions": ".accounts_get_request_options",
    "AccountsGetResponse": ".accounts_get_response",
    "AchClass": ".ach_class",
    "ActionState": ".action_state",
    "Activity": ".activity",
    "ActivityType": ".activity_type",
    "Address": ".address",
    "AddressData": ".address_data",
    "AddressDataNullable": ".address_data_nullable",
    "AddressMatchScore": ".address_match_score",
    "AddressNullable": ".address_nullable",
    "AddressPurposeLabel": ".address_purpose_label",
    "ApiClientId": ".api_client_id",
    "ApiSecret": ".api_secret",
    "Application": ".application",
    "ApplicationGetResponse": ".application_get_response",
    "ApplicationId": ".application_id",
    "Apr": ".apr",
    "AprAprType": ".apr_apr_type",
    "Asset": ".asset",
    "AssetDetail": ".asset_detail",
    "AssetHolder": ".asset_holder",
    "AssetHolderName": ".asset_holder_name",
    "AssetOwner": ".asset_owner",
    "AssetOwners": ".asset_owners",
    "AssetReport": ".asset_report",
    "AssetReportAddOns": ".asset_report_add_ons",
    "AssetReportAuditCopyCreateResponse": ".asset_report_audit_copy_create_response",
    "AssetReportAuditCopyRemoveResponse": ".asset_report_audit_copy_remove_response",
    "AssetReportCreateRequestOptions": ".asset_report_create_request_options",
    "AssetReportCreateResponse": ".asset_report_create_response",
    "AssetReportFilterResponse": ".asset_report_filter_response",
    "AssetReportFreddie": ".asset_report_freddie",
    "AssetReportFreddieGetResponse": ".asset_report_freddie_get_response",
    "AssetReportGetRequestOptions": ".asset_report_get_request_options",
    "AssetReportGetResponse": ".asset_report_get_response",
    "AssetReportId": ".asset_report_id",
    "AssetReportItem": ".asset_report_item",
    "AssetReportPdfGetRequestOptions": ".asset_report_pdf_get_request_options",
    "AssetReportPdfGetResponse": ".asset_report_pdf_get_response",
    "AssetReportRefreshAssetReportToken": ".asset_report_refresh_asset_report_token",
    "AssetReportRefreshRequestOptions": ".asset_report_refresh_request_options",
    "AssetReportRefreshResponse": ".asset_report_refresh_response",
    "AssetReportRemoveResponse": ".asset_report_remove_response",
    "AssetReportToken": ".asset_report_token",
    "AssetReportTransaction": ".asset_report_transaction",
    "AssetReportUser": ".asset_report_user",
    "AssetTransaction": ".asset_transaction",
    "AssetTransactionCategoryType": ".asset_transaction_category_type",
    "AssetTransactionDescription": ".asset_transaction_description",
    "AssetTransactionDetail": ".asset_transaction_detail",
    "AssetTransactionType": ".asset_transaction_type",
    "AssetTransactions": ".asset_transactions",
    "AssetType": ".asset_type",
    "Assets": ".assets",
    "AssetsErrorWebhook": ".assets_error_webhook",
    "AssetsProductReadyWebhook": ".assets_product_ready_webhook",
    "AuthGetNumbers": ".auth_get_numbers",
    "AuthGetRequestOptions": ".auth_get_request_options",
    "AuthGetResponse": ".auth_get_response",
    "AuthMetadata": ".auth_metadata",
    "AuthSupportedMethods": ".auth_supported_methods",
    "AutomaticallyVerifiedWebhook": ".automatically_verified_webhook",
    "BankInitiatedReturnRisk": ".bank_initiated_return_risk",
    "BankInitiatedRiskTier": ".bank_initiated_risk_tier",
    "BankTransfer": ".bank_transfer",
    "BankTransferAccessToken": ".bank_transfer_access_token",
    "BankTransferAmount": ".bank_transfer_amount",
    "BankTransferBalance": ".bank_transfer_balance",
    "BankTransferBalanceGetResponse": ".bank_transfer_balance_get_response",
    "BankTransferCancelResponse": ".bank_transfer_cancel_response",
    "BankTransferCreateResponse": ".bank_transfer_create_response",
    "BankTransferDirection": ".bank_transfer_direction",
    "BankTransferEvent": ".bank_transfer_event",
    "BankTransferEventListBankTransferType": ".bank_transfer_event_list_bank_transfer_type",
    "BankTransferEventListDirection": ".bank_transfer_event_list_direction",
    "BankTransferEventListResponse": ".bank_transfer_event_list_response",
    "BankTransferEventSyncResponse": ".bank_transfer_event_sync_response",
    "BankTransferEventType": ".bank_transfer_event_type",
    "BankTransferFailure": ".bank_transfer_failure",
    "BankTransferGetResponse": ".bank_transfer_get_response",
    "BankTransferId": ".bank_transfer_id",
    "BankTransferIdempotencyKey": ".bank_transfer_idempotency_key",
    "BankTransferListResponse": ".bank_transfer_list_response",
    "BankTransferMetadata": ".bank_transfer_metadata",
    "BankTransferMigrateAccountResponse": ".bank_transfer_migrate_account_response",
    "BankTransferNetwork": ".bank_transfer_network",
    "BankTransferStatus": ".bank_transfer_status",
    "BankTransferSweep": ".bank_transfer_sweep",
    "BankTransferSweepGetResponse": ".bank_transfer_sweep_get_response",
    "BankTransferSweepListResponse": ".bank_transfer_sweep_list_response",
    "BankTransferType": ".bank_transfer_type",
    "BankTransferUser": ".bank_transfer_user",
    "BankTransfersEventsUpdateWebhook": ".bank_transfers_events_update_webhook",
    "BankTransfersEventsUpdateWebhookForAuth": ".bank_transfers_events_update_webhook_for_auth",
    "CategoriesGetRequest": ".categories_get_request",
    "CategoriesGetResponse": ".categories_get_response",
    "Category": ".category",
    "Cause": ".cause",
    "City": ".city",
    "CityNullable": ".city_nullable",
    "ClientProvidedEnhancedTransaction": ".client_provided_enhanced_transaction",
    "ClientProvidedEnrichedTransaction": ".client_provided_enriched_transaction",
    "ClientProvidedRawTransaction": ".client_provided_raw_transaction",
    "ClientProvidedTransaction": ".client_provided_transaction",
    "ClientProvidedTransactionLocation": ".client_provided_transaction_location",
    "ClientUserId": ".client_user_id",
    "ClientUserIdNullable": ".client_user_id_nullable",
    "ConnectedApplication": ".connected_application",
    "ConsentPaymentIdempotencyKey": ".consent_payment_idempotency_key",
    "Counterparty": ".counterparty",
    "CounterpartyType": ".counterparty_type",
    "CountryCode": ".country_code",
    "Credit1099": ".credit1099",
    "Credit1099Filer": ".credit1099filer",
    "Credit1099Payer": ".credit1099payer",
    "Credit1099Recipient": ".credit1099recipient",
    "CreditAccount": ".credit_account",
    "CreditAccountSubtype": ".credit_account_subtype",
    "CreditAccountSubtypes": ".credit_account_subtypes",
    "CreditAmountWithCurrency": ".credit_amount_with_currency",
    "CreditAuditCopyTokenCreateResponse": ".credit_audit_copy_token_create_response",
    "CreditAuditCopyTokenRemoveResponse": ".credit_audit_copy_token_remove_response",
    "CreditAuditCopyTokenUpdateResponse": ".credit_audit_copy_token_update_response",
    "CreditBankEmployer": ".credit_bank_employer",
    "CreditBankEmployment": ".credit_bank_employment",
    "CreditBankEmploymentGetResponse": ".credit_bank_employment_get_response",
    "CreditBankEmploymentItem": ".credit_bank_employment_item",
    "CreditBankEmploymentReport": ".credit_bank_employment_report",
    "CreditBankEmploymentWarning": ".credit_bank_employment_warning",
    "CreditBankEmploymentWarningType": ".credit_bank_employment_warning_type",
    "CreditBankIncome": ".credit_bank_income",
    "CreditBankIncomeAccount": ".credit_bank_income_account",
    "CreditBankIncomeAccountType": ".credit_bank_income_account_type",
    "CreditBankIncomeCategory": ".credit_bank_income_category",
    "CreditBankIncomeCause": ".credit_bank_income_cause",
    "CreditBankIncomeErrorType": ".credit_bank_income_error_type",
    "CreditBankIncomeGetRequestOptions": ".credit_bank_income_get_request_options",
    "CreditBankIncomeGetResponse": ".credit_bank_income_get_response",
    "CreditBankIncomeHistoricalSummary": ".credit_bank_income_historical_summary",
    "CreditBankIncomeItem": ".credit_bank_income_item",
    "CreditBankIncomePayFrequency": ".credit_bank_income_pay_frequency",
    "CreditBankIncomePdfGetResponse": ".credit_bank_income_pdf_get_response",
    "CreditBankIncomeRefreshRequestOptions": ".credit_bank_income_refresh_request_options",
    "CreditBankIncomeRefreshResponse": ".credit_bank_income_refresh_response",
    "CreditBankIncomeSource": ".credit_bank_income_source",
    "CreditBankIncomeSummary": ".credit_bank_income_summary",
    "CreditBankIncomeTransaction": ".credit_bank_income_transaction",
    "CreditBankIncomeWarning": ".credit_bank_income_warning",
    "CreditBankIncomeWarningCode": ".credit_bank_income_warning_code",
    "CreditBankIncomeWarningType": ".credit_bank_income_warning_type",
    "CreditCardLiability": ".credit_card_liability",
    "CreditCategory": ".credit_category",
    "CreditDocumentMetadata": ".credit_document_metadata",
    "CreditDocumentType": ".credit_document_type",
    "CreditEmployerVerification": ".credit_employer_verification",
    "CreditEmploymentEmployeeType": ".credit_employment_employee_type",
    "CreditEmploymentGetResponse": ".credit_employment_get_response",
    "CreditEmploymentItem": ".credit_employment_item",
    "CreditEmploymentVerification": ".credit_employment_verification",
    "CreditEmploymentVerificationStatus": ".credit_employment_verification_status",
    "CreditFilter": ".credit_filter",
    "CreditFreddieMacAssetDetailVoe25": ".credit_freddie_mac_asset_detail_voe25",
    "CreditFreddieMacAssetTransactionDetailVoe25": ".credit_freddie_mac_asset_transaction_detail_voe25",
    "CreditFreddieMacAssetTransactionVoa24": ".credit_freddie_mac_asset_transaction_voa24",
    "CreditFreddieMacAssetTransactionVoe25": ".credit_freddie_mac_asset_transaction_voe25",
    "CreditFreddieMacAssetTransactionsVoa24": ".credit_freddie_mac_asset_transactions_voa24",
    "CreditFreddieMacAssetTransactionsVoe25": ".credit_freddie_mac_asset_transactions_voe25",
    "CreditFreddieMacAssetVoa24": ".credit_freddie_mac_asset_voa24",
    "CreditFreddieMacAssetVoe25": ".credit_freddie_mac_asset_voe25",
    "CreditFreddieMacAssetsVoa24": ".credit_freddie_mac_assets_voa24",
    "CreditFreddieMacAssetsVoe25": ".credit_freddie_mac_assets_voe25",
    "CreditFreddieMacIndividualNameVoa24": ".credit_freddie_mac_individual_name_voa24",
    "CreditFreddieMacLoanIdentifiersVoa24": ".credit_freddie_mac_loan_identifiers_voa24",
    "CreditFreddieMacLoanVoa24": ".credit_freddie_mac_loan_voa24",
    "CreditFreddieMacLoansVoa24": ".credit_freddie_mac_loans_voa24",
    "CreditFreddieMacPartiesVoa24": ".credit_freddie_mac_parties_voa24",
    "CreditFreddieMacPartyIndividualVoa24": ".credit_freddie_mac_party_individual_voa24",
    "CreditFreddieMacPartyVoa24": ".credit_freddie_mac_party_voa24",
    "CreditFreddieMacReportingInformationVoa24": ".credit_freddie_mac_reporting_information_voa24",
    "CreditFreddieMacReportsGetResponse": ".credit_freddie_mac_reports_get_response",
    "CreditFreddieMacServiceVoa24": ".credit_freddie_mac_service_voa24",
    "CreditFreddieMacServiceVoe25": ".credit_freddie_mac_service_voe25",
    "CreditFreddieMacServicesVoa24": ".credit_freddie_mac_services_voa24",
    "CreditFreddieMacServicesVoe25": ".credit_freddie_mac_services_voe25",
    "CreditFreddieMacVerificationOfAssetResponseVoa24": ".credit_freddie_mac_verification_of_asset_response_voa24",
    "CreditFreddieMacVerificationOfAssetResponseVoe25": ".credit_freddie_mac_verification_of_asset_response_voe25",
    "CreditFreddieMacVerificationOfAssetVoa24": ".credit_freddie_mac_verification_of_asset_voa24",
    "CreditFreddieMacVerificationOfAssetVoe25": ".credit_freddie_mac_verification_of_asset_voe25",
    "CreditFreddieMacVerificationOfAssetsDealVoa24": ".credit_freddie_mac_verification_of_assets_deal_voa24",
    "CreditFreddieMacVerificationOfAssetsVoa24": ".credit_freddie_mac_verification_of_assets_voa24",
    "CreditFreddieVerificationOfEmploymentDealVoe25": ".credit_freddie_verification_of_employment_deal_voe25",
    "CreditFreddieVerificationOfEmploymentVoe25": ".credit_freddie_verification_of_employment_voe25",
    "CreditIsoCurrencyCode": ".credit_iso_currency_code",
    "CreditPayStub": ".credit_pay_stub",
    "CreditPayStubAddress": ".credit_pay_stub_address",
    "CreditPayStubDeductions": ".credit_pay_stub_deductions",
    "CreditPayStubEarnings": ".credit_pay_stub_earnings",
    "CreditPayStubEmployee": ".credit_pay_stub_employee",
    "CreditPayStubEmployer": ".credit_pay_stub_employer",
    "CreditPayStubNetPay": ".credit_pay_stub_net_pay",
    "CreditPayStubPayBasisType": ".credit_pay_stub_pay_basis_type",
    "CreditPayrollIncomeGetResponse": ".credit_payroll_income_get_response",
    "CreditPayrollIncomePrecheckResponse": ".credit_payroll_income_precheck_response",
    "CreditPayrollIncomeRefreshRequestOptions": ".credit_payroll_income_refresh_request_options",
    "CreditPayrollIncomeRefreshResponse": ".credit_payroll_income_refresh_response",
    "CreditPayrollIncomeRefreshStatus": ".credit_payroll_income_refresh_status",
    "CreditPayrollIncomeRiskSignalsGetRequest": ".credit_payroll_income_risk_signals_get_request",
    "CreditPayrollIncomeRiskSignalsGetResponse": ".credit_payroll_income_risk_signals_get_response",
    "CreditPlatformIds": ".credit_platform_ids",
    "CreditRelayCreateResponse": ".credit_relay_create_response",
    "CreditRelayRefreshResponse": ".credit_relay_refresh_response",
    "CreditRelayRemoveResponse": ".credit_relay_remove_response",
    "CreditSession": ".credit_session",
    "CreditSessionBankEmploymentResult": ".credit_session_bank_employment_result",
    "CreditSessionBankEmploymentStatus": ".credit_session_bank_employment_status",
    "CreditSessionBankIncomeResult": ".credit_session_bank_income_result",
    "CreditSessionBankIncomeStatus": ".credit_session_bank_income_status",
    "CreditSessionDocumentIncomeResult": ".credit_session_document_income_result",
    "CreditSessionError": ".credit_session_error",
    "CreditSessionItemAddResult": ".credit_session_item_add_result",
    "CreditSessionPayrollIncomeResult": ".credit_session_payroll_income_result",
    "CreditSessionResults": ".credit_session_results",
    "CreditSessionsGetResponse": ".credit_sessions_get_response",
    "CreditUnofficialCurrencyCode": ".credit_unofficial_currency_code",
    "CreditW2": ".credit_w2",
    "Cursor": ".cursor",
    "CustomerInitiatedReturnRisk": ".customer_initiated_return_risk",
    "CustomerInitiatedRiskTier": ".customer_initiated_risk_tier",
    "DashboardUser": ".dashboard_user",
    "DashboardUserGetResponse": ".dashboard_user_get_response",
    "DashboardUserId": ".dashboard_user_id",
    "DashboardUserIdNullable": ".dashboard_user_id_nullable",
    "DashboardUserListResponse": ".dashboard_user_list_response",
    "DashboardUserStatus": ".dashboard_user_status",
    "DateRange": ".date_range",
    "Deductions": ".deductions",
    "DeductionsBreakdown": ".deductions_breakdown",
    "DeductionsTotal": ".deductions_total",
    "DefaultUpdateWebhook": ".default_update_webhook",
    "DepositSwitchAddressData": ".deposit_switch_address_data",
    "DepositSwitchAltCreateResponse": ".deposit_switch_alt_create_response",
    "DepositSwitchCreateRequestOptions": ".deposit_switch_create_request_options",
    "DepositSwitchCreateResponse": ".deposit_switch_create_response",
    "DepositSwitchGetResponse": ".deposit_switch_get_response",
    "DepositSwitchGetResponseState": ".deposit_switch_get_response_state",
    "DepositSwitchGetResponseSwitchMethod": ".deposit_switch_get_response_switch_method",
    "DepositSwitchStateUpdateWebhook": ".deposit_switch_state_update_webhook",
    "DepositSwitchTargetAccount": ".deposit_switch_target_account",
    "DepositSwitchTargetAccountAccountSubtype": ".deposit_switch_target_account_account_subtype",
    "DepositSwitchTargetUser": ".deposit_switch_target_user",
    "DepositSwitchTokenCreateResponse": ".deposit_switch_token_create_response",
    "DepositoryAccount": ".depository_account",
    "DepositoryAccountSubtype": ".depository_account_subtype",
    "DepositoryAccountSubtypes": ".depository_account_subtypes",
    "DepositoryFilter": ".depository_filter",
    "DetailedOriginator": ".detailed_originator",
    "DistributionBreakdown": ".distribution_breakdown",
    "DocType": ".doc_type",
    "DocumentAnalysis": ".document_analysis",
    "DocumentAuthenticityMatchCode": ".document_authenticity_match_code",
    "DocumentDateOfBirthMatchCode": ".document_date_of_birth_match_code",
    "DocumentImageBack": ".document_image_back",
    "DocumentImageCroppedBack": ".document_image_cropped_back",
    "DocumentImageCroppedFront": ".document_image_cropped_front",
    "DocumentImageFace": ".document_image_face",
    "DocumentImageFront": ".document_image_front",
    "DocumentMetadata": ".document_metadata",
    "DocumentNameMatchCode": ".document_name_match_code",
    "DocumentRiskSignal": ".document_risk_signal",
    "DocumentRiskSignalInstitutionMetadata": ".document_risk_signal_institution_metadata",
    "DocumentRiskSignalsObject": ".document_risk_signals_object",
    "DocumentRiskSummary": ".document_risk_summary",
    "DocumentStatus": ".document_status",
    "DocumentaryVerification": ".documentary_verification",
    "DocumentaryVerificationDocument": ".documentary_verification_document",
    "Earnings": ".earnings",
    "EarningsBreakdown": ".earnings_breakdown",
    "EarningsBreakdownCanonicalDescription": ".earnings_breakdown_canonical_description",
    "EarningsTotal": ".earnings_total",
    "Email": ".email",
    "EmailAddress": ".email_address",
    "EmailAddressMatchScore": ".email_address_match_score",
    "EmailAddressNullable": ".email_address_nullable",
    "EmailType": ".email_type",
    "Employee": ".employee",
    "EmployeeIncomeSummaryFieldString": ".employee_income_summary_field_string",
    "Employer": ".employer",
    "EmployerIncomeSummaryFieldString": ".employer_income_summary_field_string",
    "EmployerVerification": ".employer_verification",
    "EmployersSearchResponse": ".employers_search_response",
    "EmploymentDetails": ".employment_details",
    "EmploymentSourceType": ".employment_source_type",
    "EmploymentVerification": ".employment_verification",
    "EmploymentVerificationGetResponse": ".employment_verification_get_response",
    "EmploymentVerificationStatus": ".employment_verification_status",
    "Enhancements": ".enhancements",
    "EnrichTransactionDirection": ".enrich_transaction_direction",
    "Enrichments": ".enrichments",
    "EntityDocument": ".entity_document",
    "EntityDocumentType": ".entity_document_type",
    "EntityScreeningHitAnalysis": ".entity_screening_hit_analysis",
    "EntityScreeningHitData": ".entity_screening_hit_data",
    "EntityScreeningHitDocumentsItems": ".entity_screening_hit_documents_items",
    "EntityScreeningHitEmails": ".entity_screening_hit_emails",
    "EntityScreeningHitEmailsItems": ".entity_screening_hit_emails_items",
    "EntityScreeningHitNames": ".entity_screening_hit_names",
    "EntityScreeningHitNamesItems": ".entity_screening_hit_names_items",
    "EntityScreeningHitPhoneNumbers": ".entity_screening_hit_phone_numbers",
    "EntityScreeningHitUrls": ".entity_screening_hit_urls",
    "EntityScreeningHitUrlsItems": ".entity_screening_hit_urls_items",
    "EntityScreeningHitsPhoneNumberItems": ".entity_screening_hits_phone_number_items",
    "EntityScreeningStatusUpdatedWebhook": ".entity_screening_status_updated_webhook",
    "EntityWatchlistCode": ".entity_watchlist_code",
    "EntityWatchlistProgram": ".entity_watchlist_program",
    "EntityWatchlistProgramId": ".entity_watchlist_program_id",
    "EntityWatchlistScreening": ".entity_watchlist_screening",
    "EntityWatchlistScreeningHit": ".entity_watchlist_screening_hit",
    "EntityWatchlistScreeningHitId": ".entity_watchlist_screening_hit_id",
    "EntityWatchlistScreeningId": ".entity_watchlist_screening_id",
    "EntityWatchlistScreeningName": ".entity_watchlist_screening_name",
    "EntityWatchlistScreeningProgramName": ".entity_watchlist_screening_program_name",
    "EntityWatchlistScreeningReview": ".entity_watchlist_screening_review",
    "EntityWatchlistScreeningReviewId": ".entity_watchlist_screening_review_id",
    "EntityWatchlistScreeningSearchTerms": ".entity_watchlist_screening_search_terms",
    "EntityWatchlistSearchTerms": ".entity_watchlist_search_terms",
    "ExpirationDate": ".expiration_date",
    "ExternalPaymentInitiationConsentOptions": ".external_payment_initiation_consent_options",
    "ExternalPaymentOptions": ".external_payment_options",
    "ExternalPaymentRefundDetails": ".external_payment_refund_details",
    "ExternalPaymentScheduleBase": ".external_payment_schedule_base",
    "ExternalPaymentScheduleGet": ".external_payment_schedule_get",
    "ExternalPaymentScheduleRequest": ".external_payment_schedule_request",
    "FallbackAuthMicrodepositAutoVerifiedWebhook": ".fallback_auth_microdeposit_auto_verified_webhook",
    "FallbackAuthMicrodepositVerificationExpiredWebhook": ".fallback_auth_microdeposit_verification_expired_webhook",
    "FamilyNameField": ".family_name_field",
    "FdxContentTypes": ".fdx_content_types",
    "FdxFiAttribute": ".fdx_fi_attribute",
    "FdxHateoasLink": ".fdx_hateoas_link",
    "FdxHateoasLinkAction": ".fdx_hateoas_link_action",
    "FdxNotificationCategory": ".fdx_notification_category",
    "FdxNotificationPayload": ".fdx_notification_payload",
    "FdxNotificationPayloadIdType": ".fdx_notification_payload_id_type",
    "FdxNotificationPriority": ".fdx_notification_priority",
    "FdxNotificationSeverity": ".fdx_notification_severity",
    "FdxNotificationType": ".fdx_notification_type",
    "FdxParty": ".fdx_party",
    "FdxPartyRegistry": ".fdx_party_registry",
    "FdxPartyType": ".fdx_party_type",
    "FdxTimestamp": ".fdx_timestamp",
    "Form1099Type": ".form1099type",
    "GenericCountryCode": ".generic_country_code",
    "GenericCountryCodeNullable": ".generic_country_code_nullable",
    "GenericScreeningHitLocationItems": ".generic_screening_hit_location_items",
    "GivenNameField": ".given_name_field",
    "HealthIncident": ".health_incident",
    "HistoricalBalance": ".historical_balance",
    "HistoricalUpdateWebhook": ".historical_update_webhook",
    "Holding": ".holding",
    "HoldingsDefaultUpdateWebhook": ".holdings_default_update_webhook",
    "HoldingsOverride": ".holdings_override",
    "IdNumberType": ".id_number_type",
    "IdNumberValue": ".id_number_value",
    "IdempotencyFlag": ".idempotency_flag",
    "IdentityDefaultUpdateWebhook": ".identity_default_update_webhook",
    "IdentityGetRequestOptions": ".identity_get_request_options",
    "IdentityGetResponse": ".identity_get_response",
    "IdentityMatchIdentityVerificationId": ".identity_match_identity_verification_id",
    "IdentityMatchRequestOptions": ".identity_match_request_options",
    "IdentityMatchResponse": ".identity_match_response",
    "IdentityMatchUser": ".identity_match_user",
    "IdentityUpdateTypes": ".identity_update_types",
    "IdentityVerification": ".identity_verification",
    "IdentityVerificationConsent": ".identity_verification_consent",
    "IdentityVerificationCreateResponse": ".identity_verification_create_response",
    "IdentityVerificationGetResponse": ".identity_verification_get_response",
    "IdentityVerificationId": ".identity_verification_id",
    "IdentityVerificationListResponse": ".identity_verification_list_response",
    "IdentityVerificationRequestUser": ".identity_verification_request_user",
    "IdentityVerificationRequestUserName": ".identity_verification_request_user_name",
    "IdentityVerificationResponseUserName": ".identity_verification_response_user_name",
    "IdentityVerificationRetriedWebhook": ".identity_verification_retried_webhook",
    "IdentityVerificationRetryRequestStepsObject": ".identity_verification_retry_request_steps_object",
    "IdentityVerificationRetryResponse": ".identity_verification_retry_response",
    "IdentityVerificationStatus": ".identity_verification_status",
    "IdentityVerificationStatusUpdatedWebhook": ".identity_verification_status_updated_webhook",
    "IdentityVerificationStepStatus": ".identity_verification_step_status",
    "IdentityVerificationStepSummary": ".identity_verification_step_summary",
    "IdentityVerificationStepUpdatedWebhook": ".identity_verification_step_updated_webhook",
    "IdentityVerificationTemplateId": ".identity_verification_template_id",
    "IdentityVerificationTemplateReference": ".identity_verification_template_reference",
    "IdentityVerificationTemplateVersion": ".identity_verification_template_version",
    "IdentityVerificationUserAddress": ".identity_verification_user_address",
    "IdentityVerificationUserData": ".identity_verification_user_data",
    "IdentityVerificationUserPhoneNumber": ".identity_verification_user_phone_number",
    "ImageQuality": ".image_quality",
    "IncidentUpdate": ".incident_update",
    "IncidentUpdateStatus": ".incident_update_status",
    "IncomeBreakdown": ".income_breakdown",
    "IncomeBreakdownType": ".income_breakdown_type",
    "IncomeOverride": ".income_override",
    "IncomeSummary": ".income_summary",
    "IncomeSummaryFieldNumber": ".income_summary_field_number",
    "IncomeSummaryFieldString": ".income_summary_field_string",
    "IncomeVerificationCreateRequestOptions": ".income_verification_create_request_options",
    "IncomeVerificationCreateResponse": ".income_verification_create_response",
    "IncomeVerificationPayrollFlowType": ".income_verification_payroll_flow_type",
    "IncomeVerificationPaystubsGetResponse": ".income_verification_paystubs_get_response",
    "IncomeVerificationPrecheckConfidence": ".income_verification_precheck_confidence",
    "IncomeVerificationPrecheckEmployer": ".income_verification_precheck_employer",
    "IncomeVerificationPrecheckEmployerAddress": ".income_verification_precheck_employer_address",
    "IncomeVerificationPrecheckEmployerAddressData": ".income_verification_precheck_employer_address_data",
    "IncomeVerificationPrecheckMilitaryInfo": ".income_verification_precheck_military_info",
    "IncomeVerificationPrecheckPayrollInstitution": ".income_verification_precheck_payroll_institution",
    "IncomeVerificationPrecheckResponse": ".income_verification_precheck_response",
    "IncomeVerificationPrecheckUser": ".income_verification_precheck_user",
    "IncomeVerificationSourceType": ".income_verification_source_type",
    "IncomeVerificationStatusWebhook": ".income_verification_status_webhook",
    "IncomeVerificationTaxformsGetResponse": ".income_verification_taxforms_get_response",
    "IncomeVerificationWebhookStatus": ".income_verification_webhook_status",
    "IndividualName": ".individual_name",
    "IndividualScreeningHitNames": ".individual_screening_hit_names",
    "IndividualWatchlistCode": ".individual_watchlist_code",
    "IndividualWatchlistProgram": ".individual_watchlist_program",
    "IndividualWatchlistScreeningProgramName": ".individual_watchlist_screening_program_name",
    "InflowModel": ".inflow_model",
    "InitialUpdateWebhook": ".initial_update_webhook",
    "Institution": ".institution",
    "InstitutionStatus": ".institution_status",
    "InstitutionSupportedNetworks": ".institution_supported_networks",
    "InstitutionsGetByIdRequestOptions": ".institutions_get_by_id_request_options",
    "InstitutionsGetByIdResponse": ".institutions_get_by_id_response",
    "InstitutionsGetRequestOptions": ".institutions_get_request_options",
    "InstitutionsGetResponse": ".institutions_get_response",
    "InstitutionsSearchAccountFilter": ".institutions_search_account_filter",
    "InstitutionsSearchPaymentInitiationOptions": ".institutions_search_payment_initiation_options",
    "InstitutionsSearchRequestOptions": ".institutions_search_request_options",
    "InstitutionsSearchResponse": ".institutions_search_response",
    "InternalUid": ".internal_uid",
    "InvestmentAccountSubtype": ".investment_account_subtype",
    "InvestmentAccountSubtypeStandalone": ".investment_account_subtype_standalone",
    "InvestmentAccountSubtypes": ".investment_account_subtypes",
    "InvestmentFilter": ".investment_filter",
    "InvestmentHoldingsGetRequestOptions": ".investment_holdings_get_request_options",
    "InvestmentTransaction": ".investment_transaction",
    "InvestmentTransactionSubtype": ".investment_transaction_subtype",
    "InvestmentTransactionType": ".investment_transaction_type",
    "InvestmentsDefaultUpdateWebhook": ".investments_default_update_webhook",
    "InvestmentsHoldingsGetResponse": ".investments_holdings_get_response",
    "InvestmentsTransactionsGetRequestOptions": ".investments_transactions_get_request_options",
    "InvestmentsTransactionsGetResponse": ".investments_transactions_get_response",
    "InvestmentsTransactionsOverride": ".investments_transactions_override",
    "IpAddress": ".ip_address",
    "Iso8601Date": ".iso8601date",
    "Iso8601DateNullable": ".iso8601date_nullable",
    "IssuingCountry": ".issuing_country",
    "Item": ".item",
    "ItemAccessTokenInvalidateResponse": ".item_access_token_invalidate_response",
    "ItemActivityListResponse": ".item_activity_list_response",
    "ItemApplicationListResponse": ".item_application_list_response",
    "ItemApplicationListUserAuth": ".item_application_list_user_auth",
    "ItemApplicationScopesUpdateResponse": ".item_application_scopes_update_response",
    "ItemErrorWebhook": ".item_error_webhook",
    "ItemGetResponse": ".item_get_response",
    "ItemId": ".item_id",
    "ItemImportRequestOptions": ".item_import_request_options",
    "ItemImportRequestUserAuth": ".item_import_request_user_auth",
    "ItemImportResponse": ".item_import_response",
    "ItemLoginRepairedWebhook": ".item_login_repaired_webhook",
    "ItemProductReadyWebhook": ".item_product_ready_webhook",
    "ItemPublicTokenCreateResponse": ".item_public_token_create_response",
    "ItemPublicTokenExchangeResponse": ".item_public_token_exchange_response",
    "ItemRemoveResponse": ".item_remove_response",
    "ItemStatus": ".item_status",
    "ItemStatusInvestments": ".item_status_investments",
    "ItemStatusLastWebhook": ".item_status_last_webhook",
    "ItemStatusNullable": ".item_status_nullable",
    "ItemStatusTransactions": ".item_status_transactions",
    "ItemUpdateType": ".item_update_type",
    "ItemWebhookUpdateResponse": ".item_webhook_update_response",
    "JwkPublicKey": ".jwk_public_key",
    "JwtHeader": ".jwt_header",
    "KycCheckAddressSummary": ".kyc_check_address_summary",
    "KycCheckDateOfBirthSummary": ".kyc_check_date_of_birth_summary",
    "KycCheckDetails": ".kyc_check_details",
    "KycCheckIdNumberSummary": ".kyc_check_id_number_summary",
    "KycCheckNameSummary": ".kyc_check_name_summary",
    "KycCheckPhoneSummary": ".kyc_check_phone_summary",
    "LastDataAccessTimes": ".last_data_access_times",
    "LiabilitiesAccountIdsWithUpdatedLiabilities": ".liabilities_account_ids_with_updated_liabilities",
    "LiabilitiesDefaultUpdateWebhook": ".liabilities_default_update_webhook",
    "LiabilitiesGetRequestOptions": ".liabilities_get_request_options",
    "LiabilitiesGetResponse": ".liabilities_get_response",
    "LiabilitiesObject": ".liabilities_object",
    "LiabilityOverride": ".liability_override",
    "LinkCallbackMetadata": ".link_callback_metadata",
    "LinkDeliveryAccount": ".link_delivery_account",
    "LinkDeliveryCallbackWebhook": ".link_delivery_callback_webhook",
    "LinkDeliveryCommunicationMethod": ".link_delivery_communication_method",
    "LinkDeliveryCreateResponse": ".link_delivery_create_response",
    "LinkDeliveryDeliveryMethod": ".link_delivery_delivery_method",
    "LinkDeliveryGetResponse": ".link_delivery_get_response",
    "LinkDeliveryInstitution": ".link_delivery_institution",
    "LinkDeliveryMetadata": ".link_delivery_metadata",
    "LinkDeliveryOptions": ".link_delivery_options",
    "LinkDeliveryRecipient": ".link_delivery_recipient",
    "LinkDeliverySessionStatus": ".link_delivery_session_status",
    "LinkDeliveryVerificationStatus": ".link_delivery_verification_status",
    "LinkDeliveryWebhookCallbackType": ".link_delivery_webhook_callback_type",
    "LinkDeliveryWebhookCommunicationMethod": ".link_delivery_webhook_communication_method",
    "LinkDeliveryWebhookDeliveryStatus": ".link_delivery_webhook_delivery_status",
    "LinkEventName": ".link_event_name",
    "LinkOAuthCorrelationIdExchangeResponse": ".link_o_auth_correlation_id_exchange_response",
    "LinkTokenAccountFilters": ".link_token_account_filters",
    "LinkTokenCreateCreditFilter": ".link_token_create_credit_filter",
    "LinkTokenCreateDepositoryFilter": ".link_token_create_depository_filter",
    "LinkTokenCreateInstitutionData": ".link_token_create_institution_data",
    "LinkTokenCreateInvestmentFilter": ".link_token_create_investment_filter",
    "LinkTokenCreateLoanFilter": ".link_token_create_loan_filter",
    "LinkTokenCreateRequestAccountSubtypes": ".link_token_create_request_account_subtypes",
    "LinkTokenCreateRequestAuth": ".link_token_create_request_auth",
    "LinkTokenCreateRequestAuthFlowType": ".link_token_create_request_auth_flow_type",
    "LinkTokenCreateRequestDepositSwitch": ".link_token_create_request_deposit_switch",
    "LinkTokenCreateRequestEmployment": ".link_token_create_request_employment",
    "LinkTokenCreateRequestEmploymentBankIncome": ".link_token_create_request_employment_bank_income",
    "LinkTokenCreateRequestIdentityVerification": ".link_token_create_request_identity_verification",
    "LinkTokenCreateRequestIncomeVerification": ".link_token_create_request_income_verification",
    "LinkTokenCreateRequestIncomeVerificationBankIncome": ".link_token_create_request_income_verification_bank_income",
    "LinkTokenCreateRequestIncomeVerificationPayrollIncome": ".link_token_create_request_income_verification_payroll_income",
    "LinkTokenCreateRequestPaymentInitiation": ".link_token_create_request_payment_initiation",
    "LinkTokenCreateRequestTransfer": ".link_token_create_request_transfer",
    "LinkTokenCreateRequestUpdate": ".link_token_create_request_update",
    "LinkTokenCreateRequestUser": ".link_token_create_request_user",
    "LinkTokenCreateRequestUserName": ".link_token_create_request_user_name",
    "LinkTokenCreateRequestUserStatedIncomeSource": ".link_token_create_request_user_stated_income_source",
    "LinkTokenCreateResponse": ".link_token_create_response",
    "LinkTokenEuConfig": ".link_token_eu_config",
    "LinkTokenGetMetadataResponse": ".link_token_get_metadata_response",
    "LinkTokenGetResponse": ".link_token_get_response",
    "LinkTokenInvestments": ".link_token_investments",
    "LinkUserDeliveryStatusWebhook": ".link_user_delivery_status_webhook",
    "Loan": ".loan",
    "LoanAccount": ".loan_account",
    "LoanAccountSubtype": ".loan_account_subtype",
    "LoanAccountSubtypes": ".loan_account_subtypes",
    "LoanFilter": ".loan_filter",
    "LoanIdentifier": ".loan_identifier",
    "LoanIdentifierType": ".loan_identifier_type",
    "LoanIdentifiers": ".loan_identifiers",
    "Loans": ".loans",
    "Location": ".location",
    "MatchSummary": ".match_summary",
    "MatchSummaryCode": ".match_summary_code",
    "Meta": ".meta",
    "Mfa": ".mfa",
    "MinLastUpdatedDatetime": ".min_last_updated_datetime",
    "MortgageInterestRate": ".mortgage_interest_rate",
    "MortgageLiability": ".mortgage_liability",
    "MortgagePropertyAddress": ".mortgage_property_address",
    "MultiDocumentRiskSignal": ".multi_document_risk_signal",
    "NameMatchScore": ".name_match_score",
    "NetPay": ".net_pay",
    "NewAccountsAvailableWebhook": ".new_accounts_available_webhook",
    "Numbers": ".numbers",
    "NumbersAch": ".numbers_ach",
    "NumbersAchNullable": ".numbers_ach_nullable",
    "NumbersBacs": ".numbers_bacs",
    "NumbersBacsNullable": ".numbers_bacs_nullable",
    "NumbersEft": ".numbers_eft",
    "NumbersEftNullable": ".numbers_eft_nullable",
    "NumbersIban": ".numbers_iban",
    "NumbersIbanNullable": ".numbers_iban_nullable",
    "NumbersInternational": ".numbers_international",
    "NumbersInternationalIban": ".numbers_international_iban",
    "NumbersInternationalNullable": ".numbers_international_nullable",
    "Originator": ".originator",
    "OverrideAccountType": ".override_account_type",
    "OverrideAccounts": ".override_accounts",
    "Owner": ".owner",
    "OwnerOverride": ".owner_override",
    "OwnershipType": ".ownership_type",
    "Parties": ".parties",
    "PartnerCustomerCreateResponse": ".partner_customer_create_response",
    "PartnerCustomerEnableResponse": ".partner_customer_enable_response",
    "PartnerCustomerGetResponse": ".partner_customer_get_response",
    "PartnerCustomerOAuthInstitutionsGetResponse": ".partner_customer_o_auth_institutions_get_response",
    "PartnerCustomerRemoveResponse": ".partner_customer_remove_response",
    "PartnerEndCustomer": ".partner_end_customer",
    "PartnerEndCustomerAddress": ".partner_end_customer_address",
    "PartnerEndCustomerAssetsUnderManagement": ".partner_end_customer_assets_under_management",
    "PartnerEndCustomerBillingContact": ".partner_end_customer_billing_contact",
    "PartnerEndCustomerCustomerSupportInfo": ".partner_end_customer_customer_support_info",
    "PartnerEndCustomerFlowdownStatus": ".partner_end_customer_flowdown_status",
    "PartnerEndCustomerOAuthInstitution": ".partner_end_customer_o_auth_institution",
    "PartnerEndCustomerOAuthInstitutionApplicationStatus": ".partner_end_customer_o_auth_institution_application_status",
    "PartnerEndCustomerOAuthInstitutionEnvironments": ".partner_end_customer_o_auth_institution_environments",
    "PartnerEndCustomerOAuthStatusUpdatedValues": ".partner_end_customer_o_auth_status_updated_values",
    "PartnerEndCustomerOAuthStatusUpdatedWebhook": ".partner_end_customer_o_auth_status_updated_webhook",
    "PartnerEndCustomerQuestionnaireStatus": ".partner_end_customer_questionnaire_status",
    "PartnerEndCustomerSecrets": ".partner_end_customer_secrets",
    "PartnerEndCustomerStatus": ".partner_end_customer_status",
    "PartnerEndCustomerTechnicalContact": ".partner_end_customer_technical_contact",
    "PartnerEndCustomerWithSecrets": ".partner_end_customer_with_secrets",
    "Party": ".party",
    "PartyIndividual": ".party_individual",
    "PartyRoleType": ".party_role_type",
    "Pay": ".pay",
    "PayFrequency": ".pay_frequency",
    "PayFrequencyValue": ".pay_frequency_value",
    "PayPeriodDetails": ".pay_period_details",
    "PayPeriodDetailsPayFrequency": ".pay_period_details_pay_frequency",
    "PayStubDeductionsBreakdown": ".pay_stub_deductions_breakdown",
    "PayStubDeductionsTotal": ".pay_stub_deductions_total",
    "PayStubDistributionBreakdown": ".pay_stub_distribution_breakdown",
    "PayStubEarningsBreakdown": ".pay_stub_earnings_breakdown",
    "PayStubEarningsBreakdownCanonicalDescription": ".pay_stub_earnings_breakdown_canonical_description",
    "PayStubEarningsTotal": ".pay_stub_earnings_total",
    "PayStubPayPeriodDetails": ".pay_stub_pay_period_details",
    "PayStubTaxpayerId": ".pay_stub_taxpayer_id",
    "PaymentAmount": ".payment_amount",
    "PaymentAmountCurrency": ".payment_amount_currency",
    "PaymentAmountNullable": ".payment_amount_nullable",
    "PaymentAmountRefunded": ".payment_amount_refunded",
    "PaymentAmountToRefund": ".payment_amount_to_refund",
    "PaymentChannel": ".payment_channel",
    "PaymentConsentMaxPaymentAmount": ".payment_consent_max_payment_amount",
    "PaymentConsentPeriodicAlignment": ".payment_consent_periodic_alignment",
    "PaymentConsentPeriodicAmount": ".payment_consent_periodic_amount",
    "PaymentConsentPeriodicAmountAmount": ".payment_consent_periodic_amount_amount",
    "PaymentConsentPeriodicInterval": ".payment_consent_periodic_interval",
    "PaymentConsentValidDateTime": ".payment_consent_valid_date_time",
    "PaymentInitiationAddress": ".payment_initiation_address",
    "PaymentInitiationConsent": ".payment_initiation_consent",
    "PaymentInitiationConsentConstraints": ".payment_initiation_consent_constraints",
    "PaymentInitiationConsentCreateResponse": ".payment_initiation_consent_create_response",
    "PaymentInitiationConsentGetResponse": ".payment_initiation_consent_get_response",
    "PaymentInitiationConsentPaymentExecuteResponse": ".payment_initiation_consent_payment_execute_response",
    "PaymentInitiationConsentRevokeResponse": ".payment_initiation_consent_revoke_response",
    "PaymentInitiationConsentScope": ".payment_initiation_consent_scope",
    "PaymentInitiationConsentStatus": ".payment_initiation_consent_status",
    "PaymentInitiationMaximumPaymentAmount": ".payment_initiation_maximum_payment_amount",
    "PaymentInitiationMetadata": ".payment_initiation_metadata",
    "PaymentInitiationOptionalRestrictionBacs": ".payment_initiation_optional_restriction_bacs",
    "PaymentInitiationPayment": ".payment_initiation_payment",
    "PaymentInitiationPaymentCreateResponse": ".payment_initiation_payment_create_response",
    "PaymentInitiationPaymentCreateStatus": ".payment_initiation_payment_create_status",
    "PaymentInitiationPaymentGetResponse": ".payment_initiation_payment_get_response",
    "PaymentInitiationPaymentListResponse": ".payment_initiation_payment_list_response",
    "PaymentInitiationPaymentReverseResponse": ".payment_initiation_payment_reverse_response",
    "PaymentInitiationPaymentStatus": ".payment_initiation_payment_status",
    "PaymentInitiationPaymentTokenCreateResponse": ".payment_initiation_payment_token_create_response",
    "PaymentInitiationRecipient": ".payment_initiation_recipient",
    "PaymentInitiationRecipientCreateResponse": ".payment_initiation_recipient_create_response",
    "PaymentInitiationRecipientGetResponse": ".payment_initiation_recipient_get_response",
    "PaymentInitiationRecipientListResponse": ".payment_initiation_recipient_list_response",
    "PaymentInitiationStandingOrderMetadata": ".payment_initiation_standing_order_metadata",
    "PaymentMeta": ".payment_meta",
    "PaymentProfileCreateResponse": ".payment_profile_create_response",
    "PaymentProfileGetResponse": ".payment_profile_get_response",
    "PaymentProfileRemoveResponse": ".payment_profile_remove_response",
    "PaymentProfileStatus": ".payment_profile_status",
    "PaymentProfileToken": ".payment_profile_token",
    "PaymentScheduleInterval": ".payment_schedule_interval",
    "PaymentScheme": ".payment_scheme",
    "PaymentStatusUpdateWebhook": ".payment_status_update_webhook",
    "PayrollIncomeAccountData": ".payroll_income_account_data",
    "PayrollIncomeObject": ".payroll_income_object",
    "PayrollIncomeRateOfPay": ".payroll_income_rate_of_pay",
    "PayrollItem": ".payroll_item",
    "PayrollItemStatus": ".payroll_item_status",
    "PayrollRiskSignalsItem": ".payroll_risk_signals_item",
    "Paystub": ".paystub",
    "PaystubAddress": ".paystub_address",
    "PaystubDeduction": ".paystub_deduction",
    "PaystubDetails": ".paystub_details",
    "PaystubEmployer": ".paystub_employer",
    "PaystubOverride": ".paystub_override",
    "PaystubOverrideEmployee": ".paystub_override_employee",
    "PaystubOverrideEmployeeAddress": ".paystub_override_employee_address",
    "PaystubOverrideEmployer": ".paystub_override_employer",
    "PaystubPayFrequency": ".paystub_pay_frequency",
    "PaystubYtdDetails": ".paystub_ytd_details",
    "PendingExpirationWebhook": ".pending_expiration_webhook",
    "PersonalFinanceCategory": ".personal_finance_category",
    "PhoneNumber": ".phone_number",
    "PhoneNumberMatchScore": ".phone_number_match_score",
    "PhoneNumberType": ".phone_number_type",
    "PhoneType": ".phone_type",
    "PhysicalDocumentCategory": ".physical_document_category",
    "PhysicalDocumentExtractedData": ".physical_document_extracted_data",
    "PhysicalDocumentExtractedDataAnalysis": ".physical_document_extracted_data_analysis",
    "PhysicalDocumentIdNumber": ".physical_document_id_number",
    "PhysicalDocumentImages": ".physical_document_images",
    "PlaidError": ".plaid_error",
    "PlaidErrorType": ".plaid_error_type",
    "PlatformIds": ".platform_ids",
    "PoBoxStatus": ".po_box_status",
    "PostalCode": ".postal_code",
    "PostalCodeNullable": ".postal_code_nullable",
    "PreviousIdentityVerificationAttemptId": ".previous_identity_verification_attempt_id",
    "ProcessorAuthGetResponse": ".processor_auth_get_response",
    "ProcessorBalanceGetRequestOptions": ".processor_balance_get_request_options",
    "ProcessorBalanceGetResponse": ".processor_balance_get_response",
    "ProcessorBankTransferCreateResponse": ".processor_bank_transfer_create_response",
    "ProcessorIdentityGetResponse": ".processor_identity_get_response",
    "ProcessorNumber": ".processor_number",
    "ProcessorSignalDecisionReportResponse": ".processor_signal_decision_report_response",
    "ProcessorSignalEvaluateResponse": ".processor_signal_evaluate_response",
    "ProcessorSignalReturnReportResponse": ".processor_signal_return_report_response",
    "ProcessorStripeBankAccountTokenCreateResponse": ".processor_stripe_bank_account_token_create_response",
    "ProcessorToken": ".processor_token",
    "ProcessorTokenCreateResponse": ".processor_token_create_response",
    "ProductAccess": ".product_access",
    "ProductStatus": ".product_status",
    "ProductStatusBreakdown": ".product_status_breakdown",
    "ProductStatusBreakdownRefreshInterval": ".product_status_breakdown_refresh_interval",
    "ProductStatusStatus": ".product_status_status",
    "Products": ".products",
    "ProgramArchived": ".program_archived",
    "ProgramNameSensitivity": ".program_name_sensitivity",
    "ProjectedIncomeSummaryFieldNumber": ".projected_income_summary_field_number",
    "ProxyType": ".proxy_type",
    "PslfStatus": ".pslf_status",
    "RecaptchaRequiredError": ".recaptcha_required_error",
    "RecipientBacs": ".recipient_bacs",
    "RecipientBacsNullable": ".recipient_bacs_nullable",
    "Recurrence": ".recurrence",
    "RecurringCancelledWebhook": ".recurring_cancelled_webhook",
    "RecurringNewTransferWebhook": ".recurring_new_transfer_webhook",
    "RecurringTransactionFrequency": ".recurring_transaction_frequency",
    "RecurringTransactionsUpdateWebhook": ".recurring_transactions_update_webhook",
    "RecurringTransfer": ".recurring_transfer",
    "RecurringTransferId": ".recurring_transfer_id",
    "RecurringTransferNullable": ".recurring_transfer_nullable",
    "RecurringTransferSkippedWebhook": ".recurring_transfer_skipped_webhook",
    "Region": ".region",
    "RegionNullable": ".region_nullable",
    "RemovedTransaction": ".removed_transaction",
    "ReportType": ".report_type",
    "ReportingInformation": ".reporting_information",
    "RequestId": ".request_id",
    "ReviewComment": ".review_comment",
    "RiskCheckBehavior": ".risk_check_behavior",
    "RiskCheckBehaviorBotDetectedLabel": ".risk_check_behavior_bot_detected_label",
    "RiskCheckBehaviorFraudRingDetectedLabel": ".risk_check_behavior_fraud_ring_detected_label",
    "RiskCheckBehaviorUserInteractionsLabel": ".risk_check_behavior_user_interactions_label",
    "RiskCheckDetails": ".risk_check_details",
    "RiskCheckDevice": ".risk_check_device",
    "RiskCheckEmail": ".risk_check_email",
    "RiskCheckEmailDomainIsCustom": ".risk_check_email_domain_is_custom",
    "RiskCheckEmailDomainIsDisposable": ".risk_check_email_domain_is_disposable",
    "RiskCheckEmailDomainIsFreeProvider": ".risk_check_email_domain_is_free_provider",
    "RiskCheckEmailIsDeliverableStatus": ".risk_check_email_is_deliverable_status",
    "RiskCheckEmailTopLevelDomainIsSuspicious": ".risk_check_email_top_level_domain_is_suspicious",
    "RiskCheckLinkedService": ".risk_check_linked_service",
    "RiskCheckPhone": ".risk_check_phone",
    "RiskSignalDocumentReference": ".risk_signal_document_reference",
    "Role": ".role",
    "RoleDetail": ".role_detail",
    "Roles": ".roles",
    "SandboxBankTransferFireWebhookResponse": ".sandbox_bank_transfer_fire_webhook_response",
    "SandboxBankTransferSimulateResponse": ".sandbox_bank_transfer_simulate_response",
    "SandboxIncomeFireWebhookResponse": ".sandbox_income_fire_webhook_response",
    "SandboxItemFireWebhookResponse": ".sandbox_item_fire_webhook_response",
    "SandboxItemResetLoginResponse": ".sandbox_item_reset_login_response",
    "SandboxItemSetVerificationStatusResponse": ".sandbox_item_set_verification_status_response",
    "SandboxOauthSelectAccountsResponse": ".sandbox_oauth_select_accounts_response",
    "SandboxOverridePassword": ".sandbox_override_password",
    "SandboxOverrideUsername": ".sandbox_override_username",
    "SandboxPaymentProfileResetLoginResponse": ".sandbox_payment_profile_reset_login_response",
    "SandboxProcessorTokenCreateRequestOptions": ".sandbox_processor_token_create_request_options",
    "SandboxProcessorTokenCreateResponse": ".sandbox_processor_token_create_response",
    "SandboxPublicTokenCreateRequestIncomeVerificationBankIncome": ".sandbox_public_token_create_request_income_verification_bank_income",
    "SandboxPublicTokenCreateRequestOptions": ".sandbox_public_token_create_request_options",
    "SandboxPublicTokenCreateRequestOptionsIncomeVerification": ".sandbox_public_token_create_request_options_income_verification",
    "SandboxPublicTokenCreateRequestOptionsTransactions": ".sandbox_public_token_create_request_options_transactions",
    "SandboxPublicTokenCreateResponse": ".sandbox_public_token_create_response",
    "SandboxTransferFireWebhookResponse": ".sandbox_transfer_fire_webhook_response",
    "SandboxTransferRepaymentSimulateResponse": ".sandbox_transfer_repayment_simulate_response",
    "SandboxTransferSimulateResponse": ".sandbox_transfer_simulate_response",
    "SandboxTransferSweepSimulateResponse": ".sandbox_transfer_sweep_simulate_response",
    "SandboxTransferTestClockAdvanceResponse": ".sandbox_transfer_test_clock_advance_response",
    "SandboxTransferTestClockCreateResponse": ".sandbox_transfer_test_clock_create_response",
    "SandboxTransferTestClockGetResponse": ".sandbox_transfer_test_clock_get_response",
    "SandboxTransferTestClockListResponse": ".sandbox_transfer_test_clock_list_response",
    "Scopes": ".scopes",
    "ScopesContext": ".scopes_context",
    "ScopesNullable": ".scopes_nullable",
    "ScopesState": ".scopes_state",
    "ScreeningHitAnalysis": ".screening_hit_analysis",
    "ScreeningHitData": ".screening_hit_data",
    "ScreeningHitDateOfBirthItem": ".screening_hit_date_of_birth_item",
    "ScreeningHitDocumentsItems": ".screening_hit_documents_items",
    "ScreeningHitNamesItems": ".screening_hit_names_items",
    "ScreeningStatusUpdatedWebhook": ".screening_status_updated_webhook",
    "Security": ".security",
    "SecurityOverride": ".security_override",
    "SenderBacsNullable": ".sender_bacs_nullable",
    "Service": ".service",
    "ServiceProductFulfillment": ".service_product_fulfillment",
    "ServiceProductFulfillmentDetail": ".service_product_fulfillment_detail",
    "ServiceProductFulfillmentIdentifier": ".service_product_fulfillment_identifier",
    "ServicerAddressData": ".servicer_address_data",
    "Services": ".services",
    "ShareableUrl": ".shareable_url",
    "SignalAddressData": ".signal_address_data",
    "SignalDecisionOutcome": ".signal_decision_outcome",
    "SignalDecisionReportResponse": ".signal_decision_report_response",
    "SignalDevice": ".signal_device",
    "SignalEvaluateCoreAttributes": ".signal_evaluate_core_attributes",
    "SignalEvaluateResponse": ".signal_evaluate_response",
    "SignalPaymentMethod": ".signal_payment_method",
    "SignalPersonName": ".signal_person_name",
    "SignalPrepareResponse": ".signal_prepare_response",
    "SignalReturnReportResponse": ".signal_return_report_response",
    "SignalScore": ".signal_score",
    "SignalScores": ".signal_scores",
    "SignalUser": ".signal_user",
    "SignalWarning": ".signal_warning",
    "SimulatedTransferSweep": ".simulated_transfer_sweep",
    "SingleDocumentRiskSignal": ".single_document_risk_signal",
    "Source": ".source",
    "SourceUid": ".source_uid",
    "StandaloneAccountType": ".standalone_account_type",
    "StandaloneCurrencyCodeList": ".standalone_currency_code_list",
    "StandaloneInvestmentTransactionBuyType": ".standalone_investment_transaction_buy_type",
    "StandaloneInvestmentTransactionCashType": ".standalone_investment_transaction_cash_type",
    "StandaloneInvestmentTransactionFeeType": ".standalone_investment_transaction_fee_type",
    "StandaloneInvestmentTransactionSellType": ".standalone_investment_transaction_sell_type",
    "StandaloneInvestmentTransactionTransferType": ".standalone_investment_transaction_transfer_type",
    "StandaloneInvestmentTransactionType": ".standalone_investment_transaction_type",
    "Status": ".status",
    "Statuses": ".statuses",
    "Strategy": ".strategy",
    "Street": ".street",
    "Street2": ".street2",
    "StreetNullable": ".street_nullable",
    "StudentLoan": ".student_loan",
    "StudentLoanRepaymentModel": ".student_loan_repayment_model",
    "StudentLoanStatus": ".student_loan_status",
    "StudentLoanStatusType": ".student_loan_status_type",
    "StudentRepaymentPlan": ".student_repayment_plan",
    "StudentRepaymentPlanType": ".student_repayment_plan_type",
    "SyncUpdatesAvailableWebhook": ".sync_updates_available_webhook",
    "Taxform": ".taxform",
    "TaxpayerId": ".taxpayer_id",
    "TaxpayerIdentifier": ".taxpayer_identifier",
    "TaxpayerIdentifierType": ".taxpayer_identifier_type",
    "TaxpayerIdentifiers": ".taxpayer_identifiers",
    "Timestamp": ".timestamp",
    "TimestampNullable": ".timestamp_nullable",
    "Total": ".total",
    "TotalCanonicalDescription": ".total_canonical_description",
    "Transaction": ".transaction",
    "TransactionBase": ".transaction_base",
    "TransactionBaseTransactionType": ".transaction_base_transaction_type",
    "TransactionCode": ".transaction_code",
    "TransactionCounterparty": ".transaction_counterparty",
    "TransactionData": ".transaction_data",
    "TransactionOverride": ".transaction_override",
    "TransactionPaymentChannel": ".transaction_payment_channel",
    "TransactionStream": ".transaction_stream",
    "TransactionStreamAmount": ".transaction_stream_amount",
    "TransactionStreamStatus": ".transaction_stream_status",
    "TransactionsCategoryRule": ".transactions_category_rule",
    "TransactionsEnhanceGetResponse": ".transactions_enhance_get_response",
    "TransactionsEnrichGetResponse": ".transactions_enrich_get_response",
    "TransactionsEnrichRequestOptions": ".transactions_enrich_request_options",
    "TransactionsGetRequestOptions": ".transactions_get_request_options",
    "TransactionsGetResponse": ".transactions_get_response",
    "TransactionsRecurringGetRequestOptions": ".transactions_recurring_get_request_options",
    "TransactionsRecurringGetResponse": ".transactions_recurring_get_response",
    "TransactionsRefreshResponse": ".transactions_refresh_response",
    "TransactionsRemovedWebhook": ".transactions_removed_webhook",
    "TransactionsRuleDetails": ".transactions_rule_details",
    "TransactionsRuleField": ".transactions_rule_field",
    "TransactionsRuleType": ".transactions_rule_type",
    "TransactionsRulesCreateResponse": ".transactions_rules_create_response",
    "TransactionsRulesListResponse": ".transactions_rules_list_response",
    "TransactionsRulesRemoveResponse": ".transactions_rules_remove_response",
    "TransactionsSyncRequestOptions": ".transactions_sync_request_options",
    "TransactionsSyncResponse": ".transactions_sync_response",
    "Transfer": ".transfer",
    "TransferAccessToken": ".transfer_access_token",
    "TransferAccountId": ".transfer_account_id",
    "TransferAmount": ".transfer_amount",
    "TransferAuthorization": ".transfer_authorization",
    "TransferAuthorizationCreateResponse": ".transfer_authorization_create_response",
    "TransferAuthorizationDecision": ".transfer_authorization_decision",
    "TransferAuthorizationDecisionRationale": ".transfer_authorization_decision_rationale",
    "TransferAuthorizationDecisionRationaleCode": ".transfer_authorization_decision_rationale_code",
    "TransferAuthorizationDevice": ".transfer_authorization_device",
    "TransferAuthorizationGuaranteeDecision": ".transfer_authorization_guarantee_decision",
    "TransferAuthorizationGuaranteeDecisionRationale": ".transfer_authorization_guarantee_decision_rationale",
    "TransferAuthorizationGuaranteeDecisionRationaleCode": ".transfer_authorization_guarantee_decision_rationale_code",
    "TransferAuthorizationId": ".transfer_authorization_id",
    "TransferAuthorizationIdempotencyKey": ".transfer_authorization_idempotency_key",
    "TransferAuthorizationProposedTransfer": ".transfer_authorization_proposed_transfer",
    "TransferAuthorizationUserInRequest": ".transfer_authorization_user_in_request",
    "TransferCancelResponse": ".transfer_cancel_response",
    "TransferCapabilitiesGetResponse": ".transfer_capabilities_get_response",
    "TransferCapabilitiesGetRtp": ".transfer_capabilities_get_rtp",
    "TransferConfigurationGetResponse": ".transfer_configuration_get_response",
    "TransferCreateIdempotencyKey": ".transfer_create_idempotency_key",
    "TransferCreateResponse": ".transfer_create_response",
    "TransferDevice": ".transfer_device",
    "TransferDiligenceStatus": ".transfer_diligence_status",
    "TransferEvent": ".transfer_event",
    "TransferEventListResponse": ".transfer_event_list_response",
    "TransferEventListTransferType": ".transfer_event_list_transfer_type",
    "TransferEventSyncResponse": ".transfer_event_sync_response",
    "TransferEventType": ".transfer_event_type",
    "TransferEventsUpdateWebhook": ".transfer_events_update_webhook",
    "TransferExpectedSettlementScheduleItem": ".transfer_expected_settlement_schedule_item",
    "TransferFailure": ".transfer_failure",
    "TransferFundingAccountIdRequest": ".transfer_funding_account_id_request",
    "TransferFundingAccountIdResponse": ".transfer_funding_account_id_response",
    "TransferGetResponse": ".transfer_get_response",
    "TransferId": ".transfer_id",
    "TransferIdForRefund": ".transfer_id_for_refund",
    "TransferIntentAuthorizationDecision": ".transfer_intent_authorization_decision",
    "TransferIntentCreate": ".transfer_intent_create",
    "TransferIntentCreateMode": ".transfer_intent_create_mode",
    "TransferIntentCreateNetwork": ".transfer_intent_create_network",
    "TransferIntentCreateResponse": ".transfer_intent_create_response",
    "TransferIntentGet": ".transfer_intent_get",
    "TransferIntentGetFailureReason": ".transfer_intent_get_failure_reason",
    "TransferIntentGetResponse": ".transfer_intent_get_response",
    "TransferIntentStatus": ".transfer_intent_status",
    "TransferListResponse": ".transfer_list_response",
    "TransferMetadata": ".transfer_metadata",
    "TransferMetricsGetResponse": ".transfer_metrics_get_response",
    "TransferMigrateAccountResponse": ".transfer_migrate_account_response",
    "TransferNetwork": ".transfer_network",
    "TransferOriginatorCreateResponse": ".transfer_originator_create_response",
    "TransferOriginatorGetResponse": ".transfer_originator_get_response",
    "TransferOriginatorListResponse": ".transfer_originator_list_response",
    "TransferPaymentProfileToken": ".transfer_payment_profile_token",
    "TransferQuestionnaireCreateResponse": ".transfer_questionnaire_create_response",
    "TransferRecurringCancelResponse": ".transfer_recurring_cancel_response",
    "TransferRecurringCreateResponse": ".transfer_recurring_create_response",
    "TransferRecurringGetResponse": ".transfer_recurring_get_response",
    "TransferRecurringIdempotencyKey": ".transfer_recurring_idempotency_key",
    "TransferRecurringListResponse": ".transfer_recurring_list_response",
    "TransferRecurringSchedule": ".transfer_recurring_schedule",
    "TransferRecurringStatus": ".transfer_recurring_status",
    "TransferRefund": ".transfer_refund",
    "TransferRefundAmount": ".transfer_refund_amount",
    "TransferRefundCancelResponse": ".transfer_refund_cancel_response",
    "TransferRefundCreateResponse": ".transfer_refund_create_response",
    "TransferRefundGetResponse": ".transfer_refund_get_response",
    "TransferRefundId": ".transfer_refund_id",
    "TransferRefundIdempotencyKey": ".transfer_refund_idempotency_key",
    "TransferRefundStatus": ".transfer_refund_status",
    "TransferRepayment": ".transfer_repayment",
    "TransferRepaymentListResponse": ".transfer_repayment_list_response",
    "TransferRepaymentReturn": ".transfer_repayment_return",
    "TransferRepaymentReturnListResponse": ".transfer_repayment_return_list_response",
    "TransferScheduleIntervalCount": ".transfer_schedule_interval_count",
    "TransferScheduleIntervalUnit": ".transfer_schedule_interval_unit",
    "TransferStatus": ".transfer_status",
    "TransferSweep": ".transfer_sweep",
    "TransferSweepAmount": ".transfer_sweep_amount",
    "TransferSweepGetResponse": ".transfer_sweep_get_response",
    "TransferSweepId": ".transfer_sweep_id",
    "TransferSweepListResponse": ".transfer_sweep_list_response",
    "TransferSweepStatus": ".transfer_sweep_status",
    "TransferTestClock": ".transfer_test_clock",
    "TransferTestClockId": ".transfer_test_clock_id",
    "TransferType": ".transfer_type",
    "TransferUserAddressInRequest": ".transfer_user_address_in_request",
    "TransferUserAddressInResponse": ".transfer_user_address_in_response",
    "TransferUserInRequest": ".transfer_user_in_request",
    "TransferUserInRequestDeprecated": ".transfer_user_in_request_deprecated",
    "TransferUserInResponse": ".transfer_user_in_response",
    "UnofficialCurrencyCodeList": ".unofficial_currency_code_list",
    "UpdateEntityScreeningRequestSearchTerms": ".update_entity_screening_request_search_terms",
    "UpdateIndividualScreeningRequestSearchTerms": ".update_individual_screening_request_search_terms",
    "Url": ".url",
    "UrlNullable": ".url_nullable",
    "UserAddress": ".user_address",
    "UserCreateResponse": ".user_create_response",
    "UserCustomPassword": ".user_custom_password",
    "UserId": ".user_id",
    "UserIdNumber": ".user_id_number",
    "UserPermissionRevokedWebhook": ".user_permission_revoked_webhook",
    "UserStatedIncomeSourceCategory": ".user_stated_income_source_category",
    "UserStatedIncomeSourceFrequency": ".user_stated_income_source_frequency",
    "UserStatedIncomeSourcePayType": ".user_stated_income_source_pay_type",
    "UserToken": ".user_token",
    "UtcOffset": ".utc_offset",
    "ValidationSource": ".validation_source",
    "ValidationSources": ".validation_sources",
    "VerificationExpiredWebhook": ".verification_expired_webhook",
    "VerificationOfAsset": ".verification_of_asset",
    "VerificationOfAssetResponse": ".verification_of_asset_response",
    "VerificationRefreshStatus": ".verification_refresh_status",
    "VerificationStatus": ".verification_status",
    "VirtualTime": ".virtual_time",
    "W2": ".w2",
    "W2Box12": ".w2box12",
    "W2StateAndLocalWages": ".w2state_and_local_wages",
    "Wallet": ".wallet",
    "WalletBalance": ".wallet_balance",
    "WalletCreateResponse": ".wallet_create_response",
    "WalletGetResponse": ".wallet_get_response",
    "WalletIsoCurrencyCode": ".wallet_iso_currency_code",
    "WalletListResponse": ".wallet_list_response",
    "WalletNumbers": ".wallet_numbers",
    "WalletStatus": ".wallet_status",
    "WalletTransaction": ".wallet_transaction",
    "WalletTransactionAmount": ".wallet_transaction_amount",
    "WalletTransactionCounterparty": ".wallet_transaction_counterparty",
    "WalletTransactionCounterpartyBacs": ".wallet_transaction_counterparty_bacs",
    "WalletTransactionCounterpartyInternational": ".wallet_transaction_counterparty_international",
    "WalletTransactionCounterpartyNumbers": ".wallet_transaction_counterparty_numbers",
    "WalletTransactionExecuteResponse": ".wallet_transaction_execute_response",
    "WalletTransactionGetResponse": ".wallet_transaction_get_response",
    "WalletTransactionIdempotencyKey": ".wallet_transaction_idempotency_key",
    "WalletTransactionListRequestOptions": ".wallet_transaction_list_request_options",
    "WalletTransactionListResponse": ".wallet_transaction_list_response",
    "WalletTransactionStatus": ".wallet_transaction_status",
    "WalletTransactionStatusUpdateWebhook": ".wallet_transaction_status_update_webhook",
    "WalletTransactionType": ".wallet_transaction_type",
    "WalletTransactionsListRequest": ".wallet_transactions_list_request",
    "Warning": ".warning",
    "WarningWarningCode": ".warning_warning_code",
    "WatchlistProgramId": ".watchlist_program_id",
    "WatchlistScreeningAuditTrail": ".watchlist_screening_audit_trail",
    "WatchlistScreeningDocument": ".watchlist_screening_document",
    "WatchlistScreeningDocumentType": ".watchlist_screening_document_type",
    "WatchlistScreeningDocumentValue": ".watchlist_screening_document_value",
    "WatchlistScreeningDocumentValueNullable": ".watchlist_screening_document_value_nullable",
    "WatchlistScreeningEntityCreateResponse": ".watchlist_screening_entity_create_response",
    "WatchlistScreeningEntityGetResponse": ".watchlist_screening_entity_get_response",
    "WatchlistScreeningEntityHistoryListResponse": ".watchlist_screening_entity_history_list_response",
    "WatchlistScreeningEntityHitListResponse": ".watchlist_screening_entity_hit_list_response",
    "WatchlistScreeningEntityListResponse": ".watchlist_screening_entity_list_response",
    "WatchlistScreeningEntityProgramGetResponse": ".watchlist_screening_entity_program_get_response",
    "WatchlistScreeningEntityProgramListResponse": ".watchlist_screening_entity_program_list_response",
    "WatchlistScreeningEntityReviewCreateResponse": ".watchlist_screening_entity_review_create_response",
    "WatchlistScreeningEntityReviewListResponse": ".watchlist_screening_entity_review_list_response",
    "WatchlistScreeningEntityUpdateRequestResettableField": ".watchlist_screening_entity_update_request_resettable_field",
    "WatchlistScreeningEntityUpdateRequestResettableFieldList": ".watchlist_screening_entity_update_request_resettable_field_list",
    "WatchlistScreeningEntityUpdateResponse": ".watchlist_screening_entity_update_response",
    "WatchlistScreeningHit": ".watchlist_screening_hit",
    "WatchlistScreeningHitId": ".watchlist_screening_hit_id",
    "WatchlistScreeningHitLocations": ".watchlist_screening_hit_locations",
    "WatchlistScreeningHitStatus": ".watchlist_screening_hit_status",
    "WatchlistScreeningIndividual": ".watchlist_screening_individual",
    "WatchlistScreeningIndividualCreateResponse": ".watchlist_screening_individual_create_response",
    "WatchlistScreeningIndividualGetResponse": ".watchlist_screening_individual_get_response",
    "WatchlistScreeningIndividualHistoryListResponse": ".watchlist_screening_individual_history_list_response",
    "WatchlistScreeningIndividualHitListResponse": ".watchlist_screening_individual_hit_list_response",
    "WatchlistScreeningIndividualId": ".watchlist_screening_individual_id",
    "WatchlistScreeningIndividualIdNullable": ".watchlist_screening_individual_id_nullable",
    "WatchlistScreeningIndividualListResponse": ".watchlist_screening_individual_list_response",
    "WatchlistScreeningIndividualName": ".watchlist_screening_individual_name",
    "WatchlistScreeningIndividualProgramGetResponse": ".watchlist_screening_individual_program_get_response",
    "WatchlistScreeningIndividualProgramListResponse": ".watchlist_screening_individual_program_list_response",
    "WatchlistScreeningIndividualReviewCreateResponse": ".watchlist_screening_individual_review_create_response",
    "WatchlistScreeningIndividualReviewListResponse": ".watchlist_screening_individual_review_list_response",
    "WatchlistScreeningIndividualUpdateRequestResettableField": ".watchlist_screening_individual_update_request_resettable_field",
    "WatchlistScreeningIndividualUpdateRequestResettableFieldList": ".watchlist_screening_individual_update_request_resettable_field_list",
    "WatchlistScreeningIndividualUpdateResponse": ".watchlist_screening_individual_update_response",
    "WatchlistScreeningPhoneNumber": ".watchlist_screening_phone_number",
    "WatchlistScreeningPhoneNumberNullable": ".watchlist_screening_phone_number_nullable",
    "WatchlistScreeningRequestSearchTerms": ".watchlist_screening_request_search_terms",
    "WatchlistScreeningReview": ".watchlist_screening_review",
    "WatchlistScreeningReviewId": ".watchlist_screening_review_id",
    "WatchlistScreeningSearchTerms": ".watchlist_screening_search_terms",
    "WatchlistScreeningStatus": ".watchlist_screening_status",
    "WeakAliasDetermination": ".weak_alias_determination",
    "WebhookEnvironmentValues": ".webhook_environment_values",
    "WebhookType": ".webhook_type",
    "WebhookUpdateAcknowledgedWebhook": ".webhook_update_acknowledged_webhook",
    "WebhookVerificationKeyGetResponse": ".webhook_verification_key_get_response",
    "YtdGrossIncomeSummaryFieldNumber": ".ytd_gross_income_summary_field_number",
    "YtdNetIncomeSummaryFieldNumber": ".ytd_net_income_summary_field_number",
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
    "AccessToken",
    "AccessTokenNullable",
    "AccountAccess",
    "AccountAssets",
    "AccountBalance",
    "AccountBase",
    "AccountBaseVerificationStatus",
    "AccountFilter",
    "AccountFilterSubtypes",
    "AccountFiltersResponse",
    "AccountIdentity",
    "AccountIdentityMatchScore",
    "AccountIdsWithUpdatedIdentity",
    "AccountProductAccess",
    "AccountProductAccessNullable",
    "AccountSelectionCardinality",
    "AccountSubtype",
    "AccountSubtypes",
    "AccountType",
    "AccountsBalanceGetRequestOptions",
    "AccountsGetRequestOptions",
    "AccountsGetResponse",
    "AchClass",
    "ActionState",
    "Activity",
    "ActivityType",
    "Address",
    "AddressData",
    "AddressDataNullable",
    "AddressMatchScore",
    "AddressNullable",
    "AddressPurposeLabel",
    "ApiClientId",
    "ApiSecret",
    "Application",
    "ApplicationGetResponse",
    "ApplicationId",
    "Apr",
    "AprAprType",
    "Asset",
    "AssetDetail",
    "AssetHolder",
    "AssetHolderName",
    "AssetOwner",
    "AssetOwners",
    "AssetReport",
    "AssetReportAddOns",
    "AssetReportAuditCopyCreateResponse",
    "AssetReportAuditCopyRemoveResponse",
    "AssetReportCreateRequestOptions",
    "AssetReportCreateResponse",
    "AssetReportFilterResponse",
    "AssetReportFreddie",
    "AssetReportFreddieGetResponse",
    "AssetReportGetRequestOptions",
    "AssetReportGetResponse",
    "AssetReportId",
    "AssetReportItem",
    "AssetReportPdfGetRequestOptions",
    "AssetReportPdfGetResponse",
    "AssetReportRefreshAssetReportToken",
    "AssetReportRefreshRequestOptions",
    "AssetReportRefreshResponse",
    "AssetReportRemoveResponse",
    "AssetReportToken",
    "AssetReportTransaction",
    "AssetReportUser",
    "AssetTransaction",
    "AssetTransactionCategoryType",
    "AssetTransactionDescription",
    "AssetTransactionDetail",
    "AssetTransactionType",
    "AssetTransactions",
    "AssetType",
    "Assets",
    "AssetsErrorWebhook",
    "AssetsProductReadyWebhook",
    "AuthGetNumbers",
    "AuthGetRequestOptions",
    "AuthGetResponse",
    "AuthMetadata",
    "AuthSupportedMethods",
    "AutomaticallyVerifiedWebhook",
    "BankInitiatedReturnRisk",
    "BankInitiatedRiskTier",
    "BankTransfer",
    "BankTransferAccessToken",
    "BankTransferAmount",
    "BankTransferBalance",
    "BankTransferBalanceGetResponse",
    "BankTransferCancelResponse",
    "BankTransferCreateResponse",
    "BankTransferDirection",
    "BankTransferEvent",
    "BankTransferEventListBankTransferType",
    "BankTransferEventListDirection",
    "BankTransferEventListResponse",
    "BankTransferEventSyncResponse",
    "BankTransferEventType",
    "BankTransferFailure",
    "BankTransferGetResponse",
    "BankTransferId",
    "BankTransferIdempotencyKey",
    "BankTransferListResponse",
    "BankTransferMetadata",
    "BankTransferMigrateAccountResponse",
    "BankTransferNetwork",
    "BankTransferStatus",
    "BankTransferSweep",
    "BankTransferSweepGetResponse",
    "BankTransferSweepListResponse",
    "BankTransferType",
    "BankTransferUser",
    "BankTransfersEventsUpdateWebhook",
    "BankTransfersEventsUpdateWebhookForAuth",
    "CategoriesGetRequest",
    "CategoriesGetResponse",
    "Category",
    "Cause",
    "City",
    "CityNullable",
    "ClientProvidedEnhancedTransaction",
    "ClientProvidedEnrichedTransaction",
    "ClientProvidedRawTransaction",
    "ClientProvidedTransaction",
    "ClientProvidedTransactionLocation",
    "ClientUserId",
    "ClientUserIdNullable",
    "ConnectedApplication",
    "ConsentPaymentIdempotencyKey",
    "Counterparty",
    "CounterpartyType",
    "CountryCode",
    "Credit1099",
    "Credit1099Filer",
    "Credit1099Payer",
    "Credit1099Recipient",
    "CreditAccount",
    "CreditAccountSubtype",
    "CreditAccountSubtypes",
    "CreditAmountWithCurrency",
    "CreditAuditCopyTokenCreateResponse",
    "CreditAuditCopyTokenRemoveResponse",
    "CreditAuditCopyTokenUpdateResponse",
    "CreditBankEmployer",
    "CreditBankEmployment",
    "CreditBankEmploymentGetResponse",
    "CreditBankEmploymentItem",
    "CreditBankEmploymentReport",
    "CreditBankEmploymentWarning",
    "CreditBankEmploymentWarningType",
    "CreditBankIncome",
    "CreditBankIncomeAccount",
    "CreditBankIncomeAccountType",
    "CreditBankIncomeCategory",
    "CreditBankIncomeCause",
    "CreditBankIncomeErrorType",
    "CreditBankIncomeGetRequestOptions",
    "CreditBankIncomeGetResponse",
    "CreditBankIncomeHistoricalSummary",
    "CreditBankIncomeItem",
    "CreditBankIncomePayFrequency",
    "CreditBankIncomePdfGetResponse",
    "CreditBankIncomeRefreshRequestOptions",
    "CreditBankIncomeRefreshResponse",
    "CreditBankIncomeSource",
    "CreditBankIncomeSummary",
    "CreditBankIncomeTransaction",
    "CreditBankIncomeWarning",
    "CreditBankIncomeWarningCode",
    "CreditBankIncomeWarningType",
    "CreditCardLiability",
    "CreditCategory",
    "CreditDocumentMetadata",
    "CreditDocumentType",
    "CreditEmployerVerification",
    "CreditEmploymentEmployeeType",
    "CreditEmploymentGetResponse",
    "CreditEmploymentItem",
    "CreditEmploymentVerification",
    "CreditEmploymentVerificationStatus",
    "CreditFilter",
    "CreditFreddieMacAssetDetailVoe25",
    "CreditFreddieMacAssetTransactionDetailVoe25",
    "CreditFreddieMacAssetTransactionVoa24",
    "CreditFreddieMacAssetTransactionVoe25",
    "CreditFreddieMacAssetTransactionsVoa24",
    "CreditFreddieMacAssetTransactionsVoe25",
    "CreditFreddieMacAssetVoa24",
    "CreditFreddieMacAssetVoe25",
    "CreditFreddieMacAssetsVoa24",
    "CreditFreddieMacAssetsVoe25",
    "CreditFreddieMacIndividualNameVoa24",
    "CreditFreddieMacLoanIdentifiersVoa24",
    "CreditFreddieMacLoanVoa24",
    "CreditFreddieMacLoansVoa24",
    "CreditFreddieMacPartiesVoa24",
    "CreditFreddieMacPartyIndividualVoa24",
    "CreditFreddieMacPartyVoa24",
    "CreditFreddieMacReportingInformationVoa24",
    "CreditFreddieMacReportsGetResponse",
    "CreditFreddieMacServiceVoa24",
    "CreditFreddieMacServiceVoe25",
    "CreditFreddieMacServicesVoa24",
    "CreditFreddieMacServicesVoe25",
    "CreditFreddieMacVerificationOfAssetResponseVoa24",
    "CreditFreddieMacVerificationOfAssetResponseVoe25",
    "CreditFreddieMacVerificationOfAssetVoa24",
    "CreditFreddieMacVerificationOfAssetVoe25",
    "CreditFreddieMacVerificationOfAssetsDealVoa24",
    "CreditFreddieMacVerificationOfAssetsVoa24",
    "CreditFreddieVerificationOfEmploymentDealVoe25",
    "CreditFreddieVerificationOfEmploymentVoe25",
    "CreditIsoCurrencyCode",
    "CreditPayStub",
    "CreditPayStubAddress",
    "CreditPayStubDeductions",
    "CreditPayStubEarnings",
    "CreditPayStubEmployee",
    "CreditPayStubEmployer",
    "CreditPayStubNetPay",
    "CreditPayStubPayBasisType",
    "CreditPayrollIncomeGetResponse",
    "CreditPayrollIncomePrecheckResponse",
    "CreditPayrollIncomeRefreshRequestOptions",
    "CreditPayrollIncomeRefreshResponse",
    "CreditPayrollIncomeRefreshStatus",
    "CreditPayrollIncomeRiskSignalsGetRequest",
    "CreditPayrollIncomeRiskSignalsGetResponse",
    "CreditPlatformIds",
    "CreditRelayCreateResponse",
    "CreditRelayRefreshResponse",
    "CreditRelayRemoveResponse",
    "CreditSession",
    "CreditSessionBankEmploymentResult",
    "CreditSessionBankEmploymentStatus",
    "CreditSessionBankIncomeResult",
    "CreditSessionBankIncomeStatus",
    "CreditSessionDocumentIncomeResult",
    "CreditSessionError",
    "CreditSessionItemAddResult",
    "CreditSessionPayrollIncomeResult",
    "CreditSessionResults",
    "CreditSessionsGetResponse",
    "CreditUnofficialCurrencyCode",
    "CreditW2",
    "Cursor",
    "CustomerInitiatedReturnRisk",
    "CustomerInitiatedRiskTier",
    "DashboardUser",
    "DashboardUserGetResponse",
    "DashboardUserId",
    "DashboardUserIdNullable",
    "DashboardUserListResponse",
    "DashboardUserStatus",
    "DateRange",
    "Deductions",
    "DeductionsBreakdown",
    "DeductionsTotal",
    "DefaultUpdateWebhook",
    "DepositSwitchAddressData",
    "DepositSwitchAltCreateResponse",
    "DepositSwitchCreateRequestOptions",
    "DepositSwitchCreateResponse",
    "DepositSwitchGetResponse",
    "DepositSwitchGetResponseState",
    "DepositSwitchGetResponseSwitchMethod",
    "DepositSwitchStateUpdateWebhook",
    "DepositSwitchTargetAccount",
    "DepositSwitchTargetAccountAccountSubtype",
    "DepositSwitchTargetUser",
    "DepositSwitchTokenCreateResponse",
    "DepositoryAccount",
    "DepositoryAccountSubtype",
    "DepositoryAccountSubtypes",
    "DepositoryFilter",
    "DetailedOriginator",
    "DistributionBreakdown",
    "DocType",
    "DocumentAnalysis",
    "DocumentAuthenticityMatchCode",
    "DocumentDateOfBirthMatchCode",
    "DocumentImageBack",
    "DocumentImageCroppedBack",
    "DocumentImageCroppedFront",
    "DocumentImageFace",
    "DocumentImageFront",
    "DocumentMetadata",
    "DocumentNameMatchCode",
    "DocumentRiskSignal",
    "DocumentRiskSignalInstitutionMetadata",
    "DocumentRiskSignalsObject",
    "DocumentRiskSummary",
    "DocumentStatus",
    "DocumentaryVerification",
    "DocumentaryVerificationDocument",
    "Earnings",
    "EarningsBreakdown",
    "EarningsBreakdownCanonicalDescription",
    "EarningsTotal",
    "Email",
    "EmailAddress",
    "EmailAddressMatchScore",
    "EmailAddressNullable",
    "EmailType",
    "Employee",
    "EmployeeIncomeSummaryFieldString",
    "Employer",
    "EmployerIncomeSummaryFieldString",
    "EmployerVerification",
    "EmployersSearchResponse",
    "EmploymentDetails",
    "EmploymentSourceType",
    "EmploymentVerification",
    "EmploymentVerificationGetResponse",
    "EmploymentVerificationStatus",
    "Enhancements",
    "EnrichTransactionDirection",
    "Enrichments",
    "EntityDocument",
    "EntityDocumentType",
    "EntityScreeningHitAnalysis",
    "EntityScreeningHitData",
    "EntityScreeningHitDocumentsItems",
    "EntityScreeningHitEmails",
    "EntityScreeningHitEmailsItems",
    "EntityScreeningHitNames",
    "EntityScreeningHitNamesItems",
    "EntityScreeningHitPhoneNumbers",
    "EntityScreeningHitUrls",
    "EntityScreeningHitUrlsItems",
    "EntityScreeningHitsPhoneNumberItems",
    "EntityScreeningStatusUpdatedWebhook",
    "EntityWatchlistCode",
    "EntityWatchlistProgram",
    "EntityWatchlistProgramId",
    "EntityWatchlistScreening",
    "EntityWatchlistScreeningHit",
    "EntityWatchlistScreeningHitId",
    "EntityWatchlistScreeningId",
    "EntityWatchlistScreeningName",
    "EntityWatchlistScreeningProgramName",
    "EntityWatchlistScreeningReview",
    "EntityWatchlistScreeningReviewId",
    "EntityWatchlistScreeningSearchTerms",
    "EntityWatchlistSearchTerms",
    "ExpirationDate",
    "ExternalPaymentInitiationConsentOptions",
    "ExternalPaymentOptions",
    "ExternalPaymentRefundDetails",
    "ExternalPaymentScheduleBase",
    "ExternalPaymentScheduleGet",
    "ExternalPaymentScheduleRequest",
    "FallbackAuthMicrodepositAutoVerifiedWebhook",
    "FallbackAuthMicrodepositVerificationExpiredWebhook",
    "FamilyNameField",
    "FdxContentTypes",
    "FdxFiAttribute",
    "FdxHateoasLink",
    "FdxHateoasLinkAction",
    "FdxNotificationCategory",
    "FdxNotificationPayload",
    "FdxNotificationPayloadIdType",
    "FdxNotificationPriority",
    "FdxNotificationSeverity",
    "FdxNotificationType",
    "FdxParty",
    "FdxPartyRegistry",
    "FdxPartyType",
    "FdxTimestamp",
    "Form1099Type",
    "GenericCountryCode",
    "GenericCountryCodeNullable",
    "GenericScreeningHitLocationItems",
    "GivenNameField",
    "HealthIncident",
    "HistoricalBalance",
    "HistoricalUpdateWebhook",
    "Holding",
    "HoldingsDefaultUpdateWebhook",
    "HoldingsOverride",
    "IdNumberType",
    "IdNumberValue",
    "IdempotencyFlag",
    "IdentityDefaultUpdateWebhook",
    "IdentityGetRequestOptions",
    "IdentityGetResponse",
    "IdentityMatchIdentityVerificationId",
    "IdentityMatchRequestOptions",
    "IdentityMatchResponse",
    "IdentityMatchUser",
    "IdentityUpdateTypes",
    "IdentityVerification",
    "IdentityVerificationConsent",
    "IdentityVerificationCreateResponse",
    "IdentityVerificationGetResponse",
    "IdentityVerificationId",
    "IdentityVerificationListResponse",
    "IdentityVerificationRequestUser",
    "IdentityVerificationRequestUserName",
    "IdentityVerificationResponseUserName",
    "IdentityVerificationRetriedWebhook",
    "IdentityVerificationRetryRequestStepsObject",
    "IdentityVerificationRetryResponse",
    "IdentityVerificationStatus",
    "IdentityVerificationStatusUpdatedWebhook",
    "IdentityVerificationStepStatus",
    "IdentityVerificationStepSummary",
    "IdentityVerificationStepUpdatedWebhook",
    "IdentityVerificationTemplateId",
    "IdentityVerificationTemplateReference",
    "IdentityVerificationTemplateVersion",
    "IdentityVerificationUserAddress",
    "IdentityVerificationUserData",
    "IdentityVerificationUserPhoneNumber",
    "ImageQuality",
    "IncidentUpdate",
    "IncidentUpdateStatus",
    "IncomeBreakdown",
    "IncomeBreakdownType",
    "IncomeOverride",
    "IncomeSummary",
    "IncomeSummaryFieldNumber",
    "IncomeSummaryFieldString",
    "IncomeVerificationCreateRequestOptions",
    "IncomeVerificationCreateResponse",
    "IncomeVerificationPayrollFlowType",
    "IncomeVerificationPaystubsGetResponse",
    "IncomeVerificationPrecheckConfidence",
    "IncomeVerificationPrecheckEmployer",
    "IncomeVerificationPrecheckEmployerAddress",
    "IncomeVerificationPrecheckEmployerAddressData",
    "IncomeVerificationPrecheckMilitaryInfo",
    "IncomeVerificationPrecheckPayrollInstitution",
    "IncomeVerificationPrecheckResponse",
    "IncomeVerificationPrecheckUser",
    "IncomeVerificationSourceType",
    "IncomeVerificationStatusWebhook",
    "IncomeVerificationTaxformsGetResponse",
    "IncomeVerificationWebhookStatus",
    "IndividualName",
    "IndividualScreeningHitNames",
    "IndividualWatchlistCode",
    "IndividualWatchlistProgram",
    "IndividualWatchlistScreeningProgramName",
    "InflowModel",
    "InitialUpdateWebhook",
    "Institution",
    "InstitutionStatus",
    "InstitutionSupportedNetworks",
    "InstitutionsGetByIdRequestOptions",
    "InstitutionsGetByIdResponse",
    "InstitutionsGetRequestOptions",
    "InstitutionsGetResponse",
    "InstitutionsSearchAccountFilter",
    "InstitutionsSearchPaymentInitiationOptions",
    "InstitutionsSearchRequestOptions",
    "InstitutionsSearchResponse",
    "InternalUid",
    "InvestmentAccountSubtype",
    "InvestmentAccountSubtypeStandalone",
    "InvestmentAccountSubtypes",
    "InvestmentFilter",
    "InvestmentHoldingsGetRequestOptions",
    "InvestmentTransaction",
    "InvestmentTransactionSubtype",
    "InvestmentTransactionType",
    "InvestmentsDefaultUpdateWebhook",
    "InvestmentsHoldingsGetResponse",
    "InvestmentsTransactionsGetRequestOptions",
    "InvestmentsTransactionsGetResponse",
    "InvestmentsTransactionsOverride",
    "IpAddress",
    "Iso8601Date",
    "Iso8601DateNullable",
    "IssuingCountry",
    "Item",
    "ItemAccessTokenInvalidateResponse",
    "ItemActivityListResponse",
    "ItemApplicationListResponse",
    "ItemApplicationListUserAuth",
    "ItemApplicationScopesUpdateResponse",
    "ItemErrorWebhook",
    "ItemGetResponse",
    "ItemId",
    "ItemImportRequestOptions",
    "ItemImportRequestUserAuth",
    "ItemImportResponse",
    "ItemLoginRepairedWebhook",
    "ItemProductReadyWebhook",
    "ItemPublicTokenCreateResponse",
    "ItemPublicTokenExchangeResponse",
    "ItemRemoveResponse",
    "ItemStatus",
    "ItemStatusInvestments",
    "ItemStatusLastWebhook",
    "ItemStatusNullable",
    "ItemStatusTransactions",
    "ItemUpdateType",
    "ItemWebhookUpdateResponse",
    "JwkPublicKey",
    "JwtHeader",
    "KycCheckAddressSummary",
    "KycCheckDateOfBirthSummary",
    "KycCheckDetails",
    "KycCheckIdNumberSummary",
    "KycCheckNameSummary",
    "KycCheckPhoneSummary",
    "LastDataAccessTimes",
    "LiabilitiesAccountIdsWithUpdatedLiabilities",
    "LiabilitiesDefaultUpdateWebhook",
    "LiabilitiesGetRequestOptions",
    "LiabilitiesGetResponse",
    "LiabilitiesObject",
    "LiabilityOverride",
    "LinkCallbackMetadata",
    "LinkDeliveryAccount",
    "LinkDeliveryCallbackWebhook",
    "LinkDeliveryCommunicationMethod",
    "LinkDeliveryCreateResponse",
    "LinkDeliveryDeliveryMethod",
    "LinkDeliveryGetResponse",
    "LinkDeliveryInstitution",
    "LinkDeliveryMetadata",
    "LinkDeliveryOptions",
    "LinkDeliveryRecipient",
    "LinkDeliverySessionStatus",
    "LinkDeliveryVerificationStatus",
    "LinkDeliveryWebhookCallbackType",
    "LinkDeliveryWebhookCommunicationMethod",
    "LinkDeliveryWebhookDeliveryStatus",
    "LinkEventName",
    "LinkOAuthCorrelationIdExchangeResponse",
    "LinkTokenAccountFilters",
    "LinkTokenCreateCreditFilter",
    "LinkTokenCreateDepositoryFilter",
    "LinkTokenCreateInstitutionData",
    "LinkTokenCreateInvestmentFilter",
    "LinkTokenCreateLoanFilter",
    "LinkTokenCreateRequestAccountSubtypes",
    "LinkTokenCreateRequestAuth",
    "LinkTokenCreateRequestAuthFlowType",
    "LinkTokenCreateRequestDepositSwitch",
    "LinkTokenCreateRequestEmployment",
    "LinkTokenCreateRequestEmploymentBankIncome",
    "LinkTokenCreateRequestIdentityVerification",
    "LinkTokenCreateRequestIncomeVerification",
    "LinkTokenCreateRequestIncomeVerificationBankIncome",
    "LinkTokenCreateRequestIncomeVerificationPayrollIncome",
    "LinkTokenCreateRequestPaymentInitiation",
    "LinkTokenCreateRequestTransfer",
    "LinkTokenCreateRequestUpdate",
    "LinkTokenCreateRequestUser",
    "LinkTokenCreateRequestUserName",
    "LinkTokenCreateRequestUserStatedIncomeSource",
    "LinkTokenCreateResponse",
    "LinkTokenEuConfig",
    "LinkTokenGetMetadataResponse",
    "LinkTokenGetResponse",
    "LinkTokenInvestments",
    "LinkUserDeliveryStatusWebhook",
    "Loan",
    "LoanAccount",
    "LoanAccountSubtype",
    "LoanAccountSubtypes",
    "LoanFilter",
    "LoanIdentifier",
    "LoanIdentifierType",
    "LoanIdentifiers",
    "Loans",
    "Location",
    "MatchSummary",
    "MatchSummaryCode",
    "Meta",
    "Mfa",
    "MinLastUpdatedDatetime",
    "MortgageInterestRate",
    "MortgageLiability",
    "MortgagePropertyAddress",
    "MultiDocumentRiskSignal",
    "NameMatchScore",
    "NetPay",
    "NewAccountsAvailableWebhook",
    "Numbers",
    "NumbersAch",
    "NumbersAchNullable",
    "NumbersBacs",
    "NumbersBacsNullable",
    "NumbersEft",
    "NumbersEftNullable",
    "NumbersIban",
    "NumbersIbanNullable",
    "NumbersInternational",
    "NumbersInternationalIban",
    "NumbersInternationalNullable",
    "Originator",
    "OverrideAccountType",
    "OverrideAccounts",
    "Owner",
    "OwnerOverride",
    "OwnershipType",
    "Parties",
    "PartnerCustomerCreateResponse",
    "PartnerCustomerEnableResponse",
    "PartnerCustomerGetResponse",
    "PartnerCustomerOAuthInstitutionsGetResponse",
    "PartnerCustomerRemoveResponse",
    "PartnerEndCustomer",
    "PartnerEndCustomerAddress",
    "PartnerEndCustomerAssetsUnderManagement",
    "PartnerEndCustomerBillingContact",
    "PartnerEndCustomerCustomerSupportInfo",
    "PartnerEndCustomerFlowdownStatus",
    "PartnerEndCustomerOAuthInstitution",
    "PartnerEndCustomerOAuthInstitutionApplicationStatus",
    "PartnerEndCustomerOAuthInstitutionEnvironments",
    "PartnerEndCustomerOAuthStatusUpdatedValues",
    "PartnerEndCustomerOAuthStatusUpdatedWebhook",
    "PartnerEndCustomerQuestionnaireStatus",
    "PartnerEndCustomerSecrets",
    "PartnerEndCustomerStatus",
    "PartnerEndCustomerTechnicalContact",
    "PartnerEndCustomerWithSecrets",
    "Party",
    "PartyIndividual",
    "PartyRoleType",
    "Pay",
    "PayFrequency",
    "PayFrequencyValue",
    "PayPeriodDetails",
    "PayPeriodDetailsPayFrequency",
    "PayStubDeductionsBreakdown",
    "PayStubDeductionsTotal",
    "PayStubDistributionBreakdown",
    "PayStubEarningsBreakdown",
    "PayStubEarningsBreakdownCanonicalDescription",
    "PayStubEarningsTotal",
    "PayStubPayPeriodDetails",
    "PayStubTaxpayerId",
    "PaymentAmount",
    "PaymentAmountCurrency",
    "PaymentAmountNullable",
    "PaymentAmountRefunded",
    "PaymentAmountToRefund",
    "PaymentChannel",
    "PaymentConsentMaxPaymentAmount",
    "PaymentConsentPeriodicAlignment",
    "PaymentConsentPeriodicAmount",
    "PaymentConsentPeriodicAmountAmount",
    "PaymentConsentPeriodicInterval",
    "PaymentConsentValidDateTime",
    "PaymentInitiationAddress",
    "PaymentInitiationConsent",
    "PaymentInitiationConsentConstraints",
    "PaymentInitiationConsentCreateResponse",
    "PaymentInitiationConsentGetResponse",
    "PaymentInitiationConsentPaymentExecuteResponse",
    "PaymentInitiationConsentRevokeResponse",
    "PaymentInitiationConsentScope",
    "PaymentInitiationConsentStatus",
    "PaymentInitiationMaximumPaymentAmount",
    "PaymentInitiationMetadata",
    "PaymentInitiationOptionalRestrictionBacs",
    "PaymentInitiationPayment",
    "PaymentInitiationPaymentCreateResponse",
    "PaymentInitiationPaymentCreateStatus",
    "PaymentInitiationPaymentGetResponse",
    "PaymentInitiationPaymentListResponse",
    "PaymentInitiationPaymentReverseResponse",
    "PaymentInitiationPaymentStatus",
    "PaymentInitiationPaymentTokenCreateResponse",
    "PaymentInitiationRecipient",
    "PaymentInitiationRecipientCreateResponse",
    "PaymentInitiationRecipientGetResponse",
    "PaymentInitiationRecipientListResponse",
    "PaymentInitiationStandingOrderMetadata",
    "PaymentMeta",
    "PaymentProfileCreateResponse",
    "PaymentProfileGetResponse",
    "PaymentProfileRemoveResponse",
    "PaymentProfileStatus",
    "PaymentProfileToken",
    "PaymentScheduleInterval",
    "PaymentScheme",
    "PaymentStatusUpdateWebhook",
    "PayrollIncomeAccountData",
    "PayrollIncomeObject",
    "PayrollIncomeRateOfPay",
    "PayrollItem",
    "PayrollItemStatus",
    "PayrollRiskSignalsItem",
    "Paystub",
    "PaystubAddress",
    "PaystubDeduction",
    "PaystubDetails",
    "PaystubEmployer",
    "PaystubOverride",
    "PaystubOverrideEmployee",
    "PaystubOverrideEmployeeAddress",
    "PaystubOverrideEmployer",
    "PaystubPayFrequency",
    "PaystubYtdDetails",
    "PendingExpirationWebhook",
    "PersonalFinanceCategory",
    "PhoneNumber",
    "PhoneNumberMatchScore",
    "PhoneNumberType",
    "PhoneType",
    "PhysicalDocumentCategory",
    "PhysicalDocumentExtractedData",
    "PhysicalDocumentExtractedDataAnalysis",
    "PhysicalDocumentIdNumber",
    "PhysicalDocumentImages",
    "PlaidError",
    "PlaidErrorType",
    "PlatformIds",
    "PoBoxStatus",
    "PostalCode",
    "PostalCodeNullable",
    "PreviousIdentityVerificationAttemptId",
    "ProcessorAuthGetResponse",
    "ProcessorBalanceGetRequestOptions",
    "ProcessorBalanceGetResponse",
    "ProcessorBankTransferCreateResponse",
    "ProcessorIdentityGetResponse",
    "ProcessorNumber",
    "ProcessorSignalDecisionReportResponse",
    "ProcessorSignalEvaluateResponse",
    "ProcessorSignalReturnReportResponse",
    "ProcessorStripeBankAccountTokenCreateResponse",
    "ProcessorToken",
    "ProcessorTokenCreateResponse",
    "ProductAccess",
    "ProductStatus",
    "ProductStatusBreakdown",
    "ProductStatusBreakdownRefreshInterval",
    "ProductStatusStatus",
    "Products",
    "ProgramArchived",
    "ProgramNameSensitivity",
    "ProjectedIncomeSummaryFieldNumber",
    "ProxyType",
    "PslfStatus",
    "RecaptchaRequiredError",
    "RecipientBacs",
    "RecipientBacsNullable",
    "Recurrence",
    "RecurringCancelledWebhook",
    "RecurringNewTransferWebhook",
    "RecurringTransactionFrequency",
    "RecurringTransactionsUpdateWebhook",
    "RecurringTransfer",
    "RecurringTransferId",
    "RecurringTransferNullable",
    "RecurringTransferSkippedWebhook",
    "Region",
    "RegionNullable",
    "RemovedTransaction",
    "ReportType",
    "ReportingInformation",
    "RequestId",
    "ReviewComment",
    "RiskCheckBehavior",
    "RiskCheckBehaviorBotDetectedLabel",
    "RiskCheckBehaviorFraudRingDetectedLabel",
    "RiskCheckBehaviorUserInteractionsLabel",
    "RiskCheckDetails",
    "RiskCheckDevice",
    "RiskCheckEmail",
    "RiskCheckEmailDomainIsCustom",
    "RiskCheckEmailDomainIsDisposable",
    "RiskCheckEmailDomainIsFreeProvider",
    "RiskCheckEmailIsDeliverableStatus",
    "RiskCheckEmailTopLevelDomainIsSuspicious",
    "RiskCheckLinkedService",
    "RiskCheckPhone",
    "RiskSignalDocumentReference",
    "Role",
    "RoleDetail",
    "Roles",
    "SandboxBankTransferFireWebhookResponse",
    "SandboxBankTransferSimulateResponse",
    "SandboxIncomeFireWebhookResponse",
    "SandboxItemFireWebhookResponse",
    "SandboxItemResetLoginResponse",
    "SandboxItemSetVerificationStatusResponse",
    "SandboxOauthSelectAccountsResponse",
    "SandboxOverridePassword",
    "SandboxOverrideUsername",
    "SandboxPaymentProfileResetLoginResponse",
    "SandboxProcessorTokenCreateRequestOptions",
    "SandboxProcessorTokenCreateResponse",
    "SandboxPublicTokenCreateRequestIncomeVerificationBankIncome",
    "SandboxPublicTokenCreateRequestOptions",
    "SandboxPublicTokenCreateRequestOptionsIncomeVerification",
    "SandboxPublicTokenCreateRequestOptionsTransactions",
    "SandboxPublicTokenCreateResponse",
    "SandboxTransferFireWebhookResponse",
    "SandboxTransferRepaymentSimulateResponse",
    "SandboxTransferSimulateResponse",
    "SandboxTransferSweepSimulateResponse",
    "SandboxTransferTestClockAdvanceResponse",
    "SandboxTransferTestClockCreateResponse",
    "SandboxTransferTestClockGetResponse",
    "SandboxTransferTestClockListResponse",
    "Scopes",
    "ScopesContext",
    "ScopesNullable",
    "ScopesState",
    "ScreeningHitAnalysis",
    "ScreeningHitData",
    "ScreeningHitDateOfBirthItem",
    "ScreeningHitDocumentsItems",
    "ScreeningHitNamesItems",
    "ScreeningStatusUpdatedWebhook",
    "Security",
    "SecurityOverride",
    "SenderBacsNullable",
    "Service",
    "ServiceProductFulfillment",
    "ServiceProductFulfillmentDetail",
    "ServiceProductFulfillmentIdentifier",
    "ServicerAddressData",
    "Services",
    "ShareableUrl",
    "SignalAddressData",
    "SignalDecisionOutcome",
    "SignalDecisionReportResponse",
    "SignalDevice",
    "SignalEvaluateCoreAttributes",
    "SignalEvaluateResponse",
    "SignalPaymentMethod",
    "SignalPersonName",
    "SignalPrepareResponse",
    "SignalReturnReportResponse",
    "SignalScore",
    "SignalScores",
    "SignalUser",
    "SignalWarning",
    "SimulatedTransferSweep",
    "SingleDocumentRiskSignal",
    "Source",
    "SourceUid",
    "StandaloneAccountType",
    "StandaloneCurrencyCodeList",
    "StandaloneInvestmentTransactionBuyType",
    "StandaloneInvestmentTransactionCashType",
    "StandaloneInvestmentTransactionFeeType",
    "StandaloneInvestmentTransactionSellType",
    "StandaloneInvestmentTransactionTransferType",
    "StandaloneInvestmentTransactionType",
    "Status",
    "Statuses",
    "Strategy",
    "Street",
    "Street2",
    "StreetNullable",
    "StudentLoan",
    "StudentLoanRepaymentModel",
    "StudentLoanStatus",
    "StudentLoanStatusType",
    "StudentRepaymentPlan",
    "StudentRepaymentPlanType",
    "SyncUpdatesAvailableWebhook",
    "Taxform",
    "TaxpayerId",
    "TaxpayerIdentifier",
    "TaxpayerIdentifierType",
    "TaxpayerIdentifiers",
    "Timestamp",
    "TimestampNullable",
    "Total",
    "TotalCanonicalDescription",
    "Transaction",
    "TransactionBase",
    "TransactionBaseTransactionType",
    "TransactionCode",
    "TransactionCounterparty",
    "TransactionData",
    "TransactionOverride",
    "TransactionPaymentChannel",
    "TransactionStream",
    "TransactionStreamAmount",
    "TransactionStreamStatus",
    "TransactionsCategoryRule",
    "TransactionsEnhanceGetResponse",
    "TransactionsEnrichGetResponse",
    "TransactionsEnrichRequestOptions",
    "TransactionsGetRequestOptions",
    "TransactionsGetResponse",
    "TransactionsRecurringGetRequestOptions",
    "TransactionsRecurringGetResponse",
    "TransactionsRefreshResponse",
    "TransactionsRemovedWebhook",
    "TransactionsRuleDetails",
    "TransactionsRuleField",
    "TransactionsRuleType",
    "TransactionsRulesCreateResponse",
    "TransactionsRulesListResponse",
    "TransactionsRulesRemoveResponse",
    "TransactionsSyncRequestOptions",
    "TransactionsSyncResponse",
    "Transfer",
    "TransferAccessToken",
    "TransferAccountId",
    "TransferAmount",
    "TransferAuthorization",
    "TransferAuthorizationCreateResponse",
    "TransferAuthorizationDecision",
    "TransferAuthorizationDecisionRationale",
    "TransferAuthorizationDecisionRationaleCode",
    "TransferAuthorizationDevice",
    "TransferAuthorizationGuaranteeDecision",
    "TransferAuthorizationGuaranteeDecisionRationale",
    "TransferAuthorizationGuaranteeDecisionRationaleCode",
    "TransferAuthorizationId",
    "TransferAuthorizationIdempotencyKey",
    "TransferAuthorizationProposedTransfer",
    "TransferAuthorizationUserInRequest",
    "TransferCancelResponse",
    "TransferCapabilitiesGetResponse",
    "TransferCapabilitiesGetRtp",
    "TransferConfigurationGetResponse",
    "TransferCreateIdempotencyKey",
    "TransferCreateResponse",
    "TransferDevice",
    "TransferDiligenceStatus",
    "TransferEvent",
    "TransferEventListResponse",
    "TransferEventListTransferType",
    "TransferEventSyncResponse",
    "TransferEventType",
    "TransferEventsUpdateWebhook",
    "TransferExpectedSettlementScheduleItem",
    "TransferFailure",
    "TransferFundingAccountIdRequest",
    "TransferFundingAccountIdResponse",
    "TransferGetResponse",
    "TransferId",
    "TransferIdForRefund",
    "TransferIntentAuthorizationDecision",
    "TransferIntentCreate",
    "TransferIntentCreateMode",
    "TransferIntentCreateNetwork",
    "TransferIntentCreateResponse",
    "TransferIntentGet",
    "TransferIntentGetFailureReason",
    "TransferIntentGetResponse",
    "TransferIntentStatus",
    "TransferListResponse",
    "TransferMetadata",
    "TransferMetricsGetResponse",
    "TransferMigrateAccountResponse",
    "TransferNetwork",
    "TransferOriginatorCreateResponse",
    "TransferOriginatorGetResponse",
    "TransferOriginatorListResponse",
    "TransferPaymentProfileToken",
    "TransferQuestionnaireCreateResponse",
    "TransferRecurringCancelResponse",
    "TransferRecurringCreateResponse",
    "TransferRecurringGetResponse",
    "TransferRecurringIdempotencyKey",
    "TransferRecurringListResponse",
    "TransferRecurringSchedule",
    "TransferRecurringStatus",
    "TransferRefund",
    "TransferRefundAmount",
    "TransferRefundCancelResponse",
    "TransferRefundCreateResponse",
    "TransferRefundGetResponse",
    "TransferRefundId",
    "TransferRefundIdempotencyKey",
    "TransferRefundStatus",
    "TransferRepayment",
    "TransferRepaymentListResponse",
    "TransferRepaymentReturn",
    "TransferRepaymentReturnListResponse",
    "TransferScheduleIntervalCount",
    "TransferScheduleIntervalUnit",
    "TransferStatus",
    "TransferSweep",
    "TransferSweepAmount",
    "TransferSweepGetResponse",
    "TransferSweepId",
    "TransferSweepListResponse",
    "TransferSweepStatus",
    "TransferTestClock",
    "TransferTestClockId",
    "TransferType",
    "TransferUserAddressInRequest",
    "TransferUserAddressInResponse",
    "TransferUserInRequest",
    "TransferUserInRequestDeprecated",
    "TransferUserInResponse",
    "UnofficialCurrencyCodeList",
    "UpdateEntityScreeningRequestSearchTerms",
    "UpdateIndividualScreeningRequestSearchTerms",
    "Url",
    "UrlNullable",
    "UserAddress",
    "UserCreateResponse",
    "UserCustomPassword",
    "UserId",
    "UserIdNumber",
    "UserPermissionRevokedWebhook",
    "UserStatedIncomeSourceCategory",
    "UserStatedIncomeSourceFrequency",
    "UserStatedIncomeSourcePayType",
    "UserToken",
    "UtcOffset",
    "ValidationSource",
    "ValidationSources",
    "VerificationExpiredWebhook",
    "VerificationOfAsset",
    "VerificationOfAssetResponse",
    "VerificationRefreshStatus",
    "VerificationStatus",
    "VirtualTime",
    "W2",
    "W2Box12",
    "W2StateAndLocalWages",
    "Wallet",
    "WalletBalance",
    "WalletCreateResponse",
    "WalletGetResponse",
    "WalletIsoCurrencyCode",
    "WalletListResponse",
    "WalletNumbers",
    "WalletStatus",
    "WalletTransaction",
    "WalletTransactionAmount",
    "WalletTransactionCounterparty",
    "WalletTransactionCounterpartyBacs",
    "WalletTransactionCounterpartyInternational",
    "WalletTransactionCounterpartyNumbers",
    "WalletTransactionExecuteResponse",
    "WalletTransactionGetResponse",
    "WalletTransactionIdempotencyKey",
    "WalletTransactionListRequestOptions",
    "WalletTransactionListResponse",
    "WalletTransactionStatus",
    "WalletTransactionStatusUpdateWebhook",
    "WalletTransactionType",
    "WalletTransactionsListRequest",
    "Warning",
    "WarningWarningCode",
    "WatchlistProgramId",
    "WatchlistScreeningAuditTrail",
    "WatchlistScreeningDocument",
    "WatchlistScreeningDocumentType",
    "WatchlistScreeningDocumentValue",
    "WatchlistScreeningDocumentValueNullable",
    "WatchlistScreeningEntityCreateResponse",
    "WatchlistScreeningEntityGetResponse",
    "WatchlistScreeningEntityHistoryListResponse",
    "WatchlistScreeningEntityHitListResponse",
    "WatchlistScreeningEntityListResponse",
    "WatchlistScreeningEntityProgramGetResponse",
    "WatchlistScreeningEntityProgramListResponse",
    "WatchlistScreeningEntityReviewCreateResponse",
    "WatchlistScreeningEntityReviewListResponse",
    "WatchlistScreeningEntityUpdateRequestResettableField",
    "WatchlistScreeningEntityUpdateRequestResettableFieldList",
    "WatchlistScreeningEntityUpdateResponse",
    "WatchlistScreeningHit",
    "WatchlistScreeningHitId",
    "WatchlistScreeningHitLocations",
    "WatchlistScreeningHitStatus",
    "WatchlistScreeningIndividual",
    "WatchlistScreeningIndividualCreateResponse",
    "WatchlistScreeningIndividualGetResponse",
    "WatchlistScreeningIndividualHistoryListResponse",
    "WatchlistScreeningIndividualHitListResponse",
    "WatchlistScreeningIndividualId",
    "WatchlistScreeningIndividualIdNullable",
    "WatchlistScreeningIndividualListResponse",
    "WatchlistScreeningIndividualName",
    "WatchlistScreeningIndividualProgramGetResponse",
    "WatchlistScreeningIndividualProgramListResponse",
    "WatchlistScreeningIndividualReviewCreateResponse",
    "WatchlistScreeningIndividualReviewListResponse",
    "WatchlistScreeningIndividualUpdateRequestResettableField",
    "WatchlistScreeningIndividualUpdateRequestResettableFieldList",
    "WatchlistScreeningIndividualUpdateResponse",
    "WatchlistScreeningPhoneNumber",
    "WatchlistScreeningPhoneNumberNullable",
    "WatchlistScreeningRequestSearchTerms",
    "WatchlistScreeningReview",
    "WatchlistScreeningReviewId",
    "WatchlistScreeningSearchTerms",
    "WatchlistScreeningStatus",
    "WeakAliasDetermination",
    "WebhookEnvironmentValues",
    "WebhookType",
    "WebhookUpdateAcknowledgedWebhook",
    "WebhookVerificationKeyGetResponse",
    "YtdGrossIncomeSummaryFieldNumber",
    "YtdNetIncomeSummaryFieldNumber",
]
