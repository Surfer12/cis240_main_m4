# Example of using Free Monads for effectful operations
from python import Python
from time import sleep
from random import random
from typing import Union

# Define a sample data structure
struct UserState:
    var heart_rate: Int
    var activity_level: Int

    fn __init__(inout self, hr: Int, act: Int):
        self.heart_rate = hr
        self.activity_level = act

# Define effectful operations
struct FetchHeartRate()
struct FetchActivityLevel()

# Define the Free Monad
type FreeMonad = Union[FetchHeartRate, FetchActivityLevel, UserState]

# Function to fetch user state
fn fetch_user_state() -> FreeMonad:
    return FetchHeartRate()

fn fetch_heart_rate() -> Int:
    return 75  # Simulated heart rate

fn fetch_activity_level() -> Int:
    return 5  # Simulated activity level

fn interpret_free_monad(free_monad: FreeMonad) -> UserState:
    if isinstance(free_monad, FetchHeartRate):
        let heart_rate = fetch_heart_rate()
        return interpret_free_monad(FetchActivityLevel())
    elif isinstance(free_monad, FetchActivityLevel):
        let activity_level = fetch_activity_level()
        return UserState(heart_rate=heart_rate, activity_level=activity_level)
    else:
        return free_monad

# Example usage
fn main():
    let user_state = interpret_free_monad(fetch_user_state())
    print("User State - HR:", user_state.heart_rate, "Activity:", user_state.activity_level)
