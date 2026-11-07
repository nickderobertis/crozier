

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .attorney_law_firm import AttorneyLawFirm
from .attorney_type import AttorneyType
from .contact import Contact
from .party_attorney_associations import PartyAttorneyAssociations
from .possible_norm_attorney import PossibleNormAttorney
from .possible_norm_law_firm import PossibleNormLawFirm


class Attorney(UniversalBaseModel):
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

    attorney_law_firm_array: typing_extensions.Annotated[
        typing.List[typing.Optional[AttorneyLawFirm]],
        FieldMetadata(alias="attorneyLawFirmArray"),
        pydantic.Field(alias="attorneyLawFirmArray"),
    ]
    attorney_type: typing_extensions.Annotated[
        typing.Optional[AttorneyType], FieldMetadata(alias="attorneyType"), pydantic.Field(alias="attorneyType")
    ] = None
    bar_number: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="barNumber"),
        pydantic.Field(alias="barNumber", description="The bar enrollment number of an attorney."),
    ] = None
    """
    The bar enrollment number of an attorney.
    """

    contact: Contact
    first_fetch_date: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="firstFetchDate"),
        pydantic.Field(alias="firstFetchDate", description="When was the attorney first fetched from the court site."),
    ]
    """
    When was the attorney first fetched from the court site.
    """

    first_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="firstName"),
        pydantic.Field(alias="firstName", description="First name of the attorney. This is normalized by UniCourt."),
    ] = None
    """
    First name of the attorney. This is normalized by UniCourt.
    """

    is_visible: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="isVisible"),
        pydantic.Field(
            alias="isVisible",
            description="Signifies if the attorney as this attorney type is currently isVisible or not for the case.",
        ),
    ]
    """
    Signifies if the attorney as this attorney type is currently isVisible or not for the case.
    """

    last_fetch_date: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="lastFetchDate"),
        pydantic.Field(alias="lastFetchDate", description="When was the attorney last fetched from the court site."),
    ]
    """
    When was the attorney last fetched from the court site.
    """

    last_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="lastName"),
        pydantic.Field(alias="lastName", description="Last name of the attorney. This is normalized by UniCourt."),
    ] = None
    """
    Last name of the attorney. This is normalized by UniCourt.
    """

    middle_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="middleName"),
        pydantic.Field(alias="middleName", description="Middle name of the attorney. This is normalized by UniCourt."),
    ] = None
    """
    Middle name of the attorney. This is normalized by UniCourt.
    """

    name: str = pydantic.Field()
    """
    Name of the attorney as provided by Court.
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
    party_role_group_id_array: typing_extensions.Annotated[
        typing.List[str],
        FieldMetadata(alias="partyRoleGroupIdArray"),
        pydantic.Field(alias="partyRoleGroupIdArray", description="Party Role Group Id for a Attorney."),
    ]
    """
    Party Role Group Id for a Attorney.
    """

    party_role_id_array: typing_extensions.Annotated[
        typing.List[str],
        FieldMetadata(alias="partyRoleIdArray"),
        pydantic.Field(alias="partyRoleIdArray", description="Party Role Id for a Attorney."),
    ]
    """
    Party Role Id for a Attorney.
    """

    possible_norm_attorney_array: typing_extensions.Annotated[
        typing.List[typing.Optional[PossibleNormAttorney]],
        FieldMetadata(alias="possibleNormAttorneyArray"),
        pydantic.Field(alias="possibleNormAttorneyArray"),
    ]
    possible_norm_law_firm_array: typing_extensions.Annotated[
        typing.List[typing.Optional[PossibleNormLawFirm]],
        FieldMetadata(alias="possibleNormLawFirmArray"),
        pydantic.Field(alias="possibleNormLawFirmArray", description="Possible Norm Lawfirm array for a Attorney."),
    ]
    """
    Possible Norm Lawfirm array for a Attorney.
    """

    source_attorney_type: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="sourceAttorneyType"),
        pydantic.Field(alias="sourceAttorneyType", description="Attorney Type as provided by Court."),
    ]
    """
    Attorney Type as provided by Court.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
