

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .secret import Secret
from .slack_usergroup import SlackUsergroup


class SlackWorkspace(UniversalBaseModel):
    """
    A Slack workspace with its token and usergroups.
    """

    managed_usergroups: typing.List[str] = pydantic.Field()
    """
    This list shows the usergroup handles/names managed by qontract-api. Any user group not included here will be abandoned during reconciliation.
    """

    name: str = pydantic.Field()
    """
    Workspace name (unique identifier)
    """

    token: Secret = pydantic.Field()
    """
    Secret reference for the Slack workspace token
    """

    usergroups: typing.List[SlackUsergroup] = pydantic.Field()
    """
    List of usergroups in this workspace
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
