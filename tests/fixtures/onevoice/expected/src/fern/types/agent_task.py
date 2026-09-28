

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .agent_task_verification_status import AgentTaskVerificationStatus


class AgentTask(UniversalBaseModel):
    id: str
    business_id: typing_extensions.Annotated[str, FieldMetadata(alias="businessId"), pydantic.Field(alias="businessId")]
    type: str
    display_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="displayName"), pydantic.Field(alias="displayName")
    ] = None
    display_name_key: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="displayNameKey"), pydantic.Field(alias="displayNameKey")
    ] = None
    status: str
    platform: str
    input: typing.Optional[typing.Any] = pydantic.Field(default=None)
    """
    Free-form per-task input payload.
    """

    output: typing.Optional[typing.Any] = pydantic.Field(default=None)
    """
    Free-form per-task output payload.
    """

    error: typing.Optional[str] = None
    error_code: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="errorCode"), pydantic.Field(alias="errorCode")
    ] = None
    origin_conversation_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="originConversationId"),
        pydantic.Field(
            alias="originConversationId",
            description="Exact originating conversation, present only when it is live and owned by the requesting user.",
        ),
    ] = None
    """
    Exact originating conversation, present only when it is live and owned by the requesting user.
    """

    verification_status: typing_extensions.Annotated[
        typing.Optional[AgentTaskVerificationStatus],
        FieldMetadata(alias="verificationStatus"),
        pydantic.Field(alias="verificationStatus"),
    ] = None
    verification_fields: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="verificationFields"),
        pydantic.Field(alias="verificationFields"),
    ] = None
    verification_mismatches: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="verificationMismatches"),
        pydantic.Field(alias="verificationMismatches"),
    ] = None
    verification_error_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="verificationErrorCode"),
        pydantic.Field(alias="verificationErrorCode"),
    ] = None
    verification_checked_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="verificationCheckedAt"),
        pydantic.Field(alias="verificationCheckedAt"),
    ] = None
    verification_can_rerun: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="verificationCanRerun"),
        pydantic.Field(
            alias="verificationCanRerun",
            description="Server-authoritative eligibility for another readonly verification.",
        ),
    ] = None
    """
    Server-authoritative eligibility for another readonly verification.
    """

    started_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="startedAt"), pydantic.Field(alias="startedAt")
    ] = None
    completed_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="completedAt"), pydantic.Field(alias="completedAt")
    ] = None
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
