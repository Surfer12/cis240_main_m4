from dataclasses import dataclass
from typing import Callable, TypeVar

T = TypeVar('T')
U = TypeVar('U')

@dataclass
class Lens:
    get: Callable[[T], U]
    set: Callable[[T, U], T]

@dataclass
class UserState:
    heart_rate: int
    activity_level: int

def heart_rate_lens() -> Lens[UserState, int]:
    return Lens(
        get=lambda state: state.heart_rate,
        set=lambda state, value: UserState(heart_rate=value, activity_level=state.activity_level)
    )

def update_heart_rate(state: UserState, new_rate: int) -> UserState:
    return heart_rate_lens().set(state, new_rate)

# Example usage
initial_state = UserState(heart_rate=72, activity_level=5)
updated_state = update_heart_rate(initial_state, 80)
print(f"Updated User State: {updated_state}") 