

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .case_count_analytics_by_court_location import CaseCountAnalyticsByCourtLocation


class CaseCountAnalyticsByCourtLocationResponse(UniversalBaseModel):
    """
    Case Counts by Court Location Response.
    """

    next_page_api: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="nextPageAPI"),
        pydantic.Field(alias="nextPageAPI", description="Next page of results if applicable."),
    ] = None
    """
    Next page of results if applicable.
    """

    object: str
    previous_page_api: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="previousPageAPI"),
        pydantic.Field(alias="previousPageAPI", description="Link to previous page of results."),
    ] = None
    """
    Link to previous page of results.
    """

    results: typing.List[CaseCountAnalyticsByCourtLocation]
    total_case_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="totalCaseCount"),
        pydantic.Field(alias="totalCaseCount", description="Total no. of Cases for this criteria."),
    ]
    """
    Total no. of Cases for this criteria.
    """

    total_court_location_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="totalCourtLocationCount"),
        pydantic.Field(alias="totalCourtLocationCount", description="Total no. of Court Location for this criteria."),
    ]
    """
    Total no. of Court Location for this criteria.
    """

    total_pages: typing_extensions.Annotated[
        int, FieldMetadata(alias="totalPages"), pydantic.Field(alias="totalPages", description="Total no. of pages.")
    ]
    """
    Total no. of pages.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
