

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .filter_id import FilterId
from .resolved_concepts_result_resolved_filter_value_item import ResolvedConceptsResultResolvedFilterValueItem
from .table_id import TableId


class ResolvedConceptsResultResolvedFilter(UniversalBaseModel):
    table_id: typing_extensions.Annotated[
        typing.Optional[TableId], FieldMetadata(alias="TableId"), pydantic.Field(alias="TableId")
    ] = None
    filter_id: typing_extensions.Annotated[
        typing.Optional[FilterId], FieldMetadata(alias="FilterId"), pydantic.Field(alias="FilterId")
    ] = None
    value: typing.Optional[typing.List[ResolvedConceptsResultResolvedFilterValueItem]] = pydantic.Field(default=None)
    """
    List of resolved filter values.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
