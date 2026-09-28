

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PutMockserverScenarioNameResponse(UniversalBaseModel):
    scenario_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="scenarioName"), pydantic.Field(alias="scenarioName")
    ] = None
    current_state: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="currentState"), pydantic.Field(alias="currentState")
    ] = None
    next_state: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="nextState"), pydantic.Field(alias="nextState")
    ] = None
    transition_after_ms: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="transitionAfterMs"), pydantic.Field(alias="transitionAfterMs")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
