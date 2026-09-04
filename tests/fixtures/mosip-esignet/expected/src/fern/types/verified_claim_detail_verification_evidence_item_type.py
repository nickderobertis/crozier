

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .verified_claim_detail_verification_evidence_item_type_value import (
    VerifiedClaimDetailVerificationEvidenceItemTypeValue,
)


class VerifiedClaimDetailVerificationEvidenceItemType(UniversalBaseModel):
    """
    The value defines the type of the evidence.
    """

    value: typing.Optional[VerifiedClaimDetailVerificationEvidenceItemTypeValue] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
