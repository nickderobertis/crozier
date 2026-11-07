

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .case_analytics_api import CaseAnalyticsApi
from .norm_organization import NormOrganization
from .norm_party_individual_data import NormPartyIndividualData
from .norm_party_party_classification_type import NormPartyPartyClassificationType
from .party_analytics_api import PartyAnalyticsApi
from .related_norm_party import RelatedNormParty


class NormParty(UniversalBaseModel):
    """
    Norm Party
    """

    case_analytics_api: typing_extensions.Annotated[
        CaseAnalyticsApi, FieldMetadata(alias="caseAnalyticsAPI"), pydantic.Field(alias="caseAnalyticsAPI")
    ]
    case_search_api: typing_extensions.Annotated[
        str, FieldMetadata(alias="caseSearchAPI"), pydantic.Field(alias="caseSearchAPI")
    ]
    individual_data: typing_extensions.Annotated[
        typing.Optional[NormPartyIndividualData],
        FieldMetadata(alias="individualData"),
        pydantic.Field(alias="individualData", description="* Only applicable if the Party is an Individual."),
    ] = None
    """
    * Only applicable if the Party is an Individual.
    """

    name: str
    norm_organization_data: typing_extensions.Annotated[
        NormOrganization, FieldMetadata(alias="normOrganizationData"), pydantic.Field(alias="normOrganizationData")
    ]
    norm_party_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="normPartyId"), pydantic.Field(alias="normPartyId")
    ]
    object: str
    party_analytics_api: typing_extensions.Annotated[
        PartyAnalyticsApi, FieldMetadata(alias="partyAnalyticsAPI"), pydantic.Field(alias="partyAnalyticsAPI")
    ]
    party_classification_type: typing_extensions.Annotated[
        NormPartyPartyClassificationType,
        FieldMetadata(alias="partyClassificationType"),
        pydantic.Field(alias="partyClassificationType"),
    ]
    related_norm_party_array: typing_extensions.Annotated[
        typing.List[RelatedNormParty],
        FieldMetadata(alias="relatedNormPartyArray"),
        pydantic.Field(alias="relatedNormPartyArray"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
