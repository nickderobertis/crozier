

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PageMetadataDto(UniversalBaseModel):
    size: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of elements in the current page
    """

    total_elements: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="totalElements"),
        pydantic.Field(alias="totalElements", description="Total number of elements across all pages"),
    ] = None
    """
    Total number of elements across all pages
    """

    total_pages: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="totalPages"),
        pydantic.Field(alias="totalPages", description="Total number of pages"),
    ] = None
    """
    Total number of pages
    """

    number: typing.Optional[int] = pydantic.Field(default=None)
    """
    Current page number (zero-based)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
