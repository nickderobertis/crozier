

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Dbv0037JobReservation(UniversalBaseModel):
    """
    Reservation usage details
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Database id of reservation
    """

    name: typing.Optional[int] = pydantic.Field(default=None)
    """
    Name of reservation
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
