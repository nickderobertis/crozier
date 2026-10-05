

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DesiredNamespace(UniversalBaseModel):
    """
    A namespace that should exist or be deleted on a cluster.
    """

    delete: typing.Optional[bool] = pydantic.Field(default=None)
    """
    True = namespace should be removed
    """

    name: str = pydantic.Field()
    """
    Namespace name
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
