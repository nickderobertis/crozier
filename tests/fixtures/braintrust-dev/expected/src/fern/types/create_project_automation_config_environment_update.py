

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_project_automation_config_environment_update_action import (
    CreateProjectAutomationConfigEnvironmentUpdateAction,
)


class CreateProjectAutomationConfigEnvironmentUpdate(UniversalBaseModel):
    environment_filter: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Optional list of environment slugs to filter by
    """

    action: CreateProjectAutomationConfigEnvironmentUpdateAction = pydantic.Field()
    """
    The action to take when the automation rule is triggered
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
