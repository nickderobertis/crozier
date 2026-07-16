

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .global_config import GlobalConfig
from .import_export_admins_item import ImportExportAdminsItem
from .import_export_api_keys_item import ImportExportApiKeysItem
from .import_export_error_templates_item import ImportExportErrorTemplatesItem
from .import_export_service_descriptors_item import ImportExportServiceDescriptorsItem
from .import_export_service_groups_item import ImportExportServiceGroupsItem
from .import_export_simple_admins_item import ImportExportSimpleAdminsItem
from .import_export_stats import ImportExportStats


class ImportExport(UniversalBaseModel):
    """
    The structure that can be imported to or exported from Otoroshi. It represent the memory state of Otoroshi
    """

    admins: typing.List[ImportExportAdminsItem] = pydantic.Field()
    """
    Current U2F admin at the time of export
    """

    api_keys: typing_extensions.Annotated[
        typing.List[ImportExportApiKeysItem],
        FieldMetadata(alias="apiKeys"),
        pydantic.Field(alias="apiKeys", description="Current apik keys at the time of export"),
    ]
    """
    Current apik keys at the time of export
    """

    app_config: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]],
        FieldMetadata(alias="appConfig"),
        pydantic.Field(alias="appConfig", description="Current env variables at the time of export"),
    ] = None
    """
    Current env variables at the time of export
    """

    config: GlobalConfig = pydantic.Field()
    """
    Current global config at the time of export
    """

    date: dt.datetime
    date_raw: typing_extensions.Annotated[int, FieldMetadata(alias="dateRaw"), pydantic.Field(alias="dateRaw")]
    error_templates: typing_extensions.Annotated[
        typing.List[ImportExportErrorTemplatesItem],
        FieldMetadata(alias="errorTemplates"),
        pydantic.Field(alias="errorTemplates", description="Current error templates at the time of export"),
    ]
    """
    Current error templates at the time of export
    """

    label: str
    service_descriptors: typing_extensions.Annotated[
        typing.List[ImportExportServiceDescriptorsItem],
        FieldMetadata(alias="serviceDescriptors"),
        pydantic.Field(alias="serviceDescriptors", description="Current service descriptors at the time of export"),
    ]
    """
    Current service descriptors at the time of export
    """

    service_groups: typing_extensions.Annotated[
        typing.List[ImportExportServiceGroupsItem],
        FieldMetadata(alias="serviceGroups"),
        pydantic.Field(alias="serviceGroups", description="Current service groups at the time of export"),
    ]
    """
    Current service groups at the time of export
    """

    simple_admins: typing_extensions.Annotated[
        typing.List[ImportExportSimpleAdminsItem],
        FieldMetadata(alias="simpleAdmins"),
        pydantic.Field(alias="simpleAdmins", description="Current simple admins at the time of export"),
    ]
    """
    Current simple admins at the time of export
    """

    stats: ImportExportStats = pydantic.Field()
    """
    Current global stats at the time of export
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
