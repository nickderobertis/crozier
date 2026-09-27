

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_api_bridge_pose_request_set_parameter_values_data import PostApiBridgePoseRequestSetParameterValuesData


class PostApiBridgePoseRequestSetParameterValues(UniversalBaseModel):
    data: PostApiBridgePoseRequestSetParameterValuesData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
