

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_v2vectordb_roles_create_response_data import PostV2VectordbRolesCreateResponseData


class PostV2VectordbRolesCreateResponse(UniversalBaseModel):
    code: int
    data: PostV2VectordbRolesCreateResponseData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
