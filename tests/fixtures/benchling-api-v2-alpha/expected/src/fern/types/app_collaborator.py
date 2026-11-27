

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .app_collaborator_type import AppCollaboratorType
from .app_summary import AppSummary


class AppCollaborator(AppSummary):
    type: typing.Optional[AppCollaboratorType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
