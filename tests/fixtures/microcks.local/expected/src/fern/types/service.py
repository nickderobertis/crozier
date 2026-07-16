

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .metadata import Metadata
from .operation import Operation
from .service_type import ServiceType


class Service(UniversalBaseModel):
    """
    Represents a Service or API definition as registred into Microcks repository
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier for this Service or API
    """

    metadata: typing.Optional[Metadata] = pydantic.Field(default=None)
    """
    Metadata of Service
    """

    name: str = pydantic.Field()
    """
    Distinct name for this Service or API (maybe shared among many versions)
    """

    operations: typing.Optional[typing.List[Operation]] = pydantic.Field(default=None)
    """
    Set of Operations for Service or API
    """

    type: ServiceType = pydantic.Field()
    """
    Service or API Type
    """

    version: str = pydantic.Field()
    """
    Distinct version for a named Service or API
    """

    xml_ns: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="xmlNS"),
        pydantic.Field(alias="xmlNS", description="Associated Xml Namespace in case of Xml based Service"),
    ] = None
    """
    Associated Xml Namespace in case of Xml based Service
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
