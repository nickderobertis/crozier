

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class QosFlowReleaseRequestItem(UniversalBaseModel):
    qfi: int
    qos_rules: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="qosRules"), pydantic.Field(alias="qosRules")
    ] = None
    qos_flow_description: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="qosFlowDescription"), pydantic.Field(alias="qosFlowDescription")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
