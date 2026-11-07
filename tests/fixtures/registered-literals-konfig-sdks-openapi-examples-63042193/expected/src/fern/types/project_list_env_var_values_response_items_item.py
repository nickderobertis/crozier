

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ProjectListEnvVarValuesResponseItemsItem(UniversalBaseModel):
    """
    An environment variable is a map containing a value and an optional timestamp.
    """

    name: str = pydantic.Field()
    """
    The name of the environment variable.
    """

    value: str = pydantic.Field()
    """
    The value of the environment variable.
    """

    created_at: typing_extensions.Annotated[
        typing.Optional[typing.Any],
        FieldMetadata(alias="created-at"),
        pydantic.Field(alias="created-at", description="The creation timestamp of the environment variable."),
    ] = None
    """
    The creation timestamp of the environment variable.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
