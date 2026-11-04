

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .thesaurus_concept_broader_skos_top_concept_of_item import ThesaurusConceptBroaderSkosTopConceptOfItem


class ThesaurusConceptBroader(UniversalBaseModel):
    skos_broader: typing_extensions.Annotated[
        typing.Optional[typing.List["ThesaurusConceptBroaderSkosBroaderItem"]],
        FieldMetadata(alias="skos:broader"),
        pydantic.Field(alias="skos:broader"),
    ] = None
    skos_top_concept_of: typing_extensions.Annotated[
        typing.Optional[typing.List[ThesaurusConceptBroaderSkosTopConceptOfItem]],
        FieldMetadata(alias="skos:topConceptOf"),
        pydantic.Field(alias="skos:topConceptOf"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .thesaurus_concept_broader_skos_broader_item import ThesaurusConceptBroaderSkosBroaderItem

update_forward_refs(
    ThesaurusConceptBroader, ThesaurusConceptBroaderSkosBroaderItem=ThesaurusConceptBroaderSkosBroaderItem
)
