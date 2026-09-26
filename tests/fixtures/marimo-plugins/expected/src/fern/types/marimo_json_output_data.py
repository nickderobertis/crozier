

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .marimo_json_output_data_value_types import MarimoJsonOutputDataValueTypes


class MarimoJsonOutputData(UniversalBaseModel):
    name: typing.Optional[str] = None
    json_data: typing_extensions.Annotated[
        typing.Any, FieldMetadata(alias="jsonData"), pydantic.Field(alias="jsonData")
    ]
    value_types: typing_extensions.Annotated[
        typing.Optional[MarimoJsonOutputDataValueTypes],
        FieldMetadata(alias="valueTypes"),
        pydantic.Field(alias="valueTypes"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
