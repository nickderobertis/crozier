

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .user_collaborator_type import UserCollaboratorType
from .user_summary import UserSummary


class UserCollaborator(UserSummary):
    type: typing.Optional[UserCollaboratorType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
