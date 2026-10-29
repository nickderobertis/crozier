

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .concept_id import ConceptId
from .resolved_concepts_result_resolved_filter import ResolvedConceptsResultResolvedFilter


class ResolvedConceptsResult(UniversalBaseModel):
    """
    Response object for resolve endpoint.
    """

    resolved_concepts: typing_extensions.Annotated[
        typing.Optional[typing.List[ConceptId]],
        FieldMetadata(alias="resolvedConcepts"),
        pydantic.Field(alias="resolvedConcepts", description="Ids of resolved concept elements."),
    ] = None
    """
    Ids of resolved concept elements.
    """

    unknown_codes: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="unknownCodes"),
        pydantic.Field(alias="unknownCodes", description="Values that could not be resolved."),
    ] = None
    """
    Values that could not be resolved.
    """

    resolved_filter: typing_extensions.Annotated[
        typing.Optional[ResolvedConceptsResultResolvedFilter],
        FieldMetadata(alias="resolvedFilter"),
        pydantic.Field(alias="resolvedFilter"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
