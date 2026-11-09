

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .trace_with_details import TraceWithDetails
from .utils_meta_response import UtilsMetaResponse


class Traces(UniversalBaseModel):
    data: typing.List[TraceWithDetails]
    meta: UtilsMetaResponse

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
