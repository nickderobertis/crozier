

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .horizontal_accuracy import HorizontalAccuracy
from .lat import Lat
from .lon import Lon


class TransactionFullLocation(UniversalBaseModel):
    """
    Details of the payment location as received from the payment terminal.
    """

    lat: typing.Optional[Lat] = None
    lon: typing.Optional[Lon] = None
    horizontal_accuracy: typing.Optional[HorizontalAccuracy] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
