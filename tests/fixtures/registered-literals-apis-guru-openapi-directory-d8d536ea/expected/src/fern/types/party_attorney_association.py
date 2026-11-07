

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PartyAttorneyAssociation(UniversalBaseModel):
    attorney_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="attorneyId"),
        pydantic.Field(
            alias="attorneyId",
            description="ID for the attorney in this case. This ID is unique within a case and NOT across cases. If the same attorney were to appear in another case this ID would be different.",
        ),
    ]
    """
    ID for the attorney in this case. This ID is unique within a case and NOT across cases. If the same attorney were to appear in another case this ID would be different.
    """

    is_visible: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="isVisible"),
        pydantic.Field(
            alias="isVisible",
            description="Signifies if this party attorney relationship is currently isVisible or not for the case.",
        ),
    ]
    """
    Signifies if this party attorney relationship is currently isVisible or not for the case.
    """

    object: str = pydantic.Field()
    """
    Name of the object
    """

    party_attorney_association_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="partyAttorneyAssociationId"),
        pydantic.Field(alias="partyAttorneyAssociationId", description="ID of the association"),
    ]
    """
    ID of the association
    """

    party_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="partyId"),
        pydantic.Field(
            alias="partyId",
            description="ID for the party in this case. This ID is unique within a case and NOT across cases. If the same attorney were to appear in another case this ID would be different.",
        ),
    ]
    """
    ID for the party in this case. This ID is unique within a case and NOT across cases. If the same attorney were to appear in another case this ID would be different.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
