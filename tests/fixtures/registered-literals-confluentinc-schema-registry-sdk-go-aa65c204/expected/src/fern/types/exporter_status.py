

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .exporter_status_state import ExporterStatusState


class ExporterStatus(UniversalBaseModel):
    name: typing.Optional[str] = None
    state: typing.Optional[ExporterStatusState] = None
    offset: typing.Optional[int] = None
    ts: typing.Optional[int] = None
    trace: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
