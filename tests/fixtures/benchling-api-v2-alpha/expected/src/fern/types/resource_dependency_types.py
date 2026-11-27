

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResourceDependencyTypes(enum.StrEnum):
    AA_SEQUENCE = "aa_sequence"
    BOX = "box"
    CONTAINER = "container"
    CUSTOM_ENTITY = "custom_entity"
    DNA_OLIGO = "dna_oligo"
    DNA_SEQUENCE = "dna_sequence"
    ENTRY = "entry"
    FOLDER = "folder"
    LOCATION = "location"
    MIXTURE = "mixture"
    MOLECULE = "molecule"
    PLATE = "plate"
    PROJECT = "project"
    REGISTRY = "registry"
    RNA_OLIGO = "rna_oligo"
    RNA_SEQUENCE = "rna_sequence"
    WORKFLOW_TASK_STATUS = "workflow_task_status"
    WORKLIST = "worklist"

    def visit(
        self,
        aa_sequence: typing.Callable[[], T_Result],
        box: typing.Callable[[], T_Result],
        container: typing.Callable[[], T_Result],
        custom_entity: typing.Callable[[], T_Result],
        dna_oligo: typing.Callable[[], T_Result],
        dna_sequence: typing.Callable[[], T_Result],
        entry: typing.Callable[[], T_Result],
        folder: typing.Callable[[], T_Result],
        location: typing.Callable[[], T_Result],
        mixture: typing.Callable[[], T_Result],
        molecule: typing.Callable[[], T_Result],
        plate: typing.Callable[[], T_Result],
        project: typing.Callable[[], T_Result],
        registry: typing.Callable[[], T_Result],
        rna_oligo: typing.Callable[[], T_Result],
        rna_sequence: typing.Callable[[], T_Result],
        workflow_task_status: typing.Callable[[], T_Result],
        worklist: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ResourceDependencyTypes.AA_SEQUENCE:
            return aa_sequence()
        if self is ResourceDependencyTypes.BOX:
            return box()
        if self is ResourceDependencyTypes.CONTAINER:
            return container()
        if self is ResourceDependencyTypes.CUSTOM_ENTITY:
            return custom_entity()
        if self is ResourceDependencyTypes.DNA_OLIGO:
            return dna_oligo()
        if self is ResourceDependencyTypes.DNA_SEQUENCE:
            return dna_sequence()
        if self is ResourceDependencyTypes.ENTRY:
            return entry()
        if self is ResourceDependencyTypes.FOLDER:
            return folder()
        if self is ResourceDependencyTypes.LOCATION:
            return location()
        if self is ResourceDependencyTypes.MIXTURE:
            return mixture()
        if self is ResourceDependencyTypes.MOLECULE:
            return molecule()
        if self is ResourceDependencyTypes.PLATE:
            return plate()
        if self is ResourceDependencyTypes.PROJECT:
            return project()
        if self is ResourceDependencyTypes.REGISTRY:
            return registry()
        if self is ResourceDependencyTypes.RNA_OLIGO:
            return rna_oligo()
        if self is ResourceDependencyTypes.RNA_SEQUENCE:
            return rna_sequence()
        if self is ResourceDependencyTypes.WORKFLOW_TASK_STATUS:
            return workflow_task_status()
        if self is ResourceDependencyTypes.WORKLIST:
            return worklist()
