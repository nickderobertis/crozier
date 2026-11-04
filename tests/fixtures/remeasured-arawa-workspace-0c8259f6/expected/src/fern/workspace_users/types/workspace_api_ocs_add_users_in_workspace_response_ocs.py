

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.confirmation_message import ConfirmationMessage
from ...types.ocs_meta import OcsMeta


class WorkspaceApiOcsAddUsersInWorkspaceResponseOcs(UniversalBaseModel):
    meta: OcsMeta
    data: ConfirmationMessage

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
