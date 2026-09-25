

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .links import Links


class TimeEntry(UniversalBaseModel):
    time_entry_id: typing_extensions.Annotated[
        float, FieldMetadata(alias="timeEntryId"), pydantic.Field(alias="timeEntryId")
    ]
    company_id: typing_extensions.Annotated[float, FieldMetadata(alias="companyId"), pydantic.Field(alias="companyId")]
    user_id: typing_extensions.Annotated[float, FieldMetadata(alias="userId"), pydantic.Field(alias="userId")]
    user: str
    date_entered: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="dateEntered"), pydantic.Field(alias="dateEntered")
    ]
    start_time: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="startTime"),
        pydantic.Field(
            alias="startTime",
            description="The start time of the time entry in the format of YYYY-MM-DD HH:MM at 15 minute intervals",
        ),
    ]
    """
    The start time of the time entry in the format of YYYY-MM-DD HH:MM at 15 minute intervals
    """

    end_time: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="endTime"),
        pydantic.Field(
            alias="endTime",
            description="The end time of the time entry in the format of YYYY-MM-DD HH:MM at 15 minute intervals",
        ),
    ]
    """
    The end time of the time entry in the format of YYYY-MM-DD HH:MM at 15 minute intervals
    """

    is_locked: typing_extensions.Annotated[bool, FieldMetadata(alias="isLocked"), pydantic.Field(alias="isLocked")]
    pay_rate: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="payRate"),
        pydantic.Field(alias="payRate", description="The pay rate per hour for the time entry"),
    ]
    """
    The pay rate per hour for the time entry
    """

    charge_out_rate: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="chargeOutRate"),
        pydantic.Field(alias="chargeOutRate", description="The charge out rate per hour for the time entry"),
    ]
    """
    The charge out rate per hour for the time entry
    """

    paid_duration: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="paidDuration"),
        pydantic.Field(alias="paidDuration", description="The paid duration in hours for the time entry"),
    ]
    """
    The paid duration in hours for the time entry
    """

    uncharged_time_duration: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="unchargedTimeDuration"),
        pydantic.Field(alias="unchargedTimeDuration", description="The uncharged duration in hours for the time entry"),
    ] = None
    """
    The uncharged duration in hours for the time entry
    """

    uncharged_time_start: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="unchargedTimeStart"),
        pydantic.Field(
            alias="unchargedTimeStart",
            description="The start time of the uncharged duration in the format of YYYY-MM-DD HH:MM at 15 minute intervals",
        ),
    ] = None
    """
    The start time of the uncharged duration in the format of YYYY-MM-DD HH:MM at 15 minute intervals
    """

    uncharged_time_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="unchargedTimeType"), pydantic.Field(alias="unchargedTimeType")
    ] = None
    is_uncharged_time_unpaid: typing_extensions.Annotated[
        bool, FieldMetadata(alias="isUnchargedTimeUnpaid"), pydantic.Field(alias="isUnchargedTimeUnpaid")
    ]
    work_description: typing_extensions.Annotated[
        str, FieldMetadata(alias="workDescription"), pydantic.Field(alias="workDescription")
    ]
    job_id: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="jobId"),
        pydantic.Field(alias="jobId", description="The id of the job that the time entry is associated with"),
    ] = None
    """
    The id of the job that the time entry is associated with
    """

    job_no: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="jobNo"),
        pydantic.Field(alias="jobNo", description="The sequential job no that the time entry is associated with"),
    ] = None
    """
    The sequential job no that the time entry is associated with
    """

    job_phase_id: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="jobPhaseId"),
        pydantic.Field(
            alias="jobPhaseId", description="The id of the job phase that the time entry is associated with"
        ),
    ] = None
    """
    The id of the job phase that the time entry is associated with
    """

    job_phase_title: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="jobPhaseTitle"), pydantic.Field(alias="jobPhaseTitle")
    ] = None
    job_phase_details: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="jobPhaseDetails"), pydantic.Field(alias="jobPhaseDetails")
    ] = None
    links: typing.List[Links]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
