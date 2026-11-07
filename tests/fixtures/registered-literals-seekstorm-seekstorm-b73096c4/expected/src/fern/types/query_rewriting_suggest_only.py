

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .query_rewriting_suggest_only_suggest_only import QueryRewritingSuggestOnlySuggestOnly


class QueryRewritingSuggestOnly(UniversalBaseModel):
    """
    Search disabled, returns no query results, only returns suggestions for corrected or completed query.
    """

    suggest_only: typing_extensions.Annotated[
        QueryRewritingSuggestOnlySuggestOnly,
        FieldMetadata(alias="SuggestOnly"),
        pydantic.Field(
            alias="SuggestOnly",
            description="Search disabled, returns no query results, only returns suggestions for corrected or completed query.",
        ),
    ]
    """
    Search disabled, returns no query results, only returns suggestions for corrected or completed query.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
