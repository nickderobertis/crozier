

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_client_workspace_id_storage_response_data import PostClientWorkspaceIdStorageResponseData


class PostClientWorkspaceIdStorageResponse(UniversalBaseModel):
    data: typing.Optional[PostClientWorkspaceIdStorageResponseData] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
