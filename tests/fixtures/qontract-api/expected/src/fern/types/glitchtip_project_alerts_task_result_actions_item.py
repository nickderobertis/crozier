

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GlitchtipProjectAlertsTaskResultActionsItem_Create(UniversalBaseModel):
    action_type: typing.Literal["create"] = "create"
    alert_name: str
    instance: str
    organization: str
    project: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GlitchtipProjectAlertsTaskResultActionsItem_Delete(UniversalBaseModel):
    action_type: typing.Literal["delete"] = "delete"
    alert_name: str
    instance: str
    organization: str
    project: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GlitchtipProjectAlertsTaskResultActionsItem_Update(UniversalBaseModel):
    action_type: typing.Literal["update"] = "update"
    alert_name: str
    instance: str
    organization: str
    project: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


GlitchtipProjectAlertsTaskResultActionsItem = typing_extensions.Annotated[
    typing.Union[
        GlitchtipProjectAlertsTaskResultActionsItem_Create,
        GlitchtipProjectAlertsTaskResultActionsItem_Delete,
        GlitchtipProjectAlertsTaskResultActionsItem_Update,
    ],
    pydantic.Field(discriminator="action_type"),
]
