

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class FaultTypeDto_Nonfatal(UniversalBaseModel):
    """
    Describes the nature of a given fault simulation, and specifically the impact that it should have on any Trackables or channel activity during and after resolution.
    """

    type: typing.Literal["nonfatal"] = "nonfatal"
    resolved_within_millis: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="resolvedWithinMillis"), pydantic.Field(alias="resolvedWithinMillis")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FaultTypeDto_NonfatalWhenResolved(UniversalBaseModel):
    value: typing.Any
    type: typing.Literal["nonfatalWhenResolved"] = "nonfatalWhenResolved"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True


class FaultTypeDto_Fatal(UniversalBaseModel):
    """
    Describes the nature of a given fault simulation, and specifically the impact that it should have on any Trackables or channel activity during and after resolution.
    """

    type: typing.Literal["fatal"] = "fatal"
    failed_within_millis: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="failedWithinMillis"), pydantic.Field(alias="failedWithinMillis")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


FaultTypeDto = typing_extensions.Annotated[
    typing.Union[FaultTypeDto_Nonfatal, FaultTypeDto_NonfatalWhenResolved, FaultTypeDto_Fatal],
    pydantic.Field(discriminator="type"),
]
