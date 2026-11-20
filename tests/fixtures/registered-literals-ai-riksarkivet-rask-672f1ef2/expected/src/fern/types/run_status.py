

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RunStatus(UniversalBaseModel):
    """
    The *current* status of a run, folded from its OpenLineage lifecycle events.

    Unlike the provenance graph (terminal-only), this is the live "where are we now" view:
    ``state`` is the latest run state (START→RUNNING→COMPLETE/FAIL), with progress + error.
    """

    attempts: typing.Optional[int] = None
    author: typing.Optional[str] = None
    cascade_id: typing.Optional[str] = None
    consumed_from_version: typing.Optional[int] = None
    consumed_to_version: typing.Optional[int] = None
    error_message: typing.Optional[str] = None
    events: typing.Optional[int] = None
    job: typing.Optional[str] = None
    operation: typing.Optional[str] = None
    outputs: typing.Optional[typing.List[str]] = None
    progress_done: typing.Optional[int] = None
    progress_total: typing.Optional[int] = None
    promotion_status: typing.Optional[str] = None
    run_id: str
    source_run_id: typing.Optional[str] = None
    started_at: typing.Optional[str] = None
    state: typing.Optional[str] = None
    updated_at: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
