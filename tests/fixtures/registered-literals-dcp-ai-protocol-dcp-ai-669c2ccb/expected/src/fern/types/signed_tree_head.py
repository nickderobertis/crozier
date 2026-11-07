

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SignedTreeHead(UniversalBaseModel):
    root: typing.Optional[str] = pydantic.Field(default=None)
    """
    Hex-encoded SHA-256 Merkle root (null if log is empty).
    """

    size: int
    timestamp: dt.datetime
    log_id: str
    signature: str = pydantic.Field()
    """
    HMAC-SHA256 signature over the STH payload, base64-encoded.
    """

    public_key: str = pydantic.Field()
    """
    Hex-encoded SHA-256 hash of the operator key (for verification).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
