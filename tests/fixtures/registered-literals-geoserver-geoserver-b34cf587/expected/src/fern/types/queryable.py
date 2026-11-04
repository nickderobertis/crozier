

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .queryable_type import QueryableType


class Queryable(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    identifier of the attribute that can be used in CQL filters
    """

    type: QueryableType = pydantic.Field()
    """
    the property type
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
