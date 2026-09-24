

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .standalone_quotes_specific_query_parameters_filter_status import (
    StandaloneQuotesSpecificQueryParametersFilterStatus,
)
from .standalone_quotes_specific_query_parameters_sort_field import StandaloneQuotesSpecificQueryParametersSortField


class StandaloneQuotesSpecificQueryParameters(UniversalBaseModel):
    filter_status: typing_extensions.Annotated[
        typing.Optional[StandaloneQuotesSpecificQueryParametersFilterStatus],
        FieldMetadata(alias="filterStatus"),
        pydantic.Field(alias="filterStatus"),
    ] = None
    sort_field: typing_extensions.Annotated[
        typing.Optional[StandaloneQuotesSpecificQueryParametersSortField],
        FieldMetadata(alias="sortField"),
        pydantic.Field(alias="sortField"),
    ] = None
    created_after: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="createdAfter"),
        pydantic.Field(
            alias="createdAfter", description="Get quote created after certain time. Overrides sortField and sortOrder"
        ),
    ] = None
    """
    Get quote created after certain time. Overrides sortField and sortOrder
    """

    modified_after: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="modifiedAfter"),
        pydantic.Field(
            alias="modifiedAfter",
            description="Get quote modified after certain time. Overrides sortField and sortOrder",
        ),
    ] = None
    """
    Get quote modified after certain time. Overrides sortField and sortOrder
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
