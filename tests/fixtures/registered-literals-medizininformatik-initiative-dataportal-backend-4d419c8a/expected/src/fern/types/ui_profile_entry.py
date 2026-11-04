

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .attribute_definition import AttributeDefinition


class UiProfileEntry(UniversalBaseModel):
    attribute_definitions: typing_extensions.Annotated[
        typing.Optional[typing.List[AttributeDefinition]],
        FieldMetadata(alias="attributeDefinitions"),
        pydantic.Field(alias="attributeDefinitions"),
    ] = None
    name: typing.Optional[str] = None
    time_restriction_allowed: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="timeRestrictionAllowed"),
        pydantic.Field(alias="timeRestrictionAllowed"),
    ] = None
    value_definition: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="valueDefinition"), pydantic.Field(alias="valueDefinition")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
