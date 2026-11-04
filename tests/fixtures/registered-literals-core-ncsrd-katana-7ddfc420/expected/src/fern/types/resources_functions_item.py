

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .resources_functions_item_pnf_list_item import ResourcesFunctionsItemPnfListItem
from .resources_functions_item_shared import ResourcesFunctionsItemShared


class ResourcesFunctionsItem(UniversalBaseModel):
    """
    A PDU
    """

    db_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="DB_ID"),
        pydantic.Field(alias="DB_ID", description="The id of the function in the Slice Manager DB"),
    ] = None
    """
    The id of the function in the Slice Manager DB
    """

    function_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique ID for this network function
    """

    location: typing.Optional[str] = None
    gen: typing.Optional[str] = pydantic.Field(default=None)
    """
    4G or 5G Generation Component
    """

    functionality: typing.Optional[str] = pydantic.Field(default=None)
    """
    Core/Radio
    """

    shared: typing.Optional[ResourcesFunctionsItemShared] = pydantic.Field(default=None)
    """
    Availability to be shared amongst many network slices
    """

    pnf_list: typing.Optional[typing.List[ResourcesFunctionsItemPnfListItem]] = pydantic.Field(default=None)
    """
    Conditional - If type == Physical - A list of the PNFs that will be part of the slice
    """

    tenants: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of Tenants using the PDU
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
