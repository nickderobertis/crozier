

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GlobalResourcesSharedModelsLanguage(UniversalBaseModel):
    """
    A language used for string translations.
    """

    description: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Description"),
        pydantic.Field(
            alias="Description", description="The description of the language (e.g. “English – United States”)."
        ),
    ]
    """
    The description of the language (e.g. “English – United States”).
    """

    is_deleted: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="IsDeleted"),
        pydantic.Field(
            alias="IsDeleted",
            description="Indicates whether the API supports the language. Must be false when created. Read Only.",
        ),
    ] = None
    """
    Indicates whether the API supports the language. Must be false when created. Read Only.
    """

    locale_id: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="LocaleId"),
        pydantic.Field(alias="LocaleId", description="The Locale Id of the language."),
    ]
    """
    The Locale Id of the language.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
