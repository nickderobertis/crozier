

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .term_code import TermCode
from .unit import Unit


class AttributeDefinition(UniversalBaseModel):
    allowed_units: typing_extensions.Annotated[
        typing.Optional[typing.List[Unit]], FieldMetadata(alias="allowedUnits"), pydantic.Field(alias="allowedUnits")
    ] = None
    attribute_code: typing_extensions.Annotated[
        typing.Optional[TermCode], FieldMetadata(alias="attributeCode"), pydantic.Field(alias="attributeCode")
    ] = None
    max: typing.Optional[float] = None
    min: typing.Optional[float] = None
    optional: typing.Optional[bool] = None
    precision: typing.Optional[float] = None
    referenced_criteria_set: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="referencedCriteriaSet"),
        pydantic.Field(alias="referencedCriteriaSet"),
    ] = None
    referenced_value_set: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="referencedValueSet"),
        pydantic.Field(alias="referencedValueSet"),
    ] = None
    type: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
