

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .secret import Secret


class BaseTotpConfig(UniversalBaseModel):
    enabled: typing.Optional[bool] = None
    config_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    This name must be defined within the "totp" section of the SFTPGo configuration file. You will be unable to save a user/admin referencing a missing config_name
    """

    secret: typing.Optional[Secret] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
