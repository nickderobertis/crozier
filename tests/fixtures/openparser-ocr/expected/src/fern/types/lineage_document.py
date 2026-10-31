

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .lineage_activity import LineageActivity
from .lineage_agent import LineageAgent
from .lineage_derivation import LineageDerivation
from .lineage_document_format import LineageDocumentFormat
from .lineage_entity import LineageEntity
from .lineage_relation import LineageRelation


class LineageDocument(UniversalBaseModel):
    """
    A complete, acyclic `lineage@1` data-derivation graph grounded in W3C PROV semantics. Downstream systems can append entities, activities, agents, and derivations.
    """

    format: LineageDocumentFormat
    id: typing.Optional[str] = None
    profiles: typing.Optional[typing.List[str]] = None
    entities: typing.Dict[str, LineageEntity]
    activities: typing.Dict[str, LineageActivity]
    agents: typing.Dict[str, LineageAgent]
    derivations: typing.List[LineageDerivation]
    relations: typing.List[LineageRelation]
    outputs: typing.List[str]
    attributes: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
