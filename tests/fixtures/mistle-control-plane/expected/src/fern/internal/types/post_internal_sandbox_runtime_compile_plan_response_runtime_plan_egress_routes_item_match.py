

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanEgressRoutesItemMatch(UniversalBaseModel):
    hosts: typing.List[str]
    path_prefixes: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="pathPrefixes"), pydantic.Field(alias="pathPrefixes")
    ] = None
    methods: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
