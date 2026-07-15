

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .api_reference import ApiReference
from .language_type import LanguageType


class Language(ApiReference):
    """
    `Language`
    """

    desc: typing.Optional[str] = pydantic.Field(default=None)
    """
    Brief description of the language.
    """

    script: typing.Optional[str] = pydantic.Field(default=None)
    """
    Script used for writing in the language.
    """

    type: typing.Optional[LanguageType] = None
    typical_speakers: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of races that tend to speak the language.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
