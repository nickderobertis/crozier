

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .otoroshi_auth_oauth1module_config_type import OtoroshiAuthOauth1ModuleConfigType
from .otoroshi_models_user_rights import OtoroshiModelsUserRights
from .otoroshi_utils_json_path_validator import OtoroshiUtilsJsonPathValidator


class OtoroshiAuthOauth1ModuleConfig(UniversalBaseModel):
    """
    ???
    """

    type: typing.Optional[OtoroshiAuthOauth1ModuleConfigType] = pydantic.Field(default=None)
    """
    the type of the module
    """

    access_token_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="accessTokenURL"),
        pydantic.Field(alias="accessTokenURL", description="???"),
    ] = None
    """
    ???
    """

    desc: typing.Optional[str] = pydantic.Field(default=None)
    """
    ???
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    ???
    """

    authorize_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="authorizeURL"),
        pydantic.Field(alias="authorizeURL", description="???"),
    ] = None
    """
    ???
    """

    rights_override: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, OtoroshiModelsUserRights]],
        FieldMetadata(alias="rightsOverride"),
        pydantic.Field(alias="rightsOverride", description="???"),
    ] = None
    """
    ???
    """

    consumer_key: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="consumerKey"), pydantic.Field(alias="consumerKey", description="???")
    ] = None
    """
    ???
    """

    callback_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="callbackURL"), pydantic.Field(alias="callbackURL", description="???")
    ] = None
    """
    ???
    """

    profile_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="profileURL"), pydantic.Field(alias="profileURL", description="???")
    ] = None
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

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
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

    http_method: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="httpMethod"), pydantic.Field(alias="httpMethod")
    ] = None
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

    request_token_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="requestTokenURL"),
        pydantic.Field(alias="requestTokenURL", description="???"),
    ] = None
    """
    ???
    """

    loc: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="_loc"), pydantic.Field(alias="_loc")
    ] = None
    consumer_secret: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="consumerSecret"),
        pydantic.Field(alias="consumerSecret", description="???"),
    ] = None
    """
    ???
    """

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
