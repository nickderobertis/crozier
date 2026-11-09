

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .case_search_result import CaseSearchResult
from .pacer_party_search_content import PacerPartySearchContent


class PacerPartySearchResults(UniversalBaseModel):
    has_only_meta_info: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="hasOnlyMetaInfo"),
        pydantic.Field(
            alias="hasOnlyMetaInfo",
            description="This field determines if the UniCourt Content has only meta information. If the value is true and you require to get the latest updates of the case you will need to make a request to the updateCase API.",
        ),
    ]
    """
    This field determines if the UniCourt Content has only meta information. If the value is true and you require to get the latest updates of the case you will need to make a request to the updateCase API.
    """

    object: str = pydantic.Field()
    """
    Name of the object
    """

    pacer_content: typing_extensions.Annotated[
        PacerPartySearchContent, FieldMetadata(alias="pacerContent"), pydantic.Field(alias="pacerContent")
    ]
    uni_court_content: typing_extensions.Annotated[
        CaseSearchResult, FieldMetadata(alias="uniCourtContent"), pydantic.Field(alias="uniCourtContent")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
