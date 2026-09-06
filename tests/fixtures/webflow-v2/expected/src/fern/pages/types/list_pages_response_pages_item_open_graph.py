

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class ListPagesResponsePagesItemOpenGraph(UniversalBaseModel):
    """
    Open Graph fields for the Page
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    The title supplied to Open Graph annotations
    """

    title_copied: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="titleCopied"),
        pydantic.Field(alias="titleCopied", description="Indicates the Open Graph title was copied from the SEO title"),
    ] = None
    """
    Indicates the Open Graph title was copied from the SEO title
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description supplied to Open Graph annotations
    """

    description_copied: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="descriptionCopied"),
        pydantic.Field(
            alias="descriptionCopied",
            description="Indicates the Open Graph description was copied from the SEO description",
        ),
    ] = None
    """
    Indicates the Open Graph description was copied from the SEO description
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
