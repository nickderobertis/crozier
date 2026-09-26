

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .executable import Executable
from .parsed_inventory_sources_item import ParsedInventorySourcesItem


class ParsedInventory(UniversalBaseModel):
    app_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="appName"), pydantic.Field(alias="appName", description="Pipeline tool name")
    ]
    """
    Pipeline tool name
    """

    description: str = pydantic.Field()
    """
    Pipeline tool description
    """

    executables: typing.Optional[typing.List[Executable]] = pydantic.Field(default=None)
    """
    Pipeline tool executables
    """

    link: str = pydantic.Field()
    """
    Pipeline tool link
    """

    logo: str
    sources: typing.List[ParsedInventorySourcesItem] = pydantic.Field()
    """
    Pipeline tool sources
    """

    vendor: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
