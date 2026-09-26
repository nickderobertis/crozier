

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.http_return_code import HttpReturnCode
from ...types.index_detail import IndexDetail


class PostV2VectordbIndexesDescribeResponse(UniversalBaseModel):
    code: HttpReturnCode
    data: typing.List[IndexDetail]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
