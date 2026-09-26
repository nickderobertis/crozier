

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_versions_signatures200response_protection_certification import (
    DocVersionsSignatures200ResponseProtectionCertification,
)
from .doc_versions_signatures200response_protection_enforced import DocVersionsSignatures200ResponseProtectionEnforced
from .doc_versions_signatures200response_protection_field_locks_item import (
    DocVersionsSignatures200ResponseProtectionFieldLocksItem,
)
from .doc_versions_signatures200response_protection_judged import DocVersionsSignatures200ResponseProtectionJudged


class DocVersionsSignatures200ResponseProtection(UniversalBaseModel):
    enforced: typing.Optional[DocVersionsSignatures200ResponseProtectionEnforced] = None
    judged: typing.Optional[DocVersionsSignatures200ResponseProtectionJudged] = None
    certification: typing.Optional[DocVersionsSignatures200ResponseProtectionCertification] = None
    field_locks: typing_extensions.Annotated[
        typing.List[DocVersionsSignatures200ResponseProtectionFieldLocksItem],
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
