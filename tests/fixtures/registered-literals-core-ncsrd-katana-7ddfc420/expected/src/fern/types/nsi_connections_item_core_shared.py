

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class NsiConnectionsItemCoreShared(UniversalBaseModel):
    """
    Defines if the function can be shared between different slices
    """

    availability: bool = pydantic.Field()
    """
    true: shared, false: no shared
    """

    max_shared: typing.Optional[float] = pydantic.Field(default=None)
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
