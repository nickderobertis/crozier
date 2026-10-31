

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .copy_log_details import CopyLogDetails


class DataBoxDiskCopyLogDetails(CopyLogDetails):
    """
    Copy Log Details for a disk
    """

    disk_serial_number: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="diskSerialNumber"),
        pydantic.Field(alias="diskSerialNumber", description="Disk Serial Number."),
    ] = None
    """
    Disk Serial Number.
    """

    error_log_link: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="errorLogLink"),
        pydantic.Field(alias="errorLogLink", description="Link for copy error logs."),
    ] = None
    """
    Link for copy error logs.
    """

    verbose_log_link: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="verboseLogLink"),
        pydantic.Field(alias="verboseLogLink", description="Link for copy verbose logs."),
    ] = None
    """
    Link for copy verbose logs.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
