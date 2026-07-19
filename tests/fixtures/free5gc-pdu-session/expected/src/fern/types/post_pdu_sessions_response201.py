

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .pdu_session_created_data import PduSessionCreatedData


class PostPduSessionsResponse201(UniversalBaseModel):
    json_data: typing_extensions.Annotated[
        typing.Optional[PduSessionCreatedData], FieldMetadata(alias="jsonData"), pydantic.Field(alias="jsonData")
    ] = None
    binary_data_n1sm_info_to_ue: typing_extensions.Annotated[
        typing.Optional[bytes],
        FieldMetadata(alias="binaryDataN1SmInfoToUe"),
        pydantic.Field(alias="binaryDataN1SmInfoToUe"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
