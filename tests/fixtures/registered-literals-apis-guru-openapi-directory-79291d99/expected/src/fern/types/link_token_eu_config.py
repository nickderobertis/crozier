

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LinkTokenEuConfig(UniversalBaseModel):
    """
    Configuration parameters for EU flows
    """

    headless: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If `true`, open Link without an initial UI. Defaults to `false`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
