

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .attribute_filter import AttributeFilter
from .term_code import TermCode
from .time_restriction import TimeRestriction
from .value_filter import ValueFilter


class Criterion(UniversalBaseModel):
    term_codes: typing_extensions.Annotated[
        typing.List[TermCode], FieldMetadata(alias="termCodes"), pydantic.Field(alias="termCodes")
    ]
    attribute_filters: typing_extensions.Annotated[
        typing.Optional[typing.List[AttributeFilter]],
        FieldMetadata(alias="attributeFilters"),
        pydantic.Field(alias="attributeFilters"),
    ] = None
    value_filter: typing_extensions.Annotated[
        typing.Optional[ValueFilter], FieldMetadata(alias="valueFilter"), pydantic.Field(alias="valueFilter")
    ] = None
    time_restriction: typing_extensions.Annotated[
        typing.Optional[TimeRestriction],
        FieldMetadata(alias="timeRestriction"),
        pydantic.Field(alias="timeRestriction"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
