

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V1Permission(UniversalBaseModel):
    resource: str = pydantic.Field()
    """
    Resource name (e.g., user, project, hour)
    """

    permissions: typing.List[str] = pydantic.Field()
    """
    List of permitted operations for this resource
    """

    global_permissions: typing.List[str] = pydantic.Field()
    """
    List of globally permitted operations for this resource
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
