

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FileStatistics(UniversalBaseModel):
    """
    A file is a document usable for training and validation. It can also be a service generated document with result details.
    """

    tokens: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of tokens used in prompts and completions for files of kind "fine-tune" once validation of file content is complete.
    """

    examples: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of contained training examples in files of kind "fine-tune" once validation of file content is complete.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
