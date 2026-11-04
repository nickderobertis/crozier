

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .vocabulary_term import VocabularyTerm


class VocabularyTermOld(VocabularyTerm):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    String used to identify this term in records.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
