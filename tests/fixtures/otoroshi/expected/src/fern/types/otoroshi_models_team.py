

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class OtoroshiModelsTeam(UniversalBaseModel):
    """
    An otoroshi model for a team of users in the organization (otoroshi-ui)
    """

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Entity tags
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Entity name
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Entity description
    """

    tenant: typing.Optional[typing.Any] = None
    metadata: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Entity metadata
    """

    id: typing.Optional[typing.Any] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
