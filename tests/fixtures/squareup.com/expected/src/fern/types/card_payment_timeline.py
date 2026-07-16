

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CardPaymentTimeline(UniversalBaseModel):
    """
    The timeline for card payments.
    """

    authorized_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp when the payment was authorized, in RFC 3339 format.
    """

    captured_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp when the payment was captured, in RFC 3339 format.
    """

    voided_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp when the payment was voided, in RFC 3339 format.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
