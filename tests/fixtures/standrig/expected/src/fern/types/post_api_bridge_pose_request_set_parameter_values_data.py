

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .post_api_bridge_pose_request_set_parameter_values_data_parameters_item import (
    PostApiBridgePoseRequestSetParameterValuesDataParametersItem,
)


class PostApiBridgePoseRequestSetParameterValuesData(UniversalBaseModel):
    model_uid: typing_extensions.Annotated[str, FieldMetadata(alias="ModelUID"), pydantic.Field(alias="ModelUID")]
    parameters: typing_extensions.Annotated[
        typing.List[PostApiBridgePoseRequestSetParameterValuesDataParametersItem],
        FieldMetadata(alias="Parameters"),
        pydantic.Field(alias="Parameters"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
