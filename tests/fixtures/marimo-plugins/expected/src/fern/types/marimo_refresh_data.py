

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .marimo_refresh_data_default_interval import MarimoRefreshDataDefaultInterval
from .marimo_refresh_data_options_item import MarimoRefreshDataOptionsItem


class MarimoRefreshData(UniversalBaseModel):
    options: typing.Optional[typing.List[MarimoRefreshDataOptionsItem]] = None
    default_interval: typing_extensions.Annotated[
        typing.Optional[MarimoRefreshDataDefaultInterval],
        FieldMetadata(alias="defaultInterval"),
        pydantic.Field(alias="defaultInterval"),
    ] = None
    label: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
