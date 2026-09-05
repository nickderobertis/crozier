

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .code_bundle_location import CodeBundleLocation
from .code_bundle_runtime_context import CodeBundleRuntimeContext


class CodeBundle(UniversalBaseModel):
    runtime_context: CodeBundleRuntimeContext
    location: CodeBundleLocation
    bundle_id: typing.Optional[str] = None
    preview: typing.Optional[str] = pydantic.Field(default=None)
    """
    A preview of the code
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
