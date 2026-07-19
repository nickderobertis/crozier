

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class HelmSchemaChartProvenanceSignature(UniversalBaseModel):
    """
    Information about the included signature in the provenance file
    """

    content: typing.Optional[str] = pydantic.Field(default=None)
    """
    Specifies the signature embedded within the provenance file 
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
