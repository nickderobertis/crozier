

from __future__ import annotations

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ...types.load_scenario import LoadScenario
from .put_mockserver_load_scenario_generate_from_recording_response_state import (
    PutMockserverLoadScenarioGenerateFromRecordingResponseState,
)
from .put_mockserver_load_scenario_generate_from_recording_response_status import (
    PutMockserverLoadScenarioGenerateFromRecordingResponseStatus,
)


class PutMockserverLoadScenarioGenerateFromRecordingResponse(UniversalBaseModel):
    status: typing.Optional[PutMockserverLoadScenarioGenerateFromRecordingResponseStatus] = None
    name: typing.Optional[str] = None
    state: typing.Optional[PutMockserverLoadScenarioGenerateFromRecordingResponseState] = None
    scenario: typing.Optional[LoadScenario] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(PutMockserverLoadScenarioGenerateFromRecordingResponse)
