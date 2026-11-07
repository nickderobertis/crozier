

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BaseSliceDesPositionalSupport(UniversalBaseModel):
    """
    This attribute describes if the network slice provides geo-localization methods or supporting methods.
    """

    availability: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    Describes if this attribute is provided by the network slice and contains a list of positioning methods provided by the slice.
    """

    frequency: typing.Optional[int] = pydantic.Field(default=None)
    """
    Seconds
    """

    accuracy: typing.Optional[int] = pydantic.Field(default=None)
    """
    Meters
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
