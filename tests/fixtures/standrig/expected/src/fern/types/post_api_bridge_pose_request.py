

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_api_bridge_pose_request_clear_parameter_values_data import PostApiBridgePoseRequestClearParameterValuesData
from .post_api_bridge_pose_request_set_parameter_values_data import PostApiBridgePoseRequestSetParameterValuesData


class PostApiBridgePoseRequest_SetParameterValues(UniversalBaseModel):
    method: typing.Literal["SetParameterValues"] = "SetParameterValues"
    data: PostApiBridgePoseRequestSetParameterValuesData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PostApiBridgePoseRequest_ClearParameterValues(UniversalBaseModel):
    method: typing.Literal["ClearParameterValues"] = "ClearParameterValues"
    data: PostApiBridgePoseRequestClearParameterValuesData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


PostApiBridgePoseRequest = typing_extensions.Annotated[
    typing.Union[PostApiBridgePoseRequest_SetParameterValues, PostApiBridgePoseRequest_ClearParameterValues],
    pydantic.Field(discriminator="method"),
]
