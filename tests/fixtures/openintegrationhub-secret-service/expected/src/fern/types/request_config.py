

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .request_config_auth_type import RequestConfigAuthType
from .request_field import RequestField


class RequestConfig(UniversalBaseModel):
    request_fields: typing_extensions.Annotated[
        typing.List[RequestField], FieldMetadata(alias="requestFields"), pydantic.Field(alias="requestFields")
    ]
    label: typing.Optional[str] = None
    auth_type: typing_extensions.Annotated[
        RequestConfigAuthType, FieldMetadata(alias="authType"), pydantic.Field(alias="authType")
    ]
    url: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
