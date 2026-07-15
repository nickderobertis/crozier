

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .collection_info import CollectionInfo
from .import_error import ImportError


class ImportErrorCollection(CollectionInfo):
    """
    Collection of import errors.

    *Changed in version 2.1.0*&#58; 'total_entries' field is added.
    """

    import_errors: typing.Optional[typing.List[ImportError]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
