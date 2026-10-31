

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .namespace_id import NamespaceId
from .run_no import RunNo


class GrepIndexStatusDisabled(UniversalBaseModel):
    """
    No index is maintained for this namespace.
    """

    namespace_id: NamespaceId = pydantic.Field()
    """
    The namespace that the status describes.
    """

    next_run_no: RunNo = pydantic.Field()
    """
    The next run number that the index allocates.
    """

    reorganize_pending: bool = pydantic.Field()
    """
    Whether a partitioned segment reorganization is in progress.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
