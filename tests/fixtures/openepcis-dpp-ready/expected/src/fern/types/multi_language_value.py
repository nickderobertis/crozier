

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MultiLanguageValue(UniversalBaseModel):
    """
    A language-tagged value (EN 18223 clause 4.1.2.8).
    """

    value: str
    language: str = pydantic.Field()
    """
    ISO 639 language code, optionally with ISO 3166-1 region.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
