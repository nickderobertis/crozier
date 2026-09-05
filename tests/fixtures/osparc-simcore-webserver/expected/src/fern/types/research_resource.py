

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ResearchResource(UniversalBaseModel):
    rrid: str = pydantic.Field()
    """
    Unique identifier used as classifier, i.e. to tag studies and services
    """

    name: str
    description: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
