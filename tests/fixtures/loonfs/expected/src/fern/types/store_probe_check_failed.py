

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class StoreProbeCheckFailed(UniversalBaseModel):
    """
    The store violated the contract or the operation failed.
    """

    message: str = pydantic.Field()
    """
    The expected and actual behavior for a failed check.
    """

    name: str = pydantic.Field()
    """
    The check's stable name.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
