

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_oauth_details_v2response_errors_item_error_code import PostOauthDetailsV2ResponseErrorsItemErrorCode


class PostOauthDetailsV2ResponseErrorsItem(UniversalBaseModel):
    error_code: typing_extensions.Annotated[
        typing.Optional[PostOauthDetailsV2ResponseErrorsItemErrorCode],
        FieldMetadata(alias="errorCode"),
        pydantic.Field(alias="errorCode"),
    ] = None
    error_message: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="errorMessage"), pydantic.Field(alias="errorMessage")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
