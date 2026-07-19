

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .pdu_session_create_data import PduSessionCreateData


class PostPduSessionsRequestBody(UniversalBaseModel):
    json_data: typing_extensions.Annotated[
        typing.Optional[PduSessionCreateData], FieldMetadata(alias="jsonData"), pydantic.Field(alias="jsonData")
    ] = None
    binary_data_n1sm_info_from_ue: typing_extensions.Annotated[
        typing.Optional[bytes],
        FieldMetadata(alias="binaryDataN1SmInfoFromUe"),
        pydantic.Field(alias="binaryDataN1SmInfoFromUe"),
    ] = None
    binary_data_unknown_n1sm_info: typing_extensions.Annotated[
        typing.Optional[bytes],
        FieldMetadata(alias="binaryDataUnknownN1SmInfo"),
        pydantic.Field(alias="binaryDataUnknownN1SmInfo"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
