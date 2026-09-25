

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BaseReportTargetModel(UniversalBaseModel):
    """
    Model for base report target
    """

    account_groups: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="accountGroups"),
        pydantic.Field(alias="accountGroups", description="List of cloud account groups"),
    ] = None
    """
    List of cloud account groups
    """

    accounts: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of cloud accounts
    """

    compliance_standard_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="complianceStandardIds"),
        pydantic.Field(alias="complianceStandardIds", description="List of compliance Standard IDs"),
    ] = None
    """
    List of compliance Standard IDs
    """

    compression_enabled: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="compressionEnabled"),
        pydantic.Field(alias="compressionEnabled", description="Business unit detailed report compression enabled"),
    ] = None
    """
    Business unit detailed report compression enabled
    """

    download_now: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="downloadNow"),
        pydantic.Field(alias="downloadNow", description="True = download now"),
    ] = None
    """
    True = download now
    """

    notification_template_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="notificationTemplateId"),
        pydantic.Field(alias="notificationTemplateId", description="Notification template id"),
    ] = None
    """
    Notification template id
    """

    notify_to: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="notifyTo"),
        pydantic.Field(alias="notifyTo", description="List of email addresses to receive notification"),
    ] = None
    """
    List of email addresses to receive notification
    """

    regions: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of regions
    """

    schedule: typing.Optional[str] = pydantic.Field(default=None)
    """
    Recurring report schedule in RRULE format
    """

    schedule_enabled: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="scheduleEnabled"),
        pydantic.Field(alias="scheduleEnabled", description="Report scheduling enabled"),
    ] = None
    """
    Report scheduling enabled
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
