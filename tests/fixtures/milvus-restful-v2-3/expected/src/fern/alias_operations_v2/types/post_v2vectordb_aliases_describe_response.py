

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.alias_detail import AliasDetail
from ...types.http_return_code import HttpReturnCode


class PostV2VectordbAliasesDescribeResponse(UniversalBaseModel):
    code: HttpReturnCode
    data: AliasDetail

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
