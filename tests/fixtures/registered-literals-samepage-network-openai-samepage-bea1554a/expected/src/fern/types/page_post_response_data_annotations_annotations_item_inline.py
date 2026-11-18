

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .page_post_response_data_annotations_annotations_item_inline_attributes import (
    PagePostResponseDataAnnotationsAnnotationsItemInlineAttributes,
)


class PagePostResponseDataAnnotationsAnnotationsItemInline(UniversalBaseModel):
    start: float
    end: float
    attributes: typing.Optional[PagePostResponseDataAnnotationsAnnotationsItemInlineAttributes] = None
    app_attributes: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Dict[str, str]]],
        FieldMetadata(alias="appAttributes"),
        pydantic.Field(alias="appAttributes"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
