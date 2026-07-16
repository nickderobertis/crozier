

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TeamMemberBookingProfile(UniversalBaseModel):
    """
    The booking profile of a seller's team member, including the team member's ID, display name, description and whether the team member can be booked as a service provider.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the team member.
    """

    display_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The display name of the team member.
    """

    is_bookable: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether the team member can be booked through the Bookings API or the seller's online booking channel or site (`true) or not (`false`).
    """

    profile_image_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL of the team member's image for the bookings profile.
    """

    team_member_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the [TeamMember](https://developer.squareup.com/reference/square_2021-08-18/objects/TeamMember) object for the team member associated with the booking profile.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
