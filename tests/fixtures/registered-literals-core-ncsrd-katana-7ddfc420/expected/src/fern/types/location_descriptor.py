

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LocationDescriptor(UniversalBaseModel):
    """
    Descriptor of a registered location
    """

    id: str = pydantic.Field()
    """
    A unique ID for this location
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    A brief description of this location
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
