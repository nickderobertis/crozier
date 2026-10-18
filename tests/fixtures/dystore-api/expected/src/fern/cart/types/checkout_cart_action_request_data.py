

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .checkout_cart_action_request_data_attributes import CheckoutCartActionRequestDataAttributes


class CheckoutCartActionRequestData(UniversalBaseModel):
    attributes: typing.Optional[CheckoutCartActionRequestDataAttributes] = None
    type: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
