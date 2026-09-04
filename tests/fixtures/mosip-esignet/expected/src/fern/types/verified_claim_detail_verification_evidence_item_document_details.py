

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .evidence_issuer import EvidenceIssuer
from .filter_criteria import FilterCriteria
from .verified_claim_detail_verification_evidence_item_document_details_date_of_expiry import (
    VerifiedClaimDetailVerificationEvidenceItemDocumentDetailsDateOfExpiry,
)
from .verified_claim_detail_verification_evidence_item_document_details_date_of_issuance import (
    VerifiedClaimDetailVerificationEvidenceItemDocumentDetailsDateOfIssuance,
)


class VerifiedClaimDetailVerificationEvidenceItemDocumentDetails(UniversalBaseModel):
    """
    JSON object representing the document used to perform the identity verification.
    """

    type: FilterCriteria
    document_number: typing.Optional[str] = None
    date_of_issuance: typing.Optional[VerifiedClaimDetailVerificationEvidenceItemDocumentDetailsDateOfIssuance] = None
    date_of_expiry: typing.Optional[VerifiedClaimDetailVerificationEvidenceItemDocumentDetailsDateOfExpiry] = None
    issuer: typing.Optional[EvidenceIssuer] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
