

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .target import Target


class Canary(UniversalBaseModel):
    """
    The configuration of the canary mode for a service descriptor
    """

    enabled: bool = pydantic.Field()
    """
    Use canary mode for this service
    """

    root: str = pydantic.Field()
    """
    Otoroshi will append this root to any target choosen. If the specified root is '/api/foo', then a request to https://yyyyyyy/bar will actually hit https://xxxxxxxxx/api/foo/bar
    """

    targets: typing.List[Target] = pydantic.Field()
    """
    The list of target that Otoroshi will proxy and expose through the subdomain defined before. Otoroshi will do round-robin load balancing between all those targets with circuit breaker mecanism to avoid cascading failures
    """

    traffic: int = pydantic.Field()
    """
    Ratio of traffic that will be sent to canary targets.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
