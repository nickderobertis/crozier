

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Submission(UniversalBaseModel):
    language: str = pydantic.Field()
    """
    The language of the solution attempt, as an identifier supported by Piston
    """

    code: str = pydantic.Field()
    """
    The code to test, which is assumed to be in the language specified
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
