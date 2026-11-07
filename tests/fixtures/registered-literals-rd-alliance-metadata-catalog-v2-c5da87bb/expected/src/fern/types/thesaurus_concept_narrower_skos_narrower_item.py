

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata


class ThesaurusConceptNarrowerSkosNarrowerItem(UniversalBaseModel):
    id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="@id"), pydantic.Field(alias="@id")] = (
        None
    )
    type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="@type"), pydantic.Field(alias="@type")
    ] = None
    skos_narrower: typing_extensions.Annotated[
        typing.Optional[typing.List["ThesaurusConceptNarrowerSkosNarrowerItem"]],
        FieldMetadata(alias="skos:narrower"),
        pydantic.Field(alias="skos:narrower"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .thesaurus_concept_narrower import ThesaurusConceptNarrower

update_forward_refs(ThesaurusConceptNarrowerSkosNarrowerItem, ThesaurusConceptNarrower=ThesaurusConceptNarrower)
