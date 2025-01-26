# Example of using Lenses to update nested data structures
from python import Python
from time import sleep
from random import random

# Define a sample data structure
struct UserState:
    var heart_rate: Int
    var activity_level: Int

    fn __init__(inout self, hr: Int, act: Int):
        self.heart_rate = hr
        self.activity_level = act

struct Lens[T, U]:
    var get: fn(T) -> U
    var set: fn(T, U) -> T

# Create a Lens for the heart_rate field
fn heart_rate_lens() -> Lens[UserState, Int]:
    return Lens(
        get=lambda state: state.heart_rate,
        set=lambda state, value: UserState(heart_rate=value, activity_level=state.activity_level)
    )

# Function to update heart rate using the Lens
fn update_heart_rate(state: UserState, new_rate: Int) -> UserState:
    return heart_rate_lens().set(state, new_rate)

fn main():
    let initial_state = UserState(heart_rate=72, activity_level=5)
    let updated_state = update_heart_rate(initial_state, 80)
    print("Updated User State - HR:", updated_state.heart_rate, "Activity:", updated_state.activity_level)
