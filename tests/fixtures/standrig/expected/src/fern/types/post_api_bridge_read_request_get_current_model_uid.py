

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_api_bridge_read_request_get_current_model_uid_data import PostApiBridgeReadRequestGetCurrentModelUidData


class PostApiBridgeReadRequestGetCurrentModelUid(UniversalBaseModel):
    data: PostApiBridgeReadRequestGetCurrentModelUidData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
