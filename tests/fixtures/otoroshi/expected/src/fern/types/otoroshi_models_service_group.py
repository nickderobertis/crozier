

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class OtoroshiModelsServiceGroup(UniversalBaseModel):
    """
    The otoroshi model for a group of services
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique random string to identify your service
    """

    loc: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="_loc"), pydantic.Field(alias="_loc")
    ] = None
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of your service. Only for debug and human readability purposes
    """

    metadata: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Just a bunch of random properties
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Entity description
    """

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Entity tags
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
