

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SpellCheckResponseTokensItem(UniversalBaseModel):
    offset: typing.Optional[int] = pydantic.Field(default=None)
    """
    The zero-based offset from the beginning of the text query string to the word that is misspelled
    """

    suggestion: typing.Optional[str] = pydantic.Field(default=None)
    """
    A word that corrects the spelling error
    """

    token: typing.Optional[str] = pydantic.Field(default=None)
    """
    The misspelled word
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
