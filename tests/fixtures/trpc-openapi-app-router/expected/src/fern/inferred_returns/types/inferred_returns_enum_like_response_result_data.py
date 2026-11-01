

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .inferred_returns_enum_like_response_result_data_status import InferredReturnsEnumLikeResponseResultDataStatus


class InferredReturnsEnumLikeResponseResultData(UniversalBaseModel):
    status: InferredReturnsEnumLikeResponseResultDataStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
