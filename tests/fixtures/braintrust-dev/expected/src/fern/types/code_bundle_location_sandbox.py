

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .code_bundle_location_sandbox_sandbox_spec import CodeBundleLocationSandboxSandboxSpec


class CodeBundleLocationSandbox(UniversalBaseModel):
    sandbox_spec: CodeBundleLocationSandboxSandboxSpec
    entrypoints: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Which entrypoints to execute in the sandbox
    """

    eval_name: str
    parameters: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Parameter values for sandbox eval execution
    """

    evaluator_definition: typing.Optional[typing.Any] = pydantic.Field(default=None)
    """
    Definition of current evaluator with parameters
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
