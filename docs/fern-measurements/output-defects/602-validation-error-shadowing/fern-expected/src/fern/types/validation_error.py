

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ValidationError(UniversalBaseModel):
    """
    One style rule a manuscript line breaks.
    """

    line: int = pydantic.Field()
    """
    The one-based line the problem is on.
    """

    rule: str = pydantic.Field()
    """
    The style rule broken.
    """

    hint: typing.Optional[str] = pydantic.Field(default=None)
    """
    How to fix it.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
