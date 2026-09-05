

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V1Alpha1WorkflowStage(UniversalBaseModel):
    type: typing.Optional[str] = None
    target: str
    name: str
    description: typing.Optional[str] = None
    version: typing.Optional[str] = None
    depends_on: typing.Optional[typing.List[str]] = None
    options: typing.Optional[typing.Dict[str, typing.Any]] = None
    resources: typing.Optional[typing.Dict[str, typing.Any]] = None
    priority: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
