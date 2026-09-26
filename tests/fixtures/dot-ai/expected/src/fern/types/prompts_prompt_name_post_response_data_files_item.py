

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PromptsPromptNamePostResponseDataFilesItem(UniversalBaseModel):
    path: str = pydantic.Field()
    """
    Relative path within skill folder
    """

    content: str = pydantic.Field()
    """
    Base64-encoded file content
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
