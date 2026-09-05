

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .project_settings import ProjectSettings


class Project(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Unique identifier for the project
    """

    org_id: str = pydantic.Field()
    """
    Unique id for the organization that the project belongs under
    """

    name: str = pydantic.Field()
    """
    Name of the project
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Textual description of the project
    """

    created: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Date of project creation
    """

    deleted_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Date of project deletion, or null if the project is still active
    """

    user_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Identifies the user who created the project
    """

    settings: typing.Optional[ProjectSettings] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
