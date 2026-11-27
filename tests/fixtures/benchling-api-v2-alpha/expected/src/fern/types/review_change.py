

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .review_change_action import ReviewChangeAction
from .review_snapshot import ReviewSnapshot


class ReviewChange(UniversalBaseModel):
    action: typing.Optional[ReviewChangeAction] = pydantic.Field(default=None)
    """
    The action which was performed with this change
    """

    comment: typing.Optional[str] = pydantic.Field(default=None)
    """
    The comment which was left when the Review Change was submitted
    """

    created_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="DateTime the Review Change was created at"),
    ] = None
    """
    DateTime the Review Change was created at
    """

    esigned: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Was the action verified through an e-signature compliant step
    """

    id: typing.Optional[str] = None
    review_snapshot: typing_extensions.Annotated[
        typing.Optional[ReviewSnapshot],
        FieldMetadata(alias="reviewSnapshot"),
        pydantic.Field(alias="reviewSnapshot", description="Review Snapshot generated from this Review Change"),
    ] = None
    """
    Review Snapshot generated from this Review Change
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
