

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .acl_object_type import AclObjectType


class CreateFunctionOrigin(UniversalBaseModel):
    object_type: AclObjectType
    object_id: str = pydantic.Field()
    """
    Id of the object the function is originating from
    """

    internal: typing.Optional[bool] = pydantic.Field(default=None)
    """
    The function exists for internal purposes and should not be displayed in the list of functions.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
