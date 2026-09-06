

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class BatchCreateCustomFontsResponseFailedItem(UniversalBaseModel):
    index: int = pydantic.Field()
    """
    Zero-based position of the font in the request `items` array
    """

    file_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="fileName"),
        pydantic.Field(alias="fileName", description="The `fileName` of the font that could not be registered"),
    ]
    """
    The `fileName` of the font that could not be registered
    """

    name: str = pydantic.Field()
    """
    Error name. `FontLimitReached` indicates the site's custom font limit was reached before this font could be registered.
    """

    msg: str = pydantic.Field()
    """
    Human-readable error message
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
