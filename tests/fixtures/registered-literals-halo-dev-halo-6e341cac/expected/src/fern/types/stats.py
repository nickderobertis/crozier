

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Stats(UniversalBaseModel):
    """
    Aggregated visit, upvote, and comment counters for a content resource.
    """

    approved_comment: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="approvedComment"),
        pydantic.Field(alias="approvedComment", description="Total approved comment count."),
    ] = None
    """
    Total approved comment count.
    """

    total_comment: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="totalComment"),
        pydantic.Field(
            alias="totalComment", description="Total comment count, including comments that may not be approved."
        ),
    ] = None
    """
    Total comment count, including comments that may not be approved.
    """

    upvote: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total upvote count.
    """

    visit: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total visit count.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
