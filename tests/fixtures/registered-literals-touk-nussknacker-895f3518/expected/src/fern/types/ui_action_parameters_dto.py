

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .map_scenario_action_name_list_ui_action_node_parameters_dto import (
    MapScenarioActionNameListUiActionNodeParametersDto,
)


class UiActionParametersDto(UniversalBaseModel):
    action_name_to_parameters: typing_extensions.Annotated[
        MapScenarioActionNameListUiActionNodeParametersDto,
        FieldMetadata(alias="actionNameToParameters"),
        pydantic.Field(alias="actionNameToParameters"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
