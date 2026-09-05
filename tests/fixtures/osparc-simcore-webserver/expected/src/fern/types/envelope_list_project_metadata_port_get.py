

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .project_metadata_port_get import ProjectMetadataPortGet


class EnvelopeListProjectMetadataPortGet(UniversalBaseModel):
    data: typing.Optional[typing.List[ProjectMetadataPortGet]] = None
    error: typing.Optional[typing.Any] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
