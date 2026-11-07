

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Content(UniversalBaseModel):
    """
    Full content payload reconstructed from a content snapshot.
    """

    content: str = pydantic.Field()
    """
    Rendered HTML or normalized content derived from raw.
    """

    raw: str = pydantic.Field()
    """
    Source text stored by the editor.
    """

    raw_type: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="rawType"),
        pydantic.Field(
            alias="rawType", description="Editor/source format of the raw content, for example HTML or Markdown."
        ),
    ]
    """
    Editor/source format of the raw content, for example HTML or Markdown.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
