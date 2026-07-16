



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .accept_dispute_request import AcceptDisputeRequest
    from .accept_dispute_response import AcceptDisputeResponse
    from .accumulate_loyalty_points_response import AccumulateLoyaltyPointsResponse
    from .ach_details import AchDetails
    from .action_cancel_reason import ActionCancelReason
    from .add_group_to_customer_request import AddGroupToCustomerRequest
    from .add_group_to_customer_response import AddGroupToCustomerResponse
    from .additional_recipient import AdditionalRecipient
    from .address import Address
    from .adjust_loyalty_points_response import AdjustLoyaltyPointsResponse
    from .appointment_segment import AppointmentSegment
    from .availability import Availability
    from .bank_account import BankAccount
    from .bank_account_payment_details import BankAccountPaymentDetails
    from .bank_account_status import BankAccountStatus
    from .bank_account_type import BankAccountType
    from .batch_change_inventory_request import BatchChangeInventoryRequest
    from .batch_change_inventory_response import BatchChangeInventoryResponse
    from .batch_delete_catalog_objects_response import BatchDeleteCatalogObjectsResponse
    from .batch_retrieve_catalog_objects_response import BatchRetrieveCatalogObjectsResponse
    from .batch_retrieve_inventory_changes_request import BatchRetrieveInventoryChangesRequest
    from .batch_retrieve_inventory_changes_response import BatchRetrieveInventoryChangesResponse
    from .batch_retrieve_inventory_counts_request import BatchRetrieveInventoryCountsRequest
    from .batch_retrieve_inventory_counts_response import BatchRetrieveInventoryCountsResponse
    from .batch_retrieve_orders_response import BatchRetrieveOrdersResponse
    from .batch_upsert_catalog_objects_response import BatchUpsertCatalogObjectsResponse
    from .booking import Booking
    from .booking_status import BookingStatus
    from .break_ import Break
    from .break_type import BreakType
    from .bulk_create_team_members_response import BulkCreateTeamMembersResponse
    from .bulk_update_team_members_response import BulkUpdateTeamMembersResponse
    from .business_appointment_settings import BusinessAppointmentSettings
    from .business_appointment_settings_alignment_time import BusinessAppointmentSettingsAlignmentTime
    from .business_appointment_settings_booking_location_type import BusinessAppointmentSettingsBookingLocationType
    from .business_appointment_settings_cancellation_policy import BusinessAppointmentSettingsCancellationPolicy
    from .business_appointment_settings_max_appointments_per_day_limit_type import (
        BusinessAppointmentSettingsMaxAppointmentsPerDayLimitType,
    )
    from .business_booking_profile import BusinessBookingProfile
    from .business_booking_profile_booking_policy import BusinessBookingProfileBookingPolicy
    from .business_booking_profile_customer_timezone_choice import BusinessBookingProfileCustomerTimezoneChoice
    from .business_hours import BusinessHours
    from .business_hours_period import BusinessHoursPeriod
    from .calculate_loyalty_points_response import CalculateLoyaltyPointsResponse
    from .calculate_order_response import CalculateOrderResponse
    from .cancel_booking_response import CancelBookingResponse
    from .cancel_invoice_response import CancelInvoiceResponse
    from .cancel_payment_by_idempotency_key_response import CancelPaymentByIdempotencyKeyResponse
    from .cancel_payment_request import CancelPaymentRequest
    from .cancel_payment_response import CancelPaymentResponse
    from .cancel_subscription_request import CancelSubscriptionRequest
    from .cancel_subscription_response import CancelSubscriptionResponse
    from .cancel_terminal_checkout_request import CancelTerminalCheckoutRequest
    from .cancel_terminal_checkout_response import CancelTerminalCheckoutResponse
    from .cancel_terminal_refund_request import CancelTerminalRefundRequest
    from .cancel_terminal_refund_response import CancelTerminalRefundResponse
    from .capture_transaction_request import CaptureTransactionRequest
    from .capture_transaction_response import CaptureTransactionResponse
    from .card import Card
    from .card_brand import CardBrand
    from .card_payment_details import CardPaymentDetails
    from .card_payment_timeline import CardPaymentTimeline
    from .card_prepaid_type import CardPrepaidType
    from .card_square_product import CardSquareProduct
    from .card_type import CardType
    from .cash_drawer_device import CashDrawerDevice
    from .cash_drawer_event_type import CashDrawerEventType
    from .cash_drawer_shift import CashDrawerShift
    from .cash_drawer_shift_event import CashDrawerShiftEvent
    from .cash_drawer_shift_state import CashDrawerShiftState
    from .cash_drawer_shift_summary import CashDrawerShiftSummary
    from .cash_payment_details import CashPaymentDetails
    from .catalog_category import CatalogCategory
    from .catalog_custom_attribute_definition import CatalogCustomAttributeDefinition
    from .catalog_custom_attribute_definition_app_visibility import CatalogCustomAttributeDefinitionAppVisibility
    from .catalog_custom_attribute_definition_number_config import CatalogCustomAttributeDefinitionNumberConfig
    from .catalog_custom_attribute_definition_selection_config import CatalogCustomAttributeDefinitionSelectionConfig
    from .catalog_custom_attribute_definition_selection_config_custom_attribute_selection import (
        CatalogCustomAttributeDefinitionSelectionConfigCustomAttributeSelection,
    )
    from .catalog_custom_attribute_definition_seller_visibility import CatalogCustomAttributeDefinitionSellerVisibility
    from .catalog_custom_attribute_definition_string_config import CatalogCustomAttributeDefinitionStringConfig
    from .catalog_custom_attribute_definition_type import CatalogCustomAttributeDefinitionType
    from .catalog_custom_attribute_value import CatalogCustomAttributeValue
    from .catalog_discount import CatalogDiscount
    from .catalog_discount_modify_tax_basis import CatalogDiscountModifyTaxBasis
    from .catalog_discount_type import CatalogDiscountType
    from .catalog_id_mapping import CatalogIdMapping
    from .catalog_image import CatalogImage
    from .catalog_info_request import CatalogInfoRequest
    from .catalog_info_response import CatalogInfoResponse
    from .catalog_info_response_limits import CatalogInfoResponseLimits
    from .catalog_item import CatalogItem
    from .catalog_item_modifier_list_info import CatalogItemModifierListInfo
    from .catalog_item_option import CatalogItemOption
    from .catalog_item_option_for_item import CatalogItemOptionForItem
    from .catalog_item_option_value import CatalogItemOptionValue
    from .catalog_item_option_value_for_item_variation import CatalogItemOptionValueForItemVariation
    from .catalog_item_product_type import CatalogItemProductType
    from .catalog_item_variation import CatalogItemVariation
    from .catalog_measurement_unit import CatalogMeasurementUnit
    from .catalog_modifier import CatalogModifier
    from .catalog_modifier_list import CatalogModifierList
    from .catalog_modifier_list_selection_type import CatalogModifierListSelectionType
    from .catalog_modifier_override import CatalogModifierOverride
    from .catalog_object import CatalogObject
    from .catalog_object_batch import CatalogObjectBatch
    from .catalog_object_reference import CatalogObjectReference
    from .catalog_object_type import CatalogObjectType
    from .catalog_pricing_rule import CatalogPricingRule
    from .catalog_pricing_type import CatalogPricingType
    from .catalog_product_set import CatalogProductSet
    from .catalog_query import CatalogQuery
    from .catalog_query_exact import CatalogQueryExact
    from .catalog_query_item_variations_for_item_option_values import CatalogQueryItemVariationsForItemOptionValues
    from .catalog_query_items_for_item_options import CatalogQueryItemsForItemOptions
    from .catalog_query_items_for_modifier_list import CatalogQueryItemsForModifierList
    from .catalog_query_items_for_tax import CatalogQueryItemsForTax
    from .catalog_query_prefix import CatalogQueryPrefix
    from .catalog_query_range import CatalogQueryRange
    from .catalog_query_set import CatalogQuerySet
    from .catalog_query_sorted_attribute import CatalogQuerySortedAttribute
    from .catalog_query_text import CatalogQueryText
    from .catalog_quick_amount import CatalogQuickAmount
    from .catalog_quick_amount_type import CatalogQuickAmountType
    from .catalog_quick_amounts_settings import CatalogQuickAmountsSettings
    from .catalog_quick_amounts_settings_option import CatalogQuickAmountsSettingsOption
    from .catalog_stock_conversion import CatalogStockConversion
    from .catalog_subscription_plan import CatalogSubscriptionPlan
    from .catalog_tax import CatalogTax
    from .catalog_time_period import CatalogTimePeriod
    from .catalog_v1id import CatalogV1Id
    from .charge_request_additional_recipient import ChargeRequestAdditionalRecipient
    from .charge_response import ChargeResponse
    from .check_appointments_onboarded_request import CheckAppointmentsOnboardedRequest
    from .checkout import Checkout
    from .checkout_options_payment_type import CheckoutOptionsPaymentType
    from .complete_payment_request import CompletePaymentRequest
    from .complete_payment_response import CompletePaymentResponse
    from .coordinates import Coordinates
    from .country import Country
    from .create_booking_response import CreateBookingResponse
    from .create_break_type_response import CreateBreakTypeResponse
    from .create_card_response import CreateCardResponse
    from .create_checkout_response import CreateCheckoutResponse
    from .create_customer_card_response import CreateCustomerCardResponse
    from .create_customer_group_response import CreateCustomerGroupResponse
    from .create_customer_response import CreateCustomerResponse
    from .create_device_code_response import CreateDeviceCodeResponse
    from .create_dispute_evidence_text_response import CreateDisputeEvidenceTextResponse
    from .create_gift_card_activity_response import CreateGiftCardActivityResponse
    from .create_gift_card_response import CreateGiftCardResponse
    from .create_invoice_response import CreateInvoiceResponse
    from .create_location_response import CreateLocationResponse
    from .create_loyalty_account_response import CreateLoyaltyAccountResponse
    from .create_loyalty_reward_response import CreateLoyaltyRewardResponse
    from .create_mobile_authorization_code_response import CreateMobileAuthorizationCodeResponse
    from .create_order_request import CreateOrderRequest
    from .create_order_response import CreateOrderResponse
    from .create_payment_response import CreatePaymentResponse
    from .create_refund_response import CreateRefundResponse
    from .create_shift_response import CreateShiftResponse
    from .create_subscription_response import CreateSubscriptionResponse
    from .create_team_member_request import CreateTeamMemberRequest
    from .create_team_member_response import CreateTeamMemberResponse
    from .create_terminal_checkout_response import CreateTerminalCheckoutResponse
    from .create_terminal_refund_response import CreateTerminalRefundResponse
    from .currency import Currency
    from .custom_attribute_filter import CustomAttributeFilter
    from .customer import Customer
    from .customer_creation_source import CustomerCreationSource
    from .customer_creation_source_filter import CustomerCreationSourceFilter
    from .customer_filter import CustomerFilter
    from .customer_group import CustomerGroup
    from .customer_inclusion_exclusion import CustomerInclusionExclusion
    from .customer_preferences import CustomerPreferences
    from .customer_query import CustomerQuery
    from .customer_segment import CustomerSegment
    from .customer_sort import CustomerSort
    from .customer_sort_field import CustomerSortField
    from .customer_text_filter import CustomerTextFilter
    from .date_range import DateRange
    from .day_of_week import DayOfWeek
    from .delete_break_type_request import DeleteBreakTypeRequest
    from .delete_break_type_response import DeleteBreakTypeResponse
    from .delete_catalog_object_request import DeleteCatalogObjectRequest
    from .delete_catalog_object_response import DeleteCatalogObjectResponse
    from .delete_customer_card_request import DeleteCustomerCardRequest
    from .delete_customer_card_response import DeleteCustomerCardResponse
    from .delete_customer_group_request import DeleteCustomerGroupRequest
    from .delete_customer_group_response import DeleteCustomerGroupResponse
    from .delete_customer_request import DeleteCustomerRequest
    from .delete_customer_response import DeleteCustomerResponse
    from .delete_dispute_evidence_request import DeleteDisputeEvidenceRequest
    from .delete_dispute_evidence_response import DeleteDisputeEvidenceResponse
    from .delete_invoice_request import DeleteInvoiceRequest
    from .delete_invoice_response import DeleteInvoiceResponse
    from .delete_loyalty_reward_request import DeleteLoyaltyRewardRequest
    from .delete_loyalty_reward_response import DeleteLoyaltyRewardResponse
    from .delete_shift_request import DeleteShiftRequest
    from .delete_shift_response import DeleteShiftResponse
    from .delete_snippet_request import DeleteSnippetRequest
    from .delete_snippet_response import DeleteSnippetResponse
    from .deprecated_create_dispute_evidence_file_request import DeprecatedCreateDisputeEvidenceFileRequest
    from .deprecated_create_dispute_evidence_file_response import DeprecatedCreateDisputeEvidenceFileResponse
    from .deprecated_create_dispute_evidence_text_request import DeprecatedCreateDisputeEvidenceTextRequest
    from .deprecated_create_dispute_evidence_text_response import DeprecatedCreateDisputeEvidenceTextResponse
    from .device import Device
    from .device_checkout_options import DeviceCheckoutOptions
    from .device_code import DeviceCode
    from .device_code_status import DeviceCodeStatus
    from .device_details import DeviceDetails
    from .digital_wallet_details import DigitalWalletDetails
    from .disable_card_request import DisableCardRequest
    from .disable_card_response import DisableCardResponse
    from .dispute import Dispute
    from .dispute_evidence import DisputeEvidence
    from .dispute_evidence_created_webhook import DisputeEvidenceCreatedWebhook
    from .dispute_evidence_created_webhook_data import DisputeEvidenceCreatedWebhookData
    from .dispute_evidence_created_webhook_object import DisputeEvidenceCreatedWebhookObject
    from .dispute_evidence_file import DisputeEvidenceFile
    from .dispute_evidence_type import DisputeEvidenceType
    from .dispute_reason import DisputeReason
    from .dispute_state import DisputeState
    from .disputed_payment import DisputedPayment
    from .ecom_visibility import EcomVisibility
    from .employee import Employee
    from .employee_status import EmployeeStatus
    from .employee_wage import EmployeeWage
    from .error import Error
    from .error_category import ErrorCategory
    from .error_code import ErrorCode
    from .exclude_strategy import ExcludeStrategy
    from .external_payment_details import ExternalPaymentDetails
    from .filter_value import FilterValue
    from .gan_source import GanSource
    from .get_bank_account_by_v1id_request import GetBankAccountByV1IdRequest
    from .get_bank_account_by_v1id_response import GetBankAccountByV1IdResponse
    from .get_bank_account_request import GetBankAccountRequest
    from .get_bank_account_response import GetBankAccountResponse
    from .get_break_type_request import GetBreakTypeRequest
    from .get_break_type_response import GetBreakTypeResponse
    from .get_device_code_request import GetDeviceCodeRequest
    from .get_device_code_response import GetDeviceCodeResponse
    from .get_employee_wage_request import GetEmployeeWageRequest
    from .get_employee_wage_response import GetEmployeeWageResponse
    from .get_invoice_request import GetInvoiceRequest
    from .get_invoice_response import GetInvoiceResponse
    from .get_payment_refund_request import GetPaymentRefundRequest
    from .get_payment_refund_response import GetPaymentRefundResponse
    from .get_payment_request import GetPaymentRequest
    from .get_payment_response import GetPaymentResponse
    from .get_shift_request import GetShiftRequest
    from .get_shift_response import GetShiftResponse
    from .get_team_member_wage_request import GetTeamMemberWageRequest
    from .get_team_member_wage_response import GetTeamMemberWageResponse
    from .get_terminal_checkout_request import GetTerminalCheckoutRequest
    from .get_terminal_checkout_response import GetTerminalCheckoutResponse
    from .get_terminal_refund_request import GetTerminalRefundRequest
    from .get_terminal_refund_response import GetTerminalRefundResponse
    from .gift_card import GiftCard
    from .gift_card_activity import GiftCardActivity
    from .gift_card_activity_activate import GiftCardActivityActivate
    from .gift_card_activity_adjust_decrement import GiftCardActivityAdjustDecrement
    from .gift_card_activity_adjust_decrement_reason import GiftCardActivityAdjustDecrementReason
    from .gift_card_activity_adjust_increment import GiftCardActivityAdjustIncrement
    from .gift_card_activity_adjust_increment_reason import GiftCardActivityAdjustIncrementReason
    from .gift_card_activity_block import GiftCardActivityBlock
    from .gift_card_activity_block_reason import GiftCardActivityBlockReason
    from .gift_card_activity_clear_balance import GiftCardActivityClearBalance
    from .gift_card_activity_clear_balance_reason import GiftCardActivityClearBalanceReason
    from .gift_card_activity_deactivate import GiftCardActivityDeactivate
    from .gift_card_activity_deactivate_reason import GiftCardActivityDeactivateReason
    from .gift_card_activity_import import GiftCardActivityImport
    from .gift_card_activity_import_reversal import GiftCardActivityImportReversal
    from .gift_card_activity_load import GiftCardActivityLoad
    from .gift_card_activity_redeem import GiftCardActivityRedeem
    from .gift_card_activity_refund import GiftCardActivityRefund
    from .gift_card_activity_type import GiftCardActivityType
    from .gift_card_activity_unblock import GiftCardActivityUnblock
    from .gift_card_activity_unblock_reason import GiftCardActivityUnblockReason
    from .gift_card_activity_unlinked_activity_refund import GiftCardActivityUnlinkedActivityRefund
    from .gift_card_gan_source import GiftCardGanSource
    from .gift_card_status import GiftCardStatus
    from .gift_card_type import GiftCardType
    from .info import Info
    from .info_code import InfoCode
    from .inline_types import InlineTypes
    from .inventory_adjustment import InventoryAdjustment
    from .inventory_adjustment_group import InventoryAdjustmentGroup
    from .inventory_alert_type import InventoryAlertType
    from .inventory_change import InventoryChange
    from .inventory_change_type import InventoryChangeType
    from .inventory_count import InventoryCount
    from .inventory_physical_count import InventoryPhysicalCount
    from .inventory_state import InventoryState
    from .inventory_transfer import InventoryTransfer
    from .invoice import Invoice
    from .invoice_accepted_payment_methods import InvoiceAcceptedPaymentMethods
    from .invoice_automatic_payment_source import InvoiceAutomaticPaymentSource
    from .invoice_custom_field import InvoiceCustomField
    from .invoice_custom_field_placement import InvoiceCustomFieldPlacement
    from .invoice_delivery_method import InvoiceDeliveryMethod
    from .invoice_delivery_method_invoice_delivery_method import InvoiceDeliveryMethodInvoiceDeliveryMethod
    from .invoice_filter import InvoiceFilter
    from .invoice_payment_reminder import InvoicePaymentReminder
    from .invoice_payment_reminder_status import InvoicePaymentReminderStatus
    from .invoice_payment_request import InvoicePaymentRequest
    from .invoice_query import InvoiceQuery
    from .invoice_recipient import InvoiceRecipient
    from .invoice_request_method import InvoiceRequestMethod
    from .invoice_request_type import InvoiceRequestType
    from .invoice_sort import InvoiceSort
    from .invoice_sort_field import InvoiceSortField
    from .invoice_status import InvoiceStatus
    from .item_variation_location_overrides import ItemVariationLocationOverrides
    from .job_assignment import JobAssignment
    from .job_assignment_pay_type import JobAssignmentPayType
    from .link_customer_to_gift_card_response import LinkCustomerToGiftCardResponse
    from .list_bank_accounts_request import ListBankAccountsRequest
    from .list_bank_accounts_response import ListBankAccountsResponse
    from .list_break_types_request import ListBreakTypesRequest
    from .list_break_types_response import ListBreakTypesResponse
    from .list_cards_request import ListCardsRequest
    from .list_cards_response import ListCardsResponse
    from .list_cash_drawer_shift_events_request import ListCashDrawerShiftEventsRequest
    from .list_cash_drawer_shift_events_response import ListCashDrawerShiftEventsResponse
    from .list_cash_drawer_shifts_request import ListCashDrawerShiftsRequest
    from .list_cash_drawer_shifts_response import ListCashDrawerShiftsResponse
    from .list_catalog_request import ListCatalogRequest
    from .list_catalog_response import ListCatalogResponse
    from .list_customer_groups_request import ListCustomerGroupsRequest
    from .list_customer_groups_response import ListCustomerGroupsResponse
    from .list_customer_segments_request import ListCustomerSegmentsRequest
    from .list_customer_segments_response import ListCustomerSegmentsResponse
    from .list_customers_request import ListCustomersRequest
    from .list_customers_response import ListCustomersResponse
    from .list_device_codes_request import ListDeviceCodesRequest
    from .list_device_codes_response import ListDeviceCodesResponse
    from .list_dispute_evidence_request import ListDisputeEvidenceRequest
    from .list_dispute_evidence_response import ListDisputeEvidenceResponse
    from .list_disputes_request import ListDisputesRequest
    from .list_disputes_response import ListDisputesResponse
    from .list_employee_wages_request import ListEmployeeWagesRequest
    from .list_employee_wages_response import ListEmployeeWagesResponse
    from .list_employees_request import ListEmployeesRequest
    from .list_employees_response import ListEmployeesResponse
    from .list_gift_card_activities_request import ListGiftCardActivitiesRequest
    from .list_gift_card_activities_response import ListGiftCardActivitiesResponse
    from .list_gift_cards_request import ListGiftCardsRequest
    from .list_gift_cards_response import ListGiftCardsResponse
    from .list_invoices_request import ListInvoicesRequest
    from .list_invoices_response import ListInvoicesResponse
    from .list_locations_request import ListLocationsRequest
    from .list_locations_response import ListLocationsResponse
    from .list_loyalty_programs_request import ListLoyaltyProgramsRequest
    from .list_loyalty_programs_response import ListLoyaltyProgramsResponse
    from .list_merchants_request import ListMerchantsRequest
    from .list_merchants_response import ListMerchantsResponse
    from .list_payment_refunds_request import ListPaymentRefundsRequest
    from .list_payment_refunds_response import ListPaymentRefundsResponse
    from .list_payments_request import ListPaymentsRequest
    from .list_payments_response import ListPaymentsResponse
    from .list_refunds_request import ListRefundsRequest
    from .list_refunds_response import ListRefundsResponse
    from .list_sites_request import ListSitesRequest
    from .list_sites_response import ListSitesResponse
    from .list_subscription_events_request import ListSubscriptionEventsRequest
    from .list_subscription_events_response import ListSubscriptionEventsResponse
    from .list_team_member_booking_profiles_request import ListTeamMemberBookingProfilesRequest
    from .list_team_member_booking_profiles_response import ListTeamMemberBookingProfilesResponse
    from .list_team_member_wages_request import ListTeamMemberWagesRequest
    from .list_team_member_wages_response import ListTeamMemberWagesResponse
    from .list_transactions_request import ListTransactionsRequest
    from .list_transactions_response import ListTransactionsResponse
    from .list_workweek_configs_request import ListWorkweekConfigsRequest
    from .list_workweek_configs_response import ListWorkweekConfigsResponse
    from .location import Location
    from .location_capability import LocationCapability
    from .location_status import LocationStatus
    from .location_type import LocationType
    from .loyalty_account import LoyaltyAccount
    from .loyalty_account_expiring_point_deadline import LoyaltyAccountExpiringPointDeadline
    from .loyalty_account_mapping import LoyaltyAccountMapping
    from .loyalty_account_mapping_type import LoyaltyAccountMappingType
    from .loyalty_event import LoyaltyEvent
    from .loyalty_event_accumulate_points import LoyaltyEventAccumulatePoints
    from .loyalty_event_adjust_points import LoyaltyEventAdjustPoints
    from .loyalty_event_create_reward import LoyaltyEventCreateReward
    from .loyalty_event_date_time_filter import LoyaltyEventDateTimeFilter
    from .loyalty_event_delete_reward import LoyaltyEventDeleteReward
    from .loyalty_event_expire_points import LoyaltyEventExpirePoints
    from .loyalty_event_filter import LoyaltyEventFilter
    from .loyalty_event_location_filter import LoyaltyEventLocationFilter
    from .loyalty_event_loyalty_account_filter import LoyaltyEventLoyaltyAccountFilter
    from .loyalty_event_order_filter import LoyaltyEventOrderFilter
    from .loyalty_event_other import LoyaltyEventOther
    from .loyalty_event_query import LoyaltyEventQuery
    from .loyalty_event_redeem_reward import LoyaltyEventRedeemReward
    from .loyalty_event_source import LoyaltyEventSource
    from .loyalty_event_type import LoyaltyEventType
    from .loyalty_event_type_filter import LoyaltyEventTypeFilter
    from .loyalty_program import LoyaltyProgram
    from .loyalty_program_accrual_rule import LoyaltyProgramAccrualRule
    from .loyalty_program_accrual_rule_type import LoyaltyProgramAccrualRuleType
    from .loyalty_program_expiration_policy import LoyaltyProgramExpirationPolicy
    from .loyalty_program_reward_definition import LoyaltyProgramRewardDefinition
    from .loyalty_program_reward_definition_scope import LoyaltyProgramRewardDefinitionScope
    from .loyalty_program_reward_definition_type import LoyaltyProgramRewardDefinitionType
    from .loyalty_program_reward_tier import LoyaltyProgramRewardTier
    from .loyalty_program_status import LoyaltyProgramStatus
    from .loyalty_program_terminology import LoyaltyProgramTerminology
    from .loyalty_reward import LoyaltyReward
    from .loyalty_reward_status import LoyaltyRewardStatus
    from .measurement_unit import MeasurementUnit
    from .measurement_unit_area import MeasurementUnitArea
    from .measurement_unit_custom import MeasurementUnitCustom
    from .measurement_unit_generic import MeasurementUnitGeneric
    from .measurement_unit_length import MeasurementUnitLength
    from .measurement_unit_time import MeasurementUnitTime
    from .measurement_unit_unit_type import MeasurementUnitUnitType
    from .measurement_unit_volume import MeasurementUnitVolume
    from .measurement_unit_weight import MeasurementUnitWeight
    from .merchant import Merchant
    from .merchant_status import MerchantStatus
    from .money import Money
    from .oauth_scope import OauthScope
    from .obtain_token_response import ObtainTokenResponse
    from .onboard_appointments_request import OnboardAppointmentsRequest
    from .order import Order
    from .order_created import OrderCreated
    from .order_created_object import OrderCreatedObject
    from .order_entry import OrderEntry
    from .order_fulfillment import OrderFulfillment
    from .order_fulfillment_pickup_details import OrderFulfillmentPickupDetails
    from .order_fulfillment_pickup_details_curbside_pickup_details import (
        OrderFulfillmentPickupDetailsCurbsidePickupDetails,
    )
    from .order_fulfillment_pickup_details_schedule_type import OrderFulfillmentPickupDetailsScheduleType
    from .order_fulfillment_recipient import OrderFulfillmentRecipient
    from .order_fulfillment_shipment_details import OrderFulfillmentShipmentDetails
    from .order_fulfillment_state import OrderFulfillmentState
    from .order_fulfillment_type import OrderFulfillmentType
    from .order_fulfillment_updated import OrderFulfillmentUpdated
    from .order_fulfillment_updated_object import OrderFulfillmentUpdatedObject
    from .order_fulfillment_updated_update import OrderFulfillmentUpdatedUpdate
    from .order_line_item import OrderLineItem
    from .order_line_item_applied_discount import OrderLineItemAppliedDiscount
    from .order_line_item_applied_tax import OrderLineItemAppliedTax
    from .order_line_item_discount import OrderLineItemDiscount
    from .order_line_item_discount_scope import OrderLineItemDiscountScope
    from .order_line_item_discount_type import OrderLineItemDiscountType
    from .order_line_item_item_type import OrderLineItemItemType
    from .order_line_item_modifier import OrderLineItemModifier
    from .order_line_item_pricing_blocklists import OrderLineItemPricingBlocklists
    from .order_line_item_pricing_blocklists_blocked_discount import OrderLineItemPricingBlocklistsBlockedDiscount
    from .order_line_item_pricing_blocklists_blocked_tax import OrderLineItemPricingBlocklistsBlockedTax
    from .order_line_item_tax import OrderLineItemTax
    from .order_line_item_tax_scope import OrderLineItemTaxScope
    from .order_line_item_tax_type import OrderLineItemTaxType
    from .order_money_amounts import OrderMoneyAmounts
    from .order_pricing_options import OrderPricingOptions
    from .order_quantity_unit import OrderQuantityUnit
    from .order_return import OrderReturn
    from .order_return_discount import OrderReturnDiscount
    from .order_return_line_item import OrderReturnLineItem
    from .order_return_line_item_modifier import OrderReturnLineItemModifier
    from .order_return_service_charge import OrderReturnServiceCharge
    from .order_return_tax import OrderReturnTax
    from .order_reward import OrderReward
    from .order_rounding_adjustment import OrderRoundingAdjustment
    from .order_service_charge import OrderServiceCharge
    from .order_service_charge_calculation_phase import OrderServiceChargeCalculationPhase
    from .order_service_charge_type import OrderServiceChargeType
    from .order_source import OrderSource
    from .order_state import OrderState
    from .order_updated import OrderUpdated
    from .order_updated_object import OrderUpdatedObject
    from .pay_order_response import PayOrderResponse
    from .payment import Payment
    from .payment_options import PaymentOptions
    from .payment_refund import PaymentRefund
    from .processing_fee import ProcessingFee
    from .product import Product
    from .product_type import ProductType
    from .publish_invoice_response import PublishInvoiceResponse
    from .quantity_ratio import QuantityRatio
    from .range import Range
    from .reason import Reason
    from .redeem_loyalty_reward_response import RedeemLoyaltyRewardResponse
    from .refund import Refund
    from .refund_payment_response import RefundPaymentResponse
    from .refund_status import RefundStatus
    from .register_domain_response import RegisterDomainResponse
    from .register_domain_response_status import RegisterDomainResponseStatus
    from .remove_group_from_customer_request import RemoveGroupFromCustomerRequest
    from .remove_group_from_customer_response import RemoveGroupFromCustomerResponse
    from .renew_token_response import RenewTokenResponse
    from .resume_subscription_request import ResumeSubscriptionRequest
    from .resume_subscription_response import ResumeSubscriptionResponse
    from .retrieve_booking_request import RetrieveBookingRequest
    from .retrieve_booking_response import RetrieveBookingResponse
    from .retrieve_business_booking_profile_request import RetrieveBusinessBookingProfileRequest
    from .retrieve_business_booking_profile_response import RetrieveBusinessBookingProfileResponse
    from .retrieve_card_request import RetrieveCardRequest
    from .retrieve_card_response import RetrieveCardResponse
    from .retrieve_cash_drawer_shift_request import RetrieveCashDrawerShiftRequest
    from .retrieve_cash_drawer_shift_response import RetrieveCashDrawerShiftResponse
    from .retrieve_catalog_object_request import RetrieveCatalogObjectRequest
    from .retrieve_catalog_object_response import RetrieveCatalogObjectResponse
    from .retrieve_customer_group_request import RetrieveCustomerGroupRequest
    from .retrieve_customer_group_response import RetrieveCustomerGroupResponse
    from .retrieve_customer_request import RetrieveCustomerRequest
    from .retrieve_customer_response import RetrieveCustomerResponse
    from .retrieve_customer_segment_request import RetrieveCustomerSegmentRequest
    from .retrieve_customer_segment_response import RetrieveCustomerSegmentResponse
    from .retrieve_dispute_evidence_request import RetrieveDisputeEvidenceRequest
    from .retrieve_dispute_evidence_response import RetrieveDisputeEvidenceResponse
    from .retrieve_dispute_request import RetrieveDisputeRequest
    from .retrieve_dispute_response import RetrieveDisputeResponse
    from .retrieve_employee_request import RetrieveEmployeeRequest
    from .retrieve_employee_response import RetrieveEmployeeResponse
    from .retrieve_gift_card_from_gan_response import RetrieveGiftCardFromGanResponse
    from .retrieve_gift_card_from_nonce_response import RetrieveGiftCardFromNonceResponse
    from .retrieve_gift_card_request import RetrieveGiftCardRequest
    from .retrieve_gift_card_response import RetrieveGiftCardResponse
    from .retrieve_inventory_adjustment_request import RetrieveInventoryAdjustmentRequest
    from .retrieve_inventory_adjustment_response import RetrieveInventoryAdjustmentResponse
    from .retrieve_inventory_changes_request import RetrieveInventoryChangesRequest
    from .retrieve_inventory_changes_response import RetrieveInventoryChangesResponse
    from .retrieve_inventory_count_request import RetrieveInventoryCountRequest
    from .retrieve_inventory_count_response import RetrieveInventoryCountResponse
    from .retrieve_inventory_physical_count_request import RetrieveInventoryPhysicalCountRequest
    from .retrieve_inventory_physical_count_response import RetrieveInventoryPhysicalCountResponse
    from .retrieve_inventory_transfer_request import RetrieveInventoryTransferRequest
    from .retrieve_inventory_transfer_response import RetrieveInventoryTransferResponse
    from .retrieve_location_request import RetrieveLocationRequest
    from .retrieve_location_response import RetrieveLocationResponse
    from .retrieve_loyalty_account_request import RetrieveLoyaltyAccountRequest
    from .retrieve_loyalty_account_response import RetrieveLoyaltyAccountResponse
    from .retrieve_loyalty_program_request import RetrieveLoyaltyProgramRequest
    from .retrieve_loyalty_program_response import RetrieveLoyaltyProgramResponse
    from .retrieve_loyalty_reward_request import RetrieveLoyaltyRewardRequest
    from .retrieve_loyalty_reward_response import RetrieveLoyaltyRewardResponse
    from .retrieve_merchant_request import RetrieveMerchantRequest
    from .retrieve_merchant_response import RetrieveMerchantResponse
    from .retrieve_obs_migration_profile_request import RetrieveObsMigrationProfileRequest
    from .retrieve_order_request import RetrieveOrderRequest
    from .retrieve_order_response import RetrieveOrderResponse
    from .retrieve_snippet_request import RetrieveSnippetRequest
    from .retrieve_snippet_response import RetrieveSnippetResponse
    from .retrieve_subscription_request import RetrieveSubscriptionRequest
    from .retrieve_subscription_response import RetrieveSubscriptionResponse
    from .retrieve_team_member_booking_profile_request import RetrieveTeamMemberBookingProfileRequest
    from .retrieve_team_member_booking_profile_response import RetrieveTeamMemberBookingProfileResponse
    from .retrieve_team_member_request import RetrieveTeamMemberRequest
    from .retrieve_team_member_response import RetrieveTeamMemberResponse
    from .retrieve_transaction_request import RetrieveTransactionRequest
    from .retrieve_transaction_response import RetrieveTransactionResponse
    from .retrieve_wage_setting_request import RetrieveWageSettingRequest
    from .retrieve_wage_setting_response import RetrieveWageSettingResponse
    from .revoke_token_response import RevokeTokenResponse
    from .risk_evaluation import RiskEvaluation
    from .risk_evaluation_risk_level import RiskEvaluationRiskLevel
    from .search_availability_filter import SearchAvailabilityFilter
    from .search_availability_query import SearchAvailabilityQuery
    from .search_availability_response import SearchAvailabilityResponse
    from .search_catalog_items_request_stock_level import SearchCatalogItemsRequestStockLevel
    from .search_catalog_items_response import SearchCatalogItemsResponse
    from .search_catalog_objects_response import SearchCatalogObjectsResponse
    from .search_customers_response import SearchCustomersResponse
    from .search_invoices_response import SearchInvoicesResponse
    from .search_loyalty_accounts_request_loyalty_account_query import SearchLoyaltyAccountsRequestLoyaltyAccountQuery
    from .search_loyalty_accounts_response import SearchLoyaltyAccountsResponse
    from .search_loyalty_events_response import SearchLoyaltyEventsResponse
    from .search_loyalty_rewards_request_loyalty_reward_query import SearchLoyaltyRewardsRequestLoyaltyRewardQuery
    from .search_loyalty_rewards_response import SearchLoyaltyRewardsResponse
    from .search_orders_customer_filter import SearchOrdersCustomerFilter
    from .search_orders_date_time_filter import SearchOrdersDateTimeFilter
    from .search_orders_filter import SearchOrdersFilter
    from .search_orders_fulfillment_filter import SearchOrdersFulfillmentFilter
    from .search_orders_query import SearchOrdersQuery
    from .search_orders_response import SearchOrdersResponse
    from .search_orders_sort import SearchOrdersSort
    from .search_orders_sort_field import SearchOrdersSortField
    from .search_orders_source_filter import SearchOrdersSourceFilter
    from .search_orders_state_filter import SearchOrdersStateFilter
    from .search_shifts_response import SearchShiftsResponse
    from .search_subscriptions_filter import SearchSubscriptionsFilter
    from .search_subscriptions_query import SearchSubscriptionsQuery
    from .search_subscriptions_response import SearchSubscriptionsResponse
    from .search_team_members_filter import SearchTeamMembersFilter
    from .search_team_members_query import SearchTeamMembersQuery
    from .search_team_members_response import SearchTeamMembersResponse
    from .search_terminal_checkouts_response import SearchTerminalCheckoutsResponse
    from .search_terminal_refunds_response import SearchTerminalRefundsResponse
    from .segment_filter import SegmentFilter
    from .shift import Shift
    from .shift_filter import ShiftFilter
    from .shift_filter_status import ShiftFilterStatus
    from .shift_query import ShiftQuery
    from .shift_sort import ShiftSort
    from .shift_sort_field import ShiftSortField
    from .shift_status import ShiftStatus
    from .shift_wage import ShiftWage
    from .shift_workday import ShiftWorkday
    from .shift_workday_matcher import ShiftWorkdayMatcher
    from .site import Site
    from .snippet import Snippet
    from .snippet_response import SnippetResponse
    from .sort_order import SortOrder
    from .source_application import SourceApplication
    from .standard_unit_description import StandardUnitDescription
    from .standard_unit_description_group import StandardUnitDescriptionGroup
    from .status import Status
    from .submit_evidence_request import SubmitEvidenceRequest
    from .submit_evidence_response import SubmitEvidenceResponse
    from .subscription import Subscription
    from .subscription_cadence import SubscriptionCadence
    from .subscription_event import SubscriptionEvent
    from .subscription_event_info import SubscriptionEventInfo
    from .subscription_event_info_code import SubscriptionEventInfoCode
    from .subscription_event_subscription_event_type import SubscriptionEventSubscriptionEventType
    from .subscription_phase import SubscriptionPhase
    from .subscription_status import SubscriptionStatus
    from .tax_calculation_phase import TaxCalculationPhase
    from .tax_ids import TaxIds
    from .tax_inclusion_type import TaxInclusionType
    from .team_member import TeamMember
    from .team_member_assigned_locations import TeamMemberAssignedLocations
    from .team_member_assigned_locations_assignment_type import TeamMemberAssignedLocationsAssignmentType
    from .team_member_booking_profile import TeamMemberBookingProfile
    from .team_member_invitation_status import TeamMemberInvitationStatus
    from .team_member_status import TeamMemberStatus
    from .team_member_wage import TeamMemberWage
    from .tender import Tender
    from .tender_card_details import TenderCardDetails
    from .tender_card_details_entry_method import TenderCardDetailsEntryMethod
    from .tender_card_details_status import TenderCardDetailsStatus
    from .tender_cash_details import TenderCashDetails
    from .tender_type import TenderType
    from .terminal_checkout import TerminalCheckout
    from .terminal_checkout_query import TerminalCheckoutQuery
    from .terminal_checkout_query_filter import TerminalCheckoutQueryFilter
    from .terminal_checkout_query_sort import TerminalCheckoutQuerySort
    from .terminal_refund import TerminalRefund
    from .terminal_refund_query import TerminalRefundQuery
    from .terminal_refund_query_filter import TerminalRefundQueryFilter
    from .terminal_refund_query_sort import TerminalRefundQuerySort
    from .time_range import TimeRange
    from .tip_settings import TipSettings
    from .transaction import Transaction
    from .transaction_product import TransactionProduct
    from .transaction_type import TransactionType
    from .type import Type
    from .unlink_customer_from_gift_card_response import UnlinkCustomerFromGiftCardResponse
    from .update_booking_response import UpdateBookingResponse
    from .update_break_type_response import UpdateBreakTypeResponse
    from .update_customer_group_response import UpdateCustomerGroupResponse
    from .update_customer_response import UpdateCustomerResponse
    from .update_invoice_response import UpdateInvoiceResponse
    from .update_item_modifier_lists_response import UpdateItemModifierListsResponse
    from .update_item_taxes_response import UpdateItemTaxesResponse
    from .update_location_response import UpdateLocationResponse
    from .update_order_response import UpdateOrderResponse
    from .update_payment_response import UpdatePaymentResponse
    from .update_shift_response import UpdateShiftResponse
    from .update_subscription_response import UpdateSubscriptionResponse
    from .update_team_member_request import UpdateTeamMemberRequest
    from .update_team_member_response import UpdateTeamMemberResponse
    from .update_wage_setting_response import UpdateWageSettingResponse
    from .update_workweek_config_response import UpdateWorkweekConfigResponse
    from .upsert_catalog_object_response import UpsertCatalogObjectResponse
    from .upsert_snippet_response import UpsertSnippetResponse
    from .v1create_employee_role_request import V1CreateEmployeeRoleRequest
    from .v1create_refund_request_type import V1CreateRefundRequestType
    from .v1employee import V1Employee
    from .v1employee_role import V1EmployeeRole
    from .v1employee_role_permissions import V1EmployeeRolePermissions
    from .v1employee_status import V1EmployeeStatus
    from .v1list_employee_roles_request import V1ListEmployeeRolesRequest
    from .v1list_employee_roles_response import V1ListEmployeeRolesResponse
    from .v1list_employees_request import V1ListEmployeesRequest
    from .v1list_employees_request_status import V1ListEmployeesRequestStatus
    from .v1list_employees_response import V1ListEmployeesResponse
    from .v1list_orders_request import V1ListOrdersRequest
    from .v1list_orders_response import V1ListOrdersResponse
    from .v1list_payments_request import V1ListPaymentsRequest
    from .v1list_payments_response import V1ListPaymentsResponse
    from .v1list_refunds_request import V1ListRefundsRequest
    from .v1list_refunds_response import V1ListRefundsResponse
    from .v1list_settlements_request import V1ListSettlementsRequest
    from .v1list_settlements_request_status import V1ListSettlementsRequestStatus
    from .v1list_settlements_response import V1ListSettlementsResponse
    from .v1money import V1Money
    from .v1order import V1Order
    from .v1order_history_entry import V1OrderHistoryEntry
    from .v1order_history_entry_action import V1OrderHistoryEntryAction
    from .v1order_state import V1OrderState
    from .v1payment import V1Payment
    from .v1payment_discount import V1PaymentDiscount
    from .v1payment_item_detail import V1PaymentItemDetail
    from .v1payment_itemization import V1PaymentItemization
    from .v1payment_itemization_itemization_type import V1PaymentItemizationItemizationType
    from .v1payment_modifier import V1PaymentModifier
    from .v1payment_surcharge import V1PaymentSurcharge
    from .v1payment_surcharge_type import V1PaymentSurchargeType
    from .v1payment_tax import V1PaymentTax
    from .v1payment_tax_inclusion_type import V1PaymentTaxInclusionType
    from .v1phone_number import V1PhoneNumber
    from .v1refund import V1Refund
    from .v1refund_type import V1RefundType
    from .v1retrieve_employee_request import V1RetrieveEmployeeRequest
    from .v1retrieve_employee_role_request import V1RetrieveEmployeeRoleRequest
    from .v1retrieve_order_request import V1RetrieveOrderRequest
    from .v1retrieve_payment_request import V1RetrievePaymentRequest
    from .v1retrieve_settlement_request import V1RetrieveSettlementRequest
    from .v1settlement import V1Settlement
    from .v1settlement_entry import V1SettlementEntry
    from .v1settlement_entry_type import V1SettlementEntryType
    from .v1settlement_status import V1SettlementStatus
    from .v1tender import V1Tender
    from .v1tender_card_brand import V1TenderCardBrand
    from .v1tender_entry_method import V1TenderEntryMethod
    from .v1tender_type import V1TenderType
    from .v1update_employee_request import V1UpdateEmployeeRequest
    from .v1update_employee_role_request import V1UpdateEmployeeRoleRequest
    from .v1update_order_request_action import V1UpdateOrderRequestAction
    from .void_transaction_request import VoidTransactionRequest
    from .void_transaction_response import VoidTransactionResponse
    from .wage_setting import WageSetting
    from .weekday import Weekday
    from .workweek_config import WorkweekConfig
