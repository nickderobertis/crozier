

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1alpha1config_resource_spec import V1Alpha1ConfigResourceSpec
from .v1alpha1resource_metadata import V1Alpha1ResourceMetadata


class V1Alpha1ConfigResourceReadResponse(UniversalBaseModel):
    kind: typing.Optional[str] = None
    metadata: V1Alpha1ResourceMetadata
    spec: V1Alpha1ConfigResourceSpec

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
