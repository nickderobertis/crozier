

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DiskRequestBodyAttributes_Gp3(UniversalBaseModel):
    type: typing.Literal["gp3"] = "gp3"
    iops: int
    size_gb: int
    throughput_mibps: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DiskRequestBodyAttributes_Io2(UniversalBaseModel):
    type: typing.Literal["io2"] = "io2"
    iops: int
    size_gb: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DiskRequestBodyAttributes = typing_extensions.Annotated[
    typing.Union[DiskRequestBodyAttributes_Gp3, DiskRequestBodyAttributes_Io2], pydantic.Field(discriminator="type")
]
