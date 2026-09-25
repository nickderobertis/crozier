

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BagFlavourFullData(UniversalBaseModel):
    backend: str
    config: typing.Dict[str, typing.Any]
    default_quota: typing.Optional[int] = None
    description: str
    display_name: str
    is_from_deployment: typing.Optional[bool] = None
    name: str
    order: typing.Optional[int] = None
    project_specific: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
