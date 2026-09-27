

import typing

from ...types.payment import Payment
from ...types.payment_aggregate import PaymentAggregate

GetPaymentsV3Response = typing.Union[typing.List[Payment], typing.List[PaymentAggregate]]
