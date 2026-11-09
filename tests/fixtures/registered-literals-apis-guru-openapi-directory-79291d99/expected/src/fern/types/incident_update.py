

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .incident_update_status import IncidentUpdateStatus


class IncidentUpdate(UniversalBaseModel):
    """
    An update on the health incident
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The content of the update.
    """

    status: typing.Optional[IncidentUpdateStatus] = pydantic.Field(default=None)
    """
    The status of the incident.
    """

    updated_date: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date when the update was published, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format, e.g. `"2020-10-30T15:26:48Z"`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
