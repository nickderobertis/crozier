

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DestinyMiscDestinyColor(UniversalBaseModel):
    """
    Represents a color whose RGBA values are all represented as values between 0 and 255.
    """

    alpha: typing.Optional[str] = None
    blue: typing.Optional[str] = None
    green: typing.Optional[str] = None
    red: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
