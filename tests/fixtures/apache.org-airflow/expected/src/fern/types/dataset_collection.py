

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .collection_info import CollectionInfo
from .dataset import Dataset


class DatasetCollection(CollectionInfo):
    """
    A collection of datasets.

    *New in version 2.4.0*
    """

    datasets: typing.Optional[typing.List[Dataset]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
