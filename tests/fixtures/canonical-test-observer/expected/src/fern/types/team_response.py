

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .artefact_matching_rule_in_response import ArtefactMatchingRuleInResponse
from .permission import Permission
from .user_minimal_response import UserMinimalResponse


class TeamResponse(UniversalBaseModel):
    id: int
    name: str
    permissions: typing.List[Permission]
    members: typing.List[UserMinimalResponse]
    artefact_matching_rules: typing.List[ArtefactMatchingRuleInResponse]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
