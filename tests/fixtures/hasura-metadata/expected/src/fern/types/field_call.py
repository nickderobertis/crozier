

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .remote_arguments import RemoteArguments


class FieldCall(UniversalBaseModel):
    arguments: RemoteArguments
    field: typing.Optional["RemoteFields"] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .remote_fields import RemoteFields

update_forward_refs(FieldCall, RemoteFields=RemoteFields)
