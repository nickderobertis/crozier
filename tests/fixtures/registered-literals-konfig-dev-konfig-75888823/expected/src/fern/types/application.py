

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .app_id import AppId
from .app_name import AppName
from .auth_configuration import AuthConfiguration
from .org_id import OrgId


class Application(UniversalBaseModel):
    """
    An application object is the top level namespace for the game server.
    """

    deleted_by: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="deletedBy"),
        pydantic.Field(
            alias="deletedBy", description="UserId or email address for the user that deleted the application."
        ),
    ] = None
    """
    UserId or email address for the user that deleted the application.
    """

    deleted_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="deletedAt"),
        pydantic.Field(alias="deletedAt", description="When the application was deleted."),
    ] = None
    """
    When the application was deleted.
    """

    created_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="When the application was created."),
    ]
    """
    When the application was created.
    """

    created_by: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="createdBy"),
        pydantic.Field(
            alias="createdBy", description="UserId or email address for the user that created the application."
        ),
    ]
    """
    UserId or email address for the user that created the application.
    """

    org_id: typing_extensions.Annotated[OrgId, FieldMetadata(alias="orgId"), pydantic.Field(alias="orgId")]
    auth_configuration: typing_extensions.Annotated[
        AuthConfiguration,
        FieldMetadata(alias="authConfiguration"),
        pydantic.Field(
            alias="authConfiguration",
            description="Used to authenticate player requests. Use your own authentication or Hathora's Auth Client.",
        ),
    ]
    """
    Used to authenticate player requests. Use your own authentication or Hathora's Auth Client.
    """

    app_secret: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="appSecret"),
        pydantic.Field(alias="appSecret", description="Secret that is used for identity and access management."),
    ]
    """
    Secret that is used for identity and access management.
    """

    app_id: typing_extensions.Annotated[AppId, FieldMetadata(alias="appId"), pydantic.Field(alias="appId")]
    app_name: typing_extensions.Annotated[AppName, FieldMetadata(alias="appName"), pydantic.Field(alias="appName")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
