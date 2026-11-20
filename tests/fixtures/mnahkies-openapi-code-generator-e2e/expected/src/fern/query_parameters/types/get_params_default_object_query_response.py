

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_params_default_object_query_response_filter import GetParamsDefaultObjectQueryResponseFilter


class GetParamsDefaultObjectQueryResponse(UniversalBaseModel):
    filter: GetParamsDefaultObjectQueryResponseFilter

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
