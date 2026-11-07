

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_user_properties_response_data_item_group import GetUserPropertiesResponseDataItemGroup


class GetUserPropertiesResponseDataItem(UniversalBaseModel):
    """
    Properties details
    """

    group: typing.Optional[GetUserPropertiesResponseDataItemGroup] = pydantic.Field(default=None)
    """
    Property group details
    """

    is_computed: typing_extensions.Annotated[
        bool, FieldMetadata(alias="isComputed"), pydantic.Field(alias="isComputed")
    ]
    label: str
    name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
