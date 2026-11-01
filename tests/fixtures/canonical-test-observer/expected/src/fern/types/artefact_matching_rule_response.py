

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .family_name import FamilyName
from .permission import Permission
from .team_minimal import TeamMinimal


class ArtefactMatchingRuleResponse(UniversalBaseModel):
    """
    Artefact matching rule with associated teams
    """

    id: int
    name: typing.Optional[str] = None
    family: FamilyName
    stage: typing.Optional[str] = None
    track: typing.Optional[str] = None
    branch: typing.Optional[str] = None
    store: typing.Optional[str] = None
    series: typing.Optional[str] = None
    os: typing.Optional[str] = None
    release: typing.Optional[str] = None
    owner: typing.Optional[str] = None
    teams: typing.List[TeamMinimal]
    grant_permissions: typing.List[Permission]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
