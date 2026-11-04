

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetShipmentResponse_Parcel(UniversalBaseModel):
    kind: typing.Literal["parcel"] = "parcel"
    weight: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GetShipmentResponse_Notice(UniversalBaseModel):
    kind: typing.Literal["notice"] = "notice"
    message: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


GetShipmentResponse = typing_extensions.Annotated[
    typing.Union[GetShipmentResponse_Parcel, GetShipmentResponse_Notice], pydantic.Field(discriminator="kind")
]
