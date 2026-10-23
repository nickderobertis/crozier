

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_chains_chain_id_status_response_jobs_item_metadata_backlog import (
    GetChainsChainIdStatusResponseJobsItemMetadataBacklog,
)
from .get_chains_chain_id_status_response_jobs_item_metric_coverage_value import (
    GetChainsChainIdStatusResponseJobsItemMetricCoverageValue,
)
from .get_chains_chain_id_status_response_jobs_item_verdict import GetChainsChainIdStatusResponseJobsItemVerdict


class GetChainsChainIdStatusResponseJobsItem(UniversalBaseModel):
    job: str
    cadence_seconds: typing_extensions.Annotated[
        float, FieldMetadata(alias="cadenceSeconds"), pydantic.Field(alias="cadenceSeconds")
    ]
    verdict: GetChainsChainIdStatusResponseJobsItemVerdict
    metadata_backlog: typing_extensions.Annotated[
        typing.Optional[GetChainsChainIdStatusResponseJobsItemMetadataBacklog],
        FieldMetadata(alias="metadataBacklog"),
        pydantic.Field(
            alias="metadataBacklog",
            description="Metadata queue measured after this job's last successful batch. Null means no batch has reported coverage yet; a fresh batch does not imply complete token coverage.",
        ),
    ] = None
    """
    Metadata queue measured after this job's last successful batch. Null means no batch has reported coverage yet; a fresh batch does not imply complete token coverage.
    """

    metric_coverage: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Optional[GetChainsChainIdStatusResponseJobsItemMetricCoverageValue]]],
        FieldMetadata(alias="metricCoverage"),
        pydantic.Field(
            alias="metricCoverage",
            description="Per-metric catalog coverage measured by the job, independent from scheduler health. Current and failed may overlap when a failed refresh retains a current observation. Age these counts from measuredAt; a fresh scheduler does not make older counts current.",
        ),
    ] = None
    """
    Per-metric catalog coverage measured by the job, independent from scheduler health. Current and failed may overlap when a failed refresh retains a current observation. Age these counts from measuredAt; a fresh scheduler does not make older counts current.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
