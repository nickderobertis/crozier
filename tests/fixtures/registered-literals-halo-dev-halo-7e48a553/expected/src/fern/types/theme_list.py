

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .theme import Theme


class ThemeList(UniversalBaseModel):
    first: bool = pydantic.Field()
    """
    Indicates whether current page is the first page.
    """

    has_next: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="hasNext"),
        pydantic.Field(alias="hasNext", description="Indicates whether current page has next page."),
    ]
    """
    Indicates whether current page has next page.
    """

    has_previous: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="hasPrevious"),
        pydantic.Field(alias="hasPrevious", description="Indicates whether current page has previous page."),
    ]
    """
    Indicates whether current page has previous page.
    """

    items: typing.List[Theme] = pydantic.Field()
    """
    A chunk of items.
    """

    last: bool = pydantic.Field()
    """
    Indicates whether current page is the last page.
    """

    page: int = pydantic.Field()
    """
    Page number, starts from 1. If not set or equal to 0, it means no pagination.
    """

    size: int = pydantic.Field()
    """
    Size of each page. If not set or equal to 0, it means no pagination.
    """

    total: int = pydantic.Field()
    """
    Total elements.
    """

    total_pages: typing_extensions.Annotated[
        int, FieldMetadata(alias="totalPages"), pydantic.Field(alias="totalPages", description="Indicates total pages.")
    ]
    """
    Indicates total pages.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
