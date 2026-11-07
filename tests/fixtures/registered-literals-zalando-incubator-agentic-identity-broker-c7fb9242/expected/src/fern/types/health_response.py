

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .health_response_status import HealthResponseStatus


class HealthResponse(UniversalBaseModel):
    status: HealthResponseStatus = pydantic.Field()
    """
    Current health state of the server:
    
    - `healthy`: Operational and processing requests
    - `starting`: Initializing (binding port, setting up routes)
    - `shutting_down`: Graceful shutdown in progress
    - `unhealthy`: Error state, requires restart
    """

    timestamp: dt.datetime = pydantic.Field()
    """
    ISO 8601 timestamp of the health check (UTC)
    """

    uptime_seconds: int = pydantic.Field()
    """
    Number of seconds since the server started accepting requests
    """

    components: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Optional component-level health details.
    
    In proxy and hybrid OAuth2 modes, `upstream_jwks` reports the upstream JWKS refresh state:
    
    - `healthy`: Upstream key material is reachable and fresh
    - `degraded`: Upstream refresh has failed or become stale
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
