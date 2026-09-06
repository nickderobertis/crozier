

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .added_at import AddedAt
from .author_asin import AuthorAsin
from .author_description import AuthorDescription
from .author_id import AuthorId
from .author_image_path import AuthorImagePath
from .author_name import AuthorName
from .author_series import AuthorSeries
from .library_item_minified import LibraryItemMinified
from .updated_at import UpdatedAt


class Author(UniversalBaseModel):
    """
    An author object which includes a description and image path. The library items and series associated with the author are optionally included.
    """

    id: typing.Optional[AuthorId] = None
    asin: typing.Optional[AuthorAsin] = None
    name: typing.Optional[AuthorName] = None
    description: typing.Optional[AuthorDescription] = None
    image_path: typing_extensions.Annotated[
        typing.Optional[AuthorImagePath], FieldMetadata(alias="imagePath"), pydantic.Field(alias="imagePath")
    ] = None
    added_at: typing_extensions.Annotated[
        typing.Optional[AddedAt], FieldMetadata(alias="addedAt"), pydantic.Field(alias="addedAt")
    ] = None
    updated_at: typing_extensions.Annotated[
        typing.Optional[UpdatedAt], FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")
    ] = None
    library_items: typing_extensions.Annotated[
        typing.Optional[typing.List[LibraryItemMinified]],
        FieldMetadata(alias="libraryItems"),
        pydantic.Field(alias="libraryItems", description="The items associated with the author"),
    ] = None
    """
    The items associated with the author
    """

    series: typing.Optional[typing.List[AuthorSeries]] = pydantic.Field(default=None)
    """
    The series associated with the author
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
