

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_v2vectordb_aliases_alter_response_data import PostV2VectordbAliasesAlterResponseData


class PostV2VectordbAliasesAlterResponse(UniversalBaseModel):
    code: int
    data: PostV2VectordbAliasesAlterResponseData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
