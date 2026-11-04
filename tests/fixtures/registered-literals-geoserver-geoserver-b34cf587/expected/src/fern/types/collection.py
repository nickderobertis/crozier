

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .extent import Extent
from .link import Link


class Collection(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    identifier of the collection used, for example, in URIs
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    human readable title of the collection
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    a description of the features in the collection
    """

    links: typing.List[Link]
    extent: typing.Optional[Extent] = None
    item_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="itemType"),
        pydantic.Field(
            alias="itemType",
            description="indicator about the type of the items in the collection (the default value is 'feature').",
        ),
    ] = None
    """
    indicator about the type of the items in the collection (the default value is 'feature').
    """

    crs: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    the list of coordinate reference systems supported by the service
    """

    storage_crs: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="storageCrs"),
        pydantic.Field(
            alias="storageCrs",
            description="the CRS identifier, from the list of supported CRS identifiers, that may be used to retrieve features from a collection without the need to apply a CRS transformation",
        ),
    ] = None
    """
    the CRS identifier, from the list of supported CRS identifiers, that may be used to retrieve features from a collection without the need to apply a CRS transformation
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
