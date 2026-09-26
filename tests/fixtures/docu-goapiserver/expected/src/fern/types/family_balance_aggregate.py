

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .family_balance_aggregate_group import FamilyBalanceAggregateGroup
from .family_balance_aggregate_metrics import FamilyBalanceAggregateMetrics


class FamilyBalanceAggregate(UniversalBaseModel):
    """
    Contains the selected grouping key and requested metrics only. Grouping keys are nested under group; metric values are nested under metrics.
    """

    group: FamilyBalanceAggregateGroup
    metrics: FamilyBalanceAggregateMetrics

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
