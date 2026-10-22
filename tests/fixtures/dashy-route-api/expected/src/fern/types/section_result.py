

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .section import Section
from .write_result import WriteResult


class SectionResult(WriteResult):
    index: typing.Optional[int] = pydantic.Field(default=None)
    """
    Array index of the section
    """

    section: typing.Optional[Section] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
