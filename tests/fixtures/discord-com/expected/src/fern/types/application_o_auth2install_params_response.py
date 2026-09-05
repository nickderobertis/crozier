

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .application_o_auth2install_params_response_scopes_item import ApplicationOAuth2InstallParamsResponseScopesItem


class ApplicationOAuth2InstallParamsResponse(UniversalBaseModel):
    scopes: typing.List[ApplicationOAuth2InstallParamsResponseScopesItem]
    permissions: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
