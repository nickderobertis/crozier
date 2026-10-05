

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SlackUsergroupActionCreate(UniversalBaseModel):
    """
    Action: Create a new usergroup.
    """

    description: str = pydantic.Field()
    """
    Usergroup description
    """

    usergroup: str = pydantic.Field()
    """
    Usergroup handle/name
    """

    users: typing.List[str] = pydantic.Field()
    """
    List of users to add
    """

    workspace: str = pydantic.Field()
    """
    Workspace name
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
