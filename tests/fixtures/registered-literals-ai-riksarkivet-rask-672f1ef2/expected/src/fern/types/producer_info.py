

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ProducerInfo(UniversalBaseModel):
    """
    A run that wrote (or attempted to write) a dataset — who / when / how / version / measured size.

    A **failed** run (``event_type`` FAIL/ABORT) appears here too, with no
    ``dataset_version`` and an ``error_message`` — it tried but produced no data.

    ``row_count`` / ``size_bytes`` are the runtime-measured output statistics the compute recorded for
    this write (the rows + on-disk bytes it actually produced, from the standard ``outputStatistics``
    facet); ``None`` when the run was a dummy emit (no compute) or a failure (no data produced).

    ``quality_passed`` is the validator gate's verdict (all assertions succeeded) and ``quality_assertions``
    the checks it ran (from the standard ``dataQualityAssertions`` facet); ``quality_passed=False`` with a
    real ``dataset_version`` is the auditable record of a batch the gate blocked from promotion. Both are
    ``None`` / empty when the quality gate did not run.

    ``consumed_from_version`` / ``consumed_to_version`` are the Lance version RANGE this run consumed
    to produce the write, when it pinned one. They ride the per-dataset read so "what has this lane
    consumed?" is a question about the DATASET — a scan of the whole run board answers it only while
    every relevant run is still on the board, which is a property of the data rather than of the code.
    """

    author: typing.Optional[str] = None
    consumed_from_version: typing.Optional[int] = None
    consumed_to_version: typing.Optional[int] = None
    dataset_version: typing.Optional[str] = None
    error_message: typing.Optional[str] = None
    event_time: typing.Optional[str] = None
    event_type: typing.Optional[str] = None
    operation: typing.Optional[str] = None
    producer: typing.Optional[str] = None
    quality_assertions: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = None
    quality_passed: typing.Optional[bool] = None
    row_count: typing.Optional[int] = None
    run_id: str
    size_bytes: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
