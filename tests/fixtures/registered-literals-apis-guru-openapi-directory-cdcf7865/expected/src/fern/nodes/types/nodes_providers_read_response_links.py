

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class NodesProvidersReadResponseLinks(UniversalBaseModel):
    """
    Links to alternative representations of the file entity.
    """

    delete: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Waterbutler API route for file deletions.
    """

    download: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Waterbutler API route for file downloads.
    """

    info: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the page to view a file's information or a folder's contents.
    """

    move: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Waterbutler API route for file moves.
    """

    new_folder: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Waterbutler API route for creating a new subfolder (does not exist for files).
    """

    self_: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="self"),
        pydantic.Field(alias="self", description="A link to the detail page for the file."),
    ] = None
    """
    A link to the detail page for the file.
    """

    upload: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Waterbutler API route for file uploads.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
