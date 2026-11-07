

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .fleet_connectivity_assurance import FleetConnectivityAssurance
from .fleet_rule import FleetRule


class Fleet(UniversalBaseModel):
    connectivity_assurance: typing.Optional[FleetConnectivityAssurance] = None
    created: dt.datetime = pydantic.Field()
    """
    RFC3339 timestamp in UTC
    """

    environment_variables: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    The environment variables for this device that have been set using the Notehub API or UI.
    """

    label: str = pydantic.Field()
    """
    Fleet label
    """

    smart_rule: typing.Optional[FleetRule] = None
    smart_rule_enabled: typing.Optional[bool] = None
    uid: str = pydantic.Field()
    """
    Fleet UID
    """

    watchdog_mins: typing.Optional[int] = pydantic.Field(default=None)
    """
    A watchdog timer is used to generate an event every N minutes of inactivity. 0 means no watchdog
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
