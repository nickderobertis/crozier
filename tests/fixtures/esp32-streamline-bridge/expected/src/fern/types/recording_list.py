

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .recording_snapshot import RecordingSnapshot
from .recording_storage import RecordingStorage


class RecordingList(UniversalBaseModel):
    active: typing.List[RecordingSnapshot]
    saved: typing.List[RecordingSnapshot]
    storage: RecordingStorage

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
