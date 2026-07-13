

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class InstallationServerPublicKey(UniversalBaseModel):
    server_public_key: typing.Optional[str] = pydantic.Field(default=None)
    """
    The server's public key for this Installation. You should use this key to verify the "X-Bunq-Server-Signature" header for each response from the server.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
