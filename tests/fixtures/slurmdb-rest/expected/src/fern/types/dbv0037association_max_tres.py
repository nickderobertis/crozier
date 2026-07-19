

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dbv0037association_max_tres_minutes import Dbv0037AssociationMaxTresMinutes
from .dbv0037association_max_tres_per import Dbv0037AssociationMaxTresPer
from .dbv0037association_max_tres_total_item import Dbv0037AssociationMaxTresTotalItem


class Dbv0037AssociationMaxTres(UniversalBaseModel):
    """
    Max TRES settings
    """

    per: typing.Optional[Dbv0037AssociationMaxTresPer] = None
    total: typing.Optional[typing.List[Dbv0037AssociationMaxTresTotalItem]] = pydantic.Field(default=None)
    """
    TRES list of attributes
    """

    minutes: typing.Optional[Dbv0037AssociationMaxTresMinutes] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
