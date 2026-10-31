

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .lineage_attribution import LineageAttribution
from .lineage_confidence_assertion import LineageConfidenceAssertion
from .lineage_digest import LineageDigest
from .lineage_entity_approvals_item import LineageEntityApprovalsItem
from .lineage_entity_kind import LineageEntityKind
from .lineage_locator import LineageLocator
from .lineage_selector import LineageSelector


class LineageEntity(UniversalBaseModel):
    """
    An immutable value, artifact, evidence item, decision, or collection in a `lineage@1` derivation DAG. `path` is an RFC 6901 JSON Pointer.
    """

    kind: LineageEntityKind
    name: typing.Optional[str] = None
    value: typing.Optional[typing.Any] = None
    path: typing.Optional[str] = None
    schema_: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]], FieldMetadata(alias="schema"), pydantic.Field(alias="schema")
    ] = None
    locator: typing.Optional[LineageLocator] = None
    selector: typing.Optional[LineageSelector] = None
    digest: typing.Optional[LineageDigest] = None
    confidence: typing.Optional[typing.List[LineageConfidenceAssertion]] = None
    approvals: typing.Optional[typing.List[LineageEntityApprovalsItem]] = None
    attributions: typing.Optional[typing.List[LineageAttribution]] = None
    attributes: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
