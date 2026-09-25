

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetEventsResponseEventsItemMutedUsersMutedUsersItem(UniversalBaseModel):
    """
    Object containing the user ID and timestamp of a muted user.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the muted user.
    """

    timestamp: typing.Optional[int] = pydantic.Field(default=None)
    """
    An integer UNIX timestamp representing when the user was muted.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
