

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DelayedExceptionHandler(UniversalBaseModel):
    """
    Allows to ignore an exception for an established
    period of time after which it is raised.

    This use case most commonly occurs when dealing with
    external systems.
    For example, due to poor network  performance or
    network congestion, an external system which is healthy,
    currently is not reachable any longer.
    A possible solution:
    - ignore exceptions for an interval in which the
        system usually is reachable again by not
        raising the error
    - if the error persist give up and raise it

    Example code usage:

        delayed_handler_external_service = DelayedExceptionHandler(
            delay_for=60
        )
        try:
            function_called_periodically_accessing_external_service()
        except TargetException as e:
            delayed_handler_external_service.try_to_raise(e)
        else:
            delayed_handler_external_service.else_reset()
    """

    delay_for: float = pydantic.Field()
    """
    interval of time during which exceptions are ignored
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
