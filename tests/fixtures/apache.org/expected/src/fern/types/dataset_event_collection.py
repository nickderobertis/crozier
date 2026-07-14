

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .collection_info import CollectionInfo
from .dataset_event import DatasetEvent


class DatasetEventCollection(CollectionInfo):
    """
    A collection of dataset events.

    *New in version 2.4.0*
    """

    dataset_events: typing.Optional[typing.List[DatasetEvent]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
