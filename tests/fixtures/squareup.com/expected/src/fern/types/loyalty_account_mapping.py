

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LoyaltyAccountMapping(UniversalBaseModel):
    """
    Represents the mapping that associates a loyalty account with a buyer.

    Currently, a loyalty account can only be mapped to a buyer by phone number. For more information, see
    [Loyalty Overview](https://developer.squareup.com/docs/loyalty/overview).
    """

    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp when the mapping was created, in RFC 3339 format.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Square-assigned ID of the mapping.
    """

    phone_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    The phone number of the buyer, in E.164 format. For example, "+14155551111".
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
