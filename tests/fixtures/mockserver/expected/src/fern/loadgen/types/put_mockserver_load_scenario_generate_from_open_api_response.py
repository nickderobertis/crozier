

from __future__ import annotations

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ...types.load_scenario import LoadScenario
from .put_mockserver_load_scenario_generate_from_open_api_response_state import (
    PutMockserverLoadScenarioGenerateFromOpenApiResponseState,
)
from .put_mockserver_load_scenario_generate_from_open_api_response_status import (
    PutMockserverLoadScenarioGenerateFromOpenApiResponseStatus,
)


class PutMockserverLoadScenarioGenerateFromOpenApiResponse(UniversalBaseModel):
    status: typing.Optional[PutMockserverLoadScenarioGenerateFromOpenApiResponseStatus] = None
    name: typing.Optional[str] = None
    state: typing.Optional[PutMockserverLoadScenarioGenerateFromOpenApiResponseState] = None
    scenario: typing.Optional[LoadScenario] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(PutMockserverLoadScenarioGenerateFromOpenApiResponse)
