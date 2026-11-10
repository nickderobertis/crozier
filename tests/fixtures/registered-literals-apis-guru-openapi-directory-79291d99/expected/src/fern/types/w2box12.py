

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class W2Box12(UniversalBaseModel):
    """
    Data on the W2 Box 12
    """

    amount: typing.Optional[str] = pydantic.Field(default=None)
    """
    W2 Box 12 amount.
    """

    code: typing.Optional[str] = pydantic.Field(default=None)
    """
    W2 Box 12 code.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
