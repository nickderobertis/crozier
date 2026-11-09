

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .client_user_id import ClientUserId
from .documentary_verification import DocumentaryVerification
from .identity_verification_id import IdentityVerificationId
from .identity_verification_status import IdentityVerificationStatus
from .identity_verification_step_summary import IdentityVerificationStepSummary
from .identity_verification_template_reference import IdentityVerificationTemplateReference
from .identity_verification_user_data import IdentityVerificationUserData
from .kyc_check_details import KycCheckDetails
from .previous_identity_verification_attempt_id import PreviousIdentityVerificationAttemptId
from .request_id import RequestId
from .risk_check_details import RiskCheckDetails
from .shareable_url import ShareableUrl
from .timestamp import Timestamp
from .timestamp_nullable import TimestampNullable
from .watchlist_screening_individual_id_nullable import WatchlistScreeningIndividualIdNullable


class IdentityVerificationGetResponse(UniversalBaseModel):
    """
    A identity verification attempt represents a customer's attempt to verify their identity, reflecting the required steps for completing the session, the results for each step, and information collected in the process.
    """

    client_user_id: ClientUserId
    completed_at: typing.Optional[TimestampNullable] = None
    created_at: Timestamp
    documentary_verification: typing.Optional[DocumentaryVerification] = None
    id: IdentityVerificationId
    kyc_check: typing.Optional[KycCheckDetails] = None
    previous_attempt_id: typing.Optional[PreviousIdentityVerificationAttemptId] = None
    redacted_at: typing.Optional[TimestampNullable] = None
    request_id: RequestId
    risk_check: typing.Optional[RiskCheckDetails] = None
    shareable_url: typing.Optional[ShareableUrl] = None
    status: IdentityVerificationStatus
    steps: IdentityVerificationStepSummary
    template: IdentityVerificationTemplateReference
    user: IdentityVerificationUserData
    watchlist_screening_id: typing.Optional[WatchlistScreeningIndividualIdNullable] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
