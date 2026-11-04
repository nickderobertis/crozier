

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GroupKind(UniversalBaseModel):
    """
    GroupKind contains group and kind data only.
    """

    group: typing.Optional[str] = pydantic.Field(default=None)
    """
    is group name of Extension.
    """

    kind: typing.Optional[str] = pydantic.Field(default=None)
    """
    is kind name of Extension.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
