

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .map_ui_action_parameter_config_dto import MapUiActionParameterConfigDto


class UiActionNodeParametersDto(UniversalBaseModel):
    node_id: typing_extensions.Annotated[str, FieldMetadata(alias="nodeId"), pydantic.Field(alias="nodeId")]
    component_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="componentId"), pydantic.Field(alias="componentId")
    ]
    parameters: MapUiActionParameterConfigDto

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
