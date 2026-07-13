



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .additional_information import AdditionalInformation
    from .address import Address
    from .amount import Amount
    from .attachment import Attachment
    from .attachment_conversation_content_listing import AttachmentConversationContentListing
    from .attachment_master_card_action_refund import AttachmentMasterCardActionRefund
    from .attachment_monetary_account import AttachmentMonetaryAccount
    from .attachment_monetary_account_content_listing import AttachmentMonetaryAccountContentListing
    from .attachment_monetary_account_create import AttachmentMonetaryAccountCreate
    from .attachment_monetary_account_payment import AttachmentMonetaryAccountPayment
    from .attachment_public import AttachmentPublic
    from .attachment_public_content_listing import AttachmentPublicContentListing
    from .attachment_public_create import AttachmentPublicCreate
    from .attachment_public_read import AttachmentPublicRead
    from .attachment_url import AttachmentUrl
    from .attachment_user_content_listing import AttachmentUserContentListing
    from .attachment_user_read import AttachmentUserRead
    from .avatar import Avatar
    from .avatar_create import AvatarCreate
    from .avatar_read import AvatarRead
    from .bad_request_error_body import BadRequestErrorBody
    from .bank_switch_service_netherlands_incoming import BankSwitchServiceNetherlandsIncoming
    from .bank_switch_service_netherlands_incoming_payment import BankSwitchServiceNetherlandsIncomingPayment
    from .bank_switch_service_netherlands_incoming_payment_read import BankSwitchServiceNetherlandsIncomingPaymentRead
    from .billing_contract_subscription import BillingContractSubscription
    from .billing_contract_subscription_listing import BillingContractSubscriptionListing
    from .birdee_investment_portfolio import BirdeeInvestmentPortfolio
    from .birdee_investment_portfolio_balance import BirdeeInvestmentPortfolioBalance
    from .birdee_investment_portfolio_goal import BirdeeInvestmentPortfolioGoal
    from .birdee_portfolio_allocation import BirdeePortfolioAllocation
    from .bunq_id import BunqId
    from .bunq_me_fundraiser_profile import BunqMeFundraiserProfile
    from .bunq_me_fundraiser_profile_user_listing import BunqMeFundraiserProfileUserListing
    from .bunq_me_fundraiser_profile_user_read import BunqMeFundraiserProfileUserRead
    from .bunq_me_fundraiser_result import BunqMeFundraiserResult
    from .bunq_me_fundraiser_result_read import BunqMeFundraiserResultRead
    from .bunq_me_merchant_available import BunqMeMerchantAvailable
    from .bunq_me_tab import BunqMeTab
    from .bunq_me_tab_create import BunqMeTabCreate
    from .bunq_me_tab_entry import BunqMeTabEntry
    from .bunq_me_tab_listing import BunqMeTabListing
    from .bunq_me_tab_read import BunqMeTabRead
    from .bunq_me_tab_result_inquiry import BunqMeTabResultInquiry
    from .bunq_me_tab_result_response import BunqMeTabResultResponse
    from .bunq_me_tab_result_response_read import BunqMeTabResultResponseRead
    from .bunq_me_tab_update import BunqMeTabUpdate
    from .card import Card
    from .card_batch_create import CardBatchCreate
    from .card_batch_entry import CardBatchEntry
    from .card_batch_replace_create import CardBatchReplaceCreate
    from .card_batch_replace_entry import CardBatchReplaceEntry
    from .card_country_permission import CardCountryPermission
    from .card_credit_create import CardCreditCreate
    from .card_debit import CardDebit
    from .card_debit_create import CardDebitCreate
    from .card_generated_cvc2 import CardGeneratedCvc2
    from .card_generated_cvc2create import CardGeneratedCvc2Create
    from .card_generated_cvc2listing import CardGeneratedCvc2Listing
    from .card_generated_cvc2read import CardGeneratedCvc2Read
    from .card_generated_cvc2update import CardGeneratedCvc2Update
    from .card_listing import CardListing
    from .card_name_listing import CardNameListing
    from .card_pin_assignment import CardPinAssignment
    from .card_primary_account_number import CardPrimaryAccountNumber
    from .card_read import CardRead
    from .card_replace_create import CardReplaceCreate
    from .card_update import CardUpdate
    from .certificate import Certificate
    from .certificate_pinned_create import CertificatePinnedCreate
    from .certificate_pinned_delete import CertificatePinnedDelete
    from .certificate_pinned_listing import CertificatePinnedListing
    from .certificate_pinned_read import CertificatePinnedRead
    from .co_owner import CoOwner
    from .company import Company
    from .company_create import CompanyCreate
    from .company_listing import CompanyListing
    from .company_read import CompanyRead
    from .company_update import CompanyUpdate
    from .company_vat_number import CompanyVatNumber
    from .confirmation_of_funds_create import ConfirmationOfFundsCreate
    from .currency_cloud_beneficiary_create import CurrencyCloudBeneficiaryCreate
    from .currency_cloud_beneficiary_listing import CurrencyCloudBeneficiaryListing
    from .currency_cloud_beneficiary_read import CurrencyCloudBeneficiaryRead
    from .currency_cloud_beneficiary_requirement_field import CurrencyCloudBeneficiaryRequirementField
    from .currency_cloud_beneficiary_requirement_listing import CurrencyCloudBeneficiaryRequirementListing
    from .currency_cloud_payment_quote_create import CurrencyCloudPaymentQuoteCreate
    from .currency_conversion_listing import CurrencyConversionListing
    from .currency_conversion_quote import CurrencyConversionQuote
    from .currency_conversion_quote_create import CurrencyConversionQuoteCreate
    from .currency_conversion_quote_read import CurrencyConversionQuoteRead
    from .currency_conversion_quote_update import CurrencyConversionQuoteUpdate
    from .currency_conversion_read import CurrencyConversionRead
    from .customer import Customer
    from .customer_limit import CustomerLimit
    from .customer_limit_listing import CustomerLimitListing
    from .device_listing import DeviceListing
    from .device_read import DeviceRead
    from .device_server import DeviceServer
    from .device_server_create import DeviceServerCreate
    from .device_server_listing import DeviceServerListing
    from .device_server_read import DeviceServerRead
    from .draft_payment import DraftPayment
    from .draft_payment_anchor_object import DraftPaymentAnchorObject
    from .draft_payment_create import DraftPaymentCreate
    from .draft_payment_entry import DraftPaymentEntry
    from .draft_payment_listing import DraftPaymentListing
    from .draft_payment_read import DraftPaymentRead
    from .draft_payment_response import DraftPaymentResponse
    from .draft_payment_update import DraftPaymentUpdate
    from .error import Error
    from .error_item import ErrorItem
    from .event_listing import EventListing
    from .event_object import EventObject
    from .event_read import EventRead
    from .export_annual_overview_content_listing import ExportAnnualOverviewContentListing
    from .export_annual_overview_create import ExportAnnualOverviewCreate
    from .export_annual_overview_delete import ExportAnnualOverviewDelete
    from .export_annual_overview_listing import ExportAnnualOverviewListing
    from .export_annual_overview_read import ExportAnnualOverviewRead
    from .export_rib import ExportRib
    from .export_rib_content_listing import ExportRibContentListing
    from .export_rib_create import ExportRibCreate
    from .export_rib_delete import ExportRibDelete
    from .export_rib_listing import ExportRibListing
    from .export_rib_read import ExportRibRead
    from .export_statement_card_content_listing import ExportStatementCardContentListing
    from .export_statement_card_csv_create import ExportStatementCardCsvCreate
    from .export_statement_card_csv_delete import ExportStatementCardCsvDelete
    from .export_statement_card_csv_listing import ExportStatementCardCsvListing
    from .export_statement_card_csv_read import ExportStatementCardCsvRead
    from .export_statement_card_listing import ExportStatementCardListing
    from .export_statement_card_pdf_create import ExportStatementCardPdfCreate
    from .export_statement_card_pdf_delete import ExportStatementCardPdfDelete
    from .export_statement_card_pdf_listing import ExportStatementCardPdfListing
    from .export_statement_card_pdf_read import ExportStatementCardPdfRead
    from .export_statement_card_read import ExportStatementCardRead
    from .export_statement_content_listing import ExportStatementContentListing
    from .export_statement_create import ExportStatementCreate
    from .export_statement_delete import ExportStatementDelete
    from .export_statement_listing import ExportStatementListing
    from .export_statement_payment import ExportStatementPayment
    from .export_statement_payment_content_listing import ExportStatementPaymentContentListing
    from .export_statement_payment_create import ExportStatementPaymentCreate
    from .export_statement_payment_read import ExportStatementPaymentRead
    from .export_statement_read import ExportStatementRead
    from .feature_announcement import FeatureAnnouncement
    from .feature_announcement_read import FeatureAnnouncementRead
    from .geolocation import Geolocation
    from .ideal_merchant_transaction import IdealMerchantTransaction
    from .ideal_merchant_transaction_create import IdealMerchantTransactionCreate
    from .ideal_merchant_transaction_listing import IdealMerchantTransactionListing
    from .ideal_merchant_transaction_read import IdealMerchantTransactionRead
    from .image import Image
    from .insight_event_listing import InsightEventListing
    from .insight_listing import InsightListing
    from .insight_preference_date_listing import InsightPreferenceDateListing
    from .installation_create import InstallationCreate
    from .installation_listing import InstallationListing
    from .installation_read import InstallationRead
    from .installation_server_public_key import InstallationServerPublicKey
    from .installation_server_public_key_listing import InstallationServerPublicKeyListing
    from .installation_token import InstallationToken
    from .invoice import Invoice
    from .invoice_by_user_listing import InvoiceByUserListing
    from .invoice_by_user_read import InvoiceByUserRead
    from .invoice_export_pdf_content_listing import InvoiceExportPdfContentListing
    from .invoice_item import InvoiceItem
    from .invoice_item_group import InvoiceItemGroup
    from .invoice_listing import InvoiceListing
    from .invoice_read import InvoiceRead
    from .issuer import Issuer
    from .label_card import LabelCard
    from .label_monetary_account import LabelMonetaryAccount
    from .label_user import LabelUser
    from .master_card_action import MasterCardAction
    from .master_card_action_listing import MasterCardActionListing
    from .master_card_action_read import MasterCardActionRead
    from .master_card_action_reference import MasterCardActionReference
    from .master_card_action_refund import MasterCardActionRefund
    from .master_card_identity_check_challenge_request_user_read import MasterCardIdentityCheckChallengeRequestUserRead
    from .master_card_identity_check_challenge_request_user_update import (
        MasterCardIdentityCheckChallengeRequestUserUpdate,
    )
    from .master_card_payment_listing import MasterCardPaymentListing
    from .monetary_account_bank import MonetaryAccountBank
    from .monetary_account_bank_create import MonetaryAccountBankCreate
    from .monetary_account_bank_listing import MonetaryAccountBankListing
    from .monetary_account_bank_read import MonetaryAccountBankRead
    from .monetary_account_bank_update import MonetaryAccountBankUpdate
    from .monetary_account_external import MonetaryAccountExternal
    from .monetary_account_external_listing import MonetaryAccountExternalListing
    from .monetary_account_external_read import MonetaryAccountExternalRead
    from .monetary_account_investment import MonetaryAccountInvestment
    from .monetary_account_joint import MonetaryAccountJoint
    from .monetary_account_joint_create import MonetaryAccountJointCreate
    from .monetary_account_joint_listing import MonetaryAccountJointListing
    from .monetary_account_joint_read import MonetaryAccountJointRead
    from .monetary_account_joint_update import MonetaryAccountJointUpdate
    from .monetary_account_light import MonetaryAccountLight
    from .monetary_account_listing import MonetaryAccountListing
    from .monetary_account_profile import MonetaryAccountProfile
    from .monetary_account_profile_drain import MonetaryAccountProfileDrain
    from .monetary_account_profile_fill import MonetaryAccountProfileFill
    from .monetary_account_read import MonetaryAccountRead
    from .monetary_account_savings import MonetaryAccountSavings
    from .monetary_account_savings_create import MonetaryAccountSavingsCreate
    from .monetary_account_savings_listing import MonetaryAccountSavingsListing
    from .monetary_account_savings_read import MonetaryAccountSavingsRead
    from .monetary_account_savings_update import MonetaryAccountSavingsUpdate
    from .monetary_account_setting import MonetaryAccountSetting
    from .note_attachment_bank_switch_service_netherlands_incoming_payment import (
        NoteAttachmentBankSwitchServiceNetherlandsIncomingPayment,
    )
    from .note_attachment_bank_switch_service_netherlands_incoming_payment_create import (
        NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentCreate,
    )
    from .note_attachment_bank_switch_service_netherlands_incoming_payment_delete import (
        NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentDelete,
    )
    from .note_attachment_bank_switch_service_netherlands_incoming_payment_listing import (
        NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentListing,
    )
    from .note_attachment_bank_switch_service_netherlands_incoming_payment_read import (
        NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentRead,
    )
    from .note_attachment_bank_switch_service_netherlands_incoming_payment_update import (
        NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentUpdate,
    )
    from .note_attachment_bunq_me_fundraiser_result import NoteAttachmentBunqMeFundraiserResult
    from .note_attachment_bunq_me_fundraiser_result_create import NoteAttachmentBunqMeFundraiserResultCreate
    from .note_attachment_bunq_me_fundraiser_result_delete import NoteAttachmentBunqMeFundraiserResultDelete
    from .note_attachment_bunq_me_fundraiser_result_listing import NoteAttachmentBunqMeFundraiserResultListing
    from .note_attachment_bunq_me_fundraiser_result_read import NoteAttachmentBunqMeFundraiserResultRead
    from .note_attachment_bunq_me_fundraiser_result_update import NoteAttachmentBunqMeFundraiserResultUpdate
    from .note_attachment_draft_payment import NoteAttachmentDraftPayment
    from .note_attachment_draft_payment_create import NoteAttachmentDraftPaymentCreate
    from .note_attachment_draft_payment_delete import NoteAttachmentDraftPaymentDelete
    from .note_attachment_draft_payment_listing import NoteAttachmentDraftPaymentListing
    from .note_attachment_draft_payment_read import NoteAttachmentDraftPaymentRead
    from .note_attachment_draft_payment_update import NoteAttachmentDraftPaymentUpdate
    from .note_attachment_ideal_merchant_transaction import NoteAttachmentIdealMerchantTransaction
    from .note_attachment_ideal_merchant_transaction_create import NoteAttachmentIdealMerchantTransactionCreate
    from .note_attachment_ideal_merchant_transaction_delete import NoteAttachmentIdealMerchantTransactionDelete
    from .note_attachment_ideal_merchant_transaction_listing import NoteAttachmentIdealMerchantTransactionListing
    from .note_attachment_ideal_merchant_transaction_read import NoteAttachmentIdealMerchantTransactionRead
    from .note_attachment_ideal_merchant_transaction_update import NoteAttachmentIdealMerchantTransactionUpdate
    from .note_attachment_master_card_action import NoteAttachmentMasterCardAction
    from .note_attachment_master_card_action_create import NoteAttachmentMasterCardActionCreate
    from .note_attachment_master_card_action_delete import NoteAttachmentMasterCardActionDelete
    from .note_attachment_master_card_action_listing import NoteAttachmentMasterCardActionListing
    from .note_attachment_master_card_action_read import NoteAttachmentMasterCardActionRead
    from .note_attachment_master_card_action_update import NoteAttachmentMasterCardActionUpdate
    from .note_attachment_payment import NoteAttachmentPayment
    from .note_attachment_payment_batch import NoteAttachmentPaymentBatch
    from .note_attachment_payment_batch_create import NoteAttachmentPaymentBatchCreate
    from .note_attachment_payment_batch_delete import NoteAttachmentPaymentBatchDelete
    from .note_attachment_payment_batch_listing import NoteAttachmentPaymentBatchListing
    from .note_attachment_payment_batch_read import NoteAttachmentPaymentBatchRead
    from .note_attachment_payment_batch_update import NoteAttachmentPaymentBatchUpdate
    from .note_attachment_payment_create import NoteAttachmentPaymentCreate
    from .note_attachment_payment_delete import NoteAttachmentPaymentDelete
    from .note_attachment_payment_listing import NoteAttachmentPaymentListing
    from .note_attachment_payment_read import NoteAttachmentPaymentRead
    from .note_attachment_payment_update import NoteAttachmentPaymentUpdate
    from .note_attachment_request_inquiry import NoteAttachmentRequestInquiry
    from .note_attachment_request_inquiry_batch import NoteAttachmentRequestInquiryBatch
    from .note_attachment_request_inquiry_batch_create import NoteAttachmentRequestInquiryBatchCreate
    from .note_attachment_request_inquiry_batch_delete import NoteAttachmentRequestInquiryBatchDelete
    from .note_attachment_request_inquiry_batch_listing import NoteAttachmentRequestInquiryBatchListing
    from .note_attachment_request_inquiry_batch_read import NoteAttachmentRequestInquiryBatchRead
    from .note_attachment_request_inquiry_batch_update import NoteAttachmentRequestInquiryBatchUpdate
    from .note_attachment_request_inquiry_create import NoteAttachmentRequestInquiryCreate
    from .note_attachment_request_inquiry_delete import NoteAttachmentRequestInquiryDelete
    from .note_attachment_request_inquiry_listing import NoteAttachmentRequestInquiryListing
    from .note_attachment_request_inquiry_read import NoteAttachmentRequestInquiryRead
    from .note_attachment_request_inquiry_update import NoteAttachmentRequestInquiryUpdate
    from .note_attachment_request_response import NoteAttachmentRequestResponse
    from .note_attachment_request_response_create import NoteAttachmentRequestResponseCreate
    from .note_attachment_request_response_delete import NoteAttachmentRequestResponseDelete
    from .note_attachment_request_response_listing import NoteAttachmentRequestResponseListing
    from .note_attachment_request_response_read import NoteAttachmentRequestResponseRead
    from .note_attachment_request_response_update import NoteAttachmentRequestResponseUpdate
    from .note_attachment_schedule_instance import NoteAttachmentScheduleInstance
    from .note_attachment_schedule_instance_create import NoteAttachmentScheduleInstanceCreate
    from .note_attachment_schedule_instance_delete import NoteAttachmentScheduleInstanceDelete
    from .note_attachment_schedule_instance_listing import NoteAttachmentScheduleInstanceListing
    from .note_attachment_schedule_instance_read import NoteAttachmentScheduleInstanceRead
    from .note_attachment_schedule_instance_update import NoteAttachmentScheduleInstanceUpdate
    from .note_attachment_schedule_payment import NoteAttachmentSchedulePayment
    from .note_attachment_schedule_payment_batch import NoteAttachmentSchedulePaymentBatch
    from .note_attachment_schedule_payment_batch_create import NoteAttachmentSchedulePaymentBatchCreate
    from .note_attachment_schedule_payment_batch_delete import NoteAttachmentSchedulePaymentBatchDelete
    from .note_attachment_schedule_payment_batch_listing import NoteAttachmentSchedulePaymentBatchListing
    from .note_attachment_schedule_payment_batch_read import NoteAttachmentSchedulePaymentBatchRead
    from .note_attachment_schedule_payment_batch_update import NoteAttachmentSchedulePaymentBatchUpdate
    from .note_attachment_schedule_payment_create import NoteAttachmentSchedulePaymentCreate
    from .note_attachment_schedule_payment_delete import NoteAttachmentSchedulePaymentDelete
    from .note_attachment_schedule_payment_listing import NoteAttachmentSchedulePaymentListing
    from .note_attachment_schedule_payment_read import NoteAttachmentSchedulePaymentRead
    from .note_attachment_schedule_payment_update import NoteAttachmentSchedulePaymentUpdate
    from .note_attachment_sofort_merchant_transaction import NoteAttachmentSofortMerchantTransaction
    from .note_attachment_sofort_merchant_transaction_create import NoteAttachmentSofortMerchantTransactionCreate
    from .note_attachment_sofort_merchant_transaction_delete import NoteAttachmentSofortMerchantTransactionDelete
    from .note_attachment_sofort_merchant_transaction_listing import NoteAttachmentSofortMerchantTransactionListing
    from .note_attachment_sofort_merchant_transaction_read import NoteAttachmentSofortMerchantTransactionRead
    from .note_attachment_sofort_merchant_transaction_update import NoteAttachmentSofortMerchantTransactionUpdate
    from .note_attachment_whitelist_result import NoteAttachmentWhitelistResult
    from .note_attachment_whitelist_result_create import NoteAttachmentWhitelistResultCreate
    from .note_attachment_whitelist_result_delete import NoteAttachmentWhitelistResultDelete
    from .note_attachment_whitelist_result_listing import NoteAttachmentWhitelistResultListing
    from .note_attachment_whitelist_result_read import NoteAttachmentWhitelistResultRead
    from .note_attachment_whitelist_result_update import NoteAttachmentWhitelistResultUpdate
    from .note_text_bank_switch_service_netherlands_incoming_payment import (
        NoteTextBankSwitchServiceNetherlandsIncomingPayment,
    )
    from .note_text_bank_switch_service_netherlands_incoming_payment_create import (
        NoteTextBankSwitchServiceNetherlandsIncomingPaymentCreate,
    )
    from .note_text_bank_switch_service_netherlands_incoming_payment_delete import (
        NoteTextBankSwitchServiceNetherlandsIncomingPaymentDelete,
    )
    from .note_text_bank_switch_service_netherlands_incoming_payment_listing import (
        NoteTextBankSwitchServiceNetherlandsIncomingPaymentListing,
    )
    from .note_text_bank_switch_service_netherlands_incoming_payment_read import (
        NoteTextBankSwitchServiceNetherlandsIncomingPaymentRead,
    )
    from .note_text_bank_switch_service_netherlands_incoming_payment_update import (
        NoteTextBankSwitchServiceNetherlandsIncomingPaymentUpdate,
    )
    from .note_text_bunq_me_fundraiser_result import NoteTextBunqMeFundraiserResult
    from .note_text_bunq_me_fundraiser_result_create import NoteTextBunqMeFundraiserResultCreate
    from .note_text_bunq_me_fundraiser_result_delete import NoteTextBunqMeFundraiserResultDelete
    from .note_text_bunq_me_fundraiser_result_listing import NoteTextBunqMeFundraiserResultListing
    from .note_text_bunq_me_fundraiser_result_read import NoteTextBunqMeFundraiserResultRead
    from .note_text_bunq_me_fundraiser_result_update import NoteTextBunqMeFundraiserResultUpdate
    from .note_text_draft_payment import NoteTextDraftPayment
    from .note_text_draft_payment_create import NoteTextDraftPaymentCreate
    from .note_text_draft_payment_delete import NoteTextDraftPaymentDelete
    from .note_text_draft_payment_listing import NoteTextDraftPaymentListing
    from .note_text_draft_payment_read import NoteTextDraftPaymentRead
    from .note_text_draft_payment_update import NoteTextDraftPaymentUpdate
    from .note_text_ideal_merchant_transaction import NoteTextIdealMerchantTransaction
    from .note_text_ideal_merchant_transaction_create import NoteTextIdealMerchantTransactionCreate
    from .note_text_ideal_merchant_transaction_delete import NoteTextIdealMerchantTransactionDelete
    from .note_text_ideal_merchant_transaction_listing import NoteTextIdealMerchantTransactionListing
    from .note_text_ideal_merchant_transaction_read import NoteTextIdealMerchantTransactionRead
    from .note_text_ideal_merchant_transaction_update import NoteTextIdealMerchantTransactionUpdate
    from .note_text_master_card_action import NoteTextMasterCardAction
    from .note_text_master_card_action_create import NoteTextMasterCardActionCreate
    from .note_text_master_card_action_delete import NoteTextMasterCardActionDelete
    from .note_text_master_card_action_listing import NoteTextMasterCardActionListing
    from .note_text_master_card_action_read import NoteTextMasterCardActionRead
    from .note_text_master_card_action_update import NoteTextMasterCardActionUpdate
    from .note_text_payment import NoteTextPayment
    from .note_text_payment_batch import NoteTextPaymentBatch
    from .note_text_payment_batch_create import NoteTextPaymentBatchCreate
    from .note_text_payment_batch_delete import NoteTextPaymentBatchDelete
    from .note_text_payment_batch_listing import NoteTextPaymentBatchListing
    from .note_text_payment_batch_read import NoteTextPaymentBatchRead
    from .note_text_payment_batch_update import NoteTextPaymentBatchUpdate
    from .note_text_payment_create import NoteTextPaymentCreate
    from .note_text_payment_delete import NoteTextPaymentDelete
    from .note_text_payment_listing import NoteTextPaymentListing
    from .note_text_payment_read import NoteTextPaymentRead
    from .note_text_payment_update import NoteTextPaymentUpdate
    from .note_text_request_inquiry import NoteTextRequestInquiry
    from .note_text_request_inquiry_batch import NoteTextRequestInquiryBatch
    from .note_text_request_inquiry_batch_create import NoteTextRequestInquiryBatchCreate
    from .note_text_request_inquiry_batch_delete import NoteTextRequestInquiryBatchDelete
    from .note_text_request_inquiry_batch_listing import NoteTextRequestInquiryBatchListing
    from .note_text_request_inquiry_batch_read import NoteTextRequestInquiryBatchRead
    from .note_text_request_inquiry_batch_update import NoteTextRequestInquiryBatchUpdate
    from .note_text_request_inquiry_create import NoteTextRequestInquiryCreate
    from .note_text_request_inquiry_delete import NoteTextRequestInquiryDelete
    from .note_text_request_inquiry_listing import NoteTextRequestInquiryListing
    from .note_text_request_inquiry_read import NoteTextRequestInquiryRead
    from .note_text_request_inquiry_update import NoteTextRequestInquiryUpdate
    from .note_text_request_response import NoteTextRequestResponse
    from .note_text_request_response_create import NoteTextRequestResponseCreate
    from .note_text_request_response_delete import NoteTextRequestResponseDelete
    from .note_text_request_response_listing import NoteTextRequestResponseListing
    from .note_text_request_response_read import NoteTextRequestResponseRead
    from .note_text_request_response_update import NoteTextRequestResponseUpdate
    from .note_text_schedule_instance import NoteTextScheduleInstance
    from .note_text_schedule_instance_create import NoteTextScheduleInstanceCreate
    from .note_text_schedule_instance_delete import NoteTextScheduleInstanceDelete
    from .note_text_schedule_instance_listing import NoteTextScheduleInstanceListing
    from .note_text_schedule_instance_read import NoteTextScheduleInstanceRead
    from .note_text_schedule_instance_update import NoteTextScheduleInstanceUpdate
    from .note_text_schedule_payment import NoteTextSchedulePayment
    from .note_text_schedule_payment_batch import NoteTextSchedulePaymentBatch
    from .note_text_schedule_payment_batch_create import NoteTextSchedulePaymentBatchCreate
    from .note_text_schedule_payment_batch_delete import NoteTextSchedulePaymentBatchDelete
    from .note_text_schedule_payment_batch_listing import NoteTextSchedulePaymentBatchListing
    from .note_text_schedule_payment_batch_read import NoteTextSchedulePaymentBatchRead
    from .note_text_schedule_payment_batch_update import NoteTextSchedulePaymentBatchUpdate
    from .note_text_schedule_payment_create import NoteTextSchedulePaymentCreate
    from .note_text_schedule_payment_delete import NoteTextSchedulePaymentDelete
    from .note_text_schedule_payment_listing import NoteTextSchedulePaymentListing
    from .note_text_schedule_payment_read import NoteTextSchedulePaymentRead
    from .note_text_schedule_payment_update import NoteTextSchedulePaymentUpdate
    from .note_text_sofort_merchant_transaction import NoteTextSofortMerchantTransaction
    from .note_text_sofort_merchant_transaction_create import NoteTextSofortMerchantTransactionCreate
    from .note_text_sofort_merchant_transaction_delete import NoteTextSofortMerchantTransactionDelete
    from .note_text_sofort_merchant_transaction_listing import NoteTextSofortMerchantTransactionListing
    from .note_text_sofort_merchant_transaction_read import NoteTextSofortMerchantTransactionRead
    from .note_text_sofort_merchant_transaction_update import NoteTextSofortMerchantTransactionUpdate
    from .note_text_whitelist_result import NoteTextWhitelistResult
    from .note_text_whitelist_result_create import NoteTextWhitelistResultCreate
    from .note_text_whitelist_result_delete import NoteTextWhitelistResultDelete
    from .note_text_whitelist_result_listing import NoteTextWhitelistResultListing
    from .note_text_whitelist_result_read import NoteTextWhitelistResultRead
    from .note_text_whitelist_result_update import NoteTextWhitelistResultUpdate
    from .notification_filter import NotificationFilter
    from .notification_filter_email import NotificationFilterEmail
    from .notification_filter_email_create import NotificationFilterEmailCreate
    from .notification_filter_email_listing import NotificationFilterEmailListing
    from .notification_filter_push import NotificationFilterPush
    from .notification_filter_push_create import NotificationFilterPushCreate
    from .notification_filter_push_listing import NotificationFilterPushListing
    from .notification_filter_url import NotificationFilterUrl
    from .notification_filter_url_create import NotificationFilterUrlCreate
    from .notification_filter_url_listing import NotificationFilterUrlListing
    from .notification_filter_url_monetary_account_create import NotificationFilterUrlMonetaryAccountCreate
    from .notification_filter_url_monetary_account_listing import NotificationFilterUrlMonetaryAccountListing
    from .oauth_callback_url import OauthCallbackUrl
    from .oauth_callback_url_create import OauthCallbackUrlCreate
    from .oauth_callback_url_delete import OauthCallbackUrlDelete
    from .oauth_callback_url_listing import OauthCallbackUrlListing
    from .oauth_callback_url_read import OauthCallbackUrlRead
    from .oauth_callback_url_update import OauthCallbackUrlUpdate
    from .oauth_client import OauthClient
    from .oauth_client_create import OauthClientCreate
    from .oauth_client_listing import OauthClientListing
    from .oauth_client_read import OauthClientRead
    from .oauth_client_update import OauthClientUpdate
    from .payment import Payment
    from .payment_auto_allocate import PaymentAutoAllocate
    from .payment_auto_allocate_create import PaymentAutoAllocateCreate
    from .payment_auto_allocate_definition import PaymentAutoAllocateDefinition
    from .payment_auto_allocate_definition_listing import PaymentAutoAllocateDefinitionListing
    from .payment_auto_allocate_delete import PaymentAutoAllocateDelete
    from .payment_auto_allocate_instance import PaymentAutoAllocateInstance
    from .payment_auto_allocate_instance_listing import PaymentAutoAllocateInstanceListing
    from .payment_auto_allocate_instance_read import PaymentAutoAllocateInstanceRead
    from .payment_auto_allocate_listing import PaymentAutoAllocateListing
    from .payment_auto_allocate_read import PaymentAutoAllocateRead
    from .payment_auto_allocate_update import PaymentAutoAllocateUpdate
    from .payment_auto_allocate_user_listing import PaymentAutoAllocateUserListing
    from .payment_batch import PaymentBatch
    from .payment_batch_anchored_payment import PaymentBatchAnchoredPayment
    from .payment_batch_create import PaymentBatchCreate
    from .payment_batch_listing import PaymentBatchListing
    from .payment_batch_read import PaymentBatchRead
    from .payment_batch_update import PaymentBatchUpdate
    from .payment_create import PaymentCreate
    from .payment_listing import PaymentListing
    from .payment_read import PaymentRead
    from .payment_service_provider_credential_create import PaymentServiceProviderCredentialCreate
    from .payment_service_provider_credential_read import PaymentServiceProviderCredentialRead
    from .payment_service_provider_draft_payment import PaymentServiceProviderDraftPayment
    from .payment_service_provider_draft_payment_create import PaymentServiceProviderDraftPaymentCreate
    from .payment_service_provider_draft_payment_listing import PaymentServiceProviderDraftPaymentListing
    from .payment_service_provider_draft_payment_read import PaymentServiceProviderDraftPaymentRead
    from .payment_service_provider_draft_payment_update import PaymentServiceProviderDraftPaymentUpdate
    from .permitted_device import PermittedDevice
    from .permitted_ip import PermittedIp
    from .permitted_ip_create import PermittedIpCreate
    from .permitted_ip_listing import PermittedIpListing
    from .permitted_ip_read import PermittedIpRead
    from .permitted_ip_update import PermittedIpUpdate
    from .place_photo_lookup_content_listing import PlacePhotoLookupContentListing
    from .pointer import Pointer
    from .registry_membership import RegistryMembership
    from .registry_settlement import RegistrySettlement
    from .registry_settlement_create import RegistrySettlementCreate
    from .registry_settlement_item import RegistrySettlementItem
    from .registry_settlement_listing import RegistrySettlementListing
    from .registry_settlement_read import RegistrySettlementRead
    from .relation_user import RelationUser
    from .request_inquiry import RequestInquiry
    from .request_inquiry_batch import RequestInquiryBatch
    from .request_inquiry_batch_create import RequestInquiryBatchCreate
    from .request_inquiry_batch_listing import RequestInquiryBatchListing
    from .request_inquiry_batch_read import RequestInquiryBatchRead
    from .request_inquiry_batch_update import RequestInquiryBatchUpdate
    from .request_inquiry_create import RequestInquiryCreate
    from .request_inquiry_listing import RequestInquiryListing
    from .request_inquiry_read import RequestInquiryRead
    from .request_inquiry_reference import RequestInquiryReference
    from .request_inquiry_update import RequestInquiryUpdate
    from .request_reference_split_the_bill_anchor_object import RequestReferenceSplitTheBillAnchorObject
    from .request_response import RequestResponse
    from .request_response_listing import RequestResponseListing
    from .request_response_read import RequestResponseRead
    from .request_response_update import RequestResponseUpdate
    from .reward_listing import RewardListing
    from .reward_read import RewardRead
    from .reward_recipient import RewardRecipient
    from .reward_recipient_listing import RewardRecipientListing
    from .reward_recipient_read import RewardRecipientRead
    from .reward_sender import RewardSender
    from .reward_sender_listing import RewardSenderListing
    from .reward_sender_read import RewardSenderRead
    from .sandbox_user_company import SandboxUserCompany
    from .sandbox_user_company_create import SandboxUserCompanyCreate
    from .sandbox_user_person import SandboxUserPerson
    from .sandbox_user_person_create import SandboxUserPersonCreate
    from .schedule import Schedule
    from .schedule_anchor_object import ScheduleAnchorObject
    from .schedule_instance import ScheduleInstance
    from .schedule_instance_anchor_object import ScheduleInstanceAnchorObject
    from .schedule_instance_listing import ScheduleInstanceListing
    from .schedule_instance_read import ScheduleInstanceRead
    from .schedule_instance_update import ScheduleInstanceUpdate
    from .schedule_listing import ScheduleListing
    from .schedule_payment import SchedulePayment
    from .schedule_payment_batch import SchedulePaymentBatch
    from .schedule_payment_batch_create import SchedulePaymentBatchCreate
    from .schedule_payment_batch_delete import SchedulePaymentBatchDelete
    from .schedule_payment_batch_read import SchedulePaymentBatchRead
    from .schedule_payment_batch_update import SchedulePaymentBatchUpdate
    from .schedule_payment_create import SchedulePaymentCreate
    from .schedule_payment_delete import SchedulePaymentDelete
    from .schedule_payment_entry import SchedulePaymentEntry
    from .schedule_payment_listing import SchedulePaymentListing
    from .schedule_payment_read import SchedulePaymentRead
    from .schedule_payment_update import SchedulePaymentUpdate
    from .schedule_read import ScheduleRead
    from .schedule_user_listing import ScheduleUserListing
    from .server_error import ServerError
    from .server_error_create import ServerErrorCreate
    from .session_delete import SessionDelete
    from .session_server_create import SessionServerCreate
    from .session_server_token import SessionServerToken
    from .share_detail import ShareDetail
    from .share_detail_draft_payment import ShareDetailDraftPayment
    from .share_detail_payment import ShareDetailPayment
    from .share_detail_read_only import ShareDetailReadOnly
    from .share_invite_monetary_account_inquiry import ShareInviteMonetaryAccountInquiry
    from .share_invite_monetary_account_inquiry_create import ShareInviteMonetaryAccountInquiryCreate
    from .share_invite_monetary_account_inquiry_listing import ShareInviteMonetaryAccountInquiryListing
    from .share_invite_monetary_account_inquiry_read import ShareInviteMonetaryAccountInquiryRead
    from .share_invite_monetary_account_inquiry_update import ShareInviteMonetaryAccountInquiryUpdate
    from .share_invite_monetary_account_response import ShareInviteMonetaryAccountResponse
    from .share_invite_monetary_account_response_listing import ShareInviteMonetaryAccountResponseListing
    from .share_invite_monetary_account_response_read import ShareInviteMonetaryAccountResponseRead
    from .share_invite_monetary_account_response_update import ShareInviteMonetaryAccountResponseUpdate
    from .sofort_merchant_transaction import SofortMerchantTransaction
    from .sofort_merchant_transaction_listing import SofortMerchantTransactionListing
    from .sofort_merchant_transaction_read import SofortMerchantTransactionRead
    from .tax_resident import TaxResident
    from .token_qr_request_ideal_create import TokenQrRequestIdealCreate
    from .token_qr_request_sofort_create import TokenQrRequestSofortCreate
    from .transferwise_account_quote_create import TransferwiseAccountQuoteCreate
    from .transferwise_account_quote_delete import TransferwiseAccountQuoteDelete
    from .transferwise_account_quote_listing import TransferwiseAccountQuoteListing
    from .transferwise_account_quote_read import TransferwiseAccountQuoteRead
    from .transferwise_account_requirement_create import TransferwiseAccountRequirementCreate
    from .transferwise_account_requirement_listing import TransferwiseAccountRequirementListing
    from .transferwise_currency_listing import TransferwiseCurrencyListing
    from .transferwise_quote import TransferwiseQuote
    from .transferwise_quote_create import TransferwiseQuoteCreate
    from .transferwise_quote_read import TransferwiseQuoteRead
    from .transferwise_quote_temporary_create import TransferwiseQuoteTemporaryCreate
    from .transferwise_quote_temporary_read import TransferwiseQuoteTemporaryRead
    from .transferwise_requirement_field import TransferwiseRequirementField
    from .transferwise_requirement_field_group import TransferwiseRequirementFieldGroup
    from .transferwise_requirement_field_group_validation_async import TransferwiseRequirementFieldGroupValidationAsync
    from .transferwise_requirement_field_group_validation_async_params import (
        TransferwiseRequirementFieldGroupValidationAsyncParams,
    )
    from .transferwise_requirement_field_group_values_allowed import TransferwiseRequirementFieldGroupValuesAllowed
    from .transferwise_transfer import TransferwiseTransfer
    from .transferwise_transfer_create import TransferwiseTransferCreate
    from .transferwise_transfer_listing import TransferwiseTransferListing
    from .transferwise_transfer_read import TransferwiseTransferRead
    from .transferwise_transfer_requirement_create import TransferwiseTransferRequirementCreate
    from .transferwise_user_create import TransferwiseUserCreate
    from .transferwise_user_listing import TransferwiseUserListing
    from .translink_transaction_create import TranslinkTransactionCreate
    from .translink_transaction_entry import TranslinkTransactionEntry
    from .translink_transaction_listing import TranslinkTransactionListing
    from .translink_transaction_read import TranslinkTransactionRead
    from .tree_progress_listing import TreeProgressListing
    from .ubo import Ubo
    from .user_api_key import UserApiKey
    from .user_api_key_anchored_user import UserApiKeyAnchoredUser
    from .user_company import UserCompany
    from .user_company_name_listing import UserCompanyNameListing
    from .user_company_read import UserCompanyRead
    from .user_company_update import UserCompanyUpdate
    from .user_credential_password_ip_listing import UserCredentialPasswordIpListing
    from .user_credential_password_ip_read import UserCredentialPasswordIpRead
    from .user_legal_name_listing import UserLegalNameListing
    from .user_listing import UserListing
    from .user_payment_service_provider import UserPaymentServiceProvider
    from .user_payment_service_provider_read import UserPaymentServiceProviderRead
    from .user_person import UserPerson
    from .user_person_read import UserPersonRead
    from .user_person_update import UserPersonUpdate
    from .user_read import UserRead
    from .whitelist import Whitelist
    from .whitelist_result import WhitelistResult
    from .whitelist_result_view_anchored_object import WhitelistResultViewAnchoredObject
    from .whitelist_sdd_listing import WhitelistSddListing
    from .whitelist_sdd_monetary_account_paying_listing import WhitelistSddMonetaryAccountPayingListing
    from .whitelist_sdd_monetary_account_paying_read import WhitelistSddMonetaryAccountPayingRead
    from .whitelist_sdd_one_off import WhitelistSddOneOff
    from .whitelist_sdd_one_off_create import WhitelistSddOneOffCreate
    from .whitelist_sdd_one_off_delete import WhitelistSddOneOffDelete
    from .whitelist_sdd_one_off_listing import WhitelistSddOneOffListing
    from .whitelist_sdd_one_off_read import WhitelistSddOneOffRead
    from .whitelist_sdd_one_off_update import WhitelistSddOneOffUpdate
    from .whitelist_sdd_read import WhitelistSddRead
    from .whitelist_sdd_recurring import WhitelistSddRecurring
    from .whitelist_sdd_recurring_create import WhitelistSddRecurringCreate
    from .whitelist_sdd_recurring_delete import WhitelistSddRecurringDelete
    from .whitelist_sdd_recurring_listing import WhitelistSddRecurringListing
    from .whitelist_sdd_recurring_read import WhitelistSddRecurringRead
    from .whitelist_sdd_recurring_update import WhitelistSddRecurringUpdate
