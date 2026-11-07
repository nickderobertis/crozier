

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .stream_data_delete_result import StreamDataDeleteResult


class StreamDeleteResult(UniversalBaseModel):
    entity_model_class_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="entityModelClassId"), pydantic.Field(alias="entityModelClassId")
    ]
    ids: typing.Optional[typing.List[str]] = None
    delete_result: typing_extensions.Annotated[
        StreamDataDeleteResult, FieldMetadata(alias="deleteResult"), pydantic.Field(alias="deleteResult")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
