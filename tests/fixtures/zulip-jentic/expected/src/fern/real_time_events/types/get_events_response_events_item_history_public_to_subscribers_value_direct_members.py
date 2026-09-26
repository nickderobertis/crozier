

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetEventsResponseEventsItemHistoryPublicToSubscribersValueDirectMembers(UniversalBaseModel):
    """
    If an object, it will be a [group-setting value][setting-values] with these fields:

    [setting-values]: /api/group-setting-values
    """

    direct_members: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    The list of IDs of individual users in the collection of users with this permission.
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
