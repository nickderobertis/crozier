

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .response import Response
from .response_page_vocabulary_term_data import ResponsePageVocabularyTermData


class ResponsePageVocabularyTerm(Response):
    data: typing.Optional[ResponsePageVocabularyTermData] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
