

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .put_mockserver_load_scenario_start_response_started_item import PutMockserverLoadScenarioStartResponseStartedItem
from .put_mockserver_load_scenario_start_response_status import PutMockserverLoadScenarioStartResponseStatus


class PutMockserverLoadScenarioStartResponse(UniversalBaseModel):
    status: typing.Optional[PutMockserverLoadScenarioStartResponseStatus] = None
    started: typing.Optional[typing.List[PutMockserverLoadScenarioStartResponseStartedItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
