

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_signatures_complete200response_protection_certification import (
    DocSignaturesComplete200ResponseProtectionCertification,
)
from .doc_signatures_complete200response_protection_enforced import DocSignaturesComplete200ResponseProtectionEnforced
from .doc_signatures_complete200response_protection_field_locks_item import (
    DocSignaturesComplete200ResponseProtectionFieldLocksItem,
)
from .doc_signatures_complete200response_protection_judged import DocSignaturesComplete200ResponseProtectionJudged


class DocSignaturesComplete200ResponseProtection(UniversalBaseModel):
    enforced: typing.Optional[DocSignaturesComplete200ResponseProtectionEnforced] = None
    judged: typing.Optional[DocSignaturesComplete200ResponseProtectionJudged] = None
    certification: typing.Optional[DocSignaturesComplete200ResponseProtectionCertification] = None
    field_locks: typing_extensions.Annotated[
        typing.List[DocSignaturesComplete200ResponseProtectionFieldLocksItem],
        FieldMetadata(alias="fieldLocks"),
        pydantic.Field(alias="fieldLocks"),
    ]
    policy_version: typing_extensions.Annotated[
        int, FieldMetadata(alias="policyVersion"), pydantic.Field(alias="policyVersion")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
