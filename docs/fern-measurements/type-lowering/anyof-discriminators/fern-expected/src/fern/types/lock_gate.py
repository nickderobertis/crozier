

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LockGate_Swing(UniversalBaseModel):
    """
    A typed, required tag under an anyOf mapping.
    """

    gate_type: typing.Literal["swing"] = "swing"
    leaves: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class LockGate_Slide(UniversalBaseModel):
    """
    A typed, required tag under an anyOf mapping.
    """

    gate_type: typing.Literal["slide"] = "slide"
    track: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


LockGate = typing_extensions.Annotated[
    typing.Union[LockGate_Swing, LockGate_Slide], pydantic.Field(discriminator="gate_type")
]
