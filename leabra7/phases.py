"""Components for the AST that a leabra7 network can run."""
from typing import Dict
from typing import Sequence


class PhaseValidationError(Exception):
    """Raised when a phase fails validation checks."""
    pass


class Phase():
    """Defines network phases.
    Args:
        name: Name of phase.
        phase_type: Type of phase ('plus', 'minus', or 'none').
    Raises:
        ValueError: If phase_type not one of 'plus', 'minus', or 'none'.
    """
    # Stores a reference to each created frequency object, keyed by name
    registry: Dict[str, "Phase"] = {}

    name: str

    def __init__(self, name: str) -> None:
        if name == "":
            raise PhaseValidationError("Phase must have name.")
        if name in Phase.registry.keys():
            raise PhaseValidationError("Phase name is already taken: " + name)
        self.name = name
        Phase.registry[name] = self

    def __key(self) -> str:
        return self.name

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Phase):
            return self.__key() == other.__key()  #pylint: disable=protected-access
        raise NotImplementedError(
            "Invalid comparison between {0} and {1}".format(
                self.__class__.__name__, other.__class__.__name__))

    def __hash__(self) -> int:
        return hash(self.__key())

    def __str__(self) -> str:
        return str(self.name)

    @classmethod
    def names(cls) -> Sequence[str]:
        """Returns the names of all defined phases."""
        return tuple(cls.registry.keys())

    @classmethod
    def phases(cls) -> Sequence["Phase"]:
        """Returns all defined phases."""
        return tuple(cls.registry.values())

    @classmethod
    def from_name(cls, phase_name: str) -> "Phase":
        """Gets a phase object by its name.
        Args:
          phase_name: The name of the phase.
        Raises:
          ValueError: If no phase exists with name `phase_name`.
        """
        try:
            return cls.registry[phase_name]
        except KeyError:
            raise ValueError(
                "No phase with name {0} exists.".format(phase_name))


PlusPhase = Phase(name="plus")
MinusPhase = Phase(name="minus")
NonePhase = Phase(name="none")
