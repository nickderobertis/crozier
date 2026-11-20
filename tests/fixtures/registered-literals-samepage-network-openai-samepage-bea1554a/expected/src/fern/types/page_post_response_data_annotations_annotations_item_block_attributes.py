

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .page_post_response_data_annotations_annotations_item_block_attributes_view_type import (
    PagePostResponseDataAnnotationsAnnotationsItemBlockAttributesViewType,
)


class PagePostResponseDataAnnotationsAnnotationsItemBlockAttributes(UniversalBaseModel):
    level: float
    view_type: typing_extensions.Annotated[
        PagePostResponseDataAnnotationsAnnotationsItemBlockAttributesViewType,
        FieldMetadata(alias="viewType"),
        pydantic.Field(alias="viewType"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
