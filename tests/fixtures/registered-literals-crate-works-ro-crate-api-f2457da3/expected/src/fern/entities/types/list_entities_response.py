

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.entity import Entity


class ListEntitiesResponse(UniversalBaseModel):
    """
    A list of entities based on the provided filters.
    """

    total: int = pydantic.Field()
    """
    Total number of entities (before pagination) that match the query.
    """

    entities: typing.List[Entity]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
