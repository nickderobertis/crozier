

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nodes_identifiers_list_response_item_attributes_category import NodesIdentifiersListResponseItemAttributesCategory


class NodesIdentifiersListResponseItemAttributes(UniversalBaseModel):
    """
    The properties of the identifier entity.
    """

    category: typing.Optional[NodesIdentifiersListResponseItemAttributesCategory] = pydantic.Field(default=None)
    """
    The category of the identifier
    """

    value: typing.Optional[str] = pydantic.Field(default=None)
    """
    The identifier value itself
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
