

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class VersionInfo(UniversalBaseModel):
    """
    服务版本与许可证信息。
    """

    name: str = pydantic.Field()
    """
    应用包名。
    """

    version: str = pydantic.Field()
    """
    语义化版本号。
    """

    license: str = pydantic.Field()
    """
    SPDX 许可证标识。
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
