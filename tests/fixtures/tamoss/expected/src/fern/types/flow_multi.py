

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .flow_core import FlowCore
from .flow_multi_format import FlowMultiFormat


class FlowMulti(FlowCore):
    """
    Describes a multi-essence Flow
    """

    format: FlowMultiFormat = pydantic.Field()
    """
    The primary content type URN for the Flow.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
