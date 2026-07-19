

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .sm_context_update_error import SmContextUpdateError


class UpdateSmContextResponse404(UniversalBaseModel):
    json_data: typing_extensions.Annotated[
        typing.Optional[SmContextUpdateError], FieldMetadata(alias="jsonData"), pydantic.Field(alias="jsonData")
    ] = None
    binary_data_n1sm_message: typing_extensions.Annotated[
        typing.Optional[bytes],
        FieldMetadata(alias="binaryDataN1SmMessage"),
        pydantic.Field(alias="binaryDataN1SmMessage"),
    ] = None
    binary_data_n2sm_information: typing_extensions.Annotated[
        typing.Optional[bytes],
        FieldMetadata(alias="binaryDataN2SmInformation"),
        pydantic.Field(alias="binaryDataN2SmInformation"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
