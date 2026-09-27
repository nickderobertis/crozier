

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_mockserver_scenario_response_scenarios_item import GetMockserverScenarioResponseScenariosItem


class GetMockserverScenarioResponse(UniversalBaseModel):
    scenarios: typing.Optional[typing.List[GetMockserverScenarioResponseScenariosItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
