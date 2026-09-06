

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .totp_config import TotpConfig


class MfaStatus(UniversalBaseModel):
    is_active: typing.Optional[bool] = None
    totp_configs: typing.Optional[typing.List[TotpConfig]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
