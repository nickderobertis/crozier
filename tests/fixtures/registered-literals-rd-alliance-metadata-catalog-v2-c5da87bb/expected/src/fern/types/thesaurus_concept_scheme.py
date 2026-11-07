

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .thesaurus_base import ThesaurusBase
from .thesaurus_concept_scheme_skos_has_top_concept_item import ThesaurusConceptSchemeSkosHasTopConceptItem


class ThesaurusConceptScheme(ThesaurusBase):
    skos_has_top_concept: typing_extensions.Annotated[
        typing.Optional[typing.List[ThesaurusConceptSchemeSkosHasTopConceptItem]],
        FieldMetadata(alias="skos:hasTopConcept"),
        pydantic.Field(alias="skos:hasTopConcept"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
