

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ssh_authentications import SshAuthentications
from .ssh_binding import SshBinding
from .ssh_host_key import SshHostKey


class SshServiceStatus(UniversalBaseModel):
    is_active: typing.Optional[bool] = None
    bindings: typing.Optional[typing.List[SshBinding]] = None
    host_keys: typing.Optional[typing.List[SshHostKey]] = None
    ssh_commands: typing.Optional[typing.List[str]] = None
    authentications: typing.Optional[typing.List[SshAuthentications]] = None
    public_key_algorithms: typing.Optional[typing.List[str]] = None
    macs: typing.Optional[typing.List[str]] = None
    kex_algorithms: typing.Optional[typing.List[str]] = None
    ciphers: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
