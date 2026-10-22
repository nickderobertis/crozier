

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .sync_keychain import SyncKeychain
from .sync_strategy import SyncStrategy


class SyncOptions(UniversalBaseModel):
    keychain: SyncKeychain
    strategy: SyncStrategy

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
