

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .put_v1trace_response_result_item_type import PutV1TraceResponseResultItemType


class PutV1TraceResponseResultItem(UniversalBaseModel):
    dpid: str = pydantic.Field()
    """
    Switch datapath ID
    """

    port: int = pydantic.Field()
    """
    Incoming port in the switch
    """

    time: str = pydantic.Field()
    """
    Date time when the iteration was computed
    """

    type: PutV1TraceResponseResultItemType = pydantic.Field()
    """
    Type of the step. May be "starting", "intermediary", "last", and "loop".
    """

    vlan: typing.Optional[int] = pydantic.Field(default=None)
    """
    VLAN ID
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
