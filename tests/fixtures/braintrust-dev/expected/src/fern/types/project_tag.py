

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ProjectTag(UniversalBaseModel):
    """
    A project tag is a user-configured tag for tracking and filtering your experiments, logs, and other data
    """

    id: str = pydantic.Field()
    """
    Unique identifier for the project tag
    """

    project_id: str = pydantic.Field()
    """
    Unique identifier for the project that the project tag belongs under
    """

    user_id: str
    created: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Date of project tag creation
    """

    name: str = pydantic.Field()
    """
    Name of the project tag
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Textual description of the project tag
    """

    color: typing.Optional[str] = pydantic.Field(default=None)
    """
    Color of the tag for the UI
    """

    position: typing.Optional[str] = pydantic.Field(default=None)
    """
    An optional LexoRank-based string that sets the sort position for the tag in the UI
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
