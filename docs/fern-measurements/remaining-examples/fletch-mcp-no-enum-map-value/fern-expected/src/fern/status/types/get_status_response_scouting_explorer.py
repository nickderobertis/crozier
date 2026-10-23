

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_status_response_scouting_explorer_provider import GetStatusResponseScoutingExplorerProvider


class GetStatusResponseScoutingExplorer(UniversalBaseModel):
    searches_completed: typing_extensions.Annotated[
        int, FieldMetadata(alias="searchesCompleted"), pydantic.Field(alias="searchesCompleted")
    ]
    searches_due: typing_extensions.Annotated[
        int, FieldMetadata(alias="searchesDue"), pydantic.Field(alias="searchesDue")
    ]
    candidate_contracts: typing_extensions.Annotated[
        int, FieldMetadata(alias="candidateContracts"), pydantic.Field(alias="candidateContracts")
    ]
    pending_contract_checks: typing_extensions.Annotated[
        int, FieldMetadata(alias="pendingContractChecks"), pydantic.Field(alias="pendingContractChecks")
    ]
    last_search_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="lastSearchAt"), pydantic.Field(alias="lastSearchAt")
    ] = None
    provider: typing.Optional[GetStatusResponseScoutingExplorerProvider] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
