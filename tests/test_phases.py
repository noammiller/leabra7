from hypothesis import example
from hypothesis import given
import hypothesis.strategies as st
import pytest

from leabra7 import phases as ph


def test_you_can_get_the_names_of_all_defined_phases() -> None:
    actual = set(ph.Phase.names())
    expected = set(("plus", "minus", "none"))
    assert actual == expected


def test_you_can_get_all_defined_phases() -> None:
    actual = set(ph.Phase.phases())
    expected = set((ph.PlusPhase, ph.MinusPhase, ph.NonePhase))
    assert actual == expected


def test_phase_validates_name():
    with pytest.raises(ph.PhaseValidationError):
        new_phase = ph.Phase(name="")
    with pytest.raises(ph.PhaseValidationError):
        new_phase = ph.Phase(name="plus")
    with pytest.raises(ph.PhaseValidationError):
        new_phase = ph.Phase(name="minus")
    with pytest.raises(ph.PhaseValidationError):
        new_phase = ph.Phase(name="none")


def test_phase_inequality():
    assert ph.PlusPhase != ph.MinusPhase
    assert ph.PlusPhase != ph.NonePhase
    assert ph.MinusPhase != ph.NonePhase


@given(f=st.one_of(st.text(), st.integers(), st.floats(), st.booleans()))
def test_phase_equality_not_implemented(f):
    with pytest.raises(NotImplementedError):
        ph.PlusPhase == f


def test_phase_retrieval_by_name():
    assert ph.Phase.from_name("plus") is ph.PlusPhase
    assert ph.Phase.from_name("minus") is ph.MinusPhase
    assert ph.Phase.from_name("none") is ph.NonePhase


def test_new_phase_is_registered():
    new_phase = ph.Phase(name="new_phase")
    assert ph.Phase.from_name("new_phase") is new_phase
