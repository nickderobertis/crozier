

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .extract_batch_request_items_item_grounding import ExtractBatchRequestItemsItemGrounding
from .extract_batch_request_items_item_llm_options import ExtractBatchRequestItemsItemLlmOptions


class ExtractBatchRequestItemsItem(UniversalBaseModel):
    client_item_id: str
    file_index: typing.Optional[int] = None
    file_id: typing.Optional[str] = None
    pipeline_id: typing.Optional[str] = None
    ocr_model: typing.Optional[str] = None
    ocr_options: typing.Optional[typing.Dict[str, typing.Any]] = None
    llm_model: typing.Optional[str] = None
    llm_options: typing.Optional[ExtractBatchRequestItemsItemLlmOptions] = None
    schema_: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]], FieldMetadata(alias="schema"), pydantic.Field(alias="schema")
    ] = None
    repair_attempts: typing.Optional[int] = None
    grounding: typing.Optional[ExtractBatchRequestItemsItemGrounding] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
