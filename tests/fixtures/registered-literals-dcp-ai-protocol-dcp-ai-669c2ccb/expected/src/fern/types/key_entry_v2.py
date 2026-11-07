

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .key_entry_v2alg import KeyEntryV2Alg
from .key_entry_v2status import KeyEntryV2Status


class KeyEntryV2(UniversalBaseModel):
    kid: typing.Optional[str] = None
    alg: typing.Optional[KeyEntryV2Alg] = None
    public_key_b64: typing.Optional[str] = None
    created_at: typing.Optional[dt.datetime] = None
    expires_at: typing.Optional[dt.datetime] = None
    status: typing.Optional[KeyEntryV2Status] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
