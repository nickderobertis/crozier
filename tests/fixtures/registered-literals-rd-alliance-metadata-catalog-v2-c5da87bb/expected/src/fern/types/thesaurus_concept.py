

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .thesaurus_base import ThesaurusBase
from .thesaurus_concept_broader import ThesaurusConceptBroader
from .thesaurus_concept_narrower import ThesaurusConceptNarrower


class ThesaurusConcept(ThesaurusBase, ThesaurusConceptBroader, ThesaurusConceptNarrower):
    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
