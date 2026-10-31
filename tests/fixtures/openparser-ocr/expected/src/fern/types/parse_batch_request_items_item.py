

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ParseBatchRequestItemsItem(UniversalBaseModel):
    client_item_id: str
    file_index: typing.Optional[int] = None
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
