

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .fdx_party_registry import FdxPartyRegistry
from .fdx_party_type import FdxPartyType


class FdxParty(UniversalBaseModel):
    """
    FDX Participant - an entity or person that is a part of a FDX API transaction
    """

    home_uri: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="homeUri"),
        pydantic.Field(
            alias="homeUri",
            description="URI for party, where an end user could learn more about the company or application involved in the data sharing chain",
        ),
    ] = None
    """
    URI for party, where an end user could learn more about the company or application involved in the data sharing chain
    """

    logo_uri: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="logoUri"),
        pydantic.Field(alias="logoUri", description="URI for a logo asset to be displayed to the end user"),
    ] = None
    """
    URI for a logo asset to be displayed to the end user
    """

    name: str = pydantic.Field()
    """
    Human recognizable common name
    """

    registered_entity_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="registeredEntityId"),
        pydantic.Field(alias="registeredEntityId", description="Registered id of party"),
    ] = None
    """
    Registered id of party
    """

    registered_entity_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="registeredEntityName"),
        pydantic.Field(alias="registeredEntityName", description="Registered name of party"),
    ] = None
    """
    Registered name of party
    """

    registry: typing.Optional[FdxPartyRegistry] = None
    type: FdxPartyType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
