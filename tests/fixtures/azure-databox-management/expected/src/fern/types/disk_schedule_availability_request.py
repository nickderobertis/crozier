

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .schedule_availability_request import ScheduleAvailabilityRequest


class DiskScheduleAvailabilityRequest(ScheduleAvailabilityRequest):
    """
    Request body to get the availability for scheduling disk orders.
    """

    expected_data_size_in_terabytes: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="expectedDataSizeInTerabytes"),
        pydantic.Field(
            alias="expectedDataSizeInTerabytes",
            description="The expected size of the data, which needs to be transferred in this job, in terabytes.",
        ),
    ]
    """
    The expected size of the data, which needs to be transferred in this job, in terabytes.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
