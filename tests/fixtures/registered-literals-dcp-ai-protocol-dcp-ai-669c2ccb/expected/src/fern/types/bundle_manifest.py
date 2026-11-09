

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BundleManifest(UniversalBaseModel):
    session_nonce: str
    rpr_hash: str
    passport_hash: str
    intent_hash: str
    policy_hash: str
    audit_merkle_root: str
    audit_merkle_root_secondary: typing.Optional[str] = None
    audit_count: int
    pq_checkpoints: typing.Optional[typing.List[str]] = None
    session_expires_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    ISO 8601 timestamp after which this session/bundle is expired.
    """

    intended_verifier: typing.Optional[str] = pydantic.Field(default=None)
    """
    Audience binding — identifier of the intended verifier to prevent relay attacks.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
