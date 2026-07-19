

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .helm_schema_chart_hash import HelmSchemaChartHash
from .helm_schema_chart_provenance import HelmSchemaChartProvenance


class HelmSchemaChart(UniversalBaseModel):
    """
    Information about the Helm chart associated with the entry
    """

    hash: typing.Optional[HelmSchemaChartHash] = pydantic.Field(default=None)
    """
    Specifies the hash algorithm and value for the chart
    """

    provenance: HelmSchemaChartProvenance = pydantic.Field()
    """
    The provenance entry associated with the signed Helm Chart
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
