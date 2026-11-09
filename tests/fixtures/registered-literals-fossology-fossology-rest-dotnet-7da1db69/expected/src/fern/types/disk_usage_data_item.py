

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DiskUsageDataItem(UniversalBaseModel):
    filesystem: typing.Optional[str] = pydantic.Field(default=None)
    """
    Filesystem path
    """

    capacity: typing.Optional[str] = pydantic.Field(default=None)
    """
    Total capacity of the filesystem
    """

    used: typing.Optional[str] = pydantic.Field(default=None)
    """
    Used space in the filesystem
    """

    available: typing.Optional[str] = pydantic.Field(default=None)
    """
    Available space in the filesystem
    """

    percent_full: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="percentFull"),
        pydantic.Field(alias="percentFull", description="Percentage of the filesystem used"),
    ] = None
    """
    Percentage of the filesystem used
    """

    mount_point: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="mountPoint"),
        pydantic.Field(alias="mountPoint", description="Mount point of the filesystem"),
    ] = None
    """
    Mount point of the filesystem
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
