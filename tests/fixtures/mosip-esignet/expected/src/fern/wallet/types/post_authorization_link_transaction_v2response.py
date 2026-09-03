

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_authorization_link_transaction_v2response_errors_item import (
    PostAuthorizationLinkTransactionV2ResponseErrorsItem,
)
from .post_authorization_link_transaction_v2response_response import PostAuthorizationLinkTransactionV2ResponseResponse


class PostAuthorizationLinkTransactionV2Response(UniversalBaseModel):
    response_time: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="responseTime"), pydantic.Field(alias="responseTime")
    ] = None
    response: typing.Optional[PostAuthorizationLinkTransactionV2ResponseResponse] = None
    errors: typing.Optional[typing.List[PostAuthorizationLinkTransactionV2ResponseErrorsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
