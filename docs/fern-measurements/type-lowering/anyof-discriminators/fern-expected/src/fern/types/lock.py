

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .lock_crew import LockCrew
from .lock_gate import LockGate
from .lock_paddle import LockPaddle
from .lock_relief import LockRelief
from .lock_sensor import LockSensor
from .lockkeeper import Lockkeeper


class Lock(UniversalBaseModel):
    id: str
    gate: LockGate = pydantic.Field()
    """
    A typed, required tag under an anyOf mapping.
    """

    paddle: typing.Optional[LockPaddle] = pydantic.Field(default=None)
    """
    Typeless enum tags under an anyOf mapping.
    """

    sensor: typing.Optional[LockSensor] = pydantic.Field(default=None)
    """
    A mapping naming one member twice, whose tag is unrequired.
    """

    crew: typing.Optional[LockCrew] = pydantic.Field(default=None)
    """
    A typed, required tag under an anyOf without a mapping.
    """

    warden: typing.Optional[Lockkeeper] = pydantic.Field(default=None)
    """
    One referenced member under an unmapped discriminator.
    """

    relief: typing.Optional[LockRelief] = pydantic.Field(default=None)
    """
    One referenced member under a mapped discriminator.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
