

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_mockserver_proxy_configuration_response_environment_variables import (
    GetMockserverProxyConfigurationResponseEnvironmentVariables,
)


class GetMockserverProxyConfigurationResponse(UniversalBaseModel):
    ca_certificate_path: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="caCertificatePath"), pydantic.Field(alias="caCertificatePath")
    ] = None
    ca_certificate_pem: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="caCertificatePem"), pydantic.Field(alias="caCertificatePem")
    ] = None
    https_proxy: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="httpsProxy"), pydantic.Field(alias="httpsProxy")
    ] = None
    environment_variables: typing_extensions.Annotated[
        typing.Optional[GetMockserverProxyConfigurationResponseEnvironmentVariables],
        FieldMetadata(alias="environmentVariables"),
        pydantic.Field(alias="environmentVariables"),
    ] = None
    using_default_ca: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="usingDefaultCa"), pydantic.Field(alias="usingDefaultCa")
    ] = None
    warning: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
