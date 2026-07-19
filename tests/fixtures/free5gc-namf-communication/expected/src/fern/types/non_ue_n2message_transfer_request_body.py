

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .n2information_transfer_req_data import N2InformationTransferReqData


class NonUeN2MessageTransferRequestBody(UniversalBaseModel):
    json_data: typing_extensions.Annotated[
        typing.Optional[N2InformationTransferReqData], FieldMetadata(alias="jsonData"), pydantic.Field(alias="jsonData")
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
