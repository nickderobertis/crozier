

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SectionHeader(UniversalBaseModel):
    """
    A widget that defines a new section header. Sections populate a table of contents and allow easier navigation of long-form content.
    """

    divider_below: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="dividerBelow"),
        pydantic.Field(
            alias="dividerBelow", description="Whether to insert a divider below the section in the table of contents"
        ),
    ] = None
    """
    Whether to insert a divider below the section in the table of contents
    """

    subtitle: typing.Optional[str] = pydantic.Field(default=None)
    """
    The subtitle of the section
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
