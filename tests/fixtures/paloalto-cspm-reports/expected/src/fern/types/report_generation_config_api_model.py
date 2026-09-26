

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .report_generation_config_api_model_cloud_type import ReportGenerationConfigApiModelCloudType
from .report_generation_config_api_model_counts import ReportGenerationConfigApiModelCounts
from .report_generation_config_api_model_target import ReportGenerationConfigApiModelTarget
from .report_generation_config_api_model_type import ReportGenerationConfigApiModelType


class ReportGenerationConfigApiModel(UniversalBaseModel):
    """
    Model for report generation configuration
    """

    cloud_type: typing_extensions.Annotated[
        ReportGenerationConfigApiModelCloudType,
        FieldMetadata(alias="cloudType"),
        pydantic.Field(alias="cloudType", description="Cloud type"),
    ]
    """
    Cloud type
    """

    compliance_standard_deleted: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="complianceStandardDeleted"),
        pydantic.Field(alias="complianceStandardDeleted", description="Compliance Standard Deleted"),
    ] = None
    """
    Compliance Standard Deleted
    """

    compliance_standard_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="complianceStandardId"),
        pydantic.Field(alias="complianceStandardId", description="Compliance standard ID"),
    ] = None
    """
    Compliance standard ID
    """

    counts: typing.Optional[ReportGenerationConfigApiModelCounts] = pydantic.Field(default=None)
    """
    Model for compliance aggregate count
    """

    created_by: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="createdBy"),
        pydantic.Field(alias="createdBy", description="User who created this report"),
    ] = None
    """
    User who created this report
    """

    created_on: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="createdOn"),
        pydantic.Field(alias="createdOn", description="Report created on this timestamp"),
    ] = None
    """
    Report created on this timestamp
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Report ID
    """

    last_modified_by: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="lastModifiedBy"),
        pydantic.Field(alias="lastModifiedBy", description="Last modified by"),
    ] = None
    """
    Last modified by
    """

    last_modified_on: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="lastModifiedOn"),
        pydantic.Field(alias="lastModifiedOn", description="Timestamp of last modification"),
    ] = None
    """
    Timestamp of last modification
    """

    last_scheduled: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="lastScheduled"),
        pydantic.Field(alias="lastScheduled", description="Timestamp of last generated report"),
    ] = None
    """
    Timestamp of last generated report
    """

    locale: typing.Optional[str] = pydantic.Field(default=None)
    """
    Locale of caller (e.g. en_us, jp). Default is en_us.
    """

    name: str = pydantic.Field()
    """
    Report name
    """

    next_schedule: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="nextSchedule"),
        pydantic.Field(alias="nextSchedule", description="Timestamp of next scheduled report"),
    ] = None
    """
    Timestamp of next scheduled report
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    Report generation status
    """

    target: typing.Optional[ReportGenerationConfigApiModelTarget] = pydantic.Field(default=None)
    """
    Report definition
    """

    total_instance_count: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="totalInstanceCount"),
        pydantic.Field(alias="totalInstanceCount", description="Total number of reports for the report ID"),
    ] = None
    """
    Total number of reports for the report ID
    """

    type: typing.Optional[ReportGenerationConfigApiModelType] = pydantic.Field(default=None)
    """
    Report type. Default is COMPLIANCE.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
