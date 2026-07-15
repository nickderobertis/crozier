

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .connector_doc_audience import ConnectorDocAudience
from .connector_doc_format import ConnectorDocFormat
from .id import Id


class ConnectorDoc(UniversalBaseModel):
    audience: typing.Optional[ConnectorDocAudience] = pydantic.Field(default=None)
    """
    Audience for the doc.
    """

    format: typing.Optional[ConnectorDocFormat] = pydantic.Field(default=None)
    """
    Format of the doc.
    """

    id: typing.Optional[Id] = None
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the doc.
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Link to fetch the content of the doc.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