_dynamic_imports: typing.Dict[str, str] = {
    "AdditionalInformation": ".additional_information",
    "Address": ".address",
    "Amount": ".amount",
    "Attachment": ".attachment",
    "AttachmentConversationContentListing": ".attachment_conversation_content_listing",
    "AttachmentMasterCardActionRefund": ".attachment_master_card_action_refund",
    "AttachmentMonetaryAccount": ".attachment_monetary_account",
    "AttachmentMonetaryAccountContentListing": ".attachment_monetary_account_content_listing",
    "AttachmentMonetaryAccountCreate": ".attachment_monetary_account_create",
    "AttachmentMonetaryAccountPayment": ".attachment_monetary_account_payment",
    "AttachmentPublic": ".attachment_public",
    "AttachmentPublicContentListing": ".attachment_public_content_listing",
    "AttachmentPublicCreate": ".attachment_public_create",
    "AttachmentPublicRead": ".attachment_public_read",
    "AttachmentUrl": ".attachment_url",
    "AttachmentUserContentListing": ".attachment_user_content_listing",
    "AttachmentUserRead": ".attachment_user_read",
    "Avatar": ".avatar",
    "AvatarCreate": ".avatar_create",
    "AvatarRead": ".avatar_read",
    "BadRequestErrorBody": ".bad_request_error_body",
    "BankSwitchServiceNetherlandsIncoming": ".bank_switch_service_netherlands_incoming",
    "BankSwitchServiceNetherlandsIncomingPayment": ".bank_switch_service_netherlands_incoming_payment",
    "BankSwitchServiceNetherlandsIncomingPaymentRead": ".bank_switch_service_netherlands_incoming_payment_read",
    "BillingContractSubscription": ".billing_contract_subscription",
    "BillingContractSubscriptionListing": ".billing_contract_subscription_listing",
    "BirdeeInvestmentPortfolio": ".birdee_investment_portfolio",
    "BirdeeInvestmentPortfolioBalance": ".birdee_investment_portfolio_balance",
    "BirdeeInvestmentPortfolioGoal": ".birdee_investment_portfolio_goal",
    "BirdeePortfolioAllocation": ".birdee_portfolio_allocation",
    "BunqId": ".bunq_id",
    "BunqMeFundraiserProfile": ".bunq_me_fundraiser_profile",
    "BunqMeFundraiserProfileUserListing": ".bunq_me_fundraiser_profile_user_listing",
    "BunqMeFundraiserProfileUserRead": ".bunq_me_fundraiser_profile_user_read",
    "BunqMeFundraiserResult": ".bunq_me_fundraiser_result",
    "BunqMeFundraiserResultRead": ".bunq_me_fundraiser_result_read",
    "BunqMeMerchantAvailable": ".bunq_me_merchant_available",
    "BunqMeTab": ".bunq_me_tab",
    "BunqMeTabCreate": ".bunq_me_tab_create",
    "BunqMeTabEntry": ".bunq_me_tab_entry",
    "BunqMeTabListing": ".bunq_me_tab_listing",
    "BunqMeTabRead": ".bunq_me_tab_read",
    "BunqMeTabResultInquiry": ".bunq_me_tab_result_inquiry",
    "BunqMeTabResultResponse": ".bunq_me_tab_result_response",
    "BunqMeTabResultResponseRead": ".bunq_me_tab_result_response_read",
    "BunqMeTabUpdate": ".bunq_me_tab_update",
    "Card": ".card",
    "CardBatchCreate": ".card_batch_create",
    "CardBatchEntry": ".card_batch_entry",
    "CardBatchReplaceCreate": ".card_batch_replace_create",
    "CardBatchReplaceEntry": ".card_batch_replace_entry",
    "CardCountryPermission": ".card_country_permission",
    "CardCreditCreate": ".card_credit_create",
    "CardDebit": ".card_debit",
    "CardDebitCreate": ".card_debit_create",
    "CardGeneratedCvc2": ".card_generated_cvc2",
    "CardGeneratedCvc2Create": ".card_generated_cvc2create",
    "CardGeneratedCvc2Listing": ".card_generated_cvc2listing",
    "CardGeneratedCvc2Read": ".card_generated_cvc2read",
    "CardGeneratedCvc2Update": ".card_generated_cvc2update",
    "CardListing": ".card_listing",
    "CardNameListing": ".card_name_listing",
    "CardPinAssignment": ".card_pin_assignment",
    "CardPrimaryAccountNumber": ".card_primary_account_number",
    "CardRead": ".card_read",
    "CardReplaceCreate": ".card_replace_create",
    "CardUpdate": ".card_update",
    "Certificate": ".certificate",
    "CertificatePinnedCreate": ".certificate_pinned_create",
    "CertificatePinnedDelete": ".certificate_pinned_delete",
    "CertificatePinnedListing": ".certificate_pinned_listing",
    "CertificatePinnedRead": ".certificate_pinned_read",
    "CoOwner": ".co_owner",
    "Company": ".company",
    "CompanyCreate": ".company_create",
    "CompanyListing": ".company_listing",
    "CompanyRead": ".company_read",
    "CompanyUpdate": ".company_update",
    "CompanyVatNumber": ".company_vat_number",
    "ConfirmationOfFundsCreate": ".confirmation_of_funds_create",
    "CurrencyCloudBeneficiaryCreate": ".currency_cloud_beneficiary_create",
    "CurrencyCloudBeneficiaryListing": ".currency_cloud_beneficiary_listing",
    "CurrencyCloudBeneficiaryRead": ".currency_cloud_beneficiary_read",
    "CurrencyCloudBeneficiaryRequirementField": ".currency_cloud_beneficiary_requirement_field",
    "CurrencyCloudBeneficiaryRequirementListing": ".currency_cloud_beneficiary_requirement_listing",
    "CurrencyCloudPaymentQuoteCreate": ".currency_cloud_payment_quote_create",
    "CurrencyConversionListing": ".currency_conversion_listing",
    "CurrencyConversionQuote": ".currency_conversion_quote",
    "CurrencyConversionQuoteCreate": ".currency_conversion_quote_create",
    "CurrencyConversionQuoteRead": ".currency_conversion_quote_read",
    "CurrencyConversionQuoteUpdate": ".currency_conversion_quote_update",
    "CurrencyConversionRead": ".currency_conversion_read",
    "Customer": ".customer",
    "CustomerLimit": ".customer_limit",
    "CustomerLimitListing": ".customer_limit_listing",
    "DeviceListing": ".device_listing",
    "DeviceRead": ".device_read",
    "DeviceServer": ".device_server",
    "DeviceServerCreate": ".device_server_create",
    "DeviceServerListing": ".device_server_listing",
    "DeviceServerRead": ".device_server_read",
    "DraftPayment": ".draft_payment",
    "DraftPaymentAnchorObject": ".draft_payment_anchor_object",
    "DraftPaymentCreate": ".draft_payment_create",
    "DraftPaymentEntry": ".draft_payment_entry",
    "DraftPaymentListing": ".draft_payment_listing",
    "DraftPaymentRead": ".draft_payment_read",
    "DraftPaymentResponse": ".draft_payment_response",
    "DraftPaymentUpdate": ".draft_payment_update",
    "Error": ".error",
    "ErrorItem": ".error_item",
    "EventListing": ".event_listing",
    "EventObject": ".event_object",
    "EventRead": ".event_read",
    "ExportAnnualOverviewContentListing": ".export_annual_overview_content_listing",
    "ExportAnnualOverviewCreate": ".export_annual_overview_create",
    "ExportAnnualOverviewDelete": ".export_annual_overview_delete",
    "ExportAnnualOverviewListing": ".export_annual_overview_listing",
    "ExportAnnualOverviewRead": ".export_annual_overview_read",
    "ExportRib": ".export_rib",
    "ExportRibContentListing": ".export_rib_content_listing",
    "ExportRibCreate": ".export_rib_create",
    "ExportRibDelete": ".export_rib_delete",
    "ExportRibListing": ".export_rib_listing",
    "ExportRibRead": ".export_rib_read",
    "ExportStatementCardContentListing": ".export_statement_card_content_listing",
    "ExportStatementCardCsvCreate": ".export_statement_card_csv_create",
    "ExportStatementCardCsvDelete": ".export_statement_card_csv_delete",
    "ExportStatementCardCsvListing": ".export_statement_card_csv_listing",
    "ExportStatementCardCsvRead": ".export_statement_card_csv_read",
    "ExportStatementCardListing": ".export_statement_card_listing",
    "ExportStatementCardPdfCreate": ".export_statement_card_pdf_create",
    "ExportStatementCardPdfDelete": ".export_statement_card_pdf_delete",
    "ExportStatementCardPdfListing": ".export_statement_card_pdf_listing",
    "ExportStatementCardPdfRead": ".export_statement_card_pdf_read",
    "ExportStatementCardRead": ".export_statement_card_read",
    "ExportStatementContentListing": ".export_statement_content_listing",
    "ExportStatementCreate": ".export_statement_create",
    "ExportStatementDelete": ".export_statement_delete",
    "ExportStatementListing": ".export_statement_listing",
    "ExportStatementPayment": ".export_statement_payment",
    "ExportStatementPaymentContentListing": ".export_statement_payment_content_listing",
    "ExportStatementPaymentCreate": ".export_statement_payment_create",
    "ExportStatementPaymentRead": ".export_statement_payment_read",
    "ExportStatementRead": ".export_statement_read",
    "FeatureAnnouncement": ".feature_announcement",
    "FeatureAnnouncementRead": ".feature_announcement_read",
    "Geolocation": ".geolocation",
    "IdealMerchantTransaction": ".ideal_merchant_transaction",
    "IdealMerchantTransactionCreate": ".ideal_merchant_transaction_create",
    "IdealMerchantTransactionListing": ".ideal_merchant_transaction_listing",
    "IdealMerchantTransactionRead": ".ideal_merchant_transaction_read",
    "Image": ".image",
    "InsightEventListing": ".insight_event_listing",
    "InsightListing": ".insight_listing",
    "InsightPreferenceDateListing": ".insight_preference_date_listing",
    "InstallationCreate": ".installation_create",
    "InstallationListing": ".installation_listing",
    "InstallationRead": ".installation_read",
    "InstallationServerPublicKey": ".installation_server_public_key",
    "InstallationServerPublicKeyListing": ".installation_server_public_key_listing",
    "InstallationToken": ".installation_token",
    "Invoice": ".invoice",
    "InvoiceByUserListing": ".invoice_by_user_listing",
    "InvoiceByUserRead": ".invoice_by_user_read",
    "InvoiceExportPdfContentListing": ".invoice_export_pdf_content_listing",
    "InvoiceItem": ".invoice_item",
    "InvoiceItemGroup": ".invoice_item_group",
    "InvoiceListing": ".invoice_listing",
    "InvoiceRead": ".invoice_read",
    "Issuer": ".issuer",
    "LabelCard": ".label_card",
    "LabelMonetaryAccount": ".label_monetary_account",
    "LabelUser": ".label_user",
    "MasterCardAction": ".master_card_action",
    "MasterCardActionListing": ".master_card_action_listing",
    "MasterCardActionRead": ".master_card_action_read",
    "MasterCardActionReference": ".master_card_action_reference",
    "MasterCardActionRefund": ".master_card_action_refund",
    "MasterCardIdentityCheckChallengeRequestUserRead": ".master_card_identity_check_challenge_request_user_read",
    "MasterCardIdentityCheckChallengeRequestUserUpdate": ".master_card_identity_check_challenge_request_user_update",
    "MasterCardPaymentListing": ".master_card_payment_listing",
    "MonetaryAccountBank": ".monetary_account_bank",
    "MonetaryAccountBankCreate": ".monetary_account_bank_create",
    "MonetaryAccountBankListing": ".monetary_account_bank_listing",
    "MonetaryAccountBankRead": ".monetary_account_bank_read",
    "MonetaryAccountBankUpdate": ".monetary_account_bank_update",
    "MonetaryAccountExternal": ".monetary_account_external",
    "MonetaryAccountExternalListing": ".monetary_account_external_listing",
    "MonetaryAccountExternalRead": ".monetary_account_external_read",
    "MonetaryAccountInvestment": ".monetary_account_investment",
    "MonetaryAccountJoint": ".monetary_account_joint",
    "MonetaryAccountJointCreate": ".monetary_account_joint_create",
    "MonetaryAccountJointListing": ".monetary_account_joint_listing",
    "MonetaryAccountJointRead": ".monetary_account_joint_read",
    "MonetaryAccountJointUpdate": ".monetary_account_joint_update",
    "MonetaryAccountLight": ".monetary_account_light",
    "MonetaryAccountListing": ".monetary_account_listing",
    "MonetaryAccountProfile": ".monetary_account_profile",
    "MonetaryAccountProfileDrain": ".monetary_account_profile_drain",
    "MonetaryAccountProfileFill": ".monetary_account_profile_fill",
    "MonetaryAccountRead": ".monetary_account_read",
    "MonetaryAccountSavings": ".monetary_account_savings",
    "MonetaryAccountSavingsCreate": ".monetary_account_savings_create",
    "MonetaryAccountSavingsListing": ".monetary_account_savings_listing",
    "MonetaryAccountSavingsRead": ".monetary_account_savings_read",
    "MonetaryAccountSavingsUpdate": ".monetary_account_savings_update",
    "MonetaryAccountSetting": ".monetary_account_setting",
    "NoteAttachmentBankSwitchServiceNetherlandsIncomingPayment": ".note_attachment_bank_switch_service_netherlands_incoming_payment",
    "NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentCreate": ".note_attachment_bank_switch_service_netherlands_incoming_payment_create",
    "NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentDelete": ".note_attachment_bank_switch_service_netherlands_incoming_payment_delete",
    "NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentListing": ".note_attachment_bank_switch_service_netherlands_incoming_payment_listing",
    "NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentRead": ".note_attachment_bank_switch_service_netherlands_incoming_payment_read",
    "NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentUpdate": ".note_attachment_bank_switch_service_netherlands_incoming_payment_update",
    "NoteAttachmentBunqMeFundraiserResult": ".note_attachment_bunq_me_fundraiser_result",
    "NoteAttachmentBunqMeFundraiserResultCreate": ".note_attachment_bunq_me_fundraiser_result_create",
    "NoteAttachmentBunqMeFundraiserResultDelete": ".note_attachment_bunq_me_fundraiser_result_delete",
    "NoteAttachmentBunqMeFundraiserResultListing": ".note_attachment_bunq_me_fundraiser_result_listing",
    "NoteAttachmentBunqMeFundraiserResultRead": ".note_attachment_bunq_me_fundraiser_result_read",
    "NoteAttachmentBunqMeFundraiserResultUpdate": ".note_attachment_bunq_me_fundraiser_result_update",
    "NoteAttachmentDraftPayment": ".note_attachment_draft_payment",
    "NoteAttachmentDraftPaymentCreate": ".note_attachment_draft_payment_create",
    "NoteAttachmentDraftPaymentDelete": ".note_attachment_draft_payment_delete",
    "NoteAttachmentDraftPaymentListing": ".note_attachment_draft_payment_listing",
    "NoteAttachmentDraftPaymentRead": ".note_attachment_draft_payment_read",
    "NoteAttachmentDraftPaymentUpdate": ".note_attachment_draft_payment_update",
    "NoteAttachmentIdealMerchantTransaction": ".note_attachment_ideal_merchant_transaction",
    "NoteAttachmentIdealMerchantTransactionCreate": ".note_attachment_ideal_merchant_transaction_create",
    "NoteAttachmentIdealMerchantTransactionDelete": ".note_attachment_ideal_merchant_transaction_delete",
    "NoteAttachmentIdealMerchantTransactionListing": ".note_attachment_ideal_merchant_transaction_listing",
    "NoteAttachmentIdealMerchantTransactionRead": ".note_attachment_ideal_merchant_transaction_read",
    "NoteAttachmentIdealMerchantTransactionUpdate": ".note_attachment_ideal_merchant_transaction_update",
    "NoteAttachmentMasterCardAction": ".note_attachment_master_card_action",
    "NoteAttachmentMasterCardActionCreate": ".note_attachment_master_card_action_create",
    "NoteAttachmentMasterCardActionDelete": ".note_attachment_master_card_action_delete",
    "NoteAttachmentMasterCardActionListing": ".note_attachment_master_card_action_listing",
    "NoteAttachmentMasterCardActionRead": ".note_attachment_master_card_action_read",
    "NoteAttachmentMasterCardActionUpdate": ".note_attachment_master_card_action_update",
    "NoteAttachmentPayment": ".note_attachment_payment",
    "NoteAttachmentPaymentBatch": ".note_attachment_payment_batch",
    "NoteAttachmentPaymentBatchCreate": ".note_attachment_payment_batch_create",
    "NoteAttachmentPaymentBatchDelete": ".note_attachment_payment_batch_delete",
    "NoteAttachmentPaymentBatchListing": ".note_attachment_payment_batch_listing",
    "NoteAttachmentPaymentBatchRead": ".note_attachment_payment_batch_read",
    "NoteAttachmentPaymentBatchUpdate": ".note_attachment_payment_batch_update",
    "NoteAttachmentPaymentCreate": ".note_attachment_payment_create",
    "NoteAttachmentPaymentDelete": ".note_attachment_payment_delete",
    "NoteAttachmentPaymentListing": ".note_attachment_payment_listing",
    "NoteAttachmentPaymentRead": ".note_attachment_payment_read",
    "NoteAttachmentPaymentUpdate": ".note_attachment_payment_update",
    "NoteAttachmentRequestInquiry": ".note_attachment_request_inquiry",
    "NoteAttachmentRequestInquiryBatch": ".note_attachment_request_inquiry_batch",
    "NoteAttachmentRequestInquiryBatchCreate": ".note_attachment_request_inquiry_batch_create",
    "NoteAttachmentRequestInquiryBatchDelete": ".note_attachment_request_inquiry_batch_delete",
    "NoteAttachmentRequestInquiryBatchListing": ".note_attachment_request_inquiry_batch_listing",
    "NoteAttachmentRequestInquiryBatchRead": ".note_attachment_request_inquiry_batch_read",
    "NoteAttachmentRequestInquiryBatchUpdate": ".note_attachment_request_inquiry_batch_update",
    "NoteAttachmentRequestInquiryCreate": ".note_attachment_request_inquiry_create",
    "NoteAttachmentRequestInquiryDelete": ".note_attachment_request_inquiry_delete",
    "NoteAttachmentRequestInquiryListing": ".note_attachment_request_inquiry_listing",
    "NoteAttachmentRequestInquiryRead": ".note_attachment_request_inquiry_read",
    "NoteAttachmentRequestInquiryUpdate": ".note_attachment_request_inquiry_update",
    "NoteAttachmentRequestResponse": ".note_attachment_request_response",
    "NoteAttachmentRequestResponseCreate": ".note_attachment_request_response_create",
    "NoteAttachmentRequestResponseDelete": ".note_attachment_request_response_delete",
    "NoteAttachmentRequestResponseListing": ".note_attachment_request_response_listing",
    "NoteAttachmentRequestResponseRead": ".note_attachment_request_response_read",
    "NoteAttachmentRequestResponseUpdate": ".note_attachment_request_response_update",
    "NoteAttachmentScheduleInstance": ".note_attachment_schedule_instance",
    "NoteAttachmentScheduleInstanceCreate": ".note_attachment_schedule_instance_create",
    "NoteAttachmentScheduleInstanceDelete": ".note_attachment_schedule_instance_delete",
    "NoteAttachmentScheduleInstanceListing": ".note_attachment_schedule_instance_listing",
    "NoteAttachmentScheduleInstanceRead": ".note_attachment_schedule_instance_read",
    "NoteAttachmentScheduleInstanceUpdate": ".note_attachment_schedule_instance_update",
    "NoteAttachmentSchedulePayment": ".note_attachment_schedule_payment",
    "NoteAttachmentSchedulePaymentBatch": ".note_attachment_schedule_payment_batch",
    "NoteAttachmentSchedulePaymentBatchCreate": ".note_attachment_schedule_payment_batch_create",
    "NoteAttachmentSchedulePaymentBatchDelete": ".note_attachment_schedule_payment_batch_delete",
    "NoteAttachmentSchedulePaymentBatchListing": ".note_attachment_schedule_payment_batch_listing",
    "NoteAttachmentSchedulePaymentBatchRead": ".note_attachment_schedule_payment_batch_read",
    "NoteAttachmentSchedulePaymentBatchUpdate": ".note_attachment_schedule_payment_batch_update",
    "NoteAttachmentSchedulePaymentCreate": ".note_attachment_schedule_payment_create",
    "NoteAttachmentSchedulePaymentDelete": ".note_attachment_schedule_payment_delete",
    "NoteAttachmentSchedulePaymentListing": ".note_attachment_schedule_payment_listing",
    "NoteAttachmentSchedulePaymentRead": ".note_attachment_schedule_payment_read",
    "NoteAttachmentSchedulePaymentUpdate": ".note_attachment_schedule_payment_update",
    "NoteAttachmentSofortMerchantTransaction": ".note_attachment_sofort_merchant_transaction",
    "NoteAttachmentSofortMerchantTransactionCreate": ".note_attachment_sofort_merchant_transaction_create",
    "NoteAttachmentSofortMerchantTransactionDelete": ".note_attachment_sofort_merchant_transaction_delete",
    "NoteAttachmentSofortMerchantTransactionListing": ".note_attachment_sofort_merchant_transaction_listing",
    "NoteAttachmentSofortMerchantTransactionRead": ".note_attachment_sofort_merchant_transaction_read",
    "NoteAttachmentSofortMerchantTransactionUpdate": ".note_attachment_sofort_merchant_transaction_update",
    "NoteAttachmentWhitelistResult": ".note_attachment_whitelist_result",
    "NoteAttachmentWhitelistResultCreate": ".note_attachment_whitelist_result_create",
    "NoteAttachmentWhitelistResultDelete": ".note_attachment_whitelist_result_delete",
    "NoteAttachmentWhitelistResultListing": ".note_attachment_whitelist_result_listing",
    "NoteAttachmentWhitelistResultRead": ".note_attachment_whitelist_result_read",
    "NoteAttachmentWhitelistResultUpdate": ".note_attachment_whitelist_result_update",
    "NoteTextBankSwitchServiceNetherlandsIncomingPayment": ".note_text_bank_switch_service_netherlands_incoming_payment",
    "NoteTextBankSwitchServiceNetherlandsIncomingPaymentCreate": ".note_text_bank_switch_service_netherlands_incoming_payment_create",
    "NoteTextBankSwitchServiceNetherlandsIncomingPaymentDelete": ".note_text_bank_switch_service_netherlands_incoming_payment_delete",
    "NoteTextBankSwitchServiceNetherlandsIncomingPaymentListing": ".note_text_bank_switch_service_netherlands_incoming_payment_listing",
    "NoteTextBankSwitchServiceNetherlandsIncomingPaymentRead": ".note_text_bank_switch_service_netherlands_incoming_payment_read",
    "NoteTextBankSwitchServiceNetherlandsIncomingPaymentUpdate": ".note_text_bank_switch_service_netherlands_incoming_payment_update",
    "NoteTextBunqMeFundraiserResult": ".note_text_bunq_me_fundraiser_result",
    "NoteTextBunqMeFundraiserResultCreate": ".note_text_bunq_me_fundraiser_result_create",
    "NoteTextBunqMeFundraiserResultDelete": ".note_text_bunq_me_fundraiser_result_delete",
    "NoteTextBunqMeFundraiserResultListing": ".note_text_bunq_me_fundraiser_result_listing",
    "NoteTextBunqMeFundraiserResultRead": ".note_text_bunq_me_fundraiser_result_read",
    "NoteTextBunqMeFundraiserResultUpdate": ".note_text_bunq_me_fundraiser_result_update",
    "NoteTextDraftPayment": ".note_text_draft_payment",
    "NoteTextDraftPaymentCreate": ".note_text_draft_payment_create",
    "NoteTextDraftPaymentDelete": ".note_text_draft_payment_delete",
    "NoteTextDraftPaymentListing": ".note_text_draft_payment_listing",
    "NoteTextDraftPaymentRead": ".note_text_draft_payment_read",
    "NoteTextDraftPaymentUpdate": ".note_text_draft_payment_update",
    "NoteTextIdealMerchantTransaction": ".note_text_ideal_merchant_transaction",
    "NoteTextIdealMerchantTransactionCreate": ".note_text_ideal_merchant_transaction_create",
    "NoteTextIdealMerchantTransactionDelete": ".note_text_ideal_merchant_transaction_delete",
    "NoteTextIdealMerchantTransactionListing": ".note_text_ideal_merchant_transaction_listing",
    "NoteTextIdealMerchantTransactionRead": ".note_text_ideal_merchant_transaction_read",
    "NoteTextIdealMerchantTransactionUpdate": ".note_text_ideal_merchant_transaction_update",
    "NoteTextMasterCardAction": ".note_text_master_card_action",
    "NoteTextMasterCardActionCreate": ".note_text_master_card_action_create",
    "NoteTextMasterCardActionDelete": ".note_text_master_card_action_delete",
    "NoteTextMasterCardActionListing": ".note_text_master_card_action_listing",
    "NoteTextMasterCardActionRead": ".note_text_master_card_action_read",
    "NoteTextMasterCardActionUpdate": ".note_text_master_card_action_update",
    "NoteTextPayment": ".note_text_payment",
    "NoteTextPaymentBatch": ".note_text_payment_batch",
    "NoteTextPaymentBatchCreate": ".note_text_payment_batch_create",
    "NoteTextPaymentBatchDelete": ".note_text_payment_batch_delete",
    "NoteTextPaymentBatchListing": ".note_text_payment_batch_listing",
    "NoteTextPaymentBatchRead": ".note_text_payment_batch_read",
    "NoteTextPaymentBatchUpdate": ".note_text_payment_batch_update",
    "NoteTextPaymentCreate": ".note_text_payment_create",
    "NoteTextPaymentDelete": ".note_text_payment_delete",
    "NoteTextPaymentListing": ".note_text_payment_listing",
    "NoteTextPaymentRead": ".note_text_payment_read",
    "NoteTextPaymentUpdate": ".note_text_payment_update",
    "NoteTextRequestInquiry": ".note_text_request_inquiry",
    "NoteTextRequestInquiryBatch": ".note_text_request_inquiry_batch",
    "NoteTextRequestInquiryBatchCreate": ".note_text_request_inquiry_batch_create",
    "NoteTextRequestInquiryBatchDelete": ".note_text_request_inquiry_batch_delete",
    "NoteTextRequestInquiryBatchListing": ".note_text_request_inquiry_batch_listing",
    "NoteTextRequestInquiryBatchRead": ".note_text_request_inquiry_batch_read",
    "NoteTextRequestInquiryBatchUpdate": ".note_text_request_inquiry_batch_update",
    "NoteTextRequestInquiryCreate": ".note_text_request_inquiry_create",
    "NoteTextRequestInquiryDelete": ".note_text_request_inquiry_delete",
    "NoteTextRequestInquiryListing": ".note_text_request_inquiry_listing",
    "NoteTextRequestInquiryRead": ".note_text_request_inquiry_read",
    "NoteTextRequestInquiryUpdate": ".note_text_request_inquiry_update",
    "NoteTextRequestResponse": ".note_text_request_response",
    "NoteTextRequestResponseCreate": ".note_text_request_response_create",
    "NoteTextRequestResponseDelete": ".note_text_request_response_delete",
    "NoteTextRequestResponseListing": ".note_text_request_response_listing",
    "NoteTextRequestResponseRead": ".note_text_request_response_read",
    "NoteTextRequestResponseUpdate": ".note_text_request_response_update",
    "NoteTextScheduleInstance": ".note_text_schedule_instance",
    "NoteTextScheduleInstanceCreate": ".note_text_schedule_instance_create",
    "NoteTextScheduleInstanceDelete": ".note_text_schedule_instance_delete",
    "NoteTextScheduleInstanceListing": ".note_text_schedule_instance_listing",
    "NoteTextScheduleInstanceRead": ".note_text_schedule_instance_read",
    "NoteTextScheduleInstanceUpdate": ".note_text_schedule_instance_update",
    "NoteTextSchedulePayment": ".note_text_schedule_payment",
    "NoteTextSchedulePaymentBatch": ".note_text_schedule_payment_batch",
    "NoteTextSchedulePaymentBatchCreate": ".note_text_schedule_payment_batch_create",
    "NoteTextSchedulePaymentBatchDelete": ".note_text_schedule_payment_batch_delete",
    "NoteTextSchedulePaymentBatchListing": ".note_text_schedule_payment_batch_listing",
    "NoteTextSchedulePaymentBatchRead": ".note_text_schedule_payment_batch_read",
    "NoteTextSchedulePaymentBatchUpdate": ".note_text_schedule_payment_batch_update",
    "NoteTextSchedulePaymentCreate": ".note_text_schedule_payment_create",
    "NoteTextSchedulePaymentDelete": ".note_text_schedule_payment_delete",
    "NoteTextSchedulePaymentListing": ".note_text_schedule_payment_listing",
    "NoteTextSchedulePaymentRead": ".note_text_schedule_payment_read",
    "NoteTextSchedulePaymentUpdate": ".note_text_schedule_payment_update",
    "NoteTextSofortMerchantTransaction": ".note_text_sofort_merchant_transaction",
    "NoteTextSofortMerchantTransactionCreate": ".note_text_sofort_merchant_transaction_create",
    "NoteTextSofortMerchantTransactionDelete": ".note_text_sofort_merchant_transaction_delete",
    "NoteTextSofortMerchantTransactionListing": ".note_text_sofort_merchant_transaction_listing",
    "NoteTextSofortMerchantTransactionRead": ".note_text_sofort_merchant_transaction_read",
    "NoteTextSofortMerchantTransactionUpdate": ".note_text_sofort_merchant_transaction_update",
    "NoteTextWhitelistResult": ".note_text_whitelist_result",
    "NoteTextWhitelistResultCreate": ".note_text_whitelist_result_create",
    "NoteTextWhitelistResultDelete": ".note_text_whitelist_result_delete",
    "NoteTextWhitelistResultListing": ".note_text_whitelist_result_listing",
    "NoteTextWhitelistResultRead": ".note_text_whitelist_result_read",
    "NoteTextWhitelistResultUpdate": ".note_text_whitelist_result_update",
    "NotificationFilter": ".notification_filter",
    "NotificationFilterEmail": ".notification_filter_email",
    "NotificationFilterEmailCreate": ".notification_filter_email_create",
    "NotificationFilterEmailListing": ".notification_filter_email_listing",
    "NotificationFilterPush": ".notification_filter_push",
    "NotificationFilterPushCreate": ".notification_filter_push_create",
    "NotificationFilterPushListing": ".notification_filter_push_listing",
    "NotificationFilterUrl": ".notification_filter_url",
    "NotificationFilterUrlCreate": ".notification_filter_url_create",
    "NotificationFilterUrlListing": ".notification_filter_url_listing",
    "NotificationFilterUrlMonetaryAccountCreate": ".notification_filter_url_monetary_account_create",
    "NotificationFilterUrlMonetaryAccountListing": ".notification_filter_url_monetary_account_listing",
    "OauthCallbackUrl": ".oauth_callback_url",
    "OauthCallbackUrlCreate": ".oauth_callback_url_create",
    "OauthCallbackUrlDelete": ".oauth_callback_url_delete",
    "OauthCallbackUrlListing": ".oauth_callback_url_listing",
    "OauthCallbackUrlRead": ".oauth_callback_url_read",
    "OauthCallbackUrlUpdate": ".oauth_callback_url_update",
    "OauthClient": ".oauth_client",
    "OauthClientCreate": ".oauth_client_create",
    "OauthClientListing": ".oauth_client_listing",
    "OauthClientRead": ".oauth_client_read",
    "OauthClientUpdate": ".oauth_client_update",
    "Payment": ".payment",
    "PaymentAutoAllocate": ".payment_auto_allocate",
    "PaymentAutoAllocateCreate": ".payment_auto_allocate_create",
    "PaymentAutoAllocateDefinition": ".payment_auto_allocate_definition",
    "PaymentAutoAllocateDefinitionListing": ".payment_auto_allocate_definition_listing",
    "PaymentAutoAllocateDelete": ".payment_auto_allocate_delete",
    "PaymentAutoAllocateInstance": ".payment_auto_allocate_instance",
    "PaymentAutoAllocateInstanceListing": ".payment_auto_allocate_instance_listing",
    "PaymentAutoAllocateInstanceRead": ".payment_auto_allocate_instance_read",
    "PaymentAutoAllocateListing": ".payment_auto_allocate_listing",
    "PaymentAutoAllocateRead": ".payment_auto_allocate_read",
    "PaymentAutoAllocateUpdate": ".payment_auto_allocate_update",
    "PaymentAutoAllocateUserListing": ".payment_auto_allocate_user_listing",
    "PaymentBatch": ".payment_batch",
    "PaymentBatchAnchoredPayment": ".payment_batch_anchored_payment",
    "PaymentBatchCreate": ".payment_batch_create",
    "PaymentBatchListing": ".payment_batch_listing",
    "PaymentBatchRead": ".payment_batch_read",
    "PaymentBatchUpdate": ".payment_batch_update",
    "PaymentCreate": ".payment_create",
    "PaymentListing": ".payment_listing",
    "PaymentRead": ".payment_read",
    "PaymentServiceProviderCredentialCreate": ".payment_service_provider_credential_create",
    "PaymentServiceProviderCredentialRead": ".payment_service_provider_credential_read",
    "PaymentServiceProviderDraftPayment": ".payment_service_provider_draft_payment",
    "PaymentServiceProviderDraftPaymentCreate": ".payment_service_provider_draft_payment_create",
    "PaymentServiceProviderDraftPaymentListing": ".payment_service_provider_draft_payment_listing",
    "PaymentServiceProviderDraftPaymentRead": ".payment_service_provider_draft_payment_read",
    "PaymentServiceProviderDraftPaymentUpdate": ".payment_service_provider_draft_payment_update",
    "PermittedDevice": ".permitted_device",
    "PermittedIp": ".permitted_ip",
    "PermittedIpCreate": ".permitted_ip_create",
    "PermittedIpListing": ".permitted_ip_listing",
    "PermittedIpRead": ".permitted_ip_read",
    "PermittedIpUpdate": ".permitted_ip_update",
    "PlacePhotoLookupContentListing": ".place_photo_lookup_content_listing",
    "Pointer": ".pointer",
    "RegistryMembership": ".registry_membership",
    "RegistrySettlement": ".registry_settlement",
    "RegistrySettlementCreate": ".registry_settlement_create",
    "RegistrySettlementItem": ".registry_settlement_item",
    "RegistrySettlementListing": ".registry_settlement_listing",
    "RegistrySettlementRead": ".registry_settlement_read",
    "RelationUser": ".relation_user",
    "RequestInquiry": ".request_inquiry",
    "RequestInquiryBatch": ".request_inquiry_batch",
    "RequestInquiryBatchCreate": ".request_inquiry_batch_create",
    "RequestInquiryBatchListing": ".request_inquiry_batch_listing",
    "RequestInquiryBatchRead": ".request_inquiry_batch_read",
    "RequestInquiryBatchUpdate": ".request_inquiry_batch_update",
    "RequestInquiryCreate": ".request_inquiry_create",
    "RequestInquiryListing": ".request_inquiry_listing",
    "RequestInquiryRead": ".request_inquiry_read",
    "RequestInquiryReference": ".request_inquiry_reference",
    "RequestInquiryUpdate": ".request_inquiry_update",
    "RequestReferenceSplitTheBillAnchorObject": ".request_reference_split_the_bill_anchor_object",
    "RequestResponse": ".request_response",
    "RequestResponseListing": ".request_response_listing",
    "RequestResponseRead": ".request_response_read",
    "RequestResponseUpdate": ".request_response_update",
    "RewardListing": ".reward_listing",
    "RewardRead": ".reward_read",
    "RewardRecipient": ".reward_recipient",
    "RewardRecipientListing": ".reward_recipient_listing",
    "RewardRecipientRead": ".reward_recipient_read",
    "RewardSender": ".reward_sender",
    "RewardSenderListing": ".reward_sender_listing",
    "RewardSenderRead": ".reward_sender_read",
    "SandboxUserCompany": ".sandbox_user_company",
    "SandboxUserCompanyCreate": ".sandbox_user_company_create",
    "SandboxUserPerson": ".sandbox_user_person",
    "SandboxUserPersonCreate": ".sandbox_user_person_create",
    "Schedule": ".schedule",
    "ScheduleAnchorObject": ".schedule_anchor_object",
    "ScheduleInstance": ".schedule_instance",
    "ScheduleInstanceAnchorObject": ".schedule_instance_anchor_object",
    "ScheduleInstanceListing": ".schedule_instance_listing",
    "ScheduleInstanceRead": ".schedule_instance_read",
    "ScheduleInstanceUpdate": ".schedule_instance_update",
    "ScheduleListing": ".schedule_listing",
    "SchedulePayment": ".schedule_payment",
    "SchedulePaymentBatch": ".schedule_payment_batch",
    "SchedulePaymentBatchCreate": ".schedule_payment_batch_create",
    "SchedulePaymentBatchDelete": ".schedule_payment_batch_delete",
    "SchedulePaymentBatchRead": ".schedule_payment_batch_read",
    "SchedulePaymentBatchUpdate": ".schedule_payment_batch_update",
    "SchedulePaymentCreate": ".schedule_payment_create",
    "SchedulePaymentDelete": ".schedule_payment_delete",
    "SchedulePaymentEntry": ".schedule_payment_entry",
    "SchedulePaymentListing": ".schedule_payment_listing",
    "SchedulePaymentRead": ".schedule_payment_read",
    "SchedulePaymentUpdate": ".schedule_payment_update",
    "ScheduleRead": ".schedule_read",
    "ScheduleUserListing": ".schedule_user_listing",
    "ServerError": ".server_error",
    "ServerErrorCreate": ".server_error_create",
    "SessionDelete": ".session_delete",
    "SessionServerCreate": ".session_server_create",
    "SessionServerToken": ".session_server_token",
    "ShareDetail": ".share_detail",
    "ShareDetailDraftPayment": ".share_detail_draft_payment",
    "ShareDetailPayment": ".share_detail_payment",
    "ShareDetailReadOnly": ".share_detail_read_only",
    "ShareInviteMonetaryAccountInquiry": ".share_invite_monetary_account_inquiry",
    "ShareInviteMonetaryAccountInquiryCreate": ".share_invite_monetary_account_inquiry_create",
    "ShareInviteMonetaryAccountInquiryListing": ".share_invite_monetary_account_inquiry_listing",
    "ShareInviteMonetaryAccountInquiryRead": ".share_invite_monetary_account_inquiry_read",
    "ShareInviteMonetaryAccountInquiryUpdate": ".share_invite_monetary_account_inquiry_update",
    "ShareInviteMonetaryAccountResponse": ".share_invite_monetary_account_response",
    "ShareInviteMonetaryAccountResponseListing": ".share_invite_monetary_account_response_listing",
    "ShareInviteMonetaryAccountResponseRead": ".share_invite_monetary_account_response_read",
    "ShareInviteMonetaryAccountResponseUpdate": ".share_invite_monetary_account_response_update",
    "SofortMerchantTransaction": ".sofort_merchant_transaction",
    "SofortMerchantTransactionListing": ".sofort_merchant_transaction_listing",
    "SofortMerchantTransactionRead": ".sofort_merchant_transaction_read",
    "TaxResident": ".tax_resident",
    "TokenQrRequestIdealCreate": ".token_qr_request_ideal_create",
    "TokenQrRequestSofortCreate": ".token_qr_request_sofort_create",
    "TransferwiseAccountQuoteCreate": ".transferwise_account_quote_create",
    "TransferwiseAccountQuoteDelete": ".transferwise_account_quote_delete",
    "TransferwiseAccountQuoteListing": ".transferwise_account_quote_listing",
    "TransferwiseAccountQuoteRead": ".transferwise_account_quote_read",
    "TransferwiseAccountRequirementCreate": ".transferwise_account_requirement_create",
    "TransferwiseAccountRequirementListing": ".transferwise_account_requirement_listing",
    "TransferwiseCurrencyListing": ".transferwise_currency_listing",
    "TransferwiseQuote": ".transferwise_quote",
    "TransferwiseQuoteCreate": ".transferwise_quote_create",
    "TransferwiseQuoteRead": ".transferwise_quote_read",
    "TransferwiseQuoteTemporaryCreate": ".transferwise_quote_temporary_create",
    "TransferwiseQuoteTemporaryRead": ".transferwise_quote_temporary_read",
    "TransferwiseRequirementField": ".transferwise_requirement_field",
    "TransferwiseRequirementFieldGroup": ".transferwise_requirement_field_group",
    "TransferwiseRequirementFieldGroupValidationAsync": ".transferwise_requirement_field_group_validation_async",
    "TransferwiseRequirementFieldGroupValidationAsyncParams": ".transferwise_requirement_field_group_validation_async_params",
    "TransferwiseRequirementFieldGroupValuesAllowed": ".transferwise_requirement_field_group_values_allowed",
    "TransferwiseTransfer": ".transferwise_transfer",
    "TransferwiseTransferCreate": ".transferwise_transfer_create",
    "TransferwiseTransferListing": ".transferwise_transfer_listing",
    "TransferwiseTransferRead": ".transferwise_transfer_read",
    "TransferwiseTransferRequirementCreate": ".transferwise_transfer_requirement_create",
    "TransferwiseUserCreate": ".transferwise_user_create",
    "TransferwiseUserListing": ".transferwise_user_listing",
    "TranslinkTransactionCreate": ".translink_transaction_create",
    "TranslinkTransactionEntry": ".translink_transaction_entry",
    "TranslinkTransactionListing": ".translink_transaction_listing",
    "TranslinkTransactionRead": ".translink_transaction_read",
    "TreeProgressListing": ".tree_progress_listing",
    "Ubo": ".ubo",
    "UserApiKey": ".user_api_key",
    "UserApiKeyAnchoredUser": ".user_api_key_anchored_user",
    "UserCompany": ".user_company",
    "UserCompanyNameListing": ".user_company_name_listing",
    "UserCompanyRead": ".user_company_read",
    "UserCompanyUpdate": ".user_company_update",
    "UserCredentialPasswordIpListing": ".user_credential_password_ip_listing",
    "UserCredentialPasswordIpRead": ".user_credential_password_ip_read",
    "UserLegalNameListing": ".user_legal_name_listing",
    "UserListing": ".user_listing",
    "UserPaymentServiceProvider": ".user_payment_service_provider",
    "UserPaymentServiceProviderRead": ".user_payment_service_provider_read",
    "UserPerson": ".user_person",
    "UserPersonRead": ".user_person_read",
    "UserPersonUpdate": ".user_person_update",
    "UserRead": ".user_read",
    "Whitelist": ".whitelist",
    "WhitelistResult": ".whitelist_result",
    "WhitelistResultViewAnchoredObject": ".whitelist_result_view_anchored_object",
    "WhitelistSddListing": ".whitelist_sdd_listing",
    "WhitelistSddMonetaryAccountPayingListing": ".whitelist_sdd_monetary_account_paying_listing",
    "WhitelistSddMonetaryAccountPayingRead": ".whitelist_sdd_monetary_account_paying_read",
    "WhitelistSddOneOff": ".whitelist_sdd_one_off",
    "WhitelistSddOneOffCreate": ".whitelist_sdd_one_off_create",
    "WhitelistSddOneOffDelete": ".whitelist_sdd_one_off_delete",
    "WhitelistSddOneOffListing": ".whitelist_sdd_one_off_listing",
    "WhitelistSddOneOffRead": ".whitelist_sdd_one_off_read",
    "WhitelistSddOneOffUpdate": ".whitelist_sdd_one_off_update",
    "WhitelistSddRead": ".whitelist_sdd_read",
    "WhitelistSddRecurring": ".whitelist_sdd_recurring",
    "WhitelistSddRecurringCreate": ".whitelist_sdd_recurring_create",
    "WhitelistSddRecurringDelete": ".whitelist_sdd_recurring_delete",
    "WhitelistSddRecurringListing": ".whitelist_sdd_recurring_listing",
    "WhitelistSddRecurringRead": ".whitelist_sdd_recurring_read",
    "WhitelistSddRecurringUpdate": ".whitelist_sdd_recurring_update",
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
    "AdditionalInformation",
    "Address",
    "Amount",
    "Attachment",
    "AttachmentConversationContentListing",
    "AttachmentMasterCardActionRefund",
    "AttachmentMonetaryAccount",
    "AttachmentMonetaryAccountContentListing",
    "AttachmentMonetaryAccountCreate",
    "AttachmentMonetaryAccountPayment",
    "AttachmentPublic",
    "AttachmentPublicContentListing",
    "AttachmentPublicCreate",
    "AttachmentPublicRead",
    "AttachmentUrl",
    "AttachmentUserContentListing",
    "AttachmentUserRead",
    "Avatar",
    "AvatarCreate",
    "AvatarRead",
    "BadRequestErrorBody",
    "BankSwitchServiceNetherlandsIncoming",
    "BankSwitchServiceNetherlandsIncomingPayment",
    "BankSwitchServiceNetherlandsIncomingPaymentRead",
    "BillingContractSubscription",
    "BillingContractSubscriptionListing",
    "BirdeeInvestmentPortfolio",
    "BirdeeInvestmentPortfolioBalance",
    "BirdeeInvestmentPortfolioGoal",
    "BirdeePortfolioAllocation",
    "BunqId",
    "BunqMeFundraiserProfile",
    "BunqMeFundraiserProfileUserListing",
    "BunqMeFundraiserProfileUserRead",
    "BunqMeFundraiserResult",
    "BunqMeFundraiserResultRead",
    "BunqMeMerchantAvailable",
    "BunqMeTab",
    "BunqMeTabCreate",
    "BunqMeTabEntry",
    "BunqMeTabListing",
    "BunqMeTabRead",
    "BunqMeTabResultInquiry",
    "BunqMeTabResultResponse",
    "BunqMeTabResultResponseRead",
    "BunqMeTabUpdate",
    "Card",
    "CardBatchCreate",
    "CardBatchEntry",
    "CardBatchReplaceCreate",
    "CardBatchReplaceEntry",
    "CardCountryPermission",
    "CardCreditCreate",
    "CardDebit",
    "CardDebitCreate",
    "CardGeneratedCvc2",
    "CardGeneratedCvc2Create",
    "CardGeneratedCvc2Listing",
    "CardGeneratedCvc2Read",
    "CardGeneratedCvc2Update",
    "CardListing",
    "CardNameListing",
    "CardPinAssignment",
    "CardPrimaryAccountNumber",
    "CardRead",
    "CardReplaceCreate",
    "CardUpdate",
    "Certificate",
    "CertificatePinnedCreate",
    "CertificatePinnedDelete",
    "CertificatePinnedListing",
    "CertificatePinnedRead",
    "CoOwner",
    "Company",
    "CompanyCreate",
    "CompanyListing",
    "CompanyRead",
    "CompanyUpdate",
    "CompanyVatNumber",
    "ConfirmationOfFundsCreate",
    "CurrencyCloudBeneficiaryCreate",
    "CurrencyCloudBeneficiaryListing",
    "CurrencyCloudBeneficiaryRead",
    "CurrencyCloudBeneficiaryRequirementField",
    "CurrencyCloudBeneficiaryRequirementListing",
    "CurrencyCloudPaymentQuoteCreate",
    "CurrencyConversionListing",
    "CurrencyConversionQuote",
    "CurrencyConversionQuoteCreate",
    "CurrencyConversionQuoteRead",
    "CurrencyConversionQuoteUpdate",
    "CurrencyConversionRead",
    "Customer",
    "CustomerLimit",
    "CustomerLimitListing",
    "DeviceListing",
    "DeviceRead",
    "DeviceServer",
    "DeviceServerCreate",
    "DeviceServerListing",
    "DeviceServerRead",
    "DraftPayment",
    "DraftPaymentAnchorObject",
    "DraftPaymentCreate",
    "DraftPaymentEntry",
    "DraftPaymentListing",
    "DraftPaymentRead",
    "DraftPaymentResponse",
    "DraftPaymentUpdate",
    "Error",
    "ErrorItem",
    "EventListing",
    "EventObject",
    "EventRead",
    "ExportAnnualOverviewContentListing",
    "ExportAnnualOverviewCreate",
    "ExportAnnualOverviewDelete",
    "ExportAnnualOverviewListing",
    "ExportAnnualOverviewRead",
    "ExportRib",
    "ExportRibContentListing",
    "ExportRibCreate",
    "ExportRibDelete",
    "ExportRibListing",
    "ExportRibRead",
    "ExportStatementCardContentListing",
    "ExportStatementCardCsvCreate",
    "ExportStatementCardCsvDelete",
    "ExportStatementCardCsvListing",
    "ExportStatementCardCsvRead",
    "ExportStatementCardListing",
    "ExportStatementCardPdfCreate",
    "ExportStatementCardPdfDelete",
    "ExportStatementCardPdfListing",
    "ExportStatementCardPdfRead",
    "ExportStatementCardRead",
    "ExportStatementContentListing",
    "ExportStatementCreate",
    "ExportStatementDelete",
    "ExportStatementListing",
    "ExportStatementPayment",
    "ExportStatementPaymentContentListing",
    "ExportStatementPaymentCreate",
    "ExportStatementPaymentRead",
    "ExportStatementRead",
    "FeatureAnnouncement",
    "FeatureAnnouncementRead",
    "Geolocation",
    "IdealMerchantTransaction",
    "IdealMerchantTransactionCreate",
    "IdealMerchantTransactionListing",
    "IdealMerchantTransactionRead",
    "Image",
    "InsightEventListing",
    "InsightListing",
    "InsightPreferenceDateListing",
    "InstallationCreate",
    "InstallationListing",
    "InstallationRead",
    "InstallationServerPublicKey",
    "InstallationServerPublicKeyListing",
    "InstallationToken",
    "Invoice",
    "InvoiceByUserListing",
    "InvoiceByUserRead",
    "InvoiceExportPdfContentListing",
    "InvoiceItem",
    "InvoiceItemGroup",
    "InvoiceListing",
    "InvoiceRead",
    "Issuer",
    "LabelCard",
    "LabelMonetaryAccount",
    "LabelUser",
    "MasterCardAction",
    "MasterCardActionListing",
    "MasterCardActionRead",
    "MasterCardActionReference",
    "MasterCardActionRefund",
    "MasterCardIdentityCheckChallengeRequestUserRead",
    "MasterCardIdentityCheckChallengeRequestUserUpdate",
    "MasterCardPaymentListing",
    "MonetaryAccountBank",
    "MonetaryAccountBankCreate",
    "MonetaryAccountBankListing",
    "MonetaryAccountBankRead",
    "MonetaryAccountBankUpdate",
    "MonetaryAccountExternal",
    "MonetaryAccountExternalListing",
    "MonetaryAccountExternalRead",
    "MonetaryAccountInvestment",
    "MonetaryAccountJoint",
    "MonetaryAccountJointCreate",
    "MonetaryAccountJointListing",
    "MonetaryAccountJointRead",
    "MonetaryAccountJointUpdate",
    "MonetaryAccountLight",
    "MonetaryAccountListing",
    "MonetaryAccountProfile",
    "MonetaryAccountProfileDrain",
    "MonetaryAccountProfileFill",
    "MonetaryAccountRead",
    "MonetaryAccountSavings",
    "MonetaryAccountSavingsCreate",
    "MonetaryAccountSavingsListing",
    "MonetaryAccountSavingsRead",
    "MonetaryAccountSavingsUpdate",
    "MonetaryAccountSetting",
    "NoteAttachmentBankSwitchServiceNetherlandsIncomingPayment",
    "NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentCreate",
    "NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentDelete",
    "NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentListing",
    "NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentRead",
    "NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentUpdate",
    "NoteAttachmentBunqMeFundraiserResult",
    "NoteAttachmentBunqMeFundraiserResultCreate",
    "NoteAttachmentBunqMeFundraiserResultDelete",
    "NoteAttachmentBunqMeFundraiserResultListing",
    "NoteAttachmentBunqMeFundraiserResultRead",
    "NoteAttachmentBunqMeFundraiserResultUpdate",
    "NoteAttachmentDraftPayment",
    "NoteAttachmentDraftPaymentCreate",
    "NoteAttachmentDraftPaymentDelete",
    "NoteAttachmentDraftPaymentListing",
    "NoteAttachmentDraftPaymentRead",
    "NoteAttachmentDraftPaymentUpdate",
    "NoteAttachmentIdealMerchantTransaction",
    "NoteAttachmentIdealMerchantTransactionCreate",
    "NoteAttachmentIdealMerchantTransactionDelete",
    "NoteAttachmentIdealMerchantTransactionListing",
    "NoteAttachmentIdealMerchantTransactionRead",
    "NoteAttachmentIdealMerchantTransactionUpdate",
    "NoteAttachmentMasterCardAction",
    "NoteAttachmentMasterCardActionCreate",
    "NoteAttachmentMasterCardActionDelete",
    "NoteAttachmentMasterCardActionListing",
    "NoteAttachmentMasterCardActionRead",
    "NoteAttachmentMasterCardActionUpdate",
    "NoteAttachmentPayment",
    "NoteAttachmentPaymentBatch",
    "NoteAttachmentPaymentBatchCreate",
    "NoteAttachmentPaymentBatchDelete",
    "NoteAttachmentPaymentBatchListing",
    "NoteAttachmentPaymentBatchRead",
    "NoteAttachmentPaymentBatchUpdate",
    "NoteAttachmentPaymentCreate",
    "NoteAttachmentPaymentDelete",
    "NoteAttachmentPaymentListing",
    "NoteAttachmentPaymentRead",
    "NoteAttachmentPaymentUpdate",
    "NoteAttachmentRequestInquiry",
    "NoteAttachmentRequestInquiryBatch",
    "NoteAttachmentRequestInquiryBatchCreate",
    "NoteAttachmentRequestInquiryBatchDelete",
    "NoteAttachmentRequestInquiryBatchListing",
    "NoteAttachmentRequestInquiryBatchRead",
    "NoteAttachmentRequestInquiryBatchUpdate",
    "NoteAttachmentRequestInquiryCreate",
    "NoteAttachmentRequestInquiryDelete",
    "NoteAttachmentRequestInquiryListing",
    "NoteAttachmentRequestInquiryRead",
    "NoteAttachmentRequestInquiryUpdate",
    "NoteAttachmentRequestResponse",
    "NoteAttachmentRequestResponseCreate",
    "NoteAttachmentRequestResponseDelete",
    "NoteAttachmentRequestResponseListing",
    "NoteAttachmentRequestResponseRead",
    "NoteAttachmentRequestResponseUpdate",
    "NoteAttachmentScheduleInstance",
    "NoteAttachmentScheduleInstanceCreate",
    "NoteAttachmentScheduleInstanceDelete",
    "NoteAttachmentScheduleInstanceListing",
    "NoteAttachmentScheduleInstanceRead",
    "NoteAttachmentScheduleInstanceUpdate",
    "NoteAttachmentSchedulePayment",
    "NoteAttachmentSchedulePaymentBatch",
    "NoteAttachmentSchedulePaymentBatchCreate",
    "NoteAttachmentSchedulePaymentBatchDelete",
    "NoteAttachmentSchedulePaymentBatchListing",
    "NoteAttachmentSchedulePaymentBatchRead",
    "NoteAttachmentSchedulePaymentBatchUpdate",
    "NoteAttachmentSchedulePaymentCreate",
    "NoteAttachmentSchedulePaymentDelete",
    "NoteAttachmentSchedulePaymentListing",
    "NoteAttachmentSchedulePaymentRead",
    "NoteAttachmentSchedulePaymentUpdate",
    "NoteAttachmentSofortMerchantTransaction",
    "NoteAttachmentSofortMerchantTransactionCreate",
    "NoteAttachmentSofortMerchantTransactionDelete",
    "NoteAttachmentSofortMerchantTransactionListing",
    "NoteAttachmentSofortMerchantTransactionRead",
    "NoteAttachmentSofortMerchantTransactionUpdate",
    "NoteAttachmentWhitelistResult",
    "NoteAttachmentWhitelistResultCreate",
    "NoteAttachmentWhitelistResultDelete",
    "NoteAttachmentWhitelistResultListing",
    "NoteAttachmentWhitelistResultRead",
    "NoteAttachmentWhitelistResultUpdate",
    "NoteTextBankSwitchServiceNetherlandsIncomingPayment",
    "NoteTextBankSwitchServiceNetherlandsIncomingPaymentCreate",
    "NoteTextBankSwitchServiceNetherlandsIncomingPaymentDelete",
    "NoteTextBankSwitchServiceNetherlandsIncomingPaymentListing",
    "NoteTextBankSwitchServiceNetherlandsIncomingPaymentRead",
    "NoteTextBankSwitchServiceNetherlandsIncomingPaymentUpdate",
    "NoteTextBunqMeFundraiserResult",
    "NoteTextBunqMeFundraiserResultCreate",
    "NoteTextBunqMeFundraiserResultDelete",
    "NoteTextBunqMeFundraiserResultListing",
    "NoteTextBunqMeFundraiserResultRead",
    "NoteTextBunqMeFundraiserResultUpdate",
    "NoteTextDraftPayment",
    "NoteTextDraftPaymentCreate",
    "NoteTextDraftPaymentDelete",
    "NoteTextDraftPaymentListing",
    "NoteTextDraftPaymentRead",
    "NoteTextDraftPaymentUpdate",
    "NoteTextIdealMerchantTransaction",
    "NoteTextIdealMerchantTransactionCreate",
    "NoteTextIdealMerchantTransactionDelete",
    "NoteTextIdealMerchantTransactionListing",
    "NoteTextIdealMerchantTransactionRead",
    "NoteTextIdealMerchantTransactionUpdate",
    "NoteTextMasterCardAction",
    "NoteTextMasterCardActionCreate",
    "NoteTextMasterCardActionDelete",
    "NoteTextMasterCardActionListing",
    "NoteTextMasterCardActionRead",
    "NoteTextMasterCardActionUpdate",
    "NoteTextPayment",
    "NoteTextPaymentBatch",
    "NoteTextPaymentBatchCreate",
    "NoteTextPaymentBatchDelete",
    "NoteTextPaymentBatchListing",
    "NoteTextPaymentBatchRead",
    "NoteTextPaymentBatchUpdate",
    "NoteTextPaymentCreate",
    "NoteTextPaymentDelete",
    "NoteTextPaymentListing",
    "NoteTextPaymentRead",
    "NoteTextPaymentUpdate",
    "NoteTextRequestInquiry",
    "NoteTextRequestInquiryBatch",
    "NoteTextRequestInquiryBatchCreate",
    "NoteTextRequestInquiryBatchDelete",
    "NoteTextRequestInquiryBatchListing",
    "NoteTextRequestInquiryBatchRead",
    "NoteTextRequestInquiryBatchUpdate",
    "NoteTextRequestInquiryCreate",
    "NoteTextRequestInquiryDelete",
    "NoteTextRequestInquiryListing",
    "NoteTextRequestInquiryRead",
    "NoteTextRequestInquiryUpdate",
    "NoteTextRequestResponse",
    "NoteTextRequestResponseCreate",
    "NoteTextRequestResponseDelete",
    "NoteTextRequestResponseListing",
    "NoteTextRequestResponseRead",
    "NoteTextRequestResponseUpdate",
    "NoteTextScheduleInstance",
    "NoteTextScheduleInstanceCreate",
    "NoteTextScheduleInstanceDelete",
    "NoteTextScheduleInstanceListing",
    "NoteTextScheduleInstanceRead",
    "NoteTextScheduleInstanceUpdate",
    "NoteTextSchedulePayment",
    "NoteTextSchedulePaymentBatch",
    "NoteTextSchedulePaymentBatchCreate",
    "NoteTextSchedulePaymentBatchDelete",
    "NoteTextSchedulePaymentBatchListing",
    "NoteTextSchedulePaymentBatchRead",
    "NoteTextSchedulePaymentBatchUpdate",
    "NoteTextSchedulePaymentCreate",
    "NoteTextSchedulePaymentDelete",
    "NoteTextSchedulePaymentListing",
    "NoteTextSchedulePaymentRead",
    "NoteTextSchedulePaymentUpdate",
    "NoteTextSofortMerchantTransaction",
    "NoteTextSofortMerchantTransactionCreate",
    "NoteTextSofortMerchantTransactionDelete",
    "NoteTextSofortMerchantTransactionListing",
    "NoteTextSofortMerchantTransactionRead",
    "NoteTextSofortMerchantTransactionUpdate",
    "NoteTextWhitelistResult",
    "NoteTextWhitelistResultCreate",
    "NoteTextWhitelistResultDelete",
    "NoteTextWhitelistResultListing",
    "NoteTextWhitelistResultRead",
    "NoteTextWhitelistResultUpdate",
    "NotificationFilter",
    "NotificationFilterEmail",
    "NotificationFilterEmailCreate",
    "NotificationFilterEmailListing",
    "NotificationFilterPush",
    "NotificationFilterPushCreate",
    "NotificationFilterPushListing",
    "NotificationFilterUrl",
    "NotificationFilterUrlCreate",
    "NotificationFilterUrlListing",
    "NotificationFilterUrlMonetaryAccountCreate",
    "NotificationFilterUrlMonetaryAccountListing",
    "OauthCallbackUrl",
    "OauthCallbackUrlCreate",
    "OauthCallbackUrlDelete",
    "OauthCallbackUrlListing",
    "OauthCallbackUrlRead",
    "OauthCallbackUrlUpdate",
    "OauthClient",
    "OauthClientCreate",
    "OauthClientListing",
    "OauthClientRead",
    "OauthClientUpdate",
    "Payment",
    "PaymentAutoAllocate",
    "PaymentAutoAllocateCreate",
    "PaymentAutoAllocateDefinition",
    "PaymentAutoAllocateDefinitionListing",
    "PaymentAutoAllocateDelete",
    "PaymentAutoAllocateInstance",
    "PaymentAutoAllocateInstanceListing",
    "PaymentAutoAllocateInstanceRead",
    "PaymentAutoAllocateListing",
    "PaymentAutoAllocateRead",
    "PaymentAutoAllocateUpdate",
    "PaymentAutoAllocateUserListing",
    "PaymentBatch",
    "PaymentBatchAnchoredPayment",
    "PaymentBatchCreate",
    "PaymentBatchListing",
    "PaymentBatchRead",
    "PaymentBatchUpdate",
    "PaymentCreate",
    "PaymentListing",
    "PaymentRead",
    "PaymentServiceProviderCredentialCreate",
    "PaymentServiceProviderCredentialRead",
    "PaymentServiceProviderDraftPayment",
    "PaymentServiceProviderDraftPaymentCreate",
    "PaymentServiceProviderDraftPaymentListing",
    "PaymentServiceProviderDraftPaymentRead",
    "PaymentServiceProviderDraftPaymentUpdate",
    "PermittedDevice",
    "PermittedIp",
    "PermittedIpCreate",
    "PermittedIpListing",
    "PermittedIpRead",
    "PermittedIpUpdate",
    "PlacePhotoLookupContentListing",
    "Pointer",
    "RegistryMembership",
    "RegistrySettlement",
    "RegistrySettlementCreate",
    "RegistrySettlementItem",
    "RegistrySettlementListing",
    "RegistrySettlementRead",
    "RelationUser",
    "RequestInquiry",
    "RequestInquiryBatch",
    "RequestInquiryBatchCreate",
    "RequestInquiryBatchListing",
    "RequestInquiryBatchRead",
    "RequestInquiryBatchUpdate",
    "RequestInquiryCreate",
    "RequestInquiryListing",
    "RequestInquiryRead",
    "RequestInquiryReference",
    "RequestInquiryUpdate",
    "RequestReferenceSplitTheBillAnchorObject",
    "RequestResponse",
    "RequestResponseListing",
    "RequestResponseRead",
    "RequestResponseUpdate",
    "RewardListing",
    "RewardRead",
    "RewardRecipient",
    "RewardRecipientListing",
    "RewardRecipientRead",
    "RewardSender",
    "RewardSenderListing",
    "RewardSenderRead",
    "SandboxUserCompany",
    "SandboxUserCompanyCreate",
    "SandboxUserPerson",
    "SandboxUserPersonCreate",
    "Schedule",
    "ScheduleAnchorObject",
    "ScheduleInstance",
    "ScheduleInstanceAnchorObject",
    "ScheduleInstanceListing",
    "ScheduleInstanceRead",
    "ScheduleInstanceUpdate",
    "ScheduleListing",
    "SchedulePayment",
    "SchedulePaymentBatch",
    "SchedulePaymentBatchCreate",
    "SchedulePaymentBatchDelete",
    "SchedulePaymentBatchRead",
    "SchedulePaymentBatchUpdate",
    "SchedulePaymentCreate",
    "SchedulePaymentDelete",
    "SchedulePaymentEntry",
    "SchedulePaymentListing",
    "SchedulePaymentRead",
    "SchedulePaymentUpdate",
    "ScheduleRead",
    "ScheduleUserListing",
    "ServerError",
    "ServerErrorCreate",
    "SessionDelete",
    "SessionServerCreate",
    "SessionServerToken",
    "ShareDetail",
    "ShareDetailDraftPayment",
    "ShareDetailPayment",
    "ShareDetailReadOnly",
    "ShareInviteMonetaryAccountInquiry",
    "ShareInviteMonetaryAccountInquiryCreate",
    "ShareInviteMonetaryAccountInquiryListing",
    "ShareInviteMonetaryAccountInquiryRead",
    "ShareInviteMonetaryAccountInquiryUpdate",
    "ShareInviteMonetaryAccountResponse",
    "ShareInviteMonetaryAccountResponseListing",
    "ShareInviteMonetaryAccountResponseRead",
    "ShareInviteMonetaryAccountResponseUpdate",
    "SofortMerchantTransaction",
    "SofortMerchantTransactionListing",
    "SofortMerchantTransactionRead",
    "TaxResident",
    "TokenQrRequestIdealCreate",
    "TokenQrRequestSofortCreate",
    "TransferwiseAccountQuoteCreate",
    "TransferwiseAccountQuoteDelete",
    "TransferwiseAccountQuoteListing",
    "TransferwiseAccountQuoteRead",
    "TransferwiseAccountRequirementCreate",
    "TransferwiseAccountRequirementListing",
    "TransferwiseCurrencyListing",
    "TransferwiseQuote",
    "TransferwiseQuoteCreate",
    "TransferwiseQuoteRead",
    "TransferwiseQuoteTemporaryCreate",
    "TransferwiseQuoteTemporaryRead",
    "TransferwiseRequirementField",
    "TransferwiseRequirementFieldGroup",
    "TransferwiseRequirementFieldGroupValidationAsync",
    "TransferwiseRequirementFieldGroupValidationAsyncParams",
    "TransferwiseRequirementFieldGroupValuesAllowed",
    "TransferwiseTransfer",
    "TransferwiseTransferCreate",
    "TransferwiseTransferListing",
    "TransferwiseTransferRead",
    "TransferwiseTransferRequirementCreate",
    "TransferwiseUserCreate",
    "TransferwiseUserListing",
    "TranslinkTransactionCreate",
    "TranslinkTransactionEntry",
    "TranslinkTransactionListing",
    "TranslinkTransactionRead",
    "TreeProgressListing",
    "Ubo",
    "UserApiKey",
    "UserApiKeyAnchoredUser",
    "UserCompany",
    "UserCompanyNameListing",
    "UserCompanyRead",
    "UserCompanyUpdate",
    "UserCredentialPasswordIpListing",
    "UserCredentialPasswordIpRead",
    "UserLegalNameListing",
    "UserListing",
    "UserPaymentServiceProvider",
    "UserPaymentServiceProviderRead",
    "UserPerson",
    "UserPersonRead",
    "UserPersonUpdate",
    "UserRead",
    "Whitelist",
    "WhitelistResult",
    "WhitelistResultViewAnchoredObject",
    "WhitelistSddListing",
    "WhitelistSddMonetaryAccountPayingListing",
    "WhitelistSddMonetaryAccountPayingRead",
    "WhitelistSddOneOff",
    "WhitelistSddOneOffCreate",
    "WhitelistSddOneOffDelete",
    "WhitelistSddOneOffListing",
    "WhitelistSddOneOffRead",
    "WhitelistSddOneOffUpdate",
    "WhitelistSddRead",
    "WhitelistSddRecurring",
    "WhitelistSddRecurringCreate",
    "WhitelistSddRecurringDelete",
    "WhitelistSddRecurringListing",
    "WhitelistSddRecurringRead",
    "WhitelistSddRecurringUpdate",
]
