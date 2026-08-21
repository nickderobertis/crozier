

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PutV1TracesRequestItemTraceSwitch(UniversalBaseModel):
    dpid: str = pydantic.Field()
    """
    Initial switch datapath ID
    """

    in_port: int = pydantic.Field()
    """
    Starting incoming port
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
