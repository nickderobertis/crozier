

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .item_author_dto import ItemAuthorDto
from .komga_extension_dto import KomgaExtensionDto


class ItemDto(UniversalBaseModel):
    komga: typing_extensions.Annotated[
        typing.Optional[KomgaExtensionDto],
        FieldMetadata(alias="_komga"),
        pydantic.Field(alias="_komga", description="Additional fields for the item"),
    ] = None
    """
    Additional fields for the item
    """

    author: typing.Optional[ItemAuthorDto] = pydantic.Field(default=None)
    """
    Author of the item
    """

    content_html: typing.Optional[str] = pydantic.Field(default=None)
    """
    HTML of the item
    """

    date_modified: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Modification date in RFC 3339 format
    """

    id: str = pydantic.Field()
    """
    Unique for that item for that feed over time
    """

    summary: typing.Optional[str] = pydantic.Field(default=None)
    """
    A plain text sentence or two describing the item
    """

    tags: typing.List[str] = pydantic.Field()
    """
    Tags describing the item
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    Plain text title
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL of the resource described by the item
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
