

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .spell_check_response_tokens_item import SpellCheckResponseTokensItem


class SpellCheckResponse(UniversalBaseModel):
    corrected_text_html: str = pydantic.Field()
    """
    The corrected text for the entire search term (multiple words/tokens), where misspelled tokens are replaced with the correct texts and html tags <b><i>
    """

    tokens: typing.List[SpellCheckResponseTokensItem] = pydantic.Field()
    """
    The word in the text query string that is not spelled correctly
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
