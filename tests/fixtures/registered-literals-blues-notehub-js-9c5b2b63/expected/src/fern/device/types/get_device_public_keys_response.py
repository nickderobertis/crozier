

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_device_public_keys_response_device_public_keys_item import GetDevicePublicKeysResponseDevicePublicKeysItem


class GetDevicePublicKeysResponse(UniversalBaseModel):
    device_public_keys: typing.List[GetDevicePublicKeysResponseDevicePublicKeysItem]
    has_more: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
