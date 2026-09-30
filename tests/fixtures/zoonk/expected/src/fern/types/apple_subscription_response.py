

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .me_response import MeResponse


class AppleSubscriptionResponse(UniversalBaseModel):
    current_account: typing_extensions.Annotated[
        MeResponse, FieldMetadata(alias="currentAccount"), pydantic.Field(alias="currentAccount")
    ]
    is_active: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="isActive"),
        pydantic.Field(
            alias="isActive", description="Whether the reconciled App Store subscription currently grants access"
        ),
    ]
    """
    Whether the reconciled App Store subscription currently grants access
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
