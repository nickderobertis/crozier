

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DeviceSpec(UniversalBaseModel):
    """
    Session identity and request metadata captured for a device.
    """

    ip_address: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="ipAddress"),
        pydantic.Field(alias="ipAddress", description="Client IP address observed for the session."),
    ]
    """
    Client IP address observed for the session.
    """

    last_accessed_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="lastAccessedTime"),
        pydantic.Field(alias="lastAccessedTime", description="Last time this session accessed Halo."),
    ] = None
    """
    Last time this session accessed Halo.
    """

    last_authenticated_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="lastAuthenticatedTime"),
        pydantic.Field(alias="lastAuthenticatedTime", description="Last time the user authenticated for this session."),
    ] = None
    """
    Last time the user authenticated for this session.
    """

    principal_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="principalName"),
        pydantic.Field(alias="principalName", description="Principal name of the authenticated user."),
    ]
    """
    Principal name of the authenticated user.
    """

    remember_me_series_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="rememberMeSeriesId"),
        pydantic.Field(
            alias="rememberMeSeriesId", description="Remember-me series id associated with the session, if any."
        ),
    ] = None
    """
    Remember-me series id associated with the session, if any.
    """

    session_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="sessionId"),
        pydantic.Field(alias="sessionId", description="Web session identifier associated with the device."),
    ]
    """
    Web session identifier associated with the device.
    """

    user_agent: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="userAgent"),
        pydantic.Field(alias="userAgent", description="Client user-agent header captured for the session."),
    ] = None
    """
    Client user-agent header captured for the session.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
