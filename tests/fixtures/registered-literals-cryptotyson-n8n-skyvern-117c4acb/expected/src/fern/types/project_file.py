

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .file_encoding import FileEncoding


class ProjectFile(UniversalBaseModel):
    """
    Model representing a file in a project.
    """

    path: str = pydantic.Field()
    """
    File path relative to project root
    """

    content: str = pydantic.Field()
    """
    Base64 encoded file content
    """

    encoding: typing.Optional[FileEncoding] = pydantic.Field(default=None)
    """
    Content encoding
    """

    mime_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    MIME type (auto-detected if not provided)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
