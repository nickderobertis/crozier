

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .load_threshold_comparator import LoadThresholdComparator
from .load_threshold_metric import LoadThresholdMetric


class LoadThreshold(UniversalBaseModel):
    """
    an in-run pass/fail threshold for a load scenario: a per-run metric compared against a value. All thresholds must hold for the run verdict to be PASS (logical AND); any breach makes the verdict FAIL. Evaluated from this run's own latency histogram and counters, not the global SLO sample store.
    """

    metric: LoadThresholdMetric = pydantic.Field()
    """
    the per-run metric to evaluate: latency percentiles in milliseconds, ERROR_RATE as a 0.0-1.0 fraction, THROUGHPUT_RPS as requests/second over the run's elapsed time, CHECK_FAILURE_RATE as failed per-step checks as a 0.0-1.0 fraction of all evaluated checks (0 when no checks ran)
    """

    comparator: LoadThresholdComparator = pydantic.Field()
    """
    how the observed per-run value is compared to the threshold
    """

    threshold: float = pydantic.Field()
    """
    the threshold value (milliseconds for latency metrics, a 0.0-1.0 fraction for ERROR_RATE or CHECK_FAILURE_RATE, requests/second for THROUGHPUT_RPS)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
