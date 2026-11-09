

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .associated_norm_party import AssociatedNormParty


class AssociatedNormPartyResponse(UniversalBaseModel):
    associated_norm_party_array: typing_extensions.Annotated[
        typing.List[AssociatedNormParty],
        FieldMetadata(alias="associatedNormPartyArray"),
        pydantic.Field(alias="associatedNormPartyArray"),
    ]
    next_page_api: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="nextPageAPI"),
        pydantic.Field(alias="nextPageAPI", description="Next page of results if applicable."),
    ] = None
    """
    Next page of results if applicable.
    """

    previous_page_api: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="previousPageAPI"),
        pydantic.Field(alias="previousPageAPI", description="Link to previous page of results."),
    ] = None
    """
    Link to previous page of results.
    """

    total_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="totalCount"),
        pydantic.Field(alias="totalCount", description="Total no. of results for this criteria."),
    ]
    """
    Total no. of results for this criteria.
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
