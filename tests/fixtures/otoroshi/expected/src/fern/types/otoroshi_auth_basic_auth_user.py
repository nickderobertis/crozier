

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .otoroshi_auth_basic_auth_user_webauthn import OtoroshiAuthBasicAuthUserWebauthn
from .otoroshi_models_user_rights import OtoroshiModelsUserRights


class OtoroshiAuthBasicAuthUser(UniversalBaseModel):
    """
    ???
    """

    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    ???
    """

    password: typing.Optional[str] = pydantic.Field(default=None)
    """
    ???
    """

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    ???
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    ???
    """

    webauthn: typing.Optional[OtoroshiAuthBasicAuthUserWebauthn] = pydantic.Field(default=None)
    """
    ???
    """

    rights: typing.Optional[OtoroshiModelsUserRights] = pydantic.Field(default=None)
    """
    ???
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    ???
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
