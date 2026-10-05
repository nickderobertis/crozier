

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class OcmClusterInfo(UniversalBaseModel):
    """
    A single OCM cluster matching label_key_prefix, with merged labels.

    labels is the flat, merged view of subscription-level and
    organization-level labels whose key starts with label_key_prefix
    (subscription-level labels win on key collisions). Label *interpretation*
    is left entirely to the caller.
    """

    console_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Cluster console URL
    """

    external_auth_enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether external auth is enabled on the cluster
    """

    id: str = pydantic.Field()
    """
    OCM cluster id
    """

    labels: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Merged subscription+organization labels matching label_key_prefix
    """

    name: str = pydantic.Field()
    """
    Cluster name
    """

    organization_id: str = pydantic.Field()
    """
    OCM organization id
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
