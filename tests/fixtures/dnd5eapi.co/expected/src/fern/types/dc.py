

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .api_reference import ApiReference


class Dc(UniversalBaseModel):
    """
    `DC`
    """

    dc_type: typing.Optional[ApiReference] = None
    dc_value: typing.Optional[float] = pydantic.Field(default=None)
    """
    Value to beat
    """

    success_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Result of a successful save. Can be \\"none\\", \\"half\\", or \\"other\\"
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
