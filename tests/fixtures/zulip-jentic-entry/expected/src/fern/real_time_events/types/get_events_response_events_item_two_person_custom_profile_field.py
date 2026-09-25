

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_events_response_events_item_two_person_custom_profile_field_custom_profile_field import (
    GetEventsResponseEventsItemTwoPersonCustomProfileFieldCustomProfileField,
)


class GetEventsResponseEventsItemTwoPersonCustomProfileField(UniversalBaseModel):
    """
    When the user updates one of their custom profile
    fields.
    """

    user_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the user affected by this change.
    """

    custom_profile_field: typing.Optional[GetEventsResponseEventsItemTwoPersonCustomProfileFieldCustomProfileField] = (
        pydantic.Field(default=None)
    )
    """
    Object containing details about the custom
    profile data change.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
