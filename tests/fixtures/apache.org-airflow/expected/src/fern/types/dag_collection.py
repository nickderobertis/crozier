

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .collection_info import CollectionInfo
from .dag import Dag


class DagCollection(CollectionInfo):
    """
    Collection of DAGs.

    *Changed in version 2.1.0*&#58; 'total_entries' field is added.
    """

    dags: typing.Optional[typing.List[Dag]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
