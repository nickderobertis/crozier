

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CapsuleManifest(UniversalBaseModel):
    spec_version: str
    run_id: str
    run_fingerprint: str = pydantic.Field()
    """
    Deterministic hash of the event log
    """

    registry_snapshot_hash: typing.Optional[str] = None
    pack: typing.Optional[typing.Dict[str, typing.Any]] = None
    policy: typing.Optional[typing.Dict[str, typing.Any]] = None
    federation_path: typing.Optional[typing.List[str]] = None
    trust_scores: typing.Optional[typing.Dict[str, float]] = None
    audit_root: typing.Optional[str] = None
    environment: typing.Optional[typing.Dict[str, str]] = None
    created_at: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
