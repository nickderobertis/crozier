

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AccountingEventType(enum.StrEnum):
    ALL = "*"
    ACCOUNTING_CUSTOMER_CREATED = "accounting.customer.created"
    ACCOUNTING_CUSTOMER_UPDATED = "accounting.customer.updated"
    ACCOUNTING_CUSTOMER_DELETED = "accounting.customer.deleted"
    ACCOUNTING_INVOICE_CREATED = "accounting.invoice.created"
    ACCOUNTING_INVOICE_UPDATED = "accounting.invoice.updated"
    ACCOUNTING_INVOICE_DELETED = "accounting.invoice.deleted"
    ACCOUNTING_INVOICE_ITEM_CREATED = "accounting.invoice_item.created"
    ACCOUNTING_INVOICE_ITEM_UPDATED = "accounting.invoice_item.updated"
    ACCOUNTING_INVOICE_ITEM_DELETED = "accounting.invoice_item.deleted"
    ACCOUNTING_LEDGER_ACCOUNT_CREATED = "accounting.ledger_account.created"
    ACCOUNTING_LEDGER_ACCOUNT_UPDATED = "accounting.ledger_account.updated"
    ACCOUNTING_LEDGER_ACCOUNT_DELETED = "accounting.ledger_account.deleted"
    ACCOUNTING_TAX_RATE_CREATED = "accounting.tax_rate.created"
    ACCOUNTING_TAX_RATE_UPDATED = "accounting.tax_rate.updated"
    ACCOUNTING_TAX_RATE_DELETED = "accounting.tax_rate.deleted"
    ACCOUNTING_BILL_CREATED = "accounting.bill.created"
    ACCOUNTING_BILL_UPDATED = "accounting.bill.updated"
    ACCOUNTING_BILL_DELETED = "accounting.bill.deleted"
    ACCOUNTING_PAYMENT_CREATED = "accounting.payment.created"
    ACCOUNTING_PAYMENT_UPDATED = "accounting.payment.updated"
    ACCOUNTING_PAYMENT_DELETED = "accounting.payment.deleted"
    ACCOUNTING_SUPPLIER_CREATED = "accounting.supplier.created"
    ACCOUNTING_SUPPLIER_UPDATED = "accounting.supplier.updated"
    ACCOUNTING_SUPPLIER_DELETED = "accounting.supplier.deleted"

    def visit(
        self,
        all_: typing.Callable[[], T_Result],
        accounting_customer_created: typing.Callable[[], T_Result],
        accounting_customer_updated: typing.Callable[[], T_Result],
        accounting_customer_deleted: typing.Callable[[], T_Result],
        accounting_invoice_created: typing.Callable[[], T_Result],
        accounting_invoice_updated: typing.Callable[[], T_Result],
        accounting_invoice_deleted: typing.Callable[[], T_Result],
        accounting_invoice_item_created: typing.Callable[[], T_Result],
        accounting_invoice_item_updated: typing.Callable[[], T_Result],
        accounting_invoice_item_deleted: typing.Callable[[], T_Result],
        accounting_ledger_account_created: typing.Callable[[], T_Result],
        accounting_ledger_account_updated: typing.Callable[[], T_Result],
        accounting_ledger_account_deleted: typing.Callable[[], T_Result],
        accounting_tax_rate_created: typing.Callable[[], T_Result],
        accounting_tax_rate_updated: typing.Callable[[], T_Result],
        accounting_tax_rate_deleted: typing.Callable[[], T_Result],
        accounting_bill_created: typing.Callable[[], T_Result],
        accounting_bill_updated: typing.Callable[[], T_Result],
        accounting_bill_deleted: typing.Callable[[], T_Result],
        accounting_payment_created: typing.Callable[[], T_Result],
        accounting_payment_updated: typing.Callable[[], T_Result],
        accounting_payment_deleted: typing.Callable[[], T_Result],
        accounting_supplier_created: typing.Callable[[], T_Result],
        accounting_supplier_updated: typing.Callable[[], T_Result],
        accounting_supplier_deleted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AccountingEventType.ALL:
            return all_()
        if self is AccountingEventType.ACCOUNTING_CUSTOMER_CREATED:
            return accounting_customer_created()
        if self is AccountingEventType.ACCOUNTING_CUSTOMER_UPDATED:
            return accounting_customer_updated()
        if self is AccountingEventType.ACCOUNTING_CUSTOMER_DELETED:
            return accounting_customer_deleted()
        if self is AccountingEventType.ACCOUNTING_INVOICE_CREATED:
            return accounting_invoice_created()
        if self is AccountingEventType.ACCOUNTING_INVOICE_UPDATED:
            return accounting_invoice_updated()
        if self is AccountingEventType.ACCOUNTING_INVOICE_DELETED:
            return accounting_invoice_deleted()
        if self is AccountingEventType.ACCOUNTING_INVOICE_ITEM_CREATED:
            return accounting_invoice_item_created()
        if self is AccountingEventType.ACCOUNTING_INVOICE_ITEM_UPDATED:
            return accounting_invoice_item_updated()
        if self is AccountingEventType.ACCOUNTING_INVOICE_ITEM_DELETED:
            return accounting_invoice_item_deleted()
        if self is AccountingEventType.ACCOUNTING_LEDGER_ACCOUNT_CREATED:
            return accounting_ledger_account_created()
        if self is AccountingEventType.ACCOUNTING_LEDGER_ACCOUNT_UPDATED:
            return accounting_ledger_account_updated()
        if self is AccountingEventType.ACCOUNTING_LEDGER_ACCOUNT_DELETED:
            return accounting_ledger_account_deleted()
        if self is AccountingEventType.ACCOUNTING_TAX_RATE_CREATED:
            return accounting_tax_rate_created()
        if self is AccountingEventType.ACCOUNTING_TAX_RATE_UPDATED:
            return accounting_tax_rate_updated()
        if self is AccountingEventType.ACCOUNTING_TAX_RATE_DELETED:
            return accounting_tax_rate_deleted()
        if self is AccountingEventType.ACCOUNTING_BILL_CREATED:
            return accounting_bill_created()
        if self is AccountingEventType.ACCOUNTING_BILL_UPDATED:
            return accounting_bill_updated()
        if self is AccountingEventType.ACCOUNTING_BILL_DELETED:
            return accounting_bill_deleted()
        if self is AccountingEventType.ACCOUNTING_PAYMENT_CREATED:
            return accounting_payment_created()
        if self is AccountingEventType.ACCOUNTING_PAYMENT_UPDATED:
            return accounting_payment_updated()
        if self is AccountingEventType.ACCOUNTING_PAYMENT_DELETED:
            return accounting_payment_deleted()
        if self is AccountingEventType.ACCOUNTING_SUPPLIER_CREATED:
            return accounting_supplier_created()
        if self is AccountingEventType.ACCOUNTING_SUPPLIER_UPDATED:
            return accounting_supplier_updated()
        if self is AccountingEventType.ACCOUNTING_SUPPLIER_DELETED:
            return accounting_supplier_deleted()
