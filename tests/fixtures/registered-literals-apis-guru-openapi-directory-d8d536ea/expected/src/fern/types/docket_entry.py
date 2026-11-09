

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .docket_entry_boundary import DocketEntryBoundary
from .docket_entry_docket_badge import DocketEntryDocketBadge
from .docket_entry_primary_documents import DocketEntryPrimaryDocuments
from .docket_entry_secondary_documents import DocketEntrySecondaryDocuments
from .referenced_docket_number import ReferencedDocketNumber
from .source_structured_data import SourceStructuredData


class DocketEntry(UniversalBaseModel):
    boundary: typing.Optional[DocketEntryBoundary] = pydantic.Field(default=None)
    """
    Determines if it is the first docket entry or the last docket entry. This value will be set only for the first and last docket entry. For other docket entries it will be null. However, this will be set as single_docket_entry when the Case contains only one docket entry.
    """

    docket_badge: typing_extensions.Annotated[
        DocketEntryDocketBadge,
        FieldMetadata(alias="docketBadge"),
        pydantic.Field(
            alias="docketBadge", description="Docket Badge helps you to know what type of a docket entry it is."
        ),
    ]
    """
    Docket Badge helps you to know what type of a docket entry it is.
    """

    docket_entry_date: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="docketEntryDate"),
        pydantic.Field(alias="docketEntryDate", description="Docket Action Date"),
    ]
    """
    Docket Action Date
    """

    docket_entry_primary_documents: typing_extensions.Annotated[
        typing.Optional[DocketEntryPrimaryDocuments],
        FieldMetadata(alias="docketEntryPrimaryDocuments"),
        pydantic.Field(alias="docketEntryPrimaryDocuments"),
    ] = None
    docket_entry_secondary_documents: typing_extensions.Annotated[
        typing.Optional[DocketEntrySecondaryDocuments],
        FieldMetadata(alias="docketEntrySecondaryDocuments"),
        pydantic.Field(alias="docketEntrySecondaryDocuments"),
    ] = None
    docket_number: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="docketNumber"),
        pydantic.Field(
            alias="docketNumber",
            description="The respective docket entry number which is defined in the court website.",
        ),
    ] = None
    """
    The respective docket entry number which is defined in the court website.
    """

    last_fetch_date: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="lastFetchDate"),
        pydantic.Field(alias="lastFetchDate", description="When this docket entry was last fetched from the source."),
    ]
    """
    When this docket entry was last fetched from the source.
    """

    object: str = pydantic.Field()
    """
    Name of the object
    """

    referenced_docket_number_array: typing_extensions.Annotated[
        typing.List[typing.Optional[ReferencedDocketNumber]],
        FieldMetadata(alias="referencedDocketNumberArray"),
        pydantic.Field(
            alias="referencedDocketNumberArray",
            description="Other Docket Numbers that referenced for a particular docket entry.",
        ),
    ]
    """
    Other Docket Numbers that referenced for a particular docket entry.
    """

    sort_order: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="sortOrder"),
        pydantic.Field(alias="sortOrder", description="Order number how the dockets have stored in UniCourt."),
    ]
    """
    Order number how the dockets have stored in UniCourt.
    """

    text: str = pydantic.Field()
    """
    Source Docket Entry
    """

    text_structured: typing_extensions.Annotated[
        typing.Optional[SourceStructuredData],
        FieldMetadata(alias="textStructured"),
        pydantic.Field(alias="textStructured"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
