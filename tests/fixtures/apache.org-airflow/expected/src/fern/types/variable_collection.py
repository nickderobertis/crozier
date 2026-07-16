

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .collection_info import CollectionInfo
from .variable_collection_item import VariableCollectionItem


class VariableCollection(CollectionInfo):
    """
    Collection of variables.

    *Changed in version 2.1.0*&#58; 'total_entries' field is added.
    """

    variables: typing.Optional[typing.List[VariableCollectionItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
