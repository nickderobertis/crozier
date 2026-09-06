

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GlobalResourcesSharedModelsTranslationSetStatistics(UniversalBaseModel):
    """
    Statistics for a translation set
    """

    language_i_ds: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="LanguageIDs"),
        pydantic.Field(
            alias="LanguageIDs",
            description="The IDs of languages for which translaions in this translation set have been requested",
        ),
    ] = None
    """
    The IDs of languages for which translaions in this translation set have been requested
    """

    string_count: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="StringCount"),
        pydantic.Field(
            alias="StringCount", description="The count of unique string definitions contained in this translation set"
        ),
    ] = None
    """
    The count of unique string definitions contained in this translation set
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
