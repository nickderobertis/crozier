

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DlqEvent(UniversalBaseModel):
    """
    One staged-but-not-yet-drained lineage event in the transactional outbox (#83 ops view).

    A file's presence in the outbox means "committed write, lineage not yet confirmed delivered" — the
    at-risk set the reconcile relay drains. ``parseable=False`` marks a poison object (the relay would drop
    it): its run_id is the filename, the rest is unknown. A catalog DDL change (a ``DatasetEvent``) names no
    run, so it lists under its staged key too, with its event time and dataset but no type, job or inputs.
    """

    event_time: typing.Optional[str] = None
    event_type: typing.Optional[str] = None
    inputs: typing.Optional[typing.List[str]] = None
    job: typing.Optional[str] = None
    outputs: typing.Optional[typing.List[str]] = None
    parseable: typing.Optional[bool] = None
    run_id: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
