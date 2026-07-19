

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .access_type import AccessType
from .n1message_container import N1MessageContainer
from .plmn_id import PlmnId
from .transfer_reason import TransferReason


class UeContextTransferReqData(UniversalBaseModel):
    reason: TransferReason
    access_type: typing_extensions.Annotated[
        AccessType, FieldMetadata(alias="accessType"), pydantic.Field(alias="accessType")
    ]
    plmn_id: typing_extensions.Annotated[
        typing.Optional[PlmnId], FieldMetadata(alias="plmnId"), pydantic.Field(alias="plmnId")
    ] = None
    reg_request: typing_extensions.Annotated[
        typing.Optional[N1MessageContainer], FieldMetadata(alias="regRequest"), pydantic.Field(alias="regRequest")
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
