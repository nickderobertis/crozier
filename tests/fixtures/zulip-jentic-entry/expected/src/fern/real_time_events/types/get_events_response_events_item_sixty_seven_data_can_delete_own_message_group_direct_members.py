

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetEventsResponseEventsItemSixtySevenDataCanDeleteOwnMessageGroupDirectMembers(UniversalBaseModel):
    """
    An object with these fields:
    """

    direct_members: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    The list of IDs of individual users in the collection of users with this permission.
    
    **Changes**: Prior to Zulip 10.0 (feature level 303), this list would include
    deactivated users who had the permission before being deactivated.
    """

    direct_subgroups: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    The list of IDs of the groups in the collection of users with this permission.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
