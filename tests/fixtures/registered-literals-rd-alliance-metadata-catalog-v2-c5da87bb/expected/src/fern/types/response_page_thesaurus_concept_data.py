

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, update_forward_refs
from .page import Page
from .thesaurus_concept import ThesaurusConcept


class ResponsePageThesaurusConceptData(Page):
    items: typing.Optional[typing.List[ThesaurusConcept]] = pydantic.Field(default=None)
    """
    Items in the current page of results.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(ResponsePageThesaurusConceptData)
