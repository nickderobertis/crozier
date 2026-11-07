

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TranscriptTranslatedTexts(UniversalBaseModel):
    """
    Translated text keyed by language code. See [Translation](https://www.assemblyai.com/docs/speech-understanding/translation) for more details.
    """

    language_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    Translated text for this language code
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
