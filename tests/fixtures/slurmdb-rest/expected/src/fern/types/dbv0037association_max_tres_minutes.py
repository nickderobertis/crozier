

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dbv0037association_max_tres_minutes_per import Dbv0037AssociationMaxTresMinutesPer
from .dbv0037association_max_tres_minutes_total_item import Dbv0037AssociationMaxTresMinutesTotalItem


class Dbv0037AssociationMaxTresMinutes(UniversalBaseModel):
    """
    Max TRES minutes settings
    """

    per: typing.Optional[Dbv0037AssociationMaxTresMinutesPer] = None
    total: typing.Optional[typing.List[Dbv0037AssociationMaxTresMinutesTotalItem]] = pydantic.Field(default=None)
    """
    TRES list of attributes
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
