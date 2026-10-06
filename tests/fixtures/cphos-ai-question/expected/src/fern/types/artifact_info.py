

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ArtifactInfo(UniversalBaseModel):
    """
    单个产物文件的元数据。
    """

    name: str = pydantic.Field()
    """
    产物逻辑名（如 final_latex / draft / log / report）。
    """

    filename: str = pydantic.Field()
    """
    磁盘文件名。
    """

    size: int = pydantic.Field()
    """
    文件字节数。
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
