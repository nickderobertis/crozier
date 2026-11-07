

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .value_maps import ValueMaps


class EdgeMessageMetaData(UniversalBaseModel):
    values: ValueMaps
    indexed_values: typing_extensions.Annotated[
        ValueMaps, FieldMetadata(alias="indexedValues"), pydantic.Field(alias="indexedValues")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
