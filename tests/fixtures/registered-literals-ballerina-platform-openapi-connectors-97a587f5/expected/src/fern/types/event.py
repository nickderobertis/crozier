

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .log_level import LogLevel
from .type_discriminator import TypeDiscriminator


class Event(UniversalBaseModel):
    object: typing.Optional[TypeDiscriminator] = None
    created_at: int = pydantic.Field()
    """
    A timestamp when this event was created (in unix epochs).
    """

    level: LogLevel
    message: str = pydantic.Field()
    """
    The message describing the event. This can be a change of state, e.g., enqueued, started, failed or completed, or other events like uploaded results.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
