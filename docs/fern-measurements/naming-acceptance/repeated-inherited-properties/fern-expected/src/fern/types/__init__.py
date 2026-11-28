



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .folder import Folder
    from .oligo_base import OligoBase
    from .oligo_base_for_create import OligoBaseForCreate
    from .oligo_create import OligoCreate
    from .plasmid_base import PlasmidBase
    from .plasmid_base_for_create import PlasmidBaseForCreate
    from .plasmid_copies import PlasmidCopies
    from .plasmid_create import PlasmidCreate
    from .primer_base import PrimerBase
    from .primer_base_for_create import PrimerBaseForCreate
    from .primer_create import PrimerCreate
    from .primer_measure import PrimerMeasure
    from .registry_target import RegistryTarget
    from .strain_base import StrainBase
    from .strain_base_for_create import StrainBaseForCreate
    from .strain_create import StrainCreate
    from .strain_target import StrainTarget
    from .vector_base import VectorBase
    from .vector_base_for_create import VectorBaseForCreate
    from .vector_create import VectorCreate
    from .vector_placement import VectorPlacement
_dynamic_imports: typing.Dict[str, str] = {
    "Folder": ".folder",
    "OligoBase": ".oligo_base",
    "OligoBaseForCreate": ".oligo_base_for_create",
    "OligoCreate": ".oligo_create",
    "PlasmidBase": ".plasmid_base",
    "PlasmidBaseForCreate": ".plasmid_base_for_create",
    "PlasmidCopies": ".plasmid_copies",
    "PlasmidCreate": ".plasmid_create",
    "PrimerBase": ".primer_base",
    "PrimerBaseForCreate": ".primer_base_for_create",
    "PrimerCreate": ".primer_create",
    "PrimerMeasure": ".primer_measure",
    "RegistryTarget": ".registry_target",
    "StrainBase": ".strain_base",
    "StrainBaseForCreate": ".strain_base_for_create",
    "StrainCreate": ".strain_create",
    "StrainTarget": ".strain_target",
    "VectorBase": ".vector_base",
    "VectorBaseForCreate": ".vector_base_for_create",
    "VectorCreate": ".vector_create",
    "VectorPlacement": ".vector_placement",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "Folder",
    "OligoBase",
    "OligoBaseForCreate",
    "OligoCreate",
    "PlasmidBase",
    "PlasmidBaseForCreate",
    "PlasmidCopies",
    "PlasmidCreate",
    "PrimerBase",
    "PrimerBaseForCreate",
    "PrimerCreate",
    "PrimerMeasure",
    "RegistryTarget",
    "StrainBase",
    "StrainBaseForCreate",
    "StrainCreate",
    "StrainTarget",
    "VectorBase",
    "VectorBaseForCreate",
    "VectorCreate",
    "VectorPlacement",
]
