

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RefundOrdersResponseStripeCardExpires(UniversalBaseModel):
    """
    The card's expiration date.
    """

    year: typing.Optional[float] = pydantic.Field(default=None)
    """
    Year that the card expires
    """

    month: typing.Optional[float] = pydantic.Field(default=None)
    """
    Month that the card expires
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
