

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .qos_flow_usage_report import QosFlowUsageReport
from .rat_type import RatType


class SecondaryRatUsageReport(UniversalBaseModel):
    secondary_rat_type: typing_extensions.Annotated[
        RatType, FieldMetadata(alias="secondaryRatType"), pydantic.Field(alias="secondaryRatType")
    ]
    qos_flows_usage_data: typing_extensions.Annotated[
        typing.List[QosFlowUsageReport],
        FieldMetadata(alias="qosFlowsUsageData"),
        pydantic.Field(alias="qosFlowsUsageData"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
