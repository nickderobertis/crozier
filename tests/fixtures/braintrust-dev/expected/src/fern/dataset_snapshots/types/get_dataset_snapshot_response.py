

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.dataset_snapshot import DatasetSnapshot


class GetDatasetSnapshotResponse(UniversalBaseModel):
    objects: typing.List[DatasetSnapshot] = pydantic.Field()
    """
    A list of dataset_snapshot objects
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
