

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ContainerMappingIsobmffContainer(UniversalBaseModel):
    """
    Mapping to ISO Base Media File Format (e.g. MP4 and MOV) containers, ISO/IEC 14496-12
    """

    track_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The track ID
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
