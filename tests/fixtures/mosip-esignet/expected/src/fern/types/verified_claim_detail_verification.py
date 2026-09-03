

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .filter_criteria import FilterCriteria
from .verified_claim_detail_verification_evidence_item import VerifiedClaimDetailVerificationEvidenceItem
from .verified_claim_detail_verification_time import VerifiedClaimDetailVerificationTime


class VerifiedClaimDetailVerification(UniversalBaseModel):
    """
    Object that contains data about the verification process.
    """

    trust_framework: FilterCriteria = pydantic.Field()
    """
    String determining the trust framework governing the identity verification process of the OP. An example value is eidas, which denotes a notified eID system under eIDAS 
    """

    time: typing.Optional[VerifiedClaimDetailVerificationTime] = pydantic.Field(default=None)
    """
    Date time when the identity verification process is completed. 
    """

    assurance_level: typing.Optional[FilterCriteria] = pydantic.Field(default=None)
    """
    String determining the assurance level associated with the End-User Claims in the respective verified_claims. The value range depends on the respective trust_framework value.
    
    For example, the trust framework eidas can have the identity assurance levels low, substantial and high.
    """

    evidence: typing.Optional[typing.List[VerifiedClaimDetailVerificationEvidenceItem]] = pydantic.Field(default=None)
    """
    JSON array containing information about the evidence the OP used to verify the End-User's identity as separate JSON objects. Every object contains the property type which determines the type of the evidence. 
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
