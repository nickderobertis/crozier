

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetEventsResponseEventsItemTwoPersonRole(UniversalBaseModel):
    """
    When the [role](/help/user-roles) of a user changes.
    """

    user_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the user affected by this change.
    """

    role: typing.Optional[int] = pydantic.Field(default=None)
    """
    The new [role](/api/roles-and-permissions) of the user.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
