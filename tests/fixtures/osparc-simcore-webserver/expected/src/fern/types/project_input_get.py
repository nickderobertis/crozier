

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ProjectInputGet(UniversalBaseModel):
    key: str = pydantic.Field()
    """
    Project port's unique identifier. Same as the UUID of the associated port node
    """

    value: typing.Any
    label: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
