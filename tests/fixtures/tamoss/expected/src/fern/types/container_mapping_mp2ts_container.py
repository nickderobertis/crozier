

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ContainerMappingMp2TsContainer(UniversalBaseModel):
    """
    Mapping to MPEG-2 Transport Stream containers, ISO/IEC 13818-1 or ITU-T Recommendation H.222.0
    """

    pid: typing.Optional[int] = pydantic.Field(default=None)
    """
    The packet ID for the elementary stream packets
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
