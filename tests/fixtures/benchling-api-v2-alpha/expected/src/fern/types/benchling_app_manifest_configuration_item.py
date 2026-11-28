

import typing

from .dropdown_dependency import DropdownDependency
from .entity_schema_dependency import EntitySchemaDependency
from .manifest_array_config import ManifestArrayConfig
from .manifest_boolean_scalar_config import ManifestBooleanScalarConfig
from .manifest_date_scalar_config import ManifestDateScalarConfig
from .manifest_datetime_scalar_config import ManifestDatetimeScalarConfig
from .manifest_float_scalar_config import ManifestFloatScalarConfig
from .manifest_integer_scalar_config import ManifestIntegerScalarConfig
from .manifest_json_scalar_config import ManifestJsonScalarConfig
from .manifest_secure_text_scalar_config import ManifestSecureTextScalarConfig
from .manifest_text_scalar_config import ManifestTextScalarConfig
from .resource_dependency import ResourceDependency
from .schema_dependency import SchemaDependency
from .workflow_task_schema_dependency import WorkflowTaskSchemaDependency

BenchlingAppManifestConfigurationItem = typing.Union[
    SchemaDependency,
    EntitySchemaDependency,
    WorkflowTaskSchemaDependency,
    DropdownDependency,
    ResourceDependency,
    ManifestArrayConfig,
    ManifestTextScalarConfig,
    ManifestFloatScalarConfig,
    ManifestIntegerScalarConfig,
    ManifestBooleanScalarConfig,
    ManifestDateScalarConfig,
    ManifestDatetimeScalarConfig,
    ManifestSecureTextScalarConfig,
    ManifestJsonScalarConfig,
]
