

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .type_summary import TypeSummary


class ListTypesOutput(UniversalBaseModel):
    type_summaries: typing_extensions.Annotated[
        typing.Optional[typing.List[TypeSummary]],
        FieldMetadata(alias="TypeSummaries"),
        pydantic.Field(
            alias="TypeSummaries",
            description="A list of <code>TypeSummary</code> structures that contain information about the specified extensions.",
        ),
    ] = None
    """
    A list of <code>TypeSummary</code> structures that contain information about the specified extensions.
    """

    next_token: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="NextToken"),
        pydantic.Field(
            alias="NextToken",
            description="If the request doesn't return all the remaining results, <code>NextToken</code> is set to a token. To retrieve the next set of results, call this action again and assign that token to the request object's <code>NextToken</code> parameter. If the request returns all results, <code>NextToken</code> is set to <code>null</code>.",
        ),
    ] = None
    """
    If the request doesn't return all the remaining results, <code>NextToken</code> is set to a token. To retrieve the next set of results, call this action again and assign that token to the request object's <code>NextToken</code> parameter. If the request returns all results, <code>NextToken</code> is set to <code>null</code>.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
