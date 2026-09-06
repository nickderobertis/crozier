

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PatchProjectAutomationConfigBtqlFilterAction_Webhook(UniversalBaseModel):
    """
    The action to take when the automation rule is triggered
    """

    type: typing.Literal["webhook"] = "webhook"
    url: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PatchProjectAutomationConfigBtqlFilterAction_Slack(UniversalBaseModel):
    """
    The action to take when the automation rule is triggered
    """

    type: typing.Literal["slack"] = "slack"
    workspace_id: str
    channel: str
    message_template: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


PatchProjectAutomationConfigBtqlFilterAction = typing_extensions.Annotated[
    typing.Union[
        PatchProjectAutomationConfigBtqlFilterAction_Webhook, PatchProjectAutomationConfigBtqlFilterAction_Slack
    ],
    pydantic.Field(discriminator="type"),
]
