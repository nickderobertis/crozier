

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.composite_signature import CompositeSignature
from .compact_audit_request_compaction_type import CompactAuditRequestCompactionType


class CompactAuditRequestCompaction(UniversalBaseModel):
    type: CompactAuditRequestCompactionType
    session_nonce: str
    range: typing.Dict[str, typing.Any]
    merkle_root: str
    composite_sig: CompositeSignature

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
