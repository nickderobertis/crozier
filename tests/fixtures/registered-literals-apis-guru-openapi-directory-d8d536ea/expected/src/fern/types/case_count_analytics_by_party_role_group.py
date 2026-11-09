

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .party_role_group import PartyRoleGroup


class CaseCountAnalyticsByPartyRoleGroup(UniversalBaseModel):
    case_count: typing_extensions.Annotated[int, FieldMetadata(alias="caseCount"), pydantic.Field(alias="caseCount")]
    case_search_api: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="caseSearchAPI"),
        pydantic.Field(
            alias="caseSearchAPI", description="Link to cases for the entity involving the search criteria. TBD."
        ),
    ]
    """
    Link to cases for the entity involving the search criteria. TBD.
    """

    object: str
    party_role_group: typing_extensions.Annotated[
        PartyRoleGroup, FieldMetadata(alias="partyRoleGroup"), pydantic.Field(alias="partyRoleGroup")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
