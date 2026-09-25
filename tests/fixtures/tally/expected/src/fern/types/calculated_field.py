

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .calculated_field_type import CalculatedFieldType
from .calculated_field_value import CalculatedFieldValue
from .name import Name


class CalculatedField(UniversalBaseModel):
    uuid_: typing_extensions.Annotated[str, FieldMetadata(alias="uuid"), pydantic.Field(alias="uuid")]
    name: Name = pydantic.Field()
    """
    Name your calculated field to easily retrieve it in calculations later on.
    """

    type: CalculatedFieldType
    value: CalculatedFieldValue = pydantic.Field()
    """
    An initial value as a starting point of your calculation. This can be zero (for numbers) or left blank (for text).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
