

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .expectation_cross_protocol_scenarios_item_trigger import ExpectationCrossProtocolScenariosItemTrigger


class ExpectationCrossProtocolScenariosItem(UniversalBaseModel):
    trigger: ExpectationCrossProtocolScenariosItemTrigger
    match_pattern: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="matchPattern"), pydantic.Field(alias="matchPattern")
    ] = None
    scenario_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="scenarioName"), pydantic.Field(alias="scenarioName")
    ]
    target_state: typing_extensions.Annotated[
        str, FieldMetadata(alias="targetState"), pydantic.Field(alias="targetState")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
