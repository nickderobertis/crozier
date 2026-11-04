

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BackupFile(UniversalBaseModel):
    """
    Backup file.
    """

    filename: typing.Optional[str] = pydantic.Field(default=None)
    """
    Filename of backup file.
    """

    last_modified_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="lastModifiedTime"),
        pydantic.Field(alias="lastModifiedTime", description="Last modified time of backup file."),
    ] = None
    """
    Last modified time of backup file.
    """

    size: typing.Optional[int] = pydantic.Field(default=None)
    """
    Size of backup file.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
