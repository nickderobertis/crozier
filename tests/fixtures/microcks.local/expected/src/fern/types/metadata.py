

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Metadata(UniversalBaseModel):
    """
    Commodity object for holding metadata on any entity. This object is inspired by Kubernetes metadata.
    """

    annotations: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Annotations of attached object
    """

    created_on: typing_extensions.Annotated[int, FieldMetadata(alias="createdOn")] = pydantic.Field()
    """
    Creation date of attached object
    """

    labels: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Labels put on attached object
    """

    last_update: typing_extensions.Annotated[int, FieldMetadata(alias="lastUpdate")] = pydantic.Field()
    """
    Last update of attached object
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
