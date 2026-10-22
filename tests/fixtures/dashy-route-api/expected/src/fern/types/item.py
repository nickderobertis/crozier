

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .item_fields_target import ItemFieldsTarget


class Item(UniversalBaseModel):
    """
    A single link, app or service. Requires a `title`.
    """

    title: str = pydantic.Field()
    """
    Display name
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Text shown on hover
    """

    icon: typing.Optional[str] = pydantic.Field(default=None)
    """
    Icon (URL, favicon, font-awesome, etc.)
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Target URL
    """

    target: typing.Optional[ItemFieldsTarget] = pydantic.Field(default=None)
    """
    How the link opens
    """

    provider: typing.Optional[str] = pydantic.Field(default=None)
    """
    Hosting provider name
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier
    """

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Tags for filtering
    """

    hotkey: typing.Optional[int] = pydantic.Field(default=None)
    """
    Numeric keyboard shortcut
    """

    rel: typing.Optional[str] = pydantic.Field(default=None)
    """
    Anchor rel attribute
    """

    color: typing.Optional[str] = pydantic.Field(default=None)
    """
    Text color
    """

    background_color: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="backgroundColor"),
        pydantic.Field(alias="backgroundColor", description="Background color"),
    ] = None
    """
    Background color
    """

    display_data: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="displayData"),
        pydantic.Field(alias="displayData", description="Per-item display options"),
    ] = None
    """
    Per-item display options
    """

    sub_items: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Dict[str, typing.Any]]],
        FieldMetadata(alias="subItems"),
        pydantic.Field(alias="subItems", description="Nested child items"),
    ] = None
    """
    Nested child items
    """

    status_check: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="statusCheck"),
        pydantic.Field(alias="statusCheck", description="Enable status check for this item"),
    ] = None
    """
    Enable status check for this item
    """

    status_check_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="statusCheckUrl"),
        pydantic.Field(alias="statusCheckUrl", description="Override URL to ping"),
    ] = None
    """
    Override URL to ping
    """

    status_check_headers: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="statusCheckHeaders"),
        pydantic.Field(alias="statusCheckHeaders", description="Headers sent with the status check"),
    ] = None
    """
    Headers sent with the status check
    """

    status_check_allow_insecure: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="statusCheckAllowInsecure"),
        pydantic.Field(alias="statusCheckAllowInsecure", description="Allow invalid TLS certs"),
    ] = None
    """
    Allow invalid TLS certs
    """

    status_check_accept_codes: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="statusCheckAcceptCodes"),
        pydantic.Field(alias="statusCheckAcceptCodes", description="Extra HTTP codes treated as up"),
    ] = None
    """
    Extra HTTP codes treated as up
    """

    status_check_max_redirects: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="statusCheckMaxRedirects"),
        pydantic.Field(alias="statusCheckMaxRedirects", description="Max redirects to follow"),
    ] = None
    """
    Max redirects to follow
    """

    ping_check_enabled: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="pingCheckEnabled"),
        pydantic.Field(alias="pingCheckEnabled", description="Enable ICMP ping check"),
    ] = None
    """
    Enable ICMP ping check
    """

    ping_check_host: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pingCheckHost"),
        pydantic.Field(alias="pingCheckHost", description="Host to ping"),
    ] = None
    """
    Host to ping
    """

    ping_check_interval: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="pingCheckInterval"),
        pydantic.Field(alias="pingCheckInterval", description="Ping interval (seconds)"),
    ] = None
    """
    Ping interval (seconds)
    """

    ping_check_count: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="pingCheckCount"),
        pydantic.Field(alias="pingCheckCount", description="Number of pings"),
    ] = None
    """
    Number of pings
    """

    ping_check_timeout: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="pingCheckTimeout"),
        pydantic.Field(alias="pingCheckTimeout", description="Ping timeout (ms)"),
    ] = None
    """
    Ping timeout (ms)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
