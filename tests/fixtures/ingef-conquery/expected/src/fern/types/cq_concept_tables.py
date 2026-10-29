

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .connector_id import ConnectorId
from .cq_concept_tables_date_column import CqConceptTablesDateColumn
from .filter_value import FilterValue
from .select_id import SelectId


class CqConceptTables(UniversalBaseModel):
    id: typing_extensions.Annotated[
        typing.Optional[ConnectorId], FieldMetadata(alias="Id"), pydantic.Field(alias="Id")
    ] = None
    date_column: typing_extensions.Annotated[
        typing.Optional[CqConceptTablesDateColumn],
        FieldMetadata(alias="dateColumn"),
        pydantic.Field(
            alias="dateColumn", description="Allows the selection of one of pre-defined date for date-restrictions."
        ),
    ] = None
    """
    Allows the selection of one of pre-defined date for date-restrictions.
    """

    filters: typing.Optional[typing.List[FilterValue]] = None
    selects: typing.Optional[typing.List[SelectId]] = pydantic.Field(default=None)
    """
    References to Selects to evaluate while querying.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
