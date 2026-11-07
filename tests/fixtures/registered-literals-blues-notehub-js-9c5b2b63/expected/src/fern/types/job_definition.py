

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .batch_job_requests import BatchJobRequests
from .job_definition_report_options import JobDefinitionReportOptions
from .job_definition_select import JobDefinitionSelect


class JobDefinition(UniversalBaseModel):
    """
    Batch job definition
    """

    comment: typing.Optional[str] = pydantic.Field(default=None)
    """
    Human-readable description of the job
    """

    default_requests: typing.Optional[BatchJobRequests] = None
    device_requests: typing.Optional[typing.Dict[str, BatchJobRequests]] = pydantic.Field(default=None)
    """
    Device-specific request overrides, keyed by device UID
    """

    report_options: typing.Optional[JobDefinitionReportOptions] = pydantic.Field(default=None)
    """
    Controls what data is included in the job report
    """

    select: typing.Optional[JobDefinitionSelect] = pydantic.Field(default=None)
    """
    Device selection criteria
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
