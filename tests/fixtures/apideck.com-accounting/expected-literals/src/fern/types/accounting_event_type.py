

import typing

AccountingEventType = typing.Union[
    typing.Literal[
        "*",
        "accounting.customer.created",
        "accounting.customer.updated",
        "accounting.customer.deleted",
        "accounting.invoice.created",
        "accounting.invoice.updated",
        "accounting.invoice.deleted",
        "accounting.invoice_item.created",
        "accounting.invoice_item.updated",
        "accounting.invoice_item.deleted",
        "accounting.ledger_account.created",
        "accounting.ledger_account.updated",
        "accounting.ledger_account.deleted",
        "accounting.tax_rate.created",
        "accounting.tax_rate.updated",
        "accounting.tax_rate.deleted",
        "accounting.bill.created",
        "accounting.bill.updated",
        "accounting.bill.deleted",
        "accounting.payment.created",
        "accounting.payment.updated",
        "accounting.payment.deleted",
        "accounting.supplier.created",
        "accounting.supplier.updated",
        "accounting.supplier.deleted",
    ],
    typing.Any,
]
