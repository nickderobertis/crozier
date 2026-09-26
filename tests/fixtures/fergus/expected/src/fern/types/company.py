

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .company_contact import CompanyContact
from .company_settings_item import CompanySettingsItem
from .company_tax import CompanyTax


class Company(UniversalBaseModel):
    guid: str
    prefix: str
    name: typing.Optional[str] = None
    date_created: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="dateCreated"), pydantic.Field(alias="dateCreated")
    ]
    active: bool
    has_terms_of_trade: typing_extensions.Annotated[
        bool, FieldMetadata(alias="hasTermsOfTrade"), pydantic.Field(alias="hasTermsOfTrade")
    ]
    has_logo: typing_extensions.Annotated[bool, FieldMetadata(alias="hasLogo"), pydantic.Field(alias="hasLogo")]
    contact: typing.Optional[CompanyContact] = None
    settings: typing.List[CompanySettingsItem]
    tax: typing.Optional[CompanyTax] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
