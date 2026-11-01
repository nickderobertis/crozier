

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DiskSecret(UniversalBaseModel):
    """
    Contains all the secrets of a Disk.
    """

    bit_locker_key: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="bitLockerKey"),
        pydantic.Field(
            alias="bitLockerKey",
            description="Bit Locker key of the disk which can be used to unlock the disk to copy data.",
        ),
    ] = None
    """
    Bit Locker key of the disk which can be used to unlock the disk to copy data.
    """

    disk_serial_number: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="diskSerialNumber"),
        pydantic.Field(alias="diskSerialNumber", description="Serial number of the assigned disk."),
    ] = None
    """
    Serial number of the assigned disk.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
