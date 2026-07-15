

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ConfigSnmPv3(UniversalBaseModel):
    context_engine_id: typing.Optional[str] = None
    engine_id: typing.Optional[str] = None
    usm_db: typing.Optional[str] = None
    vacm_db: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
