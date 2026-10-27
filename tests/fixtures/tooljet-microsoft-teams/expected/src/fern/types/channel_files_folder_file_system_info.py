

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ChannelFilesFolderFileSystemInfo(UniversalBaseModel):
    created_date_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="createdDateTime"), pydantic.Field(alias="createdDateTime")
    ] = None
    last_modified_date_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="lastModifiedDateTime"),
        pydantic.Field(alias="lastModifiedDateTime"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
