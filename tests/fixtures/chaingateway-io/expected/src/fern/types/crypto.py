

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .cipherparams import Cipherparams
from .kdfparams import Kdfparams


class Crypto(UniversalBaseModel):
    cipher: str
    cipherparams: Cipherparams
    ciphertext: str
    kdf: str
    kdfparams: Kdfparams
    mac: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
