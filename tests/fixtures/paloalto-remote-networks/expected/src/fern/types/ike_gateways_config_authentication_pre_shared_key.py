

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ike_gateways_config_authentication_pre_shared_key_pre_shared_key import (
    IkeGatewaysConfigAuthenticationPreSharedKeyPreSharedKey,
)


class IkeGatewaysConfigAuthenticationPreSharedKey(UniversalBaseModel):
    pre_shared_key: typing.Optional[IkeGatewaysConfigAuthenticationPreSharedKeyPreSharedKey] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
