

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BunqMeMerchantAvailable(UniversalBaseModel):
    available: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not the merchant is available for the user.
    """

    merchant_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    A merchant type supported by bunq.me.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
