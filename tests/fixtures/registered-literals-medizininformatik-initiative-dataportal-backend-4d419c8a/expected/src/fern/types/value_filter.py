

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .term_code import TermCode
from .unit import Unit
from .value_filter_comparator import ValueFilterComparator
from .value_filter_type import ValueFilterType


class ValueFilter(UniversalBaseModel):
    """
    A ValueFilter requires different properties, depending on the type. Please refer to the JSON Schema for this.
    """

    type: ValueFilterType
    selected_concepts: typing_extensions.Annotated[
        typing.Optional[typing.List[TermCode]],
        FieldMetadata(alias="selectedConcepts"),
        pydantic.Field(alias="selectedConcepts"),
    ] = None
    comparator: typing.Optional[ValueFilterComparator] = None
    unit: typing.Optional[Unit] = None
    value: typing.Optional[float] = None
    min_value: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="minValue"), pydantic.Field(alias="minValue")
    ] = None
    max_value: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="maxValue"), pydantic.Field(alias="maxValue")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
