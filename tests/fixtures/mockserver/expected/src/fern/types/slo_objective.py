

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .slo_objective_comparator import SloObjectiveComparator
from .slo_objective_scope import SloObjectiveScope
from .slo_objective_sli import SloObjectiveSli


class SloObjective(UniversalBaseModel):
    """
    a single service-level objective over the recorded SLI samples
    """

    sli: SloObjectiveSli = pydantic.Field()
    """
    the service-level indicator to evaluate
    """

    comparator: SloObjectiveComparator = pydantic.Field()
    """
    how the observed value is compared to the threshold
    """

    threshold: float = pydantic.Field()
    """
    the objective threshold (milliseconds for latency SLIs, a 0.0-1.0 fraction for ERROR_RATE)
    """

    scope: typing.Optional[SloObjectiveScope] = pydantic.Field(default=None)
    """
    which recorded traffic to evaluate; v1 records only FORWARD (proxied/forwarded upstream) samples
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
