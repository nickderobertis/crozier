

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .delete_mockserver_load_scenario_response_status import DeleteMockserverLoadScenarioResponseStatus


class DeleteMockserverLoadScenarioResponse(UniversalBaseModel):
    status: typing.Optional[DeleteMockserverLoadScenarioResponseStatus] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
