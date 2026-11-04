

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ResourcesFunctionsItemShared(UniversalBaseModel):
    """
    Availability to be shared amongst many network slices
    """

    availability: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Available for sharing
    """

    max_shared: typing.Optional[int] = pydantic.Field(default=None)
    """
    Max number of slices - If availability is true and max_shared not defined, it will be assumed unlimited availability
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
