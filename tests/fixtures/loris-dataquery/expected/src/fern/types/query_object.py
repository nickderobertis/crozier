

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .query_criteria_group import QueryCriteriaGroup
from .query_field import QueryField
from .query_object_type import QueryObjectType


class QueryObject(UniversalBaseModel):
    """
    A set of filters and fields used to determine what is being queried.
    """

    type: QueryObjectType
    fields: typing.List[QueryField]
    criteria: typing.Optional[QueryCriteriaGroup] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
