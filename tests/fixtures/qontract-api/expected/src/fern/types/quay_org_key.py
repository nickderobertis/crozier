

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class QuayOrgKey(UniversalBaseModel):
    """
    Identifies a Quay organization uniquely across instances.
    """

    instance: str = pydantic.Field()
    """
    Quay instance name (e.g. quay.io)
    """

    org_name: str = pydantic.Field()
    """
    Quay organization name
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
