

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ErrorResponse(UniversalBaseModel):
    error: str = pydantic.Field()
    """
    Fehlercode
    """

    message: str = pydantic.Field()
    """
    Fehlerbeschreibung
    """

    timestamp: dt.datetime = pydantic.Field()
    """
    Zeitstempel des Fehlers
    """

    details: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Zusätzliche Fehlerdetails
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
