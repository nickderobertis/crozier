

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SandboxConfig(UniversalBaseModel):
    enabled: bool = pydantic.Field()
    """
    Give the agent a sandbox. Required for skills and Code Mode.
    """

    file_downloads: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Allow downloading agent-produced files via the turn download endpoint. Default: true.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
