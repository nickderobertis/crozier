

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .group_get import GroupGet
from .group_get_base import GroupGetBase


class MyGroupsGet(UniversalBaseModel):
    me: GroupGet
    organizations: typing.Optional[typing.List[GroupGet]] = None
    all_: typing_extensions.Annotated[GroupGet, FieldMetadata(alias="all"), pydantic.Field(alias="all")]
    product: typing.Optional[GroupGet] = None
    support: typing.Optional[GroupGetBase] = pydantic.Field(default=None)
    """
    Group ID of the app support team or None if no support is defined for this product
    """

    chatbot: typing.Optional[GroupGetBase] = pydantic.Field(default=None)
    """
    Group ID of the support chatbot user or None if no chatbot is defined for this product
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
