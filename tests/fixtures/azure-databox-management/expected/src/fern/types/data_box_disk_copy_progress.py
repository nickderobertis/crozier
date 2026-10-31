

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .data_box_disk_copy_progress_status import DataBoxDiskCopyProgressStatus


class DataBoxDiskCopyProgress(UniversalBaseModel):
    """
    DataBox Disk Copy Progress
    """

    bytes_copied: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="bytesCopied"),
        pydantic.Field(alias="bytesCopied", description="Bytes copied during the copy of disk."),
    ] = None
    """
    Bytes copied during the copy of disk.
    """

    percent_complete: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="percentComplete"),
        pydantic.Field(
            alias="percentComplete", description="Indicates the percentage completed for the copy of the disk."
        ),
    ] = None
    """
    Indicates the percentage completed for the copy of the disk.
    """

    serial_number: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="serialNumber"),
        pydantic.Field(alias="serialNumber", description="The serial number of the disk"),
    ] = None
    """
    The serial number of the disk
    """

    status: typing.Optional[DataBoxDiskCopyProgressStatus] = pydantic.Field(default=None)
    """
    The Status of the copy
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
