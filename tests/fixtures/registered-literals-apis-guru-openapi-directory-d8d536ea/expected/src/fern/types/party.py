

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .attorney_representation_type import AttorneyRepresentationType
from .contact import Contact
from .party_attorney_associations import PartyAttorneyAssociations
from .party_party_classification_type import PartyPartyClassificationType
from .party_role import PartyRole
from .possible_norm_party import PossibleNormParty


class Party(UniversalBaseModel):
    attorney_representation_type: typing_extensions.Annotated[
        typing.Optional[AttorneyRepresentationType],
        FieldMetadata(alias="attorneyRepresentationType"),
        pydantic.Field(alias="attorneyRepresentationType"),
    ] = None
    contact: Contact
    first_fetch_date: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="firstFetchDate"),
        pydantic.Field(alias="firstFetchDate", description="When was the party first fetched from the court site."),
    ]
    """
    When was the party first fetched from the court site.
    """

    first_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="firstName"),
        pydantic.Field(alias="firstName", description="First name of the party. This is normalized by UniCourt."),
    ] = None
    """
    First name of the party. This is normalized by UniCourt.
    """

    is_visible: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="isVisible"),
        pydantic.Field(
            alias="isVisible",
            description="Signifies if the party as this party type is currently isVisible or not for the case.",
        ),
    ]
    """
    Signifies if the party as this party type is currently isVisible or not for the case.
    """

    last_fetch_date: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="lastFetchDate"),
        pydantic.Field(alias="lastFetchDate", description="When was the party last fetched from the court site."),
    ]
    """
    When was the party last fetched from the court site.
    """

    last_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="lastName"),
        pydantic.Field(alias="lastName", description="Last name of the party. This is normalized by UniCourt."),
    ] = None
    """
    Last name of the party. This is normalized by UniCourt.
    """

    middle_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="middleName"),
        pydantic.Field(alias="middleName", description="Middle name of the party. This is normalized by UniCourt."),
    ] = None
    """
    Middle name of the party. This is normalized by UniCourt.
    """

    name: str = pydantic.Field()
    """
    Name of the party as provided by Court.
    """

    name_prefix: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="namePrefix"), pydantic.Field(alias="namePrefix")
    ] = None
    name_suffix: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="nameSuffix"), pydantic.Field(alias="nameSuffix")
    ] = None
    object: str = pydantic.Field()
    """
    Name of the object
    """

    party_attorney_associations: typing_extensions.Annotated[
        typing.Optional[PartyAttorneyAssociations],
        FieldMetadata(alias="partyAttorneyAssociations"),
        pydantic.Field(alias="partyAttorneyAssociations"),
    ] = None
    party_classification_type: typing_extensions.Annotated[
        PartyPartyClassificationType,
        FieldMetadata(alias="partyClassificationType"),
        pydantic.Field(
            alias="partyClassificationType",
            description="To know the type of an entity in a case, if it is an Individual, Company or Other. An entity to a case could be the parties, attorneys or judges involved.",
        ),
    ]
    """
    To know the type of an entity in a case, if it is an Individual, Company or Other. An entity to a case could be the parties, attorneys or judges involved.
    """

    party_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="partyId"),
        pydantic.Field(
            alias="partyId",
            description="ID for the party in this case. This ID is unique within a case and NOT across cases. If the same party were to appear in another case this ID would be different.",
        ),
    ]
    """
    ID for the party in this case. This ID is unique within a case and NOT across cases. If the same party were to appear in another case this ID would be different.
    """

    party_role: typing_extensions.Annotated[
        typing.Optional[PartyRole], FieldMetadata(alias="partyRole"), pydantic.Field(alias="partyRole")
    ] = None
    possible_norm_party_array: typing_extensions.Annotated[
        typing.List[typing.Optional[PossibleNormParty]],
        FieldMetadata(alias="possibleNormPartyArray"),
        pydantic.Field(alias="possibleNormPartyArray"),
    ]
    source_party_role: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="sourcePartyRole"),
        pydantic.Field(alias="sourcePartyRole", description="Party Type as provided by Court."),
    ]
    """
    Party Type as provided by Court.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
