

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_chains_chain_id_status_response_jobs_item import GetChainsChainIdStatusResponseJobsItem
from .get_chains_chain_id_status_response_scouting import GetChainsChainIdStatusResponseScouting
from .get_chains_chain_id_status_response_swap_indexer import GetChainsChainIdStatusResponseSwapIndexer
from .get_chains_chain_id_status_response_verdict import GetChainsChainIdStatusResponseVerdict


class GetChainsChainIdStatusResponse(UniversalBaseModel):
    verdict: typing.Optional[GetChainsChainIdStatusResponseVerdict] = None
    summary: typing.Optional[str] = None
    daemon: typing.Optional[typing.Dict[str, typing.Any]] = None
    head: typing.Optional[typing.Dict[str, typing.Any]] = None
    swap_indexer: typing_extensions.Annotated[
        typing.Optional[GetChainsChainIdStatusResponseSwapIndexer],
        FieldMetadata(alias="swapIndexer"),
        pydantic.Field(
            alias="swapIndexer",
            description="Live swap tail and separate backwards backfill. Coverage is measured independently of daemon health. USDG uses a disclosed nominal dollar assumption; supported WETH windows use explicitly estimated historical oracle samples. Inspect valuation methods and valued-pool coverage.",
        ),
    ] = None
    """
    Live swap tail and separate backwards backfill. Coverage is measured independently of daemon health. USDG uses a disclosed nominal dollar assumption; supported WETH windows use explicitly estimated historical oracle samples. Inspect valuation methods and valued-pool coverage.
    """

    scouting: typing.Optional[GetChainsChainIdStatusResponseScouting] = pydantic.Field(default=None)
    """
    Catalog ticker candidates, bytecode evidence and unfinished pool coverage. A ticker match does not establish Robinhood app contract identity.
    """

    jobs: typing.Optional[typing.List[GetChainsChainIdStatusResponseJobsItem]] = None
    figures: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
