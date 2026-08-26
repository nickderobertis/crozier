

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .known_unions_command import KnownUnionsCommand
from .known_unions_data_type import KnownUnionsDataType
from .known_unions_error import KnownUnionsError
from .known_unions_notification import KnownUnionsNotification


class KnownUnions(UniversalBaseModel):
    command: KnownUnionsCommand
    data_type: KnownUnionsDataType
    error: KnownUnionsError
    notification: KnownUnionsNotification

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(KnownUnions)
