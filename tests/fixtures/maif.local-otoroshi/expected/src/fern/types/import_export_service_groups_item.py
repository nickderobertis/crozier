

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ImportExportServiceGroupsItem(UniversalBaseModel):
    """
    An Otoroshi service group is just a group of service descriptor. It is useful to be able to define Api Keys for the whole group
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The descriptoin of the group
    """

    id: str = pydantic.Field()
    """
    The unique id of the group. Usually 64 random alpha numerical characters, but can be anything
    """

    name: str = pydantic.Field()
    """
    The name of the group
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
