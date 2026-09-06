

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListComponentsResponseComponentsItem(UniversalBaseModel):
    """
    The Component object
    """

    id: str = pydantic.Field()
    """
    Unique identifier for the Component
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Component Name
    """

    group: typing.Optional[str] = pydantic.Field(default=None)
    """
    The group that the component belongs to
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Component Description
    """

    readonly: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether the component is read-only. Components that cannot be updated within this Site are set to readonly. Workspace Libraries are a good example.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
