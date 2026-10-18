

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .api_key_response_output_type import ApiKeyResponseOutputType


class ApiKeyResponseOutput(UniversalBaseModel):
    api_key: typing.Optional[str] = None
    id: typing.Optional[str] = None
    type: typing.Optional[ApiKeyResponseOutputType] = None
    prefix: typing.Optional[str] = None
    name: str
    description: typing.Optional[str] = None
    hash: typing.Optional[str] = None
    secret_jwt_template: typing.Optional[typing.Dict[str, typing.Any]] = None
    inserted_at: typing.Optional[dt.datetime] = None
    updated_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
