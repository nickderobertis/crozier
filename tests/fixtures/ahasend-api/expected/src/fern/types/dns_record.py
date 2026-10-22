

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DnsRecord(UniversalBaseModel):
    type: str = pydantic.Field()
    """
    DNS record type (e.g., CNAME, TXT, MX)
    """

    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    Human-readable DNS record label
    """

    host: str = pydantic.Field()
    """
    DNS record host/name
    """

    content: str = pydantic.Field()
    """
    DNS record content/value
    """

    required: bool = pydantic.Field()
    """
    Whether this DNS record is required for domain verification
    """

    propagated: bool = pydantic.Field()
    """
    Whether this DNS record has been propagated and verified
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
