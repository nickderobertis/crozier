

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .data_id import DataId
from .privacy_zone_id import PrivacyZoneId


class PrivacyZoneData(UniversalBaseModel):
    """
    Describe the privacy zone information related to the DataProvider and PrivateData
    """

    private_data: DataId
    zones: typing.List[PrivacyZoneId] = pydantic.Field()
    """
    Collection of permitted privacy zones
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
