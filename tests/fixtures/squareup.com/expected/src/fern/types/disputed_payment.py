

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DisputedPayment(UniversalBaseModel):
    """
    The payment the cardholder disputed.
    """

    payment_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Square-generated unique ID of the payment being disputed.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
