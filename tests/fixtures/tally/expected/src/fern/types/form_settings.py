

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class FormSettings(UniversalBaseModel):
    language: typing.Optional[str] = None
    is_closed: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isClosed"), pydantic.Field(alias="isClosed")
    ] = None
    close_message_title: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="closeMessageTitle"), pydantic.Field(alias="closeMessageTitle")
    ] = None
    close_message_description: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="closeMessageDescription"),
        pydantic.Field(alias="closeMessageDescription"),
    ] = None
    close_timezone: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="closeTimezone"), pydantic.Field(alias="closeTimezone")
    ] = None
    close_date: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="closeDate"), pydantic.Field(alias="closeDate")
    ] = None
    close_time: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="closeTime"), pydantic.Field(alias="closeTime")
    ] = None
    submissions_limit: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="submissionsLimit"), pydantic.Field(alias="submissionsLimit")
    ] = None
    unique_submission_key: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="uniqueSubmissionKey"), pydantic.Field(alias="uniqueSubmissionKey")
    ] = None
    redirect_on_completion: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="redirectOnCompletion"), pydantic.Field(alias="redirectOnCompletion")
    ] = None
    has_self_email_notifications: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="hasSelfEmailNotifications"),
        pydantic.Field(alias="hasSelfEmailNotifications"),
    ] = None
    self_email_to: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="selfEmailTo"), pydantic.Field(alias="selfEmailTo")
    ] = None
    self_email_reply_to: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="selfEmailReplyTo"), pydantic.Field(alias="selfEmailReplyTo")
    ] = None
    self_email_subject: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="selfEmailSubject"), pydantic.Field(alias="selfEmailSubject")
    ] = None
    self_email_from_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="selfEmailFromName"), pydantic.Field(alias="selfEmailFromName")
    ] = None
    self_email_body: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="selfEmailBody"), pydantic.Field(alias="selfEmailBody")
    ] = None
    has_respondent_email_notifications: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="hasRespondentEmailNotifications"),
        pydantic.Field(alias="hasRespondentEmailNotifications"),
    ] = None
    respondent_email_to: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="respondentEmailTo"), pydantic.Field(alias="respondentEmailTo")
    ] = None
    respondent_email_reply_to: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="respondentEmailReplyTo"),
        pydantic.Field(alias="respondentEmailReplyTo"),
    ] = None
    respondent_email_subject: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="respondentEmailSubject"),
        pydantic.Field(alias="respondentEmailSubject"),
    ] = None
    respondent_email_from_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="respondentEmailFromName"),
        pydantic.Field(alias="respondentEmailFromName"),
    ] = None
    respondent_email_body: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="respondentEmailBody"), pydantic.Field(alias="respondentEmailBody")
    ] = None
    has_progress_bar: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="hasProgressBar"), pydantic.Field(alias="hasProgressBar")
    ] = None
    has_partial_submissions: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="hasPartialSubmissions"),
        pydantic.Field(alias="hasPartialSubmissions"),
    ] = None
    page_auto_jump: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="pageAutoJump"), pydantic.Field(alias="pageAutoJump")
    ] = None
    save_for_later: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="saveForLater"), pydantic.Field(alias="saveForLater")
    ] = None
    styles: typing.Optional[str] = None
    password: typing.Optional[str] = None
    submissions_data_retention_duration: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="submissionsDataRetentionDuration"),
        pydantic.Field(alias="submissionsDataRetentionDuration"),
    ] = None
    submissions_data_retention_unit: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="submissionsDataRetentionUnit"),
        pydantic.Field(alias="submissionsDataRetentionUnit"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
