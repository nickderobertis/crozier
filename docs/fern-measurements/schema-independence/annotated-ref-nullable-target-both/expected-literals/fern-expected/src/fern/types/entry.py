

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .remark import Remark


class Entry(UniversalBaseModel):
    id: typing.Optional[str] = None
    memo: str = pydantic.Field()
    """
    The wording.
    """

    note: typing.Optional[Remark] = None
    remark: typing.Optional[str] = pydantic.Field(default=None)
    """
    A remark kept beside the entry.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
