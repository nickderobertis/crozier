

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .project_automation_config import ProjectAutomationConfig


class ProjectAutomation(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Unique identifier for the project automation
    """

    project_id: str = pydantic.Field()
    """
    Unique identifier for the project that the project automation belongs under
    """

    user_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Identifies the user who created the project automation
    """

    created: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Date of project automation creation
    """

    name: str = pydantic.Field()
    """
    Name of the project automation
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Textual description of the project automation
    """

    config: ProjectAutomationConfig = pydantic.Field()
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
