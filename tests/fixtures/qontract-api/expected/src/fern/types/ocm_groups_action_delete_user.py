

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class OcmGroupsActionDeleteUser(UniversalBaseModel):
    """
    Action: remove a user from a cluster group.
    """

    cluster: str = pydantic.Field()
    """
    Cluster name
    """

    group: str = pydantic.Field()
    """
    Group name
    """

    user: str = pydantic.Field()
    """
    Username to remove
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
