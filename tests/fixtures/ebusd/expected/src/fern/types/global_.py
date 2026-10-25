

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .seconds import Seconds
from .symbol import Symbol


class Global(UniversalBaseModel):
    version: str = pydantic.Field()
    """
    the ebusd version (major.minor.sha1 or major.minor.date).
    """

    updatecheck: typing.Optional[str] = pydantic.Field(default=None)
    """
    the result of update check ("OK" or string describing available updates).
    """

    user: typing.Optional[str] = pydantic.Field(default=None)
    """
    logged in user name.
    """

    access: typing.Optional[str] = pydantic.Field(default=None)
    """
    access level(s) of the logged in user.
    """

    signal: bool = pydantic.Field()
    """
    whether signal is available.
    """

    symbolrate: typing.Optional[int] = pydantic.Field(default=None)
    """
    the current symbol rate on the bus.
    """

    maxsymbolrate: typing.Optional[int] = pydantic.Field(default=None)
    """
    the maximum symbol rate on the bus seen since start.
    """

    minarbitrationmicros: typing.Optional[int] = pydantic.Field(default=None)
    """
    the minimum arbitration delay in microseconds.
    """

    maxarbitrationmicros: typing.Optional[int] = pydantic.Field(default=None)
    """
    the maximum arbitration delay in microseconds.
    """

    minsymbollatency: typing.Optional[int] = pydantic.Field(default=None)
    """
    the minimum symbol latency in milliseconds.
    """

    maxsymbollatency: typing.Optional[int] = pydantic.Field(default=None)
    """
    the maximum symbol latency in milliseconds.
    """

    qq: typing.Optional[Symbol] = pydantic.Field(default=None)
    """
    the ebusd master address (only if not readonly).
    """

    reconnects: int = pydantic.Field()
    """
    the number of reconnects to the device since start.
    """

    masters: int = pydantic.Field()
    """
    the number of masters recognized on the bus.
    """

    messages: int = pydantic.Field()
    """
    the number of known message definitions.
    """

    lastup: Seconds = pydantic.Field()
    """
    the time in UTC seconds of the last update of any message.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
