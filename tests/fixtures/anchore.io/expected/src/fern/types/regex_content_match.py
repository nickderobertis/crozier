

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RegexContentMatch(UniversalBaseModel):
    """
    Match of a named regex on a file
    """

    lines: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    A list of line numbers in the file that matched the regex
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name associated with the regular expression
    """

    regex: typing.Optional[str] = pydantic.Field(default=None)
    """
    The regular expression used for the match
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
