

import typing

from .customer_invoice_status_five import CustomerInvoiceStatusFive
from .customer_invoice_status_four import CustomerInvoiceStatusFour
from .customer_invoice_status_one import CustomerInvoiceStatusOne
from .customer_invoice_status_three import CustomerInvoiceStatusThree
from .customer_invoice_status_two import CustomerInvoiceStatusTwo
from .customer_invoice_status_zero import CustomerInvoiceStatusZero

CustomerInvoiceStatus = typing.Union[
    CustomerInvoiceStatusZero,
    CustomerInvoiceStatusOne,
    CustomerInvoiceStatusTwo,
    CustomerInvoiceStatusThree,
    CustomerInvoiceStatusFour,
    CustomerInvoiceStatusFive,
]
