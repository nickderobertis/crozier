

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transfer_operation_type import TransferOperationType


class Transfer(UniversalBaseModel):
    operation_type: typing.Optional[TransferOperationType] = pydantic.Field(default=None)
    """
    Operations:
      * `upload`
      * `download`
    """

    path: typing.Optional[str] = pydantic.Field(default=None)
    """
    file path for the upload/download
    """

    start_time: typing.Optional[int] = pydantic.Field(default=None)
    """
    start time as unix timestamp in milliseconds
    """

    size: typing.Optional[int] = pydantic.Field(default=None)
    """
    bytes transferred
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
