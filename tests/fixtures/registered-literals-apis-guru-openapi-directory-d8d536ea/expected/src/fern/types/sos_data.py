

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .associated_so_s_person import AssociatedSoSPerson
from .contact import Contact
from .sos_associated_norm_organization import SosAssociatedNormOrganization
from .sos_data_status import SosDataStatus
from .sos_name_change import SosNameChange


class SosData(UniversalBaseModel):
    associated_so_s_person_array: typing_extensions.Annotated[
        typing.List[AssociatedSoSPerson],
        FieldMetadata(alias="associatedSoSPersonArray"),
        pydantic.Field(alias="associatedSoSPersonArray"),
    ]
    contact: Contact
    domestic_registration: typing_extensions.Annotated[
        bool, FieldMetadata(alias="domesticRegistration"), pydantic.Field(alias="domesticRegistration")
    ]
    fein: typing.Optional[str] = None
    first_fetch_date: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="firstFetchDate"), pydantic.Field(alias="firstFetchDate")
    ]
    inactivation_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="inactivationDate"), pydantic.Field(alias="inactivationDate")
    ] = None
    is_active: typing_extensions.Annotated[bool, FieldMetadata(alias="isActive"), pydantic.Field(alias="isActive")]
    last_fetch_date: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="lastFetchDate"), pydantic.Field(alias="lastFetchDate")
    ]
    last_fetch_date_with_updates: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="lastFetchDateWithUpdates"),
        pydantic.Field(alias="lastFetchDateWithUpdates", description="Last Fetch Date of Organization with Updates."),
    ]
    """
    Last Fetch Date of Organization with Updates.
    """

    name_changes_array: typing_extensions.Annotated[
        typing.List[SosNameChange], FieldMetadata(alias="nameChangesArray"), pydantic.Field(alias="nameChangesArray")
    ]
    object: str
    registered_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="registeredDate"), pydantic.Field(alias="registeredDate")
    ] = None
    sos_associated_norm_organization_array: typing_extensions.Annotated[
        typing.List[SosAssociatedNormOrganization],
        FieldMetadata(alias="sosAssociatedNormOrganizationArray"),
        pydantic.Field(alias="sosAssociatedNormOrganizationArray"),
    ]
    sos_number: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="sosNumber"), pydantic.Field(alias="sosNumber")
    ] = None
    state_code: typing_extensions.Annotated[str, FieldMetadata(alias="stateCode"), pydantic.Field(alias="stateCode")]
    status: typing.Optional[SosDataStatus] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
