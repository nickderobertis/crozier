

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .satellite_data_usage import SatelliteDataUsage


class SatellitePlan(UniversalBaseModel):
    activated: int = pydantic.Field()
    """
    Activation date of the satellite plan as Unix timestamp
    """

    last_session_at: typing.Optional[int] = pydantic.Field(default=None)
    """
    When this Starnote last had a session
    """

    minimum_billable_bytes: typing.Optional[int] = pydantic.Field(default=None)
    """
    Minimum billable bytes
    """

    ntn_provider: str = pydantic.Field()
    """
    Non-Terrestrial Network provider name
    """

    psid: str = pydantic.Field()
    """
    Provider-specific identifier for the satellite subscription
    """

    satellite_data_usage: typing.Optional[SatelliteDataUsage] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
