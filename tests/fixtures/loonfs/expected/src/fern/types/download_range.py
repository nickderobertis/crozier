

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .object_transfer_access import ObjectTransferAccess


class DownloadRange(UniversalBaseModel):
    """
    One contiguous run of a revision's bytes, which the client reads from one object.
    """

    access: ObjectTransferAccess = pydantic.Field()
    """
    A short-lived read capability for exactly this range's bytes.
    """

    length: int = pydantic.Field()
    """
    The number of bytes in the run.
    """

    start_offset: int = pydantic.Field()
    """
    The offset of the run's first byte in the revision.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
