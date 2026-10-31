

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .data_box_disk_copy_progress import DataBoxDiskCopyProgress
from .job_details import JobDetails


class DataBoxDiskJobDetails(JobDetails):
    """
    DataBox Disk Job Details.
    """

    copy_progress: typing_extensions.Annotated[
        typing.Optional[typing.List[DataBoxDiskCopyProgress]],
        FieldMetadata(alias="copyProgress"),
        pydantic.Field(alias="copyProgress", description="Copy progress per disk."),
    ] = None
    """
    Copy progress per disk.
    """

    disks_and_size_details: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, int]],
        FieldMetadata(alias="disksAndSizeDetails"),
        pydantic.Field(
            alias="disksAndSizeDetails",
            description="Contains the map of disk serial number to the disk size being used for the job. Is returned only after the disks are shipped to the customer.",
        ),
    ] = None
    """
    Contains the map of disk serial number to the disk size being used for the job. Is returned only after the disks are shipped to the customer.
    """

    passkey: typing.Optional[str] = pydantic.Field(default=None)
    """
    User entered passkey for DataBox Disk job.
    """

    preferred_disks: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, int]],
        FieldMetadata(alias="preferredDisks"),
        pydantic.Field(
            alias="preferredDisks",
            description="User preference on what size disks are needed for the job. The map is from the disk size in TB to the count. Eg. {2,5} means 5 disks of 2 TB size. Key is string but will be checked against an int.",
        ),
    ] = None
    """
    User preference on what size disks are needed for the job. The map is from the disk size in TB to the count. Eg. {2,5} means 5 disks of 2 TB size. Key is string but will be checked against an int.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
