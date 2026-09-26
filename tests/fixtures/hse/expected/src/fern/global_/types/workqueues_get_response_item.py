

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .workqueues_get_response_item_state import WorkqueuesGetResponseItemState


class WorkqueuesGetResponseItem(UniversalBaseModel):
    """
    Refer to /proc/[pid]/stat.
    """

    name: typing.Optional[str] = None
    references: typing.Optional[int] = None
    minimum_threads: typing.Optional[int] = None
    maximum_threads: typing.Optional[int] = None
    current_threads: typing.Optional[int] = None
    busy: typing.Optional[int] = None
    working: typing.Optional[int] = None
    delayed: typing.Optional[int] = None
    barrier_id: typing.Optional[int] = None
    calls: typing.Optional[int] = None
    latency_ns: typing.Optional[int] = None
    wmesg: typing.Optional[str] = None
    state: typing.Optional[WorkqueuesGetResponseItemState] = None
    processor: typing.Optional[int] = None
    time: typing.Optional[str] = None
    thread_id: typing.Optional[int] = None
    thread_name: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
