

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PacerSearchPageInfo(UniversalBaseModel):
    first: bool = pydantic.Field()
    """
    Indicates if the current page is the first page.
    """

    last: bool = pydantic.Field()
    """
    Indicates if the current page is the last page.
    """

    number: int = pydantic.Field()
    """
    Current Page number.
    """

    number_of_elements: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="numberOfElements"),
        pydantic.Field(alias="numberOfElements", description="Number of records returned."),
    ]
    """
    Number of records returned.
    """

    object: str = pydantic.Field()
    """
    Name of the object
    """

    size: int = pydantic.Field()
    """
    Number of results obtained in a page..
    """

    total_elements: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="totalElements"),
        pydantic.Field(alias="totalElements", description="Total number of records available"),
    ]
    """
    Total number of records available
    """

    total_pages: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="totalPages"),
        pydantic.Field(alias="totalPages", description="Total pages of data available."),
    ]
    """
    Total pages of data available.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
