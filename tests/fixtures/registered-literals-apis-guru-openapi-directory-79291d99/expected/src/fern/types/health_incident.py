

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .incident_update import IncidentUpdate


class HealthIncident(UniversalBaseModel):
    """
    A status health incident
    """

    end_date: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The end date of the incident, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format, e.g. `"2020-10-30T15:26:48Z"`.
    """

    incident_updates: typing.List[IncidentUpdate] = pydantic.Field()
    """
    Updates on the health incident.
    """

    start_date: dt.datetime = pydantic.Field()
    """
    The start date of the incident, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format, e.g. `"2020-10-30T15:26:48Z"`.
    """

    title: str = pydantic.Field()
    """
    The title of the incident
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
