

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_params_unexploded_object_query_response_filter import GetParamsUnexplodedObjectQueryResponseFilter


class GetParamsUnexplodedObjectQueryResponse(UniversalBaseModel):
    filter: GetParamsUnexplodedObjectQueryResponseFilter

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
