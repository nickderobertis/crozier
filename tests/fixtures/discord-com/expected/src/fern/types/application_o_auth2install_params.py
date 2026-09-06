

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .application_o_auth2install_params_scopes_item import ApplicationOAuth2InstallParamsScopesItem


class ApplicationOAuth2InstallParams(UniversalBaseModel):
    scopes: typing.Optional[typing.List[ApplicationOAuth2InstallParamsScopesItem]] = None
    permissions: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
