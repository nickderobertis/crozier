

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .put_v1trace_response_result_item import PutV1TraceResponseResultItem


class PutV1TraceResponse(UniversalBaseModel):
    result: typing.Optional[typing.List[PutV1TraceResponseResultItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
