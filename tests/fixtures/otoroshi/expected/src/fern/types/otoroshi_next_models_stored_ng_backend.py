

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class OtoroshiNextModelsStoredNgBackend(UniversalBaseModel):
    """
    A backend that can be stored in the otoroshi datastore
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the backend
    """

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The tags of the backend
    """

    metadata: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    The metadata of the backend
    """

    backend: typing.Optional[typing.Any] = None
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the backend
    """

    loc: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="_loc"), pydantic.Field(alias="_loc")
    ] = None
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the backend
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
