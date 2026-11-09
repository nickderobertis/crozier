

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .json_node import JsonNode


class EntityChangesDto(UniversalBaseModel):
    before: typing.Optional[JsonNode] = pydantic.Field(default=None)
    """
    Entity before changes
    """

    after: typing.Optional[JsonNode] = pydantic.Field(default=None)
    """
    Entity after changes
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
