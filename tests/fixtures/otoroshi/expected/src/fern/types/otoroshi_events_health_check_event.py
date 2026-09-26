

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .otoroshi_events_health_check_event_error import OtoroshiEventsHealthCheckEventError
from .otoroshi_events_health_check_event_health import OtoroshiEventsHealthCheckEventHealth


class OtoroshiEventsHealthCheckEvent(UniversalBaseModel):
    """
    ???
    """

    error: typing.Optional[OtoroshiEventsHealthCheckEventError] = pydantic.Field(default=None)
    """
    ???
    """

    health: typing.Optional[OtoroshiEventsHealthCheckEventHealth] = pydantic.Field(default=None)
    """
    ???
    """

    logic_check: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="logicCheck"), pydantic.Field(alias="logicCheck", description="???")
    ] = None
    """
    ???
    """

    status: typing.Optional[int] = pydantic.Field(default=None)
    """
    ???
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    ???
    """

    duration: typing.Optional[int] = pydantic.Field(default=None)
    """
    ???
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
