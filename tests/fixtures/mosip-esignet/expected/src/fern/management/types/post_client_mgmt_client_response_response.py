

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_client_mgmt_client_response_response_status import PostClientMgmtClientResponseResponseStatus


class PostClientMgmtClientResponseResponse(UniversalBaseModel):
    client_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="clientId"),
        pydantic.Field(alias="clientId", description="Client id as provided in the request."),
    ] = None
    """
    Client id as provided in the request.
    """

    status: typing.Optional[PostClientMgmtClientResponseResponseStatus] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
