

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_api_shards_upload_response_shard import PostApiShardsUploadResponseShard
from .post_api_shards_upload_response_version import PostApiShardsUploadResponseVersion


class PostApiShardsUploadResponse(UniversalBaseModel):
    message: typing.Optional[str] = None
    shard: typing.Optional[PostApiShardsUploadResponseShard] = None
    version: typing.Optional[PostApiShardsUploadResponseVersion] = None
    checksum: typing.Optional[str] = pydantic.Field(default=None)
    """
    SHA256 checksum of uploaded package
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
