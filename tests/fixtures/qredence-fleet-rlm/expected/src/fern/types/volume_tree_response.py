

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class VolumeTreeResponse(UniversalBaseModel):
    """
    Logical files visible in the LocalScope Workspace Volume.
    """

    paths: typing.List[str]
    directories: typing.Optional[typing.List[str]] = None
    truncated: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
