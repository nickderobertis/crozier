

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .parse_batch_request_items_item import ParseBatchRequestItemsItem
from .parse_batch_request_output_format import ParseBatchRequestOutputFormat


class ParseBatchRequest(UniversalBaseModel):
    items: typing.List[ParseBatchRequestItemsItem] = pydantic.Field()
    """
    Ordered batch items. Each item references either an uploaded `files` entry via
    `file_index` or an Eigenpal reusable `file_id`. Uploaded files must be covered by
    exactly one unique `file_index` in `[0, files.length)`.
    """

    output_format: typing.Optional[ParseBatchRequestOutputFormat] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
