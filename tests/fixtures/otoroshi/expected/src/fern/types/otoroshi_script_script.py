

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class OtoroshiScriptScript(UniversalBaseModel):
    """
    An otoroshi plugins stored as scala code in the otoroshi datastore
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the script
    """

    metadata: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Entity metadata
    """

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Entity tags
    """

    loc: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="_loc"), pydantic.Field(alias="_loc")
    ] = None
    desc: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the script
    """

    code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The code of the script
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the script
    """

    type: typing.Optional[typing.Any] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
