

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AppointmentSegment(UniversalBaseModel):
    """
    Defines an appointment segment of a booking.
    """

    duration_minutes: int = pydantic.Field()
    """
    The time span in minutes of an appointment segment.
    """

    service_variation_id: str = pydantic.Field()
    """
    The ID of the [CatalogItemVariation](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItemVariation) object representing the service booked in this segment.
    """

    service_variation_version: int = pydantic.Field()
    """
    The current version of the item variation representing the service booked in this segment.
    """

    team_member_id: str = pydantic.Field()
    """
    The ID of the [TeamMember](https://developer.squareup.com/reference/square_2021-08-18/objects/TeamMember) object representing the team member booked in this segment.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
