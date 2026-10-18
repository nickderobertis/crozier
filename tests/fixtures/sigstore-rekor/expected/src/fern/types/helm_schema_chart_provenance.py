

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .helm_schema_chart_provenance_signature import HelmSchemaChartProvenanceSignature


class HelmSchemaChartProvenance(UniversalBaseModel):
    """
    The provenance entry associated with the signed Helm Chart
    """

    signature: typing.Optional[HelmSchemaChartProvenanceSignature] = pydantic.Field(default=None)
    """
    Information about the included signature in the provenance file
    """

    content: typing.Optional[str] = pydantic.Field(default=None)
    """
    Specifies the content of the provenance file inline within the document
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
