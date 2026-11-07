

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .run_engine import RunEngine


class FileDownloadBlockYaml(UniversalBaseModel):
    label: str
    continue_on_failure: typing.Optional[bool] = None
    model: typing.Optional[typing.Dict[str, typing.Any]] = None
    navigation_goal: str
    url: typing.Optional[str] = None
    title: typing.Optional[str] = None
    engine: typing.Optional[RunEngine] = None
    error_code_mapping: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None
    max_retries: typing.Optional[int] = None
    max_steps_per_run: typing.Optional[int] = None
    parameter_keys: typing.Optional[typing.List[str]] = None
    download_suffix: typing.Optional[str] = None
    totp_verification_url: typing.Optional[str] = None
    totp_identifier: typing.Optional[str] = None
    cache_actions: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
