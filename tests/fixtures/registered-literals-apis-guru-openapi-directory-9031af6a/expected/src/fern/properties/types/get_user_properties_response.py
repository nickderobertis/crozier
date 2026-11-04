

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_user_properties_response_data_item import GetUserPropertiesResponseDataItem
from .get_user_properties_response_meta import GetUserPropertiesResponseMeta


class GetUserPropertiesResponse(UniversalBaseModel):
    meta: GetUserPropertiesResponseMeta
    data: typing.List[GetUserPropertiesResponseDataItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
