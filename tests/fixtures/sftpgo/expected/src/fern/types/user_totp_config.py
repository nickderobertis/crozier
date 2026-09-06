

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .base_totp_config import BaseTotpConfig
from .mfa_protocols import MfaProtocols


class UserTotpConfig(BaseTotpConfig):
    protocols: typing.Optional[typing.List[MfaProtocols]] = pydantic.Field(default=None)
    """
    TOTP will be required for the specified protocols. SSH protocol (SFTP/SCP/SSH commands) will ask for the TOTP passcode if the client uses keyboard interactive authentication. FTP has no standard way to support two factor authentication, if you enable the FTP support, you have to add the TOTP passcode after the password. For example if your password is "password" and your one time passcode is "123456" you have to use "password123456" as password. WebDAV is not supported since each single request must be authenticated and a passcode cannot be reused.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
