

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Creator(UniversalBaseModel):
    """
    Who created ``dataset`` — the verified catalog principal at create time (or ``None``).
    """

    creator: typing.Optional[str] = None
    dataset: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
