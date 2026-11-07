

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .attorney import Attorney


class Attorneys(UniversalBaseModel):
    attorney_array: typing_extensions.Annotated[
        typing.List[typing.Optional[Attorney]],
        FieldMetadata(alias="attorneyArray"),
        pydantic.Field(alias="attorneyArray"),
    ]
    next_page_api: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="nextPageAPI"),
        pydantic.Field(alias="nextPageAPI", description="Link to next page of a particular entity in a Case."),
    ] = None
    """
    Link to next page of a particular entity in a Case.
    """

    object: str = pydantic.Field()
    """
    Name of the object
    """

    page_number: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="pageNumber"),
        pydantic.Field(alias="pageNumber", description="Page number for which results where obtained."),
    ]
    """
    Page number for which results where obtained.
    """

    total_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="totalCount"),
        pydantic.Field(alias="totalCount", description="Total number of parties of the Case entity in a Case."),
    ]
    """
    Total number of parties of the Case entity in a Case.
    """

    total_pages: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="totalPages"),
        pydantic.Field(
            alias="totalPages", description="Total number of pages to obtain all the objects of a party in the Case."
        ),
    ]
    """
    Total number of pages to obtain all the objects of a party in the Case.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
