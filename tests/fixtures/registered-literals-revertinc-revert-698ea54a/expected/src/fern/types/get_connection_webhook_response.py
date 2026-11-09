

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .common_response_status import CommonResponseStatus


class GetConnectionWebhookResponse(UniversalBaseModel):
    status: CommonResponseStatus
    webhook: typing.Any
    error: typing.Optional[str] = None
    error_message: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="errorMessage"), pydantic.Field(alias="errorMessage")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
