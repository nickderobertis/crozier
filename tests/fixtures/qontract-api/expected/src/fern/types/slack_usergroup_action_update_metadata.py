

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SlackUsergroupActionUpdateMetadata(UniversalBaseModel):
    """
    Action: Update usergroup channels.
    """

    channels: typing.List[str] = pydantic.Field()
    """
    Usergroup channels
    """

    description: str = pydantic.Field()
    """
    Usergroup description
    """

    usergroup: str = pydantic.Field()
    """
    Usergroup handle/name
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
