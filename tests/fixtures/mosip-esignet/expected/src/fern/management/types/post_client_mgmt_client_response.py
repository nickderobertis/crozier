

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_client_mgmt_client_response_errors_item import PostClientMgmtClientResponseErrorsItem
from .post_client_mgmt_client_response_response import PostClientMgmtClientResponseResponse


class PostClientMgmtClientResponse(UniversalBaseModel):
    response_time: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="responseTime"),
        pydantic.Field(alias="responseTime", description="Date and time when the response is generated"),
    ] = None
    """
    Date and time when the response is generated
    """

    response: typing.Optional[PostClientMgmtClientResponseResponse] = None
    errors: typing.Optional[typing.List[PostClientMgmtClientResponseErrorsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
