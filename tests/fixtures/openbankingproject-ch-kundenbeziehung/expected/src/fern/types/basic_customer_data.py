

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .basic_customer_data_gender import BasicCustomerDataGender
from .basic_customer_data_marital_status import BasicCustomerDataMaritalStatus


class BasicCustomerData(UniversalBaseModel):
    last_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="lastName"), pydantic.Field(alias="lastName", description="Nachname")
    ]
    """
    Nachname
    """

    given_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="givenName"), pydantic.Field(alias="givenName", description="Vorname(n)")
    ]
    """
    Vorname(n)
    """

    middle_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="middleName"),
        pydantic.Field(alias="middleName", description="Weitere Vornamen"),
    ] = None
    """
    Weitere Vornamen
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    Titel
    """

    birth_date: typing_extensions.Annotated[
        dt.date, FieldMetadata(alias="birthDate"), pydantic.Field(alias="birthDate", description="Geburtsdatum")
    ]
    """
    Geburtsdatum
    """

    birth_place: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="birthPlace"),
        pydantic.Field(alias="birthPlace", description="Geburtsort"),
    ] = None
    """
    Geburtsort
    """

    nationality: typing.List[str] = pydantic.Field()
    """
    Nationalität(en) (ISO 3166-1)
    """

    gender: typing.Optional[BasicCustomerDataGender] = None
    marital_status: typing_extensions.Annotated[
        typing.Optional[BasicCustomerDataMaritalStatus],
        FieldMetadata(alias="maritalStatus"),
        pydantic.Field(alias="maritalStatus"),
    ] = None
    language: typing.Optional[str] = pydantic.Field(default=None)
    """
    Bevorzugte Sprache (ISO 639-1)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
