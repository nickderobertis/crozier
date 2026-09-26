

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .integration_health import IntegrationHealth


class VerifyIntegrationsResponse(UniversalBaseModel):
    """
    Result of a manual verify/repair pass: the async profile re-push has been started, and the synchronously-computed per-integration health array.
    """

    started: bool = pydantic.Field()
    """
    The async re-push + drift reschedule was triggered.
    """

    health: typing.List[IntegrationHealth]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
