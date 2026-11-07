

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .mscid import Mscid
from .uri import Uri
from .vocabulary_term_applies_item import VocabularyTermAppliesItem


class VocabularyTerm(UniversalBaseModel):
    mscid: typing.Optional[Mscid] = None
    uri: typing.Optional[Uri] = None
    label: str = pydantic.Field()
    """
    Human-readable descriptor for this term.
    """

    applies: typing.Optional[typing.List[VocabularyTermAppliesItem]] = pydantic.Field(default=None)
    """
    Entities for which this term may be used.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
