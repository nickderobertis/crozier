

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_wallet_binding_response_errors_item import PostWalletBindingResponseErrorsItem
from .post_wallet_binding_response_response import PostWalletBindingResponseResponse


class PostWalletBindingResponse(UniversalBaseModel):
    response_time: typing_extensions.Annotated[
        str, FieldMetadata(alias="responseTime"), pydantic.Field(alias="responseTime")
    ]
    response: typing.Optional[PostWalletBindingResponseResponse] = None
    errors: typing.Optional[typing.List[PostWalletBindingResponseErrorsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
