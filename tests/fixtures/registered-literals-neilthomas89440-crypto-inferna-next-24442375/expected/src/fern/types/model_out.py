

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ModelOut(UniversalBaseModel):
    id: str
    name: str
    display_name: str
    category: str
    description: typing.Optional[str] = None
    params_b: typing.Optional[float] = None
    vram_required_mb: int
    requires_hf_token: bool
    license: typing.Optional[str] = None
    is_builtin: bool
    supported_engines: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
