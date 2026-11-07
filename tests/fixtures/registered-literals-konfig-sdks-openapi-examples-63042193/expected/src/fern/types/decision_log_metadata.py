

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .decision_log_metadata_vcs import DecisionLogMetadataVcs


class DecisionLogMetadata(UniversalBaseModel):
    build_number: typing.Optional[int] = None
    project_id: typing.Optional[str] = None
    ssh_rerun: typing.Optional[bool] = None
    vcs: typing.Optional[DecisionLogMetadataVcs] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
