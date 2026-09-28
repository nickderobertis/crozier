

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PromptsSourcesPostRequestFilesItem(UniversalBaseModel):
    path: str = pydantic.Field()
    """
    Relative path within the uploaded skill source
    """

    content: str = pydantic.Field()
    """
    Base64-encoded file content
    """

    mode: typing.Optional[str] = pydantic.Field(default=None)
    """
    POSIX file mode (e.g., "0644")
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
