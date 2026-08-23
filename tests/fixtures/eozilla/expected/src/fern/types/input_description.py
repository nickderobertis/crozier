

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, update_forward_refs
from ..core.serialization import FieldMetadata
from .description_type import DescriptionType
from .input_description_max_occurs import InputDescriptionMaxOccurs


class InputDescription(DescriptionType):
    min_occurs: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="minOccurs"), pydantic.Field(alias="minOccurs")
    ] = None
    max_occurs: typing_extensions.Annotated[
        typing.Optional[InputDescriptionMaxOccurs], FieldMetadata(alias="maxOccurs"), pydantic.Field(alias="maxOccurs")
    ] = None
    schema_: typing_extensions.Annotated["Schema", FieldMetadata(alias="schema"), pydantic.Field(alias="schema")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .schema import Schema
from .schema_additional_properties import SchemaAdditionalProperties
from .schema_discriminator import SchemaDiscriminator
from .schema_items import SchemaItems

update_forward_refs(
    InputDescription,
    Schema=Schema,
    SchemaAdditionalProperties=SchemaAdditionalProperties,
    SchemaDiscriminator=SchemaDiscriminator,
    SchemaItems=SchemaItems,
)
