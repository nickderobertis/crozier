

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .bandwidth_limit import BandwidthLimit
from .hooks_filter import HooksFilter
from .login_methods import LoginMethods
from .mfa_protocols import MfaProtocols
from .patterns_filter import PatternsFilter
from .supported_protocols import SupportedProtocols
from .time_period import TimePeriod
from .user_type import UserType
from .web_client_options import WebClientOptions


class BaseUserFilters(UniversalBaseModel):
    """
    Additional user options
    """

    allowed_ip: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    only clients connecting from these IP/Mask are allowed. IP/Mask must be in CIDR notation as defined in RFC 4632 and RFC 4291, for example "192.0.2.0/24" or "2001:db8::/32"
    """

    denied_ip: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    clients connecting from these IP/Mask are not allowed. Denied rules are evaluated before allowed ones
    """

    denied_login_methods: typing.Optional[typing.List[LoginMethods]] = pydantic.Field(default=None)
    """
    if null or empty any available login method is allowed
    """

    denied_protocols: typing.Optional[typing.List[SupportedProtocols]] = pydantic.Field(default=None)
    """
    if null or empty any available protocol is allowed
    """

    file_patterns: typing.Optional[typing.List[PatternsFilter]] = pydantic.Field(default=None)
    """
    filters based on shell like file patterns. These restrictions do not apply to files listing for performance reasons, so a denied file cannot be downloaded/overwritten/renamed but it will still be in the list of files. Please note that these restrictions can be easily bypassed
    """

    max_upload_file_size: typing.Optional[int] = pydantic.Field(default=None)
    """
    maximum allowed size, as bytes, for a single file upload. The upload will be aborted if/when the size of the file being sent exceeds this limit. 0 means unlimited
    """

    tls_username: typing.Optional[str] = pydantic.Field(default=None)
    """
    defines the TLS certificate field to use as username. For FTP clients it must match the name provided using the "USER" command. For WebDAV, if no username is provided, the CN will be used as username. For WebDAV clients it must match the implicit or provided username. Ignored if mutual TLS is disabled. Currently the only supported value is `CommonName`
    """

    hooks: typing.Optional[HooksFilter] = None
    disable_fs_checks: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Disable checks for existence and automatic creation of home directory and virtual folders. SFTPGo requires that the user's home directory, virtual folder root, and intermediate paths to virtual folders exist to work properly. If you already know that the required directories exist, disabling these checks will speed up login. You could, for example, disable these checks after the first login
    """

    web_client: typing.Optional[typing.List[WebClientOptions]] = pydantic.Field(default=None)
    """
    WebClient/user REST API related configuration options
    """

    allow_api_key_auth: typing.Optional[bool] = pydantic.Field(default=None)
    """
    API key authentication allows to impersonate this user with an API key
    """

    user_type: typing.Optional[UserType] = None
    bandwidth_limits: typing.Optional[typing.List[BandwidthLimit]] = None
    external_auth_cache_time: typing.Optional[int] = pydantic.Field(default=None)
    """
    Defines the cache time, in seconds, for users authenticated using an external auth hook. 0 means no cache
    """

    start_directory: typing.Optional[str] = pydantic.Field(default=None)
    """
    Specifies an alternate starting directory. If not set, the default is "/". This option is supported for SFTP/SCP, FTP and HTTP (WebClient/REST API) protocols. Relative paths will use this directory as base.
    """

    two_factor_protocols: typing.Optional[typing.List[MfaProtocols]] = pydantic.Field(default=None)
    """
    Defines protocols that require two factor authentication
    """

    ftp_security: typing.Optional[int] = pydantic.Field(default=None)
    """
    Set to `1` to require TLS for both data and control connection. This setting is useful to allow both encrypted and plain text FTP sessions globally and require encrypted sessions on a per-user basis. The requirement is enforced after the authentication, so it holds for accounts resolved during the login as well; cleartext sessions are closed before the password is sent when the account can be resolved beforehand. It has no effect if TLS is already required for all users in the configuration file.
    """

    is_anonymous: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If enabled the user can login with any password or no password at all. Anonymous users are supported for FTP and WebDAV protocols and permissions will be automatically set to "list" and "download" (read only)
    """

    default_shares_expiration: typing.Optional[int] = pydantic.Field(default=None)
    """
    Defines the default expiration for newly created shares as number of days. 0 means no expiration
    """

    max_shares_expiration: typing.Optional[int] = pydantic.Field(default=None)
    """
    Defines the maximum allowed expiration, as a number of days, when a user creates or updates a share. 0 means no expiration
    """

    password_expiration: typing.Optional[int] = pydantic.Field(default=None)
    """
    The password expires after the defined number of days. 0 means no expiration
    """

    password_strength: typing.Optional[int] = pydantic.Field(default=None)
    """
    Defines the minimum password strength. 0 means disabled, any password will be accepted. Values in the 50-70 range are suggested for common use cases
    """

    access_time: typing.Optional[typing.List[TimePeriod]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
