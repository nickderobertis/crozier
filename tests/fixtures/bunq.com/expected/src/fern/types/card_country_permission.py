

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CardCountryPermission(UniversalBaseModel):
    country: typing.Optional[str] = pydantic.Field(default=None)
    """
    The country to allow transactions in (e.g. NL, DE).
    """

    expiry_time: typing.Optional[str] = pydantic.Field(default=None)
    """
    Expiry time of this rule.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the card country permission entry.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
