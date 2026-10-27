

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, update_forward_refs
from ..core.serialization import FieldMetadata
from .column_id import ColumnId
from .connector_condition import ConnectorCondition
from .connector_selects_item import ConnectorSelectsItem
from .filter import Filter
from .labeled import Labeled
from .table_id import TableId
from .validity_date import ValidityDate


class Connector(Labeled):
    """
    Describes a set of filters and selects for a single table. `column` provides the column to calculate the concept tree using ConceptConditions. `table` should be used, if the concept does not create a tree. `column` and `table` are therefore exclusive.
    """

    table: typing.Optional[TableId] = None
    column: typing.Optional[ColumnId] = None
    condition: typing.Optional[ConnectorCondition] = pydantic.Field(default=None)
    """
    Allows filtering of events for the tree. Useful to separate out events from a larger table for a very niche concept.
    """

    filters: typing.Optional[typing.List[Filter]] = pydantic.Field(default=None)
    """
    Definition of filters available in for querying this connector.
    """

    validity_dates_description: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="validityDatesDescription"),
        pydantic.Field(
            alias="validityDatesDescription", description="Further information about the available validity dates."
        ),
    ] = None
    """
    Further information about the available validity dates.
    """

    validity_dates: typing_extensions.Annotated[
        typing.Optional[typing.List[ValidityDate]],
        FieldMetadata(alias="validityDates"),
        pydantic.Field(
            alias="validityDates",
            description="Definitions of relevant date columns for this connector. e.g.: The publishing date of a movie, and its production period.",
        ),
    ] = None
    """
    Definitions of relevant date columns for this connector. e.g.: The publishing date of a movie, and its production period.
    """

    selects: typing.Optional[typing.List[ConnectorSelectsItem]] = pydantic.Field(default=None)
    """
    Definition of selects available for querying this connector.
    """

    default: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(Connector)
