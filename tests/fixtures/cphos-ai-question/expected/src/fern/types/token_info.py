

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TokenInfo(UniversalBaseModel):
    """
    token 元数据（不含明文 / 哈希）。
    """

    id: str
    user_id: str
    role: str
    label: typing.Optional[str] = None
    created_at: str
    revoked_at: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
