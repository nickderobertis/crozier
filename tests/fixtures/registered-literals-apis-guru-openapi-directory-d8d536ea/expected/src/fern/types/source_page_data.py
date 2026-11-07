

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .source_structured_data import SourceStructuredData


class SourcePageData(UniversalBaseModel):
    """
    Source data from different pages in the court website.
    """

    additional_source_data: typing_extensions.Annotated[
        typing.Optional[SourceStructuredData],
        FieldMetadata(alias="additionalSourceData"),
        pydantic.Field(alias="additionalSourceData"),
    ] = None
    first_fetch_date: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="firstFetchDate"),
        pydantic.Field(alias="firstFetchDate", description="When was the page first fetched from the court site."),
    ]
    """
    When was the page first fetched from the court site.
    """

    last_fetch_date: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="lastFetchDate"),
        pydantic.Field(alias="lastFetchDate", description="When was the page last fetched from the court site."),
    ]
    """
    When was the page last fetched from the court site.
    """

    object: str = pydantic.Field()
    """
    Name of the object
    """

    page_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="pageName"),
        pydantic.Field(
            alias="pageName",
            description="Pages supported for PACER pacerCaseQuery, pacerDocketReport, pacerCaseSummary, pacerAssociatedCases, pacerCaseLocatorResults, hearing, relatedCases.",
        ),
    ]
    """
    Pages supported for PACER pacerCaseQuery, pacerDocketReport, pacerCaseSummary, pacerAssociatedCases, pacerCaseLocatorResults, hearing, relatedCases.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
