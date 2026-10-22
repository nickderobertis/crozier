

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .items_create_request_data_props import ItemsCreateRequestDataProps


class ItemsCreateRequestData(UniversalBaseModel):
    props: typing_extensions.Annotated[
        ItemsCreateRequestDataProps,
        FieldMetadata(alias="Props"),
        pydantic.Field(alias="Props", description="Typed properties."),
    ]
    """
    Typed properties.
    """

    ext: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]], FieldMetadata(alias="Ext"), pydantic.Field(alias="Ext")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
