

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_v1shape_response_data_data_item_headers import GetV1ShapeResponseDataDataItemHeaders


class GetV1ShapeResponseDataDataItem(UniversalBaseModel):
    """
    Operation message
    """

    headers: typing.Optional[GetV1ShapeResponseDataDataItemHeaders] = pydantic.Field(default=None)
    """
    Metadata about the operation.
    """

    key: typing.Optional[str] = pydantic.Field(default=None)
    """
    Row ID
    """

    value: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    The row data.
    """

    old_value: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    The previous value for changed columns on an update.
    Only present when `replica=full`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
