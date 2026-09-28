

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .otoroshi_models_team_access import OtoroshiModelsTeamAccess


class OtoroshiModelsUserRight(UniversalBaseModel):
    """
    Represent a user right (teams, organizations) in otoroshi-ui
    """

    tenant: typing.Optional[typing.Any] = None
    teams: typing.Optional[typing.List[OtoroshiModelsTeamAccess]] = pydantic.Field(default=None)
    """
    Access rights on teams
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
