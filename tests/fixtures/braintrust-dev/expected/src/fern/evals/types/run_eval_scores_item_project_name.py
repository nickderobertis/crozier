

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RunEvalScoresItemProjectName(UniversalBaseModel):
    """
    Project name and slug
    """

    project_name: str = pydantic.Field()
    """
    The name of the project containing the function
    """

    slug: str = pydantic.Field()
    """
    The slug of the function
    """

    version: typing.Optional[str] = pydantic.Field(default=None)
    """
    The version of the function
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
