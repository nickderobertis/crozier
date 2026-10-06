

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AppSettingsInfo(UniversalBaseModel):
    """
    运行期应用设置当前值。
    """

    max_retry_count: typing.Optional[int] = None
    source_material_max_chars: typing.Optional[int] = None
    auto_compile_figures: typing.Optional[bool] = None
    auto_compile_latex: typing.Optional[bool] = None
    latex_compile_timeout: typing.Optional[int] = None
    latex_compiler_backend: typing.Optional[str] = None
    latex_service_base_url: typing.Optional[str] = None
    latex_service_api_key_set: typing.Optional[bool] = None
    latex_service_api_key_masked: typing.Optional[str] = None
    latex_service_poll_interval: typing.Optional[float] = None
    latex_service_max_wait: typing.Optional[float] = None
    sse_poll_interval: typing.Optional[float] = None
    sse_max_duration: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
