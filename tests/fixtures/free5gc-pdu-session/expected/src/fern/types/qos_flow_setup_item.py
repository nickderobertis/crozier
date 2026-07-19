

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .qos_flow_profile import QosFlowProfile


class QosFlowSetupItem(UniversalBaseModel):
    qfi: int
    qos_rules: typing_extensions.Annotated[str, FieldMetadata(alias="qosRules"), pydantic.Field(alias="qosRules")]
    ebi: typing.Optional[int] = None
    qos_flow_description: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="qosFlowDescription"), pydantic.Field(alias="qosFlowDescription")
    ] = None
    qos_flow_profile: typing_extensions.Annotated[
        typing.Optional[QosFlowProfile], FieldMetadata(alias="qosFlowProfile"), pydantic.Field(alias="qosFlowProfile")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
