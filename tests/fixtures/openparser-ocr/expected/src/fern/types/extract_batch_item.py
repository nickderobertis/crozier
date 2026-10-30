

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .extract_batch_item_grounding import ExtractBatchItemGrounding
from .extract_batch_item_llm_options import ExtractBatchItemLlmOptions


class ExtractBatchItem(UniversalBaseModel):
    """
    Per-item file-backed extract config with the same `pipeline_id` XOR inline rules as
    single extract. Sources are `file_index` or `file_id`; `parse_job_id` is not supported
    in batch. No parent-level batch pipeline in v1.
    """

    client_item_id: str
    file_index: typing.Optional[int] = pydantic.Field(default=None)
    """
    Zero-based index into the uploaded `files` array. Exactly one of `file_index` or
    `file_id` is required per item.
    """

    file_id: typing.Optional[str] = None
    pipeline_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Saved extraction pipeline id; mutually exclusive with inline extract fields.
    """

    ocr_model: typing.Optional[str] = None
    ocr_options: typing.Optional[typing.Dict[str, typing.Any]] = None
    llm_model: typing.Optional[str] = None
    llm_options: typing.Optional[ExtractBatchItemLlmOptions] = None
    schema_: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]], FieldMetadata(alias="schema"), pydantic.Field(alias="schema")
    ] = None
    repair_attempts: typing.Optional[int] = None
    grounding: typing.Optional[ExtractBatchItemGrounding] = pydantic.Field(default=None)
    """
    Optional field grounding mode. Defaults to `none`. `field` opts into verified
    per-leaf citations and is part of idempotency identity.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
