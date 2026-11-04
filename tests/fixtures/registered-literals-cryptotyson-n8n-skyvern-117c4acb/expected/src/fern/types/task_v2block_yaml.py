

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TaskV2BlockYaml(UniversalBaseModel):
    label: str
    continue_on_failure: typing.Optional[bool] = None
    model: typing.Optional[typing.Dict[str, typing.Any]] = None
    prompt: str
    url: typing.Optional[str] = None
    totp_verification_url: typing.Optional[str] = None
    totp_identifier: typing.Optional[str] = None
    max_iterations: typing.Optional[int] = None
    max_steps: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
