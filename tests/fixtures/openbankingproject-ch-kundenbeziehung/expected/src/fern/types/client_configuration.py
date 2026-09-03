

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .client_configuration_status import ClientConfigurationStatus


class ClientConfiguration(UniversalBaseModel):
    client_id: str
    client_secret_expires_at: typing.Optional[int] = None
    client_id_issued_at: typing.Optional[int] = None
    client_name: typing.Optional[str] = None
    client_uri: typing.Optional[str] = None
    redirect_uris: typing.Optional[typing.List[str]] = None
    grant_types: typing.Optional[typing.List[str]] = None
    response_types: typing.Optional[typing.List[str]] = None
    scope: typing.Optional[str] = None
    industry_type: typing.Optional[str] = None
    status: typing.Optional[ClientConfigurationStatus] = None
    fapi_compliance_level: typing.Optional[str] = None
    created_at: typing.Optional[dt.datetime] = None
    updated_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
