

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SharingConfig(UniversalBaseModel):
    """
    Configuration for sharing features.

        **Keys.**

        - `html`: if `False`, HTML sharing options will be hidden from the UI
        - `wasm`: if `False`, WebAssembly sharing options will be hidden from the UI
        - `molab`: if `False`, molab sharing options will be hidden from the UI
    """

    html: typing.Optional[bool] = None
    molab: typing.Optional[bool] = None
    wasm: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
