

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .created_at import CreatedAt
from .folder import Folder
from .library_id import LibraryId
from .library_name import LibraryName
from .library_settings import LibrarySettings
from .updated_at import UpdatedAt


class Library(UniversalBaseModel):
    """
    A library object which includes either books or podcasts.
    """

    id: typing.Optional[LibraryId] = None
    name: typing.Optional[LibraryName] = None
    folders: typing.Optional[typing.List[Folder]] = pydantic.Field(default=None)
    """
    The folders that belong to the library.
    """

    display_order: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="displayOrder"),
        pydantic.Field(
            alias="displayOrder", description="Display position of the library in the list of libraries. Must be >= 1."
        ),
    ] = None
    """
    Display position of the library in the list of libraries. Must be >= 1.
    """

    icon: typing.Optional[str] = pydantic.Field(default=None)
    """
    The selected icon for the library. See Library Icons for a list of possible icons.
    """

    media_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="mediaType"),
        pydantic.Field(
            alias="mediaType",
            description="The type of media that the library contains. Will be `book` or `podcast`. (Read Only)",
        ),
    ] = None
    """
    The type of media that the library contains. Will be `book` or `podcast`. (Read Only)
    """

    provider: typing.Optional[str] = pydantic.Field(default=None)
    """
    Preferred metadata provider for the library. See Metadata Providers for a list of possible providers.
    """

    settings: typing.Optional[LibrarySettings] = None
    created_at: typing_extensions.Annotated[
        typing.Optional[CreatedAt], FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ] = None
    last_update: typing_extensions.Annotated[
        typing.Optional[UpdatedAt], FieldMetadata(alias="lastUpdate"), pydantic.Field(alias="lastUpdate")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
