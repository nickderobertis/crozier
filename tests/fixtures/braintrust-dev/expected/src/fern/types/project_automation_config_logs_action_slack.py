

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ProjectAutomationConfigLogsActionSlack(UniversalBaseModel):
    workspace_id: str = pydantic.Field()
    """
    The Slack workspace ID to post to
    """

    channel: str = pydantic.Field()
    """
    The Slack channel ID to post to
    """

    message_template: typing.Optional[str] = pydantic.Field(default=None)
    """
    Custom message template for the alert
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
