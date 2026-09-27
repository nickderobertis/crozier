

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .account_category import AccountCategory


class CategoriesItem(AccountCategory):
    detail_type_description: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="detailTypeDescription"),
        pydantic.Field(
            alias="detailTypeDescription",
            description="A description of the fully categorized (to detail type) account.",
        ),
    ] = None
    """
    A description of the fully categorized (to detail type) account.
    """

    detail_type_display_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="detailTypeDisplayName"),
        pydantic.Field(alias="detailTypeDisplayName", description="Human readable detailType display name."),
    ] = None
    """
    Human readable detailType display name.
    """

    subtype_display_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="subtypeDisplayName"),
        pydantic.Field(alias="subtypeDisplayName", description="Human readable subtype display name."),
    ] = None
    """
    Human readable subtype display name.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
