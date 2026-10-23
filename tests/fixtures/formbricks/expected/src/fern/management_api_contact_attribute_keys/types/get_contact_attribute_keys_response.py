

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_contact_attribute_keys_response_data_item import GetContactAttributeKeysResponseDataItem
from .get_contact_attribute_keys_response_meta import GetContactAttributeKeysResponseMeta


class GetContactAttributeKeysResponse(UniversalBaseModel):
    data: typing.Optional[typing.List[GetContactAttributeKeysResponseDataItem]] = None
    meta: typing.Optional[GetContactAttributeKeysResponseMeta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
