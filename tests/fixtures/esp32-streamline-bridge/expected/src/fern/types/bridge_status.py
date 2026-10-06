

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .source_snapshot import SourceSnapshot
from .transport_snapshot import TransportSnapshot


class BridgeStatus(UniversalBaseModel):
    api_token_configured: bool
    bridge_version: str
    public_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Player-accessible HTTP base URL. Empty means no advertised address is configured.
    """

    sources: typing.Dict[str, SourceSnapshot]
    transport: TransportSnapshot

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
