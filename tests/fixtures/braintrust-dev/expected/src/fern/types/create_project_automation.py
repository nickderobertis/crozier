

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_project_automation_config import CreateProjectAutomationConfig


class CreateProjectAutomation(UniversalBaseModel):
    project_id: str = pydantic.Field()
    """
    Unique identifier for the project that the project automation belongs under
    """

    name: str = pydantic.Field()
    """
    Name of the project automation
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Textual description of the project automation
    """

    config: CreateProjectAutomationConfig = pydantic.Field()
    """
    The configuration for the automation rule
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
