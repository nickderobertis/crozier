

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .label_user import LabelUser


class CoOwner(UniversalBaseModel):
    alias: typing.Optional[LabelUser] = pydantic.Field(default=None)
    """
    The Alias of the co-owner.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    Can be: ACCEPTED, REJECTED, PENDING or REVOKED
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
