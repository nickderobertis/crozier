

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dns_record import DnsRecord
from .domain_object import DomainObject


class Domain(UniversalBaseModel):
    object: DomainObject = pydantic.Field()
    """
    Object type identifier
    """

    id: str = pydantic.Field()
    """
    Unique identifier for the domain
    """

    created_at: dt.datetime = pydantic.Field()
    """
    When the domain was created
    """

    updated_at: dt.datetime = pydantic.Field()
    """
    When the domain was last updated
    """

    domain: str = pydantic.Field()
    """
    The domain name
    """

    account_id: str = pydantic.Field()
    """
    Account ID this domain belongs to
    """

    dns_records: typing.List[DnsRecord] = pydantic.Field()
    """
    DNS records required for domain verification
    """

    last_dns_check_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    When DNS records were last checked
    """

    dns_valid: bool = pydantic.Field()
    """
    Whether all required DNS records are properly configured
    """

    tracking_subdomain: typing.Optional[str] = pydantic.Field(default=None)
    """
    Custom tracking subdomain. Null means the account or product default is used. Applies to both manual-DNS and managed-DNS domains.
    """

    return_path_subdomain: typing.Optional[str] = pydantic.Field(default=None)
    """
    Custom return-path subdomain. Null means the account or product default is used. Applies to both manual-DNS and managed-DNS domains.
    """

    subscription_subdomain: typing.Optional[str] = pydantic.Field(default=None)
    """
    Custom subscription management subdomain. Null means the account or product default is used. Applies to both manual-DNS and managed-DNS domains.
    """

    media_subdomain: typing.Optional[str] = pydantic.Field(default=None)
    """
    Custom media subdomain. Null means the account or product default is used. Applies to both manual-DNS and managed-DNS domains.
    """

    dkim_rotation_interval_days: typing.Optional[int] = pydantic.Field(default=None)
    """
    Custom DKIM rotation interval in days. Null means the account default is used. Only supported for managed DNS domains.
    """

    dkim_selector: typing.Optional[str] = pydantic.Field(default=None)
    """
    Per-domain DKIM selector override. Null means no per-domain override is set.
    
    This reports the configured per-domain override only, not the effective selector used for DKIM signing. The effective selector is resolved separately and can differ — for example, a selector locked after DNS verification takes precedence over this override.
    """

    rotation_ready: bool = pydantic.Field()
    """
    Whether the standby DKIM slot is ready for rotation.
    """

    dsn_recipient: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional recipient address for delivery status notifications.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
