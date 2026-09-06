

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .query_criteria_group_operator import QueryCriteriaGroupOperator
from .query_group_field import QueryGroupField


class QueryCriteriaGroup(UniversalBaseModel):
    """
    An and/or group used for filtering, all items in the group must be the same operator (but an item in the group may be a query criteria subgroup using a different operator)
    """

    operator: typing.Optional[QueryCriteriaGroupOperator] = pydantic.Field(default=None)
    """
    The operator to connect the items in group
    """

    group: typing.Optional[typing.List[QueryGroupField]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
