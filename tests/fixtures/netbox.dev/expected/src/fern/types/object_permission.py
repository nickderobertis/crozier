

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nested_group import NestedGroup
from .nested_user import NestedUser


class ObjectPermission(UniversalBaseModel):
    actions: typing.List[str] = pydantic.Field()
    """
    The list of actions granted by this permission
    """

    constraints: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    Queryset filter matching the applicable objects of the selected type(s)
    """

    description: typing.Optional[str] = None
    display: typing.Optional[str] = None
    enabled: typing.Optional[bool] = None
    groups: typing.Optional[typing.List[NestedGroup]] = None
    id: typing.Optional[int] = None
    name: str
    object_types: typing.List[str]
    url: typing.Optional[str] = None
    users: typing.Optional[typing.List[NestedUser]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
