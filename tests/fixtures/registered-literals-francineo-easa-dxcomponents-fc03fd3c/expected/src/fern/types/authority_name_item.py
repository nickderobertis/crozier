

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AuthorityNameItem(UniversalBaseModel):
    """
    A free text with a maximum length of 200 characters, optionally accompanied
    by an indication of the language in which the text is written.
    """

    text: typing.Optional[str] = None
    lang: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
