

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .put_mockserver_load_scenario_start_response_started_item_state import (
    PutMockserverLoadScenarioStartResponseStartedItemState,
)


class PutMockserverLoadScenarioStartResponseStartedItem(UniversalBaseModel):
    name: typing.Optional[str] = None
    state: typing.Optional[PutMockserverLoadScenarioStartResponseStartedItemState] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
