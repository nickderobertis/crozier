

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.access_token import AccessToken
from ..types.access_token_nullable import AccessTokenNullable
from ..types.accounts_balance_get_request_options import AccountsBalanceGetRequestOptions
from ..types.accounts_get_request_options import AccountsGetRequestOptions
from ..types.accounts_get_response import AccountsGetResponse
from ..types.ach_class import AchClass
from ..types.api_client_id import ApiClientId
from ..types.api_secret import ApiSecret
from ..types.application_get_response import ApplicationGetResponse
from ..types.application_id import ApplicationId
from ..types.asset_report_audit_copy_create_response import AssetReportAuditCopyCreateResponse
from ..types.asset_report_audit_copy_remove_response import AssetReportAuditCopyRemoveResponse
from ..types.asset_report_create_request_options import AssetReportCreateRequestOptions
from ..types.asset_report_create_response import AssetReportCreateResponse
from ..types.asset_report_filter_response import AssetReportFilterResponse
from ..types.asset_report_freddie_get_response import AssetReportFreddieGetResponse
from ..types.asset_report_get_request_options import AssetReportGetRequestOptions
from ..types.asset_report_get_response import AssetReportGetResponse
from ..types.asset_report_pdf_get_request_options import AssetReportPdfGetRequestOptions
from ..types.asset_report_refresh_asset_report_token import AssetReportRefreshAssetReportToken
from ..types.asset_report_refresh_request_options import AssetReportRefreshRequestOptions
from ..types.asset_report_refresh_response import AssetReportRefreshResponse
from ..types.asset_report_remove_response import AssetReportRemoveResponse
from ..types.asset_report_token import AssetReportToken
from ..types.auth_get_request_options import AuthGetRequestOptions
from ..types.auth_get_response import AuthGetResponse
from ..types.bank_transfer_access_token import BankTransferAccessToken
from ..types.bank_transfer_amount import BankTransferAmount
from ..types.bank_transfer_balance_get_response import BankTransferBalanceGetResponse
from ..types.bank_transfer_cancel_response import BankTransferCancelResponse
from ..types.bank_transfer_create_response import BankTransferCreateResponse
from ..types.bank_transfer_direction import BankTransferDirection
from ..types.bank_transfer_event_list_bank_transfer_type import BankTransferEventListBankTransferType
from ..types.bank_transfer_event_list_direction import BankTransferEventListDirection
from ..types.bank_transfer_event_list_response import BankTransferEventListResponse
from ..types.bank_transfer_event_sync_response import BankTransferEventSyncResponse
from ..types.bank_transfer_event_type import BankTransferEventType
from ..types.bank_transfer_failure import BankTransferFailure
from ..types.bank_transfer_get_response import BankTransferGetResponse
from ..types.bank_transfer_id import BankTransferId
from ..types.bank_transfer_idempotency_key import BankTransferIdempotencyKey
from ..types.bank_transfer_list_response import BankTransferListResponse
from ..types.bank_transfer_metadata import BankTransferMetadata
from ..types.bank_transfer_migrate_account_response import BankTransferMigrateAccountResponse
from ..types.bank_transfer_network import BankTransferNetwork
from ..types.bank_transfer_sweep_get_response import BankTransferSweepGetResponse
from ..types.bank_transfer_sweep_list_response import BankTransferSweepListResponse
from ..types.bank_transfer_type import BankTransferType
from ..types.bank_transfer_user import BankTransferUser
from ..types.categories_get_request import CategoriesGetRequest
from ..types.categories_get_response import CategoriesGetResponse
from ..types.client_provided_raw_transaction import ClientProvidedRawTransaction
from ..types.client_provided_transaction import ClientProvidedTransaction
from ..types.client_user_id import ClientUserId
from ..types.consent_payment_idempotency_key import ConsentPaymentIdempotencyKey
from ..types.country_code import CountryCode
from ..types.credit_audit_copy_token_create_response import CreditAuditCopyTokenCreateResponse
from ..types.credit_audit_copy_token_remove_response import CreditAuditCopyTokenRemoveResponse
from ..types.credit_audit_copy_token_update_response import CreditAuditCopyTokenUpdateResponse
from ..types.credit_bank_employment_get_response import CreditBankEmploymentGetResponse
from ..types.credit_bank_income_get_request_options import CreditBankIncomeGetRequestOptions
from ..types.credit_bank_income_get_response import CreditBankIncomeGetResponse
from ..types.credit_bank_income_refresh_request_options import CreditBankIncomeRefreshRequestOptions
from ..types.credit_bank_income_refresh_response import CreditBankIncomeRefreshResponse
from ..types.credit_employment_get_response import CreditEmploymentGetResponse
from ..types.credit_freddie_mac_reports_get_response import CreditFreddieMacReportsGetResponse
from ..types.credit_payroll_income_get_response import CreditPayrollIncomeGetResponse
from ..types.credit_payroll_income_precheck_response import CreditPayrollIncomePrecheckResponse
from ..types.credit_payroll_income_refresh_request_options import CreditPayrollIncomeRefreshRequestOptions
from ..types.credit_payroll_income_refresh_response import CreditPayrollIncomeRefreshResponse
from ..types.credit_relay_create_response import CreditRelayCreateResponse
from ..types.credit_relay_refresh_response import CreditRelayRefreshResponse
from ..types.credit_relay_remove_response import CreditRelayRemoveResponse
from ..types.credit_sessions_get_response import CreditSessionsGetResponse
from ..types.cursor import Cursor
from ..types.dashboard_user_get_response import DashboardUserGetResponse
from ..types.dashboard_user_id import DashboardUserId
from ..types.dashboard_user_list_response import DashboardUserListResponse
from ..types.deposit_switch_alt_create_response import DepositSwitchAltCreateResponse
from ..types.deposit_switch_create_request_options import DepositSwitchCreateRequestOptions
from ..types.deposit_switch_create_response import DepositSwitchCreateResponse
from ..types.deposit_switch_get_response import DepositSwitchGetResponse
from ..types.deposit_switch_target_account import DepositSwitchTargetAccount
from ..types.deposit_switch_target_user import DepositSwitchTargetUser
from ..types.deposit_switch_token_create_response import DepositSwitchTokenCreateResponse
from ..types.employers_search_response import EmployersSearchResponse
from ..types.employment_verification_get_response import EmploymentVerificationGetResponse
from ..types.entity_watchlist_program_id import EntityWatchlistProgramId
from ..types.entity_watchlist_screening_hit_id import EntityWatchlistScreeningHitId
from ..types.entity_watchlist_screening_id import EntityWatchlistScreeningId
from ..types.entity_watchlist_search_terms import EntityWatchlistSearchTerms
from ..types.external_payment_initiation_consent_options import ExternalPaymentInitiationConsentOptions
from ..types.external_payment_options import ExternalPaymentOptions
from ..types.external_payment_schedule_request import ExternalPaymentScheduleRequest
from ..types.fdx_hateoas_link import FdxHateoasLink
from ..types.fdx_notification_category import FdxNotificationCategory
from ..types.fdx_notification_payload import FdxNotificationPayload
from ..types.fdx_notification_priority import FdxNotificationPriority
from ..types.fdx_notification_severity import FdxNotificationSeverity
from ..types.fdx_notification_type import FdxNotificationType
from ..types.fdx_party import FdxParty
from ..types.fdx_timestamp import FdxTimestamp
from ..types.idempotency_flag import IdempotencyFlag
from ..types.identity_get_request_options import IdentityGetRequestOptions
from ..types.identity_get_response import IdentityGetResponse
from ..types.identity_match_identity_verification_id import IdentityMatchIdentityVerificationId
from ..types.identity_match_request_options import IdentityMatchRequestOptions
from ..types.identity_match_response import IdentityMatchResponse
from ..types.identity_match_user import IdentityMatchUser
from ..types.identity_verification_consent import IdentityVerificationConsent
from ..types.identity_verification_create_response import IdentityVerificationCreateResponse
from ..types.identity_verification_get_response import IdentityVerificationGetResponse
from ..types.identity_verification_id import IdentityVerificationId
from ..types.identity_verification_list_response import IdentityVerificationListResponse
from ..types.identity_verification_request_user import IdentityVerificationRequestUser
from ..types.identity_verification_retry_request_steps_object import IdentityVerificationRetryRequestStepsObject
from ..types.identity_verification_retry_response import IdentityVerificationRetryResponse
from ..types.identity_verification_template_id import IdentityVerificationTemplateId
from ..types.income_verification_create_request_options import IncomeVerificationCreateRequestOptions
from ..types.income_verification_create_response import IncomeVerificationCreateResponse
from ..types.income_verification_paystubs_get_response import IncomeVerificationPaystubsGetResponse
from ..types.income_verification_precheck_employer import IncomeVerificationPrecheckEmployer
from ..types.income_verification_precheck_military_info import IncomeVerificationPrecheckMilitaryInfo
from ..types.income_verification_precheck_payroll_institution import IncomeVerificationPrecheckPayrollInstitution
from ..types.income_verification_precheck_response import IncomeVerificationPrecheckResponse
from ..types.income_verification_precheck_user import IncomeVerificationPrecheckUser
from ..types.income_verification_taxforms_get_response import IncomeVerificationTaxformsGetResponse
from ..types.institutions_get_by_id_request_options import InstitutionsGetByIdRequestOptions
from ..types.institutions_get_by_id_response import InstitutionsGetByIdResponse
from ..types.institutions_get_request_options import InstitutionsGetRequestOptions
from ..types.institutions_get_response import InstitutionsGetResponse
from ..types.institutions_search_request_options import InstitutionsSearchRequestOptions
from ..types.institutions_search_response import InstitutionsSearchResponse
from ..types.investment_holdings_get_request_options import InvestmentHoldingsGetRequestOptions
from ..types.investments_holdings_get_response import InvestmentsHoldingsGetResponse
from ..types.investments_transactions_get_request_options import InvestmentsTransactionsGetRequestOptions
from ..types.investments_transactions_get_response import InvestmentsTransactionsGetResponse
from ..types.item_access_token_invalidate_response import ItemAccessTokenInvalidateResponse
from ..types.item_activity_list_response import ItemActivityListResponse
from ..types.item_application_list_response import ItemApplicationListResponse
from ..types.item_application_scopes_update_response import ItemApplicationScopesUpdateResponse
from ..types.item_get_response import ItemGetResponse
from ..types.item_import_request_options import ItemImportRequestOptions
from ..types.item_import_request_user_auth import ItemImportRequestUserAuth
from ..types.item_import_response import ItemImportResponse
from ..types.item_public_token_create_response import ItemPublicTokenCreateResponse
from ..types.item_public_token_exchange_response import ItemPublicTokenExchangeResponse
from ..types.item_remove_response import ItemRemoveResponse
from ..types.item_webhook_update_response import ItemWebhookUpdateResponse
from ..types.liabilities_get_request_options import LiabilitiesGetRequestOptions
from ..types.liabilities_get_response import LiabilitiesGetResponse
from ..types.link_delivery_create_response import LinkDeliveryCreateResponse
from ..types.link_delivery_get_response import LinkDeliveryGetResponse
from ..types.link_delivery_options import LinkDeliveryOptions
from ..types.link_o_auth_correlation_id_exchange_response import LinkOAuthCorrelationIdExchangeResponse
from ..types.link_token_account_filters import LinkTokenAccountFilters
from ..types.link_token_create_institution_data import LinkTokenCreateInstitutionData
from ..types.link_token_create_request_auth import LinkTokenCreateRequestAuth
from ..types.link_token_create_request_deposit_switch import LinkTokenCreateRequestDepositSwitch
from ..types.link_token_create_request_employment import LinkTokenCreateRequestEmployment
from ..types.link_token_create_request_identity_verification import LinkTokenCreateRequestIdentityVerification
from ..types.link_token_create_request_income_verification import LinkTokenCreateRequestIncomeVerification
from ..types.link_token_create_request_payment_initiation import LinkTokenCreateRequestPaymentInitiation
from ..types.link_token_create_request_transfer import LinkTokenCreateRequestTransfer
from ..types.link_token_create_request_update import LinkTokenCreateRequestUpdate
from ..types.link_token_create_request_user import LinkTokenCreateRequestUser
from ..types.link_token_create_response import LinkTokenCreateResponse
from ..types.link_token_eu_config import LinkTokenEuConfig
from ..types.link_token_get_response import LinkTokenGetResponse
from ..types.link_token_investments import LinkTokenInvestments
from ..types.partner_customer_create_response import PartnerCustomerCreateResponse
from ..types.partner_customer_enable_response import PartnerCustomerEnableResponse
from ..types.partner_customer_get_response import PartnerCustomerGetResponse
from ..types.partner_customer_o_auth_institutions_get_response import PartnerCustomerOAuthInstitutionsGetResponse
from ..types.partner_customer_remove_response import PartnerCustomerRemoveResponse
from ..types.partner_end_customer_address import PartnerEndCustomerAddress
from ..types.partner_end_customer_assets_under_management import PartnerEndCustomerAssetsUnderManagement
from ..types.partner_end_customer_billing_contact import PartnerEndCustomerBillingContact
from ..types.partner_end_customer_customer_support_info import PartnerEndCustomerCustomerSupportInfo
from ..types.partner_end_customer_technical_contact import PartnerEndCustomerTechnicalContact
from ..types.payment_amount import PaymentAmount
from ..types.payment_amount_to_refund import PaymentAmountToRefund
from ..types.payment_initiation_address import PaymentInitiationAddress
from ..types.payment_initiation_consent_constraints import PaymentInitiationConsentConstraints
from ..types.payment_initiation_consent_create_response import PaymentInitiationConsentCreateResponse
from ..types.payment_initiation_consent_get_response import PaymentInitiationConsentGetResponse
from ..types.payment_initiation_consent_payment_execute_response import PaymentInitiationConsentPaymentExecuteResponse
from ..types.payment_initiation_consent_revoke_response import PaymentInitiationConsentRevokeResponse
from ..types.payment_initiation_consent_scope import PaymentInitiationConsentScope
from ..types.payment_initiation_payment_create_response import PaymentInitiationPaymentCreateResponse
from ..types.payment_initiation_payment_get_response import PaymentInitiationPaymentGetResponse
from ..types.payment_initiation_payment_list_response import PaymentInitiationPaymentListResponse
from ..types.payment_initiation_payment_reverse_response import PaymentInitiationPaymentReverseResponse
from ..types.payment_initiation_payment_token_create_response import PaymentInitiationPaymentTokenCreateResponse
from ..types.payment_initiation_recipient_create_response import PaymentInitiationRecipientCreateResponse
from ..types.payment_initiation_recipient_get_response import PaymentInitiationRecipientGetResponse
from ..types.payment_initiation_recipient_list_response import PaymentInitiationRecipientListResponse
from ..types.payment_profile_create_response import PaymentProfileCreateResponse
from ..types.payment_profile_get_response import PaymentProfileGetResponse
from ..types.payment_profile_remove_response import PaymentProfileRemoveResponse
from ..types.payment_profile_token import PaymentProfileToken
from ..types.processor_auth_get_response import ProcessorAuthGetResponse
from ..types.processor_balance_get_request_options import ProcessorBalanceGetRequestOptions
from ..types.processor_balance_get_response import ProcessorBalanceGetResponse
from ..types.processor_bank_transfer_create_response import ProcessorBankTransferCreateResponse
from ..types.processor_identity_get_response import ProcessorIdentityGetResponse
from ..types.processor_signal_decision_report_response import ProcessorSignalDecisionReportResponse
from ..types.processor_signal_evaluate_response import ProcessorSignalEvaluateResponse
from ..types.processor_signal_return_report_response import ProcessorSignalReturnReportResponse
from ..types.processor_stripe_bank_account_token_create_response import ProcessorStripeBankAccountTokenCreateResponse
from ..types.processor_token import ProcessorToken
from ..types.processor_token_create_response import ProcessorTokenCreateResponse
from ..types.products import Products
from ..types.recipient_bacs_nullable import RecipientBacsNullable
from ..types.recurring_transfer_id import RecurringTransferId
from ..types.report_type import ReportType
from ..types.review_comment import ReviewComment
from ..types.sandbox_bank_transfer_fire_webhook_response import SandboxBankTransferFireWebhookResponse
from ..types.sandbox_bank_transfer_simulate_response import SandboxBankTransferSimulateResponse
from ..types.sandbox_income_fire_webhook_response import SandboxIncomeFireWebhookResponse
from ..types.sandbox_item_fire_webhook_response import SandboxItemFireWebhookResponse
from ..types.sandbox_item_reset_login_response import SandboxItemResetLoginResponse
from ..types.sandbox_item_set_verification_status_response import SandboxItemSetVerificationStatusResponse
from ..types.sandbox_oauth_select_accounts_response import SandboxOauthSelectAccountsResponse
from ..types.sandbox_payment_profile_reset_login_response import SandboxPaymentProfileResetLoginResponse
from ..types.sandbox_processor_token_create_request_options import SandboxProcessorTokenCreateRequestOptions
from ..types.sandbox_processor_token_create_response import SandboxProcessorTokenCreateResponse
from ..types.sandbox_public_token_create_request_options import SandboxPublicTokenCreateRequestOptions
from ..types.sandbox_public_token_create_response import SandboxPublicTokenCreateResponse
from ..types.sandbox_transfer_fire_webhook_response import SandboxTransferFireWebhookResponse
from ..types.sandbox_transfer_repayment_simulate_response import SandboxTransferRepaymentSimulateResponse
from ..types.sandbox_transfer_simulate_response import SandboxTransferSimulateResponse
from ..types.sandbox_transfer_sweep_simulate_response import SandboxTransferSweepSimulateResponse
from ..types.sandbox_transfer_test_clock_advance_response import SandboxTransferTestClockAdvanceResponse
from ..types.sandbox_transfer_test_clock_create_response import SandboxTransferTestClockCreateResponse
from ..types.sandbox_transfer_test_clock_get_response import SandboxTransferTestClockGetResponse
from ..types.sandbox_transfer_test_clock_list_response import SandboxTransferTestClockListResponse
from ..types.scopes import Scopes
from ..types.scopes_context import ScopesContext
from ..types.scopes_state import ScopesState
from ..types.signal_decision_outcome import SignalDecisionOutcome
from ..types.signal_decision_report_response import SignalDecisionReportResponse
from ..types.signal_device import SignalDevice
from ..types.signal_evaluate_response import SignalEvaluateResponse
from ..types.signal_payment_method import SignalPaymentMethod
from ..types.signal_prepare_response import SignalPrepareResponse
from ..types.signal_return_report_response import SignalReturnReportResponse
from ..types.signal_user import SignalUser
from ..types.strategy import Strategy
from ..types.transactions_enhance_get_response import TransactionsEnhanceGetResponse
from ..types.transactions_enrich_get_response import TransactionsEnrichGetResponse
from ..types.transactions_enrich_request_options import TransactionsEnrichRequestOptions
from ..types.transactions_get_request_options import TransactionsGetRequestOptions
from ..types.transactions_get_response import TransactionsGetResponse
from ..types.transactions_recurring_get_request_options import TransactionsRecurringGetRequestOptions
from ..types.transactions_recurring_get_response import TransactionsRecurringGetResponse
from ..types.transactions_refresh_response import TransactionsRefreshResponse
from ..types.transactions_rule_details import TransactionsRuleDetails
from ..types.transactions_rules_create_response import TransactionsRulesCreateResponse
from ..types.transactions_rules_list_response import TransactionsRulesListResponse
from ..types.transactions_rules_remove_response import TransactionsRulesRemoveResponse
from ..types.transactions_sync_request_options import TransactionsSyncRequestOptions
from ..types.transactions_sync_response import TransactionsSyncResponse
from ..types.transfer_access_token import TransferAccessToken
from ..types.transfer_account_id import TransferAccountId
from ..types.transfer_amount import TransferAmount
from ..types.transfer_authorization_create_response import TransferAuthorizationCreateResponse
from ..types.transfer_authorization_device import TransferAuthorizationDevice
from ..types.transfer_authorization_idempotency_key import TransferAuthorizationIdempotencyKey
from ..types.transfer_authorization_user_in_request import TransferAuthorizationUserInRequest
from ..types.transfer_cancel_response import TransferCancelResponse
from ..types.transfer_capabilities_get_response import TransferCapabilitiesGetResponse
from ..types.transfer_configuration_get_response import TransferConfigurationGetResponse
from ..types.transfer_create_idempotency_key import TransferCreateIdempotencyKey
from ..types.transfer_create_response import TransferCreateResponse
from ..types.transfer_device import TransferDevice
from ..types.transfer_event_list_response import TransferEventListResponse
from ..types.transfer_event_list_transfer_type import TransferEventListTransferType
from ..types.transfer_event_sync_response import TransferEventSyncResponse
from ..types.transfer_event_type import TransferEventType
from ..types.transfer_failure import TransferFailure
from ..types.transfer_funding_account_id_request import TransferFundingAccountIdRequest
from ..types.transfer_get_response import TransferGetResponse
from ..types.transfer_id import TransferId
from ..types.transfer_id_for_refund import TransferIdForRefund
from ..types.transfer_intent_create_mode import TransferIntentCreateMode
from ..types.transfer_intent_create_network import TransferIntentCreateNetwork
from ..types.transfer_intent_create_response import TransferIntentCreateResponse
from ..types.transfer_intent_get_response import TransferIntentGetResponse
from ..types.transfer_list_response import TransferListResponse
from ..types.transfer_metadata import TransferMetadata
from ..types.transfer_metrics_get_response import TransferMetricsGetResponse
from ..types.transfer_migrate_account_response import TransferMigrateAccountResponse
from ..types.transfer_network import TransferNetwork
from ..types.transfer_originator_create_response import TransferOriginatorCreateResponse
from ..types.transfer_originator_get_response import TransferOriginatorGetResponse
from ..types.transfer_originator_list_response import TransferOriginatorListResponse
from ..types.transfer_payment_profile_token import TransferPaymentProfileToken
from ..types.transfer_questionnaire_create_response import TransferQuestionnaireCreateResponse
from ..types.transfer_recurring_cancel_response import TransferRecurringCancelResponse
from ..types.transfer_recurring_create_response import TransferRecurringCreateResponse
from ..types.transfer_recurring_get_response import TransferRecurringGetResponse
from ..types.transfer_recurring_idempotency_key import TransferRecurringIdempotencyKey
from ..types.transfer_recurring_list_response import TransferRecurringListResponse
from ..types.transfer_recurring_schedule import TransferRecurringSchedule
from ..types.transfer_refund_amount import TransferRefundAmount
from ..types.transfer_refund_cancel_response import TransferRefundCancelResponse
from ..types.transfer_refund_create_response import TransferRefundCreateResponse
from ..types.transfer_refund_get_response import TransferRefundGetResponse
from ..types.transfer_refund_id import TransferRefundId
from ..types.transfer_refund_idempotency_key import TransferRefundIdempotencyKey
from ..types.transfer_repayment_list_response import TransferRepaymentListResponse
from ..types.transfer_repayment_return_list_response import TransferRepaymentReturnListResponse
from ..types.transfer_sweep_get_response import TransferSweepGetResponse
from ..types.transfer_sweep_list_response import TransferSweepListResponse
from ..types.transfer_test_clock_id import TransferTestClockId
from ..types.transfer_type import TransferType
from ..types.transfer_user_in_request import TransferUserInRequest
from ..types.transfer_user_in_request_deprecated import TransferUserInRequestDeprecated
from ..types.update_entity_screening_request_search_terms import UpdateEntityScreeningRequestSearchTerms
from ..types.update_individual_screening_request_search_terms import UpdateIndividualScreeningRequestSearchTerms
from ..types.user_create_response import UserCreateResponse
from ..types.user_id import UserId
from ..types.user_token import UserToken
from ..types.virtual_time import VirtualTime
from ..types.wallet_create_response import WalletCreateResponse
from ..types.wallet_get_response import WalletGetResponse
from ..types.wallet_iso_currency_code import WalletIsoCurrencyCode
from ..types.wallet_list_response import WalletListResponse
from ..types.wallet_transaction_amount import WalletTransactionAmount
from ..types.wallet_transaction_counterparty import WalletTransactionCounterparty
from ..types.wallet_transaction_execute_response import WalletTransactionExecuteResponse
from ..types.wallet_transaction_get_response import WalletTransactionGetResponse
from ..types.wallet_transaction_idempotency_key import WalletTransactionIdempotencyKey
from ..types.wallet_transaction_list_request_options import WalletTransactionListRequestOptions
from ..types.wallet_transaction_list_response import WalletTransactionListResponse
from ..types.watchlist_program_id import WatchlistProgramId
from ..types.watchlist_screening_entity_create_response import WatchlistScreeningEntityCreateResponse
from ..types.watchlist_screening_entity_get_response import WatchlistScreeningEntityGetResponse
from ..types.watchlist_screening_entity_history_list_response import WatchlistScreeningEntityHistoryListResponse
from ..types.watchlist_screening_entity_hit_list_response import WatchlistScreeningEntityHitListResponse
from ..types.watchlist_screening_entity_list_response import WatchlistScreeningEntityListResponse
from ..types.watchlist_screening_entity_program_get_response import WatchlistScreeningEntityProgramGetResponse
from ..types.watchlist_screening_entity_program_list_response import WatchlistScreeningEntityProgramListResponse
from ..types.watchlist_screening_entity_review_create_response import WatchlistScreeningEntityReviewCreateResponse
from ..types.watchlist_screening_entity_review_list_response import WatchlistScreeningEntityReviewListResponse
from ..types.watchlist_screening_entity_update_request_resettable_field_list import (
    WatchlistScreeningEntityUpdateRequestResettableFieldList,
)
from ..types.watchlist_screening_entity_update_response import WatchlistScreeningEntityUpdateResponse
from ..types.watchlist_screening_hit_id import WatchlistScreeningHitId
from ..types.watchlist_screening_individual_create_response import WatchlistScreeningIndividualCreateResponse
from ..types.watchlist_screening_individual_get_response import WatchlistScreeningIndividualGetResponse
from ..types.watchlist_screening_individual_history_list_response import WatchlistScreeningIndividualHistoryListResponse
from ..types.watchlist_screening_individual_hit_list_response import WatchlistScreeningIndividualHitListResponse
from ..types.watchlist_screening_individual_id import WatchlistScreeningIndividualId
from ..types.watchlist_screening_individual_list_response import WatchlistScreeningIndividualListResponse
from ..types.watchlist_screening_individual_program_get_response import WatchlistScreeningIndividualProgramGetResponse
from ..types.watchlist_screening_individual_program_list_response import WatchlistScreeningIndividualProgramListResponse
from ..types.watchlist_screening_individual_review_create_response import (
    WatchlistScreeningIndividualReviewCreateResponse,
)
from ..types.watchlist_screening_individual_review_list_response import WatchlistScreeningIndividualReviewListResponse
from ..types.watchlist_screening_individual_update_request_resettable_field_list import (
    WatchlistScreeningIndividualUpdateRequestResettableFieldList,
)
from ..types.watchlist_screening_individual_update_response import WatchlistScreeningIndividualUpdateResponse
from ..types.watchlist_screening_request_search_terms import WatchlistScreeningRequestSearchTerms
from ..types.watchlist_screening_status import WatchlistScreeningStatus
from ..types.webhook_type import WebhookType
from ..types.webhook_verification_key_get_response import WebhookVerificationKeyGetResponse
from .raw_client import AsyncRawPlaidClient, RawPlaidClient
from .types.deposit_switch_alt_create_request_country_code import DepositSwitchAltCreateRequestCountryCode
from .types.deposit_switch_create_request_country_code import DepositSwitchCreateRequestCountryCode
from .types.processor_token_create_request_processor import ProcessorTokenCreateRequestProcessor
from .types.sandbox_income_fire_webhook_request_verification_status import (
    SandboxIncomeFireWebhookRequestVerificationStatus,
)
from .types.sandbox_item_fire_webhook_request_webhook_code import SandboxItemFireWebhookRequestWebhookCode
from .types.sandbox_item_set_verification_status_request_verification_status import (
    SandboxItemSetVerificationStatusRequestVerificationStatus,
)


OMIT = typing.cast(typing.Any, ...)


class PlaidClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPlaidClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPlaidClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPlaidClient
        """
        return self._raw_client

    def accounts_balance_get(
        self,
        *,
        access_token: AccessToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        options: typing.Optional[AccountsBalanceGetRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountsGetResponse:
        """
        The `/accounts/balance/get` endpoint returns the real-time balance for each of an Item's accounts. While other endpoints may return a balance object, only `/accounts/balance/get` forces the available and current balance fields to be refreshed rather than cached. This endpoint can be used for existing Items that were added via any of Plaid’s other products. This endpoint can be used as long as Link has been initialized with any other product, `balance` itself is not a product that can be used to initialize Link. As this endpoint triggers a synchronous request for fresh data, latency may be higher than for other Plaid endpoints; if you encounter errors, you may find it necessary to adjust your timeout period when making requests.

        Parameters
        ----------
        access_token : AccessToken

        client_id : typing.Optional[ApiClientId]

        options : typing.Optional[AccountsBalanceGetRequestOptions]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountsGetResponse
            OK

        Examples
        --------
        from fern import AccountsBalanceGetRequestOptions, FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.accounts_balance_get(
            access_token="string",
            client_id="string",
            options=AccountsBalanceGetRequestOptions(
                account_ids=["string"],
            ),
            secret="string",
        )
        """
        _response = self._raw_client.accounts_balance_get(
            access_token=access_token,
            client_id=client_id,
            options=options,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def accounts_get(
        self,
        *,
        access_token: AccessToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        options: typing.Optional[AccountsGetRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountsGetResponse:
        """
        The `/accounts/get` endpoint can be used to retrieve a list of accounts associated with any linked Item. Plaid will only return active bank accounts — that is, accounts that are not closed and are capable of carrying a balance.
        For items that went through the updated account selection pane, this endpoint only returns accounts that were permissioned by the user when they initially created the Item. If a user creates a new account after the initial link, you can capture this event through the [`NEW_ACCOUNTS_AVAILABLE`](https://plaid.com/docs/api/items/#new_accounts_available) webhook and then use Link's [update mode](https://plaid.com/docs/link/update-mode/) to request that the user share this new account with you.

        This endpoint retrieves cached information, rather than extracting fresh information from the institution. As a result, balances returned may not be up-to-date; for realtime balance information, use `/accounts/balance/get` instead. Note that some information is nullable.

        Parameters
        ----------
        access_token : AccessToken

        client_id : typing.Optional[ApiClientId]

        options : typing.Optional[AccountsGetRequestOptions]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountsGetResponse
            success

        Examples
        --------
        from fern import AccountsGetRequestOptions, FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.accounts_get(
            access_token="string",
            client_id="string",
            options=AccountsGetRequestOptions(
                account_ids=["string"],
            ),
            secret="string",
        )
        """
        _response = self._raw_client.accounts_get(
            access_token=access_token,
            client_id=client_id,
            options=options,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def application_get(
        self,
        *,
        application_id: ApplicationId,
        client_id: ApiClientId,
        secret: ApiSecret,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApplicationGetResponse:
        """
        Allows financial institutions to retrieve information about Plaid clients for the purpose of building control-tower experiences

        Parameters
        ----------
        application_id : ApplicationId

        client_id : ApiClientId

        secret : ApiSecret

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationGetResponse
            success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.application_get(
            application_id="application_id",
            client_id="client_id",
            secret="secret",
        )
        """
        _response = self._raw_client.application_get(
            application_id=application_id, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def asset_report_audit_copy_create(
        self,
        *,
        asset_report_token: AssetReportToken,
        auditor_id: typing.Optional[str] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AssetReportAuditCopyCreateResponse:
        """
        Plaid can provide an Audit Copy of any Asset Report directly to a participating third party on your behalf. For example, Plaid can supply an Audit Copy directly to Fannie Mae on your behalf if you participate in the Day 1 Certainty™ program. An Audit Copy contains the same underlying data as the Asset Report.

        To grant access to an Audit Copy, use the `/asset_report/audit_copy/create` endpoint to create an `audit_copy_token` and then pass that token to the third party who needs access. Each third party has its own `auditor_id`, for example `fannie_mae`. You’ll need to create a separate Audit Copy for each third party to whom you want to grant access to the Report.

        Parameters
        ----------
        asset_report_token : AssetReportToken

        auditor_id : typing.Optional[str]
            The `auditor_id` of the third party with whom you would like to share the Asset Report.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AssetReportAuditCopyCreateResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.asset_report_audit_copy_create(
            asset_report_token="asset_report_token",
        )
        """
        _response = self._raw_client.asset_report_audit_copy_create(
            asset_report_token=asset_report_token,
            auditor_id=auditor_id,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def asset_report_audit_copy_get(
        self,
        *,
        audit_copy_token: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AssetReportGetResponse:
        """
        `/asset_report/audit_copy/get` allows auditors to get a copy of an Asset Report that was previously shared via the `/asset_report/audit_copy/create` endpoint.  The caller of `/asset_report/audit_copy/create` must provide the `audit_copy_token` to the auditor.  This token can then be used to call `/asset_report/audit_copy/create`.

        Parameters
        ----------
        audit_copy_token : str
            The `audit_copy_token` granting access to the Audit Copy you would like to get.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AssetReportGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.asset_report_audit_copy_get(
            audit_copy_token="audit_copy_token",
        )
        """
        _response = self._raw_client.asset_report_audit_copy_get(
            audit_copy_token=audit_copy_token, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def asset_report_audit_copy_remove(
        self,
        *,
        audit_copy_token: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AssetReportAuditCopyRemoveResponse:
        """
        The `/asset_report/audit_copy/remove` endpoint allows you to remove an Audit Copy. Removing an Audit Copy invalidates the `audit_copy_token` associated with it, meaning both you and any third parties holding the token will no longer be able to use it to access Report data. Items associated with the Asset Report, the Asset Report itself and other Audit Copies of it are not affected and will remain accessible after removing the given Audit Copy.

        Parameters
        ----------
        audit_copy_token : str
            The `audit_copy_token` granting access to the Audit Copy you would like to revoke.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AssetReportAuditCopyRemoveResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.asset_report_audit_copy_remove(
            audit_copy_token="audit_copy_token",
        )
        """
        _response = self._raw_client.asset_report_audit_copy_remove(
            audit_copy_token=audit_copy_token, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def asset_report_create(
        self,
        *,
        days_requested: int,
        access_tokens: typing.Optional[typing.Sequence[AccessToken]] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        options: typing.Optional[AssetReportCreateRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        user_token: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AssetReportCreateResponse:
        """
        The `/asset_report/create` endpoint initiates the process of creating an Asset Report, which can then be retrieved by passing the `asset_report_token` return value to the `/asset_report/get` or `/asset_report/pdf/get` endpoints.

        The Asset Report takes some time to be created and is not available immediately after calling `/asset_report/create`. When the Asset Report is ready to be retrieved using `/asset_report/get` or `/asset_report/pdf/get`, Plaid will fire a `PRODUCT_READY` webhook. For full details of the webhook schema, see [Asset Report webhooks](https://plaid.com/docs/api/products/assets/#webhooks).

        The `/asset_report/create` endpoint creates an Asset Report at a moment in time. Asset Reports are immutable. To get an updated Asset Report, use the `/asset_report/refresh` endpoint.

        Parameters
        ----------
        days_requested : int
            The maximum integer number of days of history to include in the Asset Report. If using Fannie Mae Day 1 Certainty, `days_requested` must be at least 61 for new originations or at least 31 for refinancings.

            An Asset Report requested with "Additional History" (that is, with more than 61 days of transaction history) will incur an Additional History fee.

        access_tokens : typing.Optional[typing.Sequence[AccessToken]]
            An array of access tokens corresponding to the Items that will be included in the report. The `assets` product must have been initialized for the Items during link; the Assets product cannot be added after initialization.

        client_id : typing.Optional[ApiClientId]

        options : typing.Optional[AssetReportCreateRequestOptions]

        secret : typing.Optional[ApiSecret]

        user_token : typing.Optional[str]
            The user token associated with the User for which to create an asset report for. All items associated with the User will be included in the report.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AssetReportCreateResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.asset_report_create(
            days_requested=1,
        )
        """
        _response = self._raw_client.asset_report_create(
            days_requested=days_requested,
            access_tokens=access_tokens,
            client_id=client_id,
            options=options,
            secret=secret,
            user_token=user_token,
            request_options=request_options,
        )
        return _response.data

    def asset_report_filter(
        self,
        *,
        account_ids_to_exclude: typing.Sequence[str],
        asset_report_token: AssetReportToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AssetReportFilterResponse:
        """
        By default, an Asset Report will contain all of the accounts on a given Item. In some cases, you may not want the Asset Report to contain all accounts. For example, you might have the end user choose which accounts are relevant in Link using the Account Select view, which you can enable in the dashboard. Or, you might always exclude certain account types or subtypes, which you can identify by using the `/accounts/get` endpoint. To narrow an Asset Report to only a subset of accounts, use the `/asset_report/filter` endpoint.

        To exclude certain Accounts from an Asset Report, first use the `/asset_report/create` endpoint to create the report, then send the `asset_report_token` along with a list of `account_ids` to exclude to the `/asset_report/filter` endpoint, to create a new Asset Report which contains only a subset of the original Asset Report's data.

        Because Asset Reports are immutable, calling `/asset_report/filter` does not alter the original Asset Report in any way; rather, `/asset_report/filter` creates a new Asset Report with a new token and id. Asset Reports created via `/asset_report/filter` do not contain new Asset data, and are not billed.

        Plaid will fire a [`PRODUCT_READY`](https://plaid.com/docs/api/products/assets/#product_ready) webhook once generation of the filtered Asset Report has completed.

        Parameters
        ----------
        account_ids_to_exclude : typing.Sequence[str]
            The accounts to exclude from the Asset Report, identified by `account_id`.

        asset_report_token : AssetReportToken

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AssetReportFilterResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.asset_report_filter(
            account_ids_to_exclude=["account_ids_to_exclude"],
            asset_report_token="asset_report_token",
        )
        """
        _response = self._raw_client.asset_report_filter(
            account_ids_to_exclude=account_ids_to_exclude,
            asset_report_token=asset_report_token,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def asset_report_get(
        self,
        *,
        asset_report_token: AssetReportToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        fast_report: typing.Optional[bool] = OMIT,
        include_insights: typing.Optional[bool] = OMIT,
        options: typing.Optional[AssetReportGetRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AssetReportGetResponse:
        """
        The `/asset_report/get` endpoint retrieves the Asset Report in JSON format. Before calling `/asset_report/get`, you must first create the Asset Report using `/asset_report/create` (or filter an Asset Report using `/asset_report/filter`) and then wait for the [`PRODUCT_READY`](https://plaid.com/docs/api/products/assets/#product_ready) webhook to fire, indicating that the Report is ready to be retrieved.

        By default, an Asset Report includes transaction descriptions as returned by the bank, as opposed to parsed and categorized by Plaid. You can also receive cleaned and categorized transactions, as well as additional insights like merchant name or location information. We call this an Asset Report with Insights. An Asset Report with Insights provides transaction category, location, and merchant information in addition to the transaction strings provided in a standard Asset Report.

        If report_type was set to `VERIFICATION_OF_EMPLOYMENT` when the Asset Report was created in asset_report/create, debit transactions and transaction amounts won’t be included in the report.

        To retrieve an Asset Report with Insights, call the `/asset_report/get` endpoint with `include_insights` set to `true`.

        Parameters
        ----------
        asset_report_token : AssetReportToken

        client_id : typing.Optional[ApiClientId]

        fast_report : typing.Optional[bool]
            `true` to fetch "fast" version of asset report. Defaults to false if omitted. Can only be used if `/asset_report/create` was called with `options.add_ons` set to `["fast_assets"]`.

        include_insights : typing.Optional[bool]
            `true` if you would like to retrieve the Asset Report with Insights, `false` otherwise. This field defaults to `false` if omitted.

        options : typing.Optional[AssetReportGetRequestOptions]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AssetReportGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.asset_report_get(
            asset_report_token="asset_report_token",
        )
        """
        _response = self._raw_client.asset_report_get(
            asset_report_token=asset_report_token,
            client_id=client_id,
            fast_report=fast_report,
            include_insights=include_insights,
            options=options,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def asset_report_pdf_get(
        self,
        *,
        asset_report_token: AssetReportToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        options: typing.Optional[AssetReportPdfGetRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        The `/asset_report/pdf/get` endpoint retrieves the Asset Report in PDF format. Before calling `/asset_report/pdf/get`, you must first create the Asset Report using `/asset_report/create` (or filter an Asset Report using `/asset_report/filter`) and then wait for the [`PRODUCT_READY`](https://plaid.com/docs/api/products/assets/#product_ready) webhook to fire, indicating that the Report is ready to be retrieved.

        The response to `/asset_report/pdf/get` is the PDF binary data. The `request_id`  is returned in the `Plaid-Request-ID` header.

        If report_type was set to `VERIFICATION_OF_EMPLOYMENT` when the Asset Report was created in asset_report/create, debit transactions and transaction amounts won’t be included in the report.

        [View a sample PDF Asset Report](https://plaid.com/documents/sample-asset-report.pdf).

        Parameters
        ----------
        asset_report_token : AssetReportToken

        client_id : typing.Optional[ApiClientId]

        options : typing.Optional[AssetReportPdfGetRequestOptions]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            A PDF of the Asset Report
        """
        with self._raw_client.asset_report_pdf_get(
            asset_report_token=asset_report_token,
            client_id=client_id,
            options=options,
            secret=secret,
            request_options=request_options,
        ) as r:
            yield from r.data

    def asset_report_refresh(
        self,
        *,
        asset_report_token: AssetReportRefreshAssetReportToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        days_requested: typing.Optional[int] = OMIT,
        options: typing.Optional[AssetReportRefreshRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AssetReportRefreshResponse:
        """
        An Asset Report is an immutable snapshot of a user's assets. In order to "refresh" an Asset Report you created previously, you can use the `/asset_report/refresh` endpoint to create a new Asset Report based on the old one, but with the most recent data available.

        The new Asset Report will contain the same Items as the original Report, as well as the same filters applied by any call to `/asset_report/filter`. By default, the new Asset Report will also use the same parameters you submitted with your original `/asset_report/create` request, but the original `days_requested` value and the values of any parameters in the `options` object can be overridden with new values. To change these arguments, simply supply new values for them in your request to `/asset_report/refresh`. Submit an empty string ("") for any previously-populated fields you would like set as empty.

        Parameters
        ----------
        asset_report_token : AssetReportRefreshAssetReportToken

        client_id : typing.Optional[ApiClientId]

        days_requested : typing.Optional[int]
            The maximum number of days of history to include in the Asset Report. Must be an integer. If not specified, the value from the original call to `/asset_report/create` will be used.

        options : typing.Optional[AssetReportRefreshRequestOptions]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AssetReportRefreshResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.asset_report_refresh(
            asset_report_token="asset_report_token",
        )
        """
        _response = self._raw_client.asset_report_refresh(
            asset_report_token=asset_report_token,
            client_id=client_id,
            days_requested=days_requested,
            options=options,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def asset_report_remove(
        self,
        *,
        asset_report_token: AssetReportToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AssetReportRemoveResponse:
        """
        The `/item/remove` endpoint allows you to invalidate an `access_token`, meaning you will not be able to create new Asset Reports with it. Removing an Item does not affect any Asset Reports or Audit Copies you have already created, which will remain accessible until you remove them specifically.

        The `/asset_report/remove` endpoint allows you to remove an Asset Report. Removing an Asset Report invalidates its `asset_report_token`, meaning you will no longer be able to use it to access Report data or create new Audit Copies. Removing an Asset Report does not affect the underlying Items, but does invalidate any `audit_copy_tokens` associated with the Asset Report.

        Parameters
        ----------
        asset_report_token : AssetReportToken

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AssetReportRemoveResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.asset_report_remove(
            asset_report_token="asset_report_token",
        )
        """
        _response = self._raw_client.asset_report_remove(
            asset_report_token=asset_report_token, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def auth_get(
        self,
        *,
        access_token: AccessToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        options: typing.Optional[AuthGetRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AuthGetResponse:
        """
        The `/auth/get` endpoint returns the bank account and bank identification numbers (such as routing numbers, for US accounts) associated with an Item's checking and savings accounts, along with high-level account data and balances when available.

        Note: This request may take some time to complete if `auth` was not specified as an initial product when creating the Item. This is because Plaid must communicate directly with the institution to retrieve the data.

        Versioning note: In API version 2017-03-08, the schema of the `numbers` object returned by this endpoint is substantially different. For details, see [Plaid API versioning](https://plaid.com/docs/api/versioning/#version-2018-05-22).

        Parameters
        ----------
        access_token : AccessToken

        client_id : typing.Optional[ApiClientId]

        options : typing.Optional[AuthGetRequestOptions]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthGetResponse
            success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.auth_get(
            access_token="access_token",
        )
        """
        _response = self._raw_client.auth_get(
            access_token=access_token,
            client_id=client_id,
            options=options,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def bank_transfer_balance_get(
        self,
        *,
        client_id: typing.Optional[ApiClientId] = OMIT,
        origination_account_id: typing.Optional[str] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BankTransferBalanceGetResponse:
        """
        Use the `/bank_transfer/balance/get` endpoint to see the available balance in your bank transfer account. Debit transfers increase this balance once their status is posted. Credit transfers decrease this balance when they are created.

        The transactable balance shows the amount in your account that you are able to use for transfers, and is essentially your available balance minus your minimum balance.

        Note that this endpoint can only be used with FBO accounts, when using Bank Transfers in the Full Service configuration. It cannot be used on your own account when using Bank Transfers in the BTS Platform configuration.

        Parameters
        ----------
        client_id : typing.Optional[ApiClientId]

        origination_account_id : typing.Optional[str]
            If multiple origination accounts are available, `origination_account_id` must be used to specify the account for which balance will be returned.

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BankTransferBalanceGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.bank_transfer_balance_get()
        """
        _response = self._raw_client.bank_transfer_balance_get(
            client_id=client_id,
            origination_account_id=origination_account_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def bank_transfer_cancel(
        self,
        *,
        bank_transfer_id: BankTransferId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BankTransferCancelResponse:
        """
        Use the `/bank_transfer/cancel` endpoint to cancel a bank transfer.  A transfer is eligible for cancelation if the `cancellable` property returned by `/bank_transfer/get` is `true`.

        Parameters
        ----------
        bank_transfer_id : BankTransferId

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BankTransferCancelResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.bank_transfer_cancel(
            bank_transfer_id="bank_transfer_id",
        )
        """
        _response = self._raw_client.bank_transfer_cancel(
            bank_transfer_id=bank_transfer_id, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def bank_transfer_create(
        self,
        *,
        access_token: BankTransferAccessToken,
        account_id: str,
        amount: BankTransferAmount,
        description: str,
        idempotency_key: BankTransferIdempotencyKey,
        iso_currency_code: str,
        network: BankTransferNetwork,
        type: BankTransferType,
        user: BankTransferUser,
        ach_class: typing.Optional[AchClass] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        custom_tag: typing.Optional[str] = OMIT,
        metadata: typing.Optional[BankTransferMetadata] = OMIT,
        origination_account_id: typing.Optional[str] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BankTransferCreateResponse:
        """
        Use the `/bank_transfer/create` endpoint to initiate a new bank transfer.

        Parameters
        ----------
        access_token : BankTransferAccessToken

        account_id : str
            The Plaid `account_id` for the account that will be debited or credited.

        amount : BankTransferAmount

        description : str
            The transfer description. Maximum of 10 characters.

        idempotency_key : BankTransferIdempotencyKey

        iso_currency_code : str
            The currency of the transfer amount – should be set to "USD".

        network : BankTransferNetwork

        type : BankTransferType

        user : BankTransferUser

        ach_class : typing.Optional[AchClass]

        client_id : typing.Optional[ApiClientId]

        custom_tag : typing.Optional[str]
            An arbitrary string provided by the client for storage with the bank transfer. May be up to 100 characters.

        metadata : typing.Optional[BankTransferMetadata]

        origination_account_id : typing.Optional[str]
            Plaid’s unique identifier for the origination account for this transfer. If you have more than one origination account, this value must be specified. Otherwise, this field should be left blank.

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BankTransferCreateResponse
            OK

        Examples
        --------
        from fern import BankTransferUser, FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.bank_transfer_create(
            access_token="access_token",
            account_id="account_id",
            amount="amount",
            description="description",
            idempotency_key="idempotency_key",
            iso_currency_code="iso_currency_code",
            network="ach",
            type="debit",
            user=BankTransferUser(
                legal_name="legal_name",
            ),
        )
        """
        _response = self._raw_client.bank_transfer_create(
            access_token=access_token,
            account_id=account_id,
            amount=amount,
            description=description,
            idempotency_key=idempotency_key,
            iso_currency_code=iso_currency_code,
            network=network,
            type=type,
            user=user,
            ach_class=ach_class,
            client_id=client_id,
            custom_tag=custom_tag,
            metadata=metadata,
            origination_account_id=origination_account_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def bank_transfer_event_list(
        self,
        *,
        account_id: typing.Optional[str] = OMIT,
        bank_transfer_id: typing.Optional[str] = OMIT,
        bank_transfer_type: typing.Optional[BankTransferEventListBankTransferType] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        count: typing.Optional[int] = OMIT,
        direction: typing.Optional[BankTransferEventListDirection] = OMIT,
        end_date: typing.Optional[dt.datetime] = OMIT,
        event_types: typing.Optional[typing.Sequence[BankTransferEventType]] = OMIT,
        offset: typing.Optional[int] = OMIT,
        origination_account_id: typing.Optional[str] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        start_date: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BankTransferEventListResponse:
        """
        Use the `/bank_transfer/event/list` endpoint to get a list of Plaid-initiated ACH or bank transfer events based on specified filter criteria. When using Auth with micro-deposit verification enabled, this endpoint can be used to fetch status updates on ACH micro-deposits. For more details, see [micro-deposit events](https://plaid.com/docs/auth/coverage/microdeposit-events/).

        Parameters
        ----------
        account_id : typing.Optional[str]
            The account ID to get events for all transactions to/from an account.

        bank_transfer_id : typing.Optional[str]
            Plaid’s unique identifier for a bank transfer.

        bank_transfer_type : typing.Optional[BankTransferEventListBankTransferType]

        client_id : typing.Optional[ApiClientId]

        count : typing.Optional[int]
            The maximum number of bank transfer events to return. If the number of events matching the above parameters is greater than `count`, the most recent events will be returned.

        direction : typing.Optional[BankTransferEventListDirection]

        end_date : typing.Optional[dt.datetime]
            The end datetime of bank transfers to list. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`)

        event_types : typing.Optional[typing.Sequence[BankTransferEventType]]
            Filter events by event type.

        offset : typing.Optional[int]
            The offset into the list of bank transfer events. When `count`=25 and `offset`=0, the first 25 events will be returned. When `count`=25 and `offset`=25, the next 25 bank transfer events will be returned.

        origination_account_id : typing.Optional[str]
            The origination account ID to get events for transfers from a specific origination account.

        secret : typing.Optional[ApiSecret]

        start_date : typing.Optional[dt.datetime]
            The start datetime of bank transfers to list. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BankTransferEventListResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.bank_transfer_event_list()
        """
        _response = self._raw_client.bank_transfer_event_list(
            account_id=account_id,
            bank_transfer_id=bank_transfer_id,
            bank_transfer_type=bank_transfer_type,
            client_id=client_id,
            count=count,
            direction=direction,
            end_date=end_date,
            event_types=event_types,
            offset=offset,
            origination_account_id=origination_account_id,
            secret=secret,
            start_date=start_date,
            request_options=request_options,
        )
        return _response.data

    def bank_transfer_event_sync(
        self,
        *,
        after_id: int,
        client_id: typing.Optional[ApiClientId] = OMIT,
        count: typing.Optional[int] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BankTransferEventSyncResponse:
        """
        `/bank_transfer/event/sync` allows you to request up to the next 25 Plaid-initiated bank transfer events that happened after a specific `event_id`. When using Auth with micro-deposit verification enabled, this endpoint can be used to fetch status updates on ACH micro-deposits. For more details, see [micro-deposit events](https://www.plaid.com/docs/auth/coverage/microdeposit-events/).

        Parameters
        ----------
        after_id : int
            The latest (largest) `event_id` fetched via the sync endpoint, or 0 initially.

        client_id : typing.Optional[ApiClientId]

        count : typing.Optional[int]
            The maximum number of bank transfer events to return.

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BankTransferEventSyncResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.bank_transfer_event_sync(
            after_id=1,
        )
        """
        _response = self._raw_client.bank_transfer_event_sync(
            after_id=after_id, client_id=client_id, count=count, secret=secret, request_options=request_options
        )
        return _response.data

    def bank_transfer_get(
        self,
        *,
        bank_transfer_id: BankTransferId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BankTransferGetResponse:
        """
        The `/bank_transfer/get` fetches information about the bank transfer corresponding to the given `bank_transfer_id`.

        Parameters
        ----------
        bank_transfer_id : BankTransferId

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BankTransferGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.bank_transfer_get(
            bank_transfer_id="bank_transfer_id",
        )
        """
        _response = self._raw_client.bank_transfer_get(
            bank_transfer_id=bank_transfer_id, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def bank_transfer_list(
        self,
        *,
        client_id: typing.Optional[ApiClientId] = OMIT,
        count: typing.Optional[int] = OMIT,
        direction: typing.Optional[BankTransferDirection] = OMIT,
        end_date: typing.Optional[dt.datetime] = OMIT,
        offset: typing.Optional[int] = OMIT,
        origination_account_id: typing.Optional[str] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        start_date: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BankTransferListResponse:
        """
        Use the `/bank_transfer/list` endpoint to see a list of all your bank transfers and their statuses. Results are paginated; use the `count` and `offset` query parameters to retrieve the desired bank transfers.

        Parameters
        ----------
        client_id : typing.Optional[ApiClientId]

        count : typing.Optional[int]
            The maximum number of bank transfers to return.

        direction : typing.Optional[BankTransferDirection]

        end_date : typing.Optional[dt.datetime]
            The end datetime of bank transfers to list. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`)

        offset : typing.Optional[int]
            The number of bank transfers to skip before returning results.

        origination_account_id : typing.Optional[str]
            Filter bank transfers to only those originated through the specified origination account.

        secret : typing.Optional[ApiSecret]

        start_date : typing.Optional[dt.datetime]
            The start datetime of bank transfers to list. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BankTransferListResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.bank_transfer_list()
        """
        _response = self._raw_client.bank_transfer_list(
            client_id=client_id,
            count=count,
            direction=direction,
            end_date=end_date,
            offset=offset,
            origination_account_id=origination_account_id,
            secret=secret,
            start_date=start_date,
            request_options=request_options,
        )
        return _response.data

    def bank_transfer_migrate_account(
        self,
        *,
        account_number: str,
        account_type: str,
        routing_number: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        wire_routing_number: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BankTransferMigrateAccountResponse:
        """
        As an alternative to adding Items via Link, you can also use the `/bank_transfer/migrate_account` endpoint to migrate known account and routing numbers to Plaid Items.  Note that Items created in this way are not compatible with endpoints for other products, such as `/accounts/balance/get`, and can only be used with Bank Transfer endpoints.  If you require access to other endpoints, create the Item through Link instead.  Access to `/bank_transfer/migrate_account` is not enabled by default; to obtain access, contact your Plaid Account Manager.

        Parameters
        ----------
        account_number : str
            The user's account number.

        account_type : str
            The type of the bank account (`checking` or `savings`).

        routing_number : str
            The user's routing number.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        wire_routing_number : typing.Optional[str]
            The user's wire transfer routing number. This is the ABA number; for some institutions, this may differ from the ACH number used in `routing_number`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BankTransferMigrateAccountResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.bank_transfer_migrate_account(
            account_number="account_number",
            account_type="account_type",
            routing_number="routing_number",
        )
        """
        _response = self._raw_client.bank_transfer_migrate_account(
            account_number=account_number,
            account_type=account_type,
            routing_number=routing_number,
            client_id=client_id,
            secret=secret,
            wire_routing_number=wire_routing_number,
            request_options=request_options,
        )
        return _response.data

    def bank_transfer_sweep_get(
        self,
        *,
        sweep_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BankTransferSweepGetResponse:
        """
        The `/bank_transfer/sweep/get` endpoint fetches information about the sweep corresponding to the given `sweep_id`.

        Parameters
        ----------
        sweep_id : str
            Identifier of the sweep.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BankTransferSweepGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.bank_transfer_sweep_get(
            sweep_id="sweep_id",
        )
        """
        _response = self._raw_client.bank_transfer_sweep_get(
            sweep_id=sweep_id, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def bank_transfer_sweep_list(
        self,
        *,
        client_id: typing.Optional[ApiClientId] = OMIT,
        count: typing.Optional[int] = OMIT,
        end_time: typing.Optional[dt.datetime] = OMIT,
        origination_account_id: typing.Optional[str] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        start_time: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BankTransferSweepListResponse:
        """
        The `/bank_transfer/sweep/list` endpoint fetches information about the sweeps matching the given filters.

        Parameters
        ----------
        client_id : typing.Optional[ApiClientId]

        count : typing.Optional[int]
            The maximum number of sweeps to return.

        end_time : typing.Optional[dt.datetime]
            The end datetime of sweeps to return (RFC 3339 format).

        origination_account_id : typing.Optional[str]
            If multiple origination accounts are available, `origination_account_id` must be used to specify the account that the sweeps belong to.

        secret : typing.Optional[ApiSecret]

        start_time : typing.Optional[dt.datetime]
            The start datetime of sweeps to return (RFC 3339 format).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BankTransferSweepListResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.bank_transfer_sweep_list()
        """
        _response = self._raw_client.bank_transfer_sweep_list(
            client_id=client_id,
            count=count,
            end_time=end_time,
            origination_account_id=origination_account_id,
            secret=secret,
            start_time=start_time,
            request_options=request_options,
        )
        return _response.data

    def credit_bank_employment_get(
        self,
        *,
        user_token: UserToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreditBankEmploymentGetResponse:
        """
        `/credit/bank_employment/get` returns the employment report(s) derived from bank transaction data for a specified user.

        Parameters
        ----------
        user_token : UserToken

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreditBankEmploymentGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.credit_bank_employment_get(
            user_token="user_token",
        )
        """
        _response = self._raw_client.credit_bank_employment_get(
            user_token=user_token, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def transactions_rules_create(
        self,
        *,
        access_token: AccessToken,
        personal_finance_category: str,
        rule_details: TransactionsRuleDetails,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransactionsRulesCreateResponse:
        """
        The `/transactions/rules/v1/create` endpoint creates transaction categorization rules.

        Rules will be applied on the Item's transactions returned in `/transactions/get` response.

        The product is currently in beta. To request access, contact transactions-feedback@plaid.com.

        Parameters
        ----------
        access_token : AccessToken

        personal_finance_category : str
            Personal finance detailed category.

            See the [`taxonomy csv file`](https://plaid.com/documents/transactions-personal-finance-category-taxonomy.csv) for a full list of personal finance categories.

        rule_details : TransactionsRuleDetails

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransactionsRulesCreateResponse
            OK

        Examples
        --------
        from fern import FernApi, TransactionsRuleDetails

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.transactions_rules_create(
            access_token="access-sandbox-71e02f71-0960-4a27-abd2-5631e04f2175",
            client_id="7f57eb3d2a9j6480121fx361",
            personal_finance_category="FOOD_AND_DRINK_FAST_FOOD",
            rule_details=TransactionsRuleDetails(
                field="NAME",
                query="Burger Shack",
                type="SUBSTRING_MATCH",
            ),
            secret="79g03eoofwl8240v776r2h667442119",
        )
        """
        _response = self._raw_client.transactions_rules_create(
            access_token=access_token,
            personal_finance_category=personal_finance_category,
            rule_details=rule_details,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def transactions_rules_list(
        self,
        *,
        access_token: AccessToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransactionsRulesListResponse:
        """
        The `/transactions/rules/v1/list` returns a list of transaction rules created for the Item associated with the access token.

        Parameters
        ----------
        access_token : AccessToken

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransactionsRulesListResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.transactions_rules_list(
            access_token="access-sandbox-71e02f71-0960-4a27-abd2-5631e04f2175",
            client_id="7f57eb3d2a9j6480121fx361",
            secret="79g03eoofwl8240v776r2h667442119",
        )
        """
        _response = self._raw_client.transactions_rules_list(
            access_token=access_token, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def transactions_rules_remove(
        self,
        *,
        access_token: AccessToken,
        rule_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransactionsRulesRemoveResponse:
        """
        The `/transactions/rules/v1/remove` endpoint is used to remove a transaction rule.

        Parameters
        ----------
        access_token : AccessToken

        rule_id : str
            A rule's unique identifier

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransactionsRulesRemoveResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.transactions_rules_remove(
            access_token="access-sandbox-71e02f71-0960-4a27-abd2-5631e04f2175",
            client_id="7f57eb3d2a9j6480121fx361",
            rule_id="eVBnVMp7zdTJLkRNr33Rs6zr7KNJqBF",
            secret="79g03eoofwl8240v776r2h667442119",
        )
        """
        _response = self._raw_client.transactions_rules_remove(
            access_token=access_token,
            rule_id=rule_id,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def transactions_enhance(
        self,
        *,
        account_type: str,
        transactions: typing.Sequence[ClientProvidedRawTransaction],
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransactionsEnhanceGetResponse:
        """
        The `/beta/transactions/v1/enhance` endpoint enriches raw transaction data provided directly by clients.

        The product is currently in beta.

        Parameters
        ----------
        account_type : str
            The type of account for the requested transactions (`depository` or `credit`).

        transactions : typing.Sequence[ClientProvidedRawTransaction]
            An array of raw transactions to be enhanced.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransactionsEnhanceGetResponse
            OK

        Examples
        --------
        from fern import ClientProvidedRawTransaction, FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.transactions_enhance(
            account_type="account_type",
            transactions=[
                ClientProvidedRawTransaction(
                    amount=1.1,
                    description="description",
                    id="id",
                    iso_currency_code="iso_currency_code",
                )
            ],
        )
        """
        _response = self._raw_client.transactions_enhance(
            account_type=account_type,
            transactions=transactions,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def categories_get(
        self, *, request: CategoriesGetRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> CategoriesGetResponse:
        """
        Send a request to the `/categories/get` endpoint to get detailed information on categories returned by Plaid. This endpoint does not require authentication.

        Parameters
        ----------
        request : CategoriesGetRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CategoriesGetResponse
            success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.categories_get(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.categories_get(request=request, request_options=request_options)
        return _response.data

    def credit_asset_report_freddie_mac_get(
        self,
        *,
        audit_copy_token: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AssetReportFreddieGetResponse:
        """
        The `credit/asset_report/freddie_mac/get` endpoint retrieves the Asset Report in Freddie Mac's JSON format.

        Parameters
        ----------
        audit_copy_token : str
            A token that can be shared with a third party auditor to allow them to obtain access to the Asset Report. This token should be stored securely.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AssetReportFreddieGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.credit_asset_report_freddie_mac_get(
            audit_copy_token="audit_copy_token",
        )
        """
        _response = self._raw_client.credit_asset_report_freddie_mac_get(
            audit_copy_token=audit_copy_token, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def credit_audit_copy_token_create(
        self,
        *,
        report_tokens: typing.Sequence[str],
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreditAuditCopyTokenCreateResponse:
        """
        Plaid can create an Audit Copy token of an Asset Report and/or Income Report to share with participating Government Sponsored Entity (GSE). If you participate in the Day 1 Certainty™ program, Plaid can supply an Audit Copy token directly to Fannie Mae on your behalf. An Audit Copy token contains the same underlying data as the Asset Report and/or Income Report (result of /credit/payroll_income/get).

        Use the `/credit/audit_copy_token/create` endpoint to create an `audit_copy_token` and then pass that token to the GSE who needs access.

        Parameters
        ----------
        report_tokens : typing.Sequence[str]
            List of report tokens; can include at most one VOA/standard Asset Report tokens and one VOE Asset Report Token.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreditAuditCopyTokenCreateResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.credit_audit_copy_token_create(
            report_tokens=["report_tokens"],
        )
        """
        _response = self._raw_client.credit_audit_copy_token_create(
            report_tokens=report_tokens, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def credit_report_audit_copy_remove(
        self,
        *,
        audit_copy_token: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreditAuditCopyTokenRemoveResponse:
        """
        The `/credit/audit_copy_token/remove` endpoint allows you to remove an Audit Copy. Removing an Audit Copy invalidates the `audit_copy_token` associated with it, meaning both you and any third parties holding the token will no longer be able to use it to access Report data. Items associated with the Report data and other Audit Copies of it are not affected and will remain accessible after removing the given Audit Copy.

        Parameters
        ----------
        audit_copy_token : str
            The `audit_copy_token` granting access to the Audit Copy you would like to revoke.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreditAuditCopyTokenRemoveResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.credit_report_audit_copy_remove(
            audit_copy_token="audit_copy_token",
        )
        """
        _response = self._raw_client.credit_report_audit_copy_remove(
            audit_copy_token=audit_copy_token, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def credit_audit_copy_token_update(
        self,
        *,
        audit_copy_token: str,
        report_tokens: typing.Sequence[AssetReportToken],
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreditAuditCopyTokenUpdateResponse:
        """
        The `/credit/audit_copy_token/update` endpoint updates an existing  Audit Copy Token by adding the report tokens in the `report_tokens` field to the `audit_copy_token`. If the Audit Copy Token already contains a report of a certain type, it will be replaced with the token provided in the `report_tokens` field.

        Parameters
        ----------
        audit_copy_token : str
            The `audit_copy_token` you would like to update.

        report_tokens : typing.Sequence[AssetReportToken]
            Array of tokens which the specified Audit Copy Token will be updated with. The types of token supported are asset report token and employment report token. There can be at most 1 of each token type in the array.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreditAuditCopyTokenUpdateResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.credit_audit_copy_token_update(
            audit_copy_token="audit_copy_token",
            report_tokens=["report_tokens"],
        )
        """
        _response = self._raw_client.credit_audit_copy_token_update(
            audit_copy_token=audit_copy_token,
            report_tokens=report_tokens,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def credit_bank_income_get(
        self,
        *,
        client_id: typing.Optional[ApiClientId] = OMIT,
        options: typing.Optional[CreditBankIncomeGetRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        user_token: typing.Optional[UserToken] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreditBankIncomeGetResponse:
        """
        `/credit/bank_income/get` returns the bank income report(s) for a specified user.

        Parameters
        ----------
        client_id : typing.Optional[ApiClientId]

        options : typing.Optional[CreditBankIncomeGetRequestOptions]

        secret : typing.Optional[ApiSecret]

        user_token : typing.Optional[UserToken]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreditBankIncomeGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.credit_bank_income_get()
        """
        _response = self._raw_client.credit_bank_income_get(
            client_id=client_id, options=options, secret=secret, user_token=user_token, request_options=request_options
        )
        return _response.data

    def credit_bank_income_pdf_get(
        self,
        *,
        user_token: UserToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        `/credit/bank_income/pdf/get` returns the most recent bank income report for a specified user in PDF format.

        Parameters
        ----------
        user_token : UserToken

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            A PDF of the Bank Income Report
        """
        with self._raw_client.credit_bank_income_pdf_get(
            user_token=user_token, client_id=client_id, secret=secret, request_options=request_options
        ) as r:
            yield from r.data

    def credit_bank_income_refresh(
        self,
        *,
        user_token: UserToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        options: typing.Optional[CreditBankIncomeRefreshRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreditBankIncomeRefreshResponse:
        """
        `/credit/bank_income/refresh` refreshes the bank income report data for a specific user.

        Parameters
        ----------
        user_token : UserToken

        client_id : typing.Optional[ApiClientId]

        options : typing.Optional[CreditBankIncomeRefreshRequestOptions]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreditBankIncomeRefreshResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.credit_bank_income_refresh(
            user_token="user_token",
        )
        """
        _response = self._raw_client.credit_bank_income_refresh(
            user_token=user_token, client_id=client_id, options=options, secret=secret, request_options=request_options
        )
        return _response.data

    def credit_employment_get(
        self,
        *,
        user_token: UserToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreditEmploymentGetResponse:
        """
        `/credit/employment/get` returns a list of items with employment information from a user's payroll provider that was verified by an end user.

        Parameters
        ----------
        user_token : UserToken

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreditEmploymentGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.credit_employment_get(
            user_token="user_token",
        )
        """
        _response = self._raw_client.credit_employment_get(
            user_token=user_token, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def credit_freddie_mac_reports_get(
        self,
        *,
        audit_copy_token: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreditFreddieMacReportsGetResponse:
        """
        The `credit/asset_report/freddie_mac/get` endpoint retrieves the Verification of Assets and Verification of Employment reports.

        Parameters
        ----------
        audit_copy_token : str
            A token that can be shared with a third party auditor to allow them to obtain access to the Asset Report. This token should be stored securely.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreditFreddieMacReportsGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.credit_freddie_mac_reports_get(
            audit_copy_token="audit_copy_token",
        )
        """
        _response = self._raw_client.credit_freddie_mac_reports_get(
            audit_copy_token=audit_copy_token, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def credit_payroll_income_get(
        self,
        *,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        user_token: typing.Optional[UserToken] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreditPayrollIncomeGetResponse:
        """
        This endpoint gets payroll income information for a specific user, either as a result of the user connecting to their payroll provider or uploading a pay related document.

        Parameters
        ----------
        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        user_token : typing.Optional[UserToken]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreditPayrollIncomeGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.credit_payroll_income_get()
        """
        _response = self._raw_client.credit_payroll_income_get(
            client_id=client_id, secret=secret, user_token=user_token, request_options=request_options
        )
        return _response.data

    def credit_payroll_income_precheck(
        self,
        *,
        access_tokens: typing.Optional[typing.Sequence[AccessToken]] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        employer: typing.Optional[IncomeVerificationPrecheckEmployer] = OMIT,
        payroll_institution: typing.Optional[IncomeVerificationPrecheckPayrollInstitution] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        us_military_info: typing.Optional[IncomeVerificationPrecheckMilitaryInfo] = OMIT,
        user_token: typing.Optional[UserToken] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreditPayrollIncomePrecheckResponse:
        """
        `/credit/payroll_income/precheck` is an optional endpoint that can be called before initializing a Link session for income verification. It evaluates whether a given user is supportable by digital income verification. If the user is eligible for digital verification, that information will be associated with the user token, and in this way will generate a Link UI optimized for the end user and their specific employer. If the user cannot be confirmed as eligible, the user can still use the income verification flow, but they may be required to manually upload a paystub to verify their income.

        While all request fields are optional, providing `employer` data will increase the chance of receiving a useful result.

        When testing in Sandbox, you can control the results by providing special test values in the `employer` and `access_tokens` fields. `employer_good` and `employer_bad` will result in `HIGH` and `LOW` confidence values, respectively. `employer_multi` will result in a `HIGH` confidence with multiple payroll options. Likewise, `access_good` and `access_bad` will result in `HIGH` and `LOW` confidence values, respectively. Any other value for `employer` and `access_tokens` in Sandbox will result in `UNKNOWN` confidence.

        Parameters
        ----------
        access_tokens : typing.Optional[typing.Sequence[AccessToken]]
            An array of access tokens corresponding to Items belonging to the user whose eligibility is being checked. Note that if the Items specified here are not already initialized with `transactions`, providing them in this field will cause these Items to be initialized with (and billed for) the Transactions product.

        client_id : typing.Optional[ApiClientId]

        employer : typing.Optional[IncomeVerificationPrecheckEmployer]

        payroll_institution : typing.Optional[IncomeVerificationPrecheckPayrollInstitution]

        secret : typing.Optional[ApiSecret]

        us_military_info : typing.Optional[IncomeVerificationPrecheckMilitaryInfo]

        user_token : typing.Optional[UserToken]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreditPayrollIncomePrecheckResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.credit_payroll_income_precheck()
        """
        _response = self._raw_client.credit_payroll_income_precheck(
            access_tokens=access_tokens,
            client_id=client_id,
            employer=employer,
            payroll_institution=payroll_institution,
            secret=secret,
            us_military_info=us_military_info,
            user_token=user_token,
            request_options=request_options,
        )
        return _response.data

    def credit_payroll_income_refresh(
        self,
        *,
        user_token: UserToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        options: typing.Optional[CreditPayrollIncomeRefreshRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreditPayrollIncomeRefreshResponse:
        """
        `/credit/payroll_income/refresh` refreshes a given digital payroll income verification.

        Parameters
        ----------
        user_token : UserToken

        client_id : typing.Optional[ApiClientId]

        options : typing.Optional[CreditPayrollIncomeRefreshRequestOptions]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreditPayrollIncomeRefreshResponse
            success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.credit_payroll_income_refresh(
            user_token="user_token",
        )
        """
        _response = self._raw_client.credit_payroll_income_refresh(
            user_token=user_token, client_id=client_id, options=options, secret=secret, request_options=request_options
        )
        return _response.data

    def credit_relay_create(
        self,
        *,
        report_tokens: typing.Sequence[str],
        secondary_client_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        webhook: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreditRelayCreateResponse:
        """
        Plaid can share an Asset Report directly with a participating third party on your behalf. The shared Asset Report is the exact same Asset Report originally created in `/asset_report/create`.

        To grant a third party access to an Asset Report, use the `/credit/relay/create` endpoint to create a `relay_token` and then pass that token to your third party. Each third party has its own `secondary_client_id`; for example, `ce5bd328dcd34123456`. You'll need to create a separate `relay_token` for each third party that needs access to the report on your behalf.

        Parameters
        ----------
        report_tokens : typing.Sequence[str]
            List of report token strings, with at most one token of each report type. Currently only Asset Report token is supported.

        secondary_client_id : str
            The `secondary_client_id` is the client id of the third party with whom you would like to share the relay token.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        webhook : typing.Optional[str]
            URL to which Plaid will send webhooks when the Secondary Client successfully retrieves an Asset Report by calling `/credit/relay/get`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreditRelayCreateResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.credit_relay_create(
            report_tokens=["report_tokens"],
            secondary_client_id="secondary_client_id",
        )
        """
        _response = self._raw_client.credit_relay_create(
            report_tokens=report_tokens,
            secondary_client_id=secondary_client_id,
            client_id=client_id,
            secret=secret,
            webhook=webhook,
            request_options=request_options,
        )
        return _response.data

    def credit_relay_get(
        self,
        *,
        relay_token: str,
        report_type: ReportType,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AssetReportGetResponse:
        """
        `/credit/relay/get` allows third parties to receive a report that was shared with them, using a `relay_token` that was created by the report owner.

        Parameters
        ----------
        relay_token : str
            The `relay_token` granting access to the report you would like to get.

        report_type : ReportType

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AssetReportGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.credit_relay_get(
            relay_token="relay_token",
            report_type="assets",
        )
        """
        _response = self._raw_client.credit_relay_get(
            relay_token=relay_token,
            report_type=report_type,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def credit_relay_refresh(
        self,
        *,
        relay_token: str,
        report_type: ReportType,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        webhook: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreditRelayRefreshResponse:
        """
        The `/credit/relay/refresh` endpoint allows third parties to refresh a report that was relayed to them, using a `relay_token` that was created by the report owner. A new report will be created with the original report parameters, but with the most recent data available based on the `days_requested` value of the original report.

        Parameters
        ----------
        relay_token : str
            The `relay_token` granting access to the report you would like to refresh.

        report_type : ReportType

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        webhook : typing.Optional[str]
            The URL registered to receive webhooks when the report of a relay token has been refreshed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreditRelayRefreshResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.credit_relay_refresh(
            relay_token="relay_token",
            report_type="assets",
        )
        """
        _response = self._raw_client.credit_relay_refresh(
            relay_token=relay_token,
            report_type=report_type,
            client_id=client_id,
            secret=secret,
            webhook=webhook,
            request_options=request_options,
        )
        return _response.data

    def credit_relay_remove(
        self,
        *,
        relay_token: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreditRelayRemoveResponse:
        """
        The `/credit/relay/remove` endpoint allows you to invalidate a `relay_token`. The third party holding the token will no longer be able to access or refresh the reports which the `relay_token` gives access to. The original report, associated Items, and other relay tokens that provide access to the same report are not affected and will remain accessible after removing the given `relay_token`.

        Parameters
        ----------
        relay_token : str
            The `relay_token` you would like to revoke.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreditRelayRemoveResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.credit_relay_remove(
            relay_token="relay_token",
        )
        """
        _response = self._raw_client.credit_relay_remove(
            relay_token=relay_token, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def credit_sessions_get(
        self,
        *,
        user_token: UserToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreditSessionsGetResponse:
        """
        This endpoint can be used for your end users after they complete the Link flow. This endpoint returns a list of Link sessions that your user completed, where each session includes the results from the Link flow.

        These results include details about the Item that was created and some product related metadata (showing, for example, whether the user finished the bank income verification step).

        Parameters
        ----------
        user_token : UserToken

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreditSessionsGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.credit_sessions_get(
            user_token="user_token",
        )
        """
        _response = self._raw_client.credit_sessions_get(
            user_token=user_token, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def dashboard_user_get(
        self,
        *,
        dashboard_user_id: DashboardUserId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DashboardUserGetResponse:
        """
        Retrieve information about a dashboard user.

        Parameters
        ----------
        dashboard_user_id : DashboardUserId

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DashboardUserGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.dashboard_user_get(
            dashboard_user_id="54350110fedcbaf01234ffee",
        )
        """
        _response = self._raw_client.dashboard_user_get(
            dashboard_user_id=dashboard_user_id, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def dashboard_user_list(
        self,
        *,
        client_id: typing.Optional[ApiClientId] = OMIT,
        cursor: typing.Optional[Cursor] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DashboardUserListResponse:
        """
        List all dashboard users associated with your account.

        Parameters
        ----------
        client_id : typing.Optional[ApiClientId]

        cursor : typing.Optional[Cursor]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DashboardUserListResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.dashboard_user_list()
        """
        _response = self._raw_client.dashboard_user_list(
            client_id=client_id, cursor=cursor, secret=secret, request_options=request_options
        )
        return _response.data

    def deposit_switch_alt_create(
        self,
        *,
        target_account: DepositSwitchTargetAccount,
        target_user: DepositSwitchTargetUser,
        client_id: typing.Optional[ApiClientId] = OMIT,
        country_code: typing.Optional[DepositSwitchAltCreateRequestCountryCode] = OMIT,
        options: typing.Optional[DepositSwitchCreateRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DepositSwitchAltCreateResponse:
        """
        This endpoint provides an alternative to `/deposit_switch/create` for customers who have not yet fully integrated with Plaid Exchange. Like `/deposit_switch/create`, it creates a deposit switch entity that will be persisted throughout the lifecycle of the switch.

        Parameters
        ----------
        target_account : DepositSwitchTargetAccount

        target_user : DepositSwitchTargetUser

        client_id : typing.Optional[ApiClientId]

        country_code : typing.Optional[DepositSwitchAltCreateRequestCountryCode]
            ISO-3166-1 alpha-2 country code standard.

        options : typing.Optional[DepositSwitchCreateRequestOptions]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DepositSwitchAltCreateResponse
            OK

        Examples
        --------
        from fern import DepositSwitchTargetAccount, DepositSwitchTargetUser, FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.deposit_switch_alt_create(
            target_account=DepositSwitchTargetAccount(
                account_name="account_name",
                account_number="account_number",
                account_subtype="checking",
                routing_number="routing_number",
            ),
            target_user=DepositSwitchTargetUser(
                email="email",
                family_name="family_name",
                given_name="given_name",
                phone="phone",
            ),
        )
        """
        _response = self._raw_client.deposit_switch_alt_create(
            target_account=target_account,
            target_user=target_user,
            client_id=client_id,
            country_code=country_code,
            options=options,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def deposit_switch_create(
        self,
        *,
        target_access_token: str,
        target_account_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        country_code: typing.Optional[DepositSwitchCreateRequestCountryCode] = OMIT,
        options: typing.Optional[DepositSwitchCreateRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DepositSwitchCreateResponse:
        """
        This endpoint creates a deposit switch entity that will be persisted throughout the lifecycle of the switch.

        Parameters
        ----------
        target_access_token : str
            Access token for the target Item, typically provided in the Import Item response.

        target_account_id : str
            Plaid Account ID that specifies the target bank account. This account will become the recipient for a user's direct deposit.

        client_id : typing.Optional[ApiClientId]

        country_code : typing.Optional[DepositSwitchCreateRequestCountryCode]
            ISO-3166-1 alpha-2 country code standard.

        options : typing.Optional[DepositSwitchCreateRequestOptions]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DepositSwitchCreateResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.deposit_switch_create(
            target_access_token="target_access_token",
            target_account_id="target_account_id",
        )
        """
        _response = self._raw_client.deposit_switch_create(
            target_access_token=target_access_token,
            target_account_id=target_account_id,
            client_id=client_id,
            country_code=country_code,
            options=options,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def deposit_switch_get(
        self,
        *,
        deposit_switch_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DepositSwitchGetResponse:
        """
        This endpoint returns information related to how the user has configured their payroll allocation and the state of the switch. You can use this information to build logic related to the user's direct deposit allocation preferences.

        Parameters
        ----------
        deposit_switch_id : str
            The ID of the deposit switch

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DepositSwitchGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.deposit_switch_get(
            deposit_switch_id="deposit_switch_id",
        )
        """
        _response = self._raw_client.deposit_switch_get(
            deposit_switch_id=deposit_switch_id, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def deposit_switch_token_create(
        self,
        *,
        deposit_switch_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DepositSwitchTokenCreateResponse:
        """
        In order for the end user to take action, you will need to create a public token representing the deposit switch. This token is used to initialize Link. It can be used one time and expires after 30 minutes.

        Parameters
        ----------
        deposit_switch_id : str
            The ID of the deposit switch

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DepositSwitchTokenCreateResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.deposit_switch_token_create(
            deposit_switch_id="deposit_switch_id",
        )
        """
        _response = self._raw_client.deposit_switch_token_create(
            deposit_switch_id=deposit_switch_id, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def employers_search(
        self,
        *,
        products: typing.Sequence[str],
        query: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EmployersSearchResponse:
        """
        `/employers/search` allows you the ability to search Plaid’s database of known employers, for use with Deposit Switch. You can use this endpoint to look up a user's employer in order to confirm that they are supported. Users with non-supported employers can then be routed out of the Deposit Switch flow.

        The data in the employer database is currently limited. As the Deposit Switch and Income products progress through their respective beta periods, more employers are being regularly added. Because the employer database is frequently updated, we recommend that you do not cache or store data from this endpoint for more than a day.

        Parameters
        ----------
        products : typing.Sequence[str]
            The Plaid products the returned employers should support. Currently, this field must be set to `"deposit_switch"`.

        query : str
            The employer name to be searched for.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmployersSearchResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.employers_search(
            products=["products"],
            query="query",
        )
        """
        _response = self._raw_client.employers_search(
            products=products, query=query, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def employment_verification_get(
        self,
        *,
        access_token: AccessToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EmploymentVerificationGetResponse:
        """
        `/employment/verification/get` returns a list of employments through a user payroll that was verified by an end user.

        This endpoint has been deprecated; new integrations should use `/credit/employment/get` instead.

        Parameters
        ----------
        access_token : AccessToken

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmploymentVerificationGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.employment_verification_get(
            access_token="access_token",
        )
        """
        _response = self._raw_client.employment_verification_get(
            access_token=access_token, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def fdx_notifications(
        self,
        *,
        category: FdxNotificationCategory,
        notification_id: str,
        notification_payload: FdxNotificationPayload,
        publisher: FdxParty,
        sent_on: FdxTimestamp,
        type: FdxNotificationType,
        priority: typing.Optional[FdxNotificationPriority] = OMIT,
        severity: typing.Optional[FdxNotificationSeverity] = OMIT,
        subscriber: typing.Optional[FdxParty] = OMIT,
        url: typing.Optional[FdxHateoasLink] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        A generic webhook receiver endpoint for FDX Event Notifications

        Parameters
        ----------
        category : FdxNotificationCategory

        notification_id : str
            Id of notification

        notification_payload : FdxNotificationPayload

        publisher : FdxParty

        sent_on : FdxTimestamp

        type : FdxNotificationType

        priority : typing.Optional[FdxNotificationPriority]

        severity : typing.Optional[FdxNotificationSeverity]

        subscriber : typing.Optional[FdxParty]

        url : typing.Optional[FdxHateoasLink]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import datetime

        from fern import FdxNotificationPayload, FdxParty, FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.fdx_notifications(
            category="SECURITY",
            notification_id="notificationId",
            notification_payload=FdxNotificationPayload(),
            publisher=FdxParty(
                name="name",
                type="DATA_ACCESS_PLATFORM",
            ),
            sent_on=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            type="CONSENT_REVOKED",
        )
        """
        _response = self._raw_client.fdx_notifications(
            category=category,
            notification_id=notification_id,
            notification_payload=notification_payload,
            publisher=publisher,
            sent_on=sent_on,
            type=type,
            priority=priority,
            severity=severity,
            subscriber=subscriber,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def identity_get(
        self,
        *,
        access_token: AccessToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        options: typing.Optional[IdentityGetRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IdentityGetResponse:
        """
        The `/identity/get` endpoint allows you to retrieve various account holder information on file with the financial institution, including names, emails, phone numbers, and addresses. Only name data is guaranteed to be returned; other fields will be empty arrays if not provided by the institution.

        This request may take some time to complete if identity was not specified as an initial product when creating the Item. This is because Plaid must communicate directly with the institution to retrieve the data.

        Note: In API versions 2018-05-22 and earlier, the `owners` object is not returned, and instead identity information is returned in the top level `identity` object. For more details, see [Plaid API versioning](https://plaid.com/docs/api/versioning/#version-2019-05-29).

        Parameters
        ----------
        access_token : AccessToken

        client_id : typing.Optional[ApiClientId]

        options : typing.Optional[IdentityGetRequestOptions]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IdentityGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.identity_get(
            access_token="access_token",
        )
        """
        _response = self._raw_client.identity_get(
            access_token=access_token,
            client_id=client_id,
            options=options,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def identity_match(
        self,
        *,
        access_token: AccessToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        identity_verification_id: typing.Optional[IdentityMatchIdentityVerificationId] = OMIT,
        options: typing.Optional[IdentityMatchRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        user: typing.Optional[IdentityMatchUser] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IdentityMatchResponse:
        """
        The `/identity/match` endpoint generates a match score, which indicates how well the provided identity data matches the identity information on file with the account holder's financial institution.

        This request may take some time to complete if Identity was not specified as an initial product when creating the Item. This is because Plaid must communicate directly with the institution to retrieve the data.

        Parameters
        ----------
        access_token : AccessToken

        client_id : typing.Optional[ApiClientId]

        identity_verification_id : typing.Optional[IdentityMatchIdentityVerificationId]

        options : typing.Optional[IdentityMatchRequestOptions]

        secret : typing.Optional[ApiSecret]

        user : typing.Optional[IdentityMatchUser]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IdentityMatchResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.identity_match(
            access_token="access_token",
        )
        """
        _response = self._raw_client.identity_match(
            access_token=access_token,
            client_id=client_id,
            identity_verification_id=identity_verification_id,
            options=options,
            secret=secret,
            user=user,
            request_options=request_options,
        )
        return _response.data

    def identity_verification_create(
        self,
        *,
        gave_consent: IdentityVerificationConsent,
        is_shareable: bool,
        template_id: IdentityVerificationTemplateId,
        user: IdentityVerificationRequestUser,
        client_id: typing.Optional[ApiClientId] = OMIT,
        is_idempotent: typing.Optional[IdempotencyFlag] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IdentityVerificationCreateResponse:
        """
        Create a new Identity Verification for the user specified by the `client_user_id` field. The requirements and behavior of the verification are determined by the `template_id` provided.
        If you don't know whether the associated user already has an active Identity Verification, you can specify `"is_idempotent": true` in the request body. With idempotency enabled, a new Identity Verification will only be created if one does not already exist for the associated `client_user_id` and `template_id`. If an Identity Verification is found, it will be returned unmodified with an `200 OK` HTTP status code.

        Parameters
        ----------
        gave_consent : IdentityVerificationConsent

        is_shareable : bool
            A flag specifying whether you would like Plaid to expose a shareable URL for the verification being created.

        template_id : IdentityVerificationTemplateId

        user : IdentityVerificationRequestUser

        client_id : typing.Optional[ApiClientId]

        is_idempotent : typing.Optional[IdempotencyFlag]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IdentityVerificationCreateResponse
            OK

        Examples
        --------
        from fern import FernApi, IdentityVerificationRequestUser

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.identity_verification_create(
            gave_consent=True,
            is_shareable=True,
            template_id="idvtmp_4FrXJvfQU3zGUR",
            user=IdentityVerificationRequestUser(
                client_user_id="your-db-id-3b24110",
            ),
        )
        """
        _response = self._raw_client.identity_verification_create(
            gave_consent=gave_consent,
            is_shareable=is_shareable,
            template_id=template_id,
            user=user,
            client_id=client_id,
            is_idempotent=is_idempotent,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def identity_verification_get(
        self,
        *,
        identity_verification_id: IdentityVerificationId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IdentityVerificationGetResponse:
        """
        Retrieve a previously created identity verification.

        Parameters
        ----------
        identity_verification_id : IdentityVerificationId

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IdentityVerificationGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.identity_verification_get(
            identity_verification_id="idv_52xR9LKo77r1Np",
        )
        """
        _response = self._raw_client.identity_verification_get(
            identity_verification_id=identity_verification_id,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def identity_verification_list(
        self,
        *,
        client_user_id: ClientUserId,
        template_id: IdentityVerificationTemplateId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        cursor: typing.Optional[Cursor] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IdentityVerificationListResponse:
        """
        Filter and list Identity Verifications created by your account

        Parameters
        ----------
        client_user_id : ClientUserId

        template_id : IdentityVerificationTemplateId

        client_id : typing.Optional[ApiClientId]

        cursor : typing.Optional[Cursor]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IdentityVerificationListResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.identity_verification_list(
            client_user_id="your-db-id-3b24110",
            template_id="idvtmp_4FrXJvfQU3zGUR",
        )
        """
        _response = self._raw_client.identity_verification_list(
            client_user_id=client_user_id,
            template_id=template_id,
            client_id=client_id,
            cursor=cursor,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def identity_verification_retry(
        self,
        *,
        client_user_id: ClientUserId,
        strategy: Strategy,
        template_id: IdentityVerificationTemplateId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        steps: typing.Optional[IdentityVerificationRetryRequestStepsObject] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IdentityVerificationRetryResponse:
        """
        Allow a customer to retry their identity verification

        Parameters
        ----------
        client_user_id : ClientUserId

        strategy : Strategy

        template_id : IdentityVerificationTemplateId

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        steps : typing.Optional[IdentityVerificationRetryRequestStepsObject]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IdentityVerificationRetryResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.identity_verification_retry(
            client_user_id="your-db-id-3b24110",
            strategy="reset",
            template_id="idvtmp_4FrXJvfQU3zGUR",
        )
        """
        _response = self._raw_client.identity_verification_retry(
            client_user_id=client_user_id,
            strategy=strategy,
            template_id=template_id,
            client_id=client_id,
            secret=secret,
            steps=steps,
            request_options=request_options,
        )
        return _response.data

    def income_verification_create(
        self,
        *,
        webhook: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        options: typing.Optional[IncomeVerificationCreateRequestOptions] = OMIT,
        precheck_id: typing.Optional[str] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IncomeVerificationCreateResponse:
        """
        `/income/verification/create` begins the income verification process by returning an `income_verification_id`. You can then provide the `income_verification_id` to `/link/token/create` under the `income_verification` parameter in order to create a Link instance that will prompt the user to go through the income verification flow. Plaid will fire an `INCOME` webhook once the user completes the Payroll Income flow, or when the uploaded documents in the Document Income flow have finished processing.

        Parameters
        ----------
        webhook : str
            The URL endpoint to which Plaid should send webhooks related to the progress of the income verification process.

        client_id : typing.Optional[ApiClientId]

        options : typing.Optional[IncomeVerificationCreateRequestOptions]

        precheck_id : typing.Optional[str]
            The ID of a precheck created with `/income/verification/precheck`. Will be used to improve conversion of the income verification flow.

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IncomeVerificationCreateResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.income_verification_create(
            webhook="webhook",
        )
        """
        _response = self._raw_client.income_verification_create(
            webhook=webhook,
            client_id=client_id,
            options=options,
            precheck_id=precheck_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def income_verification_documents_download(
        self,
        *,
        access_token: typing.Optional[AccessTokenNullable] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        document_id: typing.Optional[str] = OMIT,
        income_verification_id: typing.Optional[str] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        `/income/verification/documents/download` provides the ability to download the source documents associated with the verification.

        If Document Income was used, the documents will be those the user provided in Link. For Payroll Income, the most recent files available
        for download from the payroll provider will be available from this endpoint.

        The response to `/income/verification/documents/download` is a ZIP file in binary data. If a `document_id` is passed, a single document will be contained in this file.
        If not, the response will contain all documents associated with the verification.

        The `request_id` is returned in the `Plaid-Request-ID` header.

        Parameters
        ----------
        access_token : typing.Optional[AccessTokenNullable]

        client_id : typing.Optional[ApiClientId]

        document_id : typing.Optional[str]
            The document ID to download. If passed, a single document will be returned in the resulting zip file, rather than all document

        income_verification_id : typing.Optional[str]
            The ID of the verification.

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            A ZIP file containing source documents(s) used as the basis for income verification.
        """
        with self._raw_client.income_verification_documents_download(
            access_token=access_token,
            client_id=client_id,
            document_id=document_id,
            income_verification_id=income_verification_id,
            secret=secret,
            request_options=request_options,
        ) as r:
            yield from r.data

    def income_verification_paystubs_get(
        self,
        *,
        access_token: typing.Optional[AccessTokenNullable] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        income_verification_id: typing.Optional[str] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IncomeVerificationPaystubsGetResponse:
        """
        `/income/verification/paystubs/get` returns the information collected from the paystubs that were used to verify an end user's income. It can be called once the status of the verification has been set to `VERIFICATION_STATUS_PROCESSING_COMPLETE`, as reported by the `INCOME: verification_status` webhook. Attempting to call the endpoint before verification has been completed will result in an error.

        This endpoint has been deprecated; new integrations should use `/credit/payroll_income/get` instead.

        Parameters
        ----------
        access_token : typing.Optional[AccessTokenNullable]

        client_id : typing.Optional[ApiClientId]

        income_verification_id : typing.Optional[str]
            The ID of the verification for which to get paystub information.

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IncomeVerificationPaystubsGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.income_verification_paystubs_get()
        """
        _response = self._raw_client.income_verification_paystubs_get(
            access_token=access_token,
            client_id=client_id,
            income_verification_id=income_verification_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def income_verification_precheck(
        self,
        *,
        client_id: typing.Optional[ApiClientId] = OMIT,
        employer: typing.Optional[IncomeVerificationPrecheckEmployer] = OMIT,
        payroll_institution: typing.Optional[IncomeVerificationPrecheckPayrollInstitution] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        transactions_access_token: typing.Optional[AccessTokenNullable] = OMIT,
        transactions_access_tokens: typing.Optional[typing.Sequence[AccessToken]] = OMIT,
        us_military_info: typing.Optional[IncomeVerificationPrecheckMilitaryInfo] = OMIT,
        user: typing.Optional[IncomeVerificationPrecheckUser] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IncomeVerificationPrecheckResponse:
        """
        `/income/verification/precheck` is an optional endpoint that can be called before initializing a Link session for income verification. It evaluates whether a given user is supportable by digital income verification and returns a `precheck_id` that can be provided to `/link/token/create`. If the user is eligible for digital verification, providing the `precheck_id` in this way will generate a Link UI optimized for the end user and their specific employer. If the user cannot be confirmed as eligible, the `precheck_id` can still be provided to `/link/token/create` and the user can still use the income verification flow, but they may be required to manually upload a paystub to verify their income.

        While all request fields are optional, providing either `employer` or `transactions_access_tokens` data will increase the chance of receiving a useful result.

        This endpoint has been deprecated; new integrations should use `/credit/payroll_income/precheck` instead.

        Parameters
        ----------
        client_id : typing.Optional[ApiClientId]

        employer : typing.Optional[IncomeVerificationPrecheckEmployer]

        payroll_institution : typing.Optional[IncomeVerificationPrecheckPayrollInstitution]

        secret : typing.Optional[ApiSecret]

        transactions_access_token : typing.Optional[AccessTokenNullable]

        transactions_access_tokens : typing.Optional[typing.Sequence[AccessToken]]
            An array of access tokens corresponding to Items belonging to the user whose eligibility is being checked. Note that if the Items specified here are not already initialized with `transactions`, providing them in this field will cause these Items to be initialized with (and billed for) the Transactions product.

        us_military_info : typing.Optional[IncomeVerificationPrecheckMilitaryInfo]

        user : typing.Optional[IncomeVerificationPrecheckUser]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IncomeVerificationPrecheckResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.income_verification_precheck()
        """
        _response = self._raw_client.income_verification_precheck(
            client_id=client_id,
            employer=employer,
            payroll_institution=payroll_institution,
            secret=secret,
            transactions_access_token=transactions_access_token,
            transactions_access_tokens=transactions_access_tokens,
            us_military_info=us_military_info,
            user=user,
            request_options=request_options,
        )
        return _response.data

    def income_verification_taxforms_get(
        self,
        *,
        access_token: typing.Optional[AccessTokenNullable] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        income_verification_id: typing.Optional[str] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IncomeVerificationTaxformsGetResponse:
        """
        `/income/verification/taxforms/get` returns the information collected from forms that were used to verify an end user''s income. It can be called once the status of the verification has been set to `VERIFICATION_STATUS_PROCESSING_COMPLETE`, as reported by the `INCOME: verification_status` webhook. Attempting to call the endpoint before verification has been completed will result in an error.

        This endpoint has been deprecated; new integrations should use `/credit/payroll_income/get` instead.

        Parameters
        ----------
        access_token : typing.Optional[AccessTokenNullable]

        client_id : typing.Optional[ApiClientId]

        income_verification_id : typing.Optional[str]
            The ID of the verification.

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IncomeVerificationTaxformsGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.income_verification_taxforms_get()
        """
        _response = self._raw_client.income_verification_taxforms_get(
            access_token=access_token,
            client_id=client_id,
            income_verification_id=income_verification_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def institutions_get(
        self,
        *,
        count: int,
        country_codes: typing.Sequence[CountryCode],
        offset: int,
        client_id: typing.Optional[ApiClientId] = OMIT,
        options: typing.Optional[InstitutionsGetRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InstitutionsGetResponse:
        """
        Returns a JSON response containing details on all financial institutions currently supported by Plaid. Because Plaid supports thousands of institutions, results are paginated.

        If there is no overlap between an institution’s enabled products and a client’s enabled products, then the institution will be filtered out from the response. As a result, the number of institutions returned may not match the count specified in the call.

        Parameters
        ----------
        count : int
            The total number of Institutions to return.

        country_codes : typing.Sequence[CountryCode]
            Specify an array of Plaid-supported country codes this institution supports, using the ISO-3166-1 alpha-2 country code standard.

            In API versions 2019-05-29 and earlier, the `country_codes` parameter is an optional parameter within the `options` object and will default to `[US]` if it is not supplied.

        offset : int
            The number of Institutions to skip.

        client_id : typing.Optional[ApiClientId]

        options : typing.Optional[InstitutionsGetRequestOptions]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InstitutionsGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.institutions_get(
            count=1,
            country_codes=["US"],
            offset=1,
        )
        """
        _response = self._raw_client.institutions_get(
            count=count,
            country_codes=country_codes,
            offset=offset,
            client_id=client_id,
            options=options,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def institutions_get_by_id(
        self,
        *,
        country_codes: typing.Sequence[CountryCode],
        institution_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        options: typing.Optional[InstitutionsGetByIdRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InstitutionsGetByIdResponse:
        """
        Returns a JSON response containing details on a specified financial institution currently supported by Plaid.

        Versioning note: API versions 2019-05-29 and earlier allow use of the `public_key` parameter instead of the `client_id` and `secret` to authenticate to this endpoint. The `public_key` has been deprecated; all customers are encouraged to use `client_id` and `secret` instead.

        Parameters
        ----------
        country_codes : typing.Sequence[CountryCode]
            Specify an array of Plaid-supported country codes this institution supports, using the ISO-3166-1 alpha-2 country code standard. In API versions 2019-05-29 and earlier, the `country_codes` parameter is an optional parameter within the `options` object and will default to `[US]` if it is not supplied.

        institution_id : str
            The ID of the institution to get details about

        client_id : typing.Optional[ApiClientId]

        options : typing.Optional[InstitutionsGetByIdRequestOptions]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InstitutionsGetByIdResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.institutions_get_by_id(
            country_codes=["US"],
            institution_id="institution_id",
        )
        """
        _response = self._raw_client.institutions_get_by_id(
            country_codes=country_codes,
            institution_id=institution_id,
            client_id=client_id,
            options=options,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def institutions_search(
        self,
        *,
        country_codes: typing.Sequence[CountryCode],
        query: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        options: typing.Optional[InstitutionsSearchRequestOptions] = OMIT,
        products: typing.Optional[typing.Sequence[Products]] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InstitutionsSearchResponse:
        """
        Returns a JSON response containing details for institutions that match the query parameters, up to a maximum of ten institutions per query.

        Versioning note: API versions 2019-05-29 and earlier allow use of the `public_key` parameter instead of the `client_id` and `secret` parameters to authenticate to this endpoint. The `public_key` parameter has since been deprecated; all customers are encouraged to use `client_id` and `secret` instead.

        Parameters
        ----------
        country_codes : typing.Sequence[CountryCode]
            Specify an array of Plaid-supported country codes this institution supports, using the ISO-3166-1 alpha-2 country code standard. In API versions 2019-05-29 and earlier, the `country_codes` parameter is an optional parameter within the `options` object and will default to `[US]` if it is not supplied.

        query : str
            The search query. Institutions with names matching the query are returned

        client_id : typing.Optional[ApiClientId]

        options : typing.Optional[InstitutionsSearchRequestOptions]

        products : typing.Optional[typing.Sequence[Products]]
            Filter the Institutions based on whether they support all products listed in `products`. Provide `null` to get institutions regardless of supported products. Note that when `auth` is specified as a product, if you are enabled for Instant Match or Automated Micro-deposits, institutions that support those products will be returned even if `auth` is not present in their product array.

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InstitutionsSearchResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.institutions_search(
            country_codes=["US"],
            query="query",
        )
        """
        _response = self._raw_client.institutions_search(
            country_codes=country_codes,
            query=query,
            client_id=client_id,
            options=options,
            products=products,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def investments_holdings_get(
        self,
        *,
        access_token: AccessToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        options: typing.Optional[InvestmentHoldingsGetRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InvestmentsHoldingsGetResponse:
        """
        The `/investments/holdings/get` endpoint allows developers to receive user-authorized stock position data for `investment`-type accounts.

        Parameters
        ----------
        access_token : AccessToken

        client_id : typing.Optional[ApiClientId]

        options : typing.Optional[InvestmentHoldingsGetRequestOptions]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InvestmentsHoldingsGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.investments_holdings_get(
            access_token="access_token",
        )
        """
        _response = self._raw_client.investments_holdings_get(
            access_token=access_token,
            client_id=client_id,
            options=options,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def investments_transactions_get(
        self,
        *,
        access_token: AccessToken,
        end_date: dt.date,
        start_date: dt.date,
        client_id: typing.Optional[ApiClientId] = OMIT,
        options: typing.Optional[InvestmentsTransactionsGetRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InvestmentsTransactionsGetResponse:
        """
        The `/investments/transactions/get` endpoint allows developers to retrieve up to 24 months of user-authorized transaction data for investment accounts.

        Transactions are returned in reverse-chronological order, and the sequence of transaction ordering is stable and will not shift.

        Due to the potentially large number of investment transactions associated with an Item, results are paginated. Manipulate the count and offset parameters in conjunction with the `total_investment_transactions` response body field to fetch all available investment transactions.

        Note that Investments does not have a webhook to indicate when initial transaction data has loaded. Instead, if transactions data is not ready when `/investments/transactions/get` is first called, Plaid will wait for the data. For this reason, calling `/investments/transactions/get` immediately after Link may take up to one to two minutes to return.

        Parameters
        ----------
        access_token : AccessToken

        end_date : dt.date
            The most recent date for which to fetch transaction history. Dates should be formatted as YYYY-MM-DD.

        start_date : dt.date
            The earliest date for which to fetch transaction history. Dates should be formatted as YYYY-MM-DD.

        client_id : typing.Optional[ApiClientId]

        options : typing.Optional[InvestmentsTransactionsGetRequestOptions]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InvestmentsTransactionsGetResponse
            OK

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.investments_transactions_get(
            access_token="access_token",
            end_date=datetime.date.fromisoformat(
                "2023-01-15",
            ),
            start_date=datetime.date.fromisoformat(
                "2023-01-15",
            ),
        )
        """
        _response = self._raw_client.investments_transactions_get(
            access_token=access_token,
            end_date=end_date,
            start_date=start_date,
            client_id=client_id,
            options=options,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def item_access_token_invalidate(
        self,
        *,
        access_token: AccessToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ItemAccessTokenInvalidateResponse:
        """
        By default, the `access_token` associated with an Item does not expire and should be stored in a persistent, secure manner.

        You can use the `/item/access_token/invalidate` endpoint to rotate the `access_token` associated with an Item. The endpoint returns a new `access_token` and immediately invalidates the previous `access_token`.

        Parameters
        ----------
        access_token : AccessToken

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ItemAccessTokenInvalidateResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.item_access_token_invalidate(
            access_token="access_token",
        )
        """
        _response = self._raw_client.item_access_token_invalidate(
            access_token=access_token, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def item_activity_list(
        self,
        *,
        access_token: typing.Optional[AccessToken] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        count: typing.Optional[int] = OMIT,
        cursor: typing.Optional[str] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ItemActivityListResponse:
        """
        List a historical log of user consent events

        Parameters
        ----------
        access_token : typing.Optional[AccessToken]

        client_id : typing.Optional[ApiClientId]

        count : typing.Optional[int]

        cursor : typing.Optional[str]
            Cursor used for pagination.

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ItemActivityListResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.item_activity_list()
        """
        _response = self._raw_client.item_activity_list(
            access_token=access_token,
            client_id=client_id,
            count=count,
            cursor=cursor,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def item_application_list(
        self,
        *,
        access_token: typing.Optional[AccessTokenNullable] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ItemApplicationListResponse:
        """
        List a user’s connected applications

        Parameters
        ----------
        access_token : typing.Optional[AccessTokenNullable]

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ItemApplicationListResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.item_application_list()
        """
        _response = self._raw_client.item_application_list(
            access_token=access_token, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def item_application_scopes_update(
        self,
        *,
        access_token: AccessToken,
        application_id: ApplicationId,
        context: ScopesContext,
        scopes: Scopes,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        state: typing.Optional[ScopesState] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ItemApplicationScopesUpdateResponse:
        """
        Enable consumers to update product access on selected accounts for an application.

        Parameters
        ----------
        access_token : AccessToken

        application_id : ApplicationId

        context : ScopesContext

        scopes : Scopes

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        state : typing.Optional[ScopesState]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ItemApplicationScopesUpdateResponse
            success

        Examples
        --------
        from fern import FernApi, Scopes

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.item_application_scopes_update(
            access_token="access_token",
            application_id="application_id",
            context="ENROLLMENT",
            scopes=Scopes(),
        )
        """
        _response = self._raw_client.item_application_scopes_update(
            access_token=access_token,
            application_id=application_id,
            context=context,
            scopes=scopes,
            client_id=client_id,
            secret=secret,
            state=state,
            request_options=request_options,
        )
        return _response.data

    def item_get(
        self,
        *,
        access_token: AccessToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ItemGetResponse:
        """
        Returns information about the status of an Item.

        Parameters
        ----------
        access_token : AccessToken

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ItemGetResponse
            success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.item_get(
            access_token="access_token",
        )
        """
        _response = self._raw_client.item_get(
            access_token=access_token, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def item_import(
        self,
        *,
        products: typing.Sequence[Products],
        user_auth: ItemImportRequestUserAuth,
        client_id: typing.Optional[ApiClientId] = OMIT,
        options: typing.Optional[ItemImportRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ItemImportResponse:
        """
        `/item/import` creates an Item via your Plaid Exchange Integration and returns an `access_token`. As part of an `/item/import` request, you will include a User ID (`user_auth.user_id`) and Authentication Token (`user_auth.auth_token`) that enable data aggregation through your Plaid Exchange API endpoints. These authentication principals are to be chosen by you.

        Upon creating an Item via `/item/import`, Plaid will automatically begin an extraction of that Item through the Plaid Exchange infrastructure you have already integrated. This will automatically generate the Plaid native account ID for the account the user will switch their direct deposit to (`target_account_id`).

        Parameters
        ----------
        products : typing.Sequence[Products]
            Array of product strings

        user_auth : ItemImportRequestUserAuth

        client_id : typing.Optional[ApiClientId]

        options : typing.Optional[ItemImportRequestOptions]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ItemImportResponse
            OK

        Examples
        --------
        from fern import FernApi, ItemImportRequestUserAuth

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.item_import(
            products=["assets"],
            user_auth=ItemImportRequestUserAuth(
                auth_token="auth_token",
                user_id="user_id",
            ),
        )
        """
        _response = self._raw_client.item_import(
            products=products,
            user_auth=user_auth,
            client_id=client_id,
            options=options,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def item_create_public_token(
        self,
        *,
        access_token: AccessToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ItemPublicTokenCreateResponse:
        """
        Note: As of July 2020, the `/item/public_token/create` endpoint is deprecated. Instead, use `/link/token/create` with an `access_token` to create a Link token for use with [update mode](https://plaid.com/docs/link/update-mode).

        If you need your user to take action to restore or resolve an error associated with an Item, generate a public token with the `/item/public_token/create` endpoint and then initialize Link with that `public_token`.

        A `public_token` is one-time use and expires after 30 minutes. You use a `public_token` to initialize Link in [update mode](https://plaid.com/docs/link/update-mode) for a particular Item. You can generate a `public_token` for an Item even if you did not use Link to create the Item originally.

        The `/item/public_token/create` endpoint is **not** used to create your initial `public_token`. If you have not already received an `access_token` for a specific Item, use Link to obtain your `public_token` instead. See the [Quickstart](https://plaid.com/docs/quickstart) for more information.

        Parameters
        ----------
        access_token : AccessToken

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ItemPublicTokenCreateResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.item_create_public_token(
            access_token="access_token",
        )
        """
        _response = self._raw_client.item_create_public_token(
            access_token=access_token, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def item_public_token_exchange(
        self,
        *,
        public_token: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ItemPublicTokenExchangeResponse:
        """
        Exchange a Link `public_token` for an API `access_token`. Link hands off the `public_token` client-side via the `onSuccess` callback once a user has successfully created an Item. The `public_token` is ephemeral and expires after 30 minutes. An `access_token` does not expire, but can be revoked by calling `/item/remove`.

        The response also includes an `item_id` that should be stored with the `access_token`. The `item_id` is used to identify an Item in a webhook. The `item_id` can also be retrieved by making an `/item/get` request.

        Parameters
        ----------
        public_token : str
            Your `public_token`, obtained from the Link `onSuccess` callback or `/sandbox/item/public_token/create`.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ItemPublicTokenExchangeResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.item_public_token_exchange(
            public_token="public_token",
        )
        """
        _response = self._raw_client.item_public_token_exchange(
            public_token=public_token, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def item_remove(
        self,
        *,
        access_token: AccessToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ItemRemoveResponse:
        """
        The `/item/remove` endpoint allows you to remove an Item. Once removed, the `access_token`, as well as any processor tokens or bank account tokens associated with the Item, is no longer valid and cannot be used to access any data that was associated with the Item.

        Note that in the Development environment, issuing an `/item/remove`  request will not decrement your live credential count. To increase your credential account in Development, contact Support.

        Also note that for certain OAuth-based institutions, an Item removed via `/item/remove` may still show as an active connection in the institution's OAuth permission manager.

        API versions 2019-05-29 and earlier return a `removed` boolean as part of the response.

        Parameters
        ----------
        access_token : AccessToken

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ItemRemoveResponse
            success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.item_remove(
            access_token="access_token",
        )
        """
        _response = self._raw_client.item_remove(
            access_token=access_token, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def item_webhook_update(
        self,
        *,
        access_token: AccessToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        webhook: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ItemWebhookUpdateResponse:
        """
        The POST `/item/webhook/update` allows you to update the webhook URL associated with an Item. This request triggers a [`WEBHOOK_UPDATE_ACKNOWLEDGED`](https://plaid.com/docs/api/items/#webhook_update_acknowledged) webhook to the newly specified webhook URL.

        Parameters
        ----------
        access_token : AccessToken

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        webhook : typing.Optional[str]
            The new webhook URL to associate with the Item. To remove a webhook from an Item, set to `null`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ItemWebhookUpdateResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.item_webhook_update(
            access_token="access_token",
        )
        """
        _response = self._raw_client.item_webhook_update(
            access_token=access_token,
            client_id=client_id,
            secret=secret,
            webhook=webhook,
            request_options=request_options,
        )
        return _response.data

    def liabilities_get(
        self,
        *,
        access_token: AccessToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        options: typing.Optional[LiabilitiesGetRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LiabilitiesGetResponse:
        """
        The `/liabilities/get` endpoint returns various details about an Item with loan or credit accounts. Liabilities data is available primarily for US financial institutions, with some limited coverage of Canadian institutions. Currently supported account types are account type `credit` with account subtype `credit card` or `paypal`, and account type `loan` with account subtype `student` or `mortgage`. To limit accounts listed in Link to types and subtypes supported by Liabilities, you can use the `account_filters` parameter when [creating a Link token](https://plaid.com/docs/api/tokens/#linktokencreate).

        The types of information returned by Liabilities can include balances and due dates, loan terms, and account details such as original loan amount and guarantor. Data is refreshed approximately once per day; the latest data can be retrieved by calling `/liabilities/get`.

        Note: This request may take some time to complete if `liabilities` was not specified as an initial product when creating the Item. This is because Plaid must communicate directly with the institution to retrieve the additional data.

        Parameters
        ----------
        access_token : AccessToken

        client_id : typing.Optional[ApiClientId]

        options : typing.Optional[LiabilitiesGetRequestOptions]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LiabilitiesGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.liabilities_get(
            access_token="access_token",
        )
        """
        _response = self._raw_client.liabilities_get(
            access_token=access_token,
            client_id=client_id,
            options=options,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def link_oauth_correlation_id_exchange(
        self,
        *,
        link_correlation_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LinkOAuthCorrelationIdExchangeResponse:
        """
        Exchange an OAuth `link_correlation_id` for the corresponding `link_token`. The `link_correlation_id` is only available for 'payment_initiation' products and is provided to the client via the OAuth `redirect_uri` as a query parameter.
        The `link_correlation_id` is ephemeral and expires in a brief period, after which it can no longer be exchanged for the 'link_token'.

        Parameters
        ----------
        link_correlation_id : str
            A `link_correlation_id` from a received OAuth redirect URI callback

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LinkOAuthCorrelationIdExchangeResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.link_oauth_correlation_id_exchange(
            link_correlation_id="link_correlation_id",
        )
        """
        _response = self._raw_client.link_oauth_correlation_id_exchange(
            link_correlation_id=link_correlation_id, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def link_token_create(
        self,
        *,
        client_name: str,
        country_codes: typing.Sequence[CountryCode],
        language: str,
        user: LinkTokenCreateRequestUser,
        access_token: typing.Optional[str] = OMIT,
        account_filters: typing.Optional[LinkTokenAccountFilters] = OMIT,
        additional_consented_products: typing.Optional[typing.Sequence[Products]] = OMIT,
        android_package_name: typing.Optional[str] = OMIT,
        auth: typing.Optional[LinkTokenCreateRequestAuth] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        deposit_switch: typing.Optional[LinkTokenCreateRequestDepositSwitch] = OMIT,
        employment: typing.Optional[LinkTokenCreateRequestEmployment] = OMIT,
        eu_config: typing.Optional[LinkTokenEuConfig] = OMIT,
        identity_verification: typing.Optional[LinkTokenCreateRequestIdentityVerification] = OMIT,
        income_verification: typing.Optional[LinkTokenCreateRequestIncomeVerification] = OMIT,
        institution_data: typing.Optional[LinkTokenCreateInstitutionData] = OMIT,
        institution_id: typing.Optional[str] = OMIT,
        investments: typing.Optional[LinkTokenInvestments] = OMIT,
        link_customization_name: typing.Optional[str] = OMIT,
        payment_initiation: typing.Optional[LinkTokenCreateRequestPaymentInitiation] = OMIT,
        products: typing.Optional[typing.Sequence[Products]] = OMIT,
        redirect_uri: typing.Optional[str] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        transfer: typing.Optional[LinkTokenCreateRequestTransfer] = OMIT,
        update: typing.Optional[LinkTokenCreateRequestUpdate] = OMIT,
        user_token: typing.Optional[str] = OMIT,
        webhook: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LinkTokenCreateResponse:
        """
        The `/link/token/create` endpoint creates a `link_token`, which is required as a parameter when initializing Link. Once Link has been initialized, it returns a `public_token`, which can then be exchanged for an `access_token` via `/item/public_token/exchange` as part of the main Link flow.

        A `link_token` generated by `/link/token/create` is also used to initialize other Link flows, such as the update mode flow for tokens with expired credentials, or the Payment Initiation (Europe) flow.

        Parameters
        ----------
        client_name : str
            The name of your application, as it should be displayed in Link. Maximum length of 30 characters. If a value longer than 30 characters is provided, Link will display "This Application" instead.

        country_codes : typing.Sequence[CountryCode]
            Specify an array of Plaid-supported country codes using the ISO-3166-1 alpha-2 country code standard. Institutions from all listed countries will be shown. For a complete mapping of supported products by country, see https://plaid.com/global/.

            If Link is launched with multiple country codes, only products that you are enabled for in all countries will be used by Link. Note that while all countries are enabled by default in Sandbox and Development, in Production only US and Canada are enabled by default. Access to European institutions requires additional compliance steps. To request access to European institutions in the Production environment, [file a product access Support ticket](https://dashboard.plaid.com/support/new/product-and-development/product-troubleshooting/request-product-access) via the Plaid dashboard. If you initialize with a European country code, your users will see the European consent panel during the Link flow.

            If using a Link customization, make sure the country codes in the customization match those specified in `country_codes`, or the customization may not be applied.

            If using the Auth features Instant Match, Same-day Micro-deposits, or Automated Micro-deposits, `country_codes` must be set to `['US']`.

        language : str
            The language that Link should be displayed in. When initializing with Identity Verification, this field is not used; for more details, see [Identity Verification supported languages](https://www.plaid.com/docs/identity-verification/#supported-languages).

            Supported languages are:
            - Danish (`'da'`)
            - Dutch (`'nl'`)
            - English (`'en'`)
            - Estonian (`'et'`)
            - French (`'fr'`)
            - German (`'de'`)
            - Italian (`'it'`)
            - Latvian (`'lv'`)
            - Lithuanian (`'lt'`)
            - Norwegian (`'no'`)
            - Polish (`'pl'`)
            - Portuguese (`'pt'`)
            - Romanian (`'ro'`)
            - Spanish (`'es'`)
            - Swedish (`'se'`)

            When using a Link customization, the language configured here must match the setting in the customization, or the customization will not be applied.

        user : LinkTokenCreateRequestUser

        access_token : typing.Optional[str]
            The `access_token` associated with the Item to update or reference, used when updating, modifying, or accessing an existing `access_token`. Used when launching Link in update mode, when completing the Same-day (manual) Micro-deposit flow, or (optionally) when initializing Link for a returning user as part of the Transfer UI flow.

        account_filters : typing.Optional[LinkTokenAccountFilters]

        additional_consented_products : typing.Optional[typing.Sequence[Products]]
            (Beta) This field has no effect unless you are participating in the Product Scope Transparency beta program.
            List of additional Plaid product(s) you wish to collect consent for. These products will not be billed until you start using them by calling the relevant endpoints.

            `balance` is *not* a valid value, the Balance product does not require explicit initialization and will automatically have consent collected.

            Institutions that do not support these products will still be shown in Link

        android_package_name : typing.Optional[str]
            The name of your app's Android package. Required if using the `link_token` to initialize Link on Android. Any package name specified here must also be added to the Allowed Android package names setting on the [developer dashboard](https://dashboard.plaid.com/team/api). When creating a `link_token` for initializing Link on other platforms, `android_package_name` must be left blank and `redirect_uri` should be used instead.

        auth : typing.Optional[LinkTokenCreateRequestAuth]

        client_id : typing.Optional[ApiClientId]

        deposit_switch : typing.Optional[LinkTokenCreateRequestDepositSwitch]

        employment : typing.Optional[LinkTokenCreateRequestEmployment]

        eu_config : typing.Optional[LinkTokenEuConfig]

        identity_verification : typing.Optional[LinkTokenCreateRequestIdentityVerification]

        income_verification : typing.Optional[LinkTokenCreateRequestIncomeVerification]

        institution_data : typing.Optional[LinkTokenCreateInstitutionData]

        institution_id : typing.Optional[str]
            Used for certain Europe-only configurations, as well as certain legacy use cases in other regions.

        investments : typing.Optional[LinkTokenInvestments]

        link_customization_name : typing.Optional[str]
            The name of the Link customization from the Plaid Dashboard to be applied to Link. If not specified, the `default` customization will be used. When using a Link customization, the language in the customization must match the language selected via the `language` parameter, and the countries in the customization should match the country codes selected via `country_codes`.

        payment_initiation : typing.Optional[LinkTokenCreateRequestPaymentInitiation]

        products : typing.Optional[typing.Sequence[Products]]
            List of Plaid product(s) you wish to use. If launching Link in update mode, should be omitted (unless you are using update mode to add Income or Assets to an Item); required otherwise.

            `balance` is *not* a valid value, the Balance product does not require explicit initialization and will automatically be initialized when any other product is initialized.

            The products specified here will determine which institutions will be available to your users in Link. Only institutions that support *all* requested products can be selected; a if a user attempts to select an institution that does not support a listed product, a "Connectivity not supported" error message will appear in Link. To maximize the number of institutions available, initialize Link with the minimal product set required for your use case. Additional products can be added after Link initialization by calling the relevant endpoints. For details and exceptions, see [Choosing when to initialize products](https://plaid.com/docs/link/initializing-products/).

            Note that, unless you have opted to disable Instant Match support, institutions that support Instant Match will also be shown in Link if `auth` is specified as a product, even though these institutions do not contain `auth` in their product array.

            In Production, you will be billed for each product that you specify when initializing Link. Note that a product cannot be removed from an Item once the Item has been initialized with that product. To stop billing on an Item for subscription-based products, such as Liabilities, Investments, and Transactions, remove the Item via `/item/remove`.

        redirect_uri : typing.Optional[str]
            A URI indicating the destination where a user should be forwarded after completing the Link flow; used to support OAuth authentication flows when launching Link in the browser or via a webview. The `redirect_uri` should not contain any query parameters. When used in Production or Development, must be an https URI. To specify any subdomain, use `*` as a wildcard character, e.g. `https://*.example.com/oauth.html`. Note that any redirect URI must also be added to the Allowed redirect URIs list in the [developer dashboard](https://dashboard.plaid.com/team/api). If initializing on Android, `android_package_name` must be specified instead and `redirect_uri` should be left blank.

        secret : typing.Optional[ApiSecret]

        transfer : typing.Optional[LinkTokenCreateRequestTransfer]

        update : typing.Optional[LinkTokenCreateRequestUpdate]

        user_token : typing.Optional[str]
            A user token generated using `/user/create`. Any Item created during the Link session will be associated with the user.

        webhook : typing.Optional[str]
            The destination URL to which any webhooks should be sent. Note that webhooks for Payment Initiation (e-wallet transactions only), Transfer, Bank Transfer (including Auth micro-deposit notification webhooks) and Identity Verification are configured via the Dashboard instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LinkTokenCreateResponse
            OK

        Examples
        --------
        from fern import FernApi, LinkTokenCreateRequestUser

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.link_token_create(
            client_name="client_name",
            country_codes=["US"],
            language="language",
            user=LinkTokenCreateRequestUser(
                client_user_id="client_user_id",
            ),
        )
        """
        _response = self._raw_client.link_token_create(
            client_name=client_name,
            country_codes=country_codes,
            language=language,
            user=user,
            access_token=access_token,
            account_filters=account_filters,
            additional_consented_products=additional_consented_products,
            android_package_name=android_package_name,
            auth=auth,
            client_id=client_id,
            deposit_switch=deposit_switch,
            employment=employment,
            eu_config=eu_config,
            identity_verification=identity_verification,
            income_verification=income_verification,
            institution_data=institution_data,
            institution_id=institution_id,
            investments=investments,
            link_customization_name=link_customization_name,
            payment_initiation=payment_initiation,
            products=products,
            redirect_uri=redirect_uri,
            secret=secret,
            transfer=transfer,
            update=update,
            user_token=user_token,
            webhook=webhook,
            request_options=request_options,
        )
        return _response.data

    def link_token_get(
        self,
        *,
        link_token: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LinkTokenGetResponse:
        """
        The `/link/token/get` endpoint gets information about a previously-created `link_token` using the
        `/link/token/create` endpoint. It can be useful for debugging purposes.

        Parameters
        ----------
        link_token : str
            A `link_token` from a previous invocation of `/link/token/create`

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LinkTokenGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.link_token_get(
            link_token="link_token",
        )
        """
        _response = self._raw_client.link_token_get(
            link_token=link_token, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def link_delivery_create(
        self,
        *,
        link_token: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        options: typing.Optional[LinkDeliveryOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LinkDeliveryCreateResponse:
        """
        Use the `/link_delivery/create` endpoint to create a Link Delivery session.

        Parameters
        ----------
        link_token : str
            A `link_token` from a previous invocation of `/link/token/create` with Link Delivery enabled.

        client_id : typing.Optional[ApiClientId]

        options : typing.Optional[LinkDeliveryOptions]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LinkDeliveryCreateResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.link_delivery_create(
            link_token="link_token",
        )
        """
        _response = self._raw_client.link_delivery_create(
            link_token=link_token, client_id=client_id, options=options, secret=secret, request_options=request_options
        )
        return _response.data

    def link_delivery_get(
        self,
        *,
        link_delivery_session_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LinkDeliveryGetResponse:
        """
        Use the `/link_delivery/get` endpoint to get the status of a Link Delivery session.

        Parameters
        ----------
        link_delivery_session_id : str
            The ID for the Link Delivery session from a previous invocation of `/link_delivery/create`.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LinkDeliveryGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.link_delivery_get(
            link_delivery_session_id="link_delivery_session_id",
        )
        """
        _response = self._raw_client.link_delivery_get(
            link_delivery_session_id=link_delivery_session_id,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def partner_customer_create(
        self,
        *,
        address: PartnerEndCustomerAddress,
        application_name: str,
        company_name: str,
        is_bank_addendum_completed: bool,
        is_diligence_attested: bool,
        legal_entity_name: str,
        products: typing.Sequence[Products],
        website: str,
        assets_under_management: typing.Optional[PartnerEndCustomerAssetsUnderManagement] = OMIT,
        billing_contact: typing.Optional[PartnerEndCustomerBillingContact] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        create_link_customization: typing.Optional[bool] = OMIT,
        customer_support_info: typing.Optional[PartnerEndCustomerCustomerSupportInfo] = OMIT,
        logo: typing.Optional[str] = OMIT,
        redirect_uris: typing.Optional[typing.Sequence[str]] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        technical_contact: typing.Optional[PartnerEndCustomerTechnicalContact] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PartnerCustomerCreateResponse:
        """
        The `/partner/customer/create` endpoint is used by reseller partners to create end customers.

        Parameters
        ----------
        address : PartnerEndCustomerAddress

        application_name : str
            The name of the end customer's application. This will be shown to end users when they go through the Plaid Link flow.

        company_name : str
            The company name of the end customer being created. This will be used to display the end customer in the Plaid Dashboard. It will not be shown to end users.

        is_bank_addendum_completed : bool
            Denotes whether the partner has forwarded the Plaid bank addendum to the end customer.

        is_diligence_attested : bool
            Denotes whether or not the partner has completed attestation of diligence for the end customer to be created.

        legal_entity_name : str
            The end customer's legal name. This will be shared with financial institutions as part of the OAuth registration process. It will not be shown to end users.

        products : typing.Sequence[Products]
            The products to be enabled for the end customer.

        website : str
            The end customer's website.

        assets_under_management : typing.Optional[PartnerEndCustomerAssetsUnderManagement]

        billing_contact : typing.Optional[PartnerEndCustomerBillingContact]

        client_id : typing.Optional[ApiClientId]

        create_link_customization : typing.Optional[bool]
            If `true`, the end customer's default Link customization will be set to match the partner's. You can always change the end customer's Link customization in the Plaid Dashboard. See the [Link Customization docs](https://plaid.com/docs/link/customization/) for more information.

        customer_support_info : typing.Optional[PartnerEndCustomerCustomerSupportInfo]

        logo : typing.Optional[str]
            Base64-encoded representation of the end customer's logo. Must be a PNG of size 1024x1024 under 4MB. The logo will be shared with financial institutions and shown to the end user during Link flows. A logo is required if `create_link_customization` is `true`. If `create_link_customization` is `false` and the logo is omitted, a stock logo will be used.

        redirect_uris : typing.Optional[typing.Sequence[str]]
            A list of URIs indicating the destination(s) where a user can be forwarded after completing the Link flow; used to support OAuth authentication flows when launching Link in the browser or via a webview. URIs should not contain any query parameters. When used in Production or Development, URIs must use https. To specify any subdomain, use `*` as a wildcard character, e.g. `https://*.example.com/oauth.html`. To modify redirect URIs for an end customer after creating them, go to the end customer's [API page](https://dashboard.plaid.com/team/api) in the Dashboard.

        secret : typing.Optional[ApiSecret]

        technical_contact : typing.Optional[PartnerEndCustomerTechnicalContact]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PartnerCustomerCreateResponse
            OK

        Examples
        --------
        from fern import (
            FernApi,
            PartnerEndCustomerAddress,
            PartnerEndCustomerBillingContact,
            PartnerEndCustomerCustomerSupportInfo,
            PartnerEndCustomerTechnicalContact,
        )

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.partner_customer_create(
            address=PartnerEndCustomerAddress(
                city="New York",
                country_code="US",
                postal_code="12345",
                region="NY",
                street="123 Main St",
            ),
            application_name="Plaid",
            billing_contact=PartnerEndCustomerBillingContact(
                email="bob.jones@example.com",
                family_name="Jones",
                given_name="Bob",
            ),
            client_id="7f57eb3d2a9j6480121fx361",
            company_name="Plaid",
            create_link_customization=True,
            customer_support_info=PartnerEndCustomerCustomerSupportInfo(
                contact_url="example.com/contact",
                email="support@example.com",
                link_update_url="example.com/update",
                phone_number="1234567890",
            ),
            is_bank_addendum_completed=True,
            is_diligence_attested=True,
            legal_entity_name="Plaid",
            products=["auth", "identity"],
            redirect_uris=[
                "http://localhost/oauth.html",
                "https://www.example.com/oauth.html",
                "https://*.example.com/oauth.html",
            ],
            secret="79g03eoofwl8240v776r2h667442119",
            technical_contact=PartnerEndCustomerTechnicalContact(
                email="alice.smith@example.com",
                family_name="Smith",
                given_name="Alice",
            ),
            website="plaid.com",
        )
        """
        _response = self._raw_client.partner_customer_create(
            address=address,
            application_name=application_name,
            company_name=company_name,
            is_bank_addendum_completed=is_bank_addendum_completed,
            is_diligence_attested=is_diligence_attested,
            legal_entity_name=legal_entity_name,
            products=products,
            website=website,
            assets_under_management=assets_under_management,
            billing_contact=billing_contact,
            client_id=client_id,
            create_link_customization=create_link_customization,
            customer_support_info=customer_support_info,
            logo=logo,
            redirect_uris=redirect_uris,
            secret=secret,
            technical_contact=technical_contact,
            request_options=request_options,
        )
        return _response.data

    def partner_customer_enable(
        self,
        *,
        end_customer_client_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PartnerCustomerEnableResponse:
        """
        The `/partner/customer/enable` endpoint is used by reseller partners to enable an end customer in the Production environment.

        Parameters
        ----------
        end_customer_client_id : str

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PartnerCustomerEnableResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.partner_customer_enable(
            client_id="7f57eb3d2a9j6480121fx361",
            end_customer_client_id="7f57eb3d2a9j6480121fx361",
            secret="79g03eoofwl8240v776r2h667442119",
        )
        """
        _response = self._raw_client.partner_customer_enable(
            end_customer_client_id=end_customer_client_id,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def partner_customer_get(
        self,
        *,
        end_customer_client_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PartnerCustomerGetResponse:
        """
        The `/partner/customer/get` endpoint is used by reseller partners to retrieve data about a single end customer.

        Parameters
        ----------
        end_customer_client_id : str

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PartnerCustomerGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.partner_customer_get(
            client_id="7f57eb3d2a9j6480121fx361",
            end_customer_client_id="7f57eb3d2a9j6480121fx361",
            secret="79g03eoofwl8240v776r2h667442119",
        )
        """
        _response = self._raw_client.partner_customer_get(
            end_customer_client_id=end_customer_client_id,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def partner_customer_oauth_institutions_get(
        self,
        *,
        end_customer_client_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PartnerCustomerOAuthInstitutionsGetResponse:
        """
        The `/partner/customer/oauth_institutions/get` endpoint is used by reseller partners to retrieve OAuth-institution registration information about a single end customer. To learn how to set up a webhook to listen to status update events, visit the [reseller documentation](https://plaid.com/docs/account/resellers/#enabling-end-customers).

        Parameters
        ----------
        end_customer_client_id : str

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PartnerCustomerOAuthInstitutionsGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.partner_customer_oauth_institutions_get(
            client_id="7f57eb3d2a9j6480121fx361",
            end_customer_client_id="7f57eb3d2a9j6480121fx361",
            secret="79g03eoofwl8240v776r2h667442119",
        )
        """
        _response = self._raw_client.partner_customer_oauth_institutions_get(
            end_customer_client_id=end_customer_client_id,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def partner_customer_remove(
        self,
        *,
        end_customer_client_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PartnerCustomerRemoveResponse:
        """
        The `/partner/customer/remove` endpoint is used by reseller partners to remove an end customer. Removing an end customer will remove it from view in the Plaid Dashboard and deactivate its API keys. This endpoint can only be used to remove an end customer that has not yet been enabled in Production.

        Parameters
        ----------
        end_customer_client_id : str

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PartnerCustomerRemoveResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.partner_customer_remove(
            client_id="7f57eb3d2a9j6480121fx361",
            end_customer_client_id="7f57eb3d2a9j6480121fx361",
            secret="79g03eoofwl8240v776r2h667442119",
        )
        """
        _response = self._raw_client.partner_customer_remove(
            end_customer_client_id=end_customer_client_id,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def payment_initiation_consent_create(
        self,
        *,
        constraints: PaymentInitiationConsentConstraints,
        recipient_id: str,
        reference: str,
        scopes: typing.Sequence[PaymentInitiationConsentScope],
        client_id: typing.Optional[ApiClientId] = OMIT,
        options: typing.Optional[ExternalPaymentInitiationConsentOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentInitiationConsentCreateResponse:
        """
        The `/payment_initiation/consent/create` endpoint is used to create a payment consent, which can be used to initiate payments on behalf of the user. Payment consents are created with `UNAUTHORISED` status by default and must be authorised by the user before payments can be initiated.

        Consents can be limited in time and scope, and have constraints that describe limitations for payments.

        Parameters
        ----------
        constraints : PaymentInitiationConsentConstraints

        recipient_id : str
            The ID of the recipient the payment consent is for. The created consent can be used to transfer funds to this recipient only.

        reference : str
            A reference for the payment consent. This must be an alphanumeric string with at most 18 characters and must not contain any special characters.

        scopes : typing.Sequence[PaymentInitiationConsentScope]
            An array of payment consent scopes.

        client_id : typing.Optional[ApiClientId]

        options : typing.Optional[ExternalPaymentInitiationConsentOptions]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentInitiationConsentCreateResponse
            OK

        Examples
        --------
        from fern import (
            FernApi,
            PaymentAmount,
            PaymentConsentPeriodicAmount,
            PaymentInitiationConsentConstraints,
        )

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.payment_initiation_consent_create(
            constraints=PaymentInitiationConsentConstraints(
                max_payment_amount=PaymentAmount(
                    currency="GBP",
                    value=1.1,
                ),
                periodic_amounts=[
                    PaymentConsentPeriodicAmount(
                        alignment="CALENDAR",
                        amount=PaymentAmount(
                            currency="GBP",
                            value=1.1,
                        ),
                        interval="DAY",
                    )
                ],
            ),
            recipient_id="recipient_id",
            reference="reference",
            scopes=["ME_TO_ME"],
        )
        """
        _response = self._raw_client.payment_initiation_consent_create(
            constraints=constraints,
            recipient_id=recipient_id,
            reference=reference,
            scopes=scopes,
            client_id=client_id,
            options=options,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def payment_initiation_consent_get(
        self,
        *,
        consent_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentInitiationConsentGetResponse:
        """
        The `/payment_initiation/consent/get` endpoint can be used to check the status of a payment consent, as well as to receive basic information such as recipient and constraints.

        Parameters
        ----------
        consent_id : str
            The `consent_id` returned from `/payment_initiation/consent/create`.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentInitiationConsentGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.payment_initiation_consent_get(
            consent_id="consent_id",
        )
        """
        _response = self._raw_client.payment_initiation_consent_get(
            consent_id=consent_id, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def payment_initiation_consent_payment_execute(
        self,
        *,
        amount: PaymentAmount,
        consent_id: str,
        idempotency_key: ConsentPaymentIdempotencyKey,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentInitiationConsentPaymentExecuteResponse:
        """
        The `/payment_initiation/consent/payment/execute` endpoint can be used to execute payments using payment consent.

        Parameters
        ----------
        amount : PaymentAmount

        consent_id : str
            The consent ID.

        idempotency_key : ConsentPaymentIdempotencyKey

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentInitiationConsentPaymentExecuteResponse
            OK

        Examples
        --------
        from fern import FernApi, PaymentAmount

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.payment_initiation_consent_payment_execute(
            amount=PaymentAmount(
                currency="GBP",
                value=1.1,
            ),
            consent_id="consent_id",
            idempotency_key="idempotency_key",
        )
        """
        _response = self._raw_client.payment_initiation_consent_payment_execute(
            amount=amount,
            consent_id=consent_id,
            idempotency_key=idempotency_key,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def payment_initiation_consent_revoke(
        self,
        *,
        consent_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentInitiationConsentRevokeResponse:
        """
        The `/payment_initiation/consent/revoke` endpoint can be used to revoke the payment consent. Once the consent is revoked, it is not possible to initiate payments using it.

        Parameters
        ----------
        consent_id : str
            The consent ID.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentInitiationConsentRevokeResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.payment_initiation_consent_revoke(
            consent_id="consent_id",
        )
        """
        _response = self._raw_client.payment_initiation_consent_revoke(
            consent_id=consent_id, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def payment_initiation_payment_create(
        self,
        *,
        amount: PaymentAmount,
        recipient_id: str,
        reference: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        options: typing.Optional[ExternalPaymentOptions] = OMIT,
        schedule: typing.Optional[ExternalPaymentScheduleRequest] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentInitiationPaymentCreateResponse:
        """
        After creating a payment recipient, you can use the `/payment_initiation/payment/create` endpoint to create a payment to that recipient.  Payments can be one-time or standing order (recurring) and can be denominated in either EUR, GBP or other chosen [currency](https://plaid.com/docs/api/products/payment-initiation/#payment_initiation-payment-create-request-amount-currency).  If making domestic GBP-denominated payments, your recipient must have been created with BACS numbers. In general, EUR-denominated payments will be sent via SEPA Credit Transfer, GBP-denominated payments will be sent via the Faster Payments network and for non-Eurozone markets typically via the local payment scheme, but the payment network used will be determined by the institution. Payments sent via Faster Payments will typically arrive immediately, while payments sent via SEPA Credit Transfer or other local payment schemes will typically arrive in one business day.

        Standing orders (recurring payments) must be denominated in GBP and can only be sent to recipients in the UK. Once created, standing order payments cannot be modified or canceled via the API. An end user can cancel or modify a standing order directly on their banking application or website, or by contacting the bank. Standing orders will follow the payment rules of the underlying rails (Faster Payments in UK). Payments can be sent Monday to Friday, excluding bank holidays. If the pre-arranged date falls on a weekend or bank holiday, the payment is made on the next working day. It is not possible to guarantee the exact time the payment will reach the recipient’s account, although at least 90% of standing order payments are sent by 6am.

        In the Development environment, payments must be below 5 GBP or other chosen [currency](https://plaid.com/docs/api/products/payment-initiation/#payment_initiation-payment-create-request-amount-currency). For details on any payment limits in Production, contact your Plaid Account Manager.

        Parameters
        ----------
        amount : PaymentAmount

        recipient_id : str
            The ID of the recipient the payment is for.

        reference : str
            A reference for the payment. This must be an alphanumeric string with at most 18 characters and must not contain any special characters (since not all institutions support them).
            In order to track settlement via Payment Confirmation, each payment must have a unique reference. If the reference provided through the API is not unique, Plaid will adjust it.
            Both the originally provided and automatically adjusted references (if any) can be found in the `reference` and `adjusted_reference` fields, respectively.

        client_id : typing.Optional[ApiClientId]

        options : typing.Optional[ExternalPaymentOptions]

        schedule : typing.Optional[ExternalPaymentScheduleRequest]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentInitiationPaymentCreateResponse
            OK

        Examples
        --------
        from fern import FernApi, PaymentAmount

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.payment_initiation_payment_create(
            amount=PaymentAmount(
                currency="GBP",
                value=1.1,
            ),
            recipient_id="recipient_id",
            reference="reference",
        )
        """
        _response = self._raw_client.payment_initiation_payment_create(
            amount=amount,
            recipient_id=recipient_id,
            reference=reference,
            client_id=client_id,
            options=options,
            schedule=schedule,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def payment_initiation_payment_get(
        self,
        *,
        payment_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentInitiationPaymentGetResponse:
        """
        The `/payment_initiation/payment/get` endpoint can be used to check the status of a payment, as well as to receive basic information such as recipient and payment amount. In the case of standing orders, the `/payment_initiation/payment/get` endpoint will provide information about the status of the overall standing order itself; the API cannot be used to retrieve payment status for individual payments within a standing order.

        Parameters
        ----------
        payment_id : str
            The `payment_id` returned from `/payment_initiation/payment/create`.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentInitiationPaymentGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.payment_initiation_payment_get(
            payment_id="payment_id",
        )
        """
        _response = self._raw_client.payment_initiation_payment_get(
            payment_id=payment_id, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def payment_initiation_payment_list(
        self,
        *,
        client_id: typing.Optional[ApiClientId] = OMIT,
        consent_id: typing.Optional[str] = OMIT,
        count: typing.Optional[int] = OMIT,
        cursor: typing.Optional[dt.datetime] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentInitiationPaymentListResponse:
        """
        The `/payment_initiation/payment/list` endpoint can be used to retrieve all created payments. By default, the 10 most recent payments are returned. You can request more payments and paginate through the results using the optional `count` and `cursor` parameters.

        Parameters
        ----------
        client_id : typing.Optional[ApiClientId]

        consent_id : typing.Optional[str]
            The consent ID. If specified, only payments, executed using this consent, will be returned.

        count : typing.Optional[int]
            The maximum number of payments to return. If `count` is not specified, a maximum of 10 payments will be returned, beginning with the most recent payment before the cursor (if specified).

        cursor : typing.Optional[dt.datetime]
            A string in RFC 3339 format (i.e. "2019-12-06T22:35:49Z"). Only payments created before the cursor will be returned.

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentInitiationPaymentListResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.payment_initiation_payment_list()
        """
        _response = self._raw_client.payment_initiation_payment_list(
            client_id=client_id,
            consent_id=consent_id,
            count=count,
            cursor=cursor,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def payment_initiation_payment_reverse(
        self,
        *,
        idempotency_key: WalletTransactionIdempotencyKey,
        payment_id: str,
        reference: str,
        amount: typing.Optional[PaymentAmountToRefund] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentInitiationPaymentReverseResponse:
        """
        Reverse a settled payment from a Plaid virtual account.

        The original payment must be in a settled state to be refunded.
        To refund partially, specify the amount as part of the request.
        If the amount is not specified, the refund amount will be equal to all
        of the remaining payment amount that has not been refunded yet.

        The refund will go back to the source account that initiated the payment.
        The original payment must have been initiated to a Plaid virtual account
        so that this account can be used to initiate the refund.

        Parameters
        ----------
        idempotency_key : WalletTransactionIdempotencyKey

        payment_id : str
            The ID of the payment to reverse

        reference : str
            A reference for the refund. This must be an alphanumeric string with 6 to 18 characters and must not contain any special characters or spaces.

        amount : typing.Optional[PaymentAmountToRefund]

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentInitiationPaymentReverseResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.payment_initiation_payment_reverse(
            idempotency_key="idempotency_key",
            payment_id="payment_id",
            reference="reference",
        )
        """
        _response = self._raw_client.payment_initiation_payment_reverse(
            idempotency_key=idempotency_key,
            payment_id=payment_id,
            reference=reference,
            amount=amount,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def create_payment_token(
        self,
        *,
        payment_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentInitiationPaymentTokenCreateResponse:
        """
        The `/payment_initiation/payment/token/create` endpoint has been deprecated. New Plaid customers will be unable to use this endpoint, and existing customers are encouraged to migrate to the newer, `link_token`-based flow. The recommended flow is to provide the `payment_id` to `/link/token/create`, which returns a `link_token` used to initialize Link.

        The `/payment_initiation/payment/token/create` is used to create a `payment_token`, which can then be used in Link initialization to enter a payment initiation flow. You can only use a `payment_token` once. If this attempt fails, the end user aborts the flow, or the token expires, you will need to create a new payment token. Creating a new payment token does not require end user input.

        Parameters
        ----------
        payment_id : str
            The `payment_id` returned from `/payment_initiation/payment/create`.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentInitiationPaymentTokenCreateResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.create_payment_token(
            payment_id="payment_id",
        )
        """
        _response = self._raw_client.create_payment_token(
            payment_id=payment_id, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def payment_initiation_recipient_create(
        self,
        *,
        name: str,
        address: typing.Optional[PaymentInitiationAddress] = OMIT,
        bacs: typing.Optional[RecipientBacsNullable] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        iban: typing.Optional[str] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentInitiationRecipientCreateResponse:
        """
        Create a payment recipient for payment initiation.  The recipient must be in Europe, within a country that is a member of the Single Euro Payment Area (SEPA) or a non-Eurozone country [supported](https://plaid.com/global) by Plaid. For a standing order (recurring) payment, the recipient must be in the UK.

        It is recommended to use `bacs` in the UK and `iban` in EU.

        The endpoint is idempotent: if a developer has already made a request with the same payment details, Plaid will return the same `recipient_id`.

        Parameters
        ----------
        name : str
            The name of the recipient. We recommend using strings of length 18 or less and avoid special characters to ensure compatibility with all institutions.

        address : typing.Optional[PaymentInitiationAddress]

        bacs : typing.Optional[RecipientBacsNullable]

        client_id : typing.Optional[ApiClientId]

        iban : typing.Optional[str]
            The International Bank Account Number (IBAN) for the recipient. If BACS data is not provided, an IBAN is required.

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentInitiationRecipientCreateResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.payment_initiation_recipient_create(
            name="name",
        )
        """
        _response = self._raw_client.payment_initiation_recipient_create(
            name=name,
            address=address,
            bacs=bacs,
            client_id=client_id,
            iban=iban,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def payment_initiation_recipient_get(
        self,
        *,
        recipient_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentInitiationRecipientGetResponse:
        """
        Get details about a payment recipient you have previously created.

        Parameters
        ----------
        recipient_id : str
            The ID of the recipient

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentInitiationRecipientGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.payment_initiation_recipient_get(
            recipient_id="recipient_id",
        )
        """
        _response = self._raw_client.payment_initiation_recipient_get(
            recipient_id=recipient_id, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def payment_initiation_recipient_list(
        self,
        *,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentInitiationRecipientListResponse:
        """
        The `/payment_initiation/recipient/list` endpoint list the payment recipients that you have previously created.

        Parameters
        ----------
        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentInitiationRecipientListResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.payment_initiation_recipient_list()
        """
        _response = self._raw_client.payment_initiation_recipient_list(
            client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def payment_profile_create(
        self,
        *,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentProfileCreateResponse:
        """
        Use `/payment_profile/create` endpoint to create a new payment profile.
        To initiate the account linking experience, call `/link/token/create` and provide the `payment_profile_token` in the `transfer.payment_profile_token` field.
        You can then use the `payment_profile_token` when creating transfers using `/transfer/authorization/create` and `/transfer/create`.

        Parameters
        ----------
        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentProfileCreateResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.payment_profile_create()
        """
        _response = self._raw_client.payment_profile_create(
            client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def payment_profile_get(
        self,
        *,
        payment_profile_token: PaymentProfileToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentProfileGetResponse:
        """
        Use `/payment_profile/get` endpoint to get the status of a given Payment Profile.

        Parameters
        ----------
        payment_profile_token : PaymentProfileToken

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentProfileGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.payment_profile_get(
            payment_profile_token="payment_profile_token",
        )
        """
        _response = self._raw_client.payment_profile_get(
            payment_profile_token=payment_profile_token,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def payment_profile_remove(
        self,
        *,
        payment_profile_token: PaymentProfileToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentProfileRemoveResponse:
        """
        Use the `/payment_profile/remove` endpoint to remove a given Payment Profile. Once it’s removed, it can no longer be used to create transfers.

        Parameters
        ----------
        payment_profile_token : PaymentProfileToken

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentProfileRemoveResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.payment_profile_remove(
            payment_profile_token="payment_profile_token",
        )
        """
        _response = self._raw_client.payment_profile_remove(
            payment_profile_token=payment_profile_token,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def processor_apex_processor_token_create(
        self,
        *,
        access_token: AccessToken,
        account_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProcessorTokenCreateResponse:
        """
        Used to create a token suitable for sending to Apex to enable Plaid-Apex integrations.

        Parameters
        ----------
        access_token : AccessToken

        account_id : str
            The `account_id` value obtained from the `onSuccess` callback in Link

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProcessorTokenCreateResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.processor_apex_processor_token_create(
            access_token="access_token",
            account_id="account_id",
        )
        """
        _response = self._raw_client.processor_apex_processor_token_create(
            access_token=access_token,
            account_id=account_id,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def processor_auth_get(
        self,
        *,
        processor_token: ProcessorToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProcessorAuthGetResponse:
        """
        The `/processor/auth/get` endpoint returns the bank account and bank identification number (such as the routing number, for US accounts), for a checking or savings account that''s associated with a given `processor_token`. The endpoint also returns high-level account data and balances when available.

        Versioning note: API versions 2019-05-29 and earlier use a different schema for the `numbers` object returned by this endpoint. For details, see [Plaid API versioning](https://plaid.com/docs/api/versioning/#version-2020-09-14).

        Parameters
        ----------
        processor_token : ProcessorToken

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProcessorAuthGetResponse
            success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.processor_auth_get(
            processor_token="processor_token",
        )
        """
        _response = self._raw_client.processor_auth_get(
            processor_token=processor_token, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def processor_balance_get(
        self,
        *,
        processor_token: ProcessorToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        options: typing.Optional[ProcessorBalanceGetRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProcessorBalanceGetResponse:
        """
        The `/processor/balance/get` endpoint returns the real-time balance for each of an Item's accounts. While other endpoints may return a balance object, only `/processor/balance/get` forces the available and current balance fields to be refreshed rather than cached.

        Parameters
        ----------
        processor_token : ProcessorToken

        client_id : typing.Optional[ApiClientId]

        options : typing.Optional[ProcessorBalanceGetRequestOptions]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProcessorBalanceGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.processor_balance_get(
            processor_token="processor_token",
        )
        """
        _response = self._raw_client.processor_balance_get(
            processor_token=processor_token,
            client_id=client_id,
            options=options,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def processor_bank_transfer_create(
        self,
        *,
        amount: BankTransferAmount,
        description: str,
        idempotency_key: BankTransferIdempotencyKey,
        iso_currency_code: str,
        network: BankTransferNetwork,
        processor_token: ProcessorToken,
        type: BankTransferType,
        user: BankTransferUser,
        ach_class: typing.Optional[AchClass] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        custom_tag: typing.Optional[str] = OMIT,
        metadata: typing.Optional[BankTransferMetadata] = OMIT,
        origination_account_id: typing.Optional[str] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProcessorBankTransferCreateResponse:
        """
        Use the `/processor/bank_transfer/create` endpoint to initiate a new bank transfer as a processor

        Parameters
        ----------
        amount : BankTransferAmount

        description : str
            The transfer description. Maximum of 10 characters.

        idempotency_key : BankTransferIdempotencyKey

        iso_currency_code : str
            The currency of the transfer amount – should be set to "USD".

        network : BankTransferNetwork

        processor_token : ProcessorToken

        type : BankTransferType

        user : BankTransferUser

        ach_class : typing.Optional[AchClass]

        client_id : typing.Optional[ApiClientId]

        custom_tag : typing.Optional[str]
            An arbitrary string provided by the client for storage with the bank transfer. May be up to 100 characters.

        metadata : typing.Optional[BankTransferMetadata]

        origination_account_id : typing.Optional[str]
            Plaid’s unique identifier for the origination account for this transfer. If you have more than one origination account, this value must be specified.

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProcessorBankTransferCreateResponse
            OK

        Examples
        --------
        from fern import BankTransferUser, FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.processor_bank_transfer_create(
            amount="amount",
            description="description",
            idempotency_key="idempotency_key",
            iso_currency_code="iso_currency_code",
            network="ach",
            processor_token="processor_token",
            type="debit",
            user=BankTransferUser(
                legal_name="legal_name",
            ),
        )
        """
        _response = self._raw_client.processor_bank_transfer_create(
            amount=amount,
            description=description,
            idempotency_key=idempotency_key,
            iso_currency_code=iso_currency_code,
            network=network,
            processor_token=processor_token,
            type=type,
            user=user,
            ach_class=ach_class,
            client_id=client_id,
            custom_tag=custom_tag,
            metadata=metadata,
            origination_account_id=origination_account_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def processor_identity_get(
        self,
        *,
        processor_token: ProcessorToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProcessorIdentityGetResponse:
        """
        The `/processor/identity/get` endpoint allows you to retrieve various account holder information on file with the financial institution, including names, emails, phone numbers, and addresses.

        Parameters
        ----------
        processor_token : ProcessorToken

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProcessorIdentityGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.processor_identity_get(
            processor_token="processor_token",
        )
        """
        _response = self._raw_client.processor_identity_get(
            processor_token=processor_token, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def processor_signal_decision_report(
        self,
        *,
        client_transaction_id: str,
        initiated: bool,
        processor_token: ProcessorToken,
        amount_instantly_available: typing.Optional[float] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        days_funds_on_hold: typing.Optional[int] = OMIT,
        decision_outcome: typing.Optional[SignalDecisionOutcome] = OMIT,
        payment_method: typing.Optional[SignalPaymentMethod] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProcessorSignalDecisionReportResponse:
        """
        After calling `/processor/signal/evaluate`, call `/processor/signal/decision/report` to report whether the transaction was initiated. This endpoint will return an [`INVALID_FIELD`](/docs/errors/invalid-request/#invalid_field) error if called a second time with a different value for `initiated`.

        Parameters
        ----------
        client_transaction_id : str
            Must be the same as the `client_transaction_id` supplied when calling `/signal/evaluate`

        initiated : bool
            `true` if the ACH transaction was initiated, `false` otherwise.

            This field must be returned as a boolean. If formatted incorrectly, this will result in an [`INVALID_FIELD`](/docs/errors/invalid-request/#invalid_field) error.

        processor_token : ProcessorToken

        amount_instantly_available : typing.Optional[float]
            The amount (in USD) made available to your customers instantly following the debit transaction. It could be a partial amount of the requested transaction (example: 102.05).

        client_id : typing.Optional[ApiClientId]

        days_funds_on_hold : typing.Optional[int]
            The actual number of days (hold time) since the ACH debit transaction that you wait before making funds available to your customers. The holding time could affect the ACH return rate.

            For example, use 0 if you make funds available to your customers instantly or the same day following the debit transaction, or 1 if you make funds available the next day following the debit initialization.

        decision_outcome : typing.Optional[SignalDecisionOutcome]

        payment_method : typing.Optional[SignalPaymentMethod]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProcessorSignalDecisionReportResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.processor_signal_decision_report(
            client_transaction_id="client_transaction_id",
            initiated=True,
            processor_token="processor_token",
        )
        """
        _response = self._raw_client.processor_signal_decision_report(
            client_transaction_id=client_transaction_id,
            initiated=initiated,
            processor_token=processor_token,
            amount_instantly_available=amount_instantly_available,
            client_id=client_id,
            days_funds_on_hold=days_funds_on_hold,
            decision_outcome=decision_outcome,
            payment_method=payment_method,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def processor_signal_evaluate(
        self,
        *,
        amount: float,
        client_transaction_id: str,
        processor_token: ProcessorToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        client_user_id: typing.Optional[str] = OMIT,
        default_payment_method: typing.Optional[str] = OMIT,
        device: typing.Optional[SignalDevice] = OMIT,
        is_recurring: typing.Optional[bool] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        user: typing.Optional[SignalUser] = OMIT,
        user_present: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProcessorSignalEvaluateResponse:
        """
        Use `/processor/signal/evaluate` to evaluate a planned ACH transaction as a processor to get a return risk assessment (such as a risk score and risk tier) and additional risk signals.

        In order to obtain a valid score for an ACH transaction, Plaid must have an access token for the account, and the Item must be healthy (receiving product updates) or have recently been in a healthy state. If the transaction does not meet eligibility requirements, an error will be returned corresponding to the underlying cause. If `/processor/signal/evaluate` is called on the same transaction multiple times within a 24-hour period, cached results may be returned. For more information please refer to our error documentation on [item errors](/docs/errors/item/) and [Link in Update Mode](/docs/link/update-mode/).

        Note: This request may take some time to complete if Signal is being added to an existing Item. This is because Plaid must communicate directly with the institution when retrieving the data for the first time.

        Parameters
        ----------
        amount : float
            The transaction amount, in USD (e.g. `102.05`)

        client_transaction_id : str
            The unique ID that you would like to use to refer to this transaction. For your convenience mapping your internal data, you could use your internal ID/identifier for this transaction. The max length for this field is 36 characters.

        processor_token : ProcessorToken

        client_id : typing.Optional[ApiClientId]

        client_user_id : typing.Optional[str]
            A unique ID that identifies the end user in your system. This ID is used to correlate requests by a user with multiple Items. The max length for this field is 36 characters. Personally identifiable information, such as an email address or phone number, should not be used in the `client_user_id`.

        default_payment_method : typing.Optional[str]
            The default ACH or non-ACH payment method to complete the transaction.
            `SAME_DAY_ACH`: Same Day ACH by NACHA. The debit transaction is processed and settled on the same day
            `NEXT_DAY_ACH`: Next Day ACH settlement for debit transactions, offered by some payment processors
            `STANDARD_ACH`: standard ACH by NACHA
            `REAL_TIME_PAYMENTS`: real-time payments such as RTP and FedNow
            `DEBIT_CARD`: if the default payment is over debit card networks
            `MULTIPLE_PAYMENT_METHODS`: if there is no default debit rail or there are multiple payment methods
            Possible values:  `SAME_DAY_ACH`, `NEXT_DAY_ACH`, `STANDARD_ACH`, `REAL_TIME_PAYMENTS`, `DEBIT_CARD`, `MULTIPLE_PAYMENT_METHODS`

        device : typing.Optional[SignalDevice]

        is_recurring : typing.Optional[bool]
            **true** if the ACH transaction is a recurring transaction; **false** otherwise

        secret : typing.Optional[ApiSecret]

        user : typing.Optional[SignalUser]

        user_present : typing.Optional[bool]
            `true` if the end user is present while initiating the ACH transfer and the endpoint is being called; `false` otherwise (for example, when the ACH transfer is scheduled and the end user is not present, or you call this endpoint after the ACH transfer but before submitting the Nacha file for ACH processing).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProcessorSignalEvaluateResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.processor_signal_evaluate(
            amount=1.1,
            client_transaction_id="client_transaction_id",
            processor_token="processor_token",
        )
        """
        _response = self._raw_client.processor_signal_evaluate(
            amount=amount,
            client_transaction_id=client_transaction_id,
            processor_token=processor_token,
            client_id=client_id,
            client_user_id=client_user_id,
            default_payment_method=default_payment_method,
            device=device,
            is_recurring=is_recurring,
            secret=secret,
            user=user,
            user_present=user_present,
            request_options=request_options,
        )
        return _response.data

    def processor_signal_return_report(
        self,
        *,
        client_transaction_id: str,
        processor_token: ProcessorToken,
        return_code: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        returned_at: typing.Optional[dt.datetime] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProcessorSignalReturnReportResponse:
        """
        Call the `/processor/signal/return/report` endpoint to report a returned transaction that was previously sent to the `/processor/signal/evaluate` endpoint. Your feedback will be used by the model to incorporate the latest risk trend in your portfolio.

        Parameters
        ----------
        client_transaction_id : str
            Must be the same as the `client_transaction_id` supplied when calling `/processor/signal/evaluate`

        processor_token : ProcessorToken

        return_code : str
            Must be a valid ACH return code (e.g. "R01")

            If formatted incorrectly, this will result in an [`INVALID_FIELD`](/docs/errors/invalid-request/#invalid_field) error.

        client_id : typing.Optional[ApiClientId]

        returned_at : typing.Optional[dt.datetime]
            Date and time when you receive the returns from your payment processors, in ISO 8601 format (`YYYY-MM-DDTHH:mm:ssZ`).

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProcessorSignalReturnReportResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.processor_signal_return_report(
            client_transaction_id="client_transaction_id",
            processor_token="processor_token",
            return_code="return_code",
        )
        """
        _response = self._raw_client.processor_signal_return_report(
            client_transaction_id=client_transaction_id,
            processor_token=processor_token,
            return_code=return_code,
            client_id=client_id,
            returned_at=returned_at,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def processor_stripe_bank_account_token_create(
        self,
        *,
        access_token: AccessToken,
        account_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProcessorStripeBankAccountTokenCreateResponse:
        """

        Used to create a token suitable for sending to Stripe to enable Plaid-Stripe integrations. For a detailed guide on integrating Stripe, see [Add Stripe to your app](https://plaid.com/docs/auth/partnerships/stripe/).

        Note that the Stripe bank account token is a one-time use token. To store bank account information for later use, you can use a Stripe customer object and create an associated bank account from the token, or you can use a Stripe Custom account and create an associated external bank account from the token. This bank account information should work indefinitely, unless the user's bank account information changes or they revoke Plaid's permissions to access their account. Stripe bank account information cannot be modified once the bank account token has been created. If you ever need to change the bank account details used by Stripe for a specific customer, have the user go through Link again and create a new bank account token from the new `access_token`.

        Bank account tokens can also be revoked, using `/item/remove`.'

        Parameters
        ----------
        access_token : AccessToken

        account_id : str
            The `account_id` value obtained from the `onSuccess` callback in Link

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProcessorStripeBankAccountTokenCreateResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.processor_stripe_bank_account_token_create(
            access_token="access_token",
            account_id="account_id",
        )
        """
        _response = self._raw_client.processor_stripe_bank_account_token_create(
            access_token=access_token,
            account_id=account_id,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def processor_token_create(
        self,
        *,
        access_token: AccessToken,
        account_id: str,
        processor: ProcessorTokenCreateRequestProcessor,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProcessorTokenCreateResponse:
        """
        Used to create a token suitable for sending to one of Plaid's partners to enable integrations. Note that Stripe partnerships use bank account tokens instead; see `/processor/stripe/bank_account_token/create` for creating tokens for use with Stripe integrations. Once created, a processor token for a given Item cannot be modified or updated. If the account must be linked to a new or different partner resource, create a new Item by having the user go through the Link flow again; a new processor token can then be created from the new `access_token`. Processor tokens can also be revoked, using `/item/remove`.

        Parameters
        ----------
        access_token : AccessToken

        account_id : str
            The `account_id` value obtained from the `onSuccess` callback in Link

        processor : ProcessorTokenCreateRequestProcessor
            The processor you are integrating with.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProcessorTokenCreateResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.processor_token_create(
            access_token="access_token",
            account_id="account_id",
            processor="dwolla",
        )
        """
        _response = self._raw_client.processor_token_create(
            access_token=access_token,
            account_id=account_id,
            processor=processor,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def sandbox_bank_transfer_fire_webhook(
        self,
        *,
        webhook: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SandboxBankTransferFireWebhookResponse:
        """
        Use the `/sandbox/bank_transfer/fire_webhook` endpoint to manually trigger a Bank Transfers webhook in the Sandbox environment.

        Parameters
        ----------
        webhook : str
            The URL to which the webhook should be sent.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SandboxBankTransferFireWebhookResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.sandbox_bank_transfer_fire_webhook(
            webhook="webhook",
        )
        """
        _response = self._raw_client.sandbox_bank_transfer_fire_webhook(
            webhook=webhook, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def sandbox_bank_transfer_simulate(
        self,
        *,
        bank_transfer_id: BankTransferId,
        event_type: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        failure_reason: typing.Optional[BankTransferFailure] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SandboxBankTransferSimulateResponse:
        """
        Use the `/sandbox/bank_transfer/simulate` endpoint to simulate a bank transfer event in the Sandbox environment.  Note that while an event will be simulated and will appear when using endpoints such as `/bank_transfer/event/sync` or `/bank_transfer/event/list`, no transactions will actually take place and funds will not move between accounts, even within the Sandbox.

        Parameters
        ----------
        bank_transfer_id : BankTransferId

        event_type : str
            The asynchronous event to be simulated. May be: `posted`, `failed`, or `reversed`.

            An error will be returned if the event type is incompatible with the current transfer status. Compatible status --> event type transitions include:

            `pending` --> `failed`

            `pending` --> `posted`

            `posted` --> `reversed`

        client_id : typing.Optional[ApiClientId]

        failure_reason : typing.Optional[BankTransferFailure]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SandboxBankTransferSimulateResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.sandbox_bank_transfer_simulate(
            bank_transfer_id="bank_transfer_id",
            event_type="event_type",
        )
        """
        _response = self._raw_client.sandbox_bank_transfer_simulate(
            bank_transfer_id=bank_transfer_id,
            event_type=event_type,
            client_id=client_id,
            failure_reason=failure_reason,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def sandbox_income_fire_webhook(
        self,
        *,
        item_id: str,
        verification_status: SandboxIncomeFireWebhookRequestVerificationStatus,
        webhook: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        user_id: typing.Optional[UserId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SandboxIncomeFireWebhookResponse:
        """
        Use the `/sandbox/income/fire_webhook` endpoint to manually trigger an Income webhook in the Sandbox environment.

        Parameters
        ----------
        item_id : str
            The Item ID associated with the verification.

        verification_status : SandboxIncomeFireWebhookRequestVerificationStatus
            `VERIFICATION_STATUS_PROCESSING_COMPLETE`: The income verification status processing has completed. If the user uploaded multiple documents, this webhook will fire when all documents have finished processing. Call the `/income/verification/paystubs/get` endpoint and check the document metadata to see which documents were successfully parsed.

            `VERIFICATION_STATUS_PROCESSING_FAILED`: A failure occurred when attempting to process the verification documentation.

            `VERIFICATION_STATUS_PENDING_APPROVAL`: (deprecated) The income verification has been sent to the user for review.

        webhook : str
            The URL to which the webhook should be sent.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        user_id : typing.Optional[UserId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SandboxIncomeFireWebhookResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.sandbox_income_fire_webhook(
            item_id="item_id",
            verification_status="VERIFICATION_STATUS_PROCESSING_COMPLETE",
            webhook="webhook",
        )
        """
        _response = self._raw_client.sandbox_income_fire_webhook(
            item_id=item_id,
            verification_status=verification_status,
            webhook=webhook,
            client_id=client_id,
            secret=secret,
            user_id=user_id,
            request_options=request_options,
        )
        return _response.data

    def sandbox_item_fire_webhook(
        self,
        *,
        access_token: AccessToken,
        webhook_code: SandboxItemFireWebhookRequestWebhookCode,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        webhook_type: typing.Optional[WebhookType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SandboxItemFireWebhookResponse:
        """
        The `/sandbox/item/fire_webhook` endpoint is used to test that code correctly handles webhooks. This endpoint can trigger the following webhooks:

        `DEFAULT_UPDATE`: Transactions update webhook to be fired for a given Sandbox Item. If the Item does not support Transactions, a `SANDBOX_PRODUCT_NOT_ENABLED` error will result.

        `NEW_ACCOUNTS_AVAILABLE`: Webhook to be fired for a given Sandbox Item created with Account Select v2.

        `AUTH_DATA_UPDATE`: Webhook to be fired for a given Sandbox Item created with Auth as an enabled product.

        `RECURRING_TRANSACTIONS_UPDATE`: Recurring Transactions webhook to be fired for a given Sandbox Item. If the Item does not support Recurring Transactions, a `SANDBOX_PRODUCT_NOT_ENABLED` error will result.

        `SYNC_UPDATES_AVAILABLE`: Transactions webhook to be fired for a given Sandbox Item.  If the Item does not support Transactions, a `SANDBOX_PRODUCT_NOT_ENABLED` error will result.

        Note that this endpoint is provided for developer ease-of-use and is not required for testing webhooks; webhooks will also fire in Sandbox under the same conditions that they would in Production or Development.

        Parameters
        ----------
        access_token : AccessToken

        webhook_code : SandboxItemFireWebhookRequestWebhookCode
            The webhook codes that can be fired by this test endpoint.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        webhook_type : typing.Optional[WebhookType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SandboxItemFireWebhookResponse
            success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.sandbox_item_fire_webhook(
            access_token="access_token",
            webhook_code="DEFAULT_UPDATE",
        )
        """
        _response = self._raw_client.sandbox_item_fire_webhook(
            access_token=access_token,
            webhook_code=webhook_code,
            client_id=client_id,
            secret=secret,
            webhook_type=webhook_type,
            request_options=request_options,
        )
        return _response.data

    def sandbox_item_reset_login(
        self,
        *,
        access_token: AccessToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SandboxItemResetLoginResponse:
        """
        `/sandbox/item/reset_login/` forces an Item into an `ITEM_LOGIN_REQUIRED` state in order to simulate an Item whose login is no longer valid. This makes it easy to test Link's [update mode](https://plaid.com/docs/link/update-mode) flow in the Sandbox environment.  After calling `/sandbox/item/reset_login`, You can then use Plaid Link update mode to restore the Item to a good state. An `ITEM_LOGIN_REQUIRED` webhook will also be fired after a call to this endpoint, if one is associated with the Item.


        In the Sandbox, Items will transition to an `ITEM_LOGIN_REQUIRED` error state automatically after 30 days, even if this endpoint is not called.

        Parameters
        ----------
        access_token : AccessToken

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SandboxItemResetLoginResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.sandbox_item_reset_login(
            access_token="access_token",
        )
        """
        _response = self._raw_client.sandbox_item_reset_login(
            access_token=access_token, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def sandbox_item_set_verification_status(
        self,
        *,
        access_token: AccessToken,
        account_id: str,
        verification_status: SandboxItemSetVerificationStatusRequestVerificationStatus,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SandboxItemSetVerificationStatusResponse:
        """
        The `/sandbox/item/set_verification_status` endpoint can be used to change the verification status of an Item in in the Sandbox in order to simulate the Automated Micro-deposit flow.

        Note that not all Plaid developer accounts are enabled for micro-deposit based verification by default. Your account must be enabled for this feature in order to test it in Sandbox. To enable this features or check your status, contact your account manager or [submit a product access Support ticket](https://dashboard.plaid.com/support/new/product-and-development/product-troubleshooting/request-product-access).

        For more information on testing Automated Micro-deposits in Sandbox, see [Auth full coverage testing](https://plaid.com/docs/auth/coverage/testing#).

        Parameters
        ----------
        access_token : AccessToken

        account_id : str
            The `account_id` of the account whose verification status is to be modified

        verification_status : SandboxItemSetVerificationStatusRequestVerificationStatus
            The verification status to set the account to.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SandboxItemSetVerificationStatusResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.sandbox_item_set_verification_status(
            access_token="access_token",
            account_id="account_id",
            verification_status="automatically_verified",
        )
        """
        _response = self._raw_client.sandbox_item_set_verification_status(
            access_token=access_token,
            account_id=account_id,
            verification_status=verification_status,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def sandbox_oauth_select_accounts(
        self,
        *,
        accounts: typing.Sequence[str],
        oauth_state_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SandboxOauthSelectAccountsResponse:
        """
        Save the selected accounts when connecting to the Platypus Oauth institution

        Parameters
        ----------
        accounts : typing.Sequence[str]

        oauth_state_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SandboxOauthSelectAccountsResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.sandbox_oauth_select_accounts(
            accounts=["accounts"],
            oauth_state_id="oauth_state_id",
        )
        """
        _response = self._raw_client.sandbox_oauth_select_accounts(
            accounts=accounts, oauth_state_id=oauth_state_id, request_options=request_options
        )
        return _response.data

    def sandbox_payment_profile_reset_login(
        self,
        *,
        payment_profile_token: PaymentProfileToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SandboxPaymentProfileResetLoginResponse:
        """
        `/sandbox/payment_profile/reset_login/` forces a Payment Profile into a state where the login is no longer valid. This makes it easy to test update mode for Payment Profile in the Sandbox environment.

         After calling `/sandbox/payment_profile/reset_login`, calls to the `/transfer/authorization/create` with the Payment Profile will result in a `decision_rationale` `PAYMENT_PROFILE_LOGIN_REQUIRED`. You can then use update mode for Payment Profile to restore it into a good state.

         In order to invoke this endpoint, you must first [create a Payment Profile](https://plaid.com/docs/transfer/add-to-app/#create-a-payment-profile-optional) and [go through the Link flow](https://plaid.com/docs/transfer/add-to-app/#create-a-link-token).

        Parameters
        ----------
        payment_profile_token : PaymentProfileToken

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SandboxPaymentProfileResetLoginResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.sandbox_payment_profile_reset_login(
            payment_profile_token="payment_profile_token",
        )
        """
        _response = self._raw_client.sandbox_payment_profile_reset_login(
            payment_profile_token=payment_profile_token,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def sandbox_processor_token_create(
        self,
        *,
        institution_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        options: typing.Optional[SandboxProcessorTokenCreateRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SandboxProcessorTokenCreateResponse:
        """
        Use the `/sandbox/processor_token/create` endpoint to create a valid `processor_token` for an arbitrary institution ID and test credentials. The created `processor_token` corresponds to a new Sandbox Item. You can then use this `processor_token` with the `/processor/` API endpoints in Sandbox. You can also use `/sandbox/processor_token/create` with the [`user_custom` test username](https://plaid.com/docs/sandbox/user-custom) to generate a test account with custom data.

        Parameters
        ----------
        institution_id : str
            The ID of the institution the Item will be associated with

        client_id : typing.Optional[ApiClientId]

        options : typing.Optional[SandboxProcessorTokenCreateRequestOptions]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SandboxProcessorTokenCreateResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.sandbox_processor_token_create(
            institution_id="institution_id",
        )
        """
        _response = self._raw_client.sandbox_processor_token_create(
            institution_id=institution_id,
            client_id=client_id,
            options=options,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def sandbox_public_token_create(
        self,
        *,
        initial_products: typing.Sequence[Products],
        institution_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        options: typing.Optional[SandboxPublicTokenCreateRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        user_token: typing.Optional[UserToken] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SandboxPublicTokenCreateResponse:
        """
        Use the `/sandbox/public_token/create` endpoint to create a valid `public_token`  for an arbitrary institution ID, initial products, and test credentials. The created `public_token` maps to a new Sandbox Item. You can then call `/item/public_token/exchange` to exchange the `public_token` for an `access_token` and perform all API actions. `/sandbox/public_token/create` can also be used with the [`user_custom` test username](https://plaid.com/docs/sandbox/user-custom) to generate a test account with custom data. `/sandbox/public_token/create` cannot be used with OAuth institutions.

        Parameters
        ----------
        initial_products : typing.Sequence[Products]
            The products to initially pull for the Item. May be any products that the specified `institution_id`  supports. This array may not be empty.

        institution_id : str
            The ID of the institution the Item will be associated with

        client_id : typing.Optional[ApiClientId]

        options : typing.Optional[SandboxPublicTokenCreateRequestOptions]

        secret : typing.Optional[ApiSecret]

        user_token : typing.Optional[UserToken]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SandboxPublicTokenCreateResponse
            success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.sandbox_public_token_create(
            initial_products=["assets"],
            institution_id="institution_id",
        )
        """
        _response = self._raw_client.sandbox_public_token_create(
            initial_products=initial_products,
            institution_id=institution_id,
            client_id=client_id,
            options=options,
            secret=secret,
            user_token=user_token,
            request_options=request_options,
        )
        return _response.data

    def sandbox_transfer_fire_webhook(
        self,
        *,
        webhook: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SandboxTransferFireWebhookResponse:
        """
        Use the `/sandbox/transfer/fire_webhook` endpoint to manually trigger a Transfer webhook in the Sandbox environment.

        Parameters
        ----------
        webhook : str
            The URL to which the webhook should be sent.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SandboxTransferFireWebhookResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.sandbox_transfer_fire_webhook(
            webhook="webhook",
        )
        """
        _response = self._raw_client.sandbox_transfer_fire_webhook(
            webhook=webhook, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def sandbox_transfer_repayment_simulate(
        self,
        *,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SandboxTransferRepaymentSimulateResponse:
        """
        Use the `/sandbox/transfer/repayment/simulate` endpoint to trigger the creation of a repayment. As a side effect of calling this route, a repayment is created that includes all unreimbursed returns of guaranteed transfers. If there are no such returns, an 400 error is returned.

        Parameters
        ----------
        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SandboxTransferRepaymentSimulateResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.sandbox_transfer_repayment_simulate()
        """
        _response = self._raw_client.sandbox_transfer_repayment_simulate(
            client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def sandbox_transfer_simulate(
        self,
        *,
        event_type: str,
        transfer_id: TransferId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        failure_reason: typing.Optional[TransferFailure] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SandboxTransferSimulateResponse:
        """
        Use the `/sandbox/transfer/simulate` endpoint to simulate a transfer event in the Sandbox environment.  Note that while an event will be simulated and will appear when using endpoints such as `/transfer/event/sync` or `/transfer/event/list`, no transactions will actually take place and funds will not move between accounts, even within the Sandbox.

        Parameters
        ----------
        event_type : str
            The asynchronous event to be simulated. May be: `posted`, `settled`, `failed`, or `returned`.

            An error will be returned if the event type is incompatible with the current transfer status. Compatible status --> event type transitions include:

            `pending` --> `failed`

            `pending` --> `posted`

            `posted` --> `returned`

            `posted` --> `settled`

        transfer_id : TransferId

        client_id : typing.Optional[ApiClientId]

        failure_reason : typing.Optional[TransferFailure]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SandboxTransferSimulateResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.sandbox_transfer_simulate(
            event_type="event_type",
            transfer_id="transfer_id",
        )
        """
        _response = self._raw_client.sandbox_transfer_simulate(
            event_type=event_type,
            transfer_id=transfer_id,
            client_id=client_id,
            failure_reason=failure_reason,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def sandbox_transfer_sweep_simulate(
        self,
        *,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SandboxTransferSweepSimulateResponse:
        """
        Use the `/sandbox/transfer/sweep/simulate` endpoint to create a sweep and associated events in the Sandbox environment. Upon calling this endpoint, all `posted` or `pending` transfers with a sweep status of `unswept` will become `swept`, and all `returned` transfers with a sweep status of `swept` will become `return_swept`.

        Parameters
        ----------
        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SandboxTransferSweepSimulateResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.sandbox_transfer_sweep_simulate()
        """
        _response = self._raw_client.sandbox_transfer_sweep_simulate(
            client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def sandbox_transfer_test_clock_advance(
        self,
        *,
        new_virtual_time: VirtualTime,
        test_clock_id: TransferTestClockId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SandboxTransferTestClockAdvanceResponse:
        """
        Use the `/sandbox/transfer/test_clock/advance` endpoint to advance a `test_clock` in the Sandbox environment.

        A test clock object represents an independent timeline and has a `virtual_time` field indicating the current timestamp of the timeline. A test clock can be advanced by incrementing `virtual_time`, but may never go back to a lower `virtual_time`.

        If a test clock is advanced, we will simulate the changes that ought to occur during the time that elapsed.
        For instance, a client creates a weekly recurring transfer with a test clock set at t. When the client advances the test clock by setting `virtual_time` = t + 15 days, 2 new originations should be created, along with the webhook events.

        The advancement of the test clock from its current `virtual_time` should be limited such that there are no more than 20 originations resulting from the advance operation on each `recurring_transfer` associated with the `test_clock`.
        For instance, if the recurring transfer associated with this test clock originates once every 4 weeks, you can advance the `virtual_time` up to 80 weeks on each API call.

        Parameters
        ----------
        new_virtual_time : VirtualTime

        test_clock_id : TransferTestClockId

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SandboxTransferTestClockAdvanceResponse
            OK

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.sandbox_transfer_test_clock_advance(
            new_virtual_time=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            test_clock_id="test_clock_id",
        )
        """
        _response = self._raw_client.sandbox_transfer_test_clock_advance(
            new_virtual_time=new_virtual_time,
            test_clock_id=test_clock_id,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def sandbox_transfer_test_clock_create(
        self,
        *,
        virtual_time: VirtualTime,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SandboxTransferTestClockCreateResponse:
        """
        Use the `/sandbox/transfer/test_clock/create` endpoint to create a `test_clock` in the Sandbox environment.

        A test clock object represents an independent timeline and has a `virtual_time` field indicating the current timestamp of the timeline. Test clocks are used for testing recurring transfers in Sandbox.

        A test clock can be associated with up to 5 recurring transfers.

        Parameters
        ----------
        virtual_time : VirtualTime

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SandboxTransferTestClockCreateResponse
            OK

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.sandbox_transfer_test_clock_create(
            virtual_time=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
        )
        """
        _response = self._raw_client.sandbox_transfer_test_clock_create(
            virtual_time=virtual_time, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def sandbox_transfer_test_clock_get(
        self,
        *,
        test_clock_id: TransferTestClockId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SandboxTransferTestClockGetResponse:
        """
        Use the `/sandbox/transfer/test_clock/get` endpoint to get a `test_clock` in the Sandbox environment.

        Parameters
        ----------
        test_clock_id : TransferTestClockId

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SandboxTransferTestClockGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.sandbox_transfer_test_clock_get(
            test_clock_id="test_clock_id",
        )
        """
        _response = self._raw_client.sandbox_transfer_test_clock_get(
            test_clock_id=test_clock_id, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def sandbox_transfer_test_clock_list(
        self,
        *,
        client_id: typing.Optional[ApiClientId] = OMIT,
        count: typing.Optional[int] = OMIT,
        end_virtual_time: typing.Optional[dt.datetime] = OMIT,
        offset: typing.Optional[int] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        start_virtual_time: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SandboxTransferTestClockListResponse:
        """
        Use the `/sandbox/transfer/test_clock/list` endpoint to see a list of all your test clocks in the Sandbox environment, by ascending `virtual_time`. Results are paginated; use the `count` and `offset` query parameters to retrieve the desired test clocks.

        Parameters
        ----------
        client_id : typing.Optional[ApiClientId]

        count : typing.Optional[int]
            The maximum number of test clocks to return.

        end_virtual_time : typing.Optional[dt.datetime]
            The end virtual timestamp of test clocks to return. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`)

        offset : typing.Optional[int]
            The number of test clocks to skip before returning results.

        secret : typing.Optional[ApiSecret]

        start_virtual_time : typing.Optional[dt.datetime]
            The start virtual timestamp of test clocks to return. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SandboxTransferTestClockListResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.sandbox_transfer_test_clock_list()
        """
        _response = self._raw_client.sandbox_transfer_test_clock_list(
            client_id=client_id,
            count=count,
            end_virtual_time=end_virtual_time,
            offset=offset,
            secret=secret,
            start_virtual_time=start_virtual_time,
            request_options=request_options,
        )
        return _response.data

    def signal_decision_report(
        self,
        *,
        client_transaction_id: str,
        initiated: bool,
        amount_instantly_available: typing.Optional[float] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        days_funds_on_hold: typing.Optional[int] = OMIT,
        decision_outcome: typing.Optional[SignalDecisionOutcome] = OMIT,
        payment_method: typing.Optional[SignalPaymentMethod] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SignalDecisionReportResponse:
        """
        After calling `/signal/evaluate`, call `/signal/decision/report` to report whether the transaction was initiated. This endpoint will return an [`INVALID_FIELD`](/docs/errors/invalid-request/#invalid_field) error if called a second time with a different value for `initiated`.

        Parameters
        ----------
        client_transaction_id : str
            Must be the same as the `client_transaction_id` supplied when calling `/signal/evaluate`

        initiated : bool
            `true` if the ACH transaction was initiated, `false` otherwise.

            This field must be returned as a boolean. If formatted incorrectly, this will result in an [`INVALID_FIELD`](/docs/errors/invalid-request/#invalid_field) error.

        amount_instantly_available : typing.Optional[float]
            The amount (in USD) made available to your customers instantly following the debit transaction. It could be a partial amount of the requested transaction (example: 102.05).

        client_id : typing.Optional[ApiClientId]

        days_funds_on_hold : typing.Optional[int]
            The actual number of days (hold time) since the ACH debit transaction that you wait before making funds available to your customers. The holding time could affect the ACH return rate.

            For example, use 0 if you make funds available to your customers instantly or the same day following the debit transaction, or 1 if you make funds available the next day following the debit initialization.

        decision_outcome : typing.Optional[SignalDecisionOutcome]

        payment_method : typing.Optional[SignalPaymentMethod]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SignalDecisionReportResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.signal_decision_report(
            client_transaction_id="client_transaction_id",
            initiated=True,
        )
        """
        _response = self._raw_client.signal_decision_report(
            client_transaction_id=client_transaction_id,
            initiated=initiated,
            amount_instantly_available=amount_instantly_available,
            client_id=client_id,
            days_funds_on_hold=days_funds_on_hold,
            decision_outcome=decision_outcome,
            payment_method=payment_method,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def signal_evaluate(
        self,
        *,
        access_token: AccessToken,
        account_id: str,
        amount: float,
        client_transaction_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        client_user_id: typing.Optional[str] = OMIT,
        default_payment_method: typing.Optional[str] = OMIT,
        device: typing.Optional[SignalDevice] = OMIT,
        is_recurring: typing.Optional[bool] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        user: typing.Optional[SignalUser] = OMIT,
        user_present: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SignalEvaluateResponse:
        """
        Use `/signal/evaluate` to evaluate a planned ACH transaction to get a return risk assessment (such as a risk score and risk tier) and additional risk signals.

        In order to obtain a valid score for an ACH transaction, Plaid must have an access token for the account, and the Item must be healthy (receiving product updates) or have recently been in a healthy state. If the transaction does not meet eligibility requirements, an error will be returned corresponding to the underlying cause. If `/signal/evaluate` is called on the same transaction multiple times within a 24-hour period, cached results may be returned. For more information please refer to the error documentation on [Item errors](/docs/errors/item/) and [Link in Update Mode](/docs/link/update-mode/).

        Note: This request may take some time to complete if Signal is being added to an existing Item. This is because Plaid must communicate directly with the institution when retrieving the data for the first time.

        Parameters
        ----------
        access_token : AccessToken

        account_id : str
            The Plaid `account_id` of the account that is the funding source for the proposed transaction. The `account_id` is returned in the `/accounts/get` endpoint as well as the [`onSuccess`](/docs/link/ios/#link-ios-onsuccess-linkSuccess-metadata-accounts-id) callback metadata.

            This will return an [`INVALID_ACCOUNT_ID`](/docs/errors/invalid-input/#invalid_account_id) error if the account has been removed at the bank or if the `account_id` is no longer valid.

        amount : float
            The transaction amount, in USD (e.g. `102.05`)

        client_transaction_id : str
            The unique ID that you would like to use to refer to this transaction. For your convenience mapping your internal data, you could use your internal ID/identifier for this transaction. The max length for this field is 36 characters.

        client_id : typing.Optional[ApiClientId]

        client_user_id : typing.Optional[str]
            A unique ID that identifies the end user in your system. This ID is used to correlate requests by a user with multiple Items. The max length for this field is 36 characters. Personally identifiable information, such as an email address or phone number, should not be used in the `client_user_id`.

        default_payment_method : typing.Optional[str]
            The default ACH or non-ACH payment method to complete the transaction.
            `SAME_DAY_ACH`: Same Day ACH by NACHA. The debit transaction is processed and settled on the same day
            `NEXT_DAY_ACH`: Next Day ACH settlement for debit transactions, offered by some payment processors
            `STANDARD_ACH`: standard ACH by NACHA
            `REAL_TIME_PAYMENTS`: real-time payments such as RTP and FedNow
            `DEBIT_CARD`: if the default payment is over debit card networks
            `MULTIPLE_PAYMENT_METHODS`: if there is no default debit rail or there are multiple payment methods
            Possible values:  `SAME_DAY_ACH`, `NEXT_DAY_ACH`, `STANDARD_ACH`, `REAL_TIME_PAYMENTS`, `DEBIT_CARD`, `MULTIPLE_PAYMENT_METHODS`

        device : typing.Optional[SignalDevice]

        is_recurring : typing.Optional[bool]
            `true` if the ACH transaction is a recurring transaction; `false` otherwise

        secret : typing.Optional[ApiSecret]

        user : typing.Optional[SignalUser]

        user_present : typing.Optional[bool]
            `true` if the end user is present while initiating the ACH transfer and the endpoint is being called; `false` otherwise (for example, when the ACH transfer is scheduled and the end user is not present, or you call this endpoint after the ACH transfer but before submitting the Nacha file for ACH processing).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SignalEvaluateResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.signal_evaluate(
            access_token="access_token",
            account_id="account_id",
            amount=1.1,
            client_transaction_id="client_transaction_id",
        )
        """
        _response = self._raw_client.signal_evaluate(
            access_token=access_token,
            account_id=account_id,
            amount=amount,
            client_transaction_id=client_transaction_id,
            client_id=client_id,
            client_user_id=client_user_id,
            default_payment_method=default_payment_method,
            device=device,
            is_recurring=is_recurring,
            secret=secret,
            user=user,
            user_present=user_present,
            request_options=request_options,
        )
        return _response.data

    def signal_prepare(
        self,
        *,
        access_token: AccessToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SignalPrepareResponse:
        """
        When Link is not initialized with Signal, call `/signal/prepare` to opt-in that Item to the Signal data collection process, developing a Signal score.

        If you are using other Plaid products after Link, e.g. Identity or Assets, call `/signal/prepare` after those product calls are complete.

        Example flow: Link is initialized with Auth, call `/auth/get` for the account and routing number, call `/identity/get` to retrieve bank ownership details, then call `/signal/prepare` to begin Signal data collection. Later, once you have obtained details about the proposed transaction from the user, call `/signal/evaluate` for a Signal score. For more information please see [Recommendations for initializing Link with specific product combinations](https://www.plaid.com/docs/link/initializing-products/#recommendations-for-initializing-link-with-specific-product-combinations).

        Parameters
        ----------
        access_token : AccessToken

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SignalPrepareResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.signal_prepare(
            access_token="access_token",
        )
        """
        _response = self._raw_client.signal_prepare(
            access_token=access_token, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def signal_return_report(
        self,
        *,
        client_transaction_id: str,
        return_code: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        returned_at: typing.Optional[dt.datetime] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SignalReturnReportResponse:
        """
        Call the `/signal/return/report` endpoint to report a returned transaction that was previously sent to the `/signal/evaluate` endpoint. Your feedback will be used by the model to incorporate the latest risk trend in your portfolio.

        Parameters
        ----------
        client_transaction_id : str
            Must be the same as the `client_transaction_id` supplied when calling `/signal/evaluate`

        return_code : str
            Must be a valid ACH return code (e.g. "R01")

            If formatted incorrectly, this will result in an [`INVALID_FIELD`](/docs/errors/invalid-request/#invalid_field) error.

        client_id : typing.Optional[ApiClientId]

        returned_at : typing.Optional[dt.datetime]
            Date and time when you receive the returns from your payment processors, in ISO 8601 format (`YYYY-MM-DDTHH:mm:ssZ`).

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SignalReturnReportResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.signal_return_report(
            client_transaction_id="client_transaction_id",
            return_code="return_code",
        )
        """
        _response = self._raw_client.signal_return_report(
            client_transaction_id=client_transaction_id,
            return_code=return_code,
            client_id=client_id,
            returned_at=returned_at,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def transactions_enrich(
        self,
        *,
        account_type: str,
        transactions: typing.Sequence[ClientProvidedTransaction],
        client_id: typing.Optional[ApiClientId] = OMIT,
        options: typing.Optional[TransactionsEnrichRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransactionsEnrichGetResponse:
        """
        The `/transactions/enrich` endpoint enriches raw transaction data generated by your own banking products or retrieved from other non-Plaid sources.

        To request access to Enrich, reach out to your Plaid point of contact or send a note to enrich-feedback@plaid.com

        Parameters
        ----------
        account_type : str
            The account type for the requested transactions (either `depository` or `credit`).

        transactions : typing.Sequence[ClientProvidedTransaction]
            An array of transaction objects to be enriched by Plaid. Maximum of 100 transactions per request.

        client_id : typing.Optional[ApiClientId]

        options : typing.Optional[TransactionsEnrichRequestOptions]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransactionsEnrichGetResponse
            OK

        Examples
        --------
        from fern import ClientProvidedTransaction, FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.transactions_enrich(
            account_type="account_type",
            transactions=[
                ClientProvidedTransaction(
                    amount=1.1,
                    description="description",
                    direction="INFLOW",
                    id="id",
                    iso_currency_code="iso_currency_code",
                )
            ],
        )
        """
        _response = self._raw_client.transactions_enrich(
            account_type=account_type,
            transactions=transactions,
            client_id=client_id,
            options=options,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def transactions_get(
        self,
        *,
        access_token: AccessToken,
        end_date: dt.date,
        start_date: dt.date,
        client_id: typing.Optional[ApiClientId] = OMIT,
        options: typing.Optional[TransactionsGetRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransactionsGetResponse:
        """
        The `/transactions/get` endpoint allows developers to receive user-authorized transaction data for credit, depository, and some loan-type accounts (only those with account subtype `student`; coverage may be limited). For transaction history from investments accounts, use the [Investments endpoint](https://plaid.com/docs/api/products/investments/) instead. Transaction data is standardized across financial institutions, and in many cases transactions are linked to a clean name, entity type, location, and category. Similarly, account data is standardized and returned with a clean name, number, balance, and other meta information where available.

        Transactions are returned in reverse-chronological order, and the sequence of transaction ordering is stable and will not shift.  Transactions are not immutable and can also be removed altogether by the institution; a removed transaction will no longer appear in `/transactions/get`.  For more details, see [Pending and posted transactions](https://plaid.com/docs/transactions/transactions-data/#pending-and-posted-transactions).

        Due to the potentially large number of transactions associated with an Item, results are paginated. Manipulate the `count` and `offset` parameters in conjunction with the `total_transactions` response body field to fetch all available transactions.

        Data returned by `/transactions/get` will be the data available for the Item as of the most recent successful check for new transactions. Plaid typically checks for new data multiple times a day, but these checks may occur less frequently, such as once a day, depending on the institution. An Item's `status.transactions.last_successful_update` field will show the timestamp of the most recent successful update. To force Plaid to check for new transactions, you can use the `/transactions/refresh` endpoint.

        Note that data may not be immediately available to `/transactions/get`. Plaid will begin to prepare transactions data upon Item link, if Link was initialized with `transactions`, or upon the first call to `/transactions/get`, if it wasn't. To be alerted when transaction data is ready to be fetched, listen for the [`INITIAL_UPDATE`](https://plaid.com/docs/api/products/transactions/#initial_update) and [`HISTORICAL_UPDATE`](https://plaid.com/docs/api/products/transactions/#historical_update) webhooks. If no transaction history is ready when `/transactions/get` is called, it will return a `PRODUCT_NOT_READY` error.

        Parameters
        ----------
        access_token : AccessToken

        end_date : dt.date
            The latest date for which data should be returned. Dates should be formatted as YYYY-MM-DD.

        start_date : dt.date
            The earliest date for which data should be returned. Dates should be formatted as YYYY-MM-DD.

        client_id : typing.Optional[ApiClientId]

        options : typing.Optional[TransactionsGetRequestOptions]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransactionsGetResponse
            OK

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.transactions_get(
            access_token="access_token",
            end_date=datetime.date.fromisoformat(
                "2023-01-15",
            ),
            start_date=datetime.date.fromisoformat(
                "2023-01-15",
            ),
        )
        """
        _response = self._raw_client.transactions_get(
            access_token=access_token,
            end_date=end_date,
            start_date=start_date,
            client_id=client_id,
            options=options,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def transactions_recurring_get(
        self,
        *,
        access_token: AccessToken,
        account_ids: typing.Sequence[str],
        client_id: typing.Optional[ApiClientId] = OMIT,
        options: typing.Optional[TransactionsRecurringGetRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransactionsRecurringGetResponse:
        """
        The `/transactions/recurring/get` endpoint allows developers to receive a summary of the recurring outflow and inflow streams (expenses and deposits) from a user’s checking, savings or credit card accounts. Additionally, Plaid provides key insights about each recurring stream including the category, merchant, last amount, and more. Developers can use these insights to build tools and experiences that help their users better manage cash flow, monitor subscriptions, reduce spend, and stay on track with bill payments.

        This endpoint is offered as an add-on to Transactions. To request access to this endpoint, submit a [product access request](https://dashboard.plaid.com/team/products) or contact your Plaid account manager.

        This endpoint can only be called on an Item that has already been initialized with Transactions (either during Link, by specifying it in `/link/token/create`; or after Link, by calling `/transactions/get` or `/transactions/sync`). Once all historical transactions have been fetched, call `/transactions/recurring/get` to receive the Recurring Transactions streams and subscribe to the [`RECURRING_TRANSACTIONS_UPDATE`](https://plaid.com/docs/api/products/transactions/#recurring_transactions_update) webhook. To know when historical transactions have been fetched, if you are using `/transactions/sync` listen for the [`SYNC_UPDATES_AVAILABLE`](https://plaid.com/docs/api/products/transactions/#SyncUpdatesAvailableWebhook-historical-update-complete) webhook and check that the `historical_update_complete` field in the payload is `true`. If using `/transactions/get`, listen for the [`HISTORICAL_UPDATE`](https://plaid.com/docs/api/products/transactions/#historical_update) webhook.

        After the initial call, you can call `/transactions/recurring/get` endpoint at any point in the future to retrieve the latest summary of recurring streams. Listen to the [`RECURRING_TRANSACTIONS_UPDATE`](https://plaid.com/docs/api/products/transactions/#recurring_transactions_update) webhook to be notified when new updates are available.

        Parameters
        ----------
        access_token : AccessToken

        account_ids : typing.Sequence[str]
            A list of `account_ids` to retrieve for the Item

            Note: An error will be returned if a provided `account_id` is not associated with the Item.

        client_id : typing.Optional[ApiClientId]

        options : typing.Optional[TransactionsRecurringGetRequestOptions]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransactionsRecurringGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.transactions_recurring_get(
            access_token="access_token",
            account_ids=["account_ids"],
        )
        """
        _response = self._raw_client.transactions_recurring_get(
            access_token=access_token,
            account_ids=account_ids,
            client_id=client_id,
            options=options,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def transactions_refresh(
        self,
        *,
        access_token: AccessToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransactionsRefreshResponse:
        """
        `/transactions/refresh` is an optional endpoint for users of the Transactions product. It initiates an on-demand extraction to fetch the newest transactions for an Item. This on-demand extraction takes place in addition to the periodic extractions that automatically occur multiple times a day for any Transactions-enabled Item. If changes to transactions are discovered after calling `/transactions/refresh`, Plaid will fire a webhook: for `/transactions/sync` users, [`SYNC_UPDATES_AVAILABLE`](https://plaid.com/docs/api/products/transactions/#sync_updates_available) will be fired if there are any transactions updated, added, or removed. For users of both `/transactions/sync` and `/transactions/get`, [`TRANSACTIONS_REMOVED`](https://plaid.com/docs/api/products/transactions/#transactions_removed) will be fired if any removed transactions are detected, and [`DEFAULT_UPDATE`](https://plaid.com/docs/api/products/transactions/#default_update) will be fired if any new transactions are detected. New transactions can be fetched by calling `/transactions/get` or `/transactions/sync`. Note that the `/transactions/refresh` endpoint is not supported for Capital One (`ins_128026`) and will result in a `PRODUCT_NOT_SUPPORTED` error if called on an Item from that institution.

        `/transactions/refresh` is offered as an add-on to Transactions and has a separate [fee model](/docs/account/billing/#per-request-flat-fee). To request access to this endpoint, submit a [product access request](https://dashboard.plaid.com/team/products) or contact your Plaid account manager.

        Parameters
        ----------
        access_token : AccessToken

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransactionsRefreshResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.transactions_refresh(
            access_token="access_token",
        )
        """
        _response = self._raw_client.transactions_refresh(
            access_token=access_token, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def transactions_sync(
        self,
        *,
        access_token: AccessToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        count: typing.Optional[int] = OMIT,
        cursor: typing.Optional[str] = OMIT,
        options: typing.Optional[TransactionsSyncRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransactionsSyncResponse:
        """
        This endpoint replaces `/transactions/get` and its associated webhooks for most common use-cases.

        The `/transactions/sync` endpoint allows developers to subscribe to all transactions associated with an Item and get updates synchronously in a stream-like manner, using a cursor to track which updates have already been seen. `/transactions/sync` provides the same functionality as `/transactions/get` and can be used instead of `/transactions/get` to simplify the process of tracking transactions updates.

        This endpoint provides user-authorized transaction data for `credit`, `depository`, and some loan-type accounts (only those with account subtype `student`; coverage may be limited). For transaction history from `investments` accounts, use `/investments/transactions/get` instead.

        Returned transactions data is grouped into three types of update, indicating whether the transaction was added, removed, or modified since the last call to the API.

        In the first call to `/transactions/sync` for an Item, the endpoint will return all historical transactions data associated with that Item up until the time of the API call (as "adds"), which then generates a `next_cursor` for that Item. In subsequent calls, send the `next_cursor` to receive only the changes that have occurred since the previous call.

        Due to the potentially large number of transactions associated with an Item, results are paginated. The `has_more` field specifies if additional calls are necessary to fetch all available transaction updates. Call `/transactions/sync` with the new cursor, pulling all updates, until `has_more` is `false`.

        When retrieving paginated updates, track both the `next_cursor` from the latest response and the original cursor from the first call in which `has_more` was `true`; if a call to `/transactions/sync` fails when retrieving a paginated update, which can occur as a result of the [`TRANSACTIONS_SYNC_MUTATION_DURING_PAGINATION`](https://plaid.com/docs/errors/transactions/#transactions_sync_mutation_during_pagination) error, the entire pagination request loop must be restarted beginning with the cursor for the first page of the update, rather than retrying only the single request that failed.

        Whenever new or updated transaction data becomes available, `/transactions/sync` will provide these updates. Plaid typically checks for new data multiple times a day, but these checks may occur less frequently, such as once a day, depending on the institution. An Item's `status.transactions.last_successful_update` field will show the timestamp of the most recent successful update. To force Plaid to check for new transactions, use the `/transactions/refresh` endpoint.

        Note that for newly created Items, data may not be immediately available to `/transactions/sync`. Plaid begins preparing transactions data when the Item is created, but the process can take anywhere from a few seconds to several minutes to complete, depending on the number of transactions available.

        To be alerted when new data is available, listen for the [`SYNC_UPDATES_AVAILABLE`](https://plaid.com/docs/api/products/transactions/#sync_updates_available) webhook.

        Parameters
        ----------
        access_token : AccessToken

        client_id : typing.Optional[ApiClientId]

        count : typing.Optional[int]
            The number of transaction updates to fetch.

        cursor : typing.Optional[str]
            The cursor value represents the last update requested. Providing it will cause the response to only return changes after this update.
            If omitted, the entire history of updates will be returned, starting with the first-added transactions on the item.
            Note: The upper-bound length of this cursor is 256 characters of base64.

        options : typing.Optional[TransactionsSyncRequestOptions]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransactionsSyncResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.transactions_sync(
            access_token="access_token",
        )
        """
        _response = self._raw_client.transactions_sync(
            access_token=access_token,
            client_id=client_id,
            count=count,
            cursor=cursor,
            options=options,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def transfer_authorization_create(
        self,
        *,
        amount: TransferAmount,
        network: TransferNetwork,
        type: TransferType,
        user: TransferAuthorizationUserInRequest,
        access_token: typing.Optional[TransferAccessToken] = OMIT,
        account_id: typing.Optional[TransferAccountId] = OMIT,
        ach_class: typing.Optional[AchClass] = OMIT,
        beacon_session_id: typing.Optional[str] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        device: typing.Optional[TransferAuthorizationDevice] = OMIT,
        funding_account_id: typing.Optional[TransferFundingAccountIdRequest] = OMIT,
        idempotency_key: typing.Optional[TransferAuthorizationIdempotencyKey] = OMIT,
        iso_currency_code: typing.Optional[str] = OMIT,
        origination_account_id: typing.Optional[str] = OMIT,
        originator_client_id: typing.Optional[str] = OMIT,
        payment_profile_token: typing.Optional[TransferPaymentProfileToken] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        user_present: typing.Optional[bool] = OMIT,
        with_guarantee: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferAuthorizationCreateResponse:
        """
        Use the `/transfer/authorization/create` endpoint to determine transfer failure risk.

        In Plaid's Sandbox environment the decisions will be returned as follows:

          - To approve a transfer with null rationale code, make an authorization request with an `amount` less than the available balance in the account.

          - To approve a transfer with the rationale code `MANUALLY_VERIFIED_ITEM`, create an Item in Link through the [Same Day Micro-deposits flow](https://plaid.com/docs/auth/coverage/testing/#testing-same-day-micro-deposits).

          - To approve a transfer with the rationale code `ITEM_LOGIN_REQUIRED`, [reset the login for an Item](https://plaid.com/docs/sandbox/#item_login_required).

          - To decline a transfer with the rationale code `NSF`, the available balance on the account must be less than the authorization `amount`. See [Create Sandbox test data](https://plaid.com/docs/sandbox/user-custom/) for details on how to customize data in Sandbox.

          - To decline a transfer with the rationale code `RISK`, the available balance on the account must be exactly $0. See [Create Sandbox test data](https://plaid.com/docs/sandbox/user-custom/) for details on how to customize data in Sandbox.

        `device.ip_address`, `device.user_agent` are required fields.

        For [Guarantee](https://www.plaid.com/docs//transfer/guarantee/), the following fields are required : `idempotency_key`, `user.phone_number` (optional if `email_address` provided), `user.email_address` (optional if `phone_number` provided), `device.ip_address`, `device.user_agent`, and `user_present`.

        Parameters
        ----------
        amount : TransferAmount

        network : TransferNetwork

        type : TransferType

        user : TransferAuthorizationUserInRequest

        access_token : typing.Optional[TransferAccessToken]

        account_id : typing.Optional[TransferAccountId]

        ach_class : typing.Optional[AchClass]

        beacon_session_id : typing.Optional[str]
            The unique identifier returned by Plaid's [beacon](https://plaid.com/docs/transfer/guarantee/#using-a-beacon) when it is run on your webpage. Required for Guarantee customers who are not using [Transfer UI](https://plaid.com/docs/transfer/using-transfer-ui/) and have a web checkout experience.

        client_id : typing.Optional[ApiClientId]

        device : typing.Optional[TransferAuthorizationDevice]

        funding_account_id : typing.Optional[TransferFundingAccountIdRequest]

        idempotency_key : typing.Optional[TransferAuthorizationIdempotencyKey]

        iso_currency_code : typing.Optional[str]
            The currency of the transfer amount. The default value is "USD".

        origination_account_id : typing.Optional[str]
            Plaid's unique identifier for the origination account for this authorization. If not specified, the default account will be used.

        originator_client_id : typing.Optional[str]
            The Plaid client ID that is the originator of this transfer. Only needed if creating transfers on behalf of another client as a third-party sender (TPS).

        payment_profile_token : typing.Optional[TransferPaymentProfileToken]

        secret : typing.Optional[ApiSecret]

        user_present : typing.Optional[bool]
            Required for Guarantee. If the end user is initiating the specific transfer themselves via an interactive UI, this should be `true`; for automatic recurring payments where the end user is not actually initiating each individual transfer, it should be `false`.

        with_guarantee : typing.Optional[bool]
            If set to `false`, Plaid will not offer a `guarantee_decision` for this request(Guarantee customers only).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferAuthorizationCreateResponse
            OK

        Examples
        --------
        from fern import FernApi, TransferAuthorizationUserInRequest

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.transfer_authorization_create(
            amount="amount",
            network="ach",
            type="debit",
            user=TransferAuthorizationUserInRequest(
                legal_name="legal_name",
            ),
        )
        """
        _response = self._raw_client.transfer_authorization_create(
            amount=amount,
            network=network,
            type=type,
            user=user,
            access_token=access_token,
            account_id=account_id,
            ach_class=ach_class,
            beacon_session_id=beacon_session_id,
            client_id=client_id,
            device=device,
            funding_account_id=funding_account_id,
            idempotency_key=idempotency_key,
            iso_currency_code=iso_currency_code,
            origination_account_id=origination_account_id,
            originator_client_id=originator_client_id,
            payment_profile_token=payment_profile_token,
            secret=secret,
            user_present=user_present,
            with_guarantee=with_guarantee,
            request_options=request_options,
        )
        return _response.data

    def transfer_cancel(
        self,
        *,
        transfer_id: TransferId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        originator_client_id: typing.Optional[str] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferCancelResponse:
        """
        Use the `/transfer/cancel` endpoint to cancel a transfer.  A transfer is eligible for cancellation if the `cancellable` property returned by `/transfer/get` is `true`.

        Parameters
        ----------
        transfer_id : TransferId

        client_id : typing.Optional[ApiClientId]

        originator_client_id : typing.Optional[str]
            The Plaid client ID of the transfer originator. Should only be present if `client_id` is a third-party sender (TPS).

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferCancelResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.transfer_cancel(
            transfer_id="transfer_id",
        )
        """
        _response = self._raw_client.transfer_cancel(
            transfer_id=transfer_id,
            client_id=client_id,
            originator_client_id=originator_client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def transfer_capabilities_get(
        self,
        *,
        access_token: typing.Optional[TransferAccessToken] = OMIT,
        account_id: typing.Optional[TransferAccountId] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        payment_profile_token: typing.Optional[PaymentProfileToken] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferCapabilitiesGetResponse:
        """
        Use the `/transfer/capabilities/get` endpoint to determine the RTP eligibility information of a transfer.

        Parameters
        ----------
        access_token : typing.Optional[TransferAccessToken]

        account_id : typing.Optional[TransferAccountId]

        client_id : typing.Optional[ApiClientId]

        payment_profile_token : typing.Optional[PaymentProfileToken]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferCapabilitiesGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.transfer_capabilities_get()
        """
        _response = self._raw_client.transfer_capabilities_get(
            access_token=access_token,
            account_id=account_id,
            client_id=client_id,
            payment_profile_token=payment_profile_token,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def transfer_configuration_get(
        self,
        *,
        client_id: typing.Optional[ApiClientId] = OMIT,
        originator_client_id: typing.Optional[str] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferConfigurationGetResponse:
        """
        Use the `/transfer/configuration/get` endpoint to view your transfer product configurations.

        Parameters
        ----------
        client_id : typing.Optional[ApiClientId]

        originator_client_id : typing.Optional[str]
            The Plaid client ID of the transfer originator. Should only be present if `client_id` is a third-party sender (TPS).

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferConfigurationGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.transfer_configuration_get()
        """
        _response = self._raw_client.transfer_configuration_get(
            client_id=client_id,
            originator_client_id=originator_client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def transfer_create(
        self,
        *,
        authorization_id: str,
        description: str,
        access_token: typing.Optional[TransferAccessToken] = OMIT,
        account_id: typing.Optional[TransferAccountId] = OMIT,
        ach_class: typing.Optional[AchClass] = OMIT,
        amount: typing.Optional[TransferAmount] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        idempotency_key: typing.Optional[TransferCreateIdempotencyKey] = OMIT,
        iso_currency_code: typing.Optional[str] = OMIT,
        metadata: typing.Optional[TransferMetadata] = OMIT,
        network: typing.Optional[TransferNetwork] = OMIT,
        origination_account_id: typing.Optional[str] = OMIT,
        payment_profile_token: typing.Optional[TransferPaymentProfileToken] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        type: typing.Optional[TransferType] = OMIT,
        user: typing.Optional[TransferUserInRequestDeprecated] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferCreateResponse:
        """
        Use the `/transfer/create` endpoint to initiate a new transfer.

        Parameters
        ----------
        authorization_id : str
            Plaid’s unique identifier for a transfer authorization. This parameter also serves the purpose of acting as an idempotency identifier.

        description : str
            The transfer description. Maximum of 10 characters. If reprocessing a returned transfer, please note that the `description` field must be `"Retry"` to indicate that it's a retry of a previously returned transfer. You may retry a transfer up to 2 times, within 180 days of creating the original transfer. Only transfers that were returned with code `R01` or `R09` may be retried. For a full listing of ACH return codes, see [Transfer errors](https://plaid.com/docs/errors/transfer/#ach-return-codes).

        access_token : typing.Optional[TransferAccessToken]

        account_id : typing.Optional[TransferAccountId]

        ach_class : typing.Optional[AchClass]

        amount : typing.Optional[TransferAmount]

        client_id : typing.Optional[ApiClientId]

        idempotency_key : typing.Optional[TransferCreateIdempotencyKey]

        iso_currency_code : typing.Optional[str]
            The currency of the transfer amount. The default value is "USD".

        metadata : typing.Optional[TransferMetadata]

        network : typing.Optional[TransferNetwork]

        origination_account_id : typing.Optional[str]
            Plaid’s unique identifier for the origination account for this transfer. If you have more than one origination account, this value must be specified. Otherwise, this field should be left blank.

        payment_profile_token : typing.Optional[TransferPaymentProfileToken]

        secret : typing.Optional[ApiSecret]

        type : typing.Optional[TransferType]

        user : typing.Optional[TransferUserInRequestDeprecated]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferCreateResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.transfer_create(
            authorization_id="authorization_id",
            description="description",
        )
        """
        _response = self._raw_client.transfer_create(
            authorization_id=authorization_id,
            description=description,
            access_token=access_token,
            account_id=account_id,
            ach_class=ach_class,
            amount=amount,
            client_id=client_id,
            idempotency_key=idempotency_key,
            iso_currency_code=iso_currency_code,
            metadata=metadata,
            network=network,
            origination_account_id=origination_account_id,
            payment_profile_token=payment_profile_token,
            secret=secret,
            type=type,
            user=user,
            request_options=request_options,
        )
        return _response.data

    def transfer_event_list(
        self,
        *,
        account_id: typing.Optional[str] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        count: typing.Optional[int] = OMIT,
        end_date: typing.Optional[dt.datetime] = OMIT,
        event_types: typing.Optional[typing.Sequence[TransferEventType]] = OMIT,
        funding_account_id: typing.Optional[str] = OMIT,
        offset: typing.Optional[int] = OMIT,
        origination_account_id: typing.Optional[str] = OMIT,
        originator_client_id: typing.Optional[str] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        start_date: typing.Optional[dt.datetime] = OMIT,
        sweep_id: typing.Optional[str] = OMIT,
        transfer_id: typing.Optional[str] = OMIT,
        transfer_type: typing.Optional[TransferEventListTransferType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferEventListResponse:
        """
        Use the `/transfer/event/list` endpoint to get a list of transfer events based on specified filter criteria.

        Parameters
        ----------
        account_id : typing.Optional[str]
            The account ID to get events for all transactions to/from an account.

        client_id : typing.Optional[ApiClientId]

        count : typing.Optional[int]
            The maximum number of transfer events to return. If the number of events matching the above parameters is greater than `count`, the most recent events will be returned.

        end_date : typing.Optional[dt.datetime]
            The end datetime of transfers to list. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`)

        event_types : typing.Optional[typing.Sequence[TransferEventType]]
            Filter events by event type.

        funding_account_id : typing.Optional[str]
            Filter transfer events to only those with the specified `funding_account_id`.

        offset : typing.Optional[int]
            The offset into the list of transfer events. When `count`=25 and `offset`=0, the first 25 events will be returned. When `count`=25 and `offset`=25, the next 25 events will be returned.

        origination_account_id : typing.Optional[str]
            The origination account ID to get events for transfers from a specific origination account.

        originator_client_id : typing.Optional[str]
            Filter transfer events to only those with the specified originator client.

        secret : typing.Optional[ApiSecret]

        start_date : typing.Optional[dt.datetime]
            The start datetime of transfers to list. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`)

        sweep_id : typing.Optional[str]
            Plaid’s unique identifier for a sweep.

        transfer_id : typing.Optional[str]
            Plaid’s unique identifier for a transfer.

        transfer_type : typing.Optional[TransferEventListTransferType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferEventListResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.transfer_event_list()
        """
        _response = self._raw_client.transfer_event_list(
            account_id=account_id,
            client_id=client_id,
            count=count,
            end_date=end_date,
            event_types=event_types,
            funding_account_id=funding_account_id,
            offset=offset,
            origination_account_id=origination_account_id,
            originator_client_id=originator_client_id,
            secret=secret,
            start_date=start_date,
            sweep_id=sweep_id,
            transfer_id=transfer_id,
            transfer_type=transfer_type,
            request_options=request_options,
        )
        return _response.data

    def transfer_event_sync(
        self,
        *,
        after_id: int,
        client_id: typing.Optional[ApiClientId] = OMIT,
        count: typing.Optional[int] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferEventSyncResponse:
        """
        `/transfer/event/sync` allows you to request up to the next 25 transfer events that happened after a specific `event_id`. Use the `/transfer/event/sync` endpoint to guarantee you have seen all transfer events. When using Auth with micro-deposit verification enabled, this endpoint can be used to fetch status updates on ACH micro-deposits. For more details, see [micro-deposit events](https://www.plaid.com/docs/auth/coverage/microdeposit-events/).

        Parameters
        ----------
        after_id : int
            The latest (largest) `event_id` fetched via the sync endpoint, or 0 initially.

        client_id : typing.Optional[ApiClientId]

        count : typing.Optional[int]
            The maximum number of transfer events to return.

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferEventSyncResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.transfer_event_sync(
            after_id=1,
        )
        """
        _response = self._raw_client.transfer_event_sync(
            after_id=after_id, client_id=client_id, count=count, secret=secret, request_options=request_options
        )
        return _response.data

    def transfer_get(
        self,
        *,
        transfer_id: TransferId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        originator_client_id: typing.Optional[str] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferGetResponse:
        """
        The `/transfer/get` endpoint fetches information about the transfer corresponding to the given `transfer_id`.

        Parameters
        ----------
        transfer_id : TransferId

        client_id : typing.Optional[ApiClientId]

        originator_client_id : typing.Optional[str]
            The Plaid client ID of the transfer originator. Should only be present if `client_id` is a third-party sender (TPS).

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.transfer_get(
            transfer_id="transfer_id",
        )
        """
        _response = self._raw_client.transfer_get(
            transfer_id=transfer_id,
            client_id=client_id,
            originator_client_id=originator_client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def transfer_intent_create(
        self,
        *,
        amount: TransferAmount,
        description: str,
        mode: TransferIntentCreateMode,
        user: TransferUserInRequest,
        account_id: typing.Optional[str] = OMIT,
        ach_class: typing.Optional[AchClass] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        funding_account_id: typing.Optional[TransferFundingAccountIdRequest] = OMIT,
        iso_currency_code: typing.Optional[str] = OMIT,
        metadata: typing.Optional[TransferMetadata] = OMIT,
        network: typing.Optional[TransferIntentCreateNetwork] = OMIT,
        origination_account_id: typing.Optional[str] = OMIT,
        require_guarantee: typing.Optional[bool] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferIntentCreateResponse:
        """
        Use the `/transfer/intent/create` endpoint to generate a transfer intent object and invoke the Transfer UI.

        Parameters
        ----------
        amount : TransferAmount

        description : str
            A description for the underlying transfer. Maximum of 8 characters.

        mode : TransferIntentCreateMode

        user : TransferUserInRequest

        account_id : typing.Optional[str]
            The Plaid `account_id` corresponding to the end-user account that will be debited or credited.

        ach_class : typing.Optional[AchClass]

        client_id : typing.Optional[ApiClientId]

        funding_account_id : typing.Optional[TransferFundingAccountIdRequest]

        iso_currency_code : typing.Optional[str]
            The currency of the transfer amount, e.g. "USD"

        metadata : typing.Optional[TransferMetadata]

        network : typing.Optional[TransferIntentCreateNetwork]

        origination_account_id : typing.Optional[str]
            Plaid’s unique identifier for the origination account for the intent. If not provided, the default account will be used.

        require_guarantee : typing.Optional[bool]
            When `true`, the transfer requires a `GUARANTEED` decision by Plaid to proceed (Guarantee customers only).

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferIntentCreateResponse
            OK

        Examples
        --------
        from fern import FernApi, TransferUserInRequest

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.transfer_intent_create(
            amount="amount",
            description="description",
            mode="PAYMENT",
            user=TransferUserInRequest(
                legal_name="legal_name",
            ),
        )
        """
        _response = self._raw_client.transfer_intent_create(
            amount=amount,
            description=description,
            mode=mode,
            user=user,
            account_id=account_id,
            ach_class=ach_class,
            client_id=client_id,
            funding_account_id=funding_account_id,
            iso_currency_code=iso_currency_code,
            metadata=metadata,
            network=network,
            origination_account_id=origination_account_id,
            require_guarantee=require_guarantee,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def transfer_intent_get(
        self,
        *,
        transfer_intent_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferIntentGetResponse:
        """
        Use the `/transfer/intent/get` endpoint to retrieve more information about a transfer intent.

        Parameters
        ----------
        transfer_intent_id : str
            Plaid's unique identifier for a transfer intent object.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferIntentGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.transfer_intent_get(
            transfer_intent_id="transfer_intent_id",
        )
        """
        _response = self._raw_client.transfer_intent_get(
            transfer_intent_id=transfer_intent_id, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def transfer_list(
        self,
        *,
        client_id: typing.Optional[ApiClientId] = OMIT,
        count: typing.Optional[int] = OMIT,
        end_date: typing.Optional[dt.datetime] = OMIT,
        funding_account_id: typing.Optional[str] = OMIT,
        offset: typing.Optional[int] = OMIT,
        origination_account_id: typing.Optional[str] = OMIT,
        originator_client_id: typing.Optional[str] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        start_date: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferListResponse:
        """
        Use the `/transfer/list` endpoint to see a list of all your transfers and their statuses. Results are paginated; use the `count` and `offset` query parameters to retrieve the desired transfers.

        Parameters
        ----------
        client_id : typing.Optional[ApiClientId]

        count : typing.Optional[int]
            The maximum number of transfers to return.

        end_date : typing.Optional[dt.datetime]
            The end datetime of transfers to list. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`)

        funding_account_id : typing.Optional[str]
            Filter transfers to only those with the specified `funding_account_id`.

        offset : typing.Optional[int]
            The number of transfers to skip before returning results.

        origination_account_id : typing.Optional[str]
            Filter transfers to only those originated through the specified origination account.

        originator_client_id : typing.Optional[str]
            Filter transfers to only those with the specified originator client.

        secret : typing.Optional[ApiSecret]

        start_date : typing.Optional[dt.datetime]
            The start datetime of transfers to list. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferListResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.transfer_list()
        """
        _response = self._raw_client.transfer_list(
            client_id=client_id,
            count=count,
            end_date=end_date,
            funding_account_id=funding_account_id,
            offset=offset,
            origination_account_id=origination_account_id,
            originator_client_id=originator_client_id,
            secret=secret,
            start_date=start_date,
            request_options=request_options,
        )
        return _response.data

    def transfer_metrics_get(
        self,
        *,
        client_id: typing.Optional[ApiClientId] = OMIT,
        originator_client_id: typing.Optional[str] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferMetricsGetResponse:
        """
        Use the `/transfer/metrics/get` endpoint to view your transfer product usage metrics.

        Parameters
        ----------
        client_id : typing.Optional[ApiClientId]

        originator_client_id : typing.Optional[str]
            The Plaid client ID of the transfer originator. Should only be present if `client_id` is a third-party sender (TPS).

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferMetricsGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.transfer_metrics_get()
        """
        _response = self._raw_client.transfer_metrics_get(
            client_id=client_id,
            originator_client_id=originator_client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def transfer_migrate_account(
        self,
        *,
        account_number: str,
        account_type: str,
        routing_number: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        wire_routing_number: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferMigrateAccountResponse:
        """
        As an alternative to adding Items via Link, you can also use the `/transfer/migrate_account` endpoint to migrate known account and routing numbers to Plaid Items.  Note that Items created in this way are not compatible with endpoints for other products, such as `/accounts/balance/get`, and can only be used with Transfer endpoints.  If you require access to other endpoints, create the Item through Link instead.  Access to `/transfer/migrate_account` is not enabled by default; to obtain access, contact your Plaid Account Manager.

        Parameters
        ----------
        account_number : str
            The user's account number.

        account_type : str
            The type of the bank account (`checking` or `savings`).

        routing_number : str
            The user's routing number.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        wire_routing_number : typing.Optional[str]
            The user's wire transfer routing number. This is the ABA number; for some institutions, this may differ from the ACH number used in `routing_number`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferMigrateAccountResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.transfer_migrate_account(
            account_number="account_number",
            account_type="account_type",
            routing_number="routing_number",
        )
        """
        _response = self._raw_client.transfer_migrate_account(
            account_number=account_number,
            account_type=account_type,
            routing_number=routing_number,
            client_id=client_id,
            secret=secret,
            wire_routing_number=wire_routing_number,
            request_options=request_options,
        )
        return _response.data

    def transfer_originator_create(
        self,
        *,
        company_name: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferOriginatorCreateResponse:
        """
        Use the `/transfer/originator/create` endpoint to create a new originator and return an `originator_client_id`.

        Parameters
        ----------
        company_name : str
            The company name of the end customer being created. This will be displayed in public-facing surfaces, e.g. Plaid Dashboard.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferOriginatorCreateResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.transfer_originator_create(
            company_name="company_name",
        )
        """
        _response = self._raw_client.transfer_originator_create(
            company_name=company_name, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def transfer_originator_get(
        self,
        *,
        originator_client_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferOriginatorGetResponse:
        """
        The `/transfer/originator/get` endpoint gets status updates for an originator's onboarding process. This information is also available via the Transfer page on the Plaid dashboard.

        Parameters
        ----------
        originator_client_id : str
            Client ID of the end customer (i.e. the originator).

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferOriginatorGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.transfer_originator_get(
            originator_client_id="originator_client_id",
        )
        """
        _response = self._raw_client.transfer_originator_get(
            originator_client_id=originator_client_id,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def transfer_originator_list(
        self,
        *,
        client_id: typing.Optional[ApiClientId] = OMIT,
        count: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferOriginatorListResponse:
        """
        The `/transfer/originator/list` endpoint gets status updates for all of your originators' onboarding. This information is also available via the Plaid dashboard.

        Parameters
        ----------
        client_id : typing.Optional[ApiClientId]

        count : typing.Optional[int]
            The maximum number of originators to return.

        offset : typing.Optional[int]
            The number of originators to skip before returning results.

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferOriginatorListResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.transfer_originator_list()
        """
        _response = self._raw_client.transfer_originator_list(
            client_id=client_id, count=count, offset=offset, secret=secret, request_options=request_options
        )
        return _response.data

    def transfer_questionnaire_create(
        self,
        *,
        originator_client_id: str,
        redirect_uri: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferQuestionnaireCreateResponse:
        """
        The `/transfer/questionnaire/create` endpoint generates a Plaid-hosted onboarding UI URL. Redirect the originator to this URL to provide their due diligence information and agree to Plaid’s terms for ACH money movement.

        Parameters
        ----------
        originator_client_id : str
            Client ID of the end customer.

        redirect_uri : str
            URL the end customer will be redirected to after completing questions in Plaid-hosted onboarding flow.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferQuestionnaireCreateResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.transfer_questionnaire_create(
            originator_client_id="originator_client_id",
            redirect_uri="redirect_uri",
        )
        """
        _response = self._raw_client.transfer_questionnaire_create(
            originator_client_id=originator_client_id,
            redirect_uri=redirect_uri,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def transfer_recurring_cancel(
        self,
        *,
        recurring_transfer_id: RecurringTransferId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferRecurringCancelResponse:
        """
        Use the `/transfer/recurring/cancel` endpoint to cancel a recurring transfer.  Scheduled transfer that hasn't been submitted to bank will be cancelled.

        Parameters
        ----------
        recurring_transfer_id : RecurringTransferId

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferRecurringCancelResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.transfer_recurring_cancel(
            recurring_transfer_id="recurring_transfer_id",
        )
        """
        _response = self._raw_client.transfer_recurring_cancel(
            recurring_transfer_id=recurring_transfer_id,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def transfer_recurring_create(
        self,
        *,
        access_token: TransferAccessToken,
        account_id: TransferAccountId,
        amount: TransferAmount,
        description: str,
        device: TransferDevice,
        idempotency_key: TransferRecurringIdempotencyKey,
        network: TransferNetwork,
        schedule: TransferRecurringSchedule,
        type: TransferType,
        user: TransferUserInRequest,
        ach_class: typing.Optional[AchClass] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        funding_account_id: typing.Optional[TransferFundingAccountIdRequest] = OMIT,
        iso_currency_code: typing.Optional[str] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        test_clock_id: typing.Optional[str] = OMIT,
        user_present: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferRecurringCreateResponse:
        """
        Use the `/transfer/recurring/create` endpoint to initiate a new recurring transfer.

        Parameters
        ----------
        access_token : TransferAccessToken

        account_id : TransferAccountId

        amount : TransferAmount

        description : str
            The description of the recurring transfer.

        device : TransferDevice

        idempotency_key : TransferRecurringIdempotencyKey

        network : TransferNetwork

        schedule : TransferRecurringSchedule

        type : TransferType

        user : TransferUserInRequest

        ach_class : typing.Optional[AchClass]

        client_id : typing.Optional[ApiClientId]

        funding_account_id : typing.Optional[TransferFundingAccountIdRequest]

        iso_currency_code : typing.Optional[str]
            The currency of the transfer amount. The default value is "USD".

        secret : typing.Optional[ApiSecret]

        test_clock_id : typing.Optional[str]
            Plaid’s unique identifier for a test clock.

        user_present : typing.Optional[bool]
            If the end user is initiating the specific transfer themselves via an interactive UI, this should be `true`; for automatic recurring payments where the end user is not actually initiating each individual transfer, it should be `false`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferRecurringCreateResponse
            OK

        Examples
        --------
        import datetime

        from fern import (
            FernApi,
            TransferDevice,
            TransferRecurringSchedule,
            TransferUserInRequest,
        )

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.transfer_recurring_create(
            access_token="access_token",
            account_id="account_id",
            amount="amount",
            description="description",
            device=TransferDevice(
                ip_address="ip_address",
                user_agent="user_agent",
            ),
            idempotency_key="idempotency_key",
            network="ach",
            schedule=TransferRecurringSchedule(
                interval_count=1,
                interval_execution_day=1,
                interval_unit="week",
                start_date=datetime.date.fromisoformat(
                    "2023-01-15",
                ),
            ),
            type="debit",
            user=TransferUserInRequest(
                legal_name="legal_name",
            ),
        )
        """
        _response = self._raw_client.transfer_recurring_create(
            access_token=access_token,
            account_id=account_id,
            amount=amount,
            description=description,
            device=device,
            idempotency_key=idempotency_key,
            network=network,
            schedule=schedule,
            type=type,
            user=user,
            ach_class=ach_class,
            client_id=client_id,
            funding_account_id=funding_account_id,
            iso_currency_code=iso_currency_code,
            secret=secret,
            test_clock_id=test_clock_id,
            user_present=user_present,
            request_options=request_options,
        )
        return _response.data

    def transfer_recurring_get(
        self,
        *,
        recurring_transfer_id: RecurringTransferId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferRecurringGetResponse:
        """
        The `/transfer/recurring/get` fetches information about the recurring transfer corresponding to the given `recurring_transfer_id`.

        Parameters
        ----------
        recurring_transfer_id : RecurringTransferId

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferRecurringGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.transfer_recurring_get(
            recurring_transfer_id="recurring_transfer_id",
        )
        """
        _response = self._raw_client.transfer_recurring_get(
            recurring_transfer_id=recurring_transfer_id,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def transfer_recurring_list(
        self,
        *,
        client_id: typing.Optional[ApiClientId] = OMIT,
        count: typing.Optional[int] = OMIT,
        end_time: typing.Optional[dt.datetime] = OMIT,
        funding_account_id: typing.Optional[str] = OMIT,
        offset: typing.Optional[int] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        start_time: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferRecurringListResponse:
        """
        Use the `/transfer/recurring/list` endpoint to see a list of all your recurring transfers and their statuses. Results are paginated; use the `count` and `offset` query parameters to retrieve the desired recurring transfers.

        Parameters
        ----------
        client_id : typing.Optional[ApiClientId]

        count : typing.Optional[int]
            The maximum number of recurring transfers to return.

        end_time : typing.Optional[dt.datetime]
            The end datetime of recurring transfers to list. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`)

        funding_account_id : typing.Optional[str]
            Filter recurring transfers to only those with the specified `funding_account_id`.

        offset : typing.Optional[int]
            The number of recurring transfers to skip before returning results.

        secret : typing.Optional[ApiSecret]

        start_time : typing.Optional[dt.datetime]
            The start datetime of recurring transfers to list. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferRecurringListResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.transfer_recurring_list()
        """
        _response = self._raw_client.transfer_recurring_list(
            client_id=client_id,
            count=count,
            end_time=end_time,
            funding_account_id=funding_account_id,
            offset=offset,
            secret=secret,
            start_time=start_time,
            request_options=request_options,
        )
        return _response.data

    def transfer_refund_cancel(
        self,
        *,
        refund_id: TransferRefundId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferRefundCancelResponse:
        """
        Use the `/transfer/refund/cancel` endpoint to cancel a refund.  A refund is eligible for cancellation if it has not yet been submitted to the payment network.

        Parameters
        ----------
        refund_id : TransferRefundId

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferRefundCancelResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.transfer_refund_cancel(
            refund_id="refund_id",
        )
        """
        _response = self._raw_client.transfer_refund_cancel(
            refund_id=refund_id, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def transfer_refund_create(
        self,
        *,
        amount: TransferRefundAmount,
        idempotency_key: TransferRefundIdempotencyKey,
        transfer_id: TransferIdForRefund,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferRefundCreateResponse:
        """
        Use the `/transfer/refund/create` endpoint to create a refund for a transfer. A transfer can be refunded if the transfer was initiated in the past 180 days.

        Processing of the refund will not occur until at least 3 business days following the transfer's settlement date, plus any hold/settlement delays. This 3-day window helps better protect your business from regular ACH returns. Consumer initiated returns (unauthorized returns) could still happen for about 60 days from the settlement date. If the original transfer is canceled, returned or failed, all pending refunds will automatically be canceled. Processed refunds cannot be revoked.

        Parameters
        ----------
        amount : TransferRefundAmount

        idempotency_key : TransferRefundIdempotencyKey

        transfer_id : TransferIdForRefund

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferRefundCreateResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.transfer_refund_create(
            amount="amount",
            idempotency_key="idempotency_key",
            transfer_id="transfer_id",
        )
        """
        _response = self._raw_client.transfer_refund_create(
            amount=amount,
            idempotency_key=idempotency_key,
            transfer_id=transfer_id,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def transfer_refund_get(
        self,
        *,
        refund_id: TransferRefundId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferRefundGetResponse:
        """
        The `/transfer/refund/get` endpoint fetches information about the refund corresponding to the given `refund_id`.

        Parameters
        ----------
        refund_id : TransferRefundId

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferRefundGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.transfer_refund_get(
            refund_id="refund_id",
        )
        """
        _response = self._raw_client.transfer_refund_get(
            refund_id=refund_id, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def transfer_repayment_list(
        self,
        *,
        client_id: typing.Optional[ApiClientId] = OMIT,
        count: typing.Optional[int] = OMIT,
        end_date: typing.Optional[dt.datetime] = OMIT,
        offset: typing.Optional[int] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        start_date: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferRepaymentListResponse:
        """
        The `/transfer/repayment/list` endpoint fetches repayments matching the given filters. Repayments are returned in reverse-chronological order (most recent first) starting at the given `start_time`.

        Parameters
        ----------
        client_id : typing.Optional[ApiClientId]

        count : typing.Optional[int]
            The maximum number of repayments to return.

        end_date : typing.Optional[dt.datetime]
            The end datetime of repayments to return (RFC 3339 format).

        offset : typing.Optional[int]
            The number of repayments to skip before returning results.

        secret : typing.Optional[ApiSecret]

        start_date : typing.Optional[dt.datetime]
            The start datetime of repayments to return (RFC 3339 format).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferRepaymentListResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.transfer_repayment_list(
            count=1,
        )
        """
        _response = self._raw_client.transfer_repayment_list(
            client_id=client_id,
            count=count,
            end_date=end_date,
            offset=offset,
            secret=secret,
            start_date=start_date,
            request_options=request_options,
        )
        return _response.data

    def transfer_repayment_return_list(
        self,
        *,
        repayment_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        count: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferRepaymentReturnListResponse:
        """
        The `/transfer/repayment/return/list` endpoint retrieves the set of returns that were batched together into the specified repayment. The sum of amounts of returns retrieved by this request equals the amount of the repayment.

        Parameters
        ----------
        repayment_id : str
            Identifier of the repayment to query.

        client_id : typing.Optional[ApiClientId]

        count : typing.Optional[int]
            The maximum number of repayments to return.

        offset : typing.Optional[int]
            The number of repayments to skip before returning results.

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferRepaymentReturnListResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.transfer_repayment_return_list(
            count=1,
            repayment_id="d4bfce70-2470-4298-ae87-5e9b3e18bfaf",
        )
        """
        _response = self._raw_client.transfer_repayment_return_list(
            repayment_id=repayment_id,
            client_id=client_id,
            count=count,
            offset=offset,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def transfer_sweep_get(
        self,
        *,
        sweep_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferSweepGetResponse:
        """
        The `/transfer/sweep/get` endpoint fetches a sweep corresponding to the given `sweep_id`.

        Parameters
        ----------
        sweep_id : str
            Plaid’s unique identifier for a sweep.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferSweepGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.transfer_sweep_get(
            sweep_id="sweep_id",
        )
        """
        _response = self._raw_client.transfer_sweep_get(
            sweep_id=sweep_id, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def transfer_sweep_list(
        self,
        *,
        client_id: typing.Optional[ApiClientId] = OMIT,
        count: typing.Optional[int] = OMIT,
        end_date: typing.Optional[dt.datetime] = OMIT,
        funding_account_id: typing.Optional[str] = OMIT,
        offset: typing.Optional[int] = OMIT,
        originator_client_id: typing.Optional[str] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        start_date: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferSweepListResponse:
        """
        The `/transfer/sweep/list` endpoint fetches sweeps matching the given filters.

        Parameters
        ----------
        client_id : typing.Optional[ApiClientId]

        count : typing.Optional[int]
            The maximum number of sweeps to return.

        end_date : typing.Optional[dt.datetime]
            The end datetime of sweeps to return (RFC 3339 format).

        funding_account_id : typing.Optional[str]
            Filter sweeps to only those with the specified `funding_account_id`.

        offset : typing.Optional[int]
            The number of sweeps to skip before returning results.

        originator_client_id : typing.Optional[str]
            Filter sweeps to only those with the specified originator client.

        secret : typing.Optional[ApiSecret]

        start_date : typing.Optional[dt.datetime]
            The start datetime of sweeps to return (RFC 3339 format).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferSweepListResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.transfer_sweep_list()
        """
        _response = self._raw_client.transfer_sweep_list(
            client_id=client_id,
            count=count,
            end_date=end_date,
            funding_account_id=funding_account_id,
            offset=offset,
            originator_client_id=originator_client_id,
            secret=secret,
            start_date=start_date,
            request_options=request_options,
        )
        return _response.data

    def user_create(
        self,
        *,
        client_user_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UserCreateResponse:
        """
        This endpoint should be called for each of your end users before they begin a Plaid income flow. This provides you a single token to access all income data associated with the user. You should only create one per end user.

        If you call the endpoint multiple times with the same `client_user_id`, the first creation call will succeed and the rest will fail with an error message indicating that the user has been created for the given `client_user_id`.

        Ensure that you store the `user_token` along with your user's identifier in your database, as it is not possible to retrieve a previously created `user_token`.

        Parameters
        ----------
        client_user_id : str
            A unique ID representing the end user. Maximum of 128 characters. Typically this will be a user ID number from your application. Personally identifiable information, such as an email address or phone number, should not be used in the `client_user_id`.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserCreateResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.user_create(
            client_user_id="client_user_id",
        )
        """
        _response = self._raw_client.user_create(
            client_user_id=client_user_id, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def wallet_create(
        self,
        *,
        iso_currency_code: WalletIsoCurrencyCode,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WalletCreateResponse:
        """
        Create an e-wallet. The response is the newly created e-wallet object.

        Parameters
        ----------
        iso_currency_code : WalletIsoCurrencyCode

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WalletCreateResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.wallet_create(
            iso_currency_code="GBP",
        )
        """
        _response = self._raw_client.wallet_create(
            iso_currency_code=iso_currency_code, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def wallet_get(
        self,
        *,
        wallet_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WalletGetResponse:
        """
        Fetch an e-wallet. The response includes the current balance.

        Parameters
        ----------
        wallet_id : str
            The ID of the e-wallet

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WalletGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.wallet_get(
            wallet_id="wallet_id",
        )
        """
        _response = self._raw_client.wallet_get(
            wallet_id=wallet_id, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def wallet_list(
        self,
        *,
        client_id: typing.Optional[ApiClientId] = OMIT,
        count: typing.Optional[int] = OMIT,
        cursor: typing.Optional[str] = OMIT,
        iso_currency_code: typing.Optional[WalletIsoCurrencyCode] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WalletListResponse:
        """
        This endpoint lists all e-wallets in descending order of creation.

        Parameters
        ----------
        client_id : typing.Optional[ApiClientId]

        count : typing.Optional[int]
            The number of e-wallets to fetch

        cursor : typing.Optional[str]
            A base64 value representing the latest e-wallet that has already been requested. Set this to `next_cursor` received from the previous `/wallet/list` request. If provided, the response will only contain e-wallets created before that e-wallet. If omitted, the response will contain e-wallets starting from the most recent, and in descending order.

        iso_currency_code : typing.Optional[WalletIsoCurrencyCode]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WalletListResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.wallet_list()
        """
        _response = self._raw_client.wallet_list(
            client_id=client_id,
            count=count,
            cursor=cursor,
            iso_currency_code=iso_currency_code,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def wallet_transaction_execute(
        self,
        *,
        amount: WalletTransactionAmount,
        counterparty: WalletTransactionCounterparty,
        idempotency_key: WalletTransactionIdempotencyKey,
        reference: str,
        wallet_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WalletTransactionExecuteResponse:
        """
        Execute a transaction using the specified e-wallet.
        Specify the e-wallet to debit from, the counterparty to credit to, the idempotency key to prevent duplicate transactions, the amount and reference for the transaction.
        Transactions will settle in seconds to several days, depending on the underlying payment rail.

        Parameters
        ----------
        amount : WalletTransactionAmount

        counterparty : WalletTransactionCounterparty

        idempotency_key : WalletTransactionIdempotencyKey

        reference : str
            A reference for the transaction. This must be an alphanumeric string with 6 to 18 characters and must not contain any special characters or spaces.
            Ensure that the `reference` field is unique for each transaction.

        wallet_id : str
            The ID of the e-wallet to debit from

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WalletTransactionExecuteResponse
            OK

        Examples
        --------
        from fern import (
            FernApi,
            WalletTransactionAmount,
            WalletTransactionCounterparty,
            WalletTransactionCounterpartyNumbers,
        )

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.wallet_transaction_execute(
            amount=WalletTransactionAmount(
                iso_currency_code="GBP",
                value=1.1,
            ),
            counterparty=WalletTransactionCounterparty(
                name="name",
                numbers=WalletTransactionCounterpartyNumbers(),
            ),
            idempotency_key="idempotency_key",
            reference="reference",
            wallet_id="wallet_id",
        )
        """
        _response = self._raw_client.wallet_transaction_execute(
            amount=amount,
            counterparty=counterparty,
            idempotency_key=idempotency_key,
            reference=reference,
            wallet_id=wallet_id,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def wallet_transaction_get(
        self,
        *,
        transaction_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WalletTransactionGetResponse:
        """
        Fetch a specific e-wallet transaction

        Parameters
        ----------
        transaction_id : str
            The ID of the transaction to fetch

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WalletTransactionGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.wallet_transaction_get(
            transaction_id="transaction_id",
        )
        """
        _response = self._raw_client.wallet_transaction_get(
            transaction_id=transaction_id, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    def wallet_transaction_list(
        self,
        *,
        wallet_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        count: typing.Optional[int] = OMIT,
        cursor: typing.Optional[str] = OMIT,
        options: typing.Optional[WalletTransactionListRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WalletTransactionListResponse:
        """
        This endpoint lists the latest transactions of the specified e-wallet. Transactions are returned in descending order by the `created_at` time.

        Parameters
        ----------
        wallet_id : str
            The ID of the e-wallet to fetch transactions from

        client_id : typing.Optional[ApiClientId]

        count : typing.Optional[int]
            The number of transactions to fetch

        cursor : typing.Optional[str]
            A base64 value representing the latest transaction that has already been requested. Set this to `next_cursor` received from the previous `/wallet/transaction/list` request. If provided, the response will only contain transactions created before that transaction. If omitted, the response will contain transactions starting from the most recent, and in descending order by the `created_at` time.

        options : typing.Optional[WalletTransactionListRequestOptions]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WalletTransactionListResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.wallet_transaction_list(
            wallet_id="wallet_id",
        )
        """
        _response = self._raw_client.wallet_transaction_list(
            wallet_id=wallet_id,
            client_id=client_id,
            count=count,
            cursor=cursor,
            options=options,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def watchlist_screening_entity_create(
        self,
        *,
        search_terms: EntityWatchlistSearchTerms,
        client_id: typing.Optional[ApiClientId] = OMIT,
        client_user_id: typing.Optional[ClientUserId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WatchlistScreeningEntityCreateResponse:
        """
        Create a new entity watchlist screening to check your customer against watchlists defined in the associated entity watchlist program. If your associated program has ongoing screening enabled, this is the profile information that will be used to monitor your customer over time.

        Parameters
        ----------
        search_terms : EntityWatchlistSearchTerms

        client_id : typing.Optional[ApiClientId]

        client_user_id : typing.Optional[ClientUserId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WatchlistScreeningEntityCreateResponse
            OK

        Examples
        --------
        from fern import EntityWatchlistSearchTerms, FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.watchlist_screening_entity_create(
            search_terms=EntityWatchlistSearchTerms(
                entity_watchlist_program_id="entprg_2eRPsDnL66rZ7H",
                legal_name="Al-Qaida",
            ),
        )
        """
        _response = self._raw_client.watchlist_screening_entity_create(
            search_terms=search_terms,
            client_id=client_id,
            client_user_id=client_user_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def watchlist_screening_entity_get(
        self,
        *,
        entity_watchlist_screening_id: EntityWatchlistScreeningId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WatchlistScreeningEntityGetResponse:
        """
        Retrieve an entity watchlist screening.

        Parameters
        ----------
        entity_watchlist_screening_id : EntityWatchlistScreeningId

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WatchlistScreeningEntityGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.watchlist_screening_entity_get(
            entity_watchlist_screening_id="entscr_52xR9LKo77r1Np",
        )
        """
        _response = self._raw_client.watchlist_screening_entity_get(
            entity_watchlist_screening_id=entity_watchlist_screening_id,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def watchlist_screening_entity_history_list(
        self,
        *,
        entity_watchlist_screening_id: EntityWatchlistScreeningId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        cursor: typing.Optional[Cursor] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WatchlistScreeningEntityHistoryListResponse:
        """
        List all changes to the entity watchlist screening in reverse-chronological order. If the watchlist screening has not been edited, no history will be returned.

        Parameters
        ----------
        entity_watchlist_screening_id : EntityWatchlistScreeningId

        client_id : typing.Optional[ApiClientId]

        cursor : typing.Optional[Cursor]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WatchlistScreeningEntityHistoryListResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.watchlist_screening_entity_history_list(
            entity_watchlist_screening_id="entscr_52xR9LKo77r1Np",
        )
        """
        _response = self._raw_client.watchlist_screening_entity_history_list(
            entity_watchlist_screening_id=entity_watchlist_screening_id,
            client_id=client_id,
            cursor=cursor,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def watchlist_screening_entity_hit_list(
        self,
        *,
        entity_watchlist_screening_id: EntityWatchlistScreeningId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        cursor: typing.Optional[Cursor] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WatchlistScreeningEntityHitListResponse:
        """
        List all hits for the entity watchlist screening.

        Parameters
        ----------
        entity_watchlist_screening_id : EntityWatchlistScreeningId

        client_id : typing.Optional[ApiClientId]

        cursor : typing.Optional[Cursor]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WatchlistScreeningEntityHitListResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.watchlist_screening_entity_hit_list(
            entity_watchlist_screening_id="entscr_52xR9LKo77r1Np",
        )
        """
        _response = self._raw_client.watchlist_screening_entity_hit_list(
            entity_watchlist_screening_id=entity_watchlist_screening_id,
            client_id=client_id,
            cursor=cursor,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def watchlist_screening_entity_list(
        self,
        *,
        entity_watchlist_program_id: EntityWatchlistProgramId,
        assignee: typing.Optional[DashboardUserId] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        client_user_id: typing.Optional[ClientUserId] = OMIT,
        cursor: typing.Optional[Cursor] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        status: typing.Optional[WatchlistScreeningStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WatchlistScreeningEntityListResponse:
        """
        List all entity screenings.

        Parameters
        ----------
        entity_watchlist_program_id : EntityWatchlistProgramId

        assignee : typing.Optional[DashboardUserId]

        client_id : typing.Optional[ApiClientId]

        client_user_id : typing.Optional[ClientUserId]

        cursor : typing.Optional[Cursor]

        secret : typing.Optional[ApiSecret]

        status : typing.Optional[WatchlistScreeningStatus]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WatchlistScreeningEntityListResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.watchlist_screening_entity_list(
            entity_watchlist_program_id="entprg_2eRPsDnL66rZ7H",
        )
        """
        _response = self._raw_client.watchlist_screening_entity_list(
            entity_watchlist_program_id=entity_watchlist_program_id,
            assignee=assignee,
            client_id=client_id,
            client_user_id=client_user_id,
            cursor=cursor,
            secret=secret,
            status=status,
            request_options=request_options,
        )
        return _response.data

    def watchlist_screening_entity_program_get(
        self,
        *,
        entity_watchlist_program_id: EntityWatchlistProgramId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WatchlistScreeningEntityProgramGetResponse:
        """
        Get an entity watchlist screening program

        Parameters
        ----------
        entity_watchlist_program_id : EntityWatchlistProgramId

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WatchlistScreeningEntityProgramGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.watchlist_screening_entity_program_get(
            entity_watchlist_program_id="entprg_2eRPsDnL66rZ7H",
        )
        """
        _response = self._raw_client.watchlist_screening_entity_program_get(
            entity_watchlist_program_id=entity_watchlist_program_id,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def watchlist_screening_entity_program_list(
        self,
        *,
        client_id: typing.Optional[ApiClientId] = OMIT,
        cursor: typing.Optional[Cursor] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WatchlistScreeningEntityProgramListResponse:
        """
        List all entity watchlist screening programs

        Parameters
        ----------
        client_id : typing.Optional[ApiClientId]

        cursor : typing.Optional[Cursor]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WatchlistScreeningEntityProgramListResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.watchlist_screening_entity_program_list()
        """
        _response = self._raw_client.watchlist_screening_entity_program_list(
            client_id=client_id, cursor=cursor, secret=secret, request_options=request_options
        )
        return _response.data

    def watchlist_screening_entity_review_create(
        self,
        *,
        confirmed_hits: typing.Sequence[EntityWatchlistScreeningHitId],
        dismissed_hits: typing.Sequence[EntityWatchlistScreeningHitId],
        entity_watchlist_screening_id: EntityWatchlistScreeningId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        comment: typing.Optional[ReviewComment] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WatchlistScreeningEntityReviewCreateResponse:
        """
        Create a review for an entity watchlist screening. Reviews are compliance reports created by users in your organization regarding the relevance of potential hits found by Plaid.

        Parameters
        ----------
        confirmed_hits : typing.Sequence[EntityWatchlistScreeningHitId]
            Hits to mark as a true positive after thorough manual review. These hits will never recur or be updated once dismissed. In most cases, confirmed hits indicate that the customer should be rejected.

        dismissed_hits : typing.Sequence[EntityWatchlistScreeningHitId]
            Hits to mark as a false positive after thorough manual review. These hits will never recur or be updated once dismissed.

        entity_watchlist_screening_id : EntityWatchlistScreeningId

        client_id : typing.Optional[ApiClientId]

        comment : typing.Optional[ReviewComment]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WatchlistScreeningEntityReviewCreateResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.watchlist_screening_entity_review_create(
            confirmed_hits=["enthit_52xR9LKo77r1Np"],
            dismissed_hits=["enthit_52xR9LKo77r1Np"],
            entity_watchlist_screening_id="entscr_52xR9LKo77r1Np",
        )
        """
        _response = self._raw_client.watchlist_screening_entity_review_create(
            confirmed_hits=confirmed_hits,
            dismissed_hits=dismissed_hits,
            entity_watchlist_screening_id=entity_watchlist_screening_id,
            client_id=client_id,
            comment=comment,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def watchlist_screening_entity_review_list(
        self,
        *,
        entity_watchlist_screening_id: EntityWatchlistScreeningId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        cursor: typing.Optional[Cursor] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WatchlistScreeningEntityReviewListResponse:
        """
        List all reviews for a particular entity watchlist screening. Reviews are compliance reports created by users in your organization regarding the relevance of potential hits found by Plaid.

        Parameters
        ----------
        entity_watchlist_screening_id : EntityWatchlistScreeningId

        client_id : typing.Optional[ApiClientId]

        cursor : typing.Optional[Cursor]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WatchlistScreeningEntityReviewListResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.watchlist_screening_entity_review_list(
            entity_watchlist_screening_id="entscr_52xR9LKo77r1Np",
        )
        """
        _response = self._raw_client.watchlist_screening_entity_review_list(
            entity_watchlist_screening_id=entity_watchlist_screening_id,
            client_id=client_id,
            cursor=cursor,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def watchlist_screening_entity_update(
        self,
        *,
        entity_watchlist_screening_id: EntityWatchlistScreeningId,
        assignee: typing.Optional[DashboardUserId] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        client_user_id: typing.Optional[ClientUserId] = OMIT,
        reset_fields: typing.Optional[WatchlistScreeningEntityUpdateRequestResettableFieldList] = OMIT,
        search_terms: typing.Optional[UpdateEntityScreeningRequestSearchTerms] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        status: typing.Optional[WatchlistScreeningStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WatchlistScreeningEntityUpdateResponse:
        """
        Update an entity watchlist screening.

        Parameters
        ----------
        entity_watchlist_screening_id : EntityWatchlistScreeningId

        assignee : typing.Optional[DashboardUserId]

        client_id : typing.Optional[ApiClientId]

        client_user_id : typing.Optional[ClientUserId]

        reset_fields : typing.Optional[WatchlistScreeningEntityUpdateRequestResettableFieldList]

        search_terms : typing.Optional[UpdateEntityScreeningRequestSearchTerms]

        secret : typing.Optional[ApiSecret]

        status : typing.Optional[WatchlistScreeningStatus]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WatchlistScreeningEntityUpdateResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.watchlist_screening_entity_update(
            entity_watchlist_screening_id="entscr_52xR9LKo77r1Np",
        )
        """
        _response = self._raw_client.watchlist_screening_entity_update(
            entity_watchlist_screening_id=entity_watchlist_screening_id,
            assignee=assignee,
            client_id=client_id,
            client_user_id=client_user_id,
            reset_fields=reset_fields,
            search_terms=search_terms,
            secret=secret,
            status=status,
            request_options=request_options,
        )
        return _response.data

    def watchlist_screening_individual_create(
        self,
        *,
        search_terms: WatchlistScreeningRequestSearchTerms,
        client_id: typing.Optional[ApiClientId] = OMIT,
        client_user_id: typing.Optional[ClientUserId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WatchlistScreeningIndividualCreateResponse:
        """
        Create a new Watchlist Screening to check your customer against watchlists defined in the associated Watchlist Program. If your associated program has ongoing screening enabled, this is the profile information that will be used to monitor your customer over time.

        Parameters
        ----------
        search_terms : WatchlistScreeningRequestSearchTerms

        client_id : typing.Optional[ApiClientId]

        client_user_id : typing.Optional[ClientUserId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WatchlistScreeningIndividualCreateResponse
            OK

        Examples
        --------
        from fern import FernApi, WatchlistScreeningRequestSearchTerms

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.watchlist_screening_individual_create(
            search_terms=WatchlistScreeningRequestSearchTerms(
                legal_name="Aleksey Potemkin",
                watchlist_program_id="prg_2eRPsDnL66rZ7H",
            ),
        )
        """
        _response = self._raw_client.watchlist_screening_individual_create(
            search_terms=search_terms,
            client_id=client_id,
            client_user_id=client_user_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def watchlist_screening_individual_get(
        self,
        *,
        watchlist_screening_id: WatchlistScreeningIndividualId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WatchlistScreeningIndividualGetResponse:
        """
        Retrieve a previously created individual watchlist screening

        Parameters
        ----------
        watchlist_screening_id : WatchlistScreeningIndividualId

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WatchlistScreeningIndividualGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.watchlist_screening_individual_get(
            watchlist_screening_id="scr_52xR9LKo77r1Np",
        )
        """
        _response = self._raw_client.watchlist_screening_individual_get(
            watchlist_screening_id=watchlist_screening_id,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def watchlist_screening_individual_history_list(
        self,
        *,
        watchlist_screening_id: WatchlistScreeningIndividualId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        cursor: typing.Optional[Cursor] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WatchlistScreeningIndividualHistoryListResponse:
        """
        List all changes to the individual watchlist screening in reverse-chronological order. If the watchlist screening has not been edited, no history will be returned.

        Parameters
        ----------
        watchlist_screening_id : WatchlistScreeningIndividualId

        client_id : typing.Optional[ApiClientId]

        cursor : typing.Optional[Cursor]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WatchlistScreeningIndividualHistoryListResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.watchlist_screening_individual_history_list(
            watchlist_screening_id="scr_52xR9LKo77r1Np",
        )
        """
        _response = self._raw_client.watchlist_screening_individual_history_list(
            watchlist_screening_id=watchlist_screening_id,
            client_id=client_id,
            cursor=cursor,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def watchlist_screening_individual_hit_list(
        self,
        *,
        watchlist_screening_id: WatchlistScreeningIndividualId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        cursor: typing.Optional[Cursor] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WatchlistScreeningIndividualHitListResponse:
        """
        List all hits found by Plaid for a particular individual watchlist screening.

        Parameters
        ----------
        watchlist_screening_id : WatchlistScreeningIndividualId

        client_id : typing.Optional[ApiClientId]

        cursor : typing.Optional[Cursor]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WatchlistScreeningIndividualHitListResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.watchlist_screening_individual_hit_list(
            watchlist_screening_id="scr_52xR9LKo77r1Np",
        )
        """
        _response = self._raw_client.watchlist_screening_individual_hit_list(
            watchlist_screening_id=watchlist_screening_id,
            client_id=client_id,
            cursor=cursor,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def watchlist_screening_individual_list(
        self,
        *,
        watchlist_program_id: WatchlistProgramId,
        assignee: typing.Optional[DashboardUserId] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        client_user_id: typing.Optional[ClientUserId] = OMIT,
        cursor: typing.Optional[Cursor] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        status: typing.Optional[WatchlistScreeningStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WatchlistScreeningIndividualListResponse:
        """
        List previously created watchlist screenings for individuals

        Parameters
        ----------
        watchlist_program_id : WatchlistProgramId

        assignee : typing.Optional[DashboardUserId]

        client_id : typing.Optional[ApiClientId]

        client_user_id : typing.Optional[ClientUserId]

        cursor : typing.Optional[Cursor]

        secret : typing.Optional[ApiSecret]

        status : typing.Optional[WatchlistScreeningStatus]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WatchlistScreeningIndividualListResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.watchlist_screening_individual_list(
            watchlist_program_id="prg_2eRPsDnL66rZ7H",
        )
        """
        _response = self._raw_client.watchlist_screening_individual_list(
            watchlist_program_id=watchlist_program_id,
            assignee=assignee,
            client_id=client_id,
            client_user_id=client_user_id,
            cursor=cursor,
            secret=secret,
            status=status,
            request_options=request_options,
        )
        return _response.data

    def watchlist_screening_individual_program_get(
        self,
        *,
        watchlist_program_id: WatchlistProgramId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WatchlistScreeningIndividualProgramGetResponse:
        """
        Get an individual watchlist screening program

        Parameters
        ----------
        watchlist_program_id : WatchlistProgramId

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WatchlistScreeningIndividualProgramGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.watchlist_screening_individual_program_get(
            watchlist_program_id="prg_2eRPsDnL66rZ7H",
        )
        """
        _response = self._raw_client.watchlist_screening_individual_program_get(
            watchlist_program_id=watchlist_program_id,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def watchlist_screening_individual_program_list(
        self,
        *,
        client_id: typing.Optional[ApiClientId] = OMIT,
        cursor: typing.Optional[Cursor] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WatchlistScreeningIndividualProgramListResponse:
        """
        List all individual watchlist screening programs

        Parameters
        ----------
        client_id : typing.Optional[ApiClientId]

        cursor : typing.Optional[Cursor]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WatchlistScreeningIndividualProgramListResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.watchlist_screening_individual_program_list()
        """
        _response = self._raw_client.watchlist_screening_individual_program_list(
            client_id=client_id, cursor=cursor, secret=secret, request_options=request_options
        )
        return _response.data

    def watchlist_screening_individual_review_create(
        self,
        *,
        confirmed_hits: typing.Sequence[WatchlistScreeningHitId],
        dismissed_hits: typing.Sequence[WatchlistScreeningHitId],
        watchlist_screening_id: WatchlistScreeningIndividualId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        comment: typing.Optional[ReviewComment] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WatchlistScreeningIndividualReviewCreateResponse:
        """
        Create a review for the individual watchlist screening. Reviews are compliance reports created by users in your organization regarding the relevance of potential hits found by Plaid.

        Parameters
        ----------
        confirmed_hits : typing.Sequence[WatchlistScreeningHitId]
            Hits to mark as a true positive after thorough manual review. These hits will never recur or be updated once dismissed. In most cases, confirmed hits indicate that the customer should be rejected.

        dismissed_hits : typing.Sequence[WatchlistScreeningHitId]
            Hits to mark as a false positive after thorough manual review. These hits will never recur or be updated once dismissed.

        watchlist_screening_id : WatchlistScreeningIndividualId

        client_id : typing.Optional[ApiClientId]

        comment : typing.Optional[ReviewComment]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WatchlistScreeningIndividualReviewCreateResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.watchlist_screening_individual_review_create(
            confirmed_hits=["scrhit_52xR9LKo77r1Np"],
            dismissed_hits=["scrhit_52xR9LKo77r1Np"],
            watchlist_screening_id="scr_52xR9LKo77r1Np",
        )
        """
        _response = self._raw_client.watchlist_screening_individual_review_create(
            confirmed_hits=confirmed_hits,
            dismissed_hits=dismissed_hits,
            watchlist_screening_id=watchlist_screening_id,
            client_id=client_id,
            comment=comment,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def watchlist_screening_individual_review_list(
        self,
        *,
        watchlist_screening_id: WatchlistScreeningIndividualId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        cursor: typing.Optional[Cursor] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WatchlistScreeningIndividualReviewListResponse:
        """
        List all reviews for the individual watchlist screening.

        Parameters
        ----------
        watchlist_screening_id : WatchlistScreeningIndividualId

        client_id : typing.Optional[ApiClientId]

        cursor : typing.Optional[Cursor]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WatchlistScreeningIndividualReviewListResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.watchlist_screening_individual_review_list(
            watchlist_screening_id="scr_52xR9LKo77r1Np",
        )
        """
        _response = self._raw_client.watchlist_screening_individual_review_list(
            watchlist_screening_id=watchlist_screening_id,
            client_id=client_id,
            cursor=cursor,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def watchlist_screening_individual_update(
        self,
        *,
        watchlist_screening_id: WatchlistScreeningIndividualId,
        assignee: typing.Optional[DashboardUserId] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        client_user_id: typing.Optional[ClientUserId] = OMIT,
        reset_fields: typing.Optional[WatchlistScreeningIndividualUpdateRequestResettableFieldList] = OMIT,
        search_terms: typing.Optional[UpdateIndividualScreeningRequestSearchTerms] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        status: typing.Optional[WatchlistScreeningStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WatchlistScreeningIndividualUpdateResponse:
        """
        Update a specific individual watchlist screening. This endpoint can be used to add additional customer information, correct outdated information, add a reference id, assign the individual to a reviewer, and update which program it is associated with. Please note that you may not update `search_terms` and `status` at the same time since editing `search_terms` may trigger an automatic `status` change.

        Parameters
        ----------
        watchlist_screening_id : WatchlistScreeningIndividualId

        assignee : typing.Optional[DashboardUserId]

        client_id : typing.Optional[ApiClientId]

        client_user_id : typing.Optional[ClientUserId]

        reset_fields : typing.Optional[WatchlistScreeningIndividualUpdateRequestResettableFieldList]

        search_terms : typing.Optional[UpdateIndividualScreeningRequestSearchTerms]

        secret : typing.Optional[ApiSecret]

        status : typing.Optional[WatchlistScreeningStatus]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WatchlistScreeningIndividualUpdateResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.watchlist_screening_individual_update(
            watchlist_screening_id="scr_52xR9LKo77r1Np",
        )
        """
        _response = self._raw_client.watchlist_screening_individual_update(
            watchlist_screening_id=watchlist_screening_id,
            assignee=assignee,
            client_id=client_id,
            client_user_id=client_user_id,
            reset_fields=reset_fields,
            search_terms=search_terms,
            secret=secret,
            status=status,
            request_options=request_options,
        )
        return _response.data

    def webhook_verification_key_get(
        self,
        *,
        key_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebhookVerificationKeyGetResponse:
        """
        Plaid signs all outgoing webhooks and provides JSON Web Tokens (JWTs) so that you can verify the authenticity of any incoming webhooks to your application. A message signature is included in the `Plaid-Verification` header.

        The `/webhook_verification_key/get` endpoint provides a JSON Web Key (JWK) that can be used to verify a JWT.

        Parameters
        ----------
        key_id : str
            The key ID ( `kid` ) from the JWT header.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookVerificationKeyGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.plaid.webhook_verification_key_get(
            key_id="key_id",
        )
        """
        _response = self._raw_client.webhook_verification_key_get(
            key_id=key_id, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data


class AsyncPlaidClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPlaidClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPlaidClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPlaidClient
        """
        return self._raw_client

    async def accounts_balance_get(
        self,
        *,
        access_token: AccessToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        options: typing.Optional[AccountsBalanceGetRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountsGetResponse:
        """
        The `/accounts/balance/get` endpoint returns the real-time balance for each of an Item's accounts. While other endpoints may return a balance object, only `/accounts/balance/get` forces the available and current balance fields to be refreshed rather than cached. This endpoint can be used for existing Items that were added via any of Plaid’s other products. This endpoint can be used as long as Link has been initialized with any other product, `balance` itself is not a product that can be used to initialize Link. As this endpoint triggers a synchronous request for fresh data, latency may be higher than for other Plaid endpoints; if you encounter errors, you may find it necessary to adjust your timeout period when making requests.

        Parameters
        ----------
        access_token : AccessToken

        client_id : typing.Optional[ApiClientId]

        options : typing.Optional[AccountsBalanceGetRequestOptions]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountsGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AccountsBalanceGetRequestOptions, AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.accounts_balance_get(
                access_token="string",
                client_id="string",
                options=AccountsBalanceGetRequestOptions(
                    account_ids=["string"],
                ),
                secret="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.accounts_balance_get(
            access_token=access_token,
            client_id=client_id,
            options=options,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def accounts_get(
        self,
        *,
        access_token: AccessToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        options: typing.Optional[AccountsGetRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountsGetResponse:
        """
        The `/accounts/get` endpoint can be used to retrieve a list of accounts associated with any linked Item. Plaid will only return active bank accounts — that is, accounts that are not closed and are capable of carrying a balance.
        For items that went through the updated account selection pane, this endpoint only returns accounts that were permissioned by the user when they initially created the Item. If a user creates a new account after the initial link, you can capture this event through the [`NEW_ACCOUNTS_AVAILABLE`](https://plaid.com/docs/api/items/#new_accounts_available) webhook and then use Link's [update mode](https://plaid.com/docs/link/update-mode/) to request that the user share this new account with you.

        This endpoint retrieves cached information, rather than extracting fresh information from the institution. As a result, balances returned may not be up-to-date; for realtime balance information, use `/accounts/balance/get` instead. Note that some information is nullable.

        Parameters
        ----------
        access_token : AccessToken

        client_id : typing.Optional[ApiClientId]

        options : typing.Optional[AccountsGetRequestOptions]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountsGetResponse
            success

        Examples
        --------
        import asyncio

        from fern import AccountsGetRequestOptions, AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.accounts_get(
                access_token="string",
                client_id="string",
                options=AccountsGetRequestOptions(
                    account_ids=["string"],
                ),
                secret="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.accounts_get(
            access_token=access_token,
            client_id=client_id,
            options=options,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def application_get(
        self,
        *,
        application_id: ApplicationId,
        client_id: ApiClientId,
        secret: ApiSecret,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApplicationGetResponse:
        """
        Allows financial institutions to retrieve information about Plaid clients for the purpose of building control-tower experiences

        Parameters
        ----------
        application_id : ApplicationId

        client_id : ApiClientId

        secret : ApiSecret

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationGetResponse
            success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.application_get(
                application_id="application_id",
                client_id="client_id",
                secret="secret",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.application_get(
            application_id=application_id, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def asset_report_audit_copy_create(
        self,
        *,
        asset_report_token: AssetReportToken,
        auditor_id: typing.Optional[str] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AssetReportAuditCopyCreateResponse:
        """
        Plaid can provide an Audit Copy of any Asset Report directly to a participating third party on your behalf. For example, Plaid can supply an Audit Copy directly to Fannie Mae on your behalf if you participate in the Day 1 Certainty™ program. An Audit Copy contains the same underlying data as the Asset Report.

        To grant access to an Audit Copy, use the `/asset_report/audit_copy/create` endpoint to create an `audit_copy_token` and then pass that token to the third party who needs access. Each third party has its own `auditor_id`, for example `fannie_mae`. You’ll need to create a separate Audit Copy for each third party to whom you want to grant access to the Report.

        Parameters
        ----------
        asset_report_token : AssetReportToken

        auditor_id : typing.Optional[str]
            The `auditor_id` of the third party with whom you would like to share the Asset Report.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AssetReportAuditCopyCreateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.asset_report_audit_copy_create(
                asset_report_token="asset_report_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.asset_report_audit_copy_create(
            asset_report_token=asset_report_token,
            auditor_id=auditor_id,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def asset_report_audit_copy_get(
        self,
        *,
        audit_copy_token: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AssetReportGetResponse:
        """
        `/asset_report/audit_copy/get` allows auditors to get a copy of an Asset Report that was previously shared via the `/asset_report/audit_copy/create` endpoint.  The caller of `/asset_report/audit_copy/create` must provide the `audit_copy_token` to the auditor.  This token can then be used to call `/asset_report/audit_copy/create`.

        Parameters
        ----------
        audit_copy_token : str
            The `audit_copy_token` granting access to the Audit Copy you would like to get.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AssetReportGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.asset_report_audit_copy_get(
                audit_copy_token="audit_copy_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.asset_report_audit_copy_get(
            audit_copy_token=audit_copy_token, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def asset_report_audit_copy_remove(
        self,
        *,
        audit_copy_token: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AssetReportAuditCopyRemoveResponse:
        """
        The `/asset_report/audit_copy/remove` endpoint allows you to remove an Audit Copy. Removing an Audit Copy invalidates the `audit_copy_token` associated with it, meaning both you and any third parties holding the token will no longer be able to use it to access Report data. Items associated with the Asset Report, the Asset Report itself and other Audit Copies of it are not affected and will remain accessible after removing the given Audit Copy.

        Parameters
        ----------
        audit_copy_token : str
            The `audit_copy_token` granting access to the Audit Copy you would like to revoke.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AssetReportAuditCopyRemoveResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.asset_report_audit_copy_remove(
                audit_copy_token="audit_copy_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.asset_report_audit_copy_remove(
            audit_copy_token=audit_copy_token, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def asset_report_create(
        self,
        *,
        days_requested: int,
        access_tokens: typing.Optional[typing.Sequence[AccessToken]] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        options: typing.Optional[AssetReportCreateRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        user_token: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AssetReportCreateResponse:
        """
        The `/asset_report/create` endpoint initiates the process of creating an Asset Report, which can then be retrieved by passing the `asset_report_token` return value to the `/asset_report/get` or `/asset_report/pdf/get` endpoints.

        The Asset Report takes some time to be created and is not available immediately after calling `/asset_report/create`. When the Asset Report is ready to be retrieved using `/asset_report/get` or `/asset_report/pdf/get`, Plaid will fire a `PRODUCT_READY` webhook. For full details of the webhook schema, see [Asset Report webhooks](https://plaid.com/docs/api/products/assets/#webhooks).

        The `/asset_report/create` endpoint creates an Asset Report at a moment in time. Asset Reports are immutable. To get an updated Asset Report, use the `/asset_report/refresh` endpoint.

        Parameters
        ----------
        days_requested : int
            The maximum integer number of days of history to include in the Asset Report. If using Fannie Mae Day 1 Certainty, `days_requested` must be at least 61 for new originations or at least 31 for refinancings.

            An Asset Report requested with "Additional History" (that is, with more than 61 days of transaction history) will incur an Additional History fee.

        access_tokens : typing.Optional[typing.Sequence[AccessToken]]
            An array of access tokens corresponding to the Items that will be included in the report. The `assets` product must have been initialized for the Items during link; the Assets product cannot be added after initialization.

        client_id : typing.Optional[ApiClientId]

        options : typing.Optional[AssetReportCreateRequestOptions]

        secret : typing.Optional[ApiSecret]

        user_token : typing.Optional[str]
            The user token associated with the User for which to create an asset report for. All items associated with the User will be included in the report.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AssetReportCreateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.asset_report_create(
                days_requested=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.asset_report_create(
            days_requested=days_requested,
            access_tokens=access_tokens,
            client_id=client_id,
            options=options,
            secret=secret,
            user_token=user_token,
            request_options=request_options,
        )
        return _response.data

    async def asset_report_filter(
        self,
        *,
        account_ids_to_exclude: typing.Sequence[str],
        asset_report_token: AssetReportToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AssetReportFilterResponse:
        """
        By default, an Asset Report will contain all of the accounts on a given Item. In some cases, you may not want the Asset Report to contain all accounts. For example, you might have the end user choose which accounts are relevant in Link using the Account Select view, which you can enable in the dashboard. Or, you might always exclude certain account types or subtypes, which you can identify by using the `/accounts/get` endpoint. To narrow an Asset Report to only a subset of accounts, use the `/asset_report/filter` endpoint.

        To exclude certain Accounts from an Asset Report, first use the `/asset_report/create` endpoint to create the report, then send the `asset_report_token` along with a list of `account_ids` to exclude to the `/asset_report/filter` endpoint, to create a new Asset Report which contains only a subset of the original Asset Report's data.

        Because Asset Reports are immutable, calling `/asset_report/filter` does not alter the original Asset Report in any way; rather, `/asset_report/filter` creates a new Asset Report with a new token and id. Asset Reports created via `/asset_report/filter` do not contain new Asset data, and are not billed.

        Plaid will fire a [`PRODUCT_READY`](https://plaid.com/docs/api/products/assets/#product_ready) webhook once generation of the filtered Asset Report has completed.

        Parameters
        ----------
        account_ids_to_exclude : typing.Sequence[str]
            The accounts to exclude from the Asset Report, identified by `account_id`.

        asset_report_token : AssetReportToken

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AssetReportFilterResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.asset_report_filter(
                account_ids_to_exclude=["account_ids_to_exclude"],
                asset_report_token="asset_report_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.asset_report_filter(
            account_ids_to_exclude=account_ids_to_exclude,
            asset_report_token=asset_report_token,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def asset_report_get(
        self,
        *,
        asset_report_token: AssetReportToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        fast_report: typing.Optional[bool] = OMIT,
        include_insights: typing.Optional[bool] = OMIT,
        options: typing.Optional[AssetReportGetRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AssetReportGetResponse:
        """
        The `/asset_report/get` endpoint retrieves the Asset Report in JSON format. Before calling `/asset_report/get`, you must first create the Asset Report using `/asset_report/create` (or filter an Asset Report using `/asset_report/filter`) and then wait for the [`PRODUCT_READY`](https://plaid.com/docs/api/products/assets/#product_ready) webhook to fire, indicating that the Report is ready to be retrieved.

        By default, an Asset Report includes transaction descriptions as returned by the bank, as opposed to parsed and categorized by Plaid. You can also receive cleaned and categorized transactions, as well as additional insights like merchant name or location information. We call this an Asset Report with Insights. An Asset Report with Insights provides transaction category, location, and merchant information in addition to the transaction strings provided in a standard Asset Report.

        If report_type was set to `VERIFICATION_OF_EMPLOYMENT` when the Asset Report was created in asset_report/create, debit transactions and transaction amounts won’t be included in the report.

        To retrieve an Asset Report with Insights, call the `/asset_report/get` endpoint with `include_insights` set to `true`.

        Parameters
        ----------
        asset_report_token : AssetReportToken

        client_id : typing.Optional[ApiClientId]

        fast_report : typing.Optional[bool]
            `true` to fetch "fast" version of asset report. Defaults to false if omitted. Can only be used if `/asset_report/create` was called with `options.add_ons` set to `["fast_assets"]`.

        include_insights : typing.Optional[bool]
            `true` if you would like to retrieve the Asset Report with Insights, `false` otherwise. This field defaults to `false` if omitted.

        options : typing.Optional[AssetReportGetRequestOptions]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AssetReportGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.asset_report_get(
                asset_report_token="asset_report_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.asset_report_get(
            asset_report_token=asset_report_token,
            client_id=client_id,
            fast_report=fast_report,
            include_insights=include_insights,
            options=options,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def asset_report_pdf_get(
        self,
        *,
        asset_report_token: AssetReportToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        options: typing.Optional[AssetReportPdfGetRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        The `/asset_report/pdf/get` endpoint retrieves the Asset Report in PDF format. Before calling `/asset_report/pdf/get`, you must first create the Asset Report using `/asset_report/create` (or filter an Asset Report using `/asset_report/filter`) and then wait for the [`PRODUCT_READY`](https://plaid.com/docs/api/products/assets/#product_ready) webhook to fire, indicating that the Report is ready to be retrieved.

        The response to `/asset_report/pdf/get` is the PDF binary data. The `request_id`  is returned in the `Plaid-Request-ID` header.

        If report_type was set to `VERIFICATION_OF_EMPLOYMENT` when the Asset Report was created in asset_report/create, debit transactions and transaction amounts won’t be included in the report.

        [View a sample PDF Asset Report](https://plaid.com/documents/sample-asset-report.pdf).

        Parameters
        ----------
        asset_report_token : AssetReportToken

        client_id : typing.Optional[ApiClientId]

        options : typing.Optional[AssetReportPdfGetRequestOptions]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            A PDF of the Asset Report
        """
        async with self._raw_client.asset_report_pdf_get(
            asset_report_token=asset_report_token,
            client_id=client_id,
            options=options,
            secret=secret,
            request_options=request_options,
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def asset_report_refresh(
        self,
        *,
        asset_report_token: AssetReportRefreshAssetReportToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        days_requested: typing.Optional[int] = OMIT,
        options: typing.Optional[AssetReportRefreshRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AssetReportRefreshResponse:
        """
        An Asset Report is an immutable snapshot of a user's assets. In order to "refresh" an Asset Report you created previously, you can use the `/asset_report/refresh` endpoint to create a new Asset Report based on the old one, but with the most recent data available.

        The new Asset Report will contain the same Items as the original Report, as well as the same filters applied by any call to `/asset_report/filter`. By default, the new Asset Report will also use the same parameters you submitted with your original `/asset_report/create` request, but the original `days_requested` value and the values of any parameters in the `options` object can be overridden with new values. To change these arguments, simply supply new values for them in your request to `/asset_report/refresh`. Submit an empty string ("") for any previously-populated fields you would like set as empty.

        Parameters
        ----------
        asset_report_token : AssetReportRefreshAssetReportToken

        client_id : typing.Optional[ApiClientId]

        days_requested : typing.Optional[int]
            The maximum number of days of history to include in the Asset Report. Must be an integer. If not specified, the value from the original call to `/asset_report/create` will be used.

        options : typing.Optional[AssetReportRefreshRequestOptions]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AssetReportRefreshResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.asset_report_refresh(
                asset_report_token="asset_report_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.asset_report_refresh(
            asset_report_token=asset_report_token,
            client_id=client_id,
            days_requested=days_requested,
            options=options,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def asset_report_remove(
        self,
        *,
        asset_report_token: AssetReportToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AssetReportRemoveResponse:
        """
        The `/item/remove` endpoint allows you to invalidate an `access_token`, meaning you will not be able to create new Asset Reports with it. Removing an Item does not affect any Asset Reports or Audit Copies you have already created, which will remain accessible until you remove them specifically.

        The `/asset_report/remove` endpoint allows you to remove an Asset Report. Removing an Asset Report invalidates its `asset_report_token`, meaning you will no longer be able to use it to access Report data or create new Audit Copies. Removing an Asset Report does not affect the underlying Items, but does invalidate any `audit_copy_tokens` associated with the Asset Report.

        Parameters
        ----------
        asset_report_token : AssetReportToken

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AssetReportRemoveResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.asset_report_remove(
                asset_report_token="asset_report_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.asset_report_remove(
            asset_report_token=asset_report_token, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def auth_get(
        self,
        *,
        access_token: AccessToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        options: typing.Optional[AuthGetRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AuthGetResponse:
        """
        The `/auth/get` endpoint returns the bank account and bank identification numbers (such as routing numbers, for US accounts) associated with an Item's checking and savings accounts, along with high-level account data and balances when available.

        Note: This request may take some time to complete if `auth` was not specified as an initial product when creating the Item. This is because Plaid must communicate directly with the institution to retrieve the data.

        Versioning note: In API version 2017-03-08, the schema of the `numbers` object returned by this endpoint is substantially different. For details, see [Plaid API versioning](https://plaid.com/docs/api/versioning/#version-2018-05-22).

        Parameters
        ----------
        access_token : AccessToken

        client_id : typing.Optional[ApiClientId]

        options : typing.Optional[AuthGetRequestOptions]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthGetResponse
            success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.auth_get(
                access_token="access_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.auth_get(
            access_token=access_token,
            client_id=client_id,
            options=options,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def bank_transfer_balance_get(
        self,
        *,
        client_id: typing.Optional[ApiClientId] = OMIT,
        origination_account_id: typing.Optional[str] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BankTransferBalanceGetResponse:
        """
        Use the `/bank_transfer/balance/get` endpoint to see the available balance in your bank transfer account. Debit transfers increase this balance once their status is posted. Credit transfers decrease this balance when they are created.

        The transactable balance shows the amount in your account that you are able to use for transfers, and is essentially your available balance minus your minimum balance.

        Note that this endpoint can only be used with FBO accounts, when using Bank Transfers in the Full Service configuration. It cannot be used on your own account when using Bank Transfers in the BTS Platform configuration.

        Parameters
        ----------
        client_id : typing.Optional[ApiClientId]

        origination_account_id : typing.Optional[str]
            If multiple origination accounts are available, `origination_account_id` must be used to specify the account for which balance will be returned.

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BankTransferBalanceGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.bank_transfer_balance_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.bank_transfer_balance_get(
            client_id=client_id,
            origination_account_id=origination_account_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def bank_transfer_cancel(
        self,
        *,
        bank_transfer_id: BankTransferId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BankTransferCancelResponse:
        """
        Use the `/bank_transfer/cancel` endpoint to cancel a bank transfer.  A transfer is eligible for cancelation if the `cancellable` property returned by `/bank_transfer/get` is `true`.

        Parameters
        ----------
        bank_transfer_id : BankTransferId

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BankTransferCancelResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.bank_transfer_cancel(
                bank_transfer_id="bank_transfer_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.bank_transfer_cancel(
            bank_transfer_id=bank_transfer_id, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def bank_transfer_create(
        self,
        *,
        access_token: BankTransferAccessToken,
        account_id: str,
        amount: BankTransferAmount,
        description: str,
        idempotency_key: BankTransferIdempotencyKey,
        iso_currency_code: str,
        network: BankTransferNetwork,
        type: BankTransferType,
        user: BankTransferUser,
        ach_class: typing.Optional[AchClass] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        custom_tag: typing.Optional[str] = OMIT,
        metadata: typing.Optional[BankTransferMetadata] = OMIT,
        origination_account_id: typing.Optional[str] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BankTransferCreateResponse:
        """
        Use the `/bank_transfer/create` endpoint to initiate a new bank transfer.

        Parameters
        ----------
        access_token : BankTransferAccessToken

        account_id : str
            The Plaid `account_id` for the account that will be debited or credited.

        amount : BankTransferAmount

        description : str
            The transfer description. Maximum of 10 characters.

        idempotency_key : BankTransferIdempotencyKey

        iso_currency_code : str
            The currency of the transfer amount – should be set to "USD".

        network : BankTransferNetwork

        type : BankTransferType

        user : BankTransferUser

        ach_class : typing.Optional[AchClass]

        client_id : typing.Optional[ApiClientId]

        custom_tag : typing.Optional[str]
            An arbitrary string provided by the client for storage with the bank transfer. May be up to 100 characters.

        metadata : typing.Optional[BankTransferMetadata]

        origination_account_id : typing.Optional[str]
            Plaid’s unique identifier for the origination account for this transfer. If you have more than one origination account, this value must be specified. Otherwise, this field should be left blank.

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BankTransferCreateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, BankTransferUser

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.bank_transfer_create(
                access_token="access_token",
                account_id="account_id",
                amount="amount",
                description="description",
                idempotency_key="idempotency_key",
                iso_currency_code="iso_currency_code",
                network="ach",
                type="debit",
                user=BankTransferUser(
                    legal_name="legal_name",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.bank_transfer_create(
            access_token=access_token,
            account_id=account_id,
            amount=amount,
            description=description,
            idempotency_key=idempotency_key,
            iso_currency_code=iso_currency_code,
            network=network,
            type=type,
            user=user,
            ach_class=ach_class,
            client_id=client_id,
            custom_tag=custom_tag,
            metadata=metadata,
            origination_account_id=origination_account_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def bank_transfer_event_list(
        self,
        *,
        account_id: typing.Optional[str] = OMIT,
        bank_transfer_id: typing.Optional[str] = OMIT,
        bank_transfer_type: typing.Optional[BankTransferEventListBankTransferType] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        count: typing.Optional[int] = OMIT,
        direction: typing.Optional[BankTransferEventListDirection] = OMIT,
        end_date: typing.Optional[dt.datetime] = OMIT,
        event_types: typing.Optional[typing.Sequence[BankTransferEventType]] = OMIT,
        offset: typing.Optional[int] = OMIT,
        origination_account_id: typing.Optional[str] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        start_date: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BankTransferEventListResponse:
        """
        Use the `/bank_transfer/event/list` endpoint to get a list of Plaid-initiated ACH or bank transfer events based on specified filter criteria. When using Auth with micro-deposit verification enabled, this endpoint can be used to fetch status updates on ACH micro-deposits. For more details, see [micro-deposit events](https://plaid.com/docs/auth/coverage/microdeposit-events/).

        Parameters
        ----------
        account_id : typing.Optional[str]
            The account ID to get events for all transactions to/from an account.

        bank_transfer_id : typing.Optional[str]
            Plaid’s unique identifier for a bank transfer.

        bank_transfer_type : typing.Optional[BankTransferEventListBankTransferType]

        client_id : typing.Optional[ApiClientId]

        count : typing.Optional[int]
            The maximum number of bank transfer events to return. If the number of events matching the above parameters is greater than `count`, the most recent events will be returned.

        direction : typing.Optional[BankTransferEventListDirection]

        end_date : typing.Optional[dt.datetime]
            The end datetime of bank transfers to list. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`)

        event_types : typing.Optional[typing.Sequence[BankTransferEventType]]
            Filter events by event type.

        offset : typing.Optional[int]
            The offset into the list of bank transfer events. When `count`=25 and `offset`=0, the first 25 events will be returned. When `count`=25 and `offset`=25, the next 25 bank transfer events will be returned.

        origination_account_id : typing.Optional[str]
            The origination account ID to get events for transfers from a specific origination account.

        secret : typing.Optional[ApiSecret]

        start_date : typing.Optional[dt.datetime]
            The start datetime of bank transfers to list. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BankTransferEventListResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.bank_transfer_event_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.bank_transfer_event_list(
            account_id=account_id,
            bank_transfer_id=bank_transfer_id,
            bank_transfer_type=bank_transfer_type,
            client_id=client_id,
            count=count,
            direction=direction,
            end_date=end_date,
            event_types=event_types,
            offset=offset,
            origination_account_id=origination_account_id,
            secret=secret,
            start_date=start_date,
            request_options=request_options,
        )
        return _response.data

    async def bank_transfer_event_sync(
        self,
        *,
        after_id: int,
        client_id: typing.Optional[ApiClientId] = OMIT,
        count: typing.Optional[int] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BankTransferEventSyncResponse:
        """
        `/bank_transfer/event/sync` allows you to request up to the next 25 Plaid-initiated bank transfer events that happened after a specific `event_id`. When using Auth with micro-deposit verification enabled, this endpoint can be used to fetch status updates on ACH micro-deposits. For more details, see [micro-deposit events](https://www.plaid.com/docs/auth/coverage/microdeposit-events/).

        Parameters
        ----------
        after_id : int
            The latest (largest) `event_id` fetched via the sync endpoint, or 0 initially.

        client_id : typing.Optional[ApiClientId]

        count : typing.Optional[int]
            The maximum number of bank transfer events to return.

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BankTransferEventSyncResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.bank_transfer_event_sync(
                after_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.bank_transfer_event_sync(
            after_id=after_id, client_id=client_id, count=count, secret=secret, request_options=request_options
        )
        return _response.data

    async def bank_transfer_get(
        self,
        *,
        bank_transfer_id: BankTransferId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BankTransferGetResponse:
        """
        The `/bank_transfer/get` fetches information about the bank transfer corresponding to the given `bank_transfer_id`.

        Parameters
        ----------
        bank_transfer_id : BankTransferId

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BankTransferGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.bank_transfer_get(
                bank_transfer_id="bank_transfer_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.bank_transfer_get(
            bank_transfer_id=bank_transfer_id, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def bank_transfer_list(
        self,
        *,
        client_id: typing.Optional[ApiClientId] = OMIT,
        count: typing.Optional[int] = OMIT,
        direction: typing.Optional[BankTransferDirection] = OMIT,
        end_date: typing.Optional[dt.datetime] = OMIT,
        offset: typing.Optional[int] = OMIT,
        origination_account_id: typing.Optional[str] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        start_date: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BankTransferListResponse:
        """
        Use the `/bank_transfer/list` endpoint to see a list of all your bank transfers and their statuses. Results are paginated; use the `count` and `offset` query parameters to retrieve the desired bank transfers.

        Parameters
        ----------
        client_id : typing.Optional[ApiClientId]

        count : typing.Optional[int]
            The maximum number of bank transfers to return.

        direction : typing.Optional[BankTransferDirection]

        end_date : typing.Optional[dt.datetime]
            The end datetime of bank transfers to list. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`)

        offset : typing.Optional[int]
            The number of bank transfers to skip before returning results.

        origination_account_id : typing.Optional[str]
            Filter bank transfers to only those originated through the specified origination account.

        secret : typing.Optional[ApiSecret]

        start_date : typing.Optional[dt.datetime]
            The start datetime of bank transfers to list. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BankTransferListResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.bank_transfer_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.bank_transfer_list(
            client_id=client_id,
            count=count,
            direction=direction,
            end_date=end_date,
            offset=offset,
            origination_account_id=origination_account_id,
            secret=secret,
            start_date=start_date,
            request_options=request_options,
        )
        return _response.data

    async def bank_transfer_migrate_account(
        self,
        *,
        account_number: str,
        account_type: str,
        routing_number: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        wire_routing_number: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BankTransferMigrateAccountResponse:
        """
        As an alternative to adding Items via Link, you can also use the `/bank_transfer/migrate_account` endpoint to migrate known account and routing numbers to Plaid Items.  Note that Items created in this way are not compatible with endpoints for other products, such as `/accounts/balance/get`, and can only be used with Bank Transfer endpoints.  If you require access to other endpoints, create the Item through Link instead.  Access to `/bank_transfer/migrate_account` is not enabled by default; to obtain access, contact your Plaid Account Manager.

        Parameters
        ----------
        account_number : str
            The user's account number.

        account_type : str
            The type of the bank account (`checking` or `savings`).

        routing_number : str
            The user's routing number.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        wire_routing_number : typing.Optional[str]
            The user's wire transfer routing number. This is the ABA number; for some institutions, this may differ from the ACH number used in `routing_number`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BankTransferMigrateAccountResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.bank_transfer_migrate_account(
                account_number="account_number",
                account_type="account_type",
                routing_number="routing_number",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.bank_transfer_migrate_account(
            account_number=account_number,
            account_type=account_type,
            routing_number=routing_number,
            client_id=client_id,
            secret=secret,
            wire_routing_number=wire_routing_number,
            request_options=request_options,
        )
        return _response.data

    async def bank_transfer_sweep_get(
        self,
        *,
        sweep_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BankTransferSweepGetResponse:
        """
        The `/bank_transfer/sweep/get` endpoint fetches information about the sweep corresponding to the given `sweep_id`.

        Parameters
        ----------
        sweep_id : str
            Identifier of the sweep.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BankTransferSweepGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.bank_transfer_sweep_get(
                sweep_id="sweep_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.bank_transfer_sweep_get(
            sweep_id=sweep_id, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def bank_transfer_sweep_list(
        self,
        *,
        client_id: typing.Optional[ApiClientId] = OMIT,
        count: typing.Optional[int] = OMIT,
        end_time: typing.Optional[dt.datetime] = OMIT,
        origination_account_id: typing.Optional[str] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        start_time: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BankTransferSweepListResponse:
        """
        The `/bank_transfer/sweep/list` endpoint fetches information about the sweeps matching the given filters.

        Parameters
        ----------
        client_id : typing.Optional[ApiClientId]

        count : typing.Optional[int]
            The maximum number of sweeps to return.

        end_time : typing.Optional[dt.datetime]
            The end datetime of sweeps to return (RFC 3339 format).

        origination_account_id : typing.Optional[str]
            If multiple origination accounts are available, `origination_account_id` must be used to specify the account that the sweeps belong to.

        secret : typing.Optional[ApiSecret]

        start_time : typing.Optional[dt.datetime]
            The start datetime of sweeps to return (RFC 3339 format).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BankTransferSweepListResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.bank_transfer_sweep_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.bank_transfer_sweep_list(
            client_id=client_id,
            count=count,
            end_time=end_time,
            origination_account_id=origination_account_id,
            secret=secret,
            start_time=start_time,
            request_options=request_options,
        )
        return _response.data

    async def credit_bank_employment_get(
        self,
        *,
        user_token: UserToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreditBankEmploymentGetResponse:
        """
        `/credit/bank_employment/get` returns the employment report(s) derived from bank transaction data for a specified user.

        Parameters
        ----------
        user_token : UserToken

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreditBankEmploymentGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.credit_bank_employment_get(
                user_token="user_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.credit_bank_employment_get(
            user_token=user_token, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def transactions_rules_create(
        self,
        *,
        access_token: AccessToken,
        personal_finance_category: str,
        rule_details: TransactionsRuleDetails,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransactionsRulesCreateResponse:
        """
        The `/transactions/rules/v1/create` endpoint creates transaction categorization rules.

        Rules will be applied on the Item's transactions returned in `/transactions/get` response.

        The product is currently in beta. To request access, contact transactions-feedback@plaid.com.

        Parameters
        ----------
        access_token : AccessToken

        personal_finance_category : str
            Personal finance detailed category.

            See the [`taxonomy csv file`](https://plaid.com/documents/transactions-personal-finance-category-taxonomy.csv) for a full list of personal finance categories.

        rule_details : TransactionsRuleDetails

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransactionsRulesCreateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, TransactionsRuleDetails

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.transactions_rules_create(
                access_token="access-sandbox-71e02f71-0960-4a27-abd2-5631e04f2175",
                client_id="7f57eb3d2a9j6480121fx361",
                personal_finance_category="FOOD_AND_DRINK_FAST_FOOD",
                rule_details=TransactionsRuleDetails(
                    field="NAME",
                    query="Burger Shack",
                    type="SUBSTRING_MATCH",
                ),
                secret="79g03eoofwl8240v776r2h667442119",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.transactions_rules_create(
            access_token=access_token,
            personal_finance_category=personal_finance_category,
            rule_details=rule_details,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def transactions_rules_list(
        self,
        *,
        access_token: AccessToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransactionsRulesListResponse:
        """
        The `/transactions/rules/v1/list` returns a list of transaction rules created for the Item associated with the access token.

        Parameters
        ----------
        access_token : AccessToken

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransactionsRulesListResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.transactions_rules_list(
                access_token="access-sandbox-71e02f71-0960-4a27-abd2-5631e04f2175",
                client_id="7f57eb3d2a9j6480121fx361",
                secret="79g03eoofwl8240v776r2h667442119",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.transactions_rules_list(
            access_token=access_token, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def transactions_rules_remove(
        self,
        *,
        access_token: AccessToken,
        rule_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransactionsRulesRemoveResponse:
        """
        The `/transactions/rules/v1/remove` endpoint is used to remove a transaction rule.

        Parameters
        ----------
        access_token : AccessToken

        rule_id : str
            A rule's unique identifier

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransactionsRulesRemoveResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.transactions_rules_remove(
                access_token="access-sandbox-71e02f71-0960-4a27-abd2-5631e04f2175",
                client_id="7f57eb3d2a9j6480121fx361",
                rule_id="eVBnVMp7zdTJLkRNr33Rs6zr7KNJqBF",
                secret="79g03eoofwl8240v776r2h667442119",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.transactions_rules_remove(
            access_token=access_token,
            rule_id=rule_id,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def transactions_enhance(
        self,
        *,
        account_type: str,
        transactions: typing.Sequence[ClientProvidedRawTransaction],
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransactionsEnhanceGetResponse:
        """
        The `/beta/transactions/v1/enhance` endpoint enriches raw transaction data provided directly by clients.

        The product is currently in beta.

        Parameters
        ----------
        account_type : str
            The type of account for the requested transactions (`depository` or `credit`).

        transactions : typing.Sequence[ClientProvidedRawTransaction]
            An array of raw transactions to be enhanced.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransactionsEnhanceGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ClientProvidedRawTransaction

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.transactions_enhance(
                account_type="account_type",
                transactions=[
                    ClientProvidedRawTransaction(
                        amount=1.1,
                        description="description",
                        id="id",
                        iso_currency_code="iso_currency_code",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.transactions_enhance(
            account_type=account_type,
            transactions=transactions,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def categories_get(
        self, *, request: CategoriesGetRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> CategoriesGetResponse:
        """
        Send a request to the `/categories/get` endpoint to get detailed information on categories returned by Plaid. This endpoint does not require authentication.

        Parameters
        ----------
        request : CategoriesGetRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CategoriesGetResponse
            success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.categories_get(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.categories_get(request=request, request_options=request_options)
        return _response.data

    async def credit_asset_report_freddie_mac_get(
        self,
        *,
        audit_copy_token: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AssetReportFreddieGetResponse:
        """
        The `credit/asset_report/freddie_mac/get` endpoint retrieves the Asset Report in Freddie Mac's JSON format.

        Parameters
        ----------
        audit_copy_token : str
            A token that can be shared with a third party auditor to allow them to obtain access to the Asset Report. This token should be stored securely.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AssetReportFreddieGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.credit_asset_report_freddie_mac_get(
                audit_copy_token="audit_copy_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.credit_asset_report_freddie_mac_get(
            audit_copy_token=audit_copy_token, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def credit_audit_copy_token_create(
        self,
        *,
        report_tokens: typing.Sequence[str],
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreditAuditCopyTokenCreateResponse:
        """
        Plaid can create an Audit Copy token of an Asset Report and/or Income Report to share with participating Government Sponsored Entity (GSE). If you participate in the Day 1 Certainty™ program, Plaid can supply an Audit Copy token directly to Fannie Mae on your behalf. An Audit Copy token contains the same underlying data as the Asset Report and/or Income Report (result of /credit/payroll_income/get).

        Use the `/credit/audit_copy_token/create` endpoint to create an `audit_copy_token` and then pass that token to the GSE who needs access.

        Parameters
        ----------
        report_tokens : typing.Sequence[str]
            List of report tokens; can include at most one VOA/standard Asset Report tokens and one VOE Asset Report Token.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreditAuditCopyTokenCreateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.credit_audit_copy_token_create(
                report_tokens=["report_tokens"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.credit_audit_copy_token_create(
            report_tokens=report_tokens, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def credit_report_audit_copy_remove(
        self,
        *,
        audit_copy_token: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreditAuditCopyTokenRemoveResponse:
        """
        The `/credit/audit_copy_token/remove` endpoint allows you to remove an Audit Copy. Removing an Audit Copy invalidates the `audit_copy_token` associated with it, meaning both you and any third parties holding the token will no longer be able to use it to access Report data. Items associated with the Report data and other Audit Copies of it are not affected and will remain accessible after removing the given Audit Copy.

        Parameters
        ----------
        audit_copy_token : str
            The `audit_copy_token` granting access to the Audit Copy you would like to revoke.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreditAuditCopyTokenRemoveResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.credit_report_audit_copy_remove(
                audit_copy_token="audit_copy_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.credit_report_audit_copy_remove(
            audit_copy_token=audit_copy_token, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def credit_audit_copy_token_update(
        self,
        *,
        audit_copy_token: str,
        report_tokens: typing.Sequence[AssetReportToken],
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreditAuditCopyTokenUpdateResponse:
        """
        The `/credit/audit_copy_token/update` endpoint updates an existing  Audit Copy Token by adding the report tokens in the `report_tokens` field to the `audit_copy_token`. If the Audit Copy Token already contains a report of a certain type, it will be replaced with the token provided in the `report_tokens` field.

        Parameters
        ----------
        audit_copy_token : str
            The `audit_copy_token` you would like to update.

        report_tokens : typing.Sequence[AssetReportToken]
            Array of tokens which the specified Audit Copy Token will be updated with. The types of token supported are asset report token and employment report token. There can be at most 1 of each token type in the array.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreditAuditCopyTokenUpdateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.credit_audit_copy_token_update(
                audit_copy_token="audit_copy_token",
                report_tokens=["report_tokens"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.credit_audit_copy_token_update(
            audit_copy_token=audit_copy_token,
            report_tokens=report_tokens,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def credit_bank_income_get(
        self,
        *,
        client_id: typing.Optional[ApiClientId] = OMIT,
        options: typing.Optional[CreditBankIncomeGetRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        user_token: typing.Optional[UserToken] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreditBankIncomeGetResponse:
        """
        `/credit/bank_income/get` returns the bank income report(s) for a specified user.

        Parameters
        ----------
        client_id : typing.Optional[ApiClientId]

        options : typing.Optional[CreditBankIncomeGetRequestOptions]

        secret : typing.Optional[ApiSecret]

        user_token : typing.Optional[UserToken]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreditBankIncomeGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.credit_bank_income_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.credit_bank_income_get(
            client_id=client_id, options=options, secret=secret, user_token=user_token, request_options=request_options
        )
        return _response.data

    async def credit_bank_income_pdf_get(
        self,
        *,
        user_token: UserToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        `/credit/bank_income/pdf/get` returns the most recent bank income report for a specified user in PDF format.

        Parameters
        ----------
        user_token : UserToken

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            A PDF of the Bank Income Report
        """
        async with self._raw_client.credit_bank_income_pdf_get(
            user_token=user_token, client_id=client_id, secret=secret, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def credit_bank_income_refresh(
        self,
        *,
        user_token: UserToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        options: typing.Optional[CreditBankIncomeRefreshRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreditBankIncomeRefreshResponse:
        """
        `/credit/bank_income/refresh` refreshes the bank income report data for a specific user.

        Parameters
        ----------
        user_token : UserToken

        client_id : typing.Optional[ApiClientId]

        options : typing.Optional[CreditBankIncomeRefreshRequestOptions]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreditBankIncomeRefreshResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.credit_bank_income_refresh(
                user_token="user_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.credit_bank_income_refresh(
            user_token=user_token, client_id=client_id, options=options, secret=secret, request_options=request_options
        )
        return _response.data

    async def credit_employment_get(
        self,
        *,
        user_token: UserToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreditEmploymentGetResponse:
        """
        `/credit/employment/get` returns a list of items with employment information from a user's payroll provider that was verified by an end user.

        Parameters
        ----------
        user_token : UserToken

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreditEmploymentGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.credit_employment_get(
                user_token="user_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.credit_employment_get(
            user_token=user_token, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def credit_freddie_mac_reports_get(
        self,
        *,
        audit_copy_token: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreditFreddieMacReportsGetResponse:
        """
        The `credit/asset_report/freddie_mac/get` endpoint retrieves the Verification of Assets and Verification of Employment reports.

        Parameters
        ----------
        audit_copy_token : str
            A token that can be shared with a third party auditor to allow them to obtain access to the Asset Report. This token should be stored securely.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreditFreddieMacReportsGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.credit_freddie_mac_reports_get(
                audit_copy_token="audit_copy_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.credit_freddie_mac_reports_get(
            audit_copy_token=audit_copy_token, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def credit_payroll_income_get(
        self,
        *,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        user_token: typing.Optional[UserToken] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreditPayrollIncomeGetResponse:
        """
        This endpoint gets payroll income information for a specific user, either as a result of the user connecting to their payroll provider or uploading a pay related document.

        Parameters
        ----------
        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        user_token : typing.Optional[UserToken]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreditPayrollIncomeGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.credit_payroll_income_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.credit_payroll_income_get(
            client_id=client_id, secret=secret, user_token=user_token, request_options=request_options
        )
        return _response.data

    async def credit_payroll_income_precheck(
        self,
        *,
        access_tokens: typing.Optional[typing.Sequence[AccessToken]] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        employer: typing.Optional[IncomeVerificationPrecheckEmployer] = OMIT,
        payroll_institution: typing.Optional[IncomeVerificationPrecheckPayrollInstitution] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        us_military_info: typing.Optional[IncomeVerificationPrecheckMilitaryInfo] = OMIT,
        user_token: typing.Optional[UserToken] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreditPayrollIncomePrecheckResponse:
        """
        `/credit/payroll_income/precheck` is an optional endpoint that can be called before initializing a Link session for income verification. It evaluates whether a given user is supportable by digital income verification. If the user is eligible for digital verification, that information will be associated with the user token, and in this way will generate a Link UI optimized for the end user and their specific employer. If the user cannot be confirmed as eligible, the user can still use the income verification flow, but they may be required to manually upload a paystub to verify their income.

        While all request fields are optional, providing `employer` data will increase the chance of receiving a useful result.

        When testing in Sandbox, you can control the results by providing special test values in the `employer` and `access_tokens` fields. `employer_good` and `employer_bad` will result in `HIGH` and `LOW` confidence values, respectively. `employer_multi` will result in a `HIGH` confidence with multiple payroll options. Likewise, `access_good` and `access_bad` will result in `HIGH` and `LOW` confidence values, respectively. Any other value for `employer` and `access_tokens` in Sandbox will result in `UNKNOWN` confidence.

        Parameters
        ----------
        access_tokens : typing.Optional[typing.Sequence[AccessToken]]
            An array of access tokens corresponding to Items belonging to the user whose eligibility is being checked. Note that if the Items specified here are not already initialized with `transactions`, providing them in this field will cause these Items to be initialized with (and billed for) the Transactions product.

        client_id : typing.Optional[ApiClientId]

        employer : typing.Optional[IncomeVerificationPrecheckEmployer]

        payroll_institution : typing.Optional[IncomeVerificationPrecheckPayrollInstitution]

        secret : typing.Optional[ApiSecret]

        us_military_info : typing.Optional[IncomeVerificationPrecheckMilitaryInfo]

        user_token : typing.Optional[UserToken]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreditPayrollIncomePrecheckResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.credit_payroll_income_precheck()


        asyncio.run(main())
        """
        _response = await self._raw_client.credit_payroll_income_precheck(
            access_tokens=access_tokens,
            client_id=client_id,
            employer=employer,
            payroll_institution=payroll_institution,
            secret=secret,
            us_military_info=us_military_info,
            user_token=user_token,
            request_options=request_options,
        )
        return _response.data

    async def credit_payroll_income_refresh(
        self,
        *,
        user_token: UserToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        options: typing.Optional[CreditPayrollIncomeRefreshRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreditPayrollIncomeRefreshResponse:
        """
        `/credit/payroll_income/refresh` refreshes a given digital payroll income verification.

        Parameters
        ----------
        user_token : UserToken

        client_id : typing.Optional[ApiClientId]

        options : typing.Optional[CreditPayrollIncomeRefreshRequestOptions]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreditPayrollIncomeRefreshResponse
            success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.credit_payroll_income_refresh(
                user_token="user_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.credit_payroll_income_refresh(
            user_token=user_token, client_id=client_id, options=options, secret=secret, request_options=request_options
        )
        return _response.data

    async def credit_relay_create(
        self,
        *,
        report_tokens: typing.Sequence[str],
        secondary_client_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        webhook: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreditRelayCreateResponse:
        """
        Plaid can share an Asset Report directly with a participating third party on your behalf. The shared Asset Report is the exact same Asset Report originally created in `/asset_report/create`.

        To grant a third party access to an Asset Report, use the `/credit/relay/create` endpoint to create a `relay_token` and then pass that token to your third party. Each third party has its own `secondary_client_id`; for example, `ce5bd328dcd34123456`. You'll need to create a separate `relay_token` for each third party that needs access to the report on your behalf.

        Parameters
        ----------
        report_tokens : typing.Sequence[str]
            List of report token strings, with at most one token of each report type. Currently only Asset Report token is supported.

        secondary_client_id : str
            The `secondary_client_id` is the client id of the third party with whom you would like to share the relay token.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        webhook : typing.Optional[str]
            URL to which Plaid will send webhooks when the Secondary Client successfully retrieves an Asset Report by calling `/credit/relay/get`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreditRelayCreateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.credit_relay_create(
                report_tokens=["report_tokens"],
                secondary_client_id="secondary_client_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.credit_relay_create(
            report_tokens=report_tokens,
            secondary_client_id=secondary_client_id,
            client_id=client_id,
            secret=secret,
            webhook=webhook,
            request_options=request_options,
        )
        return _response.data

    async def credit_relay_get(
        self,
        *,
        relay_token: str,
        report_type: ReportType,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AssetReportGetResponse:
        """
        `/credit/relay/get` allows third parties to receive a report that was shared with them, using a `relay_token` that was created by the report owner.

        Parameters
        ----------
        relay_token : str
            The `relay_token` granting access to the report you would like to get.

        report_type : ReportType

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AssetReportGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.credit_relay_get(
                relay_token="relay_token",
                report_type="assets",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.credit_relay_get(
            relay_token=relay_token,
            report_type=report_type,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def credit_relay_refresh(
        self,
        *,
        relay_token: str,
        report_type: ReportType,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        webhook: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreditRelayRefreshResponse:
        """
        The `/credit/relay/refresh` endpoint allows third parties to refresh a report that was relayed to them, using a `relay_token` that was created by the report owner. A new report will be created with the original report parameters, but with the most recent data available based on the `days_requested` value of the original report.

        Parameters
        ----------
        relay_token : str
            The `relay_token` granting access to the report you would like to refresh.

        report_type : ReportType

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        webhook : typing.Optional[str]
            The URL registered to receive webhooks when the report of a relay token has been refreshed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreditRelayRefreshResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.credit_relay_refresh(
                relay_token="relay_token",
                report_type="assets",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.credit_relay_refresh(
            relay_token=relay_token,
            report_type=report_type,
            client_id=client_id,
            secret=secret,
            webhook=webhook,
            request_options=request_options,
        )
        return _response.data

    async def credit_relay_remove(
        self,
        *,
        relay_token: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreditRelayRemoveResponse:
        """
        The `/credit/relay/remove` endpoint allows you to invalidate a `relay_token`. The third party holding the token will no longer be able to access or refresh the reports which the `relay_token` gives access to. The original report, associated Items, and other relay tokens that provide access to the same report are not affected and will remain accessible after removing the given `relay_token`.

        Parameters
        ----------
        relay_token : str
            The `relay_token` you would like to revoke.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreditRelayRemoveResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.credit_relay_remove(
                relay_token="relay_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.credit_relay_remove(
            relay_token=relay_token, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def credit_sessions_get(
        self,
        *,
        user_token: UserToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreditSessionsGetResponse:
        """
        This endpoint can be used for your end users after they complete the Link flow. This endpoint returns a list of Link sessions that your user completed, where each session includes the results from the Link flow.

        These results include details about the Item that was created and some product related metadata (showing, for example, whether the user finished the bank income verification step).

        Parameters
        ----------
        user_token : UserToken

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreditSessionsGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.credit_sessions_get(
                user_token="user_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.credit_sessions_get(
            user_token=user_token, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def dashboard_user_get(
        self,
        *,
        dashboard_user_id: DashboardUserId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DashboardUserGetResponse:
        """
        Retrieve information about a dashboard user.

        Parameters
        ----------
        dashboard_user_id : DashboardUserId

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DashboardUserGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.dashboard_user_get(
                dashboard_user_id="54350110fedcbaf01234ffee",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.dashboard_user_get(
            dashboard_user_id=dashboard_user_id, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def dashboard_user_list(
        self,
        *,
        client_id: typing.Optional[ApiClientId] = OMIT,
        cursor: typing.Optional[Cursor] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DashboardUserListResponse:
        """
        List all dashboard users associated with your account.

        Parameters
        ----------
        client_id : typing.Optional[ApiClientId]

        cursor : typing.Optional[Cursor]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DashboardUserListResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.dashboard_user_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.dashboard_user_list(
            client_id=client_id, cursor=cursor, secret=secret, request_options=request_options
        )
        return _response.data

    async def deposit_switch_alt_create(
        self,
        *,
        target_account: DepositSwitchTargetAccount,
        target_user: DepositSwitchTargetUser,
        client_id: typing.Optional[ApiClientId] = OMIT,
        country_code: typing.Optional[DepositSwitchAltCreateRequestCountryCode] = OMIT,
        options: typing.Optional[DepositSwitchCreateRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DepositSwitchAltCreateResponse:
        """
        This endpoint provides an alternative to `/deposit_switch/create` for customers who have not yet fully integrated with Plaid Exchange. Like `/deposit_switch/create`, it creates a deposit switch entity that will be persisted throughout the lifecycle of the switch.

        Parameters
        ----------
        target_account : DepositSwitchTargetAccount

        target_user : DepositSwitchTargetUser

        client_id : typing.Optional[ApiClientId]

        country_code : typing.Optional[DepositSwitchAltCreateRequestCountryCode]
            ISO-3166-1 alpha-2 country code standard.

        options : typing.Optional[DepositSwitchCreateRequestOptions]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DepositSwitchAltCreateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            DepositSwitchTargetAccount,
            DepositSwitchTargetUser,
        )

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.deposit_switch_alt_create(
                target_account=DepositSwitchTargetAccount(
                    account_name="account_name",
                    account_number="account_number",
                    account_subtype="checking",
                    routing_number="routing_number",
                ),
                target_user=DepositSwitchTargetUser(
                    email="email",
                    family_name="family_name",
                    given_name="given_name",
                    phone="phone",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deposit_switch_alt_create(
            target_account=target_account,
            target_user=target_user,
            client_id=client_id,
            country_code=country_code,
            options=options,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def deposit_switch_create(
        self,
        *,
        target_access_token: str,
        target_account_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        country_code: typing.Optional[DepositSwitchCreateRequestCountryCode] = OMIT,
        options: typing.Optional[DepositSwitchCreateRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DepositSwitchCreateResponse:
        """
        This endpoint creates a deposit switch entity that will be persisted throughout the lifecycle of the switch.

        Parameters
        ----------
        target_access_token : str
            Access token for the target Item, typically provided in the Import Item response.

        target_account_id : str
            Plaid Account ID that specifies the target bank account. This account will become the recipient for a user's direct deposit.

        client_id : typing.Optional[ApiClientId]

        country_code : typing.Optional[DepositSwitchCreateRequestCountryCode]
            ISO-3166-1 alpha-2 country code standard.

        options : typing.Optional[DepositSwitchCreateRequestOptions]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DepositSwitchCreateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.deposit_switch_create(
                target_access_token="target_access_token",
                target_account_id="target_account_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deposit_switch_create(
            target_access_token=target_access_token,
            target_account_id=target_account_id,
            client_id=client_id,
            country_code=country_code,
            options=options,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def deposit_switch_get(
        self,
        *,
        deposit_switch_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DepositSwitchGetResponse:
        """
        This endpoint returns information related to how the user has configured their payroll allocation and the state of the switch. You can use this information to build logic related to the user's direct deposit allocation preferences.

        Parameters
        ----------
        deposit_switch_id : str
            The ID of the deposit switch

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DepositSwitchGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.deposit_switch_get(
                deposit_switch_id="deposit_switch_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deposit_switch_get(
            deposit_switch_id=deposit_switch_id, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def deposit_switch_token_create(
        self,
        *,
        deposit_switch_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DepositSwitchTokenCreateResponse:
        """
        In order for the end user to take action, you will need to create a public token representing the deposit switch. This token is used to initialize Link. It can be used one time and expires after 30 minutes.

        Parameters
        ----------
        deposit_switch_id : str
            The ID of the deposit switch

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DepositSwitchTokenCreateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.deposit_switch_token_create(
                deposit_switch_id="deposit_switch_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deposit_switch_token_create(
            deposit_switch_id=deposit_switch_id, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def employers_search(
        self,
        *,
        products: typing.Sequence[str],
        query: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EmployersSearchResponse:
        """
        `/employers/search` allows you the ability to search Plaid’s database of known employers, for use with Deposit Switch. You can use this endpoint to look up a user's employer in order to confirm that they are supported. Users with non-supported employers can then be routed out of the Deposit Switch flow.

        The data in the employer database is currently limited. As the Deposit Switch and Income products progress through their respective beta periods, more employers are being regularly added. Because the employer database is frequently updated, we recommend that you do not cache or store data from this endpoint for more than a day.

        Parameters
        ----------
        products : typing.Sequence[str]
            The Plaid products the returned employers should support. Currently, this field must be set to `"deposit_switch"`.

        query : str
            The employer name to be searched for.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmployersSearchResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.employers_search(
                products=["products"],
                query="query",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.employers_search(
            products=products, query=query, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def employment_verification_get(
        self,
        *,
        access_token: AccessToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EmploymentVerificationGetResponse:
        """
        `/employment/verification/get` returns a list of employments through a user payroll that was verified by an end user.

        This endpoint has been deprecated; new integrations should use `/credit/employment/get` instead.

        Parameters
        ----------
        access_token : AccessToken

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmploymentVerificationGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.employment_verification_get(
                access_token="access_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.employment_verification_get(
            access_token=access_token, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def fdx_notifications(
        self,
        *,
        category: FdxNotificationCategory,
        notification_id: str,
        notification_payload: FdxNotificationPayload,
        publisher: FdxParty,
        sent_on: FdxTimestamp,
        type: FdxNotificationType,
        priority: typing.Optional[FdxNotificationPriority] = OMIT,
        severity: typing.Optional[FdxNotificationSeverity] = OMIT,
        subscriber: typing.Optional[FdxParty] = OMIT,
        url: typing.Optional[FdxHateoasLink] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        A generic webhook receiver endpoint for FDX Event Notifications

        Parameters
        ----------
        category : FdxNotificationCategory

        notification_id : str
            Id of notification

        notification_payload : FdxNotificationPayload

        publisher : FdxParty

        sent_on : FdxTimestamp

        type : FdxNotificationType

        priority : typing.Optional[FdxNotificationPriority]

        severity : typing.Optional[FdxNotificationSeverity]

        subscriber : typing.Optional[FdxParty]

        url : typing.Optional[FdxHateoasLink]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi, FdxNotificationPayload, FdxParty

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.fdx_notifications(
                category="SECURITY",
                notification_id="notificationId",
                notification_payload=FdxNotificationPayload(),
                publisher=FdxParty(
                    name="name",
                    type="DATA_ACCESS_PLATFORM",
                ),
                sent_on=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                type="CONSENT_REVOKED",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fdx_notifications(
            category=category,
            notification_id=notification_id,
            notification_payload=notification_payload,
            publisher=publisher,
            sent_on=sent_on,
            type=type,
            priority=priority,
            severity=severity,
            subscriber=subscriber,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def identity_get(
        self,
        *,
        access_token: AccessToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        options: typing.Optional[IdentityGetRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IdentityGetResponse:
        """
        The `/identity/get` endpoint allows you to retrieve various account holder information on file with the financial institution, including names, emails, phone numbers, and addresses. Only name data is guaranteed to be returned; other fields will be empty arrays if not provided by the institution.

        This request may take some time to complete if identity was not specified as an initial product when creating the Item. This is because Plaid must communicate directly with the institution to retrieve the data.

        Note: In API versions 2018-05-22 and earlier, the `owners` object is not returned, and instead identity information is returned in the top level `identity` object. For more details, see [Plaid API versioning](https://plaid.com/docs/api/versioning/#version-2019-05-29).

        Parameters
        ----------
        access_token : AccessToken

        client_id : typing.Optional[ApiClientId]

        options : typing.Optional[IdentityGetRequestOptions]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IdentityGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.identity_get(
                access_token="access_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.identity_get(
            access_token=access_token,
            client_id=client_id,
            options=options,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def identity_match(
        self,
        *,
        access_token: AccessToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        identity_verification_id: typing.Optional[IdentityMatchIdentityVerificationId] = OMIT,
        options: typing.Optional[IdentityMatchRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        user: typing.Optional[IdentityMatchUser] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IdentityMatchResponse:
        """
        The `/identity/match` endpoint generates a match score, which indicates how well the provided identity data matches the identity information on file with the account holder's financial institution.

        This request may take some time to complete if Identity was not specified as an initial product when creating the Item. This is because Plaid must communicate directly with the institution to retrieve the data.

        Parameters
        ----------
        access_token : AccessToken

        client_id : typing.Optional[ApiClientId]

        identity_verification_id : typing.Optional[IdentityMatchIdentityVerificationId]

        options : typing.Optional[IdentityMatchRequestOptions]

        secret : typing.Optional[ApiSecret]

        user : typing.Optional[IdentityMatchUser]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IdentityMatchResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.identity_match(
                access_token="access_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.identity_match(
            access_token=access_token,
            client_id=client_id,
            identity_verification_id=identity_verification_id,
            options=options,
            secret=secret,
            user=user,
            request_options=request_options,
        )
        return _response.data

    async def identity_verification_create(
        self,
        *,
        gave_consent: IdentityVerificationConsent,
        is_shareable: bool,
        template_id: IdentityVerificationTemplateId,
        user: IdentityVerificationRequestUser,
        client_id: typing.Optional[ApiClientId] = OMIT,
        is_idempotent: typing.Optional[IdempotencyFlag] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IdentityVerificationCreateResponse:
        """
        Create a new Identity Verification for the user specified by the `client_user_id` field. The requirements and behavior of the verification are determined by the `template_id` provided.
        If you don't know whether the associated user already has an active Identity Verification, you can specify `"is_idempotent": true` in the request body. With idempotency enabled, a new Identity Verification will only be created if one does not already exist for the associated `client_user_id` and `template_id`. If an Identity Verification is found, it will be returned unmodified with an `200 OK` HTTP status code.

        Parameters
        ----------
        gave_consent : IdentityVerificationConsent

        is_shareable : bool
            A flag specifying whether you would like Plaid to expose a shareable URL for the verification being created.

        template_id : IdentityVerificationTemplateId

        user : IdentityVerificationRequestUser

        client_id : typing.Optional[ApiClientId]

        is_idempotent : typing.Optional[IdempotencyFlag]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IdentityVerificationCreateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, IdentityVerificationRequestUser

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.identity_verification_create(
                gave_consent=True,
                is_shareable=True,
                template_id="idvtmp_4FrXJvfQU3zGUR",
                user=IdentityVerificationRequestUser(
                    client_user_id="your-db-id-3b24110",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.identity_verification_create(
            gave_consent=gave_consent,
            is_shareable=is_shareable,
            template_id=template_id,
            user=user,
            client_id=client_id,
            is_idempotent=is_idempotent,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def identity_verification_get(
        self,
        *,
        identity_verification_id: IdentityVerificationId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IdentityVerificationGetResponse:
        """
        Retrieve a previously created identity verification.

        Parameters
        ----------
        identity_verification_id : IdentityVerificationId

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IdentityVerificationGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.identity_verification_get(
                identity_verification_id="idv_52xR9LKo77r1Np",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.identity_verification_get(
            identity_verification_id=identity_verification_id,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def identity_verification_list(
        self,
        *,
        client_user_id: ClientUserId,
        template_id: IdentityVerificationTemplateId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        cursor: typing.Optional[Cursor] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IdentityVerificationListResponse:
        """
        Filter and list Identity Verifications created by your account

        Parameters
        ----------
        client_user_id : ClientUserId

        template_id : IdentityVerificationTemplateId

        client_id : typing.Optional[ApiClientId]

        cursor : typing.Optional[Cursor]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IdentityVerificationListResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.identity_verification_list(
                client_user_id="your-db-id-3b24110",
                template_id="idvtmp_4FrXJvfQU3zGUR",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.identity_verification_list(
            client_user_id=client_user_id,
            template_id=template_id,
            client_id=client_id,
            cursor=cursor,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def identity_verification_retry(
        self,
        *,
        client_user_id: ClientUserId,
        strategy: Strategy,
        template_id: IdentityVerificationTemplateId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        steps: typing.Optional[IdentityVerificationRetryRequestStepsObject] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IdentityVerificationRetryResponse:
        """
        Allow a customer to retry their identity verification

        Parameters
        ----------
        client_user_id : ClientUserId

        strategy : Strategy

        template_id : IdentityVerificationTemplateId

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        steps : typing.Optional[IdentityVerificationRetryRequestStepsObject]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IdentityVerificationRetryResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.identity_verification_retry(
                client_user_id="your-db-id-3b24110",
                strategy="reset",
                template_id="idvtmp_4FrXJvfQU3zGUR",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.identity_verification_retry(
            client_user_id=client_user_id,
            strategy=strategy,
            template_id=template_id,
            client_id=client_id,
            secret=secret,
            steps=steps,
            request_options=request_options,
        )
        return _response.data

    async def income_verification_create(
        self,
        *,
        webhook: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        options: typing.Optional[IncomeVerificationCreateRequestOptions] = OMIT,
        precheck_id: typing.Optional[str] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IncomeVerificationCreateResponse:
        """
        `/income/verification/create` begins the income verification process by returning an `income_verification_id`. You can then provide the `income_verification_id` to `/link/token/create` under the `income_verification` parameter in order to create a Link instance that will prompt the user to go through the income verification flow. Plaid will fire an `INCOME` webhook once the user completes the Payroll Income flow, or when the uploaded documents in the Document Income flow have finished processing.

        Parameters
        ----------
        webhook : str
            The URL endpoint to which Plaid should send webhooks related to the progress of the income verification process.

        client_id : typing.Optional[ApiClientId]

        options : typing.Optional[IncomeVerificationCreateRequestOptions]

        precheck_id : typing.Optional[str]
            The ID of a precheck created with `/income/verification/precheck`. Will be used to improve conversion of the income verification flow.

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IncomeVerificationCreateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.income_verification_create(
                webhook="webhook",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.income_verification_create(
            webhook=webhook,
            client_id=client_id,
            options=options,
            precheck_id=precheck_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def income_verification_documents_download(
        self,
        *,
        access_token: typing.Optional[AccessTokenNullable] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        document_id: typing.Optional[str] = OMIT,
        income_verification_id: typing.Optional[str] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        `/income/verification/documents/download` provides the ability to download the source documents associated with the verification.

        If Document Income was used, the documents will be those the user provided in Link. For Payroll Income, the most recent files available
        for download from the payroll provider will be available from this endpoint.

        The response to `/income/verification/documents/download` is a ZIP file in binary data. If a `document_id` is passed, a single document will be contained in this file.
        If not, the response will contain all documents associated with the verification.

        The `request_id` is returned in the `Plaid-Request-ID` header.

        Parameters
        ----------
        access_token : typing.Optional[AccessTokenNullable]

        client_id : typing.Optional[ApiClientId]

        document_id : typing.Optional[str]
            The document ID to download. If passed, a single document will be returned in the resulting zip file, rather than all document

        income_verification_id : typing.Optional[str]
            The ID of the verification.

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            A ZIP file containing source documents(s) used as the basis for income verification.
        """
        async with self._raw_client.income_verification_documents_download(
            access_token=access_token,
            client_id=client_id,
            document_id=document_id,
            income_verification_id=income_verification_id,
            secret=secret,
            request_options=request_options,
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def income_verification_paystubs_get(
        self,
        *,
        access_token: typing.Optional[AccessTokenNullable] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        income_verification_id: typing.Optional[str] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IncomeVerificationPaystubsGetResponse:
        """
        `/income/verification/paystubs/get` returns the information collected from the paystubs that were used to verify an end user's income. It can be called once the status of the verification has been set to `VERIFICATION_STATUS_PROCESSING_COMPLETE`, as reported by the `INCOME: verification_status` webhook. Attempting to call the endpoint before verification has been completed will result in an error.

        This endpoint has been deprecated; new integrations should use `/credit/payroll_income/get` instead.

        Parameters
        ----------
        access_token : typing.Optional[AccessTokenNullable]

        client_id : typing.Optional[ApiClientId]

        income_verification_id : typing.Optional[str]
            The ID of the verification for which to get paystub information.

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IncomeVerificationPaystubsGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.income_verification_paystubs_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.income_verification_paystubs_get(
            access_token=access_token,
            client_id=client_id,
            income_verification_id=income_verification_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def income_verification_precheck(
        self,
        *,
        client_id: typing.Optional[ApiClientId] = OMIT,
        employer: typing.Optional[IncomeVerificationPrecheckEmployer] = OMIT,
        payroll_institution: typing.Optional[IncomeVerificationPrecheckPayrollInstitution] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        transactions_access_token: typing.Optional[AccessTokenNullable] = OMIT,
        transactions_access_tokens: typing.Optional[typing.Sequence[AccessToken]] = OMIT,
        us_military_info: typing.Optional[IncomeVerificationPrecheckMilitaryInfo] = OMIT,
        user: typing.Optional[IncomeVerificationPrecheckUser] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IncomeVerificationPrecheckResponse:
        """
        `/income/verification/precheck` is an optional endpoint that can be called before initializing a Link session for income verification. It evaluates whether a given user is supportable by digital income verification and returns a `precheck_id` that can be provided to `/link/token/create`. If the user is eligible for digital verification, providing the `precheck_id` in this way will generate a Link UI optimized for the end user and their specific employer. If the user cannot be confirmed as eligible, the `precheck_id` can still be provided to `/link/token/create` and the user can still use the income verification flow, but they may be required to manually upload a paystub to verify their income.

        While all request fields are optional, providing either `employer` or `transactions_access_tokens` data will increase the chance of receiving a useful result.

        This endpoint has been deprecated; new integrations should use `/credit/payroll_income/precheck` instead.

        Parameters
        ----------
        client_id : typing.Optional[ApiClientId]

        employer : typing.Optional[IncomeVerificationPrecheckEmployer]

        payroll_institution : typing.Optional[IncomeVerificationPrecheckPayrollInstitution]

        secret : typing.Optional[ApiSecret]

        transactions_access_token : typing.Optional[AccessTokenNullable]

        transactions_access_tokens : typing.Optional[typing.Sequence[AccessToken]]
            An array of access tokens corresponding to Items belonging to the user whose eligibility is being checked. Note that if the Items specified here are not already initialized with `transactions`, providing them in this field will cause these Items to be initialized with (and billed for) the Transactions product.

        us_military_info : typing.Optional[IncomeVerificationPrecheckMilitaryInfo]

        user : typing.Optional[IncomeVerificationPrecheckUser]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IncomeVerificationPrecheckResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.income_verification_precheck()


        asyncio.run(main())
        """
        _response = await self._raw_client.income_verification_precheck(
            client_id=client_id,
            employer=employer,
            payroll_institution=payroll_institution,
            secret=secret,
            transactions_access_token=transactions_access_token,
            transactions_access_tokens=transactions_access_tokens,
            us_military_info=us_military_info,
            user=user,
            request_options=request_options,
        )
        return _response.data

    async def income_verification_taxforms_get(
        self,
        *,
        access_token: typing.Optional[AccessTokenNullable] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        income_verification_id: typing.Optional[str] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IncomeVerificationTaxformsGetResponse:
        """
        `/income/verification/taxforms/get` returns the information collected from forms that were used to verify an end user''s income. It can be called once the status of the verification has been set to `VERIFICATION_STATUS_PROCESSING_COMPLETE`, as reported by the `INCOME: verification_status` webhook. Attempting to call the endpoint before verification has been completed will result in an error.

        This endpoint has been deprecated; new integrations should use `/credit/payroll_income/get` instead.

        Parameters
        ----------
        access_token : typing.Optional[AccessTokenNullable]

        client_id : typing.Optional[ApiClientId]

        income_verification_id : typing.Optional[str]
            The ID of the verification.

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IncomeVerificationTaxformsGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.income_verification_taxforms_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.income_verification_taxforms_get(
            access_token=access_token,
            client_id=client_id,
            income_verification_id=income_verification_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def institutions_get(
        self,
        *,
        count: int,
        country_codes: typing.Sequence[CountryCode],
        offset: int,
        client_id: typing.Optional[ApiClientId] = OMIT,
        options: typing.Optional[InstitutionsGetRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InstitutionsGetResponse:
        """
        Returns a JSON response containing details on all financial institutions currently supported by Plaid. Because Plaid supports thousands of institutions, results are paginated.

        If there is no overlap between an institution’s enabled products and a client’s enabled products, then the institution will be filtered out from the response. As a result, the number of institutions returned may not match the count specified in the call.

        Parameters
        ----------
        count : int
            The total number of Institutions to return.

        country_codes : typing.Sequence[CountryCode]
            Specify an array of Plaid-supported country codes this institution supports, using the ISO-3166-1 alpha-2 country code standard.

            In API versions 2019-05-29 and earlier, the `country_codes` parameter is an optional parameter within the `options` object and will default to `[US]` if it is not supplied.

        offset : int
            The number of Institutions to skip.

        client_id : typing.Optional[ApiClientId]

        options : typing.Optional[InstitutionsGetRequestOptions]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InstitutionsGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.institutions_get(
                count=1,
                country_codes=["US"],
                offset=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.institutions_get(
            count=count,
            country_codes=country_codes,
            offset=offset,
            client_id=client_id,
            options=options,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def institutions_get_by_id(
        self,
        *,
        country_codes: typing.Sequence[CountryCode],
        institution_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        options: typing.Optional[InstitutionsGetByIdRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InstitutionsGetByIdResponse:
        """
        Returns a JSON response containing details on a specified financial institution currently supported by Plaid.

        Versioning note: API versions 2019-05-29 and earlier allow use of the `public_key` parameter instead of the `client_id` and `secret` to authenticate to this endpoint. The `public_key` has been deprecated; all customers are encouraged to use `client_id` and `secret` instead.

        Parameters
        ----------
        country_codes : typing.Sequence[CountryCode]
            Specify an array of Plaid-supported country codes this institution supports, using the ISO-3166-1 alpha-2 country code standard. In API versions 2019-05-29 and earlier, the `country_codes` parameter is an optional parameter within the `options` object and will default to `[US]` if it is not supplied.

        institution_id : str
            The ID of the institution to get details about

        client_id : typing.Optional[ApiClientId]

        options : typing.Optional[InstitutionsGetByIdRequestOptions]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InstitutionsGetByIdResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.institutions_get_by_id(
                country_codes=["US"],
                institution_id="institution_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.institutions_get_by_id(
            country_codes=country_codes,
            institution_id=institution_id,
            client_id=client_id,
            options=options,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def institutions_search(
        self,
        *,
        country_codes: typing.Sequence[CountryCode],
        query: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        options: typing.Optional[InstitutionsSearchRequestOptions] = OMIT,
        products: typing.Optional[typing.Sequence[Products]] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InstitutionsSearchResponse:
        """
        Returns a JSON response containing details for institutions that match the query parameters, up to a maximum of ten institutions per query.

        Versioning note: API versions 2019-05-29 and earlier allow use of the `public_key` parameter instead of the `client_id` and `secret` parameters to authenticate to this endpoint. The `public_key` parameter has since been deprecated; all customers are encouraged to use `client_id` and `secret` instead.

        Parameters
        ----------
        country_codes : typing.Sequence[CountryCode]
            Specify an array of Plaid-supported country codes this institution supports, using the ISO-3166-1 alpha-2 country code standard. In API versions 2019-05-29 and earlier, the `country_codes` parameter is an optional parameter within the `options` object and will default to `[US]` if it is not supplied.

        query : str
            The search query. Institutions with names matching the query are returned

        client_id : typing.Optional[ApiClientId]

        options : typing.Optional[InstitutionsSearchRequestOptions]

        products : typing.Optional[typing.Sequence[Products]]
            Filter the Institutions based on whether they support all products listed in `products`. Provide `null` to get institutions regardless of supported products. Note that when `auth` is specified as a product, if you are enabled for Instant Match or Automated Micro-deposits, institutions that support those products will be returned even if `auth` is not present in their product array.

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InstitutionsSearchResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.institutions_search(
                country_codes=["US"],
                query="query",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.institutions_search(
            country_codes=country_codes,
            query=query,
            client_id=client_id,
            options=options,
            products=products,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def investments_holdings_get(
        self,
        *,
        access_token: AccessToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        options: typing.Optional[InvestmentHoldingsGetRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InvestmentsHoldingsGetResponse:
        """
        The `/investments/holdings/get` endpoint allows developers to receive user-authorized stock position data for `investment`-type accounts.

        Parameters
        ----------
        access_token : AccessToken

        client_id : typing.Optional[ApiClientId]

        options : typing.Optional[InvestmentHoldingsGetRequestOptions]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InvestmentsHoldingsGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.investments_holdings_get(
                access_token="access_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.investments_holdings_get(
            access_token=access_token,
            client_id=client_id,
            options=options,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def investments_transactions_get(
        self,
        *,
        access_token: AccessToken,
        end_date: dt.date,
        start_date: dt.date,
        client_id: typing.Optional[ApiClientId] = OMIT,
        options: typing.Optional[InvestmentsTransactionsGetRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InvestmentsTransactionsGetResponse:
        """
        The `/investments/transactions/get` endpoint allows developers to retrieve up to 24 months of user-authorized transaction data for investment accounts.

        Transactions are returned in reverse-chronological order, and the sequence of transaction ordering is stable and will not shift.

        Due to the potentially large number of investment transactions associated with an Item, results are paginated. Manipulate the count and offset parameters in conjunction with the `total_investment_transactions` response body field to fetch all available investment transactions.

        Note that Investments does not have a webhook to indicate when initial transaction data has loaded. Instead, if transactions data is not ready when `/investments/transactions/get` is first called, Plaid will wait for the data. For this reason, calling `/investments/transactions/get` immediately after Link may take up to one to two minutes to return.

        Parameters
        ----------
        access_token : AccessToken

        end_date : dt.date
            The most recent date for which to fetch transaction history. Dates should be formatted as YYYY-MM-DD.

        start_date : dt.date
            The earliest date for which to fetch transaction history. Dates should be formatted as YYYY-MM-DD.

        client_id : typing.Optional[ApiClientId]

        options : typing.Optional[InvestmentsTransactionsGetRequestOptions]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InvestmentsTransactionsGetResponse
            OK

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.investments_transactions_get(
                access_token="access_token",
                end_date=datetime.date.fromisoformat(
                    "2023-01-15",
                ),
                start_date=datetime.date.fromisoformat(
                    "2023-01-15",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.investments_transactions_get(
            access_token=access_token,
            end_date=end_date,
            start_date=start_date,
            client_id=client_id,
            options=options,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def item_access_token_invalidate(
        self,
        *,
        access_token: AccessToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ItemAccessTokenInvalidateResponse:
        """
        By default, the `access_token` associated with an Item does not expire and should be stored in a persistent, secure manner.

        You can use the `/item/access_token/invalidate` endpoint to rotate the `access_token` associated with an Item. The endpoint returns a new `access_token` and immediately invalidates the previous `access_token`.

        Parameters
        ----------
        access_token : AccessToken

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ItemAccessTokenInvalidateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.item_access_token_invalidate(
                access_token="access_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.item_access_token_invalidate(
            access_token=access_token, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def item_activity_list(
        self,
        *,
        access_token: typing.Optional[AccessToken] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        count: typing.Optional[int] = OMIT,
        cursor: typing.Optional[str] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ItemActivityListResponse:
        """
        List a historical log of user consent events

        Parameters
        ----------
        access_token : typing.Optional[AccessToken]

        client_id : typing.Optional[ApiClientId]

        count : typing.Optional[int]

        cursor : typing.Optional[str]
            Cursor used for pagination.

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ItemActivityListResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.item_activity_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.item_activity_list(
            access_token=access_token,
            client_id=client_id,
            count=count,
            cursor=cursor,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def item_application_list(
        self,
        *,
        access_token: typing.Optional[AccessTokenNullable] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ItemApplicationListResponse:
        """
        List a user’s connected applications

        Parameters
        ----------
        access_token : typing.Optional[AccessTokenNullable]

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ItemApplicationListResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.item_application_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.item_application_list(
            access_token=access_token, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def item_application_scopes_update(
        self,
        *,
        access_token: AccessToken,
        application_id: ApplicationId,
        context: ScopesContext,
        scopes: Scopes,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        state: typing.Optional[ScopesState] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ItemApplicationScopesUpdateResponse:
        """
        Enable consumers to update product access on selected accounts for an application.

        Parameters
        ----------
        access_token : AccessToken

        application_id : ApplicationId

        context : ScopesContext

        scopes : Scopes

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        state : typing.Optional[ScopesState]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ItemApplicationScopesUpdateResponse
            success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Scopes

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.item_application_scopes_update(
                access_token="access_token",
                application_id="application_id",
                context="ENROLLMENT",
                scopes=Scopes(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.item_application_scopes_update(
            access_token=access_token,
            application_id=application_id,
            context=context,
            scopes=scopes,
            client_id=client_id,
            secret=secret,
            state=state,
            request_options=request_options,
        )
        return _response.data

    async def item_get(
        self,
        *,
        access_token: AccessToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ItemGetResponse:
        """
        Returns information about the status of an Item.

        Parameters
        ----------
        access_token : AccessToken

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ItemGetResponse
            success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.item_get(
                access_token="access_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.item_get(
            access_token=access_token, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def item_import(
        self,
        *,
        products: typing.Sequence[Products],
        user_auth: ItemImportRequestUserAuth,
        client_id: typing.Optional[ApiClientId] = OMIT,
        options: typing.Optional[ItemImportRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ItemImportResponse:
        """
        `/item/import` creates an Item via your Plaid Exchange Integration and returns an `access_token`. As part of an `/item/import` request, you will include a User ID (`user_auth.user_id`) and Authentication Token (`user_auth.auth_token`) that enable data aggregation through your Plaid Exchange API endpoints. These authentication principals are to be chosen by you.

        Upon creating an Item via `/item/import`, Plaid will automatically begin an extraction of that Item through the Plaid Exchange infrastructure you have already integrated. This will automatically generate the Plaid native account ID for the account the user will switch their direct deposit to (`target_account_id`).

        Parameters
        ----------
        products : typing.Sequence[Products]
            Array of product strings

        user_auth : ItemImportRequestUserAuth

        client_id : typing.Optional[ApiClientId]

        options : typing.Optional[ItemImportRequestOptions]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ItemImportResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ItemImportRequestUserAuth

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.item_import(
                products=["assets"],
                user_auth=ItemImportRequestUserAuth(
                    auth_token="auth_token",
                    user_id="user_id",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.item_import(
            products=products,
            user_auth=user_auth,
            client_id=client_id,
            options=options,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def item_create_public_token(
        self,
        *,
        access_token: AccessToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ItemPublicTokenCreateResponse:
        """
        Note: As of July 2020, the `/item/public_token/create` endpoint is deprecated. Instead, use `/link/token/create` with an `access_token` to create a Link token for use with [update mode](https://plaid.com/docs/link/update-mode).

        If you need your user to take action to restore or resolve an error associated with an Item, generate a public token with the `/item/public_token/create` endpoint and then initialize Link with that `public_token`.

        A `public_token` is one-time use and expires after 30 minutes. You use a `public_token` to initialize Link in [update mode](https://plaid.com/docs/link/update-mode) for a particular Item. You can generate a `public_token` for an Item even if you did not use Link to create the Item originally.

        The `/item/public_token/create` endpoint is **not** used to create your initial `public_token`. If you have not already received an `access_token` for a specific Item, use Link to obtain your `public_token` instead. See the [Quickstart](https://plaid.com/docs/quickstart) for more information.

        Parameters
        ----------
        access_token : AccessToken

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ItemPublicTokenCreateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.item_create_public_token(
                access_token="access_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.item_create_public_token(
            access_token=access_token, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def item_public_token_exchange(
        self,
        *,
        public_token: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ItemPublicTokenExchangeResponse:
        """
        Exchange a Link `public_token` for an API `access_token`. Link hands off the `public_token` client-side via the `onSuccess` callback once a user has successfully created an Item. The `public_token` is ephemeral and expires after 30 minutes. An `access_token` does not expire, but can be revoked by calling `/item/remove`.

        The response also includes an `item_id` that should be stored with the `access_token`. The `item_id` is used to identify an Item in a webhook. The `item_id` can also be retrieved by making an `/item/get` request.

        Parameters
        ----------
        public_token : str
            Your `public_token`, obtained from the Link `onSuccess` callback or `/sandbox/item/public_token/create`.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ItemPublicTokenExchangeResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.item_public_token_exchange(
                public_token="public_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.item_public_token_exchange(
            public_token=public_token, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def item_remove(
        self,
        *,
        access_token: AccessToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ItemRemoveResponse:
        """
        The `/item/remove` endpoint allows you to remove an Item. Once removed, the `access_token`, as well as any processor tokens or bank account tokens associated with the Item, is no longer valid and cannot be used to access any data that was associated with the Item.

        Note that in the Development environment, issuing an `/item/remove`  request will not decrement your live credential count. To increase your credential account in Development, contact Support.

        Also note that for certain OAuth-based institutions, an Item removed via `/item/remove` may still show as an active connection in the institution's OAuth permission manager.

        API versions 2019-05-29 and earlier return a `removed` boolean as part of the response.

        Parameters
        ----------
        access_token : AccessToken

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ItemRemoveResponse
            success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.item_remove(
                access_token="access_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.item_remove(
            access_token=access_token, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def item_webhook_update(
        self,
        *,
        access_token: AccessToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        webhook: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ItemWebhookUpdateResponse:
        """
        The POST `/item/webhook/update` allows you to update the webhook URL associated with an Item. This request triggers a [`WEBHOOK_UPDATE_ACKNOWLEDGED`](https://plaid.com/docs/api/items/#webhook_update_acknowledged) webhook to the newly specified webhook URL.

        Parameters
        ----------
        access_token : AccessToken

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        webhook : typing.Optional[str]
            The new webhook URL to associate with the Item. To remove a webhook from an Item, set to `null`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ItemWebhookUpdateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.item_webhook_update(
                access_token="access_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.item_webhook_update(
            access_token=access_token,
            client_id=client_id,
            secret=secret,
            webhook=webhook,
            request_options=request_options,
        )
        return _response.data

    async def liabilities_get(
        self,
        *,
        access_token: AccessToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        options: typing.Optional[LiabilitiesGetRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LiabilitiesGetResponse:
        """
        The `/liabilities/get` endpoint returns various details about an Item with loan or credit accounts. Liabilities data is available primarily for US financial institutions, with some limited coverage of Canadian institutions. Currently supported account types are account type `credit` with account subtype `credit card` or `paypal`, and account type `loan` with account subtype `student` or `mortgage`. To limit accounts listed in Link to types and subtypes supported by Liabilities, you can use the `account_filters` parameter when [creating a Link token](https://plaid.com/docs/api/tokens/#linktokencreate).

        The types of information returned by Liabilities can include balances and due dates, loan terms, and account details such as original loan amount and guarantor. Data is refreshed approximately once per day; the latest data can be retrieved by calling `/liabilities/get`.

        Note: This request may take some time to complete if `liabilities` was not specified as an initial product when creating the Item. This is because Plaid must communicate directly with the institution to retrieve the additional data.

        Parameters
        ----------
        access_token : AccessToken

        client_id : typing.Optional[ApiClientId]

        options : typing.Optional[LiabilitiesGetRequestOptions]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LiabilitiesGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.liabilities_get(
                access_token="access_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.liabilities_get(
            access_token=access_token,
            client_id=client_id,
            options=options,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def link_oauth_correlation_id_exchange(
        self,
        *,
        link_correlation_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LinkOAuthCorrelationIdExchangeResponse:
        """
        Exchange an OAuth `link_correlation_id` for the corresponding `link_token`. The `link_correlation_id` is only available for 'payment_initiation' products and is provided to the client via the OAuth `redirect_uri` as a query parameter.
        The `link_correlation_id` is ephemeral and expires in a brief period, after which it can no longer be exchanged for the 'link_token'.

        Parameters
        ----------
        link_correlation_id : str
            A `link_correlation_id` from a received OAuth redirect URI callback

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LinkOAuthCorrelationIdExchangeResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.link_oauth_correlation_id_exchange(
                link_correlation_id="link_correlation_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.link_oauth_correlation_id_exchange(
            link_correlation_id=link_correlation_id, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def link_token_create(
        self,
        *,
        client_name: str,
        country_codes: typing.Sequence[CountryCode],
        language: str,
        user: LinkTokenCreateRequestUser,
        access_token: typing.Optional[str] = OMIT,
        account_filters: typing.Optional[LinkTokenAccountFilters] = OMIT,
        additional_consented_products: typing.Optional[typing.Sequence[Products]] = OMIT,
        android_package_name: typing.Optional[str] = OMIT,
        auth: typing.Optional[LinkTokenCreateRequestAuth] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        deposit_switch: typing.Optional[LinkTokenCreateRequestDepositSwitch] = OMIT,
        employment: typing.Optional[LinkTokenCreateRequestEmployment] = OMIT,
        eu_config: typing.Optional[LinkTokenEuConfig] = OMIT,
        identity_verification: typing.Optional[LinkTokenCreateRequestIdentityVerification] = OMIT,
        income_verification: typing.Optional[LinkTokenCreateRequestIncomeVerification] = OMIT,
        institution_data: typing.Optional[LinkTokenCreateInstitutionData] = OMIT,
        institution_id: typing.Optional[str] = OMIT,
        investments: typing.Optional[LinkTokenInvestments] = OMIT,
        link_customization_name: typing.Optional[str] = OMIT,
        payment_initiation: typing.Optional[LinkTokenCreateRequestPaymentInitiation] = OMIT,
        products: typing.Optional[typing.Sequence[Products]] = OMIT,
        redirect_uri: typing.Optional[str] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        transfer: typing.Optional[LinkTokenCreateRequestTransfer] = OMIT,
        update: typing.Optional[LinkTokenCreateRequestUpdate] = OMIT,
        user_token: typing.Optional[str] = OMIT,
        webhook: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LinkTokenCreateResponse:
        """
        The `/link/token/create` endpoint creates a `link_token`, which is required as a parameter when initializing Link. Once Link has been initialized, it returns a `public_token`, which can then be exchanged for an `access_token` via `/item/public_token/exchange` as part of the main Link flow.

        A `link_token` generated by `/link/token/create` is also used to initialize other Link flows, such as the update mode flow for tokens with expired credentials, or the Payment Initiation (Europe) flow.

        Parameters
        ----------
        client_name : str
            The name of your application, as it should be displayed in Link. Maximum length of 30 characters. If a value longer than 30 characters is provided, Link will display "This Application" instead.

        country_codes : typing.Sequence[CountryCode]
            Specify an array of Plaid-supported country codes using the ISO-3166-1 alpha-2 country code standard. Institutions from all listed countries will be shown. For a complete mapping of supported products by country, see https://plaid.com/global/.

            If Link is launched with multiple country codes, only products that you are enabled for in all countries will be used by Link. Note that while all countries are enabled by default in Sandbox and Development, in Production only US and Canada are enabled by default. Access to European institutions requires additional compliance steps. To request access to European institutions in the Production environment, [file a product access Support ticket](https://dashboard.plaid.com/support/new/product-and-development/product-troubleshooting/request-product-access) via the Plaid dashboard. If you initialize with a European country code, your users will see the European consent panel during the Link flow.

            If using a Link customization, make sure the country codes in the customization match those specified in `country_codes`, or the customization may not be applied.

            If using the Auth features Instant Match, Same-day Micro-deposits, or Automated Micro-deposits, `country_codes` must be set to `['US']`.

        language : str
            The language that Link should be displayed in. When initializing with Identity Verification, this field is not used; for more details, see [Identity Verification supported languages](https://www.plaid.com/docs/identity-verification/#supported-languages).

            Supported languages are:
            - Danish (`'da'`)
            - Dutch (`'nl'`)
            - English (`'en'`)
            - Estonian (`'et'`)
            - French (`'fr'`)
            - German (`'de'`)
            - Italian (`'it'`)
            - Latvian (`'lv'`)
            - Lithuanian (`'lt'`)
            - Norwegian (`'no'`)
            - Polish (`'pl'`)
            - Portuguese (`'pt'`)
            - Romanian (`'ro'`)
            - Spanish (`'es'`)
            - Swedish (`'se'`)

            When using a Link customization, the language configured here must match the setting in the customization, or the customization will not be applied.

        user : LinkTokenCreateRequestUser

        access_token : typing.Optional[str]
            The `access_token` associated with the Item to update or reference, used when updating, modifying, or accessing an existing `access_token`. Used when launching Link in update mode, when completing the Same-day (manual) Micro-deposit flow, or (optionally) when initializing Link for a returning user as part of the Transfer UI flow.

        account_filters : typing.Optional[LinkTokenAccountFilters]

        additional_consented_products : typing.Optional[typing.Sequence[Products]]
            (Beta) This field has no effect unless you are participating in the Product Scope Transparency beta program.
            List of additional Plaid product(s) you wish to collect consent for. These products will not be billed until you start using them by calling the relevant endpoints.

            `balance` is *not* a valid value, the Balance product does not require explicit initialization and will automatically have consent collected.

            Institutions that do not support these products will still be shown in Link

        android_package_name : typing.Optional[str]
            The name of your app's Android package. Required if using the `link_token` to initialize Link on Android. Any package name specified here must also be added to the Allowed Android package names setting on the [developer dashboard](https://dashboard.plaid.com/team/api). When creating a `link_token` for initializing Link on other platforms, `android_package_name` must be left blank and `redirect_uri` should be used instead.

        auth : typing.Optional[LinkTokenCreateRequestAuth]

        client_id : typing.Optional[ApiClientId]

        deposit_switch : typing.Optional[LinkTokenCreateRequestDepositSwitch]

        employment : typing.Optional[LinkTokenCreateRequestEmployment]

        eu_config : typing.Optional[LinkTokenEuConfig]

        identity_verification : typing.Optional[LinkTokenCreateRequestIdentityVerification]

        income_verification : typing.Optional[LinkTokenCreateRequestIncomeVerification]

        institution_data : typing.Optional[LinkTokenCreateInstitutionData]

        institution_id : typing.Optional[str]
            Used for certain Europe-only configurations, as well as certain legacy use cases in other regions.

        investments : typing.Optional[LinkTokenInvestments]

        link_customization_name : typing.Optional[str]
            The name of the Link customization from the Plaid Dashboard to be applied to Link. If not specified, the `default` customization will be used. When using a Link customization, the language in the customization must match the language selected via the `language` parameter, and the countries in the customization should match the country codes selected via `country_codes`.

        payment_initiation : typing.Optional[LinkTokenCreateRequestPaymentInitiation]

        products : typing.Optional[typing.Sequence[Products]]
            List of Plaid product(s) you wish to use. If launching Link in update mode, should be omitted (unless you are using update mode to add Income or Assets to an Item); required otherwise.

            `balance` is *not* a valid value, the Balance product does not require explicit initialization and will automatically be initialized when any other product is initialized.

            The products specified here will determine which institutions will be available to your users in Link. Only institutions that support *all* requested products can be selected; a if a user attempts to select an institution that does not support a listed product, a "Connectivity not supported" error message will appear in Link. To maximize the number of institutions available, initialize Link with the minimal product set required for your use case. Additional products can be added after Link initialization by calling the relevant endpoints. For details and exceptions, see [Choosing when to initialize products](https://plaid.com/docs/link/initializing-products/).

            Note that, unless you have opted to disable Instant Match support, institutions that support Instant Match will also be shown in Link if `auth` is specified as a product, even though these institutions do not contain `auth` in their product array.

            In Production, you will be billed for each product that you specify when initializing Link. Note that a product cannot be removed from an Item once the Item has been initialized with that product. To stop billing on an Item for subscription-based products, such as Liabilities, Investments, and Transactions, remove the Item via `/item/remove`.

        redirect_uri : typing.Optional[str]
            A URI indicating the destination where a user should be forwarded after completing the Link flow; used to support OAuth authentication flows when launching Link in the browser or via a webview. The `redirect_uri` should not contain any query parameters. When used in Production or Development, must be an https URI. To specify any subdomain, use `*` as a wildcard character, e.g. `https://*.example.com/oauth.html`. Note that any redirect URI must also be added to the Allowed redirect URIs list in the [developer dashboard](https://dashboard.plaid.com/team/api). If initializing on Android, `android_package_name` must be specified instead and `redirect_uri` should be left blank.

        secret : typing.Optional[ApiSecret]

        transfer : typing.Optional[LinkTokenCreateRequestTransfer]

        update : typing.Optional[LinkTokenCreateRequestUpdate]

        user_token : typing.Optional[str]
            A user token generated using `/user/create`. Any Item created during the Link session will be associated with the user.

        webhook : typing.Optional[str]
            The destination URL to which any webhooks should be sent. Note that webhooks for Payment Initiation (e-wallet transactions only), Transfer, Bank Transfer (including Auth micro-deposit notification webhooks) and Identity Verification are configured via the Dashboard instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LinkTokenCreateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, LinkTokenCreateRequestUser

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.link_token_create(
                client_name="client_name",
                country_codes=["US"],
                language="language",
                user=LinkTokenCreateRequestUser(
                    client_user_id="client_user_id",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.link_token_create(
            client_name=client_name,
            country_codes=country_codes,
            language=language,
            user=user,
            access_token=access_token,
            account_filters=account_filters,
            additional_consented_products=additional_consented_products,
            android_package_name=android_package_name,
            auth=auth,
            client_id=client_id,
            deposit_switch=deposit_switch,
            employment=employment,
            eu_config=eu_config,
            identity_verification=identity_verification,
            income_verification=income_verification,
            institution_data=institution_data,
            institution_id=institution_id,
            investments=investments,
            link_customization_name=link_customization_name,
            payment_initiation=payment_initiation,
            products=products,
            redirect_uri=redirect_uri,
            secret=secret,
            transfer=transfer,
            update=update,
            user_token=user_token,
            webhook=webhook,
            request_options=request_options,
        )
        return _response.data

    async def link_token_get(
        self,
        *,
        link_token: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LinkTokenGetResponse:
        """
        The `/link/token/get` endpoint gets information about a previously-created `link_token` using the
        `/link/token/create` endpoint. It can be useful for debugging purposes.

        Parameters
        ----------
        link_token : str
            A `link_token` from a previous invocation of `/link/token/create`

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LinkTokenGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.link_token_get(
                link_token="link_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.link_token_get(
            link_token=link_token, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def link_delivery_create(
        self,
        *,
        link_token: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        options: typing.Optional[LinkDeliveryOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LinkDeliveryCreateResponse:
        """
        Use the `/link_delivery/create` endpoint to create a Link Delivery session.

        Parameters
        ----------
        link_token : str
            A `link_token` from a previous invocation of `/link/token/create` with Link Delivery enabled.

        client_id : typing.Optional[ApiClientId]

        options : typing.Optional[LinkDeliveryOptions]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LinkDeliveryCreateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.link_delivery_create(
                link_token="link_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.link_delivery_create(
            link_token=link_token, client_id=client_id, options=options, secret=secret, request_options=request_options
        )
        return _response.data

    async def link_delivery_get(
        self,
        *,
        link_delivery_session_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LinkDeliveryGetResponse:
        """
        Use the `/link_delivery/get` endpoint to get the status of a Link Delivery session.

        Parameters
        ----------
        link_delivery_session_id : str
            The ID for the Link Delivery session from a previous invocation of `/link_delivery/create`.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LinkDeliveryGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.link_delivery_get(
                link_delivery_session_id="link_delivery_session_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.link_delivery_get(
            link_delivery_session_id=link_delivery_session_id,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def partner_customer_create(
        self,
        *,
        address: PartnerEndCustomerAddress,
        application_name: str,
        company_name: str,
        is_bank_addendum_completed: bool,
        is_diligence_attested: bool,
        legal_entity_name: str,
        products: typing.Sequence[Products],
        website: str,
        assets_under_management: typing.Optional[PartnerEndCustomerAssetsUnderManagement] = OMIT,
        billing_contact: typing.Optional[PartnerEndCustomerBillingContact] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        create_link_customization: typing.Optional[bool] = OMIT,
        customer_support_info: typing.Optional[PartnerEndCustomerCustomerSupportInfo] = OMIT,
        logo: typing.Optional[str] = OMIT,
        redirect_uris: typing.Optional[typing.Sequence[str]] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        technical_contact: typing.Optional[PartnerEndCustomerTechnicalContact] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PartnerCustomerCreateResponse:
        """
        The `/partner/customer/create` endpoint is used by reseller partners to create end customers.

        Parameters
        ----------
        address : PartnerEndCustomerAddress

        application_name : str
            The name of the end customer's application. This will be shown to end users when they go through the Plaid Link flow.

        company_name : str
            The company name of the end customer being created. This will be used to display the end customer in the Plaid Dashboard. It will not be shown to end users.

        is_bank_addendum_completed : bool
            Denotes whether the partner has forwarded the Plaid bank addendum to the end customer.

        is_diligence_attested : bool
            Denotes whether or not the partner has completed attestation of diligence for the end customer to be created.

        legal_entity_name : str
            The end customer's legal name. This will be shared with financial institutions as part of the OAuth registration process. It will not be shown to end users.

        products : typing.Sequence[Products]
            The products to be enabled for the end customer.

        website : str
            The end customer's website.

        assets_under_management : typing.Optional[PartnerEndCustomerAssetsUnderManagement]

        billing_contact : typing.Optional[PartnerEndCustomerBillingContact]

        client_id : typing.Optional[ApiClientId]

        create_link_customization : typing.Optional[bool]
            If `true`, the end customer's default Link customization will be set to match the partner's. You can always change the end customer's Link customization in the Plaid Dashboard. See the [Link Customization docs](https://plaid.com/docs/link/customization/) for more information.

        customer_support_info : typing.Optional[PartnerEndCustomerCustomerSupportInfo]

        logo : typing.Optional[str]
            Base64-encoded representation of the end customer's logo. Must be a PNG of size 1024x1024 under 4MB. The logo will be shared with financial institutions and shown to the end user during Link flows. A logo is required if `create_link_customization` is `true`. If `create_link_customization` is `false` and the logo is omitted, a stock logo will be used.

        redirect_uris : typing.Optional[typing.Sequence[str]]
            A list of URIs indicating the destination(s) where a user can be forwarded after completing the Link flow; used to support OAuth authentication flows when launching Link in the browser or via a webview. URIs should not contain any query parameters. When used in Production or Development, URIs must use https. To specify any subdomain, use `*` as a wildcard character, e.g. `https://*.example.com/oauth.html`. To modify redirect URIs for an end customer after creating them, go to the end customer's [API page](https://dashboard.plaid.com/team/api) in the Dashboard.

        secret : typing.Optional[ApiSecret]

        technical_contact : typing.Optional[PartnerEndCustomerTechnicalContact]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PartnerCustomerCreateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            PartnerEndCustomerAddress,
            PartnerEndCustomerBillingContact,
            PartnerEndCustomerCustomerSupportInfo,
            PartnerEndCustomerTechnicalContact,
        )

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.partner_customer_create(
                address=PartnerEndCustomerAddress(
                    city="New York",
                    country_code="US",
                    postal_code="12345",
                    region="NY",
                    street="123 Main St",
                ),
                application_name="Plaid",
                billing_contact=PartnerEndCustomerBillingContact(
                    email="bob.jones@example.com",
                    family_name="Jones",
                    given_name="Bob",
                ),
                client_id="7f57eb3d2a9j6480121fx361",
                company_name="Plaid",
                create_link_customization=True,
                customer_support_info=PartnerEndCustomerCustomerSupportInfo(
                    contact_url="example.com/contact",
                    email="support@example.com",
                    link_update_url="example.com/update",
                    phone_number="1234567890",
                ),
                is_bank_addendum_completed=True,
                is_diligence_attested=True,
                legal_entity_name="Plaid",
                products=["auth", "identity"],
                redirect_uris=[
                    "http://localhost/oauth.html",
                    "https://www.example.com/oauth.html",
                    "https://*.example.com/oauth.html",
                ],
                secret="79g03eoofwl8240v776r2h667442119",
                technical_contact=PartnerEndCustomerTechnicalContact(
                    email="alice.smith@example.com",
                    family_name="Smith",
                    given_name="Alice",
                ),
                website="plaid.com",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.partner_customer_create(
            address=address,
            application_name=application_name,
            company_name=company_name,
            is_bank_addendum_completed=is_bank_addendum_completed,
            is_diligence_attested=is_diligence_attested,
            legal_entity_name=legal_entity_name,
            products=products,
            website=website,
            assets_under_management=assets_under_management,
            billing_contact=billing_contact,
            client_id=client_id,
            create_link_customization=create_link_customization,
            customer_support_info=customer_support_info,
            logo=logo,
            redirect_uris=redirect_uris,
            secret=secret,
            technical_contact=technical_contact,
            request_options=request_options,
        )
        return _response.data

    async def partner_customer_enable(
        self,
        *,
        end_customer_client_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PartnerCustomerEnableResponse:
        """
        The `/partner/customer/enable` endpoint is used by reseller partners to enable an end customer in the Production environment.

        Parameters
        ----------
        end_customer_client_id : str

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PartnerCustomerEnableResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.partner_customer_enable(
                client_id="7f57eb3d2a9j6480121fx361",
                end_customer_client_id="7f57eb3d2a9j6480121fx361",
                secret="79g03eoofwl8240v776r2h667442119",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.partner_customer_enable(
            end_customer_client_id=end_customer_client_id,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def partner_customer_get(
        self,
        *,
        end_customer_client_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PartnerCustomerGetResponse:
        """
        The `/partner/customer/get` endpoint is used by reseller partners to retrieve data about a single end customer.

        Parameters
        ----------
        end_customer_client_id : str

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PartnerCustomerGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.partner_customer_get(
                client_id="7f57eb3d2a9j6480121fx361",
                end_customer_client_id="7f57eb3d2a9j6480121fx361",
                secret="79g03eoofwl8240v776r2h667442119",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.partner_customer_get(
            end_customer_client_id=end_customer_client_id,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def partner_customer_oauth_institutions_get(
        self,
        *,
        end_customer_client_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PartnerCustomerOAuthInstitutionsGetResponse:
        """
        The `/partner/customer/oauth_institutions/get` endpoint is used by reseller partners to retrieve OAuth-institution registration information about a single end customer. To learn how to set up a webhook to listen to status update events, visit the [reseller documentation](https://plaid.com/docs/account/resellers/#enabling-end-customers).

        Parameters
        ----------
        end_customer_client_id : str

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PartnerCustomerOAuthInstitutionsGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.partner_customer_oauth_institutions_get(
                client_id="7f57eb3d2a9j6480121fx361",
                end_customer_client_id="7f57eb3d2a9j6480121fx361",
                secret="79g03eoofwl8240v776r2h667442119",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.partner_customer_oauth_institutions_get(
            end_customer_client_id=end_customer_client_id,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def partner_customer_remove(
        self,
        *,
        end_customer_client_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PartnerCustomerRemoveResponse:
        """
        The `/partner/customer/remove` endpoint is used by reseller partners to remove an end customer. Removing an end customer will remove it from view in the Plaid Dashboard and deactivate its API keys. This endpoint can only be used to remove an end customer that has not yet been enabled in Production.

        Parameters
        ----------
        end_customer_client_id : str

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PartnerCustomerRemoveResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.partner_customer_remove(
                client_id="7f57eb3d2a9j6480121fx361",
                end_customer_client_id="7f57eb3d2a9j6480121fx361",
                secret="79g03eoofwl8240v776r2h667442119",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.partner_customer_remove(
            end_customer_client_id=end_customer_client_id,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def payment_initiation_consent_create(
        self,
        *,
        constraints: PaymentInitiationConsentConstraints,
        recipient_id: str,
        reference: str,
        scopes: typing.Sequence[PaymentInitiationConsentScope],
        client_id: typing.Optional[ApiClientId] = OMIT,
        options: typing.Optional[ExternalPaymentInitiationConsentOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentInitiationConsentCreateResponse:
        """
        The `/payment_initiation/consent/create` endpoint is used to create a payment consent, which can be used to initiate payments on behalf of the user. Payment consents are created with `UNAUTHORISED` status by default and must be authorised by the user before payments can be initiated.

        Consents can be limited in time and scope, and have constraints that describe limitations for payments.

        Parameters
        ----------
        constraints : PaymentInitiationConsentConstraints

        recipient_id : str
            The ID of the recipient the payment consent is for. The created consent can be used to transfer funds to this recipient only.

        reference : str
            A reference for the payment consent. This must be an alphanumeric string with at most 18 characters and must not contain any special characters.

        scopes : typing.Sequence[PaymentInitiationConsentScope]
            An array of payment consent scopes.

        client_id : typing.Optional[ApiClientId]

        options : typing.Optional[ExternalPaymentInitiationConsentOptions]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentInitiationConsentCreateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            PaymentAmount,
            PaymentConsentPeriodicAmount,
            PaymentInitiationConsentConstraints,
        )

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.payment_initiation_consent_create(
                constraints=PaymentInitiationConsentConstraints(
                    max_payment_amount=PaymentAmount(
                        currency="GBP",
                        value=1.1,
                    ),
                    periodic_amounts=[
                        PaymentConsentPeriodicAmount(
                            alignment="CALENDAR",
                            amount=PaymentAmount(
                                currency="GBP",
                                value=1.1,
                            ),
                            interval="DAY",
                        )
                    ],
                ),
                recipient_id="recipient_id",
                reference="reference",
                scopes=["ME_TO_ME"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.payment_initiation_consent_create(
            constraints=constraints,
            recipient_id=recipient_id,
            reference=reference,
            scopes=scopes,
            client_id=client_id,
            options=options,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def payment_initiation_consent_get(
        self,
        *,
        consent_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentInitiationConsentGetResponse:
        """
        The `/payment_initiation/consent/get` endpoint can be used to check the status of a payment consent, as well as to receive basic information such as recipient and constraints.

        Parameters
        ----------
        consent_id : str
            The `consent_id` returned from `/payment_initiation/consent/create`.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentInitiationConsentGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.payment_initiation_consent_get(
                consent_id="consent_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.payment_initiation_consent_get(
            consent_id=consent_id, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def payment_initiation_consent_payment_execute(
        self,
        *,
        amount: PaymentAmount,
        consent_id: str,
        idempotency_key: ConsentPaymentIdempotencyKey,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentInitiationConsentPaymentExecuteResponse:
        """
        The `/payment_initiation/consent/payment/execute` endpoint can be used to execute payments using payment consent.

        Parameters
        ----------
        amount : PaymentAmount

        consent_id : str
            The consent ID.

        idempotency_key : ConsentPaymentIdempotencyKey

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentInitiationConsentPaymentExecuteResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, PaymentAmount

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.payment_initiation_consent_payment_execute(
                amount=PaymentAmount(
                    currency="GBP",
                    value=1.1,
                ),
                consent_id="consent_id",
                idempotency_key="idempotency_key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.payment_initiation_consent_payment_execute(
            amount=amount,
            consent_id=consent_id,
            idempotency_key=idempotency_key,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def payment_initiation_consent_revoke(
        self,
        *,
        consent_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentInitiationConsentRevokeResponse:
        """
        The `/payment_initiation/consent/revoke` endpoint can be used to revoke the payment consent. Once the consent is revoked, it is not possible to initiate payments using it.

        Parameters
        ----------
        consent_id : str
            The consent ID.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentInitiationConsentRevokeResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.payment_initiation_consent_revoke(
                consent_id="consent_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.payment_initiation_consent_revoke(
            consent_id=consent_id, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def payment_initiation_payment_create(
        self,
        *,
        amount: PaymentAmount,
        recipient_id: str,
        reference: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        options: typing.Optional[ExternalPaymentOptions] = OMIT,
        schedule: typing.Optional[ExternalPaymentScheduleRequest] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentInitiationPaymentCreateResponse:
        """
        After creating a payment recipient, you can use the `/payment_initiation/payment/create` endpoint to create a payment to that recipient.  Payments can be one-time or standing order (recurring) and can be denominated in either EUR, GBP or other chosen [currency](https://plaid.com/docs/api/products/payment-initiation/#payment_initiation-payment-create-request-amount-currency).  If making domestic GBP-denominated payments, your recipient must have been created with BACS numbers. In general, EUR-denominated payments will be sent via SEPA Credit Transfer, GBP-denominated payments will be sent via the Faster Payments network and for non-Eurozone markets typically via the local payment scheme, but the payment network used will be determined by the institution. Payments sent via Faster Payments will typically arrive immediately, while payments sent via SEPA Credit Transfer or other local payment schemes will typically arrive in one business day.

        Standing orders (recurring payments) must be denominated in GBP and can only be sent to recipients in the UK. Once created, standing order payments cannot be modified or canceled via the API. An end user can cancel or modify a standing order directly on their banking application or website, or by contacting the bank. Standing orders will follow the payment rules of the underlying rails (Faster Payments in UK). Payments can be sent Monday to Friday, excluding bank holidays. If the pre-arranged date falls on a weekend or bank holiday, the payment is made on the next working day. It is not possible to guarantee the exact time the payment will reach the recipient’s account, although at least 90% of standing order payments are sent by 6am.

        In the Development environment, payments must be below 5 GBP or other chosen [currency](https://plaid.com/docs/api/products/payment-initiation/#payment_initiation-payment-create-request-amount-currency). For details on any payment limits in Production, contact your Plaid Account Manager.

        Parameters
        ----------
        amount : PaymentAmount

        recipient_id : str
            The ID of the recipient the payment is for.

        reference : str
            A reference for the payment. This must be an alphanumeric string with at most 18 characters and must not contain any special characters (since not all institutions support them).
            In order to track settlement via Payment Confirmation, each payment must have a unique reference. If the reference provided through the API is not unique, Plaid will adjust it.
            Both the originally provided and automatically adjusted references (if any) can be found in the `reference` and `adjusted_reference` fields, respectively.

        client_id : typing.Optional[ApiClientId]

        options : typing.Optional[ExternalPaymentOptions]

        schedule : typing.Optional[ExternalPaymentScheduleRequest]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentInitiationPaymentCreateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, PaymentAmount

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.payment_initiation_payment_create(
                amount=PaymentAmount(
                    currency="GBP",
                    value=1.1,
                ),
                recipient_id="recipient_id",
                reference="reference",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.payment_initiation_payment_create(
            amount=amount,
            recipient_id=recipient_id,
            reference=reference,
            client_id=client_id,
            options=options,
            schedule=schedule,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def payment_initiation_payment_get(
        self,
        *,
        payment_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentInitiationPaymentGetResponse:
        """
        The `/payment_initiation/payment/get` endpoint can be used to check the status of a payment, as well as to receive basic information such as recipient and payment amount. In the case of standing orders, the `/payment_initiation/payment/get` endpoint will provide information about the status of the overall standing order itself; the API cannot be used to retrieve payment status for individual payments within a standing order.

        Parameters
        ----------
        payment_id : str
            The `payment_id` returned from `/payment_initiation/payment/create`.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentInitiationPaymentGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.payment_initiation_payment_get(
                payment_id="payment_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.payment_initiation_payment_get(
            payment_id=payment_id, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def payment_initiation_payment_list(
        self,
        *,
        client_id: typing.Optional[ApiClientId] = OMIT,
        consent_id: typing.Optional[str] = OMIT,
        count: typing.Optional[int] = OMIT,
        cursor: typing.Optional[dt.datetime] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentInitiationPaymentListResponse:
        """
        The `/payment_initiation/payment/list` endpoint can be used to retrieve all created payments. By default, the 10 most recent payments are returned. You can request more payments and paginate through the results using the optional `count` and `cursor` parameters.

        Parameters
        ----------
        client_id : typing.Optional[ApiClientId]

        consent_id : typing.Optional[str]
            The consent ID. If specified, only payments, executed using this consent, will be returned.

        count : typing.Optional[int]
            The maximum number of payments to return. If `count` is not specified, a maximum of 10 payments will be returned, beginning with the most recent payment before the cursor (if specified).

        cursor : typing.Optional[dt.datetime]
            A string in RFC 3339 format (i.e. "2019-12-06T22:35:49Z"). Only payments created before the cursor will be returned.

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentInitiationPaymentListResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.payment_initiation_payment_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.payment_initiation_payment_list(
            client_id=client_id,
            consent_id=consent_id,
            count=count,
            cursor=cursor,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def payment_initiation_payment_reverse(
        self,
        *,
        idempotency_key: WalletTransactionIdempotencyKey,
        payment_id: str,
        reference: str,
        amount: typing.Optional[PaymentAmountToRefund] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentInitiationPaymentReverseResponse:
        """
        Reverse a settled payment from a Plaid virtual account.

        The original payment must be in a settled state to be refunded.
        To refund partially, specify the amount as part of the request.
        If the amount is not specified, the refund amount will be equal to all
        of the remaining payment amount that has not been refunded yet.

        The refund will go back to the source account that initiated the payment.
        The original payment must have been initiated to a Plaid virtual account
        so that this account can be used to initiate the refund.

        Parameters
        ----------
        idempotency_key : WalletTransactionIdempotencyKey

        payment_id : str
            The ID of the payment to reverse

        reference : str
            A reference for the refund. This must be an alphanumeric string with 6 to 18 characters and must not contain any special characters or spaces.

        amount : typing.Optional[PaymentAmountToRefund]

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentInitiationPaymentReverseResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.payment_initiation_payment_reverse(
                idempotency_key="idempotency_key",
                payment_id="payment_id",
                reference="reference",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.payment_initiation_payment_reverse(
            idempotency_key=idempotency_key,
            payment_id=payment_id,
            reference=reference,
            amount=amount,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def create_payment_token(
        self,
        *,
        payment_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentInitiationPaymentTokenCreateResponse:
        """
        The `/payment_initiation/payment/token/create` endpoint has been deprecated. New Plaid customers will be unable to use this endpoint, and existing customers are encouraged to migrate to the newer, `link_token`-based flow. The recommended flow is to provide the `payment_id` to `/link/token/create`, which returns a `link_token` used to initialize Link.

        The `/payment_initiation/payment/token/create` is used to create a `payment_token`, which can then be used in Link initialization to enter a payment initiation flow. You can only use a `payment_token` once. If this attempt fails, the end user aborts the flow, or the token expires, you will need to create a new payment token. Creating a new payment token does not require end user input.

        Parameters
        ----------
        payment_id : str
            The `payment_id` returned from `/payment_initiation/payment/create`.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentInitiationPaymentTokenCreateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.create_payment_token(
                payment_id="payment_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_payment_token(
            payment_id=payment_id, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def payment_initiation_recipient_create(
        self,
        *,
        name: str,
        address: typing.Optional[PaymentInitiationAddress] = OMIT,
        bacs: typing.Optional[RecipientBacsNullable] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        iban: typing.Optional[str] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentInitiationRecipientCreateResponse:
        """
        Create a payment recipient for payment initiation.  The recipient must be in Europe, within a country that is a member of the Single Euro Payment Area (SEPA) or a non-Eurozone country [supported](https://plaid.com/global) by Plaid. For a standing order (recurring) payment, the recipient must be in the UK.

        It is recommended to use `bacs` in the UK and `iban` in EU.

        The endpoint is idempotent: if a developer has already made a request with the same payment details, Plaid will return the same `recipient_id`.

        Parameters
        ----------
        name : str
            The name of the recipient. We recommend using strings of length 18 or less and avoid special characters to ensure compatibility with all institutions.

        address : typing.Optional[PaymentInitiationAddress]

        bacs : typing.Optional[RecipientBacsNullable]

        client_id : typing.Optional[ApiClientId]

        iban : typing.Optional[str]
            The International Bank Account Number (IBAN) for the recipient. If BACS data is not provided, an IBAN is required.

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentInitiationRecipientCreateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.payment_initiation_recipient_create(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.payment_initiation_recipient_create(
            name=name,
            address=address,
            bacs=bacs,
            client_id=client_id,
            iban=iban,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def payment_initiation_recipient_get(
        self,
        *,
        recipient_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentInitiationRecipientGetResponse:
        """
        Get details about a payment recipient you have previously created.

        Parameters
        ----------
        recipient_id : str
            The ID of the recipient

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentInitiationRecipientGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.payment_initiation_recipient_get(
                recipient_id="recipient_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.payment_initiation_recipient_get(
            recipient_id=recipient_id, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def payment_initiation_recipient_list(
        self,
        *,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentInitiationRecipientListResponse:
        """
        The `/payment_initiation/recipient/list` endpoint list the payment recipients that you have previously created.

        Parameters
        ----------
        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentInitiationRecipientListResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.payment_initiation_recipient_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.payment_initiation_recipient_list(
            client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def payment_profile_create(
        self,
        *,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentProfileCreateResponse:
        """
        Use `/payment_profile/create` endpoint to create a new payment profile.
        To initiate the account linking experience, call `/link/token/create` and provide the `payment_profile_token` in the `transfer.payment_profile_token` field.
        You can then use the `payment_profile_token` when creating transfers using `/transfer/authorization/create` and `/transfer/create`.

        Parameters
        ----------
        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentProfileCreateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.payment_profile_create()


        asyncio.run(main())
        """
        _response = await self._raw_client.payment_profile_create(
            client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def payment_profile_get(
        self,
        *,
        payment_profile_token: PaymentProfileToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentProfileGetResponse:
        """
        Use `/payment_profile/get` endpoint to get the status of a given Payment Profile.

        Parameters
        ----------
        payment_profile_token : PaymentProfileToken

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentProfileGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.payment_profile_get(
                payment_profile_token="payment_profile_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.payment_profile_get(
            payment_profile_token=payment_profile_token,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def payment_profile_remove(
        self,
        *,
        payment_profile_token: PaymentProfileToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentProfileRemoveResponse:
        """
        Use the `/payment_profile/remove` endpoint to remove a given Payment Profile. Once it’s removed, it can no longer be used to create transfers.

        Parameters
        ----------
        payment_profile_token : PaymentProfileToken

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentProfileRemoveResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.payment_profile_remove(
                payment_profile_token="payment_profile_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.payment_profile_remove(
            payment_profile_token=payment_profile_token,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def processor_apex_processor_token_create(
        self,
        *,
        access_token: AccessToken,
        account_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProcessorTokenCreateResponse:
        """
        Used to create a token suitable for sending to Apex to enable Plaid-Apex integrations.

        Parameters
        ----------
        access_token : AccessToken

        account_id : str
            The `account_id` value obtained from the `onSuccess` callback in Link

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProcessorTokenCreateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.processor_apex_processor_token_create(
                access_token="access_token",
                account_id="account_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.processor_apex_processor_token_create(
            access_token=access_token,
            account_id=account_id,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def processor_auth_get(
        self,
        *,
        processor_token: ProcessorToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProcessorAuthGetResponse:
        """
        The `/processor/auth/get` endpoint returns the bank account and bank identification number (such as the routing number, for US accounts), for a checking or savings account that''s associated with a given `processor_token`. The endpoint also returns high-level account data and balances when available.

        Versioning note: API versions 2019-05-29 and earlier use a different schema for the `numbers` object returned by this endpoint. For details, see [Plaid API versioning](https://plaid.com/docs/api/versioning/#version-2020-09-14).

        Parameters
        ----------
        processor_token : ProcessorToken

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProcessorAuthGetResponse
            success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.processor_auth_get(
                processor_token="processor_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.processor_auth_get(
            processor_token=processor_token, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def processor_balance_get(
        self,
        *,
        processor_token: ProcessorToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        options: typing.Optional[ProcessorBalanceGetRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProcessorBalanceGetResponse:
        """
        The `/processor/balance/get` endpoint returns the real-time balance for each of an Item's accounts. While other endpoints may return a balance object, only `/processor/balance/get` forces the available and current balance fields to be refreshed rather than cached.

        Parameters
        ----------
        processor_token : ProcessorToken

        client_id : typing.Optional[ApiClientId]

        options : typing.Optional[ProcessorBalanceGetRequestOptions]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProcessorBalanceGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.processor_balance_get(
                processor_token="processor_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.processor_balance_get(
            processor_token=processor_token,
            client_id=client_id,
            options=options,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def processor_bank_transfer_create(
        self,
        *,
        amount: BankTransferAmount,
        description: str,
        idempotency_key: BankTransferIdempotencyKey,
        iso_currency_code: str,
        network: BankTransferNetwork,
        processor_token: ProcessorToken,
        type: BankTransferType,
        user: BankTransferUser,
        ach_class: typing.Optional[AchClass] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        custom_tag: typing.Optional[str] = OMIT,
        metadata: typing.Optional[BankTransferMetadata] = OMIT,
        origination_account_id: typing.Optional[str] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProcessorBankTransferCreateResponse:
        """
        Use the `/processor/bank_transfer/create` endpoint to initiate a new bank transfer as a processor

        Parameters
        ----------
        amount : BankTransferAmount

        description : str
            The transfer description. Maximum of 10 characters.

        idempotency_key : BankTransferIdempotencyKey

        iso_currency_code : str
            The currency of the transfer amount – should be set to "USD".

        network : BankTransferNetwork

        processor_token : ProcessorToken

        type : BankTransferType

        user : BankTransferUser

        ach_class : typing.Optional[AchClass]

        client_id : typing.Optional[ApiClientId]

        custom_tag : typing.Optional[str]
            An arbitrary string provided by the client for storage with the bank transfer. May be up to 100 characters.

        metadata : typing.Optional[BankTransferMetadata]

        origination_account_id : typing.Optional[str]
            Plaid’s unique identifier for the origination account for this transfer. If you have more than one origination account, this value must be specified.

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProcessorBankTransferCreateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, BankTransferUser

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.processor_bank_transfer_create(
                amount="amount",
                description="description",
                idempotency_key="idempotency_key",
                iso_currency_code="iso_currency_code",
                network="ach",
                processor_token="processor_token",
                type="debit",
                user=BankTransferUser(
                    legal_name="legal_name",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.processor_bank_transfer_create(
            amount=amount,
            description=description,
            idempotency_key=idempotency_key,
            iso_currency_code=iso_currency_code,
            network=network,
            processor_token=processor_token,
            type=type,
            user=user,
            ach_class=ach_class,
            client_id=client_id,
            custom_tag=custom_tag,
            metadata=metadata,
            origination_account_id=origination_account_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def processor_identity_get(
        self,
        *,
        processor_token: ProcessorToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProcessorIdentityGetResponse:
        """
        The `/processor/identity/get` endpoint allows you to retrieve various account holder information on file with the financial institution, including names, emails, phone numbers, and addresses.

        Parameters
        ----------
        processor_token : ProcessorToken

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProcessorIdentityGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.processor_identity_get(
                processor_token="processor_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.processor_identity_get(
            processor_token=processor_token, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def processor_signal_decision_report(
        self,
        *,
        client_transaction_id: str,
        initiated: bool,
        processor_token: ProcessorToken,
        amount_instantly_available: typing.Optional[float] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        days_funds_on_hold: typing.Optional[int] = OMIT,
        decision_outcome: typing.Optional[SignalDecisionOutcome] = OMIT,
        payment_method: typing.Optional[SignalPaymentMethod] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProcessorSignalDecisionReportResponse:
        """
        After calling `/processor/signal/evaluate`, call `/processor/signal/decision/report` to report whether the transaction was initiated. This endpoint will return an [`INVALID_FIELD`](/docs/errors/invalid-request/#invalid_field) error if called a second time with a different value for `initiated`.

        Parameters
        ----------
        client_transaction_id : str
            Must be the same as the `client_transaction_id` supplied when calling `/signal/evaluate`

        initiated : bool
            `true` if the ACH transaction was initiated, `false` otherwise.

            This field must be returned as a boolean. If formatted incorrectly, this will result in an [`INVALID_FIELD`](/docs/errors/invalid-request/#invalid_field) error.

        processor_token : ProcessorToken

        amount_instantly_available : typing.Optional[float]
            The amount (in USD) made available to your customers instantly following the debit transaction. It could be a partial amount of the requested transaction (example: 102.05).

        client_id : typing.Optional[ApiClientId]

        days_funds_on_hold : typing.Optional[int]
            The actual number of days (hold time) since the ACH debit transaction that you wait before making funds available to your customers. The holding time could affect the ACH return rate.

            For example, use 0 if you make funds available to your customers instantly or the same day following the debit transaction, or 1 if you make funds available the next day following the debit initialization.

        decision_outcome : typing.Optional[SignalDecisionOutcome]

        payment_method : typing.Optional[SignalPaymentMethod]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProcessorSignalDecisionReportResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.processor_signal_decision_report(
                client_transaction_id="client_transaction_id",
                initiated=True,
                processor_token="processor_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.processor_signal_decision_report(
            client_transaction_id=client_transaction_id,
            initiated=initiated,
            processor_token=processor_token,
            amount_instantly_available=amount_instantly_available,
            client_id=client_id,
            days_funds_on_hold=days_funds_on_hold,
            decision_outcome=decision_outcome,
            payment_method=payment_method,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def processor_signal_evaluate(
        self,
        *,
        amount: float,
        client_transaction_id: str,
        processor_token: ProcessorToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        client_user_id: typing.Optional[str] = OMIT,
        default_payment_method: typing.Optional[str] = OMIT,
        device: typing.Optional[SignalDevice] = OMIT,
        is_recurring: typing.Optional[bool] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        user: typing.Optional[SignalUser] = OMIT,
        user_present: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProcessorSignalEvaluateResponse:
        """
        Use `/processor/signal/evaluate` to evaluate a planned ACH transaction as a processor to get a return risk assessment (such as a risk score and risk tier) and additional risk signals.

        In order to obtain a valid score for an ACH transaction, Plaid must have an access token for the account, and the Item must be healthy (receiving product updates) or have recently been in a healthy state. If the transaction does not meet eligibility requirements, an error will be returned corresponding to the underlying cause. If `/processor/signal/evaluate` is called on the same transaction multiple times within a 24-hour period, cached results may be returned. For more information please refer to our error documentation on [item errors](/docs/errors/item/) and [Link in Update Mode](/docs/link/update-mode/).

        Note: This request may take some time to complete if Signal is being added to an existing Item. This is because Plaid must communicate directly with the institution when retrieving the data for the first time.

        Parameters
        ----------
        amount : float
            The transaction amount, in USD (e.g. `102.05`)

        client_transaction_id : str
            The unique ID that you would like to use to refer to this transaction. For your convenience mapping your internal data, you could use your internal ID/identifier for this transaction. The max length for this field is 36 characters.

        processor_token : ProcessorToken

        client_id : typing.Optional[ApiClientId]

        client_user_id : typing.Optional[str]
            A unique ID that identifies the end user in your system. This ID is used to correlate requests by a user with multiple Items. The max length for this field is 36 characters. Personally identifiable information, such as an email address or phone number, should not be used in the `client_user_id`.

        default_payment_method : typing.Optional[str]
            The default ACH or non-ACH payment method to complete the transaction.
            `SAME_DAY_ACH`: Same Day ACH by NACHA. The debit transaction is processed and settled on the same day
            `NEXT_DAY_ACH`: Next Day ACH settlement for debit transactions, offered by some payment processors
            `STANDARD_ACH`: standard ACH by NACHA
            `REAL_TIME_PAYMENTS`: real-time payments such as RTP and FedNow
            `DEBIT_CARD`: if the default payment is over debit card networks
            `MULTIPLE_PAYMENT_METHODS`: if there is no default debit rail or there are multiple payment methods
            Possible values:  `SAME_DAY_ACH`, `NEXT_DAY_ACH`, `STANDARD_ACH`, `REAL_TIME_PAYMENTS`, `DEBIT_CARD`, `MULTIPLE_PAYMENT_METHODS`

        device : typing.Optional[SignalDevice]

        is_recurring : typing.Optional[bool]
            **true** if the ACH transaction is a recurring transaction; **false** otherwise

        secret : typing.Optional[ApiSecret]

        user : typing.Optional[SignalUser]

        user_present : typing.Optional[bool]
            `true` if the end user is present while initiating the ACH transfer and the endpoint is being called; `false` otherwise (for example, when the ACH transfer is scheduled and the end user is not present, or you call this endpoint after the ACH transfer but before submitting the Nacha file for ACH processing).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProcessorSignalEvaluateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.processor_signal_evaluate(
                amount=1.1,
                client_transaction_id="client_transaction_id",
                processor_token="processor_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.processor_signal_evaluate(
            amount=amount,
            client_transaction_id=client_transaction_id,
            processor_token=processor_token,
            client_id=client_id,
            client_user_id=client_user_id,
            default_payment_method=default_payment_method,
            device=device,
            is_recurring=is_recurring,
            secret=secret,
            user=user,
            user_present=user_present,
            request_options=request_options,
        )
        return _response.data

    async def processor_signal_return_report(
        self,
        *,
        client_transaction_id: str,
        processor_token: ProcessorToken,
        return_code: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        returned_at: typing.Optional[dt.datetime] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProcessorSignalReturnReportResponse:
        """
        Call the `/processor/signal/return/report` endpoint to report a returned transaction that was previously sent to the `/processor/signal/evaluate` endpoint. Your feedback will be used by the model to incorporate the latest risk trend in your portfolio.

        Parameters
        ----------
        client_transaction_id : str
            Must be the same as the `client_transaction_id` supplied when calling `/processor/signal/evaluate`

        processor_token : ProcessorToken

        return_code : str
            Must be a valid ACH return code (e.g. "R01")

            If formatted incorrectly, this will result in an [`INVALID_FIELD`](/docs/errors/invalid-request/#invalid_field) error.

        client_id : typing.Optional[ApiClientId]

        returned_at : typing.Optional[dt.datetime]
            Date and time when you receive the returns from your payment processors, in ISO 8601 format (`YYYY-MM-DDTHH:mm:ssZ`).

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProcessorSignalReturnReportResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.processor_signal_return_report(
                client_transaction_id="client_transaction_id",
                processor_token="processor_token",
                return_code="return_code",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.processor_signal_return_report(
            client_transaction_id=client_transaction_id,
            processor_token=processor_token,
            return_code=return_code,
            client_id=client_id,
            returned_at=returned_at,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def processor_stripe_bank_account_token_create(
        self,
        *,
        access_token: AccessToken,
        account_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProcessorStripeBankAccountTokenCreateResponse:
        """

        Used to create a token suitable for sending to Stripe to enable Plaid-Stripe integrations. For a detailed guide on integrating Stripe, see [Add Stripe to your app](https://plaid.com/docs/auth/partnerships/stripe/).

        Note that the Stripe bank account token is a one-time use token. To store bank account information for later use, you can use a Stripe customer object and create an associated bank account from the token, or you can use a Stripe Custom account and create an associated external bank account from the token. This bank account information should work indefinitely, unless the user's bank account information changes or they revoke Plaid's permissions to access their account. Stripe bank account information cannot be modified once the bank account token has been created. If you ever need to change the bank account details used by Stripe for a specific customer, have the user go through Link again and create a new bank account token from the new `access_token`.

        Bank account tokens can also be revoked, using `/item/remove`.'

        Parameters
        ----------
        access_token : AccessToken

        account_id : str
            The `account_id` value obtained from the `onSuccess` callback in Link

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProcessorStripeBankAccountTokenCreateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.processor_stripe_bank_account_token_create(
                access_token="access_token",
                account_id="account_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.processor_stripe_bank_account_token_create(
            access_token=access_token,
            account_id=account_id,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def processor_token_create(
        self,
        *,
        access_token: AccessToken,
        account_id: str,
        processor: ProcessorTokenCreateRequestProcessor,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProcessorTokenCreateResponse:
        """
        Used to create a token suitable for sending to one of Plaid's partners to enable integrations. Note that Stripe partnerships use bank account tokens instead; see `/processor/stripe/bank_account_token/create` for creating tokens for use with Stripe integrations. Once created, a processor token for a given Item cannot be modified or updated. If the account must be linked to a new or different partner resource, create a new Item by having the user go through the Link flow again; a new processor token can then be created from the new `access_token`. Processor tokens can also be revoked, using `/item/remove`.

        Parameters
        ----------
        access_token : AccessToken

        account_id : str
            The `account_id` value obtained from the `onSuccess` callback in Link

        processor : ProcessorTokenCreateRequestProcessor
            The processor you are integrating with.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProcessorTokenCreateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.processor_token_create(
                access_token="access_token",
                account_id="account_id",
                processor="dwolla",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.processor_token_create(
            access_token=access_token,
            account_id=account_id,
            processor=processor,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def sandbox_bank_transfer_fire_webhook(
        self,
        *,
        webhook: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SandboxBankTransferFireWebhookResponse:
        """
        Use the `/sandbox/bank_transfer/fire_webhook` endpoint to manually trigger a Bank Transfers webhook in the Sandbox environment.

        Parameters
        ----------
        webhook : str
            The URL to which the webhook should be sent.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SandboxBankTransferFireWebhookResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.sandbox_bank_transfer_fire_webhook(
                webhook="webhook",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.sandbox_bank_transfer_fire_webhook(
            webhook=webhook, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def sandbox_bank_transfer_simulate(
        self,
        *,
        bank_transfer_id: BankTransferId,
        event_type: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        failure_reason: typing.Optional[BankTransferFailure] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SandboxBankTransferSimulateResponse:
        """
        Use the `/sandbox/bank_transfer/simulate` endpoint to simulate a bank transfer event in the Sandbox environment.  Note that while an event will be simulated and will appear when using endpoints such as `/bank_transfer/event/sync` or `/bank_transfer/event/list`, no transactions will actually take place and funds will not move between accounts, even within the Sandbox.

        Parameters
        ----------
        bank_transfer_id : BankTransferId

        event_type : str
            The asynchronous event to be simulated. May be: `posted`, `failed`, or `reversed`.

            An error will be returned if the event type is incompatible with the current transfer status. Compatible status --> event type transitions include:

            `pending` --> `failed`

            `pending` --> `posted`

            `posted` --> `reversed`

        client_id : typing.Optional[ApiClientId]

        failure_reason : typing.Optional[BankTransferFailure]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SandboxBankTransferSimulateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.sandbox_bank_transfer_simulate(
                bank_transfer_id="bank_transfer_id",
                event_type="event_type",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.sandbox_bank_transfer_simulate(
            bank_transfer_id=bank_transfer_id,
            event_type=event_type,
            client_id=client_id,
            failure_reason=failure_reason,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def sandbox_income_fire_webhook(
        self,
        *,
        item_id: str,
        verification_status: SandboxIncomeFireWebhookRequestVerificationStatus,
        webhook: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        user_id: typing.Optional[UserId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SandboxIncomeFireWebhookResponse:
        """
        Use the `/sandbox/income/fire_webhook` endpoint to manually trigger an Income webhook in the Sandbox environment.

        Parameters
        ----------
        item_id : str
            The Item ID associated with the verification.

        verification_status : SandboxIncomeFireWebhookRequestVerificationStatus
            `VERIFICATION_STATUS_PROCESSING_COMPLETE`: The income verification status processing has completed. If the user uploaded multiple documents, this webhook will fire when all documents have finished processing. Call the `/income/verification/paystubs/get` endpoint and check the document metadata to see which documents were successfully parsed.

            `VERIFICATION_STATUS_PROCESSING_FAILED`: A failure occurred when attempting to process the verification documentation.

            `VERIFICATION_STATUS_PENDING_APPROVAL`: (deprecated) The income verification has been sent to the user for review.

        webhook : str
            The URL to which the webhook should be sent.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        user_id : typing.Optional[UserId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SandboxIncomeFireWebhookResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.sandbox_income_fire_webhook(
                item_id="item_id",
                verification_status="VERIFICATION_STATUS_PROCESSING_COMPLETE",
                webhook="webhook",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.sandbox_income_fire_webhook(
            item_id=item_id,
            verification_status=verification_status,
            webhook=webhook,
            client_id=client_id,
            secret=secret,
            user_id=user_id,
            request_options=request_options,
        )
        return _response.data

    async def sandbox_item_fire_webhook(
        self,
        *,
        access_token: AccessToken,
        webhook_code: SandboxItemFireWebhookRequestWebhookCode,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        webhook_type: typing.Optional[WebhookType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SandboxItemFireWebhookResponse:
        """
        The `/sandbox/item/fire_webhook` endpoint is used to test that code correctly handles webhooks. This endpoint can trigger the following webhooks:

        `DEFAULT_UPDATE`: Transactions update webhook to be fired for a given Sandbox Item. If the Item does not support Transactions, a `SANDBOX_PRODUCT_NOT_ENABLED` error will result.

        `NEW_ACCOUNTS_AVAILABLE`: Webhook to be fired for a given Sandbox Item created with Account Select v2.

        `AUTH_DATA_UPDATE`: Webhook to be fired for a given Sandbox Item created with Auth as an enabled product.

        `RECURRING_TRANSACTIONS_UPDATE`: Recurring Transactions webhook to be fired for a given Sandbox Item. If the Item does not support Recurring Transactions, a `SANDBOX_PRODUCT_NOT_ENABLED` error will result.

        `SYNC_UPDATES_AVAILABLE`: Transactions webhook to be fired for a given Sandbox Item.  If the Item does not support Transactions, a `SANDBOX_PRODUCT_NOT_ENABLED` error will result.

        Note that this endpoint is provided for developer ease-of-use and is not required for testing webhooks; webhooks will also fire in Sandbox under the same conditions that they would in Production or Development.

        Parameters
        ----------
        access_token : AccessToken

        webhook_code : SandboxItemFireWebhookRequestWebhookCode
            The webhook codes that can be fired by this test endpoint.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        webhook_type : typing.Optional[WebhookType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SandboxItemFireWebhookResponse
            success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.sandbox_item_fire_webhook(
                access_token="access_token",
                webhook_code="DEFAULT_UPDATE",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.sandbox_item_fire_webhook(
            access_token=access_token,
            webhook_code=webhook_code,
            client_id=client_id,
            secret=secret,
            webhook_type=webhook_type,
            request_options=request_options,
        )
        return _response.data

    async def sandbox_item_reset_login(
        self,
        *,
        access_token: AccessToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SandboxItemResetLoginResponse:
        """
        `/sandbox/item/reset_login/` forces an Item into an `ITEM_LOGIN_REQUIRED` state in order to simulate an Item whose login is no longer valid. This makes it easy to test Link's [update mode](https://plaid.com/docs/link/update-mode) flow in the Sandbox environment.  After calling `/sandbox/item/reset_login`, You can then use Plaid Link update mode to restore the Item to a good state. An `ITEM_LOGIN_REQUIRED` webhook will also be fired after a call to this endpoint, if one is associated with the Item.


        In the Sandbox, Items will transition to an `ITEM_LOGIN_REQUIRED` error state automatically after 30 days, even if this endpoint is not called.

        Parameters
        ----------
        access_token : AccessToken

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SandboxItemResetLoginResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.sandbox_item_reset_login(
                access_token="access_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.sandbox_item_reset_login(
            access_token=access_token, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def sandbox_item_set_verification_status(
        self,
        *,
        access_token: AccessToken,
        account_id: str,
        verification_status: SandboxItemSetVerificationStatusRequestVerificationStatus,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SandboxItemSetVerificationStatusResponse:
        """
        The `/sandbox/item/set_verification_status` endpoint can be used to change the verification status of an Item in in the Sandbox in order to simulate the Automated Micro-deposit flow.

        Note that not all Plaid developer accounts are enabled for micro-deposit based verification by default. Your account must be enabled for this feature in order to test it in Sandbox. To enable this features or check your status, contact your account manager or [submit a product access Support ticket](https://dashboard.plaid.com/support/new/product-and-development/product-troubleshooting/request-product-access).

        For more information on testing Automated Micro-deposits in Sandbox, see [Auth full coverage testing](https://plaid.com/docs/auth/coverage/testing#).

        Parameters
        ----------
        access_token : AccessToken

        account_id : str
            The `account_id` of the account whose verification status is to be modified

        verification_status : SandboxItemSetVerificationStatusRequestVerificationStatus
            The verification status to set the account to.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SandboxItemSetVerificationStatusResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.sandbox_item_set_verification_status(
                access_token="access_token",
                account_id="account_id",
                verification_status="automatically_verified",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.sandbox_item_set_verification_status(
            access_token=access_token,
            account_id=account_id,
            verification_status=verification_status,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def sandbox_oauth_select_accounts(
        self,
        *,
        accounts: typing.Sequence[str],
        oauth_state_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SandboxOauthSelectAccountsResponse:
        """
        Save the selected accounts when connecting to the Platypus Oauth institution

        Parameters
        ----------
        accounts : typing.Sequence[str]

        oauth_state_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SandboxOauthSelectAccountsResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.sandbox_oauth_select_accounts(
                accounts=["accounts"],
                oauth_state_id="oauth_state_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.sandbox_oauth_select_accounts(
            accounts=accounts, oauth_state_id=oauth_state_id, request_options=request_options
        )
        return _response.data

    async def sandbox_payment_profile_reset_login(
        self,
        *,
        payment_profile_token: PaymentProfileToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SandboxPaymentProfileResetLoginResponse:
        """
        `/sandbox/payment_profile/reset_login/` forces a Payment Profile into a state where the login is no longer valid. This makes it easy to test update mode for Payment Profile in the Sandbox environment.

         After calling `/sandbox/payment_profile/reset_login`, calls to the `/transfer/authorization/create` with the Payment Profile will result in a `decision_rationale` `PAYMENT_PROFILE_LOGIN_REQUIRED`. You can then use update mode for Payment Profile to restore it into a good state.

         In order to invoke this endpoint, you must first [create a Payment Profile](https://plaid.com/docs/transfer/add-to-app/#create-a-payment-profile-optional) and [go through the Link flow](https://plaid.com/docs/transfer/add-to-app/#create-a-link-token).

        Parameters
        ----------
        payment_profile_token : PaymentProfileToken

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SandboxPaymentProfileResetLoginResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.sandbox_payment_profile_reset_login(
                payment_profile_token="payment_profile_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.sandbox_payment_profile_reset_login(
            payment_profile_token=payment_profile_token,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def sandbox_processor_token_create(
        self,
        *,
        institution_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        options: typing.Optional[SandboxProcessorTokenCreateRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SandboxProcessorTokenCreateResponse:
        """
        Use the `/sandbox/processor_token/create` endpoint to create a valid `processor_token` for an arbitrary institution ID and test credentials. The created `processor_token` corresponds to a new Sandbox Item. You can then use this `processor_token` with the `/processor/` API endpoints in Sandbox. You can also use `/sandbox/processor_token/create` with the [`user_custom` test username](https://plaid.com/docs/sandbox/user-custom) to generate a test account with custom data.

        Parameters
        ----------
        institution_id : str
            The ID of the institution the Item will be associated with

        client_id : typing.Optional[ApiClientId]

        options : typing.Optional[SandboxProcessorTokenCreateRequestOptions]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SandboxProcessorTokenCreateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.sandbox_processor_token_create(
                institution_id="institution_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.sandbox_processor_token_create(
            institution_id=institution_id,
            client_id=client_id,
            options=options,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def sandbox_public_token_create(
        self,
        *,
        initial_products: typing.Sequence[Products],
        institution_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        options: typing.Optional[SandboxPublicTokenCreateRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        user_token: typing.Optional[UserToken] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SandboxPublicTokenCreateResponse:
        """
        Use the `/sandbox/public_token/create` endpoint to create a valid `public_token`  for an arbitrary institution ID, initial products, and test credentials. The created `public_token` maps to a new Sandbox Item. You can then call `/item/public_token/exchange` to exchange the `public_token` for an `access_token` and perform all API actions. `/sandbox/public_token/create` can also be used with the [`user_custom` test username](https://plaid.com/docs/sandbox/user-custom) to generate a test account with custom data. `/sandbox/public_token/create` cannot be used with OAuth institutions.

        Parameters
        ----------
        initial_products : typing.Sequence[Products]
            The products to initially pull for the Item. May be any products that the specified `institution_id`  supports. This array may not be empty.

        institution_id : str
            The ID of the institution the Item will be associated with

        client_id : typing.Optional[ApiClientId]

        options : typing.Optional[SandboxPublicTokenCreateRequestOptions]

        secret : typing.Optional[ApiSecret]

        user_token : typing.Optional[UserToken]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SandboxPublicTokenCreateResponse
            success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.sandbox_public_token_create(
                initial_products=["assets"],
                institution_id="institution_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.sandbox_public_token_create(
            initial_products=initial_products,
            institution_id=institution_id,
            client_id=client_id,
            options=options,
            secret=secret,
            user_token=user_token,
            request_options=request_options,
        )
        return _response.data

    async def sandbox_transfer_fire_webhook(
        self,
        *,
        webhook: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SandboxTransferFireWebhookResponse:
        """
        Use the `/sandbox/transfer/fire_webhook` endpoint to manually trigger a Transfer webhook in the Sandbox environment.

        Parameters
        ----------
        webhook : str
            The URL to which the webhook should be sent.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SandboxTransferFireWebhookResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.sandbox_transfer_fire_webhook(
                webhook="webhook",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.sandbox_transfer_fire_webhook(
            webhook=webhook, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def sandbox_transfer_repayment_simulate(
        self,
        *,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SandboxTransferRepaymentSimulateResponse:
        """
        Use the `/sandbox/transfer/repayment/simulate` endpoint to trigger the creation of a repayment. As a side effect of calling this route, a repayment is created that includes all unreimbursed returns of guaranteed transfers. If there are no such returns, an 400 error is returned.

        Parameters
        ----------
        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SandboxTransferRepaymentSimulateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.sandbox_transfer_repayment_simulate()


        asyncio.run(main())
        """
        _response = await self._raw_client.sandbox_transfer_repayment_simulate(
            client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def sandbox_transfer_simulate(
        self,
        *,
        event_type: str,
        transfer_id: TransferId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        failure_reason: typing.Optional[TransferFailure] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SandboxTransferSimulateResponse:
        """
        Use the `/sandbox/transfer/simulate` endpoint to simulate a transfer event in the Sandbox environment.  Note that while an event will be simulated and will appear when using endpoints such as `/transfer/event/sync` or `/transfer/event/list`, no transactions will actually take place and funds will not move between accounts, even within the Sandbox.

        Parameters
        ----------
        event_type : str
            The asynchronous event to be simulated. May be: `posted`, `settled`, `failed`, or `returned`.

            An error will be returned if the event type is incompatible with the current transfer status. Compatible status --> event type transitions include:

            `pending` --> `failed`

            `pending` --> `posted`

            `posted` --> `returned`

            `posted` --> `settled`

        transfer_id : TransferId

        client_id : typing.Optional[ApiClientId]

        failure_reason : typing.Optional[TransferFailure]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SandboxTransferSimulateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.sandbox_transfer_simulate(
                event_type="event_type",
                transfer_id="transfer_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.sandbox_transfer_simulate(
            event_type=event_type,
            transfer_id=transfer_id,
            client_id=client_id,
            failure_reason=failure_reason,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def sandbox_transfer_sweep_simulate(
        self,
        *,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SandboxTransferSweepSimulateResponse:
        """
        Use the `/sandbox/transfer/sweep/simulate` endpoint to create a sweep and associated events in the Sandbox environment. Upon calling this endpoint, all `posted` or `pending` transfers with a sweep status of `unswept` will become `swept`, and all `returned` transfers with a sweep status of `swept` will become `return_swept`.

        Parameters
        ----------
        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SandboxTransferSweepSimulateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.sandbox_transfer_sweep_simulate()


        asyncio.run(main())
        """
        _response = await self._raw_client.sandbox_transfer_sweep_simulate(
            client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def sandbox_transfer_test_clock_advance(
        self,
        *,
        new_virtual_time: VirtualTime,
        test_clock_id: TransferTestClockId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SandboxTransferTestClockAdvanceResponse:
        """
        Use the `/sandbox/transfer/test_clock/advance` endpoint to advance a `test_clock` in the Sandbox environment.

        A test clock object represents an independent timeline and has a `virtual_time` field indicating the current timestamp of the timeline. A test clock can be advanced by incrementing `virtual_time`, but may never go back to a lower `virtual_time`.

        If a test clock is advanced, we will simulate the changes that ought to occur during the time that elapsed.
        For instance, a client creates a weekly recurring transfer with a test clock set at t. When the client advances the test clock by setting `virtual_time` = t + 15 days, 2 new originations should be created, along with the webhook events.

        The advancement of the test clock from its current `virtual_time` should be limited such that there are no more than 20 originations resulting from the advance operation on each `recurring_transfer` associated with the `test_clock`.
        For instance, if the recurring transfer associated with this test clock originates once every 4 weeks, you can advance the `virtual_time` up to 80 weeks on each API call.

        Parameters
        ----------
        new_virtual_time : VirtualTime

        test_clock_id : TransferTestClockId

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SandboxTransferTestClockAdvanceResponse
            OK

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.sandbox_transfer_test_clock_advance(
                new_virtual_time=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                test_clock_id="test_clock_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.sandbox_transfer_test_clock_advance(
            new_virtual_time=new_virtual_time,
            test_clock_id=test_clock_id,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def sandbox_transfer_test_clock_create(
        self,
        *,
        virtual_time: VirtualTime,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SandboxTransferTestClockCreateResponse:
        """
        Use the `/sandbox/transfer/test_clock/create` endpoint to create a `test_clock` in the Sandbox environment.

        A test clock object represents an independent timeline and has a `virtual_time` field indicating the current timestamp of the timeline. Test clocks are used for testing recurring transfers in Sandbox.

        A test clock can be associated with up to 5 recurring transfers.

        Parameters
        ----------
        virtual_time : VirtualTime

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SandboxTransferTestClockCreateResponse
            OK

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.sandbox_transfer_test_clock_create(
                virtual_time=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.sandbox_transfer_test_clock_create(
            virtual_time=virtual_time, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def sandbox_transfer_test_clock_get(
        self,
        *,
        test_clock_id: TransferTestClockId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SandboxTransferTestClockGetResponse:
        """
        Use the `/sandbox/transfer/test_clock/get` endpoint to get a `test_clock` in the Sandbox environment.

        Parameters
        ----------
        test_clock_id : TransferTestClockId

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SandboxTransferTestClockGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.sandbox_transfer_test_clock_get(
                test_clock_id="test_clock_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.sandbox_transfer_test_clock_get(
            test_clock_id=test_clock_id, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def sandbox_transfer_test_clock_list(
        self,
        *,
        client_id: typing.Optional[ApiClientId] = OMIT,
        count: typing.Optional[int] = OMIT,
        end_virtual_time: typing.Optional[dt.datetime] = OMIT,
        offset: typing.Optional[int] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        start_virtual_time: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SandboxTransferTestClockListResponse:
        """
        Use the `/sandbox/transfer/test_clock/list` endpoint to see a list of all your test clocks in the Sandbox environment, by ascending `virtual_time`. Results are paginated; use the `count` and `offset` query parameters to retrieve the desired test clocks.

        Parameters
        ----------
        client_id : typing.Optional[ApiClientId]

        count : typing.Optional[int]
            The maximum number of test clocks to return.

        end_virtual_time : typing.Optional[dt.datetime]
            The end virtual timestamp of test clocks to return. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`)

        offset : typing.Optional[int]
            The number of test clocks to skip before returning results.

        secret : typing.Optional[ApiSecret]

        start_virtual_time : typing.Optional[dt.datetime]
            The start virtual timestamp of test clocks to return. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SandboxTransferTestClockListResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.sandbox_transfer_test_clock_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.sandbox_transfer_test_clock_list(
            client_id=client_id,
            count=count,
            end_virtual_time=end_virtual_time,
            offset=offset,
            secret=secret,
            start_virtual_time=start_virtual_time,
            request_options=request_options,
        )
        return _response.data

    async def signal_decision_report(
        self,
        *,
        client_transaction_id: str,
        initiated: bool,
        amount_instantly_available: typing.Optional[float] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        days_funds_on_hold: typing.Optional[int] = OMIT,
        decision_outcome: typing.Optional[SignalDecisionOutcome] = OMIT,
        payment_method: typing.Optional[SignalPaymentMethod] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SignalDecisionReportResponse:
        """
        After calling `/signal/evaluate`, call `/signal/decision/report` to report whether the transaction was initiated. This endpoint will return an [`INVALID_FIELD`](/docs/errors/invalid-request/#invalid_field) error if called a second time with a different value for `initiated`.

        Parameters
        ----------
        client_transaction_id : str
            Must be the same as the `client_transaction_id` supplied when calling `/signal/evaluate`

        initiated : bool
            `true` if the ACH transaction was initiated, `false` otherwise.

            This field must be returned as a boolean. If formatted incorrectly, this will result in an [`INVALID_FIELD`](/docs/errors/invalid-request/#invalid_field) error.

        amount_instantly_available : typing.Optional[float]
            The amount (in USD) made available to your customers instantly following the debit transaction. It could be a partial amount of the requested transaction (example: 102.05).

        client_id : typing.Optional[ApiClientId]

        days_funds_on_hold : typing.Optional[int]
            The actual number of days (hold time) since the ACH debit transaction that you wait before making funds available to your customers. The holding time could affect the ACH return rate.

            For example, use 0 if you make funds available to your customers instantly or the same day following the debit transaction, or 1 if you make funds available the next day following the debit initialization.

        decision_outcome : typing.Optional[SignalDecisionOutcome]

        payment_method : typing.Optional[SignalPaymentMethod]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SignalDecisionReportResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.signal_decision_report(
                client_transaction_id="client_transaction_id",
                initiated=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.signal_decision_report(
            client_transaction_id=client_transaction_id,
            initiated=initiated,
            amount_instantly_available=amount_instantly_available,
            client_id=client_id,
            days_funds_on_hold=days_funds_on_hold,
            decision_outcome=decision_outcome,
            payment_method=payment_method,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def signal_evaluate(
        self,
        *,
        access_token: AccessToken,
        account_id: str,
        amount: float,
        client_transaction_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        client_user_id: typing.Optional[str] = OMIT,
        default_payment_method: typing.Optional[str] = OMIT,
        device: typing.Optional[SignalDevice] = OMIT,
        is_recurring: typing.Optional[bool] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        user: typing.Optional[SignalUser] = OMIT,
        user_present: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SignalEvaluateResponse:
        """
        Use `/signal/evaluate` to evaluate a planned ACH transaction to get a return risk assessment (such as a risk score and risk tier) and additional risk signals.

        In order to obtain a valid score for an ACH transaction, Plaid must have an access token for the account, and the Item must be healthy (receiving product updates) or have recently been in a healthy state. If the transaction does not meet eligibility requirements, an error will be returned corresponding to the underlying cause. If `/signal/evaluate` is called on the same transaction multiple times within a 24-hour period, cached results may be returned. For more information please refer to the error documentation on [Item errors](/docs/errors/item/) and [Link in Update Mode](/docs/link/update-mode/).

        Note: This request may take some time to complete if Signal is being added to an existing Item. This is because Plaid must communicate directly with the institution when retrieving the data for the first time.

        Parameters
        ----------
        access_token : AccessToken

        account_id : str
            The Plaid `account_id` of the account that is the funding source for the proposed transaction. The `account_id` is returned in the `/accounts/get` endpoint as well as the [`onSuccess`](/docs/link/ios/#link-ios-onsuccess-linkSuccess-metadata-accounts-id) callback metadata.

            This will return an [`INVALID_ACCOUNT_ID`](/docs/errors/invalid-input/#invalid_account_id) error if the account has been removed at the bank or if the `account_id` is no longer valid.

        amount : float
            The transaction amount, in USD (e.g. `102.05`)

        client_transaction_id : str
            The unique ID that you would like to use to refer to this transaction. For your convenience mapping your internal data, you could use your internal ID/identifier for this transaction. The max length for this field is 36 characters.

        client_id : typing.Optional[ApiClientId]

        client_user_id : typing.Optional[str]
            A unique ID that identifies the end user in your system. This ID is used to correlate requests by a user with multiple Items. The max length for this field is 36 characters. Personally identifiable information, such as an email address or phone number, should not be used in the `client_user_id`.

        default_payment_method : typing.Optional[str]
            The default ACH or non-ACH payment method to complete the transaction.
            `SAME_DAY_ACH`: Same Day ACH by NACHA. The debit transaction is processed and settled on the same day
            `NEXT_DAY_ACH`: Next Day ACH settlement for debit transactions, offered by some payment processors
            `STANDARD_ACH`: standard ACH by NACHA
            `REAL_TIME_PAYMENTS`: real-time payments such as RTP and FedNow
            `DEBIT_CARD`: if the default payment is over debit card networks
            `MULTIPLE_PAYMENT_METHODS`: if there is no default debit rail or there are multiple payment methods
            Possible values:  `SAME_DAY_ACH`, `NEXT_DAY_ACH`, `STANDARD_ACH`, `REAL_TIME_PAYMENTS`, `DEBIT_CARD`, `MULTIPLE_PAYMENT_METHODS`

        device : typing.Optional[SignalDevice]

        is_recurring : typing.Optional[bool]
            `true` if the ACH transaction is a recurring transaction; `false` otherwise

        secret : typing.Optional[ApiSecret]

        user : typing.Optional[SignalUser]

        user_present : typing.Optional[bool]
            `true` if the end user is present while initiating the ACH transfer and the endpoint is being called; `false` otherwise (for example, when the ACH transfer is scheduled and the end user is not present, or you call this endpoint after the ACH transfer but before submitting the Nacha file for ACH processing).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SignalEvaluateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.signal_evaluate(
                access_token="access_token",
                account_id="account_id",
                amount=1.1,
                client_transaction_id="client_transaction_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.signal_evaluate(
            access_token=access_token,
            account_id=account_id,
            amount=amount,
            client_transaction_id=client_transaction_id,
            client_id=client_id,
            client_user_id=client_user_id,
            default_payment_method=default_payment_method,
            device=device,
            is_recurring=is_recurring,
            secret=secret,
            user=user,
            user_present=user_present,
            request_options=request_options,
        )
        return _response.data

    async def signal_prepare(
        self,
        *,
        access_token: AccessToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SignalPrepareResponse:
        """
        When Link is not initialized with Signal, call `/signal/prepare` to opt-in that Item to the Signal data collection process, developing a Signal score.

        If you are using other Plaid products after Link, e.g. Identity or Assets, call `/signal/prepare` after those product calls are complete.

        Example flow: Link is initialized with Auth, call `/auth/get` for the account and routing number, call `/identity/get` to retrieve bank ownership details, then call `/signal/prepare` to begin Signal data collection. Later, once you have obtained details about the proposed transaction from the user, call `/signal/evaluate` for a Signal score. For more information please see [Recommendations for initializing Link with specific product combinations](https://www.plaid.com/docs/link/initializing-products/#recommendations-for-initializing-link-with-specific-product-combinations).

        Parameters
        ----------
        access_token : AccessToken

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SignalPrepareResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.signal_prepare(
                access_token="access_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.signal_prepare(
            access_token=access_token, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def signal_return_report(
        self,
        *,
        client_transaction_id: str,
        return_code: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        returned_at: typing.Optional[dt.datetime] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SignalReturnReportResponse:
        """
        Call the `/signal/return/report` endpoint to report a returned transaction that was previously sent to the `/signal/evaluate` endpoint. Your feedback will be used by the model to incorporate the latest risk trend in your portfolio.

        Parameters
        ----------
        client_transaction_id : str
            Must be the same as the `client_transaction_id` supplied when calling `/signal/evaluate`

        return_code : str
            Must be a valid ACH return code (e.g. "R01")

            If formatted incorrectly, this will result in an [`INVALID_FIELD`](/docs/errors/invalid-request/#invalid_field) error.

        client_id : typing.Optional[ApiClientId]

        returned_at : typing.Optional[dt.datetime]
            Date and time when you receive the returns from your payment processors, in ISO 8601 format (`YYYY-MM-DDTHH:mm:ssZ`).

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SignalReturnReportResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.signal_return_report(
                client_transaction_id="client_transaction_id",
                return_code="return_code",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.signal_return_report(
            client_transaction_id=client_transaction_id,
            return_code=return_code,
            client_id=client_id,
            returned_at=returned_at,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def transactions_enrich(
        self,
        *,
        account_type: str,
        transactions: typing.Sequence[ClientProvidedTransaction],
        client_id: typing.Optional[ApiClientId] = OMIT,
        options: typing.Optional[TransactionsEnrichRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransactionsEnrichGetResponse:
        """
        The `/transactions/enrich` endpoint enriches raw transaction data generated by your own banking products or retrieved from other non-Plaid sources.

        To request access to Enrich, reach out to your Plaid point of contact or send a note to enrich-feedback@plaid.com

        Parameters
        ----------
        account_type : str
            The account type for the requested transactions (either `depository` or `credit`).

        transactions : typing.Sequence[ClientProvidedTransaction]
            An array of transaction objects to be enriched by Plaid. Maximum of 100 transactions per request.

        client_id : typing.Optional[ApiClientId]

        options : typing.Optional[TransactionsEnrichRequestOptions]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransactionsEnrichGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ClientProvidedTransaction

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.transactions_enrich(
                account_type="account_type",
                transactions=[
                    ClientProvidedTransaction(
                        amount=1.1,
                        description="description",
                        direction="INFLOW",
                        id="id",
                        iso_currency_code="iso_currency_code",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.transactions_enrich(
            account_type=account_type,
            transactions=transactions,
            client_id=client_id,
            options=options,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def transactions_get(
        self,
        *,
        access_token: AccessToken,
        end_date: dt.date,
        start_date: dt.date,
        client_id: typing.Optional[ApiClientId] = OMIT,
        options: typing.Optional[TransactionsGetRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransactionsGetResponse:
        """
        The `/transactions/get` endpoint allows developers to receive user-authorized transaction data for credit, depository, and some loan-type accounts (only those with account subtype `student`; coverage may be limited). For transaction history from investments accounts, use the [Investments endpoint](https://plaid.com/docs/api/products/investments/) instead. Transaction data is standardized across financial institutions, and in many cases transactions are linked to a clean name, entity type, location, and category. Similarly, account data is standardized and returned with a clean name, number, balance, and other meta information where available.

        Transactions are returned in reverse-chronological order, and the sequence of transaction ordering is stable and will not shift.  Transactions are not immutable and can also be removed altogether by the institution; a removed transaction will no longer appear in `/transactions/get`.  For more details, see [Pending and posted transactions](https://plaid.com/docs/transactions/transactions-data/#pending-and-posted-transactions).

        Due to the potentially large number of transactions associated with an Item, results are paginated. Manipulate the `count` and `offset` parameters in conjunction with the `total_transactions` response body field to fetch all available transactions.

        Data returned by `/transactions/get` will be the data available for the Item as of the most recent successful check for new transactions. Plaid typically checks for new data multiple times a day, but these checks may occur less frequently, such as once a day, depending on the institution. An Item's `status.transactions.last_successful_update` field will show the timestamp of the most recent successful update. To force Plaid to check for new transactions, you can use the `/transactions/refresh` endpoint.

        Note that data may not be immediately available to `/transactions/get`. Plaid will begin to prepare transactions data upon Item link, if Link was initialized with `transactions`, or upon the first call to `/transactions/get`, if it wasn't. To be alerted when transaction data is ready to be fetched, listen for the [`INITIAL_UPDATE`](https://plaid.com/docs/api/products/transactions/#initial_update) and [`HISTORICAL_UPDATE`](https://plaid.com/docs/api/products/transactions/#historical_update) webhooks. If no transaction history is ready when `/transactions/get` is called, it will return a `PRODUCT_NOT_READY` error.

        Parameters
        ----------
        access_token : AccessToken

        end_date : dt.date
            The latest date for which data should be returned. Dates should be formatted as YYYY-MM-DD.

        start_date : dt.date
            The earliest date for which data should be returned. Dates should be formatted as YYYY-MM-DD.

        client_id : typing.Optional[ApiClientId]

        options : typing.Optional[TransactionsGetRequestOptions]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransactionsGetResponse
            OK

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.transactions_get(
                access_token="access_token",
                end_date=datetime.date.fromisoformat(
                    "2023-01-15",
                ),
                start_date=datetime.date.fromisoformat(
                    "2023-01-15",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.transactions_get(
            access_token=access_token,
            end_date=end_date,
            start_date=start_date,
            client_id=client_id,
            options=options,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def transactions_recurring_get(
        self,
        *,
        access_token: AccessToken,
        account_ids: typing.Sequence[str],
        client_id: typing.Optional[ApiClientId] = OMIT,
        options: typing.Optional[TransactionsRecurringGetRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransactionsRecurringGetResponse:
        """
        The `/transactions/recurring/get` endpoint allows developers to receive a summary of the recurring outflow and inflow streams (expenses and deposits) from a user’s checking, savings or credit card accounts. Additionally, Plaid provides key insights about each recurring stream including the category, merchant, last amount, and more. Developers can use these insights to build tools and experiences that help their users better manage cash flow, monitor subscriptions, reduce spend, and stay on track with bill payments.

        This endpoint is offered as an add-on to Transactions. To request access to this endpoint, submit a [product access request](https://dashboard.plaid.com/team/products) or contact your Plaid account manager.

        This endpoint can only be called on an Item that has already been initialized with Transactions (either during Link, by specifying it in `/link/token/create`; or after Link, by calling `/transactions/get` or `/transactions/sync`). Once all historical transactions have been fetched, call `/transactions/recurring/get` to receive the Recurring Transactions streams and subscribe to the [`RECURRING_TRANSACTIONS_UPDATE`](https://plaid.com/docs/api/products/transactions/#recurring_transactions_update) webhook. To know when historical transactions have been fetched, if you are using `/transactions/sync` listen for the [`SYNC_UPDATES_AVAILABLE`](https://plaid.com/docs/api/products/transactions/#SyncUpdatesAvailableWebhook-historical-update-complete) webhook and check that the `historical_update_complete` field in the payload is `true`. If using `/transactions/get`, listen for the [`HISTORICAL_UPDATE`](https://plaid.com/docs/api/products/transactions/#historical_update) webhook.

        After the initial call, you can call `/transactions/recurring/get` endpoint at any point in the future to retrieve the latest summary of recurring streams. Listen to the [`RECURRING_TRANSACTIONS_UPDATE`](https://plaid.com/docs/api/products/transactions/#recurring_transactions_update) webhook to be notified when new updates are available.

        Parameters
        ----------
        access_token : AccessToken

        account_ids : typing.Sequence[str]
            A list of `account_ids` to retrieve for the Item

            Note: An error will be returned if a provided `account_id` is not associated with the Item.

        client_id : typing.Optional[ApiClientId]

        options : typing.Optional[TransactionsRecurringGetRequestOptions]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransactionsRecurringGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.transactions_recurring_get(
                access_token="access_token",
                account_ids=["account_ids"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.transactions_recurring_get(
            access_token=access_token,
            account_ids=account_ids,
            client_id=client_id,
            options=options,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def transactions_refresh(
        self,
        *,
        access_token: AccessToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransactionsRefreshResponse:
        """
        `/transactions/refresh` is an optional endpoint for users of the Transactions product. It initiates an on-demand extraction to fetch the newest transactions for an Item. This on-demand extraction takes place in addition to the periodic extractions that automatically occur multiple times a day for any Transactions-enabled Item. If changes to transactions are discovered after calling `/transactions/refresh`, Plaid will fire a webhook: for `/transactions/sync` users, [`SYNC_UPDATES_AVAILABLE`](https://plaid.com/docs/api/products/transactions/#sync_updates_available) will be fired if there are any transactions updated, added, or removed. For users of both `/transactions/sync` and `/transactions/get`, [`TRANSACTIONS_REMOVED`](https://plaid.com/docs/api/products/transactions/#transactions_removed) will be fired if any removed transactions are detected, and [`DEFAULT_UPDATE`](https://plaid.com/docs/api/products/transactions/#default_update) will be fired if any new transactions are detected. New transactions can be fetched by calling `/transactions/get` or `/transactions/sync`. Note that the `/transactions/refresh` endpoint is not supported for Capital One (`ins_128026`) and will result in a `PRODUCT_NOT_SUPPORTED` error if called on an Item from that institution.

        `/transactions/refresh` is offered as an add-on to Transactions and has a separate [fee model](/docs/account/billing/#per-request-flat-fee). To request access to this endpoint, submit a [product access request](https://dashboard.plaid.com/team/products) or contact your Plaid account manager.

        Parameters
        ----------
        access_token : AccessToken

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransactionsRefreshResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.transactions_refresh(
                access_token="access_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.transactions_refresh(
            access_token=access_token, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def transactions_sync(
        self,
        *,
        access_token: AccessToken,
        client_id: typing.Optional[ApiClientId] = OMIT,
        count: typing.Optional[int] = OMIT,
        cursor: typing.Optional[str] = OMIT,
        options: typing.Optional[TransactionsSyncRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransactionsSyncResponse:
        """
        This endpoint replaces `/transactions/get` and its associated webhooks for most common use-cases.

        The `/transactions/sync` endpoint allows developers to subscribe to all transactions associated with an Item and get updates synchronously in a stream-like manner, using a cursor to track which updates have already been seen. `/transactions/sync` provides the same functionality as `/transactions/get` and can be used instead of `/transactions/get` to simplify the process of tracking transactions updates.

        This endpoint provides user-authorized transaction data for `credit`, `depository`, and some loan-type accounts (only those with account subtype `student`; coverage may be limited). For transaction history from `investments` accounts, use `/investments/transactions/get` instead.

        Returned transactions data is grouped into three types of update, indicating whether the transaction was added, removed, or modified since the last call to the API.

        In the first call to `/transactions/sync` for an Item, the endpoint will return all historical transactions data associated with that Item up until the time of the API call (as "adds"), which then generates a `next_cursor` for that Item. In subsequent calls, send the `next_cursor` to receive only the changes that have occurred since the previous call.

        Due to the potentially large number of transactions associated with an Item, results are paginated. The `has_more` field specifies if additional calls are necessary to fetch all available transaction updates. Call `/transactions/sync` with the new cursor, pulling all updates, until `has_more` is `false`.

        When retrieving paginated updates, track both the `next_cursor` from the latest response and the original cursor from the first call in which `has_more` was `true`; if a call to `/transactions/sync` fails when retrieving a paginated update, which can occur as a result of the [`TRANSACTIONS_SYNC_MUTATION_DURING_PAGINATION`](https://plaid.com/docs/errors/transactions/#transactions_sync_mutation_during_pagination) error, the entire pagination request loop must be restarted beginning with the cursor for the first page of the update, rather than retrying only the single request that failed.

        Whenever new or updated transaction data becomes available, `/transactions/sync` will provide these updates. Plaid typically checks for new data multiple times a day, but these checks may occur less frequently, such as once a day, depending on the institution. An Item's `status.transactions.last_successful_update` field will show the timestamp of the most recent successful update. To force Plaid to check for new transactions, use the `/transactions/refresh` endpoint.

        Note that for newly created Items, data may not be immediately available to `/transactions/sync`. Plaid begins preparing transactions data when the Item is created, but the process can take anywhere from a few seconds to several minutes to complete, depending on the number of transactions available.

        To be alerted when new data is available, listen for the [`SYNC_UPDATES_AVAILABLE`](https://plaid.com/docs/api/products/transactions/#sync_updates_available) webhook.

        Parameters
        ----------
        access_token : AccessToken

        client_id : typing.Optional[ApiClientId]

        count : typing.Optional[int]
            The number of transaction updates to fetch.

        cursor : typing.Optional[str]
            The cursor value represents the last update requested. Providing it will cause the response to only return changes after this update.
            If omitted, the entire history of updates will be returned, starting with the first-added transactions on the item.
            Note: The upper-bound length of this cursor is 256 characters of base64.

        options : typing.Optional[TransactionsSyncRequestOptions]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransactionsSyncResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.transactions_sync(
                access_token="access_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.transactions_sync(
            access_token=access_token,
            client_id=client_id,
            count=count,
            cursor=cursor,
            options=options,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def transfer_authorization_create(
        self,
        *,
        amount: TransferAmount,
        network: TransferNetwork,
        type: TransferType,
        user: TransferAuthorizationUserInRequest,
        access_token: typing.Optional[TransferAccessToken] = OMIT,
        account_id: typing.Optional[TransferAccountId] = OMIT,
        ach_class: typing.Optional[AchClass] = OMIT,
        beacon_session_id: typing.Optional[str] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        device: typing.Optional[TransferAuthorizationDevice] = OMIT,
        funding_account_id: typing.Optional[TransferFundingAccountIdRequest] = OMIT,
        idempotency_key: typing.Optional[TransferAuthorizationIdempotencyKey] = OMIT,
        iso_currency_code: typing.Optional[str] = OMIT,
        origination_account_id: typing.Optional[str] = OMIT,
        originator_client_id: typing.Optional[str] = OMIT,
        payment_profile_token: typing.Optional[TransferPaymentProfileToken] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        user_present: typing.Optional[bool] = OMIT,
        with_guarantee: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferAuthorizationCreateResponse:
        """
        Use the `/transfer/authorization/create` endpoint to determine transfer failure risk.

        In Plaid's Sandbox environment the decisions will be returned as follows:

          - To approve a transfer with null rationale code, make an authorization request with an `amount` less than the available balance in the account.

          - To approve a transfer with the rationale code `MANUALLY_VERIFIED_ITEM`, create an Item in Link through the [Same Day Micro-deposits flow](https://plaid.com/docs/auth/coverage/testing/#testing-same-day-micro-deposits).

          - To approve a transfer with the rationale code `ITEM_LOGIN_REQUIRED`, [reset the login for an Item](https://plaid.com/docs/sandbox/#item_login_required).

          - To decline a transfer with the rationale code `NSF`, the available balance on the account must be less than the authorization `amount`. See [Create Sandbox test data](https://plaid.com/docs/sandbox/user-custom/) for details on how to customize data in Sandbox.

          - To decline a transfer with the rationale code `RISK`, the available balance on the account must be exactly $0. See [Create Sandbox test data](https://plaid.com/docs/sandbox/user-custom/) for details on how to customize data in Sandbox.

        `device.ip_address`, `device.user_agent` are required fields.

        For [Guarantee](https://www.plaid.com/docs//transfer/guarantee/), the following fields are required : `idempotency_key`, `user.phone_number` (optional if `email_address` provided), `user.email_address` (optional if `phone_number` provided), `device.ip_address`, `device.user_agent`, and `user_present`.

        Parameters
        ----------
        amount : TransferAmount

        network : TransferNetwork

        type : TransferType

        user : TransferAuthorizationUserInRequest

        access_token : typing.Optional[TransferAccessToken]

        account_id : typing.Optional[TransferAccountId]

        ach_class : typing.Optional[AchClass]

        beacon_session_id : typing.Optional[str]
            The unique identifier returned by Plaid's [beacon](https://plaid.com/docs/transfer/guarantee/#using-a-beacon) when it is run on your webpage. Required for Guarantee customers who are not using [Transfer UI](https://plaid.com/docs/transfer/using-transfer-ui/) and have a web checkout experience.

        client_id : typing.Optional[ApiClientId]

        device : typing.Optional[TransferAuthorizationDevice]

        funding_account_id : typing.Optional[TransferFundingAccountIdRequest]

        idempotency_key : typing.Optional[TransferAuthorizationIdempotencyKey]

        iso_currency_code : typing.Optional[str]
            The currency of the transfer amount. The default value is "USD".

        origination_account_id : typing.Optional[str]
            Plaid's unique identifier for the origination account for this authorization. If not specified, the default account will be used.

        originator_client_id : typing.Optional[str]
            The Plaid client ID that is the originator of this transfer. Only needed if creating transfers on behalf of another client as a third-party sender (TPS).

        payment_profile_token : typing.Optional[TransferPaymentProfileToken]

        secret : typing.Optional[ApiSecret]

        user_present : typing.Optional[bool]
            Required for Guarantee. If the end user is initiating the specific transfer themselves via an interactive UI, this should be `true`; for automatic recurring payments where the end user is not actually initiating each individual transfer, it should be `false`.

        with_guarantee : typing.Optional[bool]
            If set to `false`, Plaid will not offer a `guarantee_decision` for this request(Guarantee customers only).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferAuthorizationCreateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, TransferAuthorizationUserInRequest

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.transfer_authorization_create(
                amount="amount",
                network="ach",
                type="debit",
                user=TransferAuthorizationUserInRequest(
                    legal_name="legal_name",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.transfer_authorization_create(
            amount=amount,
            network=network,
            type=type,
            user=user,
            access_token=access_token,
            account_id=account_id,
            ach_class=ach_class,
            beacon_session_id=beacon_session_id,
            client_id=client_id,
            device=device,
            funding_account_id=funding_account_id,
            idempotency_key=idempotency_key,
            iso_currency_code=iso_currency_code,
            origination_account_id=origination_account_id,
            originator_client_id=originator_client_id,
            payment_profile_token=payment_profile_token,
            secret=secret,
            user_present=user_present,
            with_guarantee=with_guarantee,
            request_options=request_options,
        )
        return _response.data

    async def transfer_cancel(
        self,
        *,
        transfer_id: TransferId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        originator_client_id: typing.Optional[str] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferCancelResponse:
        """
        Use the `/transfer/cancel` endpoint to cancel a transfer.  A transfer is eligible for cancellation if the `cancellable` property returned by `/transfer/get` is `true`.

        Parameters
        ----------
        transfer_id : TransferId

        client_id : typing.Optional[ApiClientId]

        originator_client_id : typing.Optional[str]
            The Plaid client ID of the transfer originator. Should only be present if `client_id` is a third-party sender (TPS).

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferCancelResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.transfer_cancel(
                transfer_id="transfer_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.transfer_cancel(
            transfer_id=transfer_id,
            client_id=client_id,
            originator_client_id=originator_client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def transfer_capabilities_get(
        self,
        *,
        access_token: typing.Optional[TransferAccessToken] = OMIT,
        account_id: typing.Optional[TransferAccountId] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        payment_profile_token: typing.Optional[PaymentProfileToken] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferCapabilitiesGetResponse:
        """
        Use the `/transfer/capabilities/get` endpoint to determine the RTP eligibility information of a transfer.

        Parameters
        ----------
        access_token : typing.Optional[TransferAccessToken]

        account_id : typing.Optional[TransferAccountId]

        client_id : typing.Optional[ApiClientId]

        payment_profile_token : typing.Optional[PaymentProfileToken]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferCapabilitiesGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.transfer_capabilities_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.transfer_capabilities_get(
            access_token=access_token,
            account_id=account_id,
            client_id=client_id,
            payment_profile_token=payment_profile_token,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def transfer_configuration_get(
        self,
        *,
        client_id: typing.Optional[ApiClientId] = OMIT,
        originator_client_id: typing.Optional[str] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferConfigurationGetResponse:
        """
        Use the `/transfer/configuration/get` endpoint to view your transfer product configurations.

        Parameters
        ----------
        client_id : typing.Optional[ApiClientId]

        originator_client_id : typing.Optional[str]
            The Plaid client ID of the transfer originator. Should only be present if `client_id` is a third-party sender (TPS).

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferConfigurationGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.transfer_configuration_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.transfer_configuration_get(
            client_id=client_id,
            originator_client_id=originator_client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def transfer_create(
        self,
        *,
        authorization_id: str,
        description: str,
        access_token: typing.Optional[TransferAccessToken] = OMIT,
        account_id: typing.Optional[TransferAccountId] = OMIT,
        ach_class: typing.Optional[AchClass] = OMIT,
        amount: typing.Optional[TransferAmount] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        idempotency_key: typing.Optional[TransferCreateIdempotencyKey] = OMIT,
        iso_currency_code: typing.Optional[str] = OMIT,
        metadata: typing.Optional[TransferMetadata] = OMIT,
        network: typing.Optional[TransferNetwork] = OMIT,
        origination_account_id: typing.Optional[str] = OMIT,
        payment_profile_token: typing.Optional[TransferPaymentProfileToken] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        type: typing.Optional[TransferType] = OMIT,
        user: typing.Optional[TransferUserInRequestDeprecated] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferCreateResponse:
        """
        Use the `/transfer/create` endpoint to initiate a new transfer.

        Parameters
        ----------
        authorization_id : str
            Plaid’s unique identifier for a transfer authorization. This parameter also serves the purpose of acting as an idempotency identifier.

        description : str
            The transfer description. Maximum of 10 characters. If reprocessing a returned transfer, please note that the `description` field must be `"Retry"` to indicate that it's a retry of a previously returned transfer. You may retry a transfer up to 2 times, within 180 days of creating the original transfer. Only transfers that were returned with code `R01` or `R09` may be retried. For a full listing of ACH return codes, see [Transfer errors](https://plaid.com/docs/errors/transfer/#ach-return-codes).

        access_token : typing.Optional[TransferAccessToken]

        account_id : typing.Optional[TransferAccountId]

        ach_class : typing.Optional[AchClass]

        amount : typing.Optional[TransferAmount]

        client_id : typing.Optional[ApiClientId]

        idempotency_key : typing.Optional[TransferCreateIdempotencyKey]

        iso_currency_code : typing.Optional[str]
            The currency of the transfer amount. The default value is "USD".

        metadata : typing.Optional[TransferMetadata]

        network : typing.Optional[TransferNetwork]

        origination_account_id : typing.Optional[str]
            Plaid’s unique identifier for the origination account for this transfer. If you have more than one origination account, this value must be specified. Otherwise, this field should be left blank.

        payment_profile_token : typing.Optional[TransferPaymentProfileToken]

        secret : typing.Optional[ApiSecret]

        type : typing.Optional[TransferType]

        user : typing.Optional[TransferUserInRequestDeprecated]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferCreateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.transfer_create(
                authorization_id="authorization_id",
                description="description",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.transfer_create(
            authorization_id=authorization_id,
            description=description,
            access_token=access_token,
            account_id=account_id,
            ach_class=ach_class,
            amount=amount,
            client_id=client_id,
            idempotency_key=idempotency_key,
            iso_currency_code=iso_currency_code,
            metadata=metadata,
            network=network,
            origination_account_id=origination_account_id,
            payment_profile_token=payment_profile_token,
            secret=secret,
            type=type,
            user=user,
            request_options=request_options,
        )
        return _response.data

    async def transfer_event_list(
        self,
        *,
        account_id: typing.Optional[str] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        count: typing.Optional[int] = OMIT,
        end_date: typing.Optional[dt.datetime] = OMIT,
        event_types: typing.Optional[typing.Sequence[TransferEventType]] = OMIT,
        funding_account_id: typing.Optional[str] = OMIT,
        offset: typing.Optional[int] = OMIT,
        origination_account_id: typing.Optional[str] = OMIT,
        originator_client_id: typing.Optional[str] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        start_date: typing.Optional[dt.datetime] = OMIT,
        sweep_id: typing.Optional[str] = OMIT,
        transfer_id: typing.Optional[str] = OMIT,
        transfer_type: typing.Optional[TransferEventListTransferType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferEventListResponse:
        """
        Use the `/transfer/event/list` endpoint to get a list of transfer events based on specified filter criteria.

        Parameters
        ----------
        account_id : typing.Optional[str]
            The account ID to get events for all transactions to/from an account.

        client_id : typing.Optional[ApiClientId]

        count : typing.Optional[int]
            The maximum number of transfer events to return. If the number of events matching the above parameters is greater than `count`, the most recent events will be returned.

        end_date : typing.Optional[dt.datetime]
            The end datetime of transfers to list. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`)

        event_types : typing.Optional[typing.Sequence[TransferEventType]]
            Filter events by event type.

        funding_account_id : typing.Optional[str]
            Filter transfer events to only those with the specified `funding_account_id`.

        offset : typing.Optional[int]
            The offset into the list of transfer events. When `count`=25 and `offset`=0, the first 25 events will be returned. When `count`=25 and `offset`=25, the next 25 events will be returned.

        origination_account_id : typing.Optional[str]
            The origination account ID to get events for transfers from a specific origination account.

        originator_client_id : typing.Optional[str]
            Filter transfer events to only those with the specified originator client.

        secret : typing.Optional[ApiSecret]

        start_date : typing.Optional[dt.datetime]
            The start datetime of transfers to list. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`)

        sweep_id : typing.Optional[str]
            Plaid’s unique identifier for a sweep.

        transfer_id : typing.Optional[str]
            Plaid’s unique identifier for a transfer.

        transfer_type : typing.Optional[TransferEventListTransferType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferEventListResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.transfer_event_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.transfer_event_list(
            account_id=account_id,
            client_id=client_id,
            count=count,
            end_date=end_date,
            event_types=event_types,
            funding_account_id=funding_account_id,
            offset=offset,
            origination_account_id=origination_account_id,
            originator_client_id=originator_client_id,
            secret=secret,
            start_date=start_date,
            sweep_id=sweep_id,
            transfer_id=transfer_id,
            transfer_type=transfer_type,
            request_options=request_options,
        )
        return _response.data

    async def transfer_event_sync(
        self,
        *,
        after_id: int,
        client_id: typing.Optional[ApiClientId] = OMIT,
        count: typing.Optional[int] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferEventSyncResponse:
        """
        `/transfer/event/sync` allows you to request up to the next 25 transfer events that happened after a specific `event_id`. Use the `/transfer/event/sync` endpoint to guarantee you have seen all transfer events. When using Auth with micro-deposit verification enabled, this endpoint can be used to fetch status updates on ACH micro-deposits. For more details, see [micro-deposit events](https://www.plaid.com/docs/auth/coverage/microdeposit-events/).

        Parameters
        ----------
        after_id : int
            The latest (largest) `event_id` fetched via the sync endpoint, or 0 initially.

        client_id : typing.Optional[ApiClientId]

        count : typing.Optional[int]
            The maximum number of transfer events to return.

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferEventSyncResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.transfer_event_sync(
                after_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.transfer_event_sync(
            after_id=after_id, client_id=client_id, count=count, secret=secret, request_options=request_options
        )
        return _response.data

    async def transfer_get(
        self,
        *,
        transfer_id: TransferId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        originator_client_id: typing.Optional[str] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferGetResponse:
        """
        The `/transfer/get` endpoint fetches information about the transfer corresponding to the given `transfer_id`.

        Parameters
        ----------
        transfer_id : TransferId

        client_id : typing.Optional[ApiClientId]

        originator_client_id : typing.Optional[str]
            The Plaid client ID of the transfer originator. Should only be present if `client_id` is a third-party sender (TPS).

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.transfer_get(
                transfer_id="transfer_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.transfer_get(
            transfer_id=transfer_id,
            client_id=client_id,
            originator_client_id=originator_client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def transfer_intent_create(
        self,
        *,
        amount: TransferAmount,
        description: str,
        mode: TransferIntentCreateMode,
        user: TransferUserInRequest,
        account_id: typing.Optional[str] = OMIT,
        ach_class: typing.Optional[AchClass] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        funding_account_id: typing.Optional[TransferFundingAccountIdRequest] = OMIT,
        iso_currency_code: typing.Optional[str] = OMIT,
        metadata: typing.Optional[TransferMetadata] = OMIT,
        network: typing.Optional[TransferIntentCreateNetwork] = OMIT,
        origination_account_id: typing.Optional[str] = OMIT,
        require_guarantee: typing.Optional[bool] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferIntentCreateResponse:
        """
        Use the `/transfer/intent/create` endpoint to generate a transfer intent object and invoke the Transfer UI.

        Parameters
        ----------
        amount : TransferAmount

        description : str
            A description for the underlying transfer. Maximum of 8 characters.

        mode : TransferIntentCreateMode

        user : TransferUserInRequest

        account_id : typing.Optional[str]
            The Plaid `account_id` corresponding to the end-user account that will be debited or credited.

        ach_class : typing.Optional[AchClass]

        client_id : typing.Optional[ApiClientId]

        funding_account_id : typing.Optional[TransferFundingAccountIdRequest]

        iso_currency_code : typing.Optional[str]
            The currency of the transfer amount, e.g. "USD"

        metadata : typing.Optional[TransferMetadata]

        network : typing.Optional[TransferIntentCreateNetwork]

        origination_account_id : typing.Optional[str]
            Plaid’s unique identifier for the origination account for the intent. If not provided, the default account will be used.

        require_guarantee : typing.Optional[bool]
            When `true`, the transfer requires a `GUARANTEED` decision by Plaid to proceed (Guarantee customers only).

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferIntentCreateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, TransferUserInRequest

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.transfer_intent_create(
                amount="amount",
                description="description",
                mode="PAYMENT",
                user=TransferUserInRequest(
                    legal_name="legal_name",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.transfer_intent_create(
            amount=amount,
            description=description,
            mode=mode,
            user=user,
            account_id=account_id,
            ach_class=ach_class,
            client_id=client_id,
            funding_account_id=funding_account_id,
            iso_currency_code=iso_currency_code,
            metadata=metadata,
            network=network,
            origination_account_id=origination_account_id,
            require_guarantee=require_guarantee,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def transfer_intent_get(
        self,
        *,
        transfer_intent_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferIntentGetResponse:
        """
        Use the `/transfer/intent/get` endpoint to retrieve more information about a transfer intent.

        Parameters
        ----------
        transfer_intent_id : str
            Plaid's unique identifier for a transfer intent object.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferIntentGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.transfer_intent_get(
                transfer_intent_id="transfer_intent_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.transfer_intent_get(
            transfer_intent_id=transfer_intent_id, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def transfer_list(
        self,
        *,
        client_id: typing.Optional[ApiClientId] = OMIT,
        count: typing.Optional[int] = OMIT,
        end_date: typing.Optional[dt.datetime] = OMIT,
        funding_account_id: typing.Optional[str] = OMIT,
        offset: typing.Optional[int] = OMIT,
        origination_account_id: typing.Optional[str] = OMIT,
        originator_client_id: typing.Optional[str] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        start_date: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferListResponse:
        """
        Use the `/transfer/list` endpoint to see a list of all your transfers and their statuses. Results are paginated; use the `count` and `offset` query parameters to retrieve the desired transfers.

        Parameters
        ----------
        client_id : typing.Optional[ApiClientId]

        count : typing.Optional[int]
            The maximum number of transfers to return.

        end_date : typing.Optional[dt.datetime]
            The end datetime of transfers to list. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`)

        funding_account_id : typing.Optional[str]
            Filter transfers to only those with the specified `funding_account_id`.

        offset : typing.Optional[int]
            The number of transfers to skip before returning results.

        origination_account_id : typing.Optional[str]
            Filter transfers to only those originated through the specified origination account.

        originator_client_id : typing.Optional[str]
            Filter transfers to only those with the specified originator client.

        secret : typing.Optional[ApiSecret]

        start_date : typing.Optional[dt.datetime]
            The start datetime of transfers to list. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferListResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.transfer_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.transfer_list(
            client_id=client_id,
            count=count,
            end_date=end_date,
            funding_account_id=funding_account_id,
            offset=offset,
            origination_account_id=origination_account_id,
            originator_client_id=originator_client_id,
            secret=secret,
            start_date=start_date,
            request_options=request_options,
        )
        return _response.data

    async def transfer_metrics_get(
        self,
        *,
        client_id: typing.Optional[ApiClientId] = OMIT,
        originator_client_id: typing.Optional[str] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferMetricsGetResponse:
        """
        Use the `/transfer/metrics/get` endpoint to view your transfer product usage metrics.

        Parameters
        ----------
        client_id : typing.Optional[ApiClientId]

        originator_client_id : typing.Optional[str]
            The Plaid client ID of the transfer originator. Should only be present if `client_id` is a third-party sender (TPS).

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferMetricsGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.transfer_metrics_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.transfer_metrics_get(
            client_id=client_id,
            originator_client_id=originator_client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def transfer_migrate_account(
        self,
        *,
        account_number: str,
        account_type: str,
        routing_number: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        wire_routing_number: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferMigrateAccountResponse:
        """
        As an alternative to adding Items via Link, you can also use the `/transfer/migrate_account` endpoint to migrate known account and routing numbers to Plaid Items.  Note that Items created in this way are not compatible with endpoints for other products, such as `/accounts/balance/get`, and can only be used with Transfer endpoints.  If you require access to other endpoints, create the Item through Link instead.  Access to `/transfer/migrate_account` is not enabled by default; to obtain access, contact your Plaid Account Manager.

        Parameters
        ----------
        account_number : str
            The user's account number.

        account_type : str
            The type of the bank account (`checking` or `savings`).

        routing_number : str
            The user's routing number.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        wire_routing_number : typing.Optional[str]
            The user's wire transfer routing number. This is the ABA number; for some institutions, this may differ from the ACH number used in `routing_number`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferMigrateAccountResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.transfer_migrate_account(
                account_number="account_number",
                account_type="account_type",
                routing_number="routing_number",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.transfer_migrate_account(
            account_number=account_number,
            account_type=account_type,
            routing_number=routing_number,
            client_id=client_id,
            secret=secret,
            wire_routing_number=wire_routing_number,
            request_options=request_options,
        )
        return _response.data

    async def transfer_originator_create(
        self,
        *,
        company_name: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferOriginatorCreateResponse:
        """
        Use the `/transfer/originator/create` endpoint to create a new originator and return an `originator_client_id`.

        Parameters
        ----------
        company_name : str
            The company name of the end customer being created. This will be displayed in public-facing surfaces, e.g. Plaid Dashboard.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferOriginatorCreateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.transfer_originator_create(
                company_name="company_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.transfer_originator_create(
            company_name=company_name, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def transfer_originator_get(
        self,
        *,
        originator_client_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferOriginatorGetResponse:
        """
        The `/transfer/originator/get` endpoint gets status updates for an originator's onboarding process. This information is also available via the Transfer page on the Plaid dashboard.

        Parameters
        ----------
        originator_client_id : str
            Client ID of the end customer (i.e. the originator).

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferOriginatorGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.transfer_originator_get(
                originator_client_id="originator_client_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.transfer_originator_get(
            originator_client_id=originator_client_id,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def transfer_originator_list(
        self,
        *,
        client_id: typing.Optional[ApiClientId] = OMIT,
        count: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferOriginatorListResponse:
        """
        The `/transfer/originator/list` endpoint gets status updates for all of your originators' onboarding. This information is also available via the Plaid dashboard.

        Parameters
        ----------
        client_id : typing.Optional[ApiClientId]

        count : typing.Optional[int]
            The maximum number of originators to return.

        offset : typing.Optional[int]
            The number of originators to skip before returning results.

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferOriginatorListResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.transfer_originator_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.transfer_originator_list(
            client_id=client_id, count=count, offset=offset, secret=secret, request_options=request_options
        )
        return _response.data

    async def transfer_questionnaire_create(
        self,
        *,
        originator_client_id: str,
        redirect_uri: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferQuestionnaireCreateResponse:
        """
        The `/transfer/questionnaire/create` endpoint generates a Plaid-hosted onboarding UI URL. Redirect the originator to this URL to provide their due diligence information and agree to Plaid’s terms for ACH money movement.

        Parameters
        ----------
        originator_client_id : str
            Client ID of the end customer.

        redirect_uri : str
            URL the end customer will be redirected to after completing questions in Plaid-hosted onboarding flow.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferQuestionnaireCreateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.transfer_questionnaire_create(
                originator_client_id="originator_client_id",
                redirect_uri="redirect_uri",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.transfer_questionnaire_create(
            originator_client_id=originator_client_id,
            redirect_uri=redirect_uri,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def transfer_recurring_cancel(
        self,
        *,
        recurring_transfer_id: RecurringTransferId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferRecurringCancelResponse:
        """
        Use the `/transfer/recurring/cancel` endpoint to cancel a recurring transfer.  Scheduled transfer that hasn't been submitted to bank will be cancelled.

        Parameters
        ----------
        recurring_transfer_id : RecurringTransferId

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferRecurringCancelResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.transfer_recurring_cancel(
                recurring_transfer_id="recurring_transfer_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.transfer_recurring_cancel(
            recurring_transfer_id=recurring_transfer_id,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def transfer_recurring_create(
        self,
        *,
        access_token: TransferAccessToken,
        account_id: TransferAccountId,
        amount: TransferAmount,
        description: str,
        device: TransferDevice,
        idempotency_key: TransferRecurringIdempotencyKey,
        network: TransferNetwork,
        schedule: TransferRecurringSchedule,
        type: TransferType,
        user: TransferUserInRequest,
        ach_class: typing.Optional[AchClass] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        funding_account_id: typing.Optional[TransferFundingAccountIdRequest] = OMIT,
        iso_currency_code: typing.Optional[str] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        test_clock_id: typing.Optional[str] = OMIT,
        user_present: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferRecurringCreateResponse:
        """
        Use the `/transfer/recurring/create` endpoint to initiate a new recurring transfer.

        Parameters
        ----------
        access_token : TransferAccessToken

        account_id : TransferAccountId

        amount : TransferAmount

        description : str
            The description of the recurring transfer.

        device : TransferDevice

        idempotency_key : TransferRecurringIdempotencyKey

        network : TransferNetwork

        schedule : TransferRecurringSchedule

        type : TransferType

        user : TransferUserInRequest

        ach_class : typing.Optional[AchClass]

        client_id : typing.Optional[ApiClientId]

        funding_account_id : typing.Optional[TransferFundingAccountIdRequest]

        iso_currency_code : typing.Optional[str]
            The currency of the transfer amount. The default value is "USD".

        secret : typing.Optional[ApiSecret]

        test_clock_id : typing.Optional[str]
            Plaid’s unique identifier for a test clock.

        user_present : typing.Optional[bool]
            If the end user is initiating the specific transfer themselves via an interactive UI, this should be `true`; for automatic recurring payments where the end user is not actually initiating each individual transfer, it should be `false`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferRecurringCreateResponse
            OK

        Examples
        --------
        import asyncio
        import datetime

        from fern import (
            AsyncFernApi,
            TransferDevice,
            TransferRecurringSchedule,
            TransferUserInRequest,
        )

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.transfer_recurring_create(
                access_token="access_token",
                account_id="account_id",
                amount="amount",
                description="description",
                device=TransferDevice(
                    ip_address="ip_address",
                    user_agent="user_agent",
                ),
                idempotency_key="idempotency_key",
                network="ach",
                schedule=TransferRecurringSchedule(
                    interval_count=1,
                    interval_execution_day=1,
                    interval_unit="week",
                    start_date=datetime.date.fromisoformat(
                        "2023-01-15",
                    ),
                ),
                type="debit",
                user=TransferUserInRequest(
                    legal_name="legal_name",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.transfer_recurring_create(
            access_token=access_token,
            account_id=account_id,
            amount=amount,
            description=description,
            device=device,
            idempotency_key=idempotency_key,
            network=network,
            schedule=schedule,
            type=type,
            user=user,
            ach_class=ach_class,
            client_id=client_id,
            funding_account_id=funding_account_id,
            iso_currency_code=iso_currency_code,
            secret=secret,
            test_clock_id=test_clock_id,
            user_present=user_present,
            request_options=request_options,
        )
        return _response.data

    async def transfer_recurring_get(
        self,
        *,
        recurring_transfer_id: RecurringTransferId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferRecurringGetResponse:
        """
        The `/transfer/recurring/get` fetches information about the recurring transfer corresponding to the given `recurring_transfer_id`.

        Parameters
        ----------
        recurring_transfer_id : RecurringTransferId

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferRecurringGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.transfer_recurring_get(
                recurring_transfer_id="recurring_transfer_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.transfer_recurring_get(
            recurring_transfer_id=recurring_transfer_id,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def transfer_recurring_list(
        self,
        *,
        client_id: typing.Optional[ApiClientId] = OMIT,
        count: typing.Optional[int] = OMIT,
        end_time: typing.Optional[dt.datetime] = OMIT,
        funding_account_id: typing.Optional[str] = OMIT,
        offset: typing.Optional[int] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        start_time: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferRecurringListResponse:
        """
        Use the `/transfer/recurring/list` endpoint to see a list of all your recurring transfers and their statuses. Results are paginated; use the `count` and `offset` query parameters to retrieve the desired recurring transfers.

        Parameters
        ----------
        client_id : typing.Optional[ApiClientId]

        count : typing.Optional[int]
            The maximum number of recurring transfers to return.

        end_time : typing.Optional[dt.datetime]
            The end datetime of recurring transfers to list. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`)

        funding_account_id : typing.Optional[str]
            Filter recurring transfers to only those with the specified `funding_account_id`.

        offset : typing.Optional[int]
            The number of recurring transfers to skip before returning results.

        secret : typing.Optional[ApiSecret]

        start_time : typing.Optional[dt.datetime]
            The start datetime of recurring transfers to list. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferRecurringListResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.transfer_recurring_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.transfer_recurring_list(
            client_id=client_id,
            count=count,
            end_time=end_time,
            funding_account_id=funding_account_id,
            offset=offset,
            secret=secret,
            start_time=start_time,
            request_options=request_options,
        )
        return _response.data

    async def transfer_refund_cancel(
        self,
        *,
        refund_id: TransferRefundId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferRefundCancelResponse:
        """
        Use the `/transfer/refund/cancel` endpoint to cancel a refund.  A refund is eligible for cancellation if it has not yet been submitted to the payment network.

        Parameters
        ----------
        refund_id : TransferRefundId

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferRefundCancelResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.transfer_refund_cancel(
                refund_id="refund_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.transfer_refund_cancel(
            refund_id=refund_id, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def transfer_refund_create(
        self,
        *,
        amount: TransferRefundAmount,
        idempotency_key: TransferRefundIdempotencyKey,
        transfer_id: TransferIdForRefund,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferRefundCreateResponse:
        """
        Use the `/transfer/refund/create` endpoint to create a refund for a transfer. A transfer can be refunded if the transfer was initiated in the past 180 days.

        Processing of the refund will not occur until at least 3 business days following the transfer's settlement date, plus any hold/settlement delays. This 3-day window helps better protect your business from regular ACH returns. Consumer initiated returns (unauthorized returns) could still happen for about 60 days from the settlement date. If the original transfer is canceled, returned or failed, all pending refunds will automatically be canceled. Processed refunds cannot be revoked.

        Parameters
        ----------
        amount : TransferRefundAmount

        idempotency_key : TransferRefundIdempotencyKey

        transfer_id : TransferIdForRefund

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferRefundCreateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.transfer_refund_create(
                amount="amount",
                idempotency_key="idempotency_key",
                transfer_id="transfer_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.transfer_refund_create(
            amount=amount,
            idempotency_key=idempotency_key,
            transfer_id=transfer_id,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def transfer_refund_get(
        self,
        *,
        refund_id: TransferRefundId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferRefundGetResponse:
        """
        The `/transfer/refund/get` endpoint fetches information about the refund corresponding to the given `refund_id`.

        Parameters
        ----------
        refund_id : TransferRefundId

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferRefundGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.transfer_refund_get(
                refund_id="refund_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.transfer_refund_get(
            refund_id=refund_id, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def transfer_repayment_list(
        self,
        *,
        client_id: typing.Optional[ApiClientId] = OMIT,
        count: typing.Optional[int] = OMIT,
        end_date: typing.Optional[dt.datetime] = OMIT,
        offset: typing.Optional[int] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        start_date: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferRepaymentListResponse:
        """
        The `/transfer/repayment/list` endpoint fetches repayments matching the given filters. Repayments are returned in reverse-chronological order (most recent first) starting at the given `start_time`.

        Parameters
        ----------
        client_id : typing.Optional[ApiClientId]

        count : typing.Optional[int]
            The maximum number of repayments to return.

        end_date : typing.Optional[dt.datetime]
            The end datetime of repayments to return (RFC 3339 format).

        offset : typing.Optional[int]
            The number of repayments to skip before returning results.

        secret : typing.Optional[ApiSecret]

        start_date : typing.Optional[dt.datetime]
            The start datetime of repayments to return (RFC 3339 format).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferRepaymentListResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.transfer_repayment_list(
                count=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.transfer_repayment_list(
            client_id=client_id,
            count=count,
            end_date=end_date,
            offset=offset,
            secret=secret,
            start_date=start_date,
            request_options=request_options,
        )
        return _response.data

    async def transfer_repayment_return_list(
        self,
        *,
        repayment_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        count: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferRepaymentReturnListResponse:
        """
        The `/transfer/repayment/return/list` endpoint retrieves the set of returns that were batched together into the specified repayment. The sum of amounts of returns retrieved by this request equals the amount of the repayment.

        Parameters
        ----------
        repayment_id : str
            Identifier of the repayment to query.

        client_id : typing.Optional[ApiClientId]

        count : typing.Optional[int]
            The maximum number of repayments to return.

        offset : typing.Optional[int]
            The number of repayments to skip before returning results.

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferRepaymentReturnListResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.transfer_repayment_return_list(
                count=1,
                repayment_id="d4bfce70-2470-4298-ae87-5e9b3e18bfaf",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.transfer_repayment_return_list(
            repayment_id=repayment_id,
            client_id=client_id,
            count=count,
            offset=offset,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def transfer_sweep_get(
        self,
        *,
        sweep_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferSweepGetResponse:
        """
        The `/transfer/sweep/get` endpoint fetches a sweep corresponding to the given `sweep_id`.

        Parameters
        ----------
        sweep_id : str
            Plaid’s unique identifier for a sweep.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferSweepGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.transfer_sweep_get(
                sweep_id="sweep_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.transfer_sweep_get(
            sweep_id=sweep_id, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def transfer_sweep_list(
        self,
        *,
        client_id: typing.Optional[ApiClientId] = OMIT,
        count: typing.Optional[int] = OMIT,
        end_date: typing.Optional[dt.datetime] = OMIT,
        funding_account_id: typing.Optional[str] = OMIT,
        offset: typing.Optional[int] = OMIT,
        originator_client_id: typing.Optional[str] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        start_date: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferSweepListResponse:
        """
        The `/transfer/sweep/list` endpoint fetches sweeps matching the given filters.

        Parameters
        ----------
        client_id : typing.Optional[ApiClientId]

        count : typing.Optional[int]
            The maximum number of sweeps to return.

        end_date : typing.Optional[dt.datetime]
            The end datetime of sweeps to return (RFC 3339 format).

        funding_account_id : typing.Optional[str]
            Filter sweeps to only those with the specified `funding_account_id`.

        offset : typing.Optional[int]
            The number of sweeps to skip before returning results.

        originator_client_id : typing.Optional[str]
            Filter sweeps to only those with the specified originator client.

        secret : typing.Optional[ApiSecret]

        start_date : typing.Optional[dt.datetime]
            The start datetime of sweeps to return (RFC 3339 format).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferSweepListResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.transfer_sweep_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.transfer_sweep_list(
            client_id=client_id,
            count=count,
            end_date=end_date,
            funding_account_id=funding_account_id,
            offset=offset,
            originator_client_id=originator_client_id,
            secret=secret,
            start_date=start_date,
            request_options=request_options,
        )
        return _response.data

    async def user_create(
        self,
        *,
        client_user_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UserCreateResponse:
        """
        This endpoint should be called for each of your end users before they begin a Plaid income flow. This provides you a single token to access all income data associated with the user. You should only create one per end user.

        If you call the endpoint multiple times with the same `client_user_id`, the first creation call will succeed and the rest will fail with an error message indicating that the user has been created for the given `client_user_id`.

        Ensure that you store the `user_token` along with your user's identifier in your database, as it is not possible to retrieve a previously created `user_token`.

        Parameters
        ----------
        client_user_id : str
            A unique ID representing the end user. Maximum of 128 characters. Typically this will be a user ID number from your application. Personally identifiable information, such as an email address or phone number, should not be used in the `client_user_id`.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserCreateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.user_create(
                client_user_id="client_user_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.user_create(
            client_user_id=client_user_id, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def wallet_create(
        self,
        *,
        iso_currency_code: WalletIsoCurrencyCode,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WalletCreateResponse:
        """
        Create an e-wallet. The response is the newly created e-wallet object.

        Parameters
        ----------
        iso_currency_code : WalletIsoCurrencyCode

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WalletCreateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.wallet_create(
                iso_currency_code="GBP",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.wallet_create(
            iso_currency_code=iso_currency_code, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def wallet_get(
        self,
        *,
        wallet_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WalletGetResponse:
        """
        Fetch an e-wallet. The response includes the current balance.

        Parameters
        ----------
        wallet_id : str
            The ID of the e-wallet

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WalletGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.wallet_get(
                wallet_id="wallet_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.wallet_get(
            wallet_id=wallet_id, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def wallet_list(
        self,
        *,
        client_id: typing.Optional[ApiClientId] = OMIT,
        count: typing.Optional[int] = OMIT,
        cursor: typing.Optional[str] = OMIT,
        iso_currency_code: typing.Optional[WalletIsoCurrencyCode] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WalletListResponse:
        """
        This endpoint lists all e-wallets in descending order of creation.

        Parameters
        ----------
        client_id : typing.Optional[ApiClientId]

        count : typing.Optional[int]
            The number of e-wallets to fetch

        cursor : typing.Optional[str]
            A base64 value representing the latest e-wallet that has already been requested. Set this to `next_cursor` received from the previous `/wallet/list` request. If provided, the response will only contain e-wallets created before that e-wallet. If omitted, the response will contain e-wallets starting from the most recent, and in descending order.

        iso_currency_code : typing.Optional[WalletIsoCurrencyCode]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WalletListResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.wallet_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.wallet_list(
            client_id=client_id,
            count=count,
            cursor=cursor,
            iso_currency_code=iso_currency_code,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def wallet_transaction_execute(
        self,
        *,
        amount: WalletTransactionAmount,
        counterparty: WalletTransactionCounterparty,
        idempotency_key: WalletTransactionIdempotencyKey,
        reference: str,
        wallet_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WalletTransactionExecuteResponse:
        """
        Execute a transaction using the specified e-wallet.
        Specify the e-wallet to debit from, the counterparty to credit to, the idempotency key to prevent duplicate transactions, the amount and reference for the transaction.
        Transactions will settle in seconds to several days, depending on the underlying payment rail.

        Parameters
        ----------
        amount : WalletTransactionAmount

        counterparty : WalletTransactionCounterparty

        idempotency_key : WalletTransactionIdempotencyKey

        reference : str
            A reference for the transaction. This must be an alphanumeric string with 6 to 18 characters and must not contain any special characters or spaces.
            Ensure that the `reference` field is unique for each transaction.

        wallet_id : str
            The ID of the e-wallet to debit from

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WalletTransactionExecuteResponse
            OK

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            WalletTransactionAmount,
            WalletTransactionCounterparty,
            WalletTransactionCounterpartyNumbers,
        )

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.wallet_transaction_execute(
                amount=WalletTransactionAmount(
                    iso_currency_code="GBP",
                    value=1.1,
                ),
                counterparty=WalletTransactionCounterparty(
                    name="name",
                    numbers=WalletTransactionCounterpartyNumbers(),
                ),
                idempotency_key="idempotency_key",
                reference="reference",
                wallet_id="wallet_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.wallet_transaction_execute(
            amount=amount,
            counterparty=counterparty,
            idempotency_key=idempotency_key,
            reference=reference,
            wallet_id=wallet_id,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def wallet_transaction_get(
        self,
        *,
        transaction_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WalletTransactionGetResponse:
        """
        Fetch a specific e-wallet transaction

        Parameters
        ----------
        transaction_id : str
            The ID of the transaction to fetch

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WalletTransactionGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.wallet_transaction_get(
                transaction_id="transaction_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.wallet_transaction_get(
            transaction_id=transaction_id, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data

    async def wallet_transaction_list(
        self,
        *,
        wallet_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        count: typing.Optional[int] = OMIT,
        cursor: typing.Optional[str] = OMIT,
        options: typing.Optional[WalletTransactionListRequestOptions] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WalletTransactionListResponse:
        """
        This endpoint lists the latest transactions of the specified e-wallet. Transactions are returned in descending order by the `created_at` time.

        Parameters
        ----------
        wallet_id : str
            The ID of the e-wallet to fetch transactions from

        client_id : typing.Optional[ApiClientId]

        count : typing.Optional[int]
            The number of transactions to fetch

        cursor : typing.Optional[str]
            A base64 value representing the latest transaction that has already been requested. Set this to `next_cursor` received from the previous `/wallet/transaction/list` request. If provided, the response will only contain transactions created before that transaction. If omitted, the response will contain transactions starting from the most recent, and in descending order by the `created_at` time.

        options : typing.Optional[WalletTransactionListRequestOptions]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WalletTransactionListResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.wallet_transaction_list(
                wallet_id="wallet_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.wallet_transaction_list(
            wallet_id=wallet_id,
            client_id=client_id,
            count=count,
            cursor=cursor,
            options=options,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def watchlist_screening_entity_create(
        self,
        *,
        search_terms: EntityWatchlistSearchTerms,
        client_id: typing.Optional[ApiClientId] = OMIT,
        client_user_id: typing.Optional[ClientUserId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WatchlistScreeningEntityCreateResponse:
        """
        Create a new entity watchlist screening to check your customer against watchlists defined in the associated entity watchlist program. If your associated program has ongoing screening enabled, this is the profile information that will be used to monitor your customer over time.

        Parameters
        ----------
        search_terms : EntityWatchlistSearchTerms

        client_id : typing.Optional[ApiClientId]

        client_user_id : typing.Optional[ClientUserId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WatchlistScreeningEntityCreateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, EntityWatchlistSearchTerms

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.watchlist_screening_entity_create(
                search_terms=EntityWatchlistSearchTerms(
                    entity_watchlist_program_id="entprg_2eRPsDnL66rZ7H",
                    legal_name="Al-Qaida",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.watchlist_screening_entity_create(
            search_terms=search_terms,
            client_id=client_id,
            client_user_id=client_user_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def watchlist_screening_entity_get(
        self,
        *,
        entity_watchlist_screening_id: EntityWatchlistScreeningId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WatchlistScreeningEntityGetResponse:
        """
        Retrieve an entity watchlist screening.

        Parameters
        ----------
        entity_watchlist_screening_id : EntityWatchlistScreeningId

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WatchlistScreeningEntityGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.watchlist_screening_entity_get(
                entity_watchlist_screening_id="entscr_52xR9LKo77r1Np",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.watchlist_screening_entity_get(
            entity_watchlist_screening_id=entity_watchlist_screening_id,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def watchlist_screening_entity_history_list(
        self,
        *,
        entity_watchlist_screening_id: EntityWatchlistScreeningId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        cursor: typing.Optional[Cursor] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WatchlistScreeningEntityHistoryListResponse:
        """
        List all changes to the entity watchlist screening in reverse-chronological order. If the watchlist screening has not been edited, no history will be returned.

        Parameters
        ----------
        entity_watchlist_screening_id : EntityWatchlistScreeningId

        client_id : typing.Optional[ApiClientId]

        cursor : typing.Optional[Cursor]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WatchlistScreeningEntityHistoryListResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.watchlist_screening_entity_history_list(
                entity_watchlist_screening_id="entscr_52xR9LKo77r1Np",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.watchlist_screening_entity_history_list(
            entity_watchlist_screening_id=entity_watchlist_screening_id,
            client_id=client_id,
            cursor=cursor,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def watchlist_screening_entity_hit_list(
        self,
        *,
        entity_watchlist_screening_id: EntityWatchlistScreeningId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        cursor: typing.Optional[Cursor] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WatchlistScreeningEntityHitListResponse:
        """
        List all hits for the entity watchlist screening.

        Parameters
        ----------
        entity_watchlist_screening_id : EntityWatchlistScreeningId

        client_id : typing.Optional[ApiClientId]

        cursor : typing.Optional[Cursor]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WatchlistScreeningEntityHitListResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.watchlist_screening_entity_hit_list(
                entity_watchlist_screening_id="entscr_52xR9LKo77r1Np",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.watchlist_screening_entity_hit_list(
            entity_watchlist_screening_id=entity_watchlist_screening_id,
            client_id=client_id,
            cursor=cursor,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def watchlist_screening_entity_list(
        self,
        *,
        entity_watchlist_program_id: EntityWatchlistProgramId,
        assignee: typing.Optional[DashboardUserId] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        client_user_id: typing.Optional[ClientUserId] = OMIT,
        cursor: typing.Optional[Cursor] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        status: typing.Optional[WatchlistScreeningStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WatchlistScreeningEntityListResponse:
        """
        List all entity screenings.

        Parameters
        ----------
        entity_watchlist_program_id : EntityWatchlistProgramId

        assignee : typing.Optional[DashboardUserId]

        client_id : typing.Optional[ApiClientId]

        client_user_id : typing.Optional[ClientUserId]

        cursor : typing.Optional[Cursor]

        secret : typing.Optional[ApiSecret]

        status : typing.Optional[WatchlistScreeningStatus]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WatchlistScreeningEntityListResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.watchlist_screening_entity_list(
                entity_watchlist_program_id="entprg_2eRPsDnL66rZ7H",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.watchlist_screening_entity_list(
            entity_watchlist_program_id=entity_watchlist_program_id,
            assignee=assignee,
            client_id=client_id,
            client_user_id=client_user_id,
            cursor=cursor,
            secret=secret,
            status=status,
            request_options=request_options,
        )
        return _response.data

    async def watchlist_screening_entity_program_get(
        self,
        *,
        entity_watchlist_program_id: EntityWatchlistProgramId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WatchlistScreeningEntityProgramGetResponse:
        """
        Get an entity watchlist screening program

        Parameters
        ----------
        entity_watchlist_program_id : EntityWatchlistProgramId

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WatchlistScreeningEntityProgramGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.watchlist_screening_entity_program_get(
                entity_watchlist_program_id="entprg_2eRPsDnL66rZ7H",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.watchlist_screening_entity_program_get(
            entity_watchlist_program_id=entity_watchlist_program_id,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def watchlist_screening_entity_program_list(
        self,
        *,
        client_id: typing.Optional[ApiClientId] = OMIT,
        cursor: typing.Optional[Cursor] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WatchlistScreeningEntityProgramListResponse:
        """
        List all entity watchlist screening programs

        Parameters
        ----------
        client_id : typing.Optional[ApiClientId]

        cursor : typing.Optional[Cursor]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WatchlistScreeningEntityProgramListResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.watchlist_screening_entity_program_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.watchlist_screening_entity_program_list(
            client_id=client_id, cursor=cursor, secret=secret, request_options=request_options
        )
        return _response.data

    async def watchlist_screening_entity_review_create(
        self,
        *,
        confirmed_hits: typing.Sequence[EntityWatchlistScreeningHitId],
        dismissed_hits: typing.Sequence[EntityWatchlistScreeningHitId],
        entity_watchlist_screening_id: EntityWatchlistScreeningId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        comment: typing.Optional[ReviewComment] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WatchlistScreeningEntityReviewCreateResponse:
        """
        Create a review for an entity watchlist screening. Reviews are compliance reports created by users in your organization regarding the relevance of potential hits found by Plaid.

        Parameters
        ----------
        confirmed_hits : typing.Sequence[EntityWatchlistScreeningHitId]
            Hits to mark as a true positive after thorough manual review. These hits will never recur or be updated once dismissed. In most cases, confirmed hits indicate that the customer should be rejected.

        dismissed_hits : typing.Sequence[EntityWatchlistScreeningHitId]
            Hits to mark as a false positive after thorough manual review. These hits will never recur or be updated once dismissed.

        entity_watchlist_screening_id : EntityWatchlistScreeningId

        client_id : typing.Optional[ApiClientId]

        comment : typing.Optional[ReviewComment]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WatchlistScreeningEntityReviewCreateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.watchlist_screening_entity_review_create(
                confirmed_hits=["enthit_52xR9LKo77r1Np"],
                dismissed_hits=["enthit_52xR9LKo77r1Np"],
                entity_watchlist_screening_id="entscr_52xR9LKo77r1Np",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.watchlist_screening_entity_review_create(
            confirmed_hits=confirmed_hits,
            dismissed_hits=dismissed_hits,
            entity_watchlist_screening_id=entity_watchlist_screening_id,
            client_id=client_id,
            comment=comment,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def watchlist_screening_entity_review_list(
        self,
        *,
        entity_watchlist_screening_id: EntityWatchlistScreeningId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        cursor: typing.Optional[Cursor] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WatchlistScreeningEntityReviewListResponse:
        """
        List all reviews for a particular entity watchlist screening. Reviews are compliance reports created by users in your organization regarding the relevance of potential hits found by Plaid.

        Parameters
        ----------
        entity_watchlist_screening_id : EntityWatchlistScreeningId

        client_id : typing.Optional[ApiClientId]

        cursor : typing.Optional[Cursor]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WatchlistScreeningEntityReviewListResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.watchlist_screening_entity_review_list(
                entity_watchlist_screening_id="entscr_52xR9LKo77r1Np",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.watchlist_screening_entity_review_list(
            entity_watchlist_screening_id=entity_watchlist_screening_id,
            client_id=client_id,
            cursor=cursor,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def watchlist_screening_entity_update(
        self,
        *,
        entity_watchlist_screening_id: EntityWatchlistScreeningId,
        assignee: typing.Optional[DashboardUserId] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        client_user_id: typing.Optional[ClientUserId] = OMIT,
        reset_fields: typing.Optional[WatchlistScreeningEntityUpdateRequestResettableFieldList] = OMIT,
        search_terms: typing.Optional[UpdateEntityScreeningRequestSearchTerms] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        status: typing.Optional[WatchlistScreeningStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WatchlistScreeningEntityUpdateResponse:
        """
        Update an entity watchlist screening.

        Parameters
        ----------
        entity_watchlist_screening_id : EntityWatchlistScreeningId

        assignee : typing.Optional[DashboardUserId]

        client_id : typing.Optional[ApiClientId]

        client_user_id : typing.Optional[ClientUserId]

        reset_fields : typing.Optional[WatchlistScreeningEntityUpdateRequestResettableFieldList]

        search_terms : typing.Optional[UpdateEntityScreeningRequestSearchTerms]

        secret : typing.Optional[ApiSecret]

        status : typing.Optional[WatchlistScreeningStatus]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WatchlistScreeningEntityUpdateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.watchlist_screening_entity_update(
                entity_watchlist_screening_id="entscr_52xR9LKo77r1Np",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.watchlist_screening_entity_update(
            entity_watchlist_screening_id=entity_watchlist_screening_id,
            assignee=assignee,
            client_id=client_id,
            client_user_id=client_user_id,
            reset_fields=reset_fields,
            search_terms=search_terms,
            secret=secret,
            status=status,
            request_options=request_options,
        )
        return _response.data

    async def watchlist_screening_individual_create(
        self,
        *,
        search_terms: WatchlistScreeningRequestSearchTerms,
        client_id: typing.Optional[ApiClientId] = OMIT,
        client_user_id: typing.Optional[ClientUserId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WatchlistScreeningIndividualCreateResponse:
        """
        Create a new Watchlist Screening to check your customer against watchlists defined in the associated Watchlist Program. If your associated program has ongoing screening enabled, this is the profile information that will be used to monitor your customer over time.

        Parameters
        ----------
        search_terms : WatchlistScreeningRequestSearchTerms

        client_id : typing.Optional[ApiClientId]

        client_user_id : typing.Optional[ClientUserId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WatchlistScreeningIndividualCreateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, WatchlistScreeningRequestSearchTerms

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.watchlist_screening_individual_create(
                search_terms=WatchlistScreeningRequestSearchTerms(
                    legal_name="Aleksey Potemkin",
                    watchlist_program_id="prg_2eRPsDnL66rZ7H",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.watchlist_screening_individual_create(
            search_terms=search_terms,
            client_id=client_id,
            client_user_id=client_user_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def watchlist_screening_individual_get(
        self,
        *,
        watchlist_screening_id: WatchlistScreeningIndividualId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WatchlistScreeningIndividualGetResponse:
        """
        Retrieve a previously created individual watchlist screening

        Parameters
        ----------
        watchlist_screening_id : WatchlistScreeningIndividualId

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WatchlistScreeningIndividualGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.watchlist_screening_individual_get(
                watchlist_screening_id="scr_52xR9LKo77r1Np",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.watchlist_screening_individual_get(
            watchlist_screening_id=watchlist_screening_id,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def watchlist_screening_individual_history_list(
        self,
        *,
        watchlist_screening_id: WatchlistScreeningIndividualId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        cursor: typing.Optional[Cursor] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WatchlistScreeningIndividualHistoryListResponse:
        """
        List all changes to the individual watchlist screening in reverse-chronological order. If the watchlist screening has not been edited, no history will be returned.

        Parameters
        ----------
        watchlist_screening_id : WatchlistScreeningIndividualId

        client_id : typing.Optional[ApiClientId]

        cursor : typing.Optional[Cursor]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WatchlistScreeningIndividualHistoryListResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.watchlist_screening_individual_history_list(
                watchlist_screening_id="scr_52xR9LKo77r1Np",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.watchlist_screening_individual_history_list(
            watchlist_screening_id=watchlist_screening_id,
            client_id=client_id,
            cursor=cursor,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def watchlist_screening_individual_hit_list(
        self,
        *,
        watchlist_screening_id: WatchlistScreeningIndividualId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        cursor: typing.Optional[Cursor] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WatchlistScreeningIndividualHitListResponse:
        """
        List all hits found by Plaid for a particular individual watchlist screening.

        Parameters
        ----------
        watchlist_screening_id : WatchlistScreeningIndividualId

        client_id : typing.Optional[ApiClientId]

        cursor : typing.Optional[Cursor]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WatchlistScreeningIndividualHitListResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.watchlist_screening_individual_hit_list(
                watchlist_screening_id="scr_52xR9LKo77r1Np",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.watchlist_screening_individual_hit_list(
            watchlist_screening_id=watchlist_screening_id,
            client_id=client_id,
            cursor=cursor,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def watchlist_screening_individual_list(
        self,
        *,
        watchlist_program_id: WatchlistProgramId,
        assignee: typing.Optional[DashboardUserId] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        client_user_id: typing.Optional[ClientUserId] = OMIT,
        cursor: typing.Optional[Cursor] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        status: typing.Optional[WatchlistScreeningStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WatchlistScreeningIndividualListResponse:
        """
        List previously created watchlist screenings for individuals

        Parameters
        ----------
        watchlist_program_id : WatchlistProgramId

        assignee : typing.Optional[DashboardUserId]

        client_id : typing.Optional[ApiClientId]

        client_user_id : typing.Optional[ClientUserId]

        cursor : typing.Optional[Cursor]

        secret : typing.Optional[ApiSecret]

        status : typing.Optional[WatchlistScreeningStatus]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WatchlistScreeningIndividualListResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.watchlist_screening_individual_list(
                watchlist_program_id="prg_2eRPsDnL66rZ7H",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.watchlist_screening_individual_list(
            watchlist_program_id=watchlist_program_id,
            assignee=assignee,
            client_id=client_id,
            client_user_id=client_user_id,
            cursor=cursor,
            secret=secret,
            status=status,
            request_options=request_options,
        )
        return _response.data

    async def watchlist_screening_individual_program_get(
        self,
        *,
        watchlist_program_id: WatchlistProgramId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WatchlistScreeningIndividualProgramGetResponse:
        """
        Get an individual watchlist screening program

        Parameters
        ----------
        watchlist_program_id : WatchlistProgramId

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WatchlistScreeningIndividualProgramGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.watchlist_screening_individual_program_get(
                watchlist_program_id="prg_2eRPsDnL66rZ7H",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.watchlist_screening_individual_program_get(
            watchlist_program_id=watchlist_program_id,
            client_id=client_id,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def watchlist_screening_individual_program_list(
        self,
        *,
        client_id: typing.Optional[ApiClientId] = OMIT,
        cursor: typing.Optional[Cursor] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WatchlistScreeningIndividualProgramListResponse:
        """
        List all individual watchlist screening programs

        Parameters
        ----------
        client_id : typing.Optional[ApiClientId]

        cursor : typing.Optional[Cursor]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WatchlistScreeningIndividualProgramListResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.watchlist_screening_individual_program_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.watchlist_screening_individual_program_list(
            client_id=client_id, cursor=cursor, secret=secret, request_options=request_options
        )
        return _response.data

    async def watchlist_screening_individual_review_create(
        self,
        *,
        confirmed_hits: typing.Sequence[WatchlistScreeningHitId],
        dismissed_hits: typing.Sequence[WatchlistScreeningHitId],
        watchlist_screening_id: WatchlistScreeningIndividualId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        comment: typing.Optional[ReviewComment] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WatchlistScreeningIndividualReviewCreateResponse:
        """
        Create a review for the individual watchlist screening. Reviews are compliance reports created by users in your organization regarding the relevance of potential hits found by Plaid.

        Parameters
        ----------
        confirmed_hits : typing.Sequence[WatchlistScreeningHitId]
            Hits to mark as a true positive after thorough manual review. These hits will never recur or be updated once dismissed. In most cases, confirmed hits indicate that the customer should be rejected.

        dismissed_hits : typing.Sequence[WatchlistScreeningHitId]
            Hits to mark as a false positive after thorough manual review. These hits will never recur or be updated once dismissed.

        watchlist_screening_id : WatchlistScreeningIndividualId

        client_id : typing.Optional[ApiClientId]

        comment : typing.Optional[ReviewComment]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WatchlistScreeningIndividualReviewCreateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.watchlist_screening_individual_review_create(
                confirmed_hits=["scrhit_52xR9LKo77r1Np"],
                dismissed_hits=["scrhit_52xR9LKo77r1Np"],
                watchlist_screening_id="scr_52xR9LKo77r1Np",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.watchlist_screening_individual_review_create(
            confirmed_hits=confirmed_hits,
            dismissed_hits=dismissed_hits,
            watchlist_screening_id=watchlist_screening_id,
            client_id=client_id,
            comment=comment,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def watchlist_screening_individual_review_list(
        self,
        *,
        watchlist_screening_id: WatchlistScreeningIndividualId,
        client_id: typing.Optional[ApiClientId] = OMIT,
        cursor: typing.Optional[Cursor] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WatchlistScreeningIndividualReviewListResponse:
        """
        List all reviews for the individual watchlist screening.

        Parameters
        ----------
        watchlist_screening_id : WatchlistScreeningIndividualId

        client_id : typing.Optional[ApiClientId]

        cursor : typing.Optional[Cursor]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WatchlistScreeningIndividualReviewListResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.watchlist_screening_individual_review_list(
                watchlist_screening_id="scr_52xR9LKo77r1Np",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.watchlist_screening_individual_review_list(
            watchlist_screening_id=watchlist_screening_id,
            client_id=client_id,
            cursor=cursor,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def watchlist_screening_individual_update(
        self,
        *,
        watchlist_screening_id: WatchlistScreeningIndividualId,
        assignee: typing.Optional[DashboardUserId] = OMIT,
        client_id: typing.Optional[ApiClientId] = OMIT,
        client_user_id: typing.Optional[ClientUserId] = OMIT,
        reset_fields: typing.Optional[WatchlistScreeningIndividualUpdateRequestResettableFieldList] = OMIT,
        search_terms: typing.Optional[UpdateIndividualScreeningRequestSearchTerms] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        status: typing.Optional[WatchlistScreeningStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WatchlistScreeningIndividualUpdateResponse:
        """
        Update a specific individual watchlist screening. This endpoint can be used to add additional customer information, correct outdated information, add a reference id, assign the individual to a reviewer, and update which program it is associated with. Please note that you may not update `search_terms` and `status` at the same time since editing `search_terms` may trigger an automatic `status` change.

        Parameters
        ----------
        watchlist_screening_id : WatchlistScreeningIndividualId

        assignee : typing.Optional[DashboardUserId]

        client_id : typing.Optional[ApiClientId]

        client_user_id : typing.Optional[ClientUserId]

        reset_fields : typing.Optional[WatchlistScreeningIndividualUpdateRequestResettableFieldList]

        search_terms : typing.Optional[UpdateIndividualScreeningRequestSearchTerms]

        secret : typing.Optional[ApiSecret]

        status : typing.Optional[WatchlistScreeningStatus]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WatchlistScreeningIndividualUpdateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.watchlist_screening_individual_update(
                watchlist_screening_id="scr_52xR9LKo77r1Np",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.watchlist_screening_individual_update(
            watchlist_screening_id=watchlist_screening_id,
            assignee=assignee,
            client_id=client_id,
            client_user_id=client_user_id,
            reset_fields=reset_fields,
            search_terms=search_terms,
            secret=secret,
            status=status,
            request_options=request_options,
        )
        return _response.data

    async def webhook_verification_key_get(
        self,
        *,
        key_id: str,
        client_id: typing.Optional[ApiClientId] = OMIT,
        secret: typing.Optional[ApiSecret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebhookVerificationKeyGetResponse:
        """
        Plaid signs all outgoing webhooks and provides JSON Web Tokens (JWTs) so that you can verify the authenticity of any incoming webhooks to your application. A message signature is included in the `Plaid-Verification` header.

        The `/webhook_verification_key/get` endpoint provides a JSON Web Key (JWK) that can be used to verify a JWT.

        Parameters
        ----------
        key_id : str
            The key ID ( `kid` ) from the JWT header.

        client_id : typing.Optional[ApiClientId]

        secret : typing.Optional[ApiSecret]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookVerificationKeyGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            plaid_version="YOUR_PLAID_VERSION",
            plaid_secret="YOUR_PLAID_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.plaid.webhook_verification_key_get(
                key_id="key_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.webhook_verification_key_get(
            key_id=key_id, client_id=client_id, secret=secret, request_options=request_options
        )
        return _response.data
