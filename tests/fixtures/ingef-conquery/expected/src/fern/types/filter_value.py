

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .filter_id import FilterId
from .filter_value_integer_range_value import FilterValueIntegerRangeValue
from .filter_value_number_range_value import FilterValueNumberRangeValue


class FilterValue_IntegerRange(UniversalBaseModel):
    """
    Reference to a filter, and parameters for filtering with it. Note that the filter is included by reference, and its actual logic is described in the defining concept.
    """

    type: typing.Literal["INTEGER_RANGE"] = "INTEGER_RANGE"
    value: typing.Optional[FilterValueIntegerRangeValue] = None
    filter: typing.Optional[FilterId] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FilterValue_RealRange(UniversalBaseModel):
    """
    Reference to a filter, and parameters for filtering with it. Note that the filter is included by reference, and its actual logic is described in the defining concept.
    """

    type: typing.Literal["REAL_RANGE"] = "REAL_RANGE"
    value: typing.Optional[FilterValueNumberRangeValue] = None
    filter: typing.Optional[FilterId] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FilterValue_MoneyRange(UniversalBaseModel):
    """
    Reference to a filter, and parameters for filtering with it. Note that the filter is included by reference, and its actual logic is described in the defining concept.
    """

    type: typing.Literal["MONEY_RANGE"] = "MONEY_RANGE"
    value: typing.Optional[FilterValueNumberRangeValue] = None
    filter: typing.Optional[FilterId] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FilterValue_DecimalRange(UniversalBaseModel):
    """
    Reference to a filter, and parameters for filtering with it. Note that the filter is included by reference, and its actual logic is described in the defining concept.
    """

    type: typing.Literal["DECIMAL_RANGE"] = "DECIMAL_RANGE"
    value: typing.Optional[FilterValueNumberRangeValue] = None
    filter: typing.Optional[FilterId] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FilterValue_Integer(UniversalBaseModel):
    """
    Reference to a filter, and parameters for filtering with it. Note that the filter is included by reference, and its actual logic is described in the defining concept.
    """

    type: typing.Literal["INTEGER"] = "INTEGER"
    value: typing.Optional[int] = None
    filter: typing.Optional[FilterId] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FilterValue_String(UniversalBaseModel):
    """
    Reference to a filter, and parameters for filtering with it. Note that the filter is included by reference, and its actual logic is described in the defining concept.
    """

    type: typing.Literal["STRING"] = "STRING"
    value: typing.Optional[str] = None
    filter: typing.Optional[FilterId] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FilterValue_Select(UniversalBaseModel):
    """
    Reference to a filter, and parameters for filtering with it. Note that the filter is included by reference, and its actual logic is described in the defining concept.
    """

    type: typing.Literal["SELECT"] = "SELECT"
    value: typing.Optional[str] = None
    filter: typing.Optional[FilterId] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FilterValue_BigMultiSelect(UniversalBaseModel):
    """
    Reference to a filter, and parameters for filtering with it. Note that the filter is included by reference, and its actual logic is described in the defining concept.
    """

    type: typing.Literal["BIG_MULTI_SELECT"] = "BIG_MULTI_SELECT"
    value: typing.Optional[typing.List[str]] = None
    filter: typing.Optional[FilterId] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FilterValue_MultiSelect(UniversalBaseModel):
    """
    Reference to a filter, and parameters for filtering with it. Note that the filter is included by reference, and its actual logic is described in the defining concept.
    """

    type: typing.Literal["MULTI_SELECT"] = "MULTI_SELECT"
    value: typing.Optional[typing.List[str]] = None
    filter: typing.Optional[FilterId] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


FilterValue = typing_extensions.Annotated[
    typing.Union[
        FilterValue_IntegerRange,
        FilterValue_RealRange,
        FilterValue_MoneyRange,
        FilterValue_DecimalRange,
        FilterValue_Integer,
        FilterValue_String,
        FilterValue_Select,
        FilterValue_BigMultiSelect,
        FilterValue_MultiSelect,
    ],
    pydantic.Field(discriminator="type"),
]
