

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ImportExportErrorTemplatesItem(UniversalBaseModel):
    """
    Error templates for a service descriptor
    """

    messages: typing.Dict[str, str] = pydantic.Field()
    """
    Map for custom messages
    """

    service_id: typing_extensions.Annotated[str, FieldMetadata(alias="serviceId")] = pydantic.Field()
    """
    The Id of the service for which the error template is enabled
    """

    template40x: str = pydantic.Field()
    """
    The html template for 40x errors
    """

    template50x: str = pydantic.Field()
    """
    The html template for 50x errors
    """

    template_build: typing_extensions.Annotated[str, FieldMetadata(alias="templateBuild")] = pydantic.Field()
    """
    The html template for build page
    """

    template_maintenance: typing_extensions.Annotated[str, FieldMetadata(alias="templateMaintenance")] = (
        pydantic.Field()
    )
    """
    The html template for maintenance page
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
