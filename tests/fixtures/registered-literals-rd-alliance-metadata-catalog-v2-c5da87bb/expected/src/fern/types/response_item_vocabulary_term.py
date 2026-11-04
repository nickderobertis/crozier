

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .response import Response
from .vocabulary_term_old import VocabularyTermOld


class ResponseItemVocabularyTerm(Response):
    data: typing.Optional[VocabularyTermOld] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
