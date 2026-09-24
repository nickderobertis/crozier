

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .alert_rule_notification_config_model_frequency import AlertRuleNotificationConfigModelFrequency
from .alert_rule_notification_config_model_type import AlertRuleNotificationConfigModelType
from .week_day import WeekDay


class AlertRuleNotificationConfigModel(UniversalBaseModel):
    """
    Model for Alert Rule Notification Config
    """

    day_of_month: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="dayOfMonth"),
        pydantic.Field(alias="dayOfMonth", description="Day of month"),
    ] = None
    """
    Day of month
    """

    days_of_week: typing_extensions.Annotated[
        typing.Optional[typing.List[WeekDay]],
        FieldMetadata(alias="daysOfWeek"),
        pydantic.Field(alias="daysOfWeek", description="Days of week"),
    ] = None
    """
    Days of week
    """

    detailed_report: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="detailedReport"),
        pydantic.Field(alias="detailedReport", description="Provide csv detailed report"),
    ] = None
    """
    Provide csv detailed report
    """

    enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Scan enabled
    """

    frequency: typing.Optional[AlertRuleNotificationConfigModelFrequency] = None
    frequency_from_r_rule: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="frequencyFromRRule"),
        pydantic.Field(alias="frequencyFromRRule", description="Frequency from RRule"),
    ] = None
    """
    Frequency from RRule
    """

    hour_of_day: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="hourOfDay"),
        pydantic.Field(alias="hourOfDay", description="Hour of day"),
    ] = None
    """
    Hour of day
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Alert rule notification config ID
    """

    include_remediation: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="includeRemediation"),
        pydantic.Field(alias="includeRemediation", description="Include remediation in detailed report"),
    ] = None
    """
    Include remediation in detailed report
    """

    last_updated: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="lastUpdated"),
        pydantic.Field(alias="lastUpdated", description="Last Updated"),
    ] = None
    """
    Last Updated
    """

    last_sent_ts: typing.Optional[int] = pydantic.Field(default=None)
    """
    Time of last notification in milliseconds
    """

    recipients: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    * For email notifications: List of unique email addresses to notify
    * For integrations without notification templates: List of integration ids
    * For integrations with notification templates: List of notification template ids
    """

    rrule_schedule: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="rruleSchedule"), pydantic.Field(alias="rruleSchedule")
    ] = None
    template_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="templateId"),
        pydantic.Field(alias="templateId", description="Template ID"),
    ] = None
    """
    Template ID
    """

    timezone: typing.Optional[str] = pydantic.Field(default=None)
    """
    Java time zone ID (e.g. America/Los_Angeles) 
    """

    type: typing.Optional[AlertRuleNotificationConfigModelType] = pydantic.Field(default=None)
    """
    Integration type
    """

    with_compression: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="withCompression"),
        pydantic.Field(alias="withCompression", description="Compress detailed report"),
    ] = None
    """
    Compress detailed report
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
