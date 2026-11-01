

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_api_v3axissections_response_data import GetApiV3AxissectionsResponseData


class GetApiV3AxissectionsResponse(UniversalBaseModel):
    data: typing.Optional[GetApiV3AxissectionsResponseData] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
