

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class InvalidInputProperty(UniversalBaseModel):
    invalid_value: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="invalidValue"), pydantic.Field(alias="invalidValue")
    ] = None
    message: typing.Optional[str] = None
    property_path: typing_extensions.Annotated[
        str, FieldMetadata(alias="propertyPath"), pydantic.Field(alias="propertyPath")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
