

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TaskCompileResult(UniversalBaseModel):
    """
    按需编译的结果。
    """

    task_id: str
    latex_compile_status: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    最终文档编译状态：{ok, detail, template_dir}。
    """

    figure_compile_status: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    各图片编译状态：{图标识: {ok, detail}}。
    """

    final_pdf_available: typing.Optional[bool] = pydantic.Field(default=None)
    """
    编译后是否产出可下载 / 预览的最终 PDF。
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
