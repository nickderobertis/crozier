

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .otoroshi_models_simple_otoroshi_admin_type import OtoroshiModelsSimpleOtoroshiAdminType
from .otoroshi_models_user_rights import OtoroshiModelsUserRights


class OtoroshiModelsSimpleOtoroshiAdmin(UniversalBaseModel):
    """
    An otoroshi admin user
    """

    type: typing.Optional[OtoroshiModelsSimpleOtoroshiAdminType] = pydantic.Field(default=None)
    """
    the kind of admin
    """

    username: typing.Optional[str] = pydantic.Field(default=None)
    """
    User username
    """

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Entity tags
    """

    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    User label
    """

    loc: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="_loc"), pydantic.Field(alias="_loc")
    ] = None
    typ: typing.Optional[typing.Any] = None
    created_at: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="User creation date"),
    ] = None
    """
    User creation date
    """

    metadata: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Entity metadata
    """

    rights: typing.Optional[OtoroshiModelsUserRights] = pydantic.Field(default=None)
    """
    User rights
    """

    password: typing.Optional[str] = pydantic.Field(default=None)
    """
    User password (bcrypt hashed)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
