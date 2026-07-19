

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .n2information_transfer_result import N2InformationTransferResult
from .pws_response_data import PwsResponseData


class N2InformationTransferRspData(UniversalBaseModel):
    result: N2InformationTransferResult
    pws_rsp_data: typing_extensions.Annotated[
        typing.Optional[PwsResponseData], FieldMetadata(alias="pwsRspData"), pydantic.Field(alias="pwsRspData")
    ] = None
    supported_features: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="supportedFeatures"), pydantic.Field(alias="supportedFeatures")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
