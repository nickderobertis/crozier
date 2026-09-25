

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TargetConversionParameters(UniversalBaseModel):
    """
    Specify target settings (add_raw_pages, add_annotations).

    Fields left null are set to platform defaults.
    """

    add_raw_pages: typing.Optional[bool] = None
    add_annotations: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
