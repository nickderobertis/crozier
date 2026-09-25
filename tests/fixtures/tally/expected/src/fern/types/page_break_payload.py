

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .button import Button
from .name import Name


class PageBreakPayload(UniversalBaseModel):
    """
    Payload for PAGE_BREAK block type. Used for multi-page form navigation.
    """

    index: typing.Optional[float] = pydantic.Field(default=None)
    """
    Sequential position of this page break within the form, starting from 0.
    """

    is_first: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isFirst"),
        pydantic.Field(alias="isFirst", description="When true, indicates this is the first page break in the form."),
    ] = None
    """
    When true, indicates this is the first page break in the form.
    """

    is_last: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isLast"),
        pydantic.Field(alias="isLast", description="When true, indicates this is the last page break in the form."),
    ] = None
    """
    When true, indicates this is the last page break in the form.
    """

    name: typing.Optional[Name] = None
    is_thank_you_page: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isThankYouPage"),
        pydantic.Field(
            alias="isThankYouPage",
            description="When true, indicates this page break represents a custom thank-you page shown after form submission.",
        ),
    ] = None
    """
    When true, indicates this page break represents a custom thank-you page shown after form submission.
    """

    button: typing.Optional[Button] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
