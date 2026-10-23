

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Tenant(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    Name of the tenant.
    """

    esd: str = pydantic.Field()
    """
    Entitlements group Sub Domain (ESD). For instance, if the entitlements group is users.datalake.viewers@{datapartition}.{domain}.com, the esd value is {datapartition}.{domain}.com. It has to start with the name of the data partition.
    """

    gcpid: str = pydantic.Field()
    """
    Google cloud project id associated with the tenant. For other providers, name of the data partition.
    """

    default_acls: str = pydantic.Field()
    """
    Entitlements authorization group to manage tenant administrators.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
