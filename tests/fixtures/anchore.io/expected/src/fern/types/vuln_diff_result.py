

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class VulnDiffResult(UniversalBaseModel):
    """
    The results of the comparing two vulnerability records during an update
    """

    added: typing.Optional[typing.List[typing.Optional[typing.Any]]] = None
    removed: typing.Optional[typing.List[typing.Optional[typing.Any]]] = None
    updated: typing.Optional[typing.List[typing.Optional[typing.Any]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
