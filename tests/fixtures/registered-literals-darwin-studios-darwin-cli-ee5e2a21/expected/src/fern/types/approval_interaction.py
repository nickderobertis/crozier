

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .approval_interaction_kind import ApprovalInteractionKind
from .approval_interaction_state import ApprovalInteractionState


class ApprovalInteraction(UniversalBaseModel):
    """
    An exact reviewed consequential decision. The approval ID, payload digest, revision, and expiry must all still match when the user decides.
    """

    id: str
    kind: ApprovalInteractionKind
    state: ApprovalInteractionState
    display_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="displayName"), pydantic.Field(alias="displayName")
    ]
    hostname: str
    expires_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="expiresAt"), pydantic.Field(alias="expiresAt")
    ]
    approval_id: typing_extensions.Annotated[str, FieldMetadata(alias="approvalId"), pydantic.Field(alias="approvalId")]
    expected_revision: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="expectedRevision"), pydantic.Field(alias="expectedRevision")
    ]
    reviewed_payload_digest: typing_extensions.Annotated[
        str, FieldMetadata(alias="reviewedPayloadDigest"), pydantic.Field(alias="reviewedPayloadDigest")
    ]
    preview: typing.Dict[str, typing.Any]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
