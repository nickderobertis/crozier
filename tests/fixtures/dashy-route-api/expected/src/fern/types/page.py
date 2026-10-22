

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Page(UniversalBaseModel):
    """
    An extra config file loaded as a separate page.
    """

    name: str = pydantic.Field()
    """
    Unique page identifier
    """

    path: str = pydantic.Field()
    """
    File name or path of the page's config
    """

    display_data: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="displayData"),
        pydantic.Field(alias="displayData", description="Page visibility and display options"),
    ] = None
    """
    Page visibility and display options
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
