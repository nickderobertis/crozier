

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ParametersRow(UniversalBaseModel):
    description: str
    display_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="displayName"), pydantic.Field(alias="displayName")
    ]
    id: int
    is_core: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isCore"), pydantic.Field(alias="isCore")
    ] = None
    max_color_value: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="maxColorValue"), pydantic.Field(alias="maxColorValue")
    ] = None
    name: str
    preferred_unit: typing_extensions.Annotated[
        str, FieldMetadata(alias="preferredUnit"), pydantic.Field(alias="preferredUnit")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
