

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .user_account_preview_rejection_get import UserAccountPreviewRejectionGet


class EnvelopeUserAccountPreviewRejectionGet(UniversalBaseModel):
    data: typing.Optional[UserAccountPreviewRejectionGet] = None
    error: typing.Optional[typing.Any] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
