

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .put_client_client_id_response_errors_item import PutClientClientIdResponseErrorsItem
from .put_client_client_id_response_response import PutClientClientIdResponseResponse


class PutClientClientIdResponse(UniversalBaseModel):
    response_time: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="responseTime"),
        pydantic.Field(alias="responseTime", description="Date and time when the response is generated"),
    ] = None
    """
    Date and time when the response is generated
    """

    response: typing.Optional[PutClientClientIdResponseResponse] = None
    errors: typing.Optional[typing.List[PutClientClientIdResponseErrorsItem]] = pydantic.Field(default=None)
    """
    List of Errors in case of request validation / processing failure in Idp server. When request processing is fully successful, this array will be empty.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
