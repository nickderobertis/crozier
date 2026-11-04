

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_account_properties_response_data_item import GetAccountPropertiesResponseDataItem
from .get_account_properties_response_meta import GetAccountPropertiesResponseMeta


class GetAccountPropertiesResponse(UniversalBaseModel):
    meta: GetAccountPropertiesResponseMeta
    data: typing.List[GetAccountPropertiesResponseDataItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
