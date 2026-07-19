

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .additional_qos_flow_info import AdditionalQosFlowInfo
from .arp import Arp
from .dynamic5qi import Dynamic5Qi
from .gbr_qos_flow_information import GbrQosFlowInformation
from .non_dynamic5qi import NonDynamic5Qi
from .reflective_qo_s_attribute import ReflectiveQoSAttribute


class QosFlowProfile(UniversalBaseModel):
    f_5qi: typing_extensions.Annotated[int, FieldMetadata(alias="5qi"), pydantic.Field(alias="5qi")]
    non_dynamic5qi: typing_extensions.Annotated[
        typing.Optional[NonDynamic5Qi], FieldMetadata(alias="nonDynamic5Qi"), pydantic.Field(alias="nonDynamic5Qi")
    ] = None
    dynamic5qi: typing_extensions.Annotated[
        typing.Optional[Dynamic5Qi], FieldMetadata(alias="dynamic5Qi"), pydantic.Field(alias="dynamic5Qi")
    ] = None
    arp: typing.Optional[Arp] = None
    gbr_qos_flow_info: typing_extensions.Annotated[
        typing.Optional[GbrQosFlowInformation],
        FieldMetadata(alias="gbrQosFlowInfo"),
        pydantic.Field(alias="gbrQosFlowInfo"),
    ] = None
    rqa: typing.Optional[ReflectiveQoSAttribute] = None
    additional_qos_flow_info: typing_extensions.Annotated[
        typing.Optional[AdditionalQosFlowInfo],
        FieldMetadata(alias="additionalQosFlowInfo"),
        pydantic.Field(alias="additionalQosFlowInfo"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
