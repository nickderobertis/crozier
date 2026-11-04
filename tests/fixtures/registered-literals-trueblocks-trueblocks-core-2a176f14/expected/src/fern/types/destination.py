

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Destination(UniversalBaseModel):
    """
    an enhanced url used by chifra explore
    """

    term: typing.Optional[str] = pydantic.Field(default=None)
    """
    the term used to produce the url
    """

    term_type: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="termType"),
        pydantic.Field(alias="termType", description="the type of the term"),
    ] = None
    """
    the type of the term
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    the url produced
    """

    source: typing.Optional[str] = pydantic.Field(default=None)
    """
    the option that produced the url
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
