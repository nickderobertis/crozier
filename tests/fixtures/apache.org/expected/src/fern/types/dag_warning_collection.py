

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .collection_info import CollectionInfo
from .dag_warning import DagWarning


class DagWarningCollection(CollectionInfo):
    """
    Collection of DAG warnings.
    """

    import_errors: typing.Optional[typing.List[DagWarning]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
