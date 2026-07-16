

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Location(UniversalBaseModel):
    teams: typing.List[typing.Dict[str, str]] = pydantic.Field()
    """
    Team ids
    """

    tenant: str = pydantic.Field()
    """
    Tenant id
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
