

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Metadata(UniversalBaseModel):
    """
    Metadata of Extension.
    """

    annotations: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Annotations are like key-value format.
    """

    creation_timestamp: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="creationTimestamp"),
        pydantic.Field(alias="creationTimestamp", description="Creation timestamp of the Extension."),
    ] = None
    """
    Creation timestamp of the Extension.
    """

    deletion_timestamp: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="deletionTimestamp"),
        pydantic.Field(alias="deletionTimestamp", description="Deletion timestamp of the Extension."),
    ] = None
    """
    Deletion timestamp of the Extension.
    """

    finalizers: typing.Optional[typing.List[typing.Optional[str]]] = None
    generate_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="generateName"),
        pydantic.Field(
            alias="generateName",
            description="The name field will be generated automatically according to the given generateName field",
        ),
    ] = None
    """
    The name field will be generated automatically according to the given generateName field
    """

    labels: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Labels are like key-value format.
    """

    name: str = pydantic.Field()
    """
    Metadata name
    """

    version: typing.Optional[int] = pydantic.Field(default=None)
    """
    Current version of the Extension. It will be bumped up every update.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
