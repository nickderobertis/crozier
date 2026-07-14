

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class File(UniversalBaseModel):
    """
    File
    """

    id: typing_extensions.Annotated[str, FieldMetadata(alias="$id")] = pydantic.Field()
    """
    File ID.
    """

    permissions: typing_extensions.Annotated[
        typing.Dict[str, typing.Optional[typing.Any]], FieldMetadata(alias="$permissions")
    ] = pydantic.Field()
    """
    File permissions.
    """

    date_created: typing_extensions.Annotated[int, FieldMetadata(alias="dateCreated")] = pydantic.Field()
    """
    File creation date in Unix timestamp.
    """

    mime_type: typing_extensions.Annotated[str, FieldMetadata(alias="mimeType")] = pydantic.Field()
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

    size_original: typing_extensions.Annotated[int, FieldMetadata(alias="sizeOriginal")] = pydantic.Field()
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
