

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .thesaurus_base_context import ThesaurusBaseContext
from .thesaurus_base_skos_pref_label_item import ThesaurusBaseSkosPrefLabelItem


class ThesaurusBase(UniversalBaseModel):
    context: typing_extensions.Annotated[
        typing.Optional[ThesaurusBaseContext], FieldMetadata(alias="@context"), pydantic.Field(alias="@context")
    ] = None
    id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="@id"), pydantic.Field(alias="@id")] = (
        None
    )
    type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="@type"), pydantic.Field(alias="@type")
    ] = None
    skos_pref_label: typing_extensions.Annotated[
        typing.Optional[typing.List[ThesaurusBaseSkosPrefLabelItem]],
        FieldMetadata(alias="skos:prefLabel"),
        pydantic.Field(alias="skos:prefLabel"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
