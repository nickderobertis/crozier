

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .display_entry import DisplayEntry
from .elastic_search_relation_entry import ElasticSearchRelationEntry


class RelationsEntry(UniversalBaseModel):
    display: typing.Optional[DisplayEntry] = None
    selectable: typing.Optional[bool] = None
    termcode: typing.Optional[str] = None
    terminology: typing.Optional[str] = None
    parents: typing.Optional[typing.List[ElasticSearchRelationEntry]] = None
    children: typing.Optional[typing.List[ElasticSearchRelationEntry]] = None
    related_terms: typing_extensions.Annotated[
        typing.Optional[typing.List[ElasticSearchRelationEntry]],
        FieldMetadata(alias="relatedTerms"),
        pydantic.Field(alias="relatedTerms"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
