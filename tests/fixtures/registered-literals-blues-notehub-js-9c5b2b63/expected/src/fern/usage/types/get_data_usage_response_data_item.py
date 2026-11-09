

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.usage_data import UsageData
from .get_data_usage_response_data_item_type import GetDataUsageResponseDataItemType


class GetDataUsageResponseDataItem(UniversalBaseModel):
    data: typing.List[UsageData]
    device: typing.Optional[str] = pydantic.Field(default=None)
    """
    The device UID this usage data belongs to (only present when aggregate is 'device')
    """

    device_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    the number of devices represented by this data point
    """

    fleet: typing.Optional[str] = pydantic.Field(default=None)
    """
    The fleet UID this usage data belongs to (only present when aggregate is 'fleet')
    """

    iccid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ICCID of the cellular SIM card (only present when type is 'cellular')
    """

    psid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The PSID (Packet Service ID) of the satellite (or other packet-based device)
    """

    type: GetDataUsageResponseDataItemType = pydantic.Field()
    """
    The type of connectivity
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
