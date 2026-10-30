

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ParseBatchItem(UniversalBaseModel):
    client_item_id: str = pydantic.Field()
    """
    Caller-supplied stable identifier for this batch item.
    """

    file_index: typing.Optional[int] = pydantic.Field(default=None)
    """
    Zero-based index into the uploaded `files` array. Exactly one of `file_index` or
    `file_id` is required per item.
    """

    file_id: typing.Optional[str] = None
    ocr_model: str
    ocr_options: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
