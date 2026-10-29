

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .output_description_base import OutputDescriptionBase


class LineOutput(OutputDescriptionBase):
    """
    Emits the line number. The line-number is not guaranteed to be in file order, just an incrementing unique number: If multiple files are preprocessed, the line-number will not reset to zero.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
