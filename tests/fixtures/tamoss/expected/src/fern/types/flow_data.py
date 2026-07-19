

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .flow_core import FlowCore
from .flow_data_essence_parameters import FlowDataEssenceParameters
from .flow_data_format import FlowDataFormat


class FlowData(FlowCore):
    """
    Describes a data Flow
    """

    format: FlowDataFormat = pydantic.Field()
    """
    The primary content type URN for the Flow.
    """

    essence_parameters: FlowDataEssenceParameters = pydantic.Field()
    """
    Describes the parameters of the essence inside this data Flow
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
