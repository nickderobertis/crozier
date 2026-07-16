

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class File(UniversalBaseModel):
    """
    File
    """

    id: typing_extensions.Annotated[
        str, FieldMetadata(alias="$id"), pydantic.Field(alias="$id", description="File ID.")
    ]
    """
    File ID.
    """

    permissions: typing_extensions.Annotated[
        typing.Dict[str, typing.Any],
        FieldMetadata(alias="$permissions"),
        pydantic.Field(alias="$permissions", description="File permissions."),
    ]
    """
    File permissions.
    """

    date_created: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="dateCreated"),
        pydantic.Field(alias="dateCreated", description="File creation date in Unix timestamp."),
    ]
    """
    File creation date in Unix timestamp.
    """

    mime_type: typing_extensions.Annotated[
        str, FieldMetadata(alias="mimeType"), pydantic.Field(alias="mimeType", description="File mime type.")
    ]
    """
    File mime type.
    """

    name: str = pydantic.Field()
    """
    File name.
    """

    signature: str = pydantic.Field()
    """
    File MD5 signature.
    """

    size_original: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="sizeOriginal"),
        pydantic.Field(alias="sizeOriginal", description="File original size in bytes."),
    ]
    """
    File original size in bytes.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
