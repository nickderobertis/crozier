

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .me_response_role import MeResponseRole


class MeResponse(UniversalBaseModel):
    """
    当前调用者的身份与角色（任意有效 token 均可访问）。
    """

    user_id: str = pydantic.Field()
    """
    当前 token 所属用户 ID。
    """

    role: MeResponseRole = pydantic.Field()
    """
    当前 token 角色。
    """

    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    用户备注名。
    """

    token_id: str = pydantic.Field()
    """
    当前会话所用 token 的 ID。
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
