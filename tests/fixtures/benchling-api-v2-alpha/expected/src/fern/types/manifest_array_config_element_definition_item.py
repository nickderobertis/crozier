

import typing

from .dropdown_dependency import DropdownDependency
from .entity_schema_dependency import EntitySchemaDependency
from .manifest_scalar_config import ManifestScalarConfig
from .resource_dependency import ResourceDependency
from .schema_dependency import SchemaDependency
from .workflow_task_schema_dependency import WorkflowTaskSchemaDependency

ManifestArrayConfigElementDefinitionItem = typing.Union[
    SchemaDependency,
    EntitySchemaDependency,
    WorkflowTaskSchemaDependency,
    DropdownDependency,
    ResourceDependency,
    ManifestScalarConfig,
]
