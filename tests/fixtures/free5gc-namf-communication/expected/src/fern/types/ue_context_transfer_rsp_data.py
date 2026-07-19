

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .n2info_content import N2InfoContent
from .ue_context import UeContext


class UeContextTransferRspData(UniversalBaseModel):
    ue_context: typing_extensions.Annotated[
        UeContext, FieldMetadata(alias="ueContext"), pydantic.Field(alias="ueContext")
    ]
    ue_radio_capability: typing_extensions.Annotated[
        typing.Optional[N2InfoContent],
        FieldMetadata(alias="ueRadioCapability"),
        pydantic.Field(alias="ueRadioCapability"),
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
