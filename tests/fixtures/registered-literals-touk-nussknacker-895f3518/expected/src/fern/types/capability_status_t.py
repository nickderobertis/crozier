

import typing

from .available_t import AvailableT
from .not_available1 import NotAvailable1

CapabilityStatusT = typing.Union[AvailableT, NotAvailable1]
