

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .artifact_info import ArtifactInfo


class TaskResult(UniversalBaseModel):
    """
    任务关键文本结果（内联返回）。
    """

    task_id: str
    status: str
    final_latex: typing.Optional[str] = pydantic.Field(default=None)
    """
    最终可编译的 CPHOS LaTeX 文本。
    """

    report: typing.Optional[str] = pydantic.Field(default=None)
    """
    仲裁报告 Markdown 文本。
    """

    artifacts: typing.Optional[typing.List[ArtifactInfo]] = None
    latex_compile_status: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    最终文档编译状态：{ok, detail, template_dir}；未编译时为空。
    """

    figure_compile_status: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    各图片编译状态：{图标识: {ok, detail}}；未编译时为空。
    """

    final_pdf_available: typing.Optional[bool] = pydantic.Field(default=None)
    """
    是否已生成可下载 / 预览的最终 PDF（final_pdf 产物存在）。
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
