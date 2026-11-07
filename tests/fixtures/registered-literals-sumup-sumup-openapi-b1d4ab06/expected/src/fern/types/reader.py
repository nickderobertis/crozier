

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .metadata import Metadata
from .reader_device import ReaderDevice
from .reader_id import ReaderId
from .reader_name import ReaderName
from .reader_status import ReaderStatus


class Reader(UniversalBaseModel):
    """
    A physical card reader device that can accept in-person payments.
    """

    id: ReaderId
    name: ReaderName
    status: ReaderStatus
    device: ReaderDevice
    metadata: typing.Optional[Metadata] = None
    service_account_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Identifier of the system-managed service account associated with this reader.
    Present only for readers that are already paired.
    This field is currently in beta and may change.
    """

    created_at: dt.datetime = pydantic.Field()
    """
    The timestamp of when the reader was created.
    """

    updated_at: dt.datetime = pydantic.Field()
    """
    The timestamp of when the reader was last updated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
