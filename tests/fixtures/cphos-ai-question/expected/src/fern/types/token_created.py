

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TokenCreated(UniversalBaseModel):
    """
    新签发 token 的响应（含一次性明文）。
    """

    id: str
    token: str = pydantic.Field()
    """
    token 明文，仅此一次返回，请立即安全保存并分发。
    """

    user_id: str
    role: str
    label: typing.Optional[str] = None
    created_at: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
