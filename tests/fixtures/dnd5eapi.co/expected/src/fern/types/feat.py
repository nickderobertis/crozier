

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .api_reference import ApiReference
from .prerequisite import Prerequisite
from .resource_description import ResourceDescription


class Feat(ApiReference, ResourceDescription):
    """
    `Feat`
    """

    prerequisites: typing.Optional[typing.List[Prerequisite]] = pydantic.Field(default=None)
    """
    An object of APIReferences to ability scores and minimum scores.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
