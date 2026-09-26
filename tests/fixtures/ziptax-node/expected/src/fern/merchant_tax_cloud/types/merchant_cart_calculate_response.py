

import typing

from ...types.cart_calculate_response_body import CartCalculateResponseBody
from ...types.self_managed_cart_calculate_response_body import SelfManagedCartCalculateResponseBody

MerchantCartCalculateResponse = typing.Union[CartCalculateResponseBody, SelfManagedCartCalculateResponseBody]
