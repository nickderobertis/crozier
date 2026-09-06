

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .secret import Secret


class SftpFsConfig(UniversalBaseModel):
    endpoint: typing.Optional[str] = pydantic.Field(default=None)
    """
    remote SFTP endpoint as host:port
    """

    username: typing.Optional[str] = pydantic.Field(default=None)
    """
    you can specify a password or private key or both. In the latter case the private key will be tried first.
    """

    password: typing.Optional[Secret] = None
    private_key: typing.Optional[Secret] = None
    key_passphrase: typing.Optional[Secret] = None
    fingerprints: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    SHA256 fingerprints to use for host key verification. If you don't provide any fingerprint the remote host key will not be verified, this is a security risk
    """

    prefix: typing.Optional[str] = pydantic.Field(default=None)
    """
    Specifying a prefix you can restrict all operations to a given path within the remote SFTP server.
    """

    disable_concurrent_reads: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Concurrent reads are safe to use and disabling them will degrade performance. Some servers automatically delete files once they are downloaded. Using concurrent reads is problematic with such servers.
    """

    buffer_size: typing.Optional[int] = pydantic.Field(default=None)
    """
    The size of the buffer (in MB) to use for transfers. By enabling buffering, the reads and writes, from/to the remote SFTP server, are split in multiple concurrent requests and this allows data to be transferred at a faster rate, over high latency networks, by overlapping round-trip times. With buffering enabled, resuming uploads is not supported and a file cannot be opened for both reading and writing at the same time. 0 means disabled.
    """

    equality_check_mode: typing.Optional[int] = pydantic.Field(default=None)
    """
    Defines how to check if this config points to the same server as another config. If different configs point to the same server the renaming between the fs configs is allowed:
     * `0` username and endpoint must match. This is the default
     * `1` only the endpoint must match
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
