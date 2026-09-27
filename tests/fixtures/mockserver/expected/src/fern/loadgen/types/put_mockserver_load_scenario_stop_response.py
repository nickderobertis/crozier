

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .put_mockserver_load_scenario_stop_response_status import PutMockserverLoadScenarioStopResponseStatus
from .put_mockserver_load_scenario_stop_response_stopped_item import PutMockserverLoadScenarioStopResponseStoppedItem


class PutMockserverLoadScenarioStopResponse(UniversalBaseModel):
    status: typing.Optional[PutMockserverLoadScenarioStopResponseStatus] = None
    stopped: typing.Optional[typing.List[PutMockserverLoadScenarioStopResponseStoppedItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
