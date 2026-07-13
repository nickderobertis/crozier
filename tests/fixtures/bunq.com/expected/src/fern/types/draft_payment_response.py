

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .label_user import LabelUser


class DraftPaymentResponse(UniversalBaseModel):
    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status with which was responded.
    """

    user_alias_created: typing.Optional[LabelUser] = pydantic.Field(default=None)
    """
    The user that responded to the DraftPayment.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
