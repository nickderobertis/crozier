



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .accounting_customer import AccountingCustomer
    from .accounting_customer_status import AccountingCustomerStatus
    from .accounting_event_type import AccountingEventType
    from .accounting_webhook_event import AccountingWebhookEvent
    from .active import Active
    from .address import Address
    from .address_type import AddressType
    from .bad_request_response import BadRequestResponse
    from .bad_request_response_detail import BadRequestResponseDetail
    from .balance_sheet import BalanceSheet
    from .balance_sheet_assets import BalanceSheetAssets
    from .balance_sheet_assets_current_assets import BalanceSheetAssetsCurrentAssets
    from .balance_sheet_assets_current_assets_accounts_item import BalanceSheetAssetsCurrentAssetsAccountsItem
    from .balance_sheet_assets_fixed_assets import BalanceSheetAssetsFixedAssets
    from .balance_sheet_assets_fixed_assets_accounts_item import BalanceSheetAssetsFixedAssetsAccountsItem
    from .balance_sheet_equity import BalanceSheetEquity
    from .balance_sheet_equity_items_item import BalanceSheetEquityItemsItem
    from .balance_sheet_filter import BalanceSheetFilter
    from .balance_sheet_liabilities import BalanceSheetLiabilities
    from .balance_sheet_liabilities_accounts_item import BalanceSheetLiabilitiesAccountsItem
    from .bank_account import BankAccount
    from .bank_account_account_type import BankAccountAccountType
    from .bill import Bill
    from .bill_line_item import BillLineItem
    from .bill_line_item_type import BillLineItemType
    from .bill_status import BillStatus
    from .bills_sort import BillsSort
    from .bills_sort_by import BillsSortBy
    from .company import Company
    from .company_info import CompanyInfo
    from .company_info_fiscal_year_start_month import CompanyInfoFiscalYearStartMonth
    from .company_info_status import CompanyInfoStatus
    from .company_name import CompanyName
    from .company_row_type import CompanyRowType
    from .contact import Contact
    from .contact_gender import ContactGender
    from .contact_type import ContactType
    from .create_bill_response import CreateBillResponse
    from .create_credit_note_response import CreateCreditNoteResponse
    from .create_customer_response import CreateCustomerResponse
    from .create_invoice_item_response import CreateInvoiceItemResponse
    from .create_invoice_response import CreateInvoiceResponse
    from .create_journal_entry_response import CreateJournalEntryResponse
    from .create_ledger_account_response import CreateLedgerAccountResponse
    from .create_payment_response import CreatePaymentResponse
    from .create_supplier_response import CreateSupplierResponse
    from .create_tax_rate_response import CreateTaxRateResponse
    from .created_at import CreatedAt
    from .created_by import CreatedBy
    from .credit_note import CreditNote
    from .credit_note_allocations_item import CreditNoteAllocationsItem
    from .credit_note_allocations_item_type import CreditNoteAllocationsItemType
    from .credit_note_status import CreditNoteStatus
    from .credit_note_type import CreditNoteType
    from .currency import Currency
    from .currency_rate import CurrencyRate
    from .custom_field import CustomField
    from .custom_field_value import CustomFieldValue
    from .customers_filter import CustomersFilter
    from .delete_bill_response import DeleteBillResponse
    from .delete_credit_note_response import DeleteCreditNoteResponse
    from .delete_customer_response import DeleteCustomerResponse
    from .delete_invoice_item_response import DeleteInvoiceItemResponse
    from .delete_invoice_response import DeleteInvoiceResponse
    from .delete_journal_entry_response import DeleteJournalEntryResponse
    from .delete_ledger_account_response import DeleteLedgerAccountResponse
    from .delete_payment_response import DeletePaymentResponse
    from .delete_supplier_response import DeleteSupplierResponse
    from .delete_tax_rate_response import DeleteTaxRateResponse
    from .downstream_id import DownstreamId
    from .email import Email
    from .email_type import EmailType
    from .first_name import FirstName
    from .get_balance_sheet_response import GetBalanceSheetResponse
    from .get_bill_response import GetBillResponse
    from .get_bills_response import GetBillsResponse
    from .get_company_info_response import GetCompanyInfoResponse
    from .get_credit_note_response import GetCreditNoteResponse
    from .get_credit_notes_response import GetCreditNotesResponse
    from .get_customer_response import GetCustomerResponse
    from .get_customers_response import GetCustomersResponse
    from .get_invoice_item_response import GetInvoiceItemResponse
    from .get_invoice_items_response import GetInvoiceItemsResponse
    from .get_invoice_response import GetInvoiceResponse
    from .get_invoices_response import GetInvoicesResponse
    from .get_journal_entries_response import GetJournalEntriesResponse
    from .get_journal_entry_response import GetJournalEntryResponse
    from .get_ledger_account_response import GetLedgerAccountResponse
    from .get_ledger_accounts_response import GetLedgerAccountsResponse
    from .get_payment_response import GetPaymentResponse
    from .get_payments_response import GetPaymentsResponse
    from .get_profit_and_loss_response import GetProfitAndLossResponse
    from .get_supplier_response import GetSupplierResponse
    from .get_suppliers_response import GetSuppliersResponse
    from .get_tax_rate_response import GetTaxRateResponse
    from .get_tax_rates_response import GetTaxRatesResponse
    from .id import Id
    from .invoice import Invoice
    from .invoice_item import InvoiceItem
    from .invoice_item_asset_account import InvoiceItemAssetAccount
    from .invoice_item_expense_account import InvoiceItemExpenseAccount
    from .invoice_item_income_account import InvoiceItemIncomeAccount
    from .invoice_item_purchase_details import InvoiceItemPurchaseDetails
    from .invoice_item_sales_details import InvoiceItemSalesDetails
    from .invoice_item_type import InvoiceItemType
    from .invoice_items_filter import InvoiceItemsFilter
    from .invoice_line_item import InvoiceLineItem
    from .invoice_line_item_type import InvoiceLineItemType
    from .invoice_response import InvoiceResponse
    from .invoice_status import InvoiceStatus
    from .invoice_type import InvoiceType
    from .invoices_sort import InvoicesSort
    from .invoices_sort_by import InvoicesSortBy
    from .journal_entry import JournalEntry
    from .journal_entry_line_item import JournalEntryLineItem
    from .journal_entry_line_item_type import JournalEntryLineItemType
    from .language import Language
    from .last_name import LastName
    from .ledger_account import LedgerAccount
    from .ledger_account_categories_item import LedgerAccountCategoriesItem
    from .ledger_account_classification import LedgerAccountClassification
    from .ledger_account_parent_account import LedgerAccountParentAccount
    from .ledger_account_status import LedgerAccountStatus
    from .ledger_account_sub_accounts_item import LedgerAccountSubAccountsItem
    from .ledger_account_type import LedgerAccountType
    from .ledger_accounts import LedgerAccounts
    from .linked_customer import LinkedCustomer
    from .linked_invoice_item import LinkedInvoiceItem
    from .linked_ledger_account import LinkedLedgerAccount
    from .linked_parent_customer import LinkedParentCustomer
    from .linked_supplier import LinkedSupplier
    from .linked_tax_rate import LinkedTaxRate
    from .linked_tracking_category import LinkedTrackingCategory
    from .links import Links
    from .meta import Meta
    from .meta_cursors import MetaCursors
    from .middle_name import MiddleName
    from .not_found_response import NotFoundResponse
    from .not_found_response_detail import NotFoundResponseDetail
    from .not_implemented_response import NotImplementedResponse
    from .not_implemented_response_detail import NotImplementedResponseDetail
    from .pass_through_query import PassThroughQuery
    from .payment import Payment
    from .payment_allocations_item import PaymentAllocationsItem
    from .payment_allocations_item_type import PaymentAllocationsItemType
    from .payment_required_response import PaymentRequiredResponse
    from .payment_status import PaymentStatus
    from .payment_type import PaymentType
    from .phone_number import PhoneNumber
    from .phone_number_type import PhoneNumberType
    from .profit_and_loss import ProfitAndLoss
    from .profit_and_loss_expenses import ProfitAndLossExpenses
    from .profit_and_loss_filter import ProfitAndLossFilter
    from .profit_and_loss_gross_profit import ProfitAndLossGrossProfit
    from .profit_and_loss_income import ProfitAndLossIncome
    from .profit_and_loss_net_income import ProfitAndLossNetIncome
    from .profit_and_loss_net_operating_income import ProfitAndLossNetOperatingIncome
    from .profit_and_loss_record import ProfitAndLossRecord
    from .profit_and_loss_records import ProfitAndLossRecords
    from .profit_and_loss_records_item import (
        ProfitAndLossRecordsItem,
        ProfitAndLossRecordsItem_Record,
        ProfitAndLossRecordsItem_Section,
    )
    from .profit_and_loss_section import ProfitAndLossSection
    from .quantity import Quantity
    from .row_version import RowVersion
    from .sales_tax_number import SalesTaxNumber
    from .social_link import SocialLink
    from .sort_direction import SortDirection
    from .suffix import Suffix
    from .supplier import Supplier
    from .supplier_status import SupplierStatus
    from .suppliers_filter import SuppliersFilter
    from .tags import Tags
    from .tax_inclusive import TaxInclusive
    from .tax_number import TaxNumber
    from .tax_rate import TaxRate
    from .tax_rate_components_item import TaxRateComponentsItem
    from .tax_rate_status import TaxRateStatus
    from .tax_rates_filter import TaxRatesFilter
    from .title import Title
    from .too_many_requests_response import TooManyRequestsResponse
    from .too_many_requests_response_detail import TooManyRequestsResponseDetail
    from .unauthorized_response import UnauthorizedResponse
    from .unexpected_error_response import UnexpectedErrorResponse
    from .unexpected_error_response_detail import UnexpectedErrorResponseDetail
    from .unified_id import UnifiedId
    from .unit_of_measure import UnitOfMeasure
    from .unit_price import UnitPrice
    from .unprocessable_response import UnprocessableResponse
    from .update_bill_response import UpdateBillResponse
    from .update_credit_note_response import UpdateCreditNoteResponse
    from .update_customer_response import UpdateCustomerResponse
    from .update_invoice_items_response import UpdateInvoiceItemsResponse
    from .update_invoice_response import UpdateInvoiceResponse
    from .update_journal_entry_response import UpdateJournalEntryResponse
    from .update_ledger_account_response import UpdateLedgerAccountResponse
    from .update_payment_response import UpdatePaymentResponse
    from .update_supplier_response import UpdateSupplierResponse
    from .update_tax_rate_response import UpdateTaxRateResponse
    from .updated_at import UpdatedAt
    from .updated_by import UpdatedBy
    from .website import Website
    from .website_type import WebsiteType
