

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class OcmGroupUser(UniversalBaseModel):
    """
    A single user membership in a cluster group.
    """

    cluster: str = pydantic.Field()
    """
    Cluster name
    """

    group: str = pydantic.Field()
    """
    Group name (e.g. dedicated-admins)
    """

    user: str = pydantic.Field()
    """
    Username
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
