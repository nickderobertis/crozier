

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .wireless_link_auth_cipher_label import WirelessLinkAuthCipherLabel
from .wireless_link_auth_cipher_value import WirelessLinkAuthCipherValue


class WirelessLinkAuthCipher(UniversalBaseModel):
    label: WirelessLinkAuthCipherLabel
    value: WirelessLinkAuthCipherValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
