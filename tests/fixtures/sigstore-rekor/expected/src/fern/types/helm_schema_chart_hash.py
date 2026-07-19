

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .helm_schema_chart_hash_algorithm import HelmSchemaChartHashAlgorithm


class HelmSchemaChartHash(UniversalBaseModel):
    """
    Specifies the hash algorithm and value for the chart
    """

    algorithm: HelmSchemaChartHashAlgorithm = pydantic.Field()
    """
    The hashing function used to compute the hash value
    """

    value: str = pydantic.Field()
    """
    The hash value for the chart
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
