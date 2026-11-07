

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.key_entry_v2 import KeyEntryV2


class LookupKeyResponse(UniversalBaseModel):
    found: typing.Optional[bool] = None
    kid: typing.Optional[str] = None
    key: typing.Optional[KeyEntryV2] = None
    agent_id: typing.Optional[str] = None
    revoked: typing.Optional[bool] = None
    expired: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
