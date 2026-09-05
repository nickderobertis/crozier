

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1alpha2config_selector import V1Alpha2ConfigSelector


class V1Alpha2ConfigResourceSpec(UniversalBaseModel):
    selector: typing.Optional[V1Alpha2ConfigSelector] = None
    data: typing.Dict[str, typing.Any]
    new: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
