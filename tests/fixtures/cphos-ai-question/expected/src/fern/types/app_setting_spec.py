

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AppSettingSpec(UniversalBaseModel):
    """
    单个运行期应用设置项的元信息（供管理端表单渲染）。
    """

    key: str = pydantic.Field()
    """
    设置项键名。
    """

    type: str = pydantic.Field()
    """
    值类型：int / float / bool / str。
    """

    min: typing.Optional[float] = pydantic.Field(default=None)
    """
    允许的最小值（含）。
    """

    exclusive_min: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="exclusiveMin"),
        pydantic.Field(alias="exclusiveMin", description="允许的最小值（不含）。"),
    ] = None
    """
    允许的最小值（不含）。
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
