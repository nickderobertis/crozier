

import typing

from .customer_invoice_type_one import CustomerInvoiceTypeOne
from .customer_invoice_type_two import CustomerInvoiceTypeTwo
from .customer_invoice_type_zero import CustomerInvoiceTypeZero

CustomerInvoiceType = typing.Union[CustomerInvoiceTypeZero, CustomerInvoiceTypeOne, CustomerInvoiceTypeTwo]
