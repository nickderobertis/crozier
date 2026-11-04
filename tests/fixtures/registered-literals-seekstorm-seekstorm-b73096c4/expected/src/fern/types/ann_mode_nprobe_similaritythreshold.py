

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AnnModeNprobeSimilaritythreshold(UniversalBaseModel):
    """
    Search only in the clusters with the highest similarity scores to the query vector, but only if their similarity scores are above the specified threshold, and up to the number of clusters specified by the n-probe parameter.
    For dot product similarity, the similarity threshold should be between 0.0 and 1.0, where higher values indicate higher similarity (identical=1.0).
    For Euclidean distance similarity, the similarity threshold should be between 0.0 and infinity, where lower values indicate higher similarity (identical=0.0).
    """

    nprobe_similaritythreshold: typing_extensions.Annotated[
        typing.List[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="NprobeSimilaritythreshold"),
        pydantic.Field(
            alias="NprobeSimilaritythreshold",
            description="Search only in the clusters with the highest similarity scores to the query vector, but only if their similarity scores are above the specified threshold, and up to the number of clusters specified by the n-probe parameter.\nFor dot product similarity, the similarity threshold should be between 0.0 and 1.0, where higher values indicate higher similarity (identical=1.0).\nFor Euclidean distance similarity, the similarity threshold should be between 0.0 and infinity, where lower values indicate higher similarity (identical=0.0).",
        ),
    ]
    """
    Search only in the clusters with the highest similarity scores to the query vector, but only if their similarity scores are above the specified threshold, and up to the number of clusters specified by the n-probe parameter.
    For dot product similarity, the similarity threshold should be between 0.0 and 1.0, where higher values indicate higher similarity (identical=1.0).
    For Euclidean distance similarity, the similarity threshold should be between 0.0 and infinity, where lower values indicate higher similarity (identical=0.0).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
