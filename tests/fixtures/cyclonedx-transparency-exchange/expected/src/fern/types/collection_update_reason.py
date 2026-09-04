

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .collection_update_reason_type import CollectionUpdateReasonType


class CollectionUpdateReason(UniversalBaseModel):
    """
    Reason for the update to the TEA collection
    """

    type: typing.Optional[CollectionUpdateReasonType] = pydantic.Field(default=None)
    """
    Type of update reason.
    """

    comment: typing.Optional[str] = pydantic.Field(default=None)
    """
    Free text description
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
