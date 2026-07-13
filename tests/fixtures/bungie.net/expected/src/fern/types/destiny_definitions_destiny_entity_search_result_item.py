

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_common_destiny_display_properties_definition import (
    DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition,
)


class DestinyDefinitionsDestinyEntitySearchResultItem(UniversalBaseModel):
    """
    An individual Destiny Entity returned from the entity search.
    """

    display_properties: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition],
        FieldMetadata(alias="displayProperties"),
    ] = pydantic.Field(default=None)
    """
    Basic display properties on the entity, so you don't have to look up the definition to show basic results for the item.
    """

    entity_type: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="entityType")] = pydantic.Field(
        default=None
    )
    """
    The type of entity, returned as a string matching the DestinyDefinition's contract class name. You'll have to have your own mapping from class names to actually looking up those definitions in the manifest databases.
    """

    hash: typing.Optional[int] = pydantic.Field(default=None)
    """
    The hash identifier of the entity. You will use this to look up the DestinyDefinition relevant for the entity found.
    """

    weight: typing.Optional[float] = pydantic.Field(default=None)
    """
    The ranking value for sorting that we calculated using our relevance formula. This will hopefully get better with time and iteration.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
