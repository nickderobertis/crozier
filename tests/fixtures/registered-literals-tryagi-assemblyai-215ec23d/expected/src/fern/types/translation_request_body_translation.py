

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TranslationRequestBodyTranslation(UniversalBaseModel):
    target_languages: typing.List[str] = pydantic.Field()
    """
    List of target language codes (e.g., `["es", "de"]`). See [Translation](https://www.assemblyai.com/docs/speech-understanding/translation) for supported languages.
    """

    formal: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Use formal language style. See [Translation](https://www.assemblyai.com/docs/speech-understanding/translation) for more details.
    """

    match_original_utterance: typing.Optional[bool] = pydantic.Field(default=None)
    """
    When enabled with Speaker Labels, returns translated text in the utterances array. Each utterance will include a `translated_texts` key containing translations for each target language.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
