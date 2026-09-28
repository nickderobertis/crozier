

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .otoroshi_auth_basic_auth_module_config_type import OtoroshiAuthBasicAuthModuleConfigType
from .otoroshi_auth_basic_auth_user import OtoroshiAuthBasicAuthUser
from .otoroshi_utils_json_path_validator import OtoroshiUtilsJsonPathValidator


class OtoroshiAuthBasicAuthModuleConfig(UniversalBaseModel):
    """
    ???
    """

    type: typing.Optional[OtoroshiAuthBasicAuthModuleConfigType] = pydantic.Field(default=None)
    """
    the type of the module
    """

    desc: typing.Optional[str] = pydantic.Field(default=None)
    """
    ???
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    ???
    """

    client_side_session_enabled: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="clientSideSessionEnabled"),
        pydantic.Field(alias="clientSideSessionEnabled", description="???"),
    ] = None
    """
    ???
    """

    basic_auth: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="basicAuth"), pydantic.Field(alias="basicAuth", description="???")
    ] = None
    """
    ???
    """

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    ???
    """

    users: typing.Optional[typing.List[OtoroshiAuthBasicAuthUser]] = pydantic.Field(default=None)
    """
    ???
    """

    session_max_age: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="sessionMaxAge"),
        pydantic.Field(alias="sessionMaxAge", description="???"),
    ] = None
    """
    ???
    """

    webauthn: typing.Optional[bool] = pydantic.Field(default=None)
    """
    ???
    """

    user_validators: typing_extensions.Annotated[
        typing.Optional[typing.List[OtoroshiUtilsJsonPathValidator]],
        FieldMetadata(alias="userValidators"),
        pydantic.Field(alias="userValidators", description="???"),
    ] = None
    """
    ???
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ???
    """

    loc: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="_loc"), pydantic.Field(alias="_loc")
    ] = None
    metadata: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    ???
    """

    session_cookie_values: typing_extensions.Annotated[
        typing.Optional[typing.Any],
        FieldMetadata(alias="sessionCookieValues"),
        pydantic.Field(alias="sessionCookieValues"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
