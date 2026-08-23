

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .format import Format
from .transmission_mode import TransmissionMode


class Output(UniversalBaseModel):
    format: typing.Optional[Format] = None
    transmission_mode: typing_extensions.Annotated[
        typing.Optional[TransmissionMode],
        FieldMetadata(alias="transmissionMode"),
        pydantic.Field(alias="transmissionMode"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(Output)
