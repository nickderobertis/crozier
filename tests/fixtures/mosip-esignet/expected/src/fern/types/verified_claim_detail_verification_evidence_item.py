

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .electronic_record import ElectronicRecord
from .evidence_check_detail import EvidenceCheckDetail
from .filter_criteria import FilterCriteria
from .verified_claim_detail_verification_evidence_item_created_at import (
    VerifiedClaimDetailVerificationEvidenceItemCreatedAt,
)
from .verified_claim_detail_verification_evidence_item_document_details import (
    VerifiedClaimDetailVerificationEvidenceItemDocumentDetails,
)
from .verified_claim_detail_verification_evidence_item_time import VerifiedClaimDetailVerificationEvidenceItemTime
from .verified_claim_detail_verification_evidence_item_type import VerifiedClaimDetailVerificationEvidenceItemType
from .verified_claim_detail_verification_evidence_item_verification_method import (
    VerifiedClaimDetailVerificationEvidenceItemVerificationMethod,
)


class VerifiedClaimDetailVerificationEvidenceItem(UniversalBaseModel):
    type: VerifiedClaimDetailVerificationEvidenceItemType = pydantic.Field()
    """
    The value defines the type of the evidence.
    """

    method: typing.Optional[FilterCriteria] = pydantic.Field(default=None)
    """
    The method used to validate the document and verify the person is the owner of it.
    """

    time: typing.Optional[VerifiedClaimDetailVerificationEvidenceItemTime] = None
    verification_method: typing.Optional[VerifiedClaimDetailVerificationEvidenceItemVerificationMethod] = None
    check_details: typing.Optional[typing.List[EvidenceCheckDetail]] = pydantic.Field(default=None)
    """
    JSON array representing the checks done in relation to the evidence. When present this array MUST have at least one member. This is applicable only for below evidence types:
    1. document
    2. electronic_record
    3. vouch
    """

    document_details: typing.Optional[VerifiedClaimDetailVerificationEvidenceItemDocumentDetails] = pydantic.Field(
        default=None
    )
    """
     JSON object representing the document used to perform the identity verification.
    """

    attestation: typing.Optional[str] = pydantic.Field(default=None)
    """
    Represents the attestation that is the basis of the vouch. Applicable only when evidence type is `vouch`
    """

    signature_type: typing.Optional[FilterCriteria] = pydantic.Field(default=None)
    """
    Applicable when evidence type is `electronic_signature`. String denoting the type of signature used as evidence. The value range might be restricted by the respective trust framework.
    """

    issuer: typing.Optional[FilterCriteria] = pydantic.Field(default=None)
    """
    Applicable when evidence type is `electronic_signature`.String denoting the certification authority that issued the signer's certificate.
    """

    serial_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    Applicable when evidence type is `electronic_signature`.String containing the serial number of the certificate used to sign.
    """

    created_at: typing.Optional[VerifiedClaimDetailVerificationEvidenceItemCreatedAt] = pydantic.Field(default=None)
    """
    Applicable when evidence type is `electronic_signature`. The time the signature was created
    """

    record: typing.Optional[ElectronicRecord] = pydantic.Field(default=None)
    """
    Applicable when the evidence type is `electronic_record`
    object representing the record used to perform the identity verification.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