_dynamic_imports: typing.Dict[str, str] = {
    "AccountingCustomer": ".accounting_customer",
    "AccountingCustomerStatus": ".accounting_customer_status",
    "AccountingEventType": ".accounting_event_type",
    "AccountingWebhookEvent": ".accounting_webhook_event",
    "Active": ".active",
    "Address": ".address",
    "AddressType": ".address_type",
    "BadRequestResponse": ".bad_request_response",
    "BadRequestResponseDetail": ".bad_request_response_detail",
    "BalanceSheet": ".balance_sheet",
    "BalanceSheetAssets": ".balance_sheet_assets",
    "BalanceSheetAssetsCurrentAssets": ".balance_sheet_assets_current_assets",
    "BalanceSheetAssetsCurrentAssetsAccountsItem": ".balance_sheet_assets_current_assets_accounts_item",
    "BalanceSheetAssetsFixedAssets": ".balance_sheet_assets_fixed_assets",
    "BalanceSheetAssetsFixedAssetsAccountsItem": ".balance_sheet_assets_fixed_assets_accounts_item",
    "BalanceSheetEquity": ".balance_sheet_equity",
    "BalanceSheetEquityItemsItem": ".balance_sheet_equity_items_item",
    "BalanceSheetFilter": ".balance_sheet_filter",
    "BalanceSheetLiabilities": ".balance_sheet_liabilities",
    "BalanceSheetLiabilitiesAccountsItem": ".balance_sheet_liabilities_accounts_item",
    "BankAccount": ".bank_account",
    "BankAccountAccountType": ".bank_account_account_type",
    "Bill": ".bill",
    "BillLineItem": ".bill_line_item",
    "BillLineItemType": ".bill_line_item_type",
    "BillStatus": ".bill_status",
    "BillsSort": ".bills_sort",
    "BillsSortBy": ".bills_sort_by",
    "Company": ".company",
    "CompanyInfo": ".company_info",
    "CompanyInfoFiscalYearStartMonth": ".company_info_fiscal_year_start_month",
    "CompanyInfoStatus": ".company_info_status",
    "CompanyName": ".company_name",
    "CompanyRowType": ".company_row_type",
    "Contact": ".contact",
    "ContactGender": ".contact_gender",
    "ContactType": ".contact_type",
    "CreateBillResponse": ".create_bill_response",
    "CreateCreditNoteResponse": ".create_credit_note_response",
    "CreateCustomerResponse": ".create_customer_response",
    "CreateInvoiceItemResponse": ".create_invoice_item_response",
    "CreateInvoiceResponse": ".create_invoice_response",
    "CreateJournalEntryResponse": ".create_journal_entry_response",
    "CreateLedgerAccountResponse": ".create_ledger_account_response",
    "CreatePaymentResponse": ".create_payment_response",
    "CreateSupplierResponse": ".create_supplier_response",
    "CreateTaxRateResponse": ".create_tax_rate_response",
    "CreatedAt": ".created_at",
    "CreatedBy": ".created_by",
    "CreditNote": ".credit_note",
    "CreditNoteAllocationsItem": ".credit_note_allocations_item",
    "CreditNoteAllocationsItemType": ".credit_note_allocations_item_type",
    "CreditNoteStatus": ".credit_note_status",
    "CreditNoteType": ".credit_note_type",
    "Currency": ".currency",
    "CurrencyRate": ".currency_rate",
    "CustomField": ".custom_field",
    "CustomFieldValue": ".custom_field_value",
    "CustomersFilter": ".customers_filter",
    "DeleteBillResponse": ".delete_bill_response",
    "DeleteCreditNoteResponse": ".delete_credit_note_response",
    "DeleteCustomerResponse": ".delete_customer_response",
    "DeleteInvoiceItemResponse": ".delete_invoice_item_response",
    "DeleteInvoiceResponse": ".delete_invoice_response",
    "DeleteJournalEntryResponse": ".delete_journal_entry_response",
    "DeleteLedgerAccountResponse": ".delete_ledger_account_response",
    "DeletePaymentResponse": ".delete_payment_response",
    "DeleteSupplierResponse": ".delete_supplier_response",
    "DeleteTaxRateResponse": ".delete_tax_rate_response",
    "DownstreamId": ".downstream_id",
    "Email": ".email",
    "EmailType": ".email_type",
    "FirstName": ".first_name",
    "GetBalanceSheetResponse": ".get_balance_sheet_response",
    "GetBillResponse": ".get_bill_response",
    "GetBillsResponse": ".get_bills_response",
    "GetCompanyInfoResponse": ".get_company_info_response",
    "GetCreditNoteResponse": ".get_credit_note_response",
    "GetCreditNotesResponse": ".get_credit_notes_response",
    "GetCustomerResponse": ".get_customer_response",
    "GetCustomersResponse": ".get_customers_response",
    "GetInvoiceItemResponse": ".get_invoice_item_response",
    "GetInvoiceItemsResponse": ".get_invoice_items_response",
    "GetInvoiceResponse": ".get_invoice_response",
    "GetInvoicesResponse": ".get_invoices_response",
    "GetJournalEntriesResponse": ".get_journal_entries_response",
    "GetJournalEntryResponse": ".get_journal_entry_response",
    "GetLedgerAccountResponse": ".get_ledger_account_response",
    "GetLedgerAccountsResponse": ".get_ledger_accounts_response",
    "GetPaymentResponse": ".get_payment_response",
    "GetPaymentsResponse": ".get_payments_response",
    "GetProfitAndLossResponse": ".get_profit_and_loss_response",
    "GetSupplierResponse": ".get_supplier_response",
    "GetSuppliersResponse": ".get_suppliers_response",
    "GetTaxRateResponse": ".get_tax_rate_response",
    "GetTaxRatesResponse": ".get_tax_rates_response",
    "Id": ".id",
    "Invoice": ".invoice",
    "InvoiceItem": ".invoice_item",
    "InvoiceItemAssetAccount": ".invoice_item_asset_account",
    "InvoiceItemExpenseAccount": ".invoice_item_expense_account",
    "InvoiceItemIncomeAccount": ".invoice_item_income_account",
    "InvoiceItemPurchaseDetails": ".invoice_item_purchase_details",
    "InvoiceItemSalesDetails": ".invoice_item_sales_details",
    "InvoiceItemType": ".invoice_item_type",
    "InvoiceItemsFilter": ".invoice_items_filter",
    "InvoiceLineItem": ".invoice_line_item",
    "InvoiceLineItemType": ".invoice_line_item_type",
    "InvoiceResponse": ".invoice_response",
    "InvoiceStatus": ".invoice_status",
    "InvoiceType": ".invoice_type",
    "InvoicesSort": ".invoices_sort",
    "InvoicesSortBy": ".invoices_sort_by",
    "JournalEntry": ".journal_entry",
    "JournalEntryLineItem": ".journal_entry_line_item",
    "JournalEntryLineItemType": ".journal_entry_line_item_type",
    "Language": ".language",
    "LastName": ".last_name",
    "LedgerAccount": ".ledger_account",
    "LedgerAccountCategoriesItem": ".ledger_account_categories_item",
    "LedgerAccountClassification": ".ledger_account_classification",
    "LedgerAccountParentAccount": ".ledger_account_parent_account",
    "LedgerAccountStatus": ".ledger_account_status",
    "LedgerAccountSubAccountsItem": ".ledger_account_sub_accounts_item",
    "LedgerAccountType": ".ledger_account_type",
    "LedgerAccounts": ".ledger_accounts",
    "LinkedCustomer": ".linked_customer",
    "LinkedInvoiceItem": ".linked_invoice_item",
    "LinkedLedgerAccount": ".linked_ledger_account",
    "LinkedParentCustomer": ".linked_parent_customer",
    "LinkedSupplier": ".linked_supplier",
    "LinkedTaxRate": ".linked_tax_rate",
    "LinkedTrackingCategory": ".linked_tracking_category",
    "Links": ".links",
    "Meta": ".meta",
    "MetaCursors": ".meta_cursors",
    "MiddleName": ".middle_name",
    "NotFoundResponse": ".not_found_response",
    "NotFoundResponseDetail": ".not_found_response_detail",
    "NotImplementedResponse": ".not_implemented_response",
    "NotImplementedResponseDetail": ".not_implemented_response_detail",
    "PassThroughQuery": ".pass_through_query",
    "Payment": ".payment",
    "PaymentAllocationsItem": ".payment_allocations_item",
    "PaymentAllocationsItemType": ".payment_allocations_item_type",
    "PaymentRequiredResponse": ".payment_required_response",
    "PaymentStatus": ".payment_status",
    "PaymentType": ".payment_type",
    "PhoneNumber": ".phone_number",
    "PhoneNumberType": ".phone_number_type",
    "ProfitAndLoss": ".profit_and_loss",
    "ProfitAndLossExpenses": ".profit_and_loss_expenses",
    "ProfitAndLossFilter": ".profit_and_loss_filter",
    "ProfitAndLossGrossProfit": ".profit_and_loss_gross_profit",
    "ProfitAndLossIncome": ".profit_and_loss_income",
    "ProfitAndLossNetIncome": ".profit_and_loss_net_income",
    "ProfitAndLossNetOperatingIncome": ".profit_and_loss_net_operating_income",
    "ProfitAndLossRecord": ".profit_and_loss_record",
    "ProfitAndLossRecords": ".profit_and_loss_records",
    "ProfitAndLossRecordsItem": ".profit_and_loss_records_item",
    "ProfitAndLossRecordsItem_Record": ".profit_and_loss_records_item",
    "ProfitAndLossRecordsItem_Section": ".profit_and_loss_records_item",
    "ProfitAndLossSection": ".profit_and_loss_section",
    "Quantity": ".quantity",
    "RowVersion": ".row_version",
    "SalesTaxNumber": ".sales_tax_number",
    "SocialLink": ".social_link",
    "SortDirection": ".sort_direction",
    "Suffix": ".suffix",
    "Supplier": ".supplier",
    "SupplierStatus": ".supplier_status",
    "SuppliersFilter": ".suppliers_filter",
    "Tags": ".tags",
    "TaxInclusive": ".tax_inclusive",
    "TaxNumber": ".tax_number",
    "TaxRate": ".tax_rate",
    "TaxRateComponentsItem": ".tax_rate_components_item",
    "TaxRateStatus": ".tax_rate_status",
    "TaxRatesFilter": ".tax_rates_filter",
    "Title": ".title",
    "TooManyRequestsResponse": ".too_many_requests_response",
    "TooManyRequestsResponseDetail": ".too_many_requests_response_detail",
    "UnauthorizedResponse": ".unauthorized_response",
    "UnexpectedErrorResponse": ".unexpected_error_response",
    "UnexpectedErrorResponseDetail": ".unexpected_error_response_detail",
    "UnifiedId": ".unified_id",
    "UnitOfMeasure": ".unit_of_measure",
    "UnitPrice": ".unit_price",
    "UnprocessableResponse": ".unprocessable_response",
    "UpdateBillResponse": ".update_bill_response",
    "UpdateCreditNoteResponse": ".update_credit_note_response",
    "UpdateCustomerResponse": ".update_customer_response",
    "UpdateInvoiceItemsResponse": ".update_invoice_items_response",
    "UpdateInvoiceResponse": ".update_invoice_response",
    "UpdateJournalEntryResponse": ".update_journal_entry_response",
    "UpdateLedgerAccountResponse": ".update_ledger_account_response",
    "UpdatePaymentResponse": ".update_payment_response",
    "UpdateSupplierResponse": ".update_supplier_response",
    "UpdateTaxRateResponse": ".update_tax_rate_response",
    "UpdatedAt": ".updated_at",
    "UpdatedBy": ".updated_by",
    "Website": ".website",
    "WebsiteType": ".website_type",
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
    "AccountingCustomer",
    "AccountingCustomerStatus",
    "AccountingEventType",
    "AccountingWebhookEvent",
    "Active",
    "Address",
    "AddressType",
    "BadRequestResponse",
    "BadRequestResponseDetail",
    "BalanceSheet",
    "BalanceSheetAssets",
    "BalanceSheetAssetsCurrentAssets",
    "BalanceSheetAssetsCurrentAssetsAccountsItem",
    "BalanceSheetAssetsFixedAssets",
    "BalanceSheetAssetsFixedAssetsAccountsItem",
    "BalanceSheetEquity",
    "BalanceSheetEquityItemsItem",
    "BalanceSheetFilter",
    "BalanceSheetLiabilities",
    "BalanceSheetLiabilitiesAccountsItem",
    "BankAccount",
    "BankAccountAccountType",
    "Bill",
    "BillLineItem",
    "BillLineItemType",
    "BillStatus",
    "BillsSort",
    "BillsSortBy",
    "Company",
    "CompanyInfo",
    "CompanyInfoFiscalYearStartMonth",
    "CompanyInfoStatus",
    "CompanyName",
    "CompanyRowType",
    "Contact",
    "ContactGender",
    "ContactType",
    "CreateBillResponse",
    "CreateCreditNoteResponse",
    "CreateCustomerResponse",
    "CreateInvoiceItemResponse",
    "CreateInvoiceResponse",
    "CreateJournalEntryResponse",
    "CreateLedgerAccountResponse",
    "CreatePaymentResponse",
    "CreateSupplierResponse",
    "CreateTaxRateResponse",
    "CreatedAt",
    "CreatedBy",
    "CreditNote",
    "CreditNoteAllocationsItem",
    "CreditNoteAllocationsItemType",
    "CreditNoteStatus",
    "CreditNoteType",
    "Currency",
    "CurrencyRate",
    "CustomField",
    "CustomFieldValue",
    "CustomersFilter",
    "DeleteBillResponse",
    "DeleteCreditNoteResponse",
    "DeleteCustomerResponse",
    "DeleteInvoiceItemResponse",
    "DeleteInvoiceResponse",
    "DeleteJournalEntryResponse",
    "DeleteLedgerAccountResponse",
    "DeletePaymentResponse",
    "DeleteSupplierResponse",
    "DeleteTaxRateResponse",
    "DownstreamId",
    "Email",
    "EmailType",
    "FirstName",
    "GetBalanceSheetResponse",
    "GetBillResponse",
    "GetBillsResponse",
    "GetCompanyInfoResponse",
    "GetCreditNoteResponse",
    "GetCreditNotesResponse",
    "GetCustomerResponse",
    "GetCustomersResponse",
    "GetInvoiceItemResponse",
    "GetInvoiceItemsResponse",
    "GetInvoiceResponse",
    "GetInvoicesResponse",
    "GetJournalEntriesResponse",
    "GetJournalEntryResponse",
    "GetLedgerAccountResponse",
    "GetLedgerAccountsResponse",
    "GetPaymentResponse",
    "GetPaymentsResponse",
    "GetProfitAndLossResponse",
    "GetSupplierResponse",
    "GetSuppliersResponse",
    "GetTaxRateResponse",
    "GetTaxRatesResponse",
    "Id",
    "Invoice",
    "InvoiceItem",
    "InvoiceItemAssetAccount",
    "InvoiceItemExpenseAccount",
    "InvoiceItemIncomeAccount",
    "InvoiceItemPurchaseDetails",
    "InvoiceItemSalesDetails",
    "InvoiceItemType",
    "InvoiceItemsFilter",
    "InvoiceLineItem",
    "InvoiceLineItemType",
    "InvoiceResponse",
    "InvoiceStatus",
    "InvoiceType",
    "InvoicesSort",
    "InvoicesSortBy",
    "JournalEntry",
    "JournalEntryLineItem",
    "JournalEntryLineItemType",
    "Language",
    "LastName",
    "LedgerAccount",
    "LedgerAccountCategoriesItem",
    "LedgerAccountClassification",
    "LedgerAccountParentAccount",
    "LedgerAccountStatus",
    "LedgerAccountSubAccountsItem",
    "LedgerAccountType",
    "LedgerAccounts",
    "LinkedCustomer",
    "LinkedInvoiceItem",
    "LinkedLedgerAccount",
    "LinkedParentCustomer",
    "LinkedSupplier",
    "LinkedTaxRate",
    "LinkedTrackingCategory",
    "Links",
    "Meta",
    "MetaCursors",
    "MiddleName",
    "NotFoundResponse",
    "NotFoundResponseDetail",
    "NotImplementedResponse",
    "NotImplementedResponseDetail",
    "PassThroughQuery",
    "Payment",
    "PaymentAllocationsItem",
    "PaymentAllocationsItemType",
    "PaymentRequiredResponse",
    "PaymentStatus",
    "PaymentType",
    "PhoneNumber",
    "PhoneNumberType",
    "ProfitAndLoss",
    "ProfitAndLossExpenses",
    "ProfitAndLossFilter",
    "ProfitAndLossGrossProfit",
    "ProfitAndLossIncome",
    "ProfitAndLossNetIncome",
    "ProfitAndLossNetOperatingIncome",
    "ProfitAndLossRecord",
    "ProfitAndLossRecords",
    "ProfitAndLossRecordsItem",
    "ProfitAndLossRecordsItem_Record",
    "ProfitAndLossRecordsItem_Section",
    "ProfitAndLossSection",
    "Quantity",
    "RowVersion",
    "SalesTaxNumber",
    "SocialLink",
    "SortDirection",
    "Suffix",
    "Supplier",
    "SupplierStatus",
    "SuppliersFilter",
    "Tags",
    "TaxInclusive",
    "TaxNumber",
    "TaxRate",
    "TaxRateComponentsItem",
    "TaxRateStatus",
    "TaxRatesFilter",
    "Title",
    "TooManyRequestsResponse",
    "TooManyRequestsResponseDetail",
    "UnauthorizedResponse",
    "UnexpectedErrorResponse",
    "UnexpectedErrorResponseDetail",
    "UnifiedId",
    "UnitOfMeasure",
    "UnitPrice",
    "UnprocessableResponse",
    "UpdateBillResponse",
    "UpdateCreditNoteResponse",
    "UpdateCustomerResponse",
    "UpdateInvoiceItemsResponse",
    "UpdateInvoiceResponse",
    "UpdateJournalEntryResponse",
    "UpdateLedgerAccountResponse",
    "UpdatePaymentResponse",
    "UpdateSupplierResponse",
    "UpdateTaxRateResponse",
    "UpdatedAt",
    "UpdatedBy",
    "Website",
    "WebsiteType",
]
