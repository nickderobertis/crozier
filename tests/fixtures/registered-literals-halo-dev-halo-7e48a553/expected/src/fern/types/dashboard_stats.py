

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DashboardStats(UniversalBaseModel):
    """
    Dashboard statistics for the console overview.
    """

    approved_comments: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="approvedComments"),
        pydantic.Field(alias="approvedComments", description="Approved comment count."),
    ]
    """
    Approved comment count.
    """

    comments: int = pydantic.Field()
    """
    Total comment count.
    """

    posts: int = pydantic.Field()
    """
    Total non-deleted post count.
    """

    upvotes: int = pydantic.Field()
    """
    Total upvote count.
    """

    users: int = pydantic.Field()
    """
    Total user count.
    """

    visits: int = pydantic.Field()
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
