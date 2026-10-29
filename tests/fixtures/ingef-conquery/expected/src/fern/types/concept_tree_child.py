

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, update_forward_refs
from ..core.serialization import FieldMetadata
from .concept_tree_child_additional_infos_item import ConceptTreeChildAdditionalInfosItem
from .labeled import Labeled


class ConceptTreeChild(Labeled):
    """
    See documentation for Concept.
    """

    children: typing.Optional[typing.List["ConceptTreeChild"]] = None
    condition: typing.Optional["ConceptCondition"] = None
    description: typing.Optional[str] = None
    additional_infos: typing_extensions.Annotated[
        typing.Optional[typing.List[ConceptTreeChildAdditionalInfosItem]],
        FieldMetadata(alias="additionalInfos"),
        pydantic.Field(alias="additionalInfos"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .and_condition import AndCondition
from .not_condition import NotCondition
from .or_condition import OrCondition
from .concept_condition import ConceptCondition

update_forward_refs(
    ConceptTreeChild,
    AndCondition=AndCondition,
    ConceptCondition=ConceptCondition,
    NotCondition=NotCondition,
    OrCondition=OrCondition,
)