_dynamic_imports: typing.Dict[str, str] = {
    "AcceptDisputeRequest": ".accept_dispute_request",
    "AcceptDisputeResponse": ".accept_dispute_response",
    "AccumulateLoyaltyPointsResponse": ".accumulate_loyalty_points_response",
    "AchDetails": ".ach_details",
    "ActionCancelReason": ".action_cancel_reason",
    "AddGroupToCustomerRequest": ".add_group_to_customer_request",
    "AddGroupToCustomerResponse": ".add_group_to_customer_response",
    "AdditionalRecipient": ".additional_recipient",
    "Address": ".address",
    "AdjustLoyaltyPointsResponse": ".adjust_loyalty_points_response",
    "AppointmentSegment": ".appointment_segment",
    "Availability": ".availability",
    "BankAccount": ".bank_account",
    "BankAccountPaymentDetails": ".bank_account_payment_details",
    "BankAccountStatus": ".bank_account_status",
    "BankAccountType": ".bank_account_type",
    "BatchChangeInventoryRequest": ".batch_change_inventory_request",
    "BatchChangeInventoryResponse": ".batch_change_inventory_response",
    "BatchDeleteCatalogObjectsResponse": ".batch_delete_catalog_objects_response",
    "BatchRetrieveCatalogObjectsResponse": ".batch_retrieve_catalog_objects_response",
    "BatchRetrieveInventoryChangesRequest": ".batch_retrieve_inventory_changes_request",
    "BatchRetrieveInventoryChangesResponse": ".batch_retrieve_inventory_changes_response",
    "BatchRetrieveInventoryCountsRequest": ".batch_retrieve_inventory_counts_request",
    "BatchRetrieveInventoryCountsResponse": ".batch_retrieve_inventory_counts_response",
    "BatchRetrieveOrdersResponse": ".batch_retrieve_orders_response",
    "BatchUpsertCatalogObjectsResponse": ".batch_upsert_catalog_objects_response",
    "Booking": ".booking",
    "BookingStatus": ".booking_status",
    "Break": ".break_",
    "BreakType": ".break_type",
    "BulkCreateTeamMembersResponse": ".bulk_create_team_members_response",
    "BulkUpdateTeamMembersResponse": ".bulk_update_team_members_response",
    "BusinessAppointmentSettings": ".business_appointment_settings",
    "BusinessAppointmentSettingsAlignmentTime": ".business_appointment_settings_alignment_time",
    "BusinessAppointmentSettingsBookingLocationType": ".business_appointment_settings_booking_location_type",
    "BusinessAppointmentSettingsCancellationPolicy": ".business_appointment_settings_cancellation_policy",
    "BusinessAppointmentSettingsMaxAppointmentsPerDayLimitType": ".business_appointment_settings_max_appointments_per_day_limit_type",
    "BusinessBookingProfile": ".business_booking_profile",
    "BusinessBookingProfileBookingPolicy": ".business_booking_profile_booking_policy",
    "BusinessBookingProfileCustomerTimezoneChoice": ".business_booking_profile_customer_timezone_choice",
    "BusinessHours": ".business_hours",
    "BusinessHoursPeriod": ".business_hours_period",
    "CalculateLoyaltyPointsResponse": ".calculate_loyalty_points_response",
    "CalculateOrderResponse": ".calculate_order_response",
    "CancelBookingResponse": ".cancel_booking_response",
    "CancelInvoiceResponse": ".cancel_invoice_response",
    "CancelPaymentByIdempotencyKeyResponse": ".cancel_payment_by_idempotency_key_response",
    "CancelPaymentRequest": ".cancel_payment_request",
    "CancelPaymentResponse": ".cancel_payment_response",
    "CancelSubscriptionRequest": ".cancel_subscription_request",
    "CancelSubscriptionResponse": ".cancel_subscription_response",
    "CancelTerminalCheckoutRequest": ".cancel_terminal_checkout_request",
    "CancelTerminalCheckoutResponse": ".cancel_terminal_checkout_response",
    "CancelTerminalRefundRequest": ".cancel_terminal_refund_request",
    "CancelTerminalRefundResponse": ".cancel_terminal_refund_response",
    "CaptureTransactionRequest": ".capture_transaction_request",
    "CaptureTransactionResponse": ".capture_transaction_response",
    "Card": ".card",
    "CardBrand": ".card_brand",
    "CardPaymentDetails": ".card_payment_details",
    "CardPaymentTimeline": ".card_payment_timeline",
    "CardPrepaidType": ".card_prepaid_type",
    "CardSquareProduct": ".card_square_product",
    "CardType": ".card_type",
    "CashDrawerDevice": ".cash_drawer_device",
    "CashDrawerEventType": ".cash_drawer_event_type",
    "CashDrawerShift": ".cash_drawer_shift",
    "CashDrawerShiftEvent": ".cash_drawer_shift_event",
    "CashDrawerShiftState": ".cash_drawer_shift_state",
    "CashDrawerShiftSummary": ".cash_drawer_shift_summary",
    "CashPaymentDetails": ".cash_payment_details",
    "CatalogCategory": ".catalog_category",
    "CatalogCustomAttributeDefinition": ".catalog_custom_attribute_definition",
    "CatalogCustomAttributeDefinitionAppVisibility": ".catalog_custom_attribute_definition_app_visibility",
    "CatalogCustomAttributeDefinitionNumberConfig": ".catalog_custom_attribute_definition_number_config",
    "CatalogCustomAttributeDefinitionSelectionConfig": ".catalog_custom_attribute_definition_selection_config",
    "CatalogCustomAttributeDefinitionSelectionConfigCustomAttributeSelection": ".catalog_custom_attribute_definition_selection_config_custom_attribute_selection",
    "CatalogCustomAttributeDefinitionSellerVisibility": ".catalog_custom_attribute_definition_seller_visibility",
    "CatalogCustomAttributeDefinitionStringConfig": ".catalog_custom_attribute_definition_string_config",
    "CatalogCustomAttributeDefinitionType": ".catalog_custom_attribute_definition_type",
    "CatalogCustomAttributeValue": ".catalog_custom_attribute_value",
    "CatalogDiscount": ".catalog_discount",
    "CatalogDiscountModifyTaxBasis": ".catalog_discount_modify_tax_basis",
    "CatalogDiscountType": ".catalog_discount_type",
    "CatalogIdMapping": ".catalog_id_mapping",
    "CatalogImage": ".catalog_image",
    "CatalogInfoRequest": ".catalog_info_request",
    "CatalogInfoResponse": ".catalog_info_response",
    "CatalogInfoResponseLimits": ".catalog_info_response_limits",
    "CatalogItem": ".catalog_item",
    "CatalogItemModifierListInfo": ".catalog_item_modifier_list_info",
    "CatalogItemOption": ".catalog_item_option",
    "CatalogItemOptionForItem": ".catalog_item_option_for_item",
    "CatalogItemOptionValue": ".catalog_item_option_value",
    "CatalogItemOptionValueForItemVariation": ".catalog_item_option_value_for_item_variation",
    "CatalogItemProductType": ".catalog_item_product_type",
    "CatalogItemVariation": ".catalog_item_variation",
    "CatalogMeasurementUnit": ".catalog_measurement_unit",
    "CatalogModifier": ".catalog_modifier",
    "CatalogModifierList": ".catalog_modifier_list",
    "CatalogModifierListSelectionType": ".catalog_modifier_list_selection_type",
    "CatalogModifierOverride": ".catalog_modifier_override",
    "CatalogObject": ".catalog_object",
    "CatalogObjectBatch": ".catalog_object_batch",
    "CatalogObjectReference": ".catalog_object_reference",
    "CatalogObjectType": ".catalog_object_type",
    "CatalogPricingRule": ".catalog_pricing_rule",
    "CatalogPricingType": ".catalog_pricing_type",
    "CatalogProductSet": ".catalog_product_set",
    "CatalogQuery": ".catalog_query",
    "CatalogQueryExact": ".catalog_query_exact",
    "CatalogQueryItemVariationsForItemOptionValues": ".catalog_query_item_variations_for_item_option_values",
    "CatalogQueryItemsForItemOptions": ".catalog_query_items_for_item_options",
    "CatalogQueryItemsForModifierList": ".catalog_query_items_for_modifier_list",
    "CatalogQueryItemsForTax": ".catalog_query_items_for_tax",
    "CatalogQueryPrefix": ".catalog_query_prefix",
    "CatalogQueryRange": ".catalog_query_range",
    "CatalogQuerySet": ".catalog_query_set",
    "CatalogQuerySortedAttribute": ".catalog_query_sorted_attribute",
    "CatalogQueryText": ".catalog_query_text",
    "CatalogQuickAmount": ".catalog_quick_amount",
    "CatalogQuickAmountType": ".catalog_quick_amount_type",
    "CatalogQuickAmountsSettings": ".catalog_quick_amounts_settings",
    "CatalogQuickAmountsSettingsOption": ".catalog_quick_amounts_settings_option",
    "CatalogStockConversion": ".catalog_stock_conversion",
    "CatalogSubscriptionPlan": ".catalog_subscription_plan",
    "CatalogTax": ".catalog_tax",
    "CatalogTimePeriod": ".catalog_time_period",
    "CatalogV1Id": ".catalog_v1id",
    "ChargeRequestAdditionalRecipient": ".charge_request_additional_recipient",
    "ChargeResponse": ".charge_response",
    "CheckAppointmentsOnboardedRequest": ".check_appointments_onboarded_request",
    "Checkout": ".checkout",
    "CheckoutOptionsPaymentType": ".checkout_options_payment_type",
    "CompletePaymentRequest": ".complete_payment_request",
    "CompletePaymentResponse": ".complete_payment_response",
    "Coordinates": ".coordinates",
    "Country": ".country",
    "CreateBookingResponse": ".create_booking_response",
    "CreateBreakTypeResponse": ".create_break_type_response",
    "CreateCardResponse": ".create_card_response",
    "CreateCheckoutResponse": ".create_checkout_response",
    "CreateCustomerCardResponse": ".create_customer_card_response",
    "CreateCustomerGroupResponse": ".create_customer_group_response",
    "CreateCustomerResponse": ".create_customer_response",
    "CreateDeviceCodeResponse": ".create_device_code_response",
    "CreateDisputeEvidenceTextResponse": ".create_dispute_evidence_text_response",
    "CreateGiftCardActivityResponse": ".create_gift_card_activity_response",
    "CreateGiftCardResponse": ".create_gift_card_response",
    "CreateInvoiceResponse": ".create_invoice_response",
    "CreateLocationResponse": ".create_location_response",
    "CreateLoyaltyAccountResponse": ".create_loyalty_account_response",
    "CreateLoyaltyRewardResponse": ".create_loyalty_reward_response",
    "CreateMobileAuthorizationCodeResponse": ".create_mobile_authorization_code_response",
    "CreateOrderRequest": ".create_order_request",
    "CreateOrderResponse": ".create_order_response",
    "CreatePaymentResponse": ".create_payment_response",
    "CreateRefundResponse": ".create_refund_response",
    "CreateShiftResponse": ".create_shift_response",
    "CreateSubscriptionResponse": ".create_subscription_response",
    "CreateTeamMemberRequest": ".create_team_member_request",
    "CreateTeamMemberResponse": ".create_team_member_response",
    "CreateTerminalCheckoutResponse": ".create_terminal_checkout_response",
    "CreateTerminalRefundResponse": ".create_terminal_refund_response",
    "Currency": ".currency",
    "CustomAttributeFilter": ".custom_attribute_filter",
    "Customer": ".customer",
    "CustomerCreationSource": ".customer_creation_source",
    "CustomerCreationSourceFilter": ".customer_creation_source_filter",
    "CustomerFilter": ".customer_filter",
    "CustomerGroup": ".customer_group",
    "CustomerInclusionExclusion": ".customer_inclusion_exclusion",
    "CustomerPreferences": ".customer_preferences",
    "CustomerQuery": ".customer_query",
    "CustomerSegment": ".customer_segment",
    "CustomerSort": ".customer_sort",
    "CustomerSortField": ".customer_sort_field",
    "CustomerTextFilter": ".customer_text_filter",
    "DateRange": ".date_range",
    "DayOfWeek": ".day_of_week",
    "DeleteBreakTypeRequest": ".delete_break_type_request",
    "DeleteBreakTypeResponse": ".delete_break_type_response",
    "DeleteCatalogObjectRequest": ".delete_catalog_object_request",
    "DeleteCatalogObjectResponse": ".delete_catalog_object_response",
    "DeleteCustomerCardRequest": ".delete_customer_card_request",
    "DeleteCustomerCardResponse": ".delete_customer_card_response",
    "DeleteCustomerGroupRequest": ".delete_customer_group_request",
    "DeleteCustomerGroupResponse": ".delete_customer_group_response",
    "DeleteCustomerRequest": ".delete_customer_request",
    "DeleteCustomerResponse": ".delete_customer_response",
    "DeleteDisputeEvidenceRequest": ".delete_dispute_evidence_request",
    "DeleteDisputeEvidenceResponse": ".delete_dispute_evidence_response",
    "DeleteInvoiceRequest": ".delete_invoice_request",
    "DeleteInvoiceResponse": ".delete_invoice_response",
    "DeleteLoyaltyRewardRequest": ".delete_loyalty_reward_request",
    "DeleteLoyaltyRewardResponse": ".delete_loyalty_reward_response",
    "DeleteShiftRequest": ".delete_shift_request",
    "DeleteShiftResponse": ".delete_shift_response",
    "DeleteSnippetRequest": ".delete_snippet_request",
    "DeleteSnippetResponse": ".delete_snippet_response",
    "DeprecatedCreateDisputeEvidenceFileRequest": ".deprecated_create_dispute_evidence_file_request",
    "DeprecatedCreateDisputeEvidenceFileResponse": ".deprecated_create_dispute_evidence_file_response",
    "DeprecatedCreateDisputeEvidenceTextRequest": ".deprecated_create_dispute_evidence_text_request",
    "DeprecatedCreateDisputeEvidenceTextResponse": ".deprecated_create_dispute_evidence_text_response",
    "Device": ".device",
    "DeviceCheckoutOptions": ".device_checkout_options",
    "DeviceCode": ".device_code",
    "DeviceCodeStatus": ".device_code_status",
    "DeviceDetails": ".device_details",
    "DigitalWalletDetails": ".digital_wallet_details",
    "DisableCardRequest": ".disable_card_request",
    "DisableCardResponse": ".disable_card_response",
    "Dispute": ".dispute",
    "DisputeEvidence": ".dispute_evidence",
    "DisputeEvidenceCreatedWebhook": ".dispute_evidence_created_webhook",
    "DisputeEvidenceCreatedWebhookData": ".dispute_evidence_created_webhook_data",
    "DisputeEvidenceCreatedWebhookObject": ".dispute_evidence_created_webhook_object",
    "DisputeEvidenceFile": ".dispute_evidence_file",
    "DisputeEvidenceType": ".dispute_evidence_type",
    "DisputeReason": ".dispute_reason",
    "DisputeState": ".dispute_state",
    "DisputedPayment": ".disputed_payment",
    "EcomVisibility": ".ecom_visibility",
    "Employee": ".employee",
    "EmployeeStatus": ".employee_status",
    "EmployeeWage": ".employee_wage",
    "Error": ".error",
    "ErrorCategory": ".error_category",
    "ErrorCode": ".error_code",
    "ExcludeStrategy": ".exclude_strategy",
    "ExternalPaymentDetails": ".external_payment_details",
    "FilterValue": ".filter_value",
    "GanSource": ".gan_source",
    "GetBankAccountByV1IdRequest": ".get_bank_account_by_v1id_request",
    "GetBankAccountByV1IdResponse": ".get_bank_account_by_v1id_response",
    "GetBankAccountRequest": ".get_bank_account_request",
    "GetBankAccountResponse": ".get_bank_account_response",
    "GetBreakTypeRequest": ".get_break_type_request",
    "GetBreakTypeResponse": ".get_break_type_response",
    "GetDeviceCodeRequest": ".get_device_code_request",
    "GetDeviceCodeResponse": ".get_device_code_response",
    "GetEmployeeWageRequest": ".get_employee_wage_request",
    "GetEmployeeWageResponse": ".get_employee_wage_response",
    "GetInvoiceRequest": ".get_invoice_request",
    "GetInvoiceResponse": ".get_invoice_response",
    "GetPaymentRefundRequest": ".get_payment_refund_request",
    "GetPaymentRefundResponse": ".get_payment_refund_response",
    "GetPaymentRequest": ".get_payment_request",
    "GetPaymentResponse": ".get_payment_response",
    "GetShiftRequest": ".get_shift_request",
    "GetShiftResponse": ".get_shift_response",
    "GetTeamMemberWageRequest": ".get_team_member_wage_request",
    "GetTeamMemberWageResponse": ".get_team_member_wage_response",
    "GetTerminalCheckoutRequest": ".get_terminal_checkout_request",
    "GetTerminalCheckoutResponse": ".get_terminal_checkout_response",
    "GetTerminalRefundRequest": ".get_terminal_refund_request",
    "GetTerminalRefundResponse": ".get_terminal_refund_response",
    "GiftCard": ".gift_card",
    "GiftCardActivity": ".gift_card_activity",
    "GiftCardActivityActivate": ".gift_card_activity_activate",
    "GiftCardActivityAdjustDecrement": ".gift_card_activity_adjust_decrement",
    "GiftCardActivityAdjustDecrementReason": ".gift_card_activity_adjust_decrement_reason",
    "GiftCardActivityAdjustIncrement": ".gift_card_activity_adjust_increment",
    "GiftCardActivityAdjustIncrementReason": ".gift_card_activity_adjust_increment_reason",
    "GiftCardActivityBlock": ".gift_card_activity_block",
    "GiftCardActivityBlockReason": ".gift_card_activity_block_reason",
    "GiftCardActivityClearBalance": ".gift_card_activity_clear_balance",
    "GiftCardActivityClearBalanceReason": ".gift_card_activity_clear_balance_reason",
    "GiftCardActivityDeactivate": ".gift_card_activity_deactivate",
    "GiftCardActivityDeactivateReason": ".gift_card_activity_deactivate_reason",
    "GiftCardActivityImport": ".gift_card_activity_import",
    "GiftCardActivityImportReversal": ".gift_card_activity_import_reversal",
    "GiftCardActivityLoad": ".gift_card_activity_load",
    "GiftCardActivityRedeem": ".gift_card_activity_redeem",
    "GiftCardActivityRefund": ".gift_card_activity_refund",
    "GiftCardActivityType": ".gift_card_activity_type",
    "GiftCardActivityUnblock": ".gift_card_activity_unblock",
    "GiftCardActivityUnblockReason": ".gift_card_activity_unblock_reason",
    "GiftCardActivityUnlinkedActivityRefund": ".gift_card_activity_unlinked_activity_refund",
    "GiftCardGanSource": ".gift_card_gan_source",
    "GiftCardStatus": ".gift_card_status",
    "GiftCardType": ".gift_card_type",
    "Info": ".info",
    "InfoCode": ".info_code",
    "InlineTypes": ".inline_types",
    "InventoryAdjustment": ".inventory_adjustment",
    "InventoryAdjustmentGroup": ".inventory_adjustment_group",
    "InventoryAlertType": ".inventory_alert_type",
    "InventoryChange": ".inventory_change",
    "InventoryChangeType": ".inventory_change_type",
    "InventoryCount": ".inventory_count",
    "InventoryPhysicalCount": ".inventory_physical_count",
    "InventoryState": ".inventory_state",
    "InventoryTransfer": ".inventory_transfer",
    "Invoice": ".invoice",
    "InvoiceAcceptedPaymentMethods": ".invoice_accepted_payment_methods",
    "InvoiceAutomaticPaymentSource": ".invoice_automatic_payment_source",
    "InvoiceCustomField": ".invoice_custom_field",
    "InvoiceCustomFieldPlacement": ".invoice_custom_field_placement",
    "InvoiceDeliveryMethod": ".invoice_delivery_method",
    "InvoiceDeliveryMethodInvoiceDeliveryMethod": ".invoice_delivery_method_invoice_delivery_method",
    "InvoiceFilter": ".invoice_filter",
    "InvoicePaymentReminder": ".invoice_payment_reminder",
    "InvoicePaymentReminderStatus": ".invoice_payment_reminder_status",
    "InvoicePaymentRequest": ".invoice_payment_request",
    "InvoiceQuery": ".invoice_query",
    "InvoiceRecipient": ".invoice_recipient",
    "InvoiceRequestMethod": ".invoice_request_method",
    "InvoiceRequestType": ".invoice_request_type",
    "InvoiceSort": ".invoice_sort",
    "InvoiceSortField": ".invoice_sort_field",
    "InvoiceStatus": ".invoice_status",
    "ItemVariationLocationOverrides": ".item_variation_location_overrides",
    "JobAssignment": ".job_assignment",
    "JobAssignmentPayType": ".job_assignment_pay_type",
    "LinkCustomerToGiftCardResponse": ".link_customer_to_gift_card_response",
    "ListBankAccountsRequest": ".list_bank_accounts_request",
    "ListBankAccountsResponse": ".list_bank_accounts_response",
    "ListBreakTypesRequest": ".list_break_types_request",
    "ListBreakTypesResponse": ".list_break_types_response",
    "ListCardsRequest": ".list_cards_request",
    "ListCardsResponse": ".list_cards_response",
    "ListCashDrawerShiftEventsRequest": ".list_cash_drawer_shift_events_request",
    "ListCashDrawerShiftEventsResponse": ".list_cash_drawer_shift_events_response",
    "ListCashDrawerShiftsRequest": ".list_cash_drawer_shifts_request",
    "ListCashDrawerShiftsResponse": ".list_cash_drawer_shifts_response",
    "ListCatalogRequest": ".list_catalog_request",
    "ListCatalogResponse": ".list_catalog_response",
    "ListCustomerGroupsRequest": ".list_customer_groups_request",
    "ListCustomerGroupsResponse": ".list_customer_groups_response",
    "ListCustomerSegmentsRequest": ".list_customer_segments_request",
    "ListCustomerSegmentsResponse": ".list_customer_segments_response",
    "ListCustomersRequest": ".list_customers_request",
    "ListCustomersResponse": ".list_customers_response",
    "ListDeviceCodesRequest": ".list_device_codes_request",
    "ListDeviceCodesResponse": ".list_device_codes_response",
    "ListDisputeEvidenceRequest": ".list_dispute_evidence_request",
    "ListDisputeEvidenceResponse": ".list_dispute_evidence_response",
    "ListDisputesRequest": ".list_disputes_request",
    "ListDisputesResponse": ".list_disputes_response",
    "ListEmployeeWagesRequest": ".list_employee_wages_request",
    "ListEmployeeWagesResponse": ".list_employee_wages_response",
    "ListEmployeesRequest": ".list_employees_request",
    "ListEmployeesResponse": ".list_employees_response",
    "ListGiftCardActivitiesRequest": ".list_gift_card_activities_request",
    "ListGiftCardActivitiesResponse": ".list_gift_card_activities_response",
    "ListGiftCardsRequest": ".list_gift_cards_request",
    "ListGiftCardsResponse": ".list_gift_cards_response",
    "ListInvoicesRequest": ".list_invoices_request",
    "ListInvoicesResponse": ".list_invoices_response",
    "ListLocationsRequest": ".list_locations_request",
    "ListLocationsResponse": ".list_locations_response",
    "ListLoyaltyProgramsRequest": ".list_loyalty_programs_request",
    "ListLoyaltyProgramsResponse": ".list_loyalty_programs_response",
    "ListMerchantsRequest": ".list_merchants_request",
    "ListMerchantsResponse": ".list_merchants_response",
    "ListPaymentRefundsRequest": ".list_payment_refunds_request",
    "ListPaymentRefundsResponse": ".list_payment_refunds_response",
    "ListPaymentsRequest": ".list_payments_request",
    "ListPaymentsResponse": ".list_payments_response",
    "ListRefundsRequest": ".list_refunds_request",
    "ListRefundsResponse": ".list_refunds_response",
    "ListSitesRequest": ".list_sites_request",
    "ListSitesResponse": ".list_sites_response",
    "ListSubscriptionEventsRequest": ".list_subscription_events_request",
    "ListSubscriptionEventsResponse": ".list_subscription_events_response",
    "ListTeamMemberBookingProfilesRequest": ".list_team_member_booking_profiles_request",
    "ListTeamMemberBookingProfilesResponse": ".list_team_member_booking_profiles_response",
    "ListTeamMemberWagesRequest": ".list_team_member_wages_request",
    "ListTeamMemberWagesResponse": ".list_team_member_wages_response",
    "ListTransactionsRequest": ".list_transactions_request",
    "ListTransactionsResponse": ".list_transactions_response",
    "ListWorkweekConfigsRequest": ".list_workweek_configs_request",
    "ListWorkweekConfigsResponse": ".list_workweek_configs_response",
    "Location": ".location",
    "LocationCapability": ".location_capability",
    "LocationStatus": ".location_status",
    "LocationType": ".location_type",
    "LoyaltyAccount": ".loyalty_account",
    "LoyaltyAccountExpiringPointDeadline": ".loyalty_account_expiring_point_deadline",
    "LoyaltyAccountMapping": ".loyalty_account_mapping",
    "LoyaltyAccountMappingType": ".loyalty_account_mapping_type",
    "LoyaltyEvent": ".loyalty_event",
    "LoyaltyEventAccumulatePoints": ".loyalty_event_accumulate_points",
    "LoyaltyEventAdjustPoints": ".loyalty_event_adjust_points",
    "LoyaltyEventCreateReward": ".loyalty_event_create_reward",
    "LoyaltyEventDateTimeFilter": ".loyalty_event_date_time_filter",
    "LoyaltyEventDeleteReward": ".loyalty_event_delete_reward",
    "LoyaltyEventExpirePoints": ".loyalty_event_expire_points",
    "LoyaltyEventFilter": ".loyalty_event_filter",
    "LoyaltyEventLocationFilter": ".loyalty_event_location_filter",
    "LoyaltyEventLoyaltyAccountFilter": ".loyalty_event_loyalty_account_filter",
    "LoyaltyEventOrderFilter": ".loyalty_event_order_filter",
    "LoyaltyEventOther": ".loyalty_event_other",
    "LoyaltyEventQuery": ".loyalty_event_query",
    "LoyaltyEventRedeemReward": ".loyalty_event_redeem_reward",
    "LoyaltyEventSource": ".loyalty_event_source",
    "LoyaltyEventType": ".loyalty_event_type",
    "LoyaltyEventTypeFilter": ".loyalty_event_type_filter",
    "LoyaltyProgram": ".loyalty_program",
    "LoyaltyProgramAccrualRule": ".loyalty_program_accrual_rule",
    "LoyaltyProgramAccrualRuleType": ".loyalty_program_accrual_rule_type",
    "LoyaltyProgramExpirationPolicy": ".loyalty_program_expiration_policy",
    "LoyaltyProgramRewardDefinition": ".loyalty_program_reward_definition",
    "LoyaltyProgramRewardDefinitionScope": ".loyalty_program_reward_definition_scope",
    "LoyaltyProgramRewardDefinitionType": ".loyalty_program_reward_definition_type",
    "LoyaltyProgramRewardTier": ".loyalty_program_reward_tier",
    "LoyaltyProgramStatus": ".loyalty_program_status",
    "LoyaltyProgramTerminology": ".loyalty_program_terminology",
    "LoyaltyReward": ".loyalty_reward",
    "LoyaltyRewardStatus": ".loyalty_reward_status",
    "MeasurementUnit": ".measurement_unit",
    "MeasurementUnitArea": ".measurement_unit_area",
    "MeasurementUnitCustom": ".measurement_unit_custom",
    "MeasurementUnitGeneric": ".measurement_unit_generic",
    "MeasurementUnitLength": ".measurement_unit_length",
    "MeasurementUnitTime": ".measurement_unit_time",
    "MeasurementUnitUnitType": ".measurement_unit_unit_type",
    "MeasurementUnitVolume": ".measurement_unit_volume",
    "MeasurementUnitWeight": ".measurement_unit_weight",
    "Merchant": ".merchant",
    "MerchantStatus": ".merchant_status",
    "Money": ".money",
    "OauthScope": ".oauth_scope",
    "ObtainTokenResponse": ".obtain_token_response",
    "OnboardAppointmentsRequest": ".onboard_appointments_request",
    "Order": ".order",
    "OrderCreated": ".order_created",
    "OrderCreatedObject": ".order_created_object",
    "OrderEntry": ".order_entry",
    "OrderFulfillment": ".order_fulfillment",
    "OrderFulfillmentPickupDetails": ".order_fulfillment_pickup_details",
    "OrderFulfillmentPickupDetailsCurbsidePickupDetails": ".order_fulfillment_pickup_details_curbside_pickup_details",
    "OrderFulfillmentPickupDetailsScheduleType": ".order_fulfillment_pickup_details_schedule_type",
    "OrderFulfillmentRecipient": ".order_fulfillment_recipient",
    "OrderFulfillmentShipmentDetails": ".order_fulfillment_shipment_details",
    "OrderFulfillmentState": ".order_fulfillment_state",
    "OrderFulfillmentType": ".order_fulfillment_type",
    "OrderFulfillmentUpdated": ".order_fulfillment_updated",
    "OrderFulfillmentUpdatedObject": ".order_fulfillment_updated_object",
    "OrderFulfillmentUpdatedUpdate": ".order_fulfillment_updated_update",
    "OrderLineItem": ".order_line_item",
    "OrderLineItemAppliedDiscount": ".order_line_item_applied_discount",
    "OrderLineItemAppliedTax": ".order_line_item_applied_tax",
    "OrderLineItemDiscount": ".order_line_item_discount",
    "OrderLineItemDiscountScope": ".order_line_item_discount_scope",
    "OrderLineItemDiscountType": ".order_line_item_discount_type",
    "OrderLineItemItemType": ".order_line_item_item_type",
    "OrderLineItemModifier": ".order_line_item_modifier",
    "OrderLineItemPricingBlocklists": ".order_line_item_pricing_blocklists",
    "OrderLineItemPricingBlocklistsBlockedDiscount": ".order_line_item_pricing_blocklists_blocked_discount",
    "OrderLineItemPricingBlocklistsBlockedTax": ".order_line_item_pricing_blocklists_blocked_tax",
    "OrderLineItemTax": ".order_line_item_tax",
    "OrderLineItemTaxScope": ".order_line_item_tax_scope",
    "OrderLineItemTaxType": ".order_line_item_tax_type",
    "OrderMoneyAmounts": ".order_money_amounts",
    "OrderPricingOptions": ".order_pricing_options",
    "OrderQuantityUnit": ".order_quantity_unit",
    "OrderReturn": ".order_return",
    "OrderReturnDiscount": ".order_return_discount",
    "OrderReturnLineItem": ".order_return_line_item",
    "OrderReturnLineItemModifier": ".order_return_line_item_modifier",
    "OrderReturnServiceCharge": ".order_return_service_charge",
    "OrderReturnTax": ".order_return_tax",
    "OrderReward": ".order_reward",
    "OrderRoundingAdjustment": ".order_rounding_adjustment",
    "OrderServiceCharge": ".order_service_charge",
    "OrderServiceChargeCalculationPhase": ".order_service_charge_calculation_phase",
    "OrderServiceChargeType": ".order_service_charge_type",
    "OrderSource": ".order_source",
    "OrderState": ".order_state",
    "OrderUpdated": ".order_updated",
    "OrderUpdatedObject": ".order_updated_object",
    "PayOrderResponse": ".pay_order_response",
    "Payment": ".payment",
    "PaymentOptions": ".payment_options",
    "PaymentRefund": ".payment_refund",
    "ProcessingFee": ".processing_fee",
    "Product": ".product",
    "ProductType": ".product_type",
    "PublishInvoiceResponse": ".publish_invoice_response",
    "QuantityRatio": ".quantity_ratio",
    "Range": ".range",
    "Reason": ".reason",
    "RedeemLoyaltyRewardResponse": ".redeem_loyalty_reward_response",
    "Refund": ".refund",
    "RefundPaymentResponse": ".refund_payment_response",
    "RefundStatus": ".refund_status",
    "RegisterDomainResponse": ".register_domain_response",
    "RegisterDomainResponseStatus": ".register_domain_response_status",
    "RemoveGroupFromCustomerRequest": ".remove_group_from_customer_request",
    "RemoveGroupFromCustomerResponse": ".remove_group_from_customer_response",
    "RenewTokenResponse": ".renew_token_response",
    "ResumeSubscriptionRequest": ".resume_subscription_request",
    "ResumeSubscriptionResponse": ".resume_subscription_response",
    "RetrieveBookingRequest": ".retrieve_booking_request",
    "RetrieveBookingResponse": ".retrieve_booking_response",
    "RetrieveBusinessBookingProfileRequest": ".retrieve_business_booking_profile_request",
    "RetrieveBusinessBookingProfileResponse": ".retrieve_business_booking_profile_response",
    "RetrieveCardRequest": ".retrieve_card_request",
    "RetrieveCardResponse": ".retrieve_card_response",
    "RetrieveCashDrawerShiftRequest": ".retrieve_cash_drawer_shift_request",
    "RetrieveCashDrawerShiftResponse": ".retrieve_cash_drawer_shift_response",
    "RetrieveCatalogObjectRequest": ".retrieve_catalog_object_request",
    "RetrieveCatalogObjectResponse": ".retrieve_catalog_object_response",
    "RetrieveCustomerGroupRequest": ".retrieve_customer_group_request",
    "RetrieveCustomerGroupResponse": ".retrieve_customer_group_response",
    "RetrieveCustomerRequest": ".retrieve_customer_request",
    "RetrieveCustomerResponse": ".retrieve_customer_response",
    "RetrieveCustomerSegmentRequest": ".retrieve_customer_segment_request",
    "RetrieveCustomerSegmentResponse": ".retrieve_customer_segment_response",
    "RetrieveDisputeEvidenceRequest": ".retrieve_dispute_evidence_request",
    "RetrieveDisputeEvidenceResponse": ".retrieve_dispute_evidence_response",
    "RetrieveDisputeRequest": ".retrieve_dispute_request",
    "RetrieveDisputeResponse": ".retrieve_dispute_response",
    "RetrieveEmployeeRequest": ".retrieve_employee_request",
    "RetrieveEmployeeResponse": ".retrieve_employee_response",
    "RetrieveGiftCardFromGanResponse": ".retrieve_gift_card_from_gan_response",
    "RetrieveGiftCardFromNonceResponse": ".retrieve_gift_card_from_nonce_response",
    "RetrieveGiftCardRequest": ".retrieve_gift_card_request",
    "RetrieveGiftCardResponse": ".retrieve_gift_card_response",
    "RetrieveInventoryAdjustmentRequest": ".retrieve_inventory_adjustment_request",
    "RetrieveInventoryAdjustmentResponse": ".retrieve_inventory_adjustment_response",
    "RetrieveInventoryChangesRequest": ".retrieve_inventory_changes_request",
    "RetrieveInventoryChangesResponse": ".retrieve_inventory_changes_response",
    "RetrieveInventoryCountRequest": ".retrieve_inventory_count_request",
    "RetrieveInventoryCountResponse": ".retrieve_inventory_count_response",
    "RetrieveInventoryPhysicalCountRequest": ".retrieve_inventory_physical_count_request",
    "RetrieveInventoryPhysicalCountResponse": ".retrieve_inventory_physical_count_response",
    "RetrieveInventoryTransferRequest": ".retrieve_inventory_transfer_request",
    "RetrieveInventoryTransferResponse": ".retrieve_inventory_transfer_response",
    "RetrieveLocationRequest": ".retrieve_location_request",
    "RetrieveLocationResponse": ".retrieve_location_response",
    "RetrieveLoyaltyAccountRequest": ".retrieve_loyalty_account_request",
    "RetrieveLoyaltyAccountResponse": ".retrieve_loyalty_account_response",
    "RetrieveLoyaltyProgramRequest": ".retrieve_loyalty_program_request",
    "RetrieveLoyaltyProgramResponse": ".retrieve_loyalty_program_response",
    "RetrieveLoyaltyRewardRequest": ".retrieve_loyalty_reward_request",
    "RetrieveLoyaltyRewardResponse": ".retrieve_loyalty_reward_response",
    "RetrieveMerchantRequest": ".retrieve_merchant_request",
    "RetrieveMerchantResponse": ".retrieve_merchant_response",
    "RetrieveObsMigrationProfileRequest": ".retrieve_obs_migration_profile_request",
    "RetrieveOrderRequest": ".retrieve_order_request",
    "RetrieveOrderResponse": ".retrieve_order_response",
    "RetrieveSnippetRequest": ".retrieve_snippet_request",
    "RetrieveSnippetResponse": ".retrieve_snippet_response",
    "RetrieveSubscriptionRequest": ".retrieve_subscription_request",
    "RetrieveSubscriptionResponse": ".retrieve_subscription_response",
    "RetrieveTeamMemberBookingProfileRequest": ".retrieve_team_member_booking_profile_request",
    "RetrieveTeamMemberBookingProfileResponse": ".retrieve_team_member_booking_profile_response",
    "RetrieveTeamMemberRequest": ".retrieve_team_member_request",
    "RetrieveTeamMemberResponse": ".retrieve_team_member_response",
    "RetrieveTransactionRequest": ".retrieve_transaction_request",
    "RetrieveTransactionResponse": ".retrieve_transaction_response",
    "RetrieveWageSettingRequest": ".retrieve_wage_setting_request",
    "RetrieveWageSettingResponse": ".retrieve_wage_setting_response",
    "RevokeTokenResponse": ".revoke_token_response",
    "RiskEvaluation": ".risk_evaluation",
    "RiskEvaluationRiskLevel": ".risk_evaluation_risk_level",
    "SearchAvailabilityFilter": ".search_availability_filter",
    "SearchAvailabilityQuery": ".search_availability_query",
    "SearchAvailabilityResponse": ".search_availability_response",
    "SearchCatalogItemsRequestStockLevel": ".search_catalog_items_request_stock_level",
    "SearchCatalogItemsResponse": ".search_catalog_items_response",
    "SearchCatalogObjectsResponse": ".search_catalog_objects_response",
    "SearchCustomersResponse": ".search_customers_response",
    "SearchInvoicesResponse": ".search_invoices_response",
    "SearchLoyaltyAccountsRequestLoyaltyAccountQuery": ".search_loyalty_accounts_request_loyalty_account_query",
    "SearchLoyaltyAccountsResponse": ".search_loyalty_accounts_response",
    "SearchLoyaltyEventsResponse": ".search_loyalty_events_response",
    "SearchLoyaltyRewardsRequestLoyaltyRewardQuery": ".search_loyalty_rewards_request_loyalty_reward_query",
    "SearchLoyaltyRewardsResponse": ".search_loyalty_rewards_response",
    "SearchOrdersCustomerFilter": ".search_orders_customer_filter",
    "SearchOrdersDateTimeFilter": ".search_orders_date_time_filter",
    "SearchOrdersFilter": ".search_orders_filter",
    "SearchOrdersFulfillmentFilter": ".search_orders_fulfillment_filter",
    "SearchOrdersQuery": ".search_orders_query",
    "SearchOrdersResponse": ".search_orders_response",
    "SearchOrdersSort": ".search_orders_sort",
    "SearchOrdersSortField": ".search_orders_sort_field",
    "SearchOrdersSourceFilter": ".search_orders_source_filter",
    "SearchOrdersStateFilter": ".search_orders_state_filter",
    "SearchShiftsResponse": ".search_shifts_response",
    "SearchSubscriptionsFilter": ".search_subscriptions_filter",
    "SearchSubscriptionsQuery": ".search_subscriptions_query",
    "SearchSubscriptionsResponse": ".search_subscriptions_response",
    "SearchTeamMembersFilter": ".search_team_members_filter",
    "SearchTeamMembersQuery": ".search_team_members_query",
    "SearchTeamMembersResponse": ".search_team_members_response",
    "SearchTerminalCheckoutsResponse": ".search_terminal_checkouts_response",
    "SearchTerminalRefundsResponse": ".search_terminal_refunds_response",
    "SegmentFilter": ".segment_filter",
    "Shift": ".shift",
    "ShiftFilter": ".shift_filter",
    "ShiftFilterStatus": ".shift_filter_status",
    "ShiftQuery": ".shift_query",
    "ShiftSort": ".shift_sort",
    "ShiftSortField": ".shift_sort_field",
    "ShiftStatus": ".shift_status",
    "ShiftWage": ".shift_wage",
    "ShiftWorkday": ".shift_workday",
    "ShiftWorkdayMatcher": ".shift_workday_matcher",
    "Site": ".site",
    "Snippet": ".snippet",
    "SnippetResponse": ".snippet_response",
    "SortOrder": ".sort_order",
    "SourceApplication": ".source_application",
    "StandardUnitDescription": ".standard_unit_description",
    "StandardUnitDescriptionGroup": ".standard_unit_description_group",
    "Status": ".status",
    "SubmitEvidenceRequest": ".submit_evidence_request",
    "SubmitEvidenceResponse": ".submit_evidence_response",
    "Subscription": ".subscription",
    "SubscriptionCadence": ".subscription_cadence",
    "SubscriptionEvent": ".subscription_event",
    "SubscriptionEventInfo": ".subscription_event_info",
    "SubscriptionEventInfoCode": ".subscription_event_info_code",
    "SubscriptionEventSubscriptionEventType": ".subscription_event_subscription_event_type",
    "SubscriptionPhase": ".subscription_phase",
    "SubscriptionStatus": ".subscription_status",
    "TaxCalculationPhase": ".tax_calculation_phase",
    "TaxIds": ".tax_ids",
    "TaxInclusionType": ".tax_inclusion_type",
    "TeamMember": ".team_member",
    "TeamMemberAssignedLocations": ".team_member_assigned_locations",
    "TeamMemberAssignedLocationsAssignmentType": ".team_member_assigned_locations_assignment_type",
    "TeamMemberBookingProfile": ".team_member_booking_profile",
    "TeamMemberInvitationStatus": ".team_member_invitation_status",
    "TeamMemberStatus": ".team_member_status",
    "TeamMemberWage": ".team_member_wage",
    "Tender": ".tender",
    "TenderCardDetails": ".tender_card_details",
    "TenderCardDetailsEntryMethod": ".tender_card_details_entry_method",
    "TenderCardDetailsStatus": ".tender_card_details_status",
    "TenderCashDetails": ".tender_cash_details",
    "TenderType": ".tender_type",
    "TerminalCheckout": ".terminal_checkout",
    "TerminalCheckoutQuery": ".terminal_checkout_query",
    "TerminalCheckoutQueryFilter": ".terminal_checkout_query_filter",
    "TerminalCheckoutQuerySort": ".terminal_checkout_query_sort",
    "TerminalRefund": ".terminal_refund",
    "TerminalRefundQuery": ".terminal_refund_query",
    "TerminalRefundQueryFilter": ".terminal_refund_query_filter",
    "TerminalRefundQuerySort": ".terminal_refund_query_sort",
    "TimeRange": ".time_range",
    "TipSettings": ".tip_settings",
    "Transaction": ".transaction",
    "TransactionProduct": ".transaction_product",
    "TransactionType": ".transaction_type",
    "Type": ".type",
    "UnlinkCustomerFromGiftCardResponse": ".unlink_customer_from_gift_card_response",
    "UpdateBookingResponse": ".update_booking_response",
    "UpdateBreakTypeResponse": ".update_break_type_response",
    "UpdateCustomerGroupResponse": ".update_customer_group_response",
    "UpdateCustomerResponse": ".update_customer_response",
    "UpdateInvoiceResponse": ".update_invoice_response",
    "UpdateItemModifierListsResponse": ".update_item_modifier_lists_response",
    "UpdateItemTaxesResponse": ".update_item_taxes_response",
    "UpdateLocationResponse": ".update_location_response",
    "UpdateOrderResponse": ".update_order_response",
    "UpdatePaymentResponse": ".update_payment_response",
    "UpdateShiftResponse": ".update_shift_response",
    "UpdateSubscriptionResponse": ".update_subscription_response",
    "UpdateTeamMemberRequest": ".update_team_member_request",
    "UpdateTeamMemberResponse": ".update_team_member_response",
    "UpdateWageSettingResponse": ".update_wage_setting_response",
    "UpdateWorkweekConfigResponse": ".update_workweek_config_response",
    "UpsertCatalogObjectResponse": ".upsert_catalog_object_response",
    "UpsertSnippetResponse": ".upsert_snippet_response",
    "V1CreateEmployeeRoleRequest": ".v1create_employee_role_request",
    "V1CreateRefundRequestType": ".v1create_refund_request_type",
    "V1Employee": ".v1employee",
    "V1EmployeeRole": ".v1employee_role",
    "V1EmployeeRolePermissions": ".v1employee_role_permissions",
    "V1EmployeeStatus": ".v1employee_status",
    "V1ListEmployeeRolesRequest": ".v1list_employee_roles_request",
    "V1ListEmployeeRolesResponse": ".v1list_employee_roles_response",
    "V1ListEmployeesRequest": ".v1list_employees_request",
    "V1ListEmployeesRequestStatus": ".v1list_employees_request_status",
    "V1ListEmployeesResponse": ".v1list_employees_response",
    "V1ListOrdersRequest": ".v1list_orders_request",
    "V1ListOrdersResponse": ".v1list_orders_response",
    "V1ListPaymentsRequest": ".v1list_payments_request",
    "V1ListPaymentsResponse": ".v1list_payments_response",
    "V1ListRefundsRequest": ".v1list_refunds_request",
    "V1ListRefundsResponse": ".v1list_refunds_response",
    "V1ListSettlementsRequest": ".v1list_settlements_request",
    "V1ListSettlementsRequestStatus": ".v1list_settlements_request_status",
    "V1ListSettlementsResponse": ".v1list_settlements_response",
    "V1Money": ".v1money",
    "V1Order": ".v1order",
    "V1OrderHistoryEntry": ".v1order_history_entry",
    "V1OrderHistoryEntryAction": ".v1order_history_entry_action",
    "V1OrderState": ".v1order_state",
    "V1Payment": ".v1payment",
    "V1PaymentDiscount": ".v1payment_discount",
    "V1PaymentItemDetail": ".v1payment_item_detail",
    "V1PaymentItemization": ".v1payment_itemization",
    "V1PaymentItemizationItemizationType": ".v1payment_itemization_itemization_type",
    "V1PaymentModifier": ".v1payment_modifier",
    "V1PaymentSurcharge": ".v1payment_surcharge",
    "V1PaymentSurchargeType": ".v1payment_surcharge_type",
    "V1PaymentTax": ".v1payment_tax",
    "V1PaymentTaxInclusionType": ".v1payment_tax_inclusion_type",
    "V1PhoneNumber": ".v1phone_number",
    "V1Refund": ".v1refund",
    "V1RefundType": ".v1refund_type",
    "V1RetrieveEmployeeRequest": ".v1retrieve_employee_request",
    "V1RetrieveEmployeeRoleRequest": ".v1retrieve_employee_role_request",
    "V1RetrieveOrderRequest": ".v1retrieve_order_request",
    "V1RetrievePaymentRequest": ".v1retrieve_payment_request",
    "V1RetrieveSettlementRequest": ".v1retrieve_settlement_request",
    "V1Settlement": ".v1settlement",
    "V1SettlementEntry": ".v1settlement_entry",
    "V1SettlementEntryType": ".v1settlement_entry_type",
    "V1SettlementStatus": ".v1settlement_status",
    "V1Tender": ".v1tender",
    "V1TenderCardBrand": ".v1tender_card_brand",
    "V1TenderEntryMethod": ".v1tender_entry_method",
    "V1TenderType": ".v1tender_type",
    "V1UpdateEmployeeRequest": ".v1update_employee_request",
    "V1UpdateEmployeeRoleRequest": ".v1update_employee_role_request",
    "V1UpdateOrderRequestAction": ".v1update_order_request_action",
    "VoidTransactionRequest": ".void_transaction_request",
    "VoidTransactionResponse": ".void_transaction_response",
    "WageSetting": ".wage_setting",
    "Weekday": ".weekday",
    "WorkweekConfig": ".workweek_config",
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
    "AcceptDisputeRequest",
    "AcceptDisputeResponse",
    "AccumulateLoyaltyPointsResponse",
    "AchDetails",
    "ActionCancelReason",
    "AddGroupToCustomerRequest",
    "AddGroupToCustomerResponse",
    "AdditionalRecipient",
    "Address",
    "AdjustLoyaltyPointsResponse",
    "AppointmentSegment",
    "Availability",
    "BankAccount",
    "BankAccountPaymentDetails",
    "BankAccountStatus",
    "BankAccountType",
    "BatchChangeInventoryRequest",
    "BatchChangeInventoryResponse",
    "BatchDeleteCatalogObjectsResponse",
    "BatchRetrieveCatalogObjectsResponse",
    "BatchRetrieveInventoryChangesRequest",
    "BatchRetrieveInventoryChangesResponse",
    "BatchRetrieveInventoryCountsRequest",
    "BatchRetrieveInventoryCountsResponse",
    "BatchRetrieveOrdersResponse",
    "BatchUpsertCatalogObjectsResponse",
    "Booking",
    "BookingStatus",
    "Break",
    "BreakType",
    "BulkCreateTeamMembersResponse",
    "BulkUpdateTeamMembersResponse",
    "BusinessAppointmentSettings",
    "BusinessAppointmentSettingsAlignmentTime",
    "BusinessAppointmentSettingsBookingLocationType",
    "BusinessAppointmentSettingsCancellationPolicy",
    "BusinessAppointmentSettingsMaxAppointmentsPerDayLimitType",
    "BusinessBookingProfile",
    "BusinessBookingProfileBookingPolicy",
    "BusinessBookingProfileCustomerTimezoneChoice",
    "BusinessHours",
    "BusinessHoursPeriod",
    "CalculateLoyaltyPointsResponse",
    "CalculateOrderResponse",
    "CancelBookingResponse",
    "CancelInvoiceResponse",
    "CancelPaymentByIdempotencyKeyResponse",
    "CancelPaymentRequest",
    "CancelPaymentResponse",
    "CancelSubscriptionRequest",
    "CancelSubscriptionResponse",
    "CancelTerminalCheckoutRequest",
    "CancelTerminalCheckoutResponse",
    "CancelTerminalRefundRequest",
    "CancelTerminalRefundResponse",
    "CaptureTransactionRequest",
    "CaptureTransactionResponse",
    "Card",
    "CardBrand",
    "CardPaymentDetails",
    "CardPaymentTimeline",
    "CardPrepaidType",
    "CardSquareProduct",
    "CardType",
    "CashDrawerDevice",
    "CashDrawerEventType",
    "CashDrawerShift",
    "CashDrawerShiftEvent",
    "CashDrawerShiftState",
    "CashDrawerShiftSummary",
    "CashPaymentDetails",
    "CatalogCategory",
    "CatalogCustomAttributeDefinition",
    "CatalogCustomAttributeDefinitionAppVisibility",
    "CatalogCustomAttributeDefinitionNumberConfig",
    "CatalogCustomAttributeDefinitionSelectionConfig",
    "CatalogCustomAttributeDefinitionSelectionConfigCustomAttributeSelection",
    "CatalogCustomAttributeDefinitionSellerVisibility",
    "CatalogCustomAttributeDefinitionStringConfig",
    "CatalogCustomAttributeDefinitionType",
    "CatalogCustomAttributeValue",
    "CatalogDiscount",
    "CatalogDiscountModifyTaxBasis",
    "CatalogDiscountType",
    "CatalogIdMapping",
    "CatalogImage",
    "CatalogInfoRequest",
    "CatalogInfoResponse",
    "CatalogInfoResponseLimits",
    "CatalogItem",
    "CatalogItemModifierListInfo",
    "CatalogItemOption",
    "CatalogItemOptionForItem",
    "CatalogItemOptionValue",
    "CatalogItemOptionValueForItemVariation",
    "CatalogItemProductType",
    "CatalogItemVariation",
    "CatalogMeasurementUnit",
    "CatalogModifier",
    "CatalogModifierList",
    "CatalogModifierListSelectionType",
    "CatalogModifierOverride",
    "CatalogObject",
    "CatalogObjectBatch",
    "CatalogObjectReference",
    "CatalogObjectType",
    "CatalogPricingRule",
    "CatalogPricingType",
    "CatalogProductSet",
    "CatalogQuery",
    "CatalogQueryExact",
    "CatalogQueryItemVariationsForItemOptionValues",
    "CatalogQueryItemsForItemOptions",
    "CatalogQueryItemsForModifierList",
    "CatalogQueryItemsForTax",
    "CatalogQueryPrefix",
    "CatalogQueryRange",
    "CatalogQuerySet",
    "CatalogQuerySortedAttribute",
    "CatalogQueryText",
    "CatalogQuickAmount",
    "CatalogQuickAmountType",
    "CatalogQuickAmountsSettings",
    "CatalogQuickAmountsSettingsOption",
    "CatalogStockConversion",
    "CatalogSubscriptionPlan",
    "CatalogTax",
    "CatalogTimePeriod",
    "CatalogV1Id",
    "ChargeRequestAdditionalRecipient",
    "ChargeResponse",
    "CheckAppointmentsOnboardedRequest",
    "Checkout",
    "CheckoutOptionsPaymentType",
    "CompletePaymentRequest",
    "CompletePaymentResponse",
    "Coordinates",
    "Country",
    "CreateBookingResponse",
    "CreateBreakTypeResponse",
    "CreateCardResponse",
    "CreateCheckoutResponse",
    "CreateCustomerCardResponse",
    "CreateCustomerGroupResponse",
    "CreateCustomerResponse",
    "CreateDeviceCodeResponse",
    "CreateDisputeEvidenceTextResponse",
    "CreateGiftCardActivityResponse",
    "CreateGiftCardResponse",
    "CreateInvoiceResponse",
    "CreateLocationResponse",
    "CreateLoyaltyAccountResponse",
    "CreateLoyaltyRewardResponse",
    "CreateMobileAuthorizationCodeResponse",
    "CreateOrderRequest",
    "CreateOrderResponse",
    "CreatePaymentResponse",
    "CreateRefundResponse",
    "CreateShiftResponse",
    "CreateSubscriptionResponse",
    "CreateTeamMemberRequest",
    "CreateTeamMemberResponse",
    "CreateTerminalCheckoutResponse",
    "CreateTerminalRefundResponse",
    "Currency",
    "CustomAttributeFilter",
    "Customer",
    "CustomerCreationSource",
    "CustomerCreationSourceFilter",
    "CustomerFilter",
    "CustomerGroup",
    "CustomerInclusionExclusion",
    "CustomerPreferences",
    "CustomerQuery",
    "CustomerSegment",
    "CustomerSort",
    "CustomerSortField",
    "CustomerTextFilter",
    "DateRange",
    "DayOfWeek",
    "DeleteBreakTypeRequest",
    "DeleteBreakTypeResponse",
    "DeleteCatalogObjectRequest",
    "DeleteCatalogObjectResponse",
    "DeleteCustomerCardRequest",
    "DeleteCustomerCardResponse",
    "DeleteCustomerGroupRequest",
    "DeleteCustomerGroupResponse",
    "DeleteCustomerRequest",
    "DeleteCustomerResponse",
    "DeleteDisputeEvidenceRequest",
    "DeleteDisputeEvidenceResponse",
    "DeleteInvoiceRequest",
    "DeleteInvoiceResponse",
    "DeleteLoyaltyRewardRequest",
    "DeleteLoyaltyRewardResponse",
    "DeleteShiftRequest",
    "DeleteShiftResponse",
    "DeleteSnippetRequest",
    "DeleteSnippetResponse",
    "DeprecatedCreateDisputeEvidenceFileRequest",
    "DeprecatedCreateDisputeEvidenceFileResponse",
    "DeprecatedCreateDisputeEvidenceTextRequest",
    "DeprecatedCreateDisputeEvidenceTextResponse",
    "Device",
    "DeviceCheckoutOptions",
    "DeviceCode",
    "DeviceCodeStatus",
    "DeviceDetails",
    "DigitalWalletDetails",
    "DisableCardRequest",
    "DisableCardResponse",
    "Dispute",
    "DisputeEvidence",
    "DisputeEvidenceCreatedWebhook",
    "DisputeEvidenceCreatedWebhookData",
    "DisputeEvidenceCreatedWebhookObject",
    "DisputeEvidenceFile",
    "DisputeEvidenceType",
    "DisputeReason",
    "DisputeState",
    "DisputedPayment",
    "EcomVisibility",
    "Employee",
    "EmployeeStatus",
    "EmployeeWage",
    "Error",
    "ErrorCategory",
    "ErrorCode",
    "ExcludeStrategy",
    "ExternalPaymentDetails",
    "FilterValue",
    "GanSource",
    "GetBankAccountByV1IdRequest",
    "GetBankAccountByV1IdResponse",
    "GetBankAccountRequest",
    "GetBankAccountResponse",
    "GetBreakTypeRequest",
    "GetBreakTypeResponse",
    "GetDeviceCodeRequest",
    "GetDeviceCodeResponse",
    "GetEmployeeWageRequest",
    "GetEmployeeWageResponse",
    "GetInvoiceRequest",
    "GetInvoiceResponse",
    "GetPaymentRefundRequest",
    "GetPaymentRefundResponse",
    "GetPaymentRequest",
    "GetPaymentResponse",
    "GetShiftRequest",
    "GetShiftResponse",
    "GetTeamMemberWageRequest",
    "GetTeamMemberWageResponse",
    "GetTerminalCheckoutRequest",
    "GetTerminalCheckoutResponse",
    "GetTerminalRefundRequest",
    "GetTerminalRefundResponse",
    "GiftCard",
    "GiftCardActivity",
    "GiftCardActivityActivate",
    "GiftCardActivityAdjustDecrement",
    "GiftCardActivityAdjustDecrementReason",
    "GiftCardActivityAdjustIncrement",
    "GiftCardActivityAdjustIncrementReason",
    "GiftCardActivityBlock",
    "GiftCardActivityBlockReason",
    "GiftCardActivityClearBalance",
    "GiftCardActivityClearBalanceReason",
    "GiftCardActivityDeactivate",
    "GiftCardActivityDeactivateReason",
    "GiftCardActivityImport",
    "GiftCardActivityImportReversal",
    "GiftCardActivityLoad",
    "GiftCardActivityRedeem",
    "GiftCardActivityRefund",
    "GiftCardActivityType",
    "GiftCardActivityUnblock",
    "GiftCardActivityUnblockReason",
    "GiftCardActivityUnlinkedActivityRefund",
    "GiftCardGanSource",
    "GiftCardStatus",
    "GiftCardType",
    "Info",
    "InfoCode",
    "InlineTypes",
    "InventoryAdjustment",
    "InventoryAdjustmentGroup",
    "InventoryAlertType",
    "InventoryChange",
    "InventoryChangeType",
    "InventoryCount",
    "InventoryPhysicalCount",
    "InventoryState",
    "InventoryTransfer",
    "Invoice",
    "InvoiceAcceptedPaymentMethods",
    "InvoiceAutomaticPaymentSource",
    "InvoiceCustomField",
    "InvoiceCustomFieldPlacement",
    "InvoiceDeliveryMethod",
    "InvoiceDeliveryMethodInvoiceDeliveryMethod",
    "InvoiceFilter",
    "InvoicePaymentReminder",
    "InvoicePaymentReminderStatus",
    "InvoicePaymentRequest",
    "InvoiceQuery",
    "InvoiceRecipient",
    "InvoiceRequestMethod",
    "InvoiceRequestType",
    "InvoiceSort",
    "InvoiceSortField",
    "InvoiceStatus",
    "ItemVariationLocationOverrides",
    "JobAssignment",
    "JobAssignmentPayType",
    "LinkCustomerToGiftCardResponse",
    "ListBankAccountsRequest",
    "ListBankAccountsResponse",
    "ListBreakTypesRequest",
    "ListBreakTypesResponse",
    "ListCardsRequest",
    "ListCardsResponse",
    "ListCashDrawerShiftEventsRequest",
    "ListCashDrawerShiftEventsResponse",
    "ListCashDrawerShiftsRequest",
    "ListCashDrawerShiftsResponse",
    "ListCatalogRequest",
    "ListCatalogResponse",
    "ListCustomerGroupsRequest",
    "ListCustomerGroupsResponse",
    "ListCustomerSegmentsRequest",
    "ListCustomerSegmentsResponse",
    "ListCustomersRequest",
    "ListCustomersResponse",
    "ListDeviceCodesRequest",
    "ListDeviceCodesResponse",
    "ListDisputeEvidenceRequest",
    "ListDisputeEvidenceResponse",
    "ListDisputesRequest",
    "ListDisputesResponse",
    "ListEmployeeWagesRequest",
    "ListEmployeeWagesResponse",
    "ListEmployeesRequest",
    "ListEmployeesResponse",
    "ListGiftCardActivitiesRequest",
    "ListGiftCardActivitiesResponse",
    "ListGiftCardsRequest",
    "ListGiftCardsResponse",
    "ListInvoicesRequest",
    "ListInvoicesResponse",
    "ListLocationsRequest",
    "ListLocationsResponse",
    "ListLoyaltyProgramsRequest",
    "ListLoyaltyProgramsResponse",
    "ListMerchantsRequest",
    "ListMerchantsResponse",
    "ListPaymentRefundsRequest",
    "ListPaymentRefundsResponse",
    "ListPaymentsRequest",
    "ListPaymentsResponse",
    "ListRefundsRequest",
    "ListRefundsResponse",
    "ListSitesRequest",
    "ListSitesResponse",
    "ListSubscriptionEventsRequest",
    "ListSubscriptionEventsResponse",
    "ListTeamMemberBookingProfilesRequest",
    "ListTeamMemberBookingProfilesResponse",
    "ListTeamMemberWagesRequest",
    "ListTeamMemberWagesResponse",
    "ListTransactionsRequest",
    "ListTransactionsResponse",
    "ListWorkweekConfigsRequest",
    "ListWorkweekConfigsResponse",
    "Location",
    "LocationCapability",
    "LocationStatus",
    "LocationType",
    "LoyaltyAccount",
    "LoyaltyAccountExpiringPointDeadline",
    "LoyaltyAccountMapping",
    "LoyaltyAccountMappingType",
    "LoyaltyEvent",
    "LoyaltyEventAccumulatePoints",
    "LoyaltyEventAdjustPoints",
    "LoyaltyEventCreateReward",
    "LoyaltyEventDateTimeFilter",
    "LoyaltyEventDeleteReward",
    "LoyaltyEventExpirePoints",
    "LoyaltyEventFilter",
    "LoyaltyEventLocationFilter",
    "LoyaltyEventLoyaltyAccountFilter",
    "LoyaltyEventOrderFilter",
    "LoyaltyEventOther",
    "LoyaltyEventQuery",
    "LoyaltyEventRedeemReward",
    "LoyaltyEventSource",
    "LoyaltyEventType",
    "LoyaltyEventTypeFilter",
    "LoyaltyProgram",
    "LoyaltyProgramAccrualRule",
    "LoyaltyProgramAccrualRuleType",
    "LoyaltyProgramExpirationPolicy",
    "LoyaltyProgramRewardDefinition",
    "LoyaltyProgramRewardDefinitionScope",
    "LoyaltyProgramRewardDefinitionType",
    "LoyaltyProgramRewardTier",
    "LoyaltyProgramStatus",
    "LoyaltyProgramTerminology",
    "LoyaltyReward",
    "LoyaltyRewardStatus",
    "MeasurementUnit",
    "MeasurementUnitArea",
    "MeasurementUnitCustom",
    "MeasurementUnitGeneric",
    "MeasurementUnitLength",
    "MeasurementUnitTime",
    "MeasurementUnitUnitType",
    "MeasurementUnitVolume",
    "MeasurementUnitWeight",
    "Merchant",
    "MerchantStatus",
    "Money",
    "OauthScope",
    "ObtainTokenResponse",
    "OnboardAppointmentsRequest",
    "Order",
    "OrderCreated",
    "OrderCreatedObject",
    "OrderEntry",
    "OrderFulfillment",
    "OrderFulfillmentPickupDetails",
    "OrderFulfillmentPickupDetailsCurbsidePickupDetails",
    "OrderFulfillmentPickupDetailsScheduleType",
    "OrderFulfillmentRecipient",
    "OrderFulfillmentShipmentDetails",
    "OrderFulfillmentState",
    "OrderFulfillmentType",
    "OrderFulfillmentUpdated",
    "OrderFulfillmentUpdatedObject",
    "OrderFulfillmentUpdatedUpdate",
    "OrderLineItem",
    "OrderLineItemAppliedDiscount",
    "OrderLineItemAppliedTax",
    "OrderLineItemDiscount",
    "OrderLineItemDiscountScope",
    "OrderLineItemDiscountType",
    "OrderLineItemItemType",
    "OrderLineItemModifier",
    "OrderLineItemPricingBlocklists",
    "OrderLineItemPricingBlocklistsBlockedDiscount",
    "OrderLineItemPricingBlocklistsBlockedTax",
    "OrderLineItemTax",
    "OrderLineItemTaxScope",
    "OrderLineItemTaxType",
    "OrderMoneyAmounts",
    "OrderPricingOptions",
    "OrderQuantityUnit",
    "OrderReturn",
    "OrderReturnDiscount",
    "OrderReturnLineItem",
    "OrderReturnLineItemModifier",
    "OrderReturnServiceCharge",
    "OrderReturnTax",
    "OrderReward",
    "OrderRoundingAdjustment",
    "OrderServiceCharge",
    "OrderServiceChargeCalculationPhase",
    "OrderServiceChargeType",
    "OrderSource",
    "OrderState",
    "OrderUpdated",
    "OrderUpdatedObject",
    "PayOrderResponse",
    "Payment",
    "PaymentOptions",
    "PaymentRefund",
    "ProcessingFee",
    "Product",
    "ProductType",
    "PublishInvoiceResponse",
    "QuantityRatio",
    "Range",
    "Reason",
    "RedeemLoyaltyRewardResponse",
    "Refund",
    "RefundPaymentResponse",
    "RefundStatus",
    "RegisterDomainResponse",
    "RegisterDomainResponseStatus",
    "RemoveGroupFromCustomerRequest",
    "RemoveGroupFromCustomerResponse",
    "RenewTokenResponse",
    "ResumeSubscriptionRequest",
    "ResumeSubscriptionResponse",
    "RetrieveBookingRequest",
    "RetrieveBookingResponse",
    "RetrieveBusinessBookingProfileRequest",
    "RetrieveBusinessBookingProfileResponse",
    "RetrieveCardRequest",
    "RetrieveCardResponse",
    "RetrieveCashDrawerShiftRequest",
    "RetrieveCashDrawerShiftResponse",
    "RetrieveCatalogObjectRequest",
    "RetrieveCatalogObjectResponse",
    "RetrieveCustomerGroupRequest",
    "RetrieveCustomerGroupResponse",
    "RetrieveCustomerRequest",
    "RetrieveCustomerResponse",
    "RetrieveCustomerSegmentRequest",
    "RetrieveCustomerSegmentResponse",
    "RetrieveDisputeEvidenceRequest",
    "RetrieveDisputeEvidenceResponse",
    "RetrieveDisputeRequest",
    "RetrieveDisputeResponse",
    "RetrieveEmployeeRequest",
    "RetrieveEmployeeResponse",
    "RetrieveGiftCardFromGanResponse",
    "RetrieveGiftCardFromNonceResponse",
    "RetrieveGiftCardRequest",
    "RetrieveGiftCardResponse",
    "RetrieveInventoryAdjustmentRequest",
    "RetrieveInventoryAdjustmentResponse",
    "RetrieveInventoryChangesRequest",
    "RetrieveInventoryChangesResponse",
    "RetrieveInventoryCountRequest",
    "RetrieveInventoryCountResponse",
    "RetrieveInventoryPhysicalCountRequest",
    "RetrieveInventoryPhysicalCountResponse",
    "RetrieveInventoryTransferRequest",
    "RetrieveInventoryTransferResponse",
    "RetrieveLocationRequest",
    "RetrieveLocationResponse",
    "RetrieveLoyaltyAccountRequest",
    "RetrieveLoyaltyAccountResponse",
    "RetrieveLoyaltyProgramRequest",
    "RetrieveLoyaltyProgramResponse",
    "RetrieveLoyaltyRewardRequest",
    "RetrieveLoyaltyRewardResponse",
    "RetrieveMerchantRequest",
    "RetrieveMerchantResponse",
    "RetrieveObsMigrationProfileRequest",
    "RetrieveOrderRequest",
    "RetrieveOrderResponse",
    "RetrieveSnippetRequest",
    "RetrieveSnippetResponse",
    "RetrieveSubscriptionRequest",
    "RetrieveSubscriptionResponse",
    "RetrieveTeamMemberBookingProfileRequest",
    "RetrieveTeamMemberBookingProfileResponse",
    "RetrieveTeamMemberRequest",
    "RetrieveTeamMemberResponse",
    "RetrieveTransactionRequest",
    "RetrieveTransactionResponse",
    "RetrieveWageSettingRequest",
    "RetrieveWageSettingResponse",
    "RevokeTokenResponse",
    "RiskEvaluation",
    "RiskEvaluationRiskLevel",
    "SearchAvailabilityFilter",
    "SearchAvailabilityQuery",
    "SearchAvailabilityResponse",
    "SearchCatalogItemsRequestStockLevel",
    "SearchCatalogItemsResponse",
    "SearchCatalogObjectsResponse",
    "SearchCustomersResponse",
    "SearchInvoicesResponse",
    "SearchLoyaltyAccountsRequestLoyaltyAccountQuery",
    "SearchLoyaltyAccountsResponse",
    "SearchLoyaltyEventsResponse",
    "SearchLoyaltyRewardsRequestLoyaltyRewardQuery",
    "SearchLoyaltyRewardsResponse",
    "SearchOrdersCustomerFilter",
    "SearchOrdersDateTimeFilter",
    "SearchOrdersFilter",
    "SearchOrdersFulfillmentFilter",
    "SearchOrdersQuery",
    "SearchOrdersResponse",
    "SearchOrdersSort",
    "SearchOrdersSortField",
    "SearchOrdersSourceFilter",
    "SearchOrdersStateFilter",
    "SearchShiftsResponse",
    "SearchSubscriptionsFilter",
    "SearchSubscriptionsQuery",
    "SearchSubscriptionsResponse",
    "SearchTeamMembersFilter",
    "SearchTeamMembersQuery",
    "SearchTeamMembersResponse",
    "SearchTerminalCheckoutsResponse",
    "SearchTerminalRefundsResponse",
    "SegmentFilter",
    "Shift",
    "ShiftFilter",
    "ShiftFilterStatus",
    "ShiftQuery",
    "ShiftSort",
    "ShiftSortField",
    "ShiftStatus",
    "ShiftWage",
    "ShiftWorkday",
    "ShiftWorkdayMatcher",
    "Site",
    "Snippet",
    "SnippetResponse",
    "SortOrder",
    "SourceApplication",
    "StandardUnitDescription",
    "StandardUnitDescriptionGroup",
    "Status",
    "SubmitEvidenceRequest",
    "SubmitEvidenceResponse",
    "Subscription",
    "SubscriptionCadence",
    "SubscriptionEvent",
    "SubscriptionEventInfo",
    "SubscriptionEventInfoCode",
    "SubscriptionEventSubscriptionEventType",
    "SubscriptionPhase",
    "SubscriptionStatus",
    "TaxCalculationPhase",
    "TaxIds",
    "TaxInclusionType",
    "TeamMember",
    "TeamMemberAssignedLocations",
    "TeamMemberAssignedLocationsAssignmentType",
    "TeamMemberBookingProfile",
    "TeamMemberInvitationStatus",
    "TeamMemberStatus",
    "TeamMemberWage",
    "Tender",
    "TenderCardDetails",
    "TenderCardDetailsEntryMethod",
    "TenderCardDetailsStatus",
    "TenderCashDetails",
    "TenderType",
    "TerminalCheckout",
    "TerminalCheckoutQuery",
    "TerminalCheckoutQueryFilter",
    "TerminalCheckoutQuerySort",
    "TerminalRefund",
    "TerminalRefundQuery",
    "TerminalRefundQueryFilter",
    "TerminalRefundQuerySort",
    "TimeRange",
    "TipSettings",
    "Transaction",
    "TransactionProduct",
    "TransactionType",
    "Type",
    "UnlinkCustomerFromGiftCardResponse",
    "UpdateBookingResponse",
    "UpdateBreakTypeResponse",
    "UpdateCustomerGroupResponse",
    "UpdateCustomerResponse",
    "UpdateInvoiceResponse",
    "UpdateItemModifierListsResponse",
    "UpdateItemTaxesResponse",
    "UpdateLocationResponse",
    "UpdateOrderResponse",
    "UpdatePaymentResponse",
    "UpdateShiftResponse",
    "UpdateSubscriptionResponse",
    "UpdateTeamMemberRequest",
    "UpdateTeamMemberResponse",
    "UpdateWageSettingResponse",
    "UpdateWorkweekConfigResponse",
    "UpsertCatalogObjectResponse",
    "UpsertSnippetResponse",
    "V1CreateEmployeeRoleRequest",
    "V1CreateRefundRequestType",
    "V1Employee",
    "V1EmployeeRole",
    "V1EmployeeRolePermissions",
    "V1EmployeeStatus",
    "V1ListEmployeeRolesRequest",
    "V1ListEmployeeRolesResponse",
    "V1ListEmployeesRequest",
    "V1ListEmployeesRequestStatus",
    "V1ListEmployeesResponse",
    "V1ListOrdersRequest",
    "V1ListOrdersResponse",
    "V1ListPaymentsRequest",
    "V1ListPaymentsResponse",
    "V1ListRefundsRequest",
    "V1ListRefundsResponse",
    "V1ListSettlementsRequest",
    "V1ListSettlementsRequestStatus",
    "V1ListSettlementsResponse",
    "V1Money",
    "V1Order",
    "V1OrderHistoryEntry",
    "V1OrderHistoryEntryAction",
    "V1OrderState",
    "V1Payment",
    "V1PaymentDiscount",
    "V1PaymentItemDetail",
    "V1PaymentItemization",
    "V1PaymentItemizationItemizationType",
    "V1PaymentModifier",
    "V1PaymentSurcharge",
    "V1PaymentSurchargeType",
    "V1PaymentTax",
    "V1PaymentTaxInclusionType",
    "V1PhoneNumber",
    "V1Refund",
    "V1RefundType",
    "V1RetrieveEmployeeRequest",
    "V1RetrieveEmployeeRoleRequest",
    "V1RetrieveOrderRequest",
    "V1RetrievePaymentRequest",
    "V1RetrieveSettlementRequest",
    "V1Settlement",
    "V1SettlementEntry",
    "V1SettlementEntryType",
    "V1SettlementStatus",
    "V1Tender",
    "V1TenderCardBrand",
    "V1TenderEntryMethod",
    "V1TenderType",
    "V1UpdateEmployeeRequest",
    "V1UpdateEmployeeRoleRequest",
    "V1UpdateOrderRequestAction",
    "VoidTransactionRequest",
    "VoidTransactionResponse",
    "WageSetting",
    "Weekday",
    "WorkweekConfig",
]
