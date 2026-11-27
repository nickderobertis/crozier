

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class EntryExternalFile(UniversalBaseModel):
    """
    The ExternalFile resource stores metadata about the file. The actual original file can be downloaded by using the 'downloadURL' property.
    """

    download_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="downloadURL"),
        pydantic.Field(
            alias="downloadURL", description="A short-lived URL that can be used to download the original file."
        ),
    ] = None
    """
    A short-lived URL that can be used to download the original file.
    """

    expires_at: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="expiresAt"),
        pydantic.Field(alias="expiresAt", description="UNIX timestamp when downloadURL expires."),
    ] = None
    """
    UNIX timestamp when downloadURL expires.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the external file
    """

    size: typing.Optional[int] = pydantic.Field(default=None)
    """
    Size, in bytes, of the external file
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
