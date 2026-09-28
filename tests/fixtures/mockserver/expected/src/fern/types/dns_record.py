

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .dns_record_dns_class import DnsRecordDnsClass
from .dns_record_type import DnsRecordType


class DnsRecord(UniversalBaseModel):
    """
    DNS record
    """

    name: typing.Optional[str] = None
    type: typing.Optional[DnsRecordType] = None
    dns_class: typing_extensions.Annotated[
        typing.Optional[DnsRecordDnsClass], FieldMetadata(alias="dnsClass"), pydantic.Field(alias="dnsClass")
    ] = None
    ttl: typing.Optional[int] = None
    value: typing.Optional[str] = None
    priority: typing.Optional[int] = None
    weight: typing.Optional[int] = None
    port: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
