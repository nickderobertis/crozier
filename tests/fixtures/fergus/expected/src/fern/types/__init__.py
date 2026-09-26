



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .accept_quote_data import AcceptQuoteData
    from .accept_quote_response import AcceptQuoteResponse
    from .accept_quote_response_data import AcceptQuoteResponseData
    from .add_quote_payload import AddQuotePayload
    from .add_quote_payload_sections_item import AddQuotePayloadSectionsItem
    from .add_quote_payload_sections_item_favourite_section_id import AddQuotePayloadSectionsItemFavouriteSectionId
    from .add_quote_payload_sections_item_favourite_section_id_combined import (
        AddQuotePayloadSectionsItemFavouriteSectionIdCombined,
    )
    from .add_quote_payload_sections_item_favourite_section_ids import AddQuotePayloadSectionsItemFavouriteSectionIds
    from .add_quote_payload_sections_item_favourite_section_ids_one_item import (
        AddQuotePayloadSectionsItemFavouriteSectionIdsOneItem,
    )
    from .add_quote_payload_sections_item_line_items_item import AddQuotePayloadSectionsItemLineItemsItem
    from .add_quote_response import AddQuoteResponse
    from .add_quote_response_data import AddQuoteResponseData
    from .add_quote_response_data_deposit import AddQuoteResponseDataDeposit
    from .add_quote_response_data_deposit_option_type import AddQuoteResponseDataDepositOptionType
    from .add_quote_response_data_deposit_option_type_one import AddQuoteResponseDataDepositOptionTypeOne
    from .add_quote_response_data_deposit_option_type_zero import AddQuoteResponseDataDepositOptionTypeZero
    from .add_quote_response_data_links_item import AddQuoteResponseDataLinksItem
    from .add_quote_response_data_links_item_type import AddQuoteResponseDataLinksItemType
    from .add_quote_response_data_sections_item import AddQuoteResponseDataSectionsItem
    from .add_quote_response_data_sections_item_line_items_item import AddQuoteResponseDataSectionsItemLineItemsItem
    from .add_quote_response_data_sections_item_section_config import AddQuoteResponseDataSectionsItemSectionConfig
    from .add_quote_response_data_sections_item_selection_mode import AddQuoteResponseDataSectionsItemSelectionMode
    from .address_contact import AddressContact
    from .address_payload import AddressPayload
    from .calendar_event import CalendarEvent
    from .calendar_event_by_id_response import CalendarEventByIdResponse
    from .calendar_event_event_type import CalendarEventEventType
    from .calendar_events_response import CalendarEventsResponse
    from .charge_up_job_financial_summary import ChargeUpJobFinancialSummary
    from .charge_up_job_financial_summary_chargeable_amount import ChargeUpJobFinancialSummaryChargeableAmount
    from .charge_up_job_financial_summary_costs_incurred import ChargeUpJobFinancialSummaryCostsIncurred
    from .charge_up_job_financial_summary_labour_hours import ChargeUpJobFinancialSummaryLabourHours
    from .charge_up_job_financial_summary_total_billed import ChargeUpJobFinancialSummaryTotalBilled
    from .company import Company
    from .company_contact import CompanyContact
    from .company_contact_contact_items_item import CompanyContactContactItemsItem
    from .company_contact_item import CompanyContactItem
    from .company_setting import CompanySetting
    from .company_settings_item import CompanySettingsItem
    from .company_tax import CompanyTax
    from .contact import Contact
    from .contact_by_id_response import ContactByIdResponse
    from .contact_contact_type import ContactContactType
    from .contact_item import ContactItem
    from .contact_item_contact_type import ContactItemContactType
    from .contact_item_payload import ContactItemPayload
    from .contact_item_payload_contact_type import ContactItemPayloadContactType
    from .contacts_query_parameters import ContactsQueryParameters
    from .contacts_query_parameters_filter_contact_type import ContactsQueryParametersFilterContactType
    from .contacts_query_parameters_sort_field import ContactsQueryParametersSortField
    from .contacts_query_parameters_sort_order import ContactsQueryParametersSortOrder
    from .contacts_response import ContactsResponse
    from .create_draft_job import CreateDraftJob
    from .create_draft_job_job_type import CreateDraftJobJobType
    from .create_enquiry_payload import CreateEnquiryPayload
    from .create_job_phase import CreateJobPhase
    from .create_non_draft_job import CreateNonDraftJob
    from .create_non_draft_job_job_type import CreateNonDraftJobJobType
    from .create_stock_on_hand_item import CreateStockOnHandItem
    from .create_stock_on_hand_item_item_cost import CreateStockOnHandItemItemCost
    from .create_stock_on_hand_item_price_book_line_item_id import CreateStockOnHandItemPriceBookLineItemId
    from .customer import Customer
    from .customer_invoice import CustomerInvoice
    from .customer_invoice_due_days import CustomerInvoiceDueDays
    from .customer_invoice_status import CustomerInvoiceStatus
    from .customer_invoice_status_five import CustomerInvoiceStatusFive
    from .customer_invoice_status_four import CustomerInvoiceStatusFour
    from .customer_invoice_status_one import CustomerInvoiceStatusOne
    from .customer_invoice_status_three import CustomerInvoiceStatusThree
    from .customer_invoice_status_two import CustomerInvoiceStatusTwo
    from .customer_invoice_status_zero import CustomerInvoiceStatusZero
    from .customer_invoice_type import CustomerInvoiceType
    from .customer_invoice_type_one import CustomerInvoiceTypeOne
    from .customer_invoice_type_two import CustomerInvoiceTypeTwo
    from .customer_invoice_type_zero import CustomerInvoiceTypeZero
    from .detailed_customer_invoice import DetailedCustomerInvoice
    from .detailed_customer_invoice_customer import DetailedCustomerInvoiceCustomer
    from .detailed_customer_invoice_due_days import DetailedCustomerInvoiceDueDays
    from .detailed_customer_invoice_sections_item import DetailedCustomerInvoiceSectionsItem
    from .detailed_customer_invoice_sections_item_line_items_item import (
        DetailedCustomerInvoiceSectionsItemLineItemsItem,
    )
    from .detailed_customer_invoice_status import DetailedCustomerInvoiceStatus
    from .detailed_customer_invoice_status_five import DetailedCustomerInvoiceStatusFive
    from .detailed_customer_invoice_status_four import DetailedCustomerInvoiceStatusFour
    from .detailed_customer_invoice_status_one import DetailedCustomerInvoiceStatusOne
    from .detailed_customer_invoice_status_three import DetailedCustomerInvoiceStatusThree
    from .detailed_customer_invoice_status_two import DetailedCustomerInvoiceStatusTwo
    from .detailed_customer_invoice_status_zero import DetailedCustomerInvoiceStatusZero
    from .detailed_customer_invoice_type import DetailedCustomerInvoiceType
    from .detailed_customer_invoice_type_one import DetailedCustomerInvoiceTypeOne
    from .detailed_customer_invoice_type_two import DetailedCustomerInvoiceTypeTwo
    from .detailed_customer_invoice_type_zero import DetailedCustomerInvoiceTypeZero
    from .enquiries_response import EnquiriesResponse
    from .enquiry import Enquiry
    from .enquiry_by_id_response import EnquiryByIdResponse
    from .enquiry_created_response import EnquiryCreatedResponse
    from .enquiry_with_job_ids import EnquiryWithJobIds
    from .error_response import ErrorResponse
    from .favourites_folder import FavouritesFolder
    from .favourites_folder_sections_item import FavouritesFolderSectionsItem
    from .favourites_query_parameters import FavouritesQueryParameters
    from .favourites_query_parameters_representation import FavouritesQueryParametersRepresentation
    from .favourites_query_parameters_sort_field import FavouritesQueryParametersSortField
    from .favourites_query_parameters_sort_order import FavouritesQueryParametersSortOrder
    from .favourites_response import FavouritesResponse
    from .favourites_response_data import FavouritesResponseData
    from .favourites_response_data_children import FavouritesResponseDataChildren
    from .favourites_response_data_children_sections_item import FavouritesResponseDataChildrenSectionsItem
    from .favourites_response_data_description import FavouritesResponseDataDescription
    from .favourites_section import FavouritesSection
    from .favourites_section_line_items_item import FavouritesSectionLineItemsItem
    from .favourites_section_path import FavouritesSectionPath
    from .favourites_section_path_item import FavouritesSectionPathItem
    from .get_company_response import GetCompanyResponse
    from .get_customer_by_id_response import GetCustomerByIdResponse
    from .get_customer_invoice_by_id_response import GetCustomerInvoiceByIdResponse
    from .get_customers_response import GetCustomersResponse
    from .get_notes_response import GetNotesResponse
    from .get_price_book_by_id_response import GetPriceBookByIdResponse
    from .get_pricebook_item_by_id_response import GetPricebookItemByIdResponse
    from .get_pricebook_items_response import GetPricebookItemsResponse
    from .get_pricebooks_response import GetPricebooksResponse
    from .get_pricing_tier_by_id_response import GetPricingTierByIdResponse
    from .get_pricing_tiers_response import GetPricingTiersResponse
    from .get_quote_by_id_quote_response import GetQuoteByIdQuoteResponse
    from .get_quote_by_id_quote_response_data import GetQuoteByIdQuoteResponseData
    from .get_quote_by_id_quote_response_data_deposit import GetQuoteByIdQuoteResponseDataDeposit
    from .get_quote_by_id_quote_response_data_deposit_option_type import GetQuoteByIdQuoteResponseDataDepositOptionType
    from .get_quote_by_id_quote_response_data_deposit_option_type_one import (
        GetQuoteByIdQuoteResponseDataDepositOptionTypeOne,
    )
    from .get_quote_by_id_quote_response_data_deposit_option_type_zero import (
        GetQuoteByIdQuoteResponseDataDepositOptionTypeZero,
    )
    from .get_quote_by_id_quote_response_data_links_item import GetQuoteByIdQuoteResponseDataLinksItem
    from .get_quote_by_id_quote_response_data_links_item_type import GetQuoteByIdQuoteResponseDataLinksItemType
    from .get_quote_by_id_quote_response_data_sections_item import GetQuoteByIdQuoteResponseDataSectionsItem
    from .get_quote_by_id_quote_response_data_sections_item_line_items_item import (
        GetQuoteByIdQuoteResponseDataSectionsItemLineItemsItem,
    )
    from .get_quote_by_id_quote_response_data_sections_item_section_config import (
        GetQuoteByIdQuoteResponseDataSectionsItemSectionConfig,
    )
    from .get_quote_by_id_quote_response_data_sections_item_selection_mode import (
        GetQuoteByIdQuoteResponseDataSectionsItemSelectionMode,
    )
    from .get_quotes_response import GetQuotesResponse
    from .get_standalone_quotes_response import GetStandaloneQuotesResponse
    from .headers import Headers
    from .invoice_section import InvoiceSection
    from .invoice_section_line_items_item import InvoiceSectionLineItemsItem
    from .invoices_query_parameters import InvoicesQueryParameters
    from .invoices_query_parameters_sort_field import InvoicesQueryParametersSortField
    from .invoices_query_parameters_sort_order import InvoicesQueryParametersSortOrder
    from .job import Job
    from .job_active_quote import JobActiveQuote
    from .job_customer import JobCustomer
    from .job_financial_summary import JobFinancialSummary
    from .job_financial_summary_one import JobFinancialSummaryOne
    from .job_financial_summary_one_chargeable_amount import JobFinancialSummaryOneChargeableAmount
    from .job_financial_summary_one_costs_incurred import JobFinancialSummaryOneCostsIncurred
    from .job_financial_summary_one_job_type import JobFinancialSummaryOneJobType
    from .job_financial_summary_one_labour_hours import JobFinancialSummaryOneLabourHours
    from .job_financial_summary_one_total_billed import JobFinancialSummaryOneTotalBilled
    from .job_financial_summary_quote_summary import JobFinancialSummaryQuoteSummary
    from .job_financial_summary_quote_summary_chargeable_amount import JobFinancialSummaryQuoteSummaryChargeableAmount
    from .job_financial_summary_quote_summary_costs_incurred import JobFinancialSummaryQuoteSummaryCostsIncurred
    from .job_financial_summary_quote_summary_job_type import JobFinancialSummaryQuoteSummaryJobType
    from .job_financial_summary_quote_summary_job_type_one import JobFinancialSummaryQuoteSummaryJobTypeOne
    from .job_financial_summary_quote_summary_job_type_zero import JobFinancialSummaryQuoteSummaryJobTypeZero
    from .job_financial_summary_quote_summary_labour_hours import JobFinancialSummaryQuoteSummaryLabourHours
    from .job_financial_summary_quote_summary_quote_summary import JobFinancialSummaryQuoteSummaryQuoteSummary
    from .job_financial_summary_quote_summary_total_billed import JobFinancialSummaryQuoteSummaryTotalBilled
    from .job_financial_summary_response import JobFinancialSummaryResponse
    from .job_main_contact import JobMainContact
    from .job_parameter import JobParameter
    from .job_phase import JobPhase
    from .job_phase_parameter import JobPhaseParameter
    from .job_phase_response import JobPhaseResponse
    from .job_phases_response import JobPhasesResponse
    from .job_response import JobResponse
    from .job_site_address import JobSiteAddress
    from .jobs_query_parameters import JobsQueryParameters
    from .jobs_query_parameters_filter_job_status import JobsQueryParametersFilterJobStatus
    from .jobs_query_parameters_filter_job_type import JobsQueryParametersFilterJobType
    from .jobs_query_parameters_sort_field import JobsQueryParametersSortField
    from .jobs_query_parameters_sort_order import JobsQueryParametersSortOrder
    from .jobs_response import JobsResponse
    from .links import Links
    from .links_type import LinksType
    from .list_customer_invoices_response import ListCustomerInvoicesResponse
    from .note import Note
    from .note_entity_name import NoteEntityName
    from .note_entity_name_five import NoteEntityNameFive
    from .note_entity_name_four import NoteEntityNameFour
    from .note_entity_name_one import NoteEntityNameOne
    from .note_entity_name_seven import NoteEntityNameSeven
    from .note_entity_name_six import NoteEntityNameSix
    from .note_entity_name_three import NoteEntityNameThree
    from .note_entity_name_two import NoteEntityNameTwo
    from .note_entity_name_zero import NoteEntityNameZero
    from .note_reply import NoteReply
    from .note_reply_entity_name import NoteReplyEntityName
    from .note_reply_entity_name_five import NoteReplyEntityNameFive
    from .note_reply_entity_name_four import NoteReplyEntityNameFour
    from .note_reply_entity_name_one import NoteReplyEntityNameOne
    from .note_reply_entity_name_seven import NoteReplyEntityNameSeven
    from .note_reply_entity_name_six import NoteReplyEntityNameSix
    from .note_reply_entity_name_three import NoteReplyEntityNameThree
    from .note_reply_entity_name_two import NoteReplyEntityNameTwo
    from .note_reply_entity_name_zero import NoteReplyEntityNameZero
    from .pagination import Pagination
    from .pagination_links import PaginationLinks
    from .person_contact import PersonContact
    from .person_payload import PersonPayload
    from .pricebook import Pricebook
    from .pricebook_item import PricebookItem
    from .pricebook_item_pricing_tier import PricebookItemPricingTier
    from .pricebook_search_item import PricebookSearchItem
    from .pricebook_type import PricebookType
    from .pricebook_type_one import PricebookTypeOne
    from .pricebook_type_two import PricebookTypeTwo
    from .pricebook_type_zero import PricebookTypeZero
    from .pricing_tier import PricingTier
    from .quote import Quote
    from .quote_config import QuoteConfig
    from .quote_deposit import QuoteDeposit
    from .quote_deposit_option_type import QuoteDepositOptionType
    from .quote_deposit_option_type_one import QuoteDepositOptionTypeOne
    from .quote_deposit_option_type_zero import QuoteDepositOptionTypeZero
    from .quote_job_financial_summary import QuoteJobFinancialSummary
    from .quote_links_item import QuoteLinksItem
    from .quote_links_item_type import QuoteLinksItemType
    from .quote_parameters import QuoteParameters
    from .quote_section import QuoteSection
    from .quote_section_line_items_item import QuoteSectionLineItemsItem
    from .quote_section_section_config import QuoteSectionSectionConfig
    from .quote_section_selection_mode import QuoteSectionSelectionMode
    from .quote_sections_item import QuoteSectionsItem
    from .quote_sections_item_line_items_item import QuoteSectionsItemLineItemsItem
    from .quote_sections_item_section_config import QuoteSectionsItemSectionConfig
    from .quote_sections_item_selection_mode import QuoteSectionsItemSelectionMode
    from .quote_totals import QuoteTotals
    from .quote_totals_quote_total import QuoteTotalsQuoteTotal
    from .quote_totals_response import QuoteTotalsResponse
    from .quote_totals_section_totals_item import QuoteTotalsSectionTotalsItem
    from .recurring_event_details import RecurringEventDetails
    from .redirect_response import RedirectResponse
    from .search_pricebooks_response import SearchPricebooksResponse
    from .section_config import SectionConfig
    from .site import Site
    from .site_by_id_response import SiteByIdResponse
    from .sites_response import SitesResponse
    from .standalone_quotes_specific_query_parameters import StandaloneQuotesSpecificQueryParameters
    from .standalone_quotes_specific_query_parameters_filter_status import (
        StandaloneQuotesSpecificQueryParametersFilterStatus,
    )
    from .standalone_quotes_specific_query_parameters_sort_field import StandaloneQuotesSpecificQueryParametersSortField
    from .stock_on_hand_item import StockOnHandItem
    from .stock_on_hand_list_response import StockOnHandListResponse
    from .stock_on_hand_query_parameters import StockOnHandQueryParameters
    from .stock_on_hand_query_parameters_sort_field import StockOnHandQueryParametersSortField
    from .stock_on_hand_query_parameters_sort_order import StockOnHandQueryParametersSortOrder
    from .stock_on_hand_response import StockOnHandResponse
    from .stock_used_item import StockUsedItem
    from .stock_used_list_response import StockUsedListResponse
    from .stock_used_query_parameters import StockUsedQueryParameters
    from .time_entries_response import TimeEntriesResponse
    from .time_entry import TimeEntry
    from .update_quote_payload import UpdateQuotePayload
    from .update_quote_payload_sections_item import UpdateQuotePayloadSectionsItem
    from .update_quote_payload_sections_item_favourite_section_id import (
        UpdateQuotePayloadSectionsItemFavouriteSectionId,
    )
    from .update_quote_payload_sections_item_favourite_section_id_combined import (
        UpdateQuotePayloadSectionsItemFavouriteSectionIdCombined,
    )
    from .update_quote_payload_sections_item_favourite_section_ids import (
        UpdateQuotePayloadSectionsItemFavouriteSectionIds,
    )
    from .update_quote_payload_sections_item_favourite_section_ids_one_item import (
        UpdateQuotePayloadSectionsItemFavouriteSectionIdsOneItem,
    )
    from .update_quote_payload_sections_item_line_items_item import UpdateQuotePayloadSectionsItemLineItemsItem
    from .update_quote_response import UpdateQuoteResponse
    from .update_quote_response_data import UpdateQuoteResponseData
    from .update_quote_response_data_deposit import UpdateQuoteResponseDataDeposit
    from .update_quote_response_data_deposit_option_type import UpdateQuoteResponseDataDepositOptionType
    from .update_quote_response_data_deposit_option_type_one import UpdateQuoteResponseDataDepositOptionTypeOne
    from .update_quote_response_data_deposit_option_type_zero import UpdateQuoteResponseDataDepositOptionTypeZero
    from .update_quote_response_data_line_items_item import UpdateQuoteResponseDataLineItemsItem
    from .update_quote_response_data_links_item import UpdateQuoteResponseDataLinksItem
    from .update_quote_response_data_links_item_type import UpdateQuoteResponseDataLinksItemType
    from .update_quote_response_data_sections_item import UpdateQuoteResponseDataSectionsItem
    from .update_quote_response_data_sections_item_line_items_item import (
        UpdateQuoteResponseDataSectionsItemLineItemsItem,
    )
    from .update_quote_response_data_sections_item_section_config import (
        UpdateQuoteResponseDataSectionsItemSectionConfig,
    )
    from .update_quote_response_data_sections_item_selection_mode import (
        UpdateQuoteResponseDataSectionsItemSelectionMode,
    )
    from .update_stock_on_hand_item import UpdateStockOnHandItem
    from .upsert_quote_section import UpsertQuoteSection
    from .upsert_quote_section_favourite_section_id import UpsertQuoteSectionFavouriteSectionId
    from .upsert_quote_section_favourite_section_id_combined import UpsertQuoteSectionFavouriteSectionIdCombined
    from .upsert_quote_section_favourite_section_ids import UpsertQuoteSectionFavouriteSectionIds
    from .upsert_quote_section_favourite_section_ids_one_item import UpsertQuoteSectionFavouriteSectionIdsOneItem
    from .upsert_quote_section_line_items_item import UpsertQuoteSectionLineItemsItem
    from .user import User
    from .user_by_id_response import UserByIdResponse
    from .user_status import UserStatus
    from .user_user_type import UserUserType
    from .users_response import UsersResponse
    from .users_response_data_item import UsersResponseDataItem
    from .users_response_data_item_status import UsersResponseDataItemStatus
    from .users_response_data_item_user_type import UsersResponseDataItemUserType
