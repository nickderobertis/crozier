

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .role import Role


class DataSetAttributes(UniversalBaseModel):
    """
    Data Set Attributes.

    Data attributes that apply to all data in this set.
    """

    role: typing.Optional[Role] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
