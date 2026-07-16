

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .action import Action
from .filter_type import FilterType
from .interface_descriptor import InterfaceDescriptor
from .traffic_filter import TrafficFilter


class TrafficRuleDescriptor(UniversalBaseModel):
    action: Action
    dst_interface: typing_extensions.Annotated[
        typing.Optional[typing.List[InterfaceDescriptor]],
        FieldMetadata(alias="dstInterface"),
        pydantic.Field(alias="dstInterface"),
    ] = None
    filter_type: typing_extensions.Annotated[
        FilterType, FieldMetadata(alias="filterType"), pydantic.Field(alias="filterType")
    ]
    priority: int = pydantic.Field()
    """
    Priority of this traffic rule. If traffic rule conflicts, the one with higher priority take precedence.
    """

    traffic_filter: typing_extensions.Annotated[
        typing.List[TrafficFilter],
        FieldMetadata(alias="trafficFilter"),
        pydantic.Field(
            alias="trafficFilter",
            description="The filter used to identify specific flow/packets that need to be handled by the MEC host.",
        ),
    ]
    """
    The filter used to identify specific flow/packets that need to be handled by the MEC host.
    """

    traffic_rule_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="trafficRuleId"),
        pydantic.Field(alias="trafficRuleId", description="Identifies the traffic rule."),
    ]
    """
    Identifies the traffic rule.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
