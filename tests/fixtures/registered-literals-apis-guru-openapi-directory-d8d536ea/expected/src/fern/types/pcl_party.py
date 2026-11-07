

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .pacer_party_search_results import PacerPartySearchResults
from .pacer_search_page_info import PacerSearchPageInfo
from .pacer_search_receipt import PacerSearchReceipt


class PclParty(UniversalBaseModel):
    next_page_api: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="nextPageAPI"),
        pydantic.Field(alias="nextPageAPI", description="Link to next page of the PCL Search Results."),
    ] = None
    """
    Link to next page of the PCL Search Results.
    """

    object: str = pydantic.Field()
    """
    Name of the object
    """

    pacer_page_info: typing_extensions.Annotated[
        PacerSearchPageInfo, FieldMetadata(alias="pacerPageInfo"), pydantic.Field(alias="pacerPageInfo")
    ]
    pacer_receipt: typing_extensions.Annotated[
        PacerSearchReceipt, FieldMetadata(alias="pacerReceipt"), pydantic.Field(alias="pacerReceipt")
    ]
    pacer_search_results_array: typing_extensions.Annotated[
        typing.List[PacerPartySearchResults],
        FieldMetadata(alias="pacerSearchResultsArray"),
        pydantic.Field(alias="pacerSearchResultsArray"),
    ]
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
        pydantic.Field(alias="totalCount", description="Total number of records available for this Search."),
    ]
    """
    Total number of records available for this Search.
    """

    total_pages: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="totalPages"),
        pydantic.Field(
            alias="totalPages", description="Total number of pages to obtain all the objects the current PCL Search."
        ),
    ]
    """
    Total number of pages to obtain all the objects the current PCL Search.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
