

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .norm_corporate_group import NormCorporateGroup
from .norm_organization_organization_type import NormOrganizationOrganizationType
from .norm_organization_ticker_array_item import NormOrganizationTickerArrayItem
from .sos_data import SosData


class NormOrganization(UniversalBaseModel):
    cik: typing.Optional[str] = None
    is_involved_in_litigation: typing_extensions.Annotated[
        bool, FieldMetadata(alias="isInvolvedInLitigation"), pydantic.Field(alias="isInvolvedInLitigation")
    ]
    lei: typing.Optional[str] = None
    naics: typing.Optional[str] = None
    naics_description: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="naicsDescription"), pydantic.Field(alias="naicsDescription")
    ] = None
    name: str
    norm_corporate_group_array: typing_extensions.Annotated[
        typing.List[NormCorporateGroup],
        FieldMetadata(alias="normCorporateGroupArray"),
        pydantic.Field(alias="normCorporateGroupArray"),
    ]
    norm_organization_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="normOrganizationId"), pydantic.Field(alias="normOrganizationId")
    ]
    norm_party_api: typing_extensions.Annotated[
        str, FieldMetadata(alias="normPartyAPI"), pydantic.Field(alias="normPartyAPI")
    ]
    object: str
    organization_type: typing_extensions.Annotated[
        NormOrganizationOrganizationType,
        FieldMetadata(alias="organizationType"),
        pydantic.Field(alias="organizationType"),
    ]
    sic: typing.Optional[str] = None
    sic_description: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="sicDescription"), pydantic.Field(alias="sicDescription")
    ] = None
    sos_data_array: typing_extensions.Annotated[
        typing.List[SosData], FieldMetadata(alias="sosDataArray"), pydantic.Field(alias="sosDataArray")
    ]
    ticker_array: typing_extensions.Annotated[
        typing.List[NormOrganizationTickerArrayItem],
        FieldMetadata(alias="tickerArray"),
        pydantic.Field(alias="tickerArray"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
