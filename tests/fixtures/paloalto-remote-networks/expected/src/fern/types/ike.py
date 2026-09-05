

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ike_advanced import IkeAdvanced
from .ike_authentication import IkeAuthentication
from .ike_crypto import IkeCrypto
from .ike_local_id import IkeLocalId
from .ike_peer_address import IkePeerAddress
from .ike_peer_id import IkePeerId
from .ike_version import IkeVersion


class Ike(UniversalBaseModel):
    advanced: typing.Optional[IkeAdvanced] = None
    authentication: IkeAuthentication
    crypto: IkeCrypto
    local_id: typing.Optional[IkeLocalId] = None
    peer_address: IkePeerAddress
    peer_id: typing.Optional[IkePeerId] = None
    version: typing.Optional[IkeVersion] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
