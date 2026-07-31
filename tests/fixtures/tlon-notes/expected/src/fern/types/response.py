

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .request_id import RequestId
from .response_body import ResponseBody


class Response(UniversalBaseModel):
    request_id: typing_extensions.Annotated[
        RequestId, FieldMetadata(alias="requestId"), pydantic.Field(alias="requestId")
    ]
    body: ResponseBody

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