_dynamic_imports: typing.Dict[str, str] = {
    "AcceptQuoteData": ".accept_quote_data",
    "AcceptQuoteResponse": ".accept_quote_response",
    "AcceptQuoteResponseData": ".accept_quote_response_data",
    "AddQuotePayload": ".add_quote_payload",
    "AddQuotePayloadSectionsItem": ".add_quote_payload_sections_item",
    "AddQuotePayloadSectionsItemFavouriteSectionId": ".add_quote_payload_sections_item_favourite_section_id",
    "AddQuotePayloadSectionsItemFavouriteSectionIdCombined": ".add_quote_payload_sections_item_favourite_section_id_combined",
    "AddQuotePayloadSectionsItemFavouriteSectionIds": ".add_quote_payload_sections_item_favourite_section_ids",
    "AddQuotePayloadSectionsItemFavouriteSectionIdsOneItem": ".add_quote_payload_sections_item_favourite_section_ids_one_item",
    "AddQuotePayloadSectionsItemLineItemsItem": ".add_quote_payload_sections_item_line_items_item",
    "AddQuoteResponse": ".add_quote_response",
    "AddQuoteResponseData": ".add_quote_response_data",
    "AddQuoteResponseDataDeposit": ".add_quote_response_data_deposit",
    "AddQuoteResponseDataDepositOptionType": ".add_quote_response_data_deposit_option_type",
    "AddQuoteResponseDataDepositOptionTypeOne": ".add_quote_response_data_deposit_option_type_one",
    "AddQuoteResponseDataDepositOptionTypeZero": ".add_quote_response_data_deposit_option_type_zero",
    "AddQuoteResponseDataLinksItem": ".add_quote_response_data_links_item",
    "AddQuoteResponseDataLinksItemType": ".add_quote_response_data_links_item_type",
    "AddQuoteResponseDataSectionsItem": ".add_quote_response_data_sections_item",
    "AddQuoteResponseDataSectionsItemLineItemsItem": ".add_quote_response_data_sections_item_line_items_item",
    "AddQuoteResponseDataSectionsItemSectionConfig": ".add_quote_response_data_sections_item_section_config",
    "AddQuoteResponseDataSectionsItemSelectionMode": ".add_quote_response_data_sections_item_selection_mode",
    "AddressContact": ".address_contact",
    "AddressPayload": ".address_payload",
    "CalendarEvent": ".calendar_event",
    "CalendarEventByIdResponse": ".calendar_event_by_id_response",
    "CalendarEventEventType": ".calendar_event_event_type",
    "CalendarEventsResponse": ".calendar_events_response",
    "ChargeUpJobFinancialSummary": ".charge_up_job_financial_summary",
    "ChargeUpJobFinancialSummaryChargeableAmount": ".charge_up_job_financial_summary_chargeable_amount",
    "ChargeUpJobFinancialSummaryCostsIncurred": ".charge_up_job_financial_summary_costs_incurred",
    "ChargeUpJobFinancialSummaryLabourHours": ".charge_up_job_financial_summary_labour_hours",
    "ChargeUpJobFinancialSummaryTotalBilled": ".charge_up_job_financial_summary_total_billed",
    "Company": ".company",
    "CompanyContact": ".company_contact",
    "CompanyContactContactItemsItem": ".company_contact_contact_items_item",
    "CompanyContactItem": ".company_contact_item",
    "CompanySetting": ".company_setting",
    "CompanySettingsItem": ".company_settings_item",
    "CompanyTax": ".company_tax",
    "Contact": ".contact",
    "ContactByIdResponse": ".contact_by_id_response",
    "ContactContactType": ".contact_contact_type",
    "ContactItem": ".contact_item",
    "ContactItemContactType": ".contact_item_contact_type",
    "ContactItemPayload": ".contact_item_payload",
    "ContactItemPayloadContactType": ".contact_item_payload_contact_type",
    "ContactsQueryParameters": ".contacts_query_parameters",
    "ContactsQueryParametersFilterContactType": ".contacts_query_parameters_filter_contact_type",
    "ContactsQueryParametersSortField": ".contacts_query_parameters_sort_field",
    "ContactsQueryParametersSortOrder": ".contacts_query_parameters_sort_order",
    "ContactsResponse": ".contacts_response",
    "CreateDraftJob": ".create_draft_job",
    "CreateDraftJobJobType": ".create_draft_job_job_type",
    "CreateEnquiryPayload": ".create_enquiry_payload",
    "CreateJobPhase": ".create_job_phase",
    "CreateNonDraftJob": ".create_non_draft_job",
    "CreateNonDraftJobJobType": ".create_non_draft_job_job_type",
    "CreateStockOnHandItem": ".create_stock_on_hand_item",
    "CreateStockOnHandItemItemCost": ".create_stock_on_hand_item_item_cost",
    "CreateStockOnHandItemPriceBookLineItemId": ".create_stock_on_hand_item_price_book_line_item_id",
    "Customer": ".customer",
    "CustomerInvoice": ".customer_invoice",
    "CustomerInvoiceDueDays": ".customer_invoice_due_days",
    "CustomerInvoiceStatus": ".customer_invoice_status",
    "CustomerInvoiceStatusFive": ".customer_invoice_status_five",
    "CustomerInvoiceStatusFour": ".customer_invoice_status_four",
    "CustomerInvoiceStatusOne": ".customer_invoice_status_one",
    "CustomerInvoiceStatusThree": ".customer_invoice_status_three",
    "CustomerInvoiceStatusTwo": ".customer_invoice_status_two",
    "CustomerInvoiceStatusZero": ".customer_invoice_status_zero",
    "CustomerInvoiceType": ".customer_invoice_type",
    "CustomerInvoiceTypeOne": ".customer_invoice_type_one",
    "CustomerInvoiceTypeTwo": ".customer_invoice_type_two",
    "CustomerInvoiceTypeZero": ".customer_invoice_type_zero",
    "DetailedCustomerInvoice": ".detailed_customer_invoice",
    "DetailedCustomerInvoiceCustomer": ".detailed_customer_invoice_customer",
    "DetailedCustomerInvoiceDueDays": ".detailed_customer_invoice_due_days",
    "DetailedCustomerInvoiceSectionsItem": ".detailed_customer_invoice_sections_item",
    "DetailedCustomerInvoiceSectionsItemLineItemsItem": ".detailed_customer_invoice_sections_item_line_items_item",
    "DetailedCustomerInvoiceStatus": ".detailed_customer_invoice_status",
    "DetailedCustomerInvoiceStatusFive": ".detailed_customer_invoice_status_five",
    "DetailedCustomerInvoiceStatusFour": ".detailed_customer_invoice_status_four",
    "DetailedCustomerInvoiceStatusOne": ".detailed_customer_invoice_status_one",
    "DetailedCustomerInvoiceStatusThree": ".detailed_customer_invoice_status_three",
    "DetailedCustomerInvoiceStatusTwo": ".detailed_customer_invoice_status_two",
    "DetailedCustomerInvoiceStatusZero": ".detailed_customer_invoice_status_zero",
    "DetailedCustomerInvoiceType": ".detailed_customer_invoice_type",
    "DetailedCustomerInvoiceTypeOne": ".detailed_customer_invoice_type_one",
    "DetailedCustomerInvoiceTypeTwo": ".detailed_customer_invoice_type_two",
    "DetailedCustomerInvoiceTypeZero": ".detailed_customer_invoice_type_zero",
    "EnquiriesResponse": ".enquiries_response",
    "Enquiry": ".enquiry",
    "EnquiryByIdResponse": ".enquiry_by_id_response",
    "EnquiryCreatedResponse": ".enquiry_created_response",
    "EnquiryWithJobIds": ".enquiry_with_job_ids",
    "ErrorResponse": ".error_response",
    "FavouritesFolder": ".favourites_folder",
    "FavouritesFolderSectionsItem": ".favourites_folder_sections_item",
    "FavouritesQueryParameters": ".favourites_query_parameters",
    "FavouritesQueryParametersRepresentation": ".favourites_query_parameters_representation",
    "FavouritesQueryParametersSortField": ".favourites_query_parameters_sort_field",
    "FavouritesQueryParametersSortOrder": ".favourites_query_parameters_sort_order",
    "FavouritesResponse": ".favourites_response",
    "FavouritesResponseData": ".favourites_response_data",
    "FavouritesResponseDataChildren": ".favourites_response_data_children",
    "FavouritesResponseDataChildrenSectionsItem": ".favourites_response_data_children_sections_item",
    "FavouritesResponseDataDescription": ".favourites_response_data_description",
    "FavouritesSection": ".favourites_section",
    "FavouritesSectionLineItemsItem": ".favourites_section_line_items_item",
    "FavouritesSectionPath": ".favourites_section_path",
    "FavouritesSectionPathItem": ".favourites_section_path_item",
    "GetCompanyResponse": ".get_company_response",
    "GetCustomerByIdResponse": ".get_customer_by_id_response",
    "GetCustomerInvoiceByIdResponse": ".get_customer_invoice_by_id_response",
    "GetCustomersResponse": ".get_customers_response",
    "GetNotesResponse": ".get_notes_response",
    "GetPriceBookByIdResponse": ".get_price_book_by_id_response",
    "GetPricebookItemByIdResponse": ".get_pricebook_item_by_id_response",
    "GetPricebookItemsResponse": ".get_pricebook_items_response",
    "GetPricebooksResponse": ".get_pricebooks_response",
    "GetPricingTierByIdResponse": ".get_pricing_tier_by_id_response",
    "GetPricingTiersResponse": ".get_pricing_tiers_response",
    "GetQuoteByIdQuoteResponse": ".get_quote_by_id_quote_response",
    "GetQuoteByIdQuoteResponseData": ".get_quote_by_id_quote_response_data",
    "GetQuoteByIdQuoteResponseDataDeposit": ".get_quote_by_id_quote_response_data_deposit",
    "GetQuoteByIdQuoteResponseDataDepositOptionType": ".get_quote_by_id_quote_response_data_deposit_option_type",
    "GetQuoteByIdQuoteResponseDataDepositOptionTypeOne": ".get_quote_by_id_quote_response_data_deposit_option_type_one",
    "GetQuoteByIdQuoteResponseDataDepositOptionTypeZero": ".get_quote_by_id_quote_response_data_deposit_option_type_zero",
    "GetQuoteByIdQuoteResponseDataLinksItem": ".get_quote_by_id_quote_response_data_links_item",
    "GetQuoteByIdQuoteResponseDataLinksItemType": ".get_quote_by_id_quote_response_data_links_item_type",
    "GetQuoteByIdQuoteResponseDataSectionsItem": ".get_quote_by_id_quote_response_data_sections_item",
    "GetQuoteByIdQuoteResponseDataSectionsItemLineItemsItem": ".get_quote_by_id_quote_response_data_sections_item_line_items_item",
    "GetQuoteByIdQuoteResponseDataSectionsItemSectionConfig": ".get_quote_by_id_quote_response_data_sections_item_section_config",
    "GetQuoteByIdQuoteResponseDataSectionsItemSelectionMode": ".get_quote_by_id_quote_response_data_sections_item_selection_mode",
    "GetQuotesResponse": ".get_quotes_response",
    "GetStandaloneQuotesResponse": ".get_standalone_quotes_response",
    "Headers": ".headers",
    "InvoiceSection": ".invoice_section",
    "InvoiceSectionLineItemsItem": ".invoice_section_line_items_item",
    "InvoicesQueryParameters": ".invoices_query_parameters",
    "InvoicesQueryParametersSortField": ".invoices_query_parameters_sort_field",
    "InvoicesQueryParametersSortOrder": ".invoices_query_parameters_sort_order",
    "Job": ".job",
    "JobActiveQuote": ".job_active_quote",
    "JobCustomer": ".job_customer",
    "JobFinancialSummary": ".job_financial_summary",
    "JobFinancialSummaryOne": ".job_financial_summary_one",
    "JobFinancialSummaryOneChargeableAmount": ".job_financial_summary_one_chargeable_amount",
    "JobFinancialSummaryOneCostsIncurred": ".job_financial_summary_one_costs_incurred",
    "JobFinancialSummaryOneJobType": ".job_financial_summary_one_job_type",
    "JobFinancialSummaryOneLabourHours": ".job_financial_summary_one_labour_hours",
    "JobFinancialSummaryOneTotalBilled": ".job_financial_summary_one_total_billed",
    "JobFinancialSummaryQuoteSummary": ".job_financial_summary_quote_summary",
    "JobFinancialSummaryQuoteSummaryChargeableAmount": ".job_financial_summary_quote_summary_chargeable_amount",
    "JobFinancialSummaryQuoteSummaryCostsIncurred": ".job_financial_summary_quote_summary_costs_incurred",
    "JobFinancialSummaryQuoteSummaryJobType": ".job_financial_summary_quote_summary_job_type",
    "JobFinancialSummaryQuoteSummaryJobTypeOne": ".job_financial_summary_quote_summary_job_type_one",
    "JobFinancialSummaryQuoteSummaryJobTypeZero": ".job_financial_summary_quote_summary_job_type_zero",
    "JobFinancialSummaryQuoteSummaryLabourHours": ".job_financial_summary_quote_summary_labour_hours",
    "JobFinancialSummaryQuoteSummaryQuoteSummary": ".job_financial_summary_quote_summary_quote_summary",
    "JobFinancialSummaryQuoteSummaryTotalBilled": ".job_financial_summary_quote_summary_total_billed",
    "JobFinancialSummaryResponse": ".job_financial_summary_response",
    "JobMainContact": ".job_main_contact",
    "JobParameter": ".job_parameter",
    "JobPhase": ".job_phase",
    "JobPhaseParameter": ".job_phase_parameter",
    "JobPhaseResponse": ".job_phase_response",
    "JobPhasesResponse": ".job_phases_response",
    "JobResponse": ".job_response",
    "JobSiteAddress": ".job_site_address",
    "JobsQueryParameters": ".jobs_query_parameters",
    "JobsQueryParametersFilterJobStatus": ".jobs_query_parameters_filter_job_status",
    "JobsQueryParametersFilterJobType": ".jobs_query_parameters_filter_job_type",
    "JobsQueryParametersSortField": ".jobs_query_parameters_sort_field",
    "JobsQueryParametersSortOrder": ".jobs_query_parameters_sort_order",
    "JobsResponse": ".jobs_response",
    "Links": ".links",
    "LinksType": ".links_type",
    "ListCustomerInvoicesResponse": ".list_customer_invoices_response",
    "Note": ".note",
    "NoteEntityName": ".note_entity_name",
    "NoteEntityNameFive": ".note_entity_name_five",
    "NoteEntityNameFour": ".note_entity_name_four",
    "NoteEntityNameOne": ".note_entity_name_one",
    "NoteEntityNameSeven": ".note_entity_name_seven",
    "NoteEntityNameSix": ".note_entity_name_six",
    "NoteEntityNameThree": ".note_entity_name_three",
    "NoteEntityNameTwo": ".note_entity_name_two",
    "NoteEntityNameZero": ".note_entity_name_zero",
    "NoteReply": ".note_reply",
    "NoteReplyEntityName": ".note_reply_entity_name",
    "NoteReplyEntityNameFive": ".note_reply_entity_name_five",
    "NoteReplyEntityNameFour": ".note_reply_entity_name_four",
    "NoteReplyEntityNameOne": ".note_reply_entity_name_one",
    "NoteReplyEntityNameSeven": ".note_reply_entity_name_seven",
    "NoteReplyEntityNameSix": ".note_reply_entity_name_six",
    "NoteReplyEntityNameThree": ".note_reply_entity_name_three",
    "NoteReplyEntityNameTwo": ".note_reply_entity_name_two",
    "NoteReplyEntityNameZero": ".note_reply_entity_name_zero",
    "Pagination": ".pagination",
    "PaginationLinks": ".pagination_links",
    "PersonContact": ".person_contact",
    "PersonPayload": ".person_payload",
    "Pricebook": ".pricebook",
    "PricebookItem": ".pricebook_item",
    "PricebookItemPricingTier": ".pricebook_item_pricing_tier",
    "PricebookSearchItem": ".pricebook_search_item",
    "PricebookType": ".pricebook_type",
    "PricebookTypeOne": ".pricebook_type_one",
    "PricebookTypeTwo": ".pricebook_type_two",
    "PricebookTypeZero": ".pricebook_type_zero",
    "PricingTier": ".pricing_tier",
    "Quote": ".quote",
    "QuoteConfig": ".quote_config",
    "QuoteDeposit": ".quote_deposit",
    "QuoteDepositOptionType": ".quote_deposit_option_type",
    "QuoteDepositOptionTypeOne": ".quote_deposit_option_type_one",
    "QuoteDepositOptionTypeZero": ".quote_deposit_option_type_zero",
    "QuoteJobFinancialSummary": ".quote_job_financial_summary",
    "QuoteLinksItem": ".quote_links_item",
    "QuoteLinksItemType": ".quote_links_item_type",
    "QuoteParameters": ".quote_parameters",
    "QuoteSection": ".quote_section",
    "QuoteSectionLineItemsItem": ".quote_section_line_items_item",
    "QuoteSectionSectionConfig": ".quote_section_section_config",
    "QuoteSectionSelectionMode": ".quote_section_selection_mode",
    "QuoteSectionsItem": ".quote_sections_item",
    "QuoteSectionsItemLineItemsItem": ".quote_sections_item_line_items_item",
    "QuoteSectionsItemSectionConfig": ".quote_sections_item_section_config",
    "QuoteSectionsItemSelectionMode": ".quote_sections_item_selection_mode",
    "QuoteTotals": ".quote_totals",
    "QuoteTotalsQuoteTotal": ".quote_totals_quote_total",
    "QuoteTotalsResponse": ".quote_totals_response",
    "QuoteTotalsSectionTotalsItem": ".quote_totals_section_totals_item",
    "RecurringEventDetails": ".recurring_event_details",
    "RedirectResponse": ".redirect_response",
    "SearchPricebooksResponse": ".search_pricebooks_response",
    "SectionConfig": ".section_config",
    "Site": ".site",
    "SiteByIdResponse": ".site_by_id_response",
    "SitesResponse": ".sites_response",
    "StandaloneQuotesSpecificQueryParameters": ".standalone_quotes_specific_query_parameters",
    "StandaloneQuotesSpecificQueryParametersFilterStatus": ".standalone_quotes_specific_query_parameters_filter_status",
    "StandaloneQuotesSpecificQueryParametersSortField": ".standalone_quotes_specific_query_parameters_sort_field",
    "StockOnHandItem": ".stock_on_hand_item",
    "StockOnHandListResponse": ".stock_on_hand_list_response",
    "StockOnHandQueryParameters": ".stock_on_hand_query_parameters",
    "StockOnHandQueryParametersSortField": ".stock_on_hand_query_parameters_sort_field",
    "StockOnHandQueryParametersSortOrder": ".stock_on_hand_query_parameters_sort_order",
    "StockOnHandResponse": ".stock_on_hand_response",
    "StockUsedItem": ".stock_used_item",
    "StockUsedListResponse": ".stock_used_list_response",
    "StockUsedQueryParameters": ".stock_used_query_parameters",
    "TimeEntriesResponse": ".time_entries_response",
    "TimeEntry": ".time_entry",
    "UpdateQuotePayload": ".update_quote_payload",
    "UpdateQuotePayloadSectionsItem": ".update_quote_payload_sections_item",
    "UpdateQuotePayloadSectionsItemFavouriteSectionId": ".update_quote_payload_sections_item_favourite_section_id",
    "UpdateQuotePayloadSectionsItemFavouriteSectionIdCombined": ".update_quote_payload_sections_item_favourite_section_id_combined",
    "UpdateQuotePayloadSectionsItemFavouriteSectionIds": ".update_quote_payload_sections_item_favourite_section_ids",
    "UpdateQuotePayloadSectionsItemFavouriteSectionIdsOneItem": ".update_quote_payload_sections_item_favourite_section_ids_one_item",
    "UpdateQuotePayloadSectionsItemLineItemsItem": ".update_quote_payload_sections_item_line_items_item",
    "UpdateQuoteResponse": ".update_quote_response",
    "UpdateQuoteResponseData": ".update_quote_response_data",
    "UpdateQuoteResponseDataDeposit": ".update_quote_response_data_deposit",
    "UpdateQuoteResponseDataDepositOptionType": ".update_quote_response_data_deposit_option_type",
    "UpdateQuoteResponseDataDepositOptionTypeOne": ".update_quote_response_data_deposit_option_type_one",
    "UpdateQuoteResponseDataDepositOptionTypeZero": ".update_quote_response_data_deposit_option_type_zero",
    "UpdateQuoteResponseDataLineItemsItem": ".update_quote_response_data_line_items_item",
    "UpdateQuoteResponseDataLinksItem": ".update_quote_response_data_links_item",
    "UpdateQuoteResponseDataLinksItemType": ".update_quote_response_data_links_item_type",
    "UpdateQuoteResponseDataSectionsItem": ".update_quote_response_data_sections_item",
    "UpdateQuoteResponseDataSectionsItemLineItemsItem": ".update_quote_response_data_sections_item_line_items_item",
    "UpdateQuoteResponseDataSectionsItemSectionConfig": ".update_quote_response_data_sections_item_section_config",
    "UpdateQuoteResponseDataSectionsItemSelectionMode": ".update_quote_response_data_sections_item_selection_mode",
    "UpdateStockOnHandItem": ".update_stock_on_hand_item",
    "UpsertQuoteSection": ".upsert_quote_section",
    "UpsertQuoteSectionFavouriteSectionId": ".upsert_quote_section_favourite_section_id",
    "UpsertQuoteSectionFavouriteSectionIdCombined": ".upsert_quote_section_favourite_section_id_combined",
    "UpsertQuoteSectionFavouriteSectionIds": ".upsert_quote_section_favourite_section_ids",
    "UpsertQuoteSectionFavouriteSectionIdsOneItem": ".upsert_quote_section_favourite_section_ids_one_item",
    "UpsertQuoteSectionLineItemsItem": ".upsert_quote_section_line_items_item",
    "User": ".user",
    "UserByIdResponse": ".user_by_id_response",
    "UserStatus": ".user_status",
    "UserUserType": ".user_user_type",
    "UsersResponse": ".users_response",
    "UsersResponseDataItem": ".users_response_data_item",
    "UsersResponseDataItemStatus": ".users_response_data_item_status",
    "UsersResponseDataItemUserType": ".users_response_data_item_user_type",
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
    "AcceptQuoteData",
    "AcceptQuoteResponse",
    "AcceptQuoteResponseData",
    "AddQuotePayload",
    "AddQuotePayloadSectionsItem",
    "AddQuotePayloadSectionsItemFavouriteSectionId",
    "AddQuotePayloadSectionsItemFavouriteSectionIdCombined",
    "AddQuotePayloadSectionsItemFavouriteSectionIds",
    "AddQuotePayloadSectionsItemFavouriteSectionIdsOneItem",
    "AddQuotePayloadSectionsItemLineItemsItem",
    "AddQuoteResponse",
    "AddQuoteResponseData",
    "AddQuoteResponseDataDeposit",
    "AddQuoteResponseDataDepositOptionType",
    "AddQuoteResponseDataDepositOptionTypeOne",
    "AddQuoteResponseDataDepositOptionTypeZero",
    "AddQuoteResponseDataLinksItem",
    "AddQuoteResponseDataLinksItemType",
    "AddQuoteResponseDataSectionsItem",
    "AddQuoteResponseDataSectionsItemLineItemsItem",
    "AddQuoteResponseDataSectionsItemSectionConfig",
    "AddQuoteResponseDataSectionsItemSelectionMode",
    "AddressContact",
    "AddressPayload",
    "CalendarEvent",
    "CalendarEventByIdResponse",
    "CalendarEventEventType",
    "CalendarEventsResponse",
    "ChargeUpJobFinancialSummary",
    "ChargeUpJobFinancialSummaryChargeableAmount",
    "ChargeUpJobFinancialSummaryCostsIncurred",
    "ChargeUpJobFinancialSummaryLabourHours",
    "ChargeUpJobFinancialSummaryTotalBilled",
    "Company",
    "CompanyContact",
    "CompanyContactContactItemsItem",
    "CompanyContactItem",
    "CompanySetting",
    "CompanySettingsItem",
    "CompanyTax",
    "Contact",
    "ContactByIdResponse",
    "ContactContactType",
    "ContactItem",
    "ContactItemContactType",
    "ContactItemPayload",
    "ContactItemPayloadContactType",
    "ContactsQueryParameters",
    "ContactsQueryParametersFilterContactType",
    "ContactsQueryParametersSortField",
    "ContactsQueryParametersSortOrder",
    "ContactsResponse",
    "CreateDraftJob",
    "CreateDraftJobJobType",
    "CreateEnquiryPayload",
    "CreateJobPhase",
    "CreateNonDraftJob",
    "CreateNonDraftJobJobType",
    "CreateStockOnHandItem",
    "CreateStockOnHandItemItemCost",
    "CreateStockOnHandItemPriceBookLineItemId",
    "Customer",
    "CustomerInvoice",
    "CustomerInvoiceDueDays",
    "CustomerInvoiceStatus",
    "CustomerInvoiceStatusFive",
    "CustomerInvoiceStatusFour",
    "CustomerInvoiceStatusOne",
    "CustomerInvoiceStatusThree",
    "CustomerInvoiceStatusTwo",
    "CustomerInvoiceStatusZero",
    "CustomerInvoiceType",
    "CustomerInvoiceTypeOne",
    "CustomerInvoiceTypeTwo",
    "CustomerInvoiceTypeZero",
    "DetailedCustomerInvoice",
    "DetailedCustomerInvoiceCustomer",
    "DetailedCustomerInvoiceDueDays",
    "DetailedCustomerInvoiceSectionsItem",
    "DetailedCustomerInvoiceSectionsItemLineItemsItem",
    "DetailedCustomerInvoiceStatus",
    "DetailedCustomerInvoiceStatusFive",
    "DetailedCustomerInvoiceStatusFour",
    "DetailedCustomerInvoiceStatusOne",
    "DetailedCustomerInvoiceStatusThree",
    "DetailedCustomerInvoiceStatusTwo",
    "DetailedCustomerInvoiceStatusZero",
    "DetailedCustomerInvoiceType",
    "DetailedCustomerInvoiceTypeOne",
    "DetailedCustomerInvoiceTypeTwo",
    "DetailedCustomerInvoiceTypeZero",
    "EnquiriesResponse",
    "Enquiry",
    "EnquiryByIdResponse",
    "EnquiryCreatedResponse",
    "EnquiryWithJobIds",
    "ErrorResponse",
    "FavouritesFolder",
    "FavouritesFolderSectionsItem",
    "FavouritesQueryParameters",
    "FavouritesQueryParametersRepresentation",
    "FavouritesQueryParametersSortField",
    "FavouritesQueryParametersSortOrder",
    "FavouritesResponse",
    "FavouritesResponseData",
    "FavouritesResponseDataChildren",
    "FavouritesResponseDataChildrenSectionsItem",
    "FavouritesResponseDataDescription",
    "FavouritesSection",
    "FavouritesSectionLineItemsItem",
    "FavouritesSectionPath",
    "FavouritesSectionPathItem",
    "GetCompanyResponse",
    "GetCustomerByIdResponse",
    "GetCustomerInvoiceByIdResponse",
    "GetCustomersResponse",
    "GetNotesResponse",
    "GetPriceBookByIdResponse",
    "GetPricebookItemByIdResponse",
    "GetPricebookItemsResponse",
    "GetPricebooksResponse",
    "GetPricingTierByIdResponse",
    "GetPricingTiersResponse",
    "GetQuoteByIdQuoteResponse",
    "GetQuoteByIdQuoteResponseData",
    "GetQuoteByIdQuoteResponseDataDeposit",
    "GetQuoteByIdQuoteResponseDataDepositOptionType",
    "GetQuoteByIdQuoteResponseDataDepositOptionTypeOne",
    "GetQuoteByIdQuoteResponseDataDepositOptionTypeZero",
    "GetQuoteByIdQuoteResponseDataLinksItem",
    "GetQuoteByIdQuoteResponseDataLinksItemType",
    "GetQuoteByIdQuoteResponseDataSectionsItem",
    "GetQuoteByIdQuoteResponseDataSectionsItemLineItemsItem",
    "GetQuoteByIdQuoteResponseDataSectionsItemSectionConfig",
    "GetQuoteByIdQuoteResponseDataSectionsItemSelectionMode",
    "GetQuotesResponse",
    "GetStandaloneQuotesResponse",
    "Headers",
    "InvoiceSection",
    "InvoiceSectionLineItemsItem",
    "InvoicesQueryParameters",
    "InvoicesQueryParametersSortField",
    "InvoicesQueryParametersSortOrder",
    "Job",
    "JobActiveQuote",
    "JobCustomer",
    "JobFinancialSummary",
    "JobFinancialSummaryOne",
    "JobFinancialSummaryOneChargeableAmount",
    "JobFinancialSummaryOneCostsIncurred",
    "JobFinancialSummaryOneJobType",
    "JobFinancialSummaryOneLabourHours",
    "JobFinancialSummaryOneTotalBilled",
    "JobFinancialSummaryQuoteSummary",
    "JobFinancialSummaryQuoteSummaryChargeableAmount",
    "JobFinancialSummaryQuoteSummaryCostsIncurred",
    "JobFinancialSummaryQuoteSummaryJobType",
    "JobFinancialSummaryQuoteSummaryJobTypeOne",
    "JobFinancialSummaryQuoteSummaryJobTypeZero",
    "JobFinancialSummaryQuoteSummaryLabourHours",
    "JobFinancialSummaryQuoteSummaryQuoteSummary",
    "JobFinancialSummaryQuoteSummaryTotalBilled",
    "JobFinancialSummaryResponse",
    "JobMainContact",
    "JobParameter",
    "JobPhase",
    "JobPhaseParameter",
    "JobPhaseResponse",
    "JobPhasesResponse",
    "JobResponse",
    "JobSiteAddress",
    "JobsQueryParameters",
    "JobsQueryParametersFilterJobStatus",
    "JobsQueryParametersFilterJobType",
    "JobsQueryParametersSortField",
    "JobsQueryParametersSortOrder",
    "JobsResponse",
    "Links",
    "LinksType",
    "ListCustomerInvoicesResponse",
    "Note",
    "NoteEntityName",
    "NoteEntityNameFive",
    "NoteEntityNameFour",
    "NoteEntityNameOne",
    "NoteEntityNameSeven",
    "NoteEntityNameSix",
    "NoteEntityNameThree",
    "NoteEntityNameTwo",
    "NoteEntityNameZero",
    "NoteReply",
    "NoteReplyEntityName",
    "NoteReplyEntityNameFive",
    "NoteReplyEntityNameFour",
    "NoteReplyEntityNameOne",
    "NoteReplyEntityNameSeven",
    "NoteReplyEntityNameSix",
    "NoteReplyEntityNameThree",
    "NoteReplyEntityNameTwo",
    "NoteReplyEntityNameZero",
    "Pagination",
    "PaginationLinks",
    "PersonContact",
    "PersonPayload",
    "Pricebook",
    "PricebookItem",
    "PricebookItemPricingTier",
    "PricebookSearchItem",
    "PricebookType",
    "PricebookTypeOne",
    "PricebookTypeTwo",
    "PricebookTypeZero",
    "PricingTier",
    "Quote",
    "QuoteConfig",
    "QuoteDeposit",
    "QuoteDepositOptionType",
    "QuoteDepositOptionTypeOne",
    "QuoteDepositOptionTypeZero",
    "QuoteJobFinancialSummary",
    "QuoteLinksItem",
    "QuoteLinksItemType",
    "QuoteParameters",
    "QuoteSection",
    "QuoteSectionLineItemsItem",
    "QuoteSectionSectionConfig",
    "QuoteSectionSelectionMode",
    "QuoteSectionsItem",
    "QuoteSectionsItemLineItemsItem",
    "QuoteSectionsItemSectionConfig",
    "QuoteSectionsItemSelectionMode",
    "QuoteTotals",
    "QuoteTotalsQuoteTotal",
    "QuoteTotalsResponse",
    "QuoteTotalsSectionTotalsItem",
    "RecurringEventDetails",
    "RedirectResponse",
    "SearchPricebooksResponse",
    "SectionConfig",
    "Site",
    "SiteByIdResponse",
    "SitesResponse",
    "StandaloneQuotesSpecificQueryParameters",
    "StandaloneQuotesSpecificQueryParametersFilterStatus",
    "StandaloneQuotesSpecificQueryParametersSortField",
    "StockOnHandItem",
    "StockOnHandListResponse",
    "StockOnHandQueryParameters",
    "StockOnHandQueryParametersSortField",
    "StockOnHandQueryParametersSortOrder",
    "StockOnHandResponse",
    "StockUsedItem",
    "StockUsedListResponse",
    "StockUsedQueryParameters",
    "TimeEntriesResponse",
    "TimeEntry",
    "UpdateQuotePayload",
    "UpdateQuotePayloadSectionsItem",
    "UpdateQuotePayloadSectionsItemFavouriteSectionId",
    "UpdateQuotePayloadSectionsItemFavouriteSectionIdCombined",
    "UpdateQuotePayloadSectionsItemFavouriteSectionIds",
    "UpdateQuotePayloadSectionsItemFavouriteSectionIdsOneItem",
    "UpdateQuotePayloadSectionsItemLineItemsItem",
    "UpdateQuoteResponse",
    "UpdateQuoteResponseData",
    "UpdateQuoteResponseDataDeposit",
    "UpdateQuoteResponseDataDepositOptionType",
    "UpdateQuoteResponseDataDepositOptionTypeOne",
    "UpdateQuoteResponseDataDepositOptionTypeZero",
    "UpdateQuoteResponseDataLineItemsItem",
    "UpdateQuoteResponseDataLinksItem",
    "UpdateQuoteResponseDataLinksItemType",
    "UpdateQuoteResponseDataSectionsItem",
    "UpdateQuoteResponseDataSectionsItemLineItemsItem",
    "UpdateQuoteResponseDataSectionsItemSectionConfig",
    "UpdateQuoteResponseDataSectionsItemSelectionMode",
    "UpdateStockOnHandItem",
    "UpsertQuoteSection",
    "UpsertQuoteSectionFavouriteSectionId",
    "UpsertQuoteSectionFavouriteSectionIdCombined",
    "UpsertQuoteSectionFavouriteSectionIds",
    "UpsertQuoteSectionFavouriteSectionIdsOneItem",
    "UpsertQuoteSectionLineItemsItem",
    "User",
    "UserByIdResponse",
    "UserStatus",
    "UserUserType",
    "UsersResponse",
    "UsersResponseDataItem",
    "UsersResponseDataItemStatus",
    "UsersResponseDataItemUserType",
]
