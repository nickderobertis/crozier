

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .problem import Problem


class AlreadyMemberProblem(Problem):
    """
    Names the team the caller already belongs to, so that a refusal still answers the question the call was asking.
    """

    team_id: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
