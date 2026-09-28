

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .put_mockserver_load_scenario_response_state import PutMockserverLoadScenarioResponseState
from .put_mockserver_load_scenario_response_status import PutMockserverLoadScenarioResponseStatus


class PutMockserverLoadScenarioResponse(UniversalBaseModel):
    status: typing.Optional[PutMockserverLoadScenarioResponseStatus] = None
    name: typing.Optional[str] = None
    state: typing.Optional[PutMockserverLoadScenarioResponseState] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
