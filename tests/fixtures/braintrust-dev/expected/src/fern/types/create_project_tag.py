

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CreateProjectTag(UniversalBaseModel):
    project_id: str = pydantic.Field()
    """
    Unique identifier for the project that the project tag belongs under
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

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
