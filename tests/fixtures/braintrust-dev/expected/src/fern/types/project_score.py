

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .project_score_categories import ProjectScoreCategories
from .project_score_config import ProjectScoreConfig
from .project_score_type import ProjectScoreType


class ProjectScore(UniversalBaseModel):
    """
    A project score is a user-configured score, which can be manually-labeled through the UI
    """

    id: str = pydantic.Field()
    """
    Unique identifier for the project score
    """

    project_id: str = pydantic.Field()
    """
    Unique identifier for the project that the project score belongs under
    """

    user_id: str
    created: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Date of project score creation
    """

    name: str = pydantic.Field()
    """
    Name of the project score
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Textual description of the project score
    """

    score_type: ProjectScoreType
    categories: typing.Optional[ProjectScoreCategories] = None
    config: typing.Optional[ProjectScoreConfig] = None
    position: typing.Optional[str] = pydantic.Field(default=None)
    """
    An optional LexoRank-based string that sets the sort position for the score in the UI
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
