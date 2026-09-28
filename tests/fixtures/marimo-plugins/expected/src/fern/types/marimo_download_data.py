

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MarimoDownloadData(UniversalBaseModel):
    data: str
    disabled: typing.Optional[bool] = None
    filename: typing.Optional[str] = None
    label: typing.Optional[str] = None
    lazy: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
