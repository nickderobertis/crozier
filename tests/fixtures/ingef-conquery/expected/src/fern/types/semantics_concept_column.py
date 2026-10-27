

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .concept_id import ConceptId
from .semantics_base import SemanticsBase


class SemanticsConceptColumn(SemanticsBase):
    """
    Values contain the ids of the concept-element resolved to the event.
    """

    concept: typing.Optional[ConceptId] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
