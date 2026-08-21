

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .proxy_error_error_type import ProxyErrorErrorType


class ProxyErrorError(UniversalBaseModel):
    type: ProxyErrorErrorType
    code: str
    message: str
    request_id: typing_extensions.Annotated[str, FieldMetadata(alias="requestId"), pydantic.Field(alias="requestId")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
