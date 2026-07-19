

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ue_context_created_data import UeContextCreatedData


class CreateUeContextResponse201(UniversalBaseModel):
    json_data: typing_extensions.Annotated[
        typing.Optional[UeContextCreatedData], FieldMetadata(alias="jsonData"), pydantic.Field(alias="jsonData")
    ] = None
    binary_data_n1message: typing_extensions.Annotated[
        typing.Optional[bytes], FieldMetadata(alias="binaryDataN1Message"), pydantic.Field(alias="binaryDataN1Message")
    ] = None
    binary_data_n2information: typing_extensions.Annotated[
        typing.Optional[bytes],
        FieldMetadata(alias="binaryDataN2Information"),
        pydantic.Field(alias="binaryDataN2Information"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
