

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ErrorResponse(UniversalBaseModel):
    """
    统一错误响应体。

    所有显式抛出的业务错误（``HTTPException`` / :class:`api.errors.ApiError`）均以
    此结构返回，便于前端按 ``code`` 做稳定的分支处理；``detail`` 为面向人类的提示。
    请求体校验错误（FastAPI 422）保留框架默认的结构化 ``{detail: [...]}`` 形态。
    """

    code: str = pydantic.Field()
    """
    稳定的机器可读错误码（如 not_found / forbidden / task_not_terminal）。
    """

    detail: str = pydantic.Field()
    """
    面向人类的错误说明。
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
