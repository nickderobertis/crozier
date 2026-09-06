

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .application_o_auth2install_params_response import ApplicationOAuth2InstallParamsResponse


class ApplicationIntegrationTypeConfigurationResponse(UniversalBaseModel):
    oauth2install_params: typing_extensions.Annotated[
        typing.Optional[ApplicationOAuth2InstallParamsResponse],
        FieldMetadata(alias="oauth2_install_params"),
        pydantic.Field(alias="oauth2_install_params"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
