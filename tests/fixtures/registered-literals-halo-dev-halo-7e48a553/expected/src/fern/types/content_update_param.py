

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ContentUpdateParam(UniversalBaseModel):
    """
    Content update payload for post and single page editors.
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

    version: typing.Optional[int] = pydantic.Field(default=None)
    """
    Expected current head snapshot version; conflicts create a new head snapshot.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
