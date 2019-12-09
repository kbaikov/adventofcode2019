import pytest


@pytest.fixture
def init_register():
    register = dict(
        instruction_pointer=0,
        opcode=0,
        parameter1_mode=0,
        parameter2_mode=0,
        parameter3_mode=0,
        input=0,
        output=0,
        relative_base=0,
    )
    yield register

    register = dict(
        instruction_pointer=0,
        opcode=0,
        parameter1_mode=0,
        parameter2_mode=0,
        parameter3_mode=0,
        input=0,
        output=0,
        relative_base=0,
    )
