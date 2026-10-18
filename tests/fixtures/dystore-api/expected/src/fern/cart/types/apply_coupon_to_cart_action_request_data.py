

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .apply_coupon_to_cart_action_request_data_attributes import ApplyCouponToCartActionRequestDataAttributes


class ApplyCouponToCartActionRequestData(UniversalBaseModel):
    attributes: typing.Optional[ApplyCouponToCartActionRequestDataAttributes] = None
    type: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
