

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class V2TableExportDownloadData(UniversalBaseModel):
    """
    Signed URL and filename for a completed table export.
    """

    url: str = pydantic.Field()
    """
    Short-lived signed download URL.
    """

    file_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="fileName"), pydantic.Field(alias="fileName", description="Suggested export filename.")
    ]
    """
    Suggested export filename.
    """

    expires_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="expiresAt"),
        pydantic.Field(alias="expiresAt", description="ISO 8601 URL expiration timestamp."),
    ]
    """
    ISO 8601 URL expiration timestamp.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
