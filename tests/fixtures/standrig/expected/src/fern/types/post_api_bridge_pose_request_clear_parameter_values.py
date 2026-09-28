

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_api_bridge_pose_request_clear_parameter_values_data import PostApiBridgePoseRequestClearParameterValuesData


class PostApiBridgePoseRequestClearParameterValues(UniversalBaseModel):
    data: PostApiBridgePoseRequestClearParameterValuesData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
