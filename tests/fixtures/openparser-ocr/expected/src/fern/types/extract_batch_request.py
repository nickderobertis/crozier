

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .extract_batch_request_items_item import ExtractBatchRequestItemsItem
from .extract_batch_request_output_format import ExtractBatchRequestOutputFormat


class ExtractBatchRequest(UniversalBaseModel):
    items: typing.List[ExtractBatchRequestItemsItem] = pydantic.Field()
    """
    Ordered batch items. Each item references either an uploaded `files` entry via
    `file_index` or an Eigenpal reusable `file_id`.
    """

    output_format: typing.Optional[ExtractBatchRequestOutputFormat] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
