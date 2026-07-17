

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_common_destiny_display_properties_definition import (
    DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition,
)
from .destiny_definitions_seasons_destiny_event_card_images import DestinyDefinitionsSeasonsDestinyEventCardImages
from .destiny_misc_destiny_color import DestinyMiscDestinyColor


class DestinyDefinitionsSeasonsDestinyEventCardDefinition(UniversalBaseModel):
    """
    Defines the properties of an 'Event Card' in Destiny 2, to coincide with a seasonal event for additional challenges, premium rewards, a new seal, and a special title. For example: Solstice of Heroes 2022.
    """

    color: typing.Optional[DestinyMiscDestinyColor] = None
    display_properties: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition],
        FieldMetadata(alias="displayProperties"),
        pydantic.Field(alias="displayProperties"),
    ] = None
    end_time: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="endTime"), pydantic.Field(alias="endTime")
    ] = None
    hash: typing.Optional[int] = pydantic.Field(default=None)
    """
    The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
    When entities refer to each other in Destiny content, it is this hash that they are referring to.
    """

    images: typing.Optional[DestinyDefinitionsSeasonsDestinyEventCardImages] = None
    index: typing.Optional[int] = pydantic.Field(default=None)
    """
    The index of the entity as it was found in the investment tables.
    """

    link_redirect_path: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="linkRedirectPath"), pydantic.Field(alias="linkRedirectPath")
    ] = None
    redacted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    seal_presentation_node_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="sealPresentationNodeHash"),
        pydantic.Field(alias="sealPresentationNodeHash"),
    ] = None
    ticket_currency_item_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="ticketCurrencyItemHash"),
        pydantic.Field(alias="ticketCurrencyItemHash"),
    ] = None
    ticket_vendor_category_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="ticketVendorCategoryHash"),
        pydantic.Field(alias="ticketVendorCategoryHash"),
    ] = None
    ticket_vendor_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="ticketVendorHash"), pydantic.Field(alias="ticketVendorHash")
    ] = None
    triumphs_presentation_node_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="triumphsPresentationNodeHash"),
        pydantic.Field(alias="triumphsPresentationNodeHash"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
