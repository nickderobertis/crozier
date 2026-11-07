

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .listed_snapshot_spec import ListedSnapshotSpec
from .metadata import Metadata


class ListedSnapshotDto(UniversalBaseModel):
    """
    Content snapshot list item with metadata and display-oriented snapshot fields.
    """

    metadata: Metadata
    spec: ListedSnapshotSpec

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
