from dataclasses import dataclass
from typing import Callable, Union

@dataclass
class UserState:
    heart_rate: int
    activity_level: int

class FetchHeartRate:
    pass

class FetchActivityLevel:
    pass

# Define the Free Monad type
FreeMonad = Union[FetchHeartRate, FetchActivityLevel, UserState]

def fetch_user_state() -> FreeMonad:
    def fetch_heart_rate() -> int:
        return 75  # Simulated heart rate

    def fetch_activity_level() -> int:
        return 5  # Simulated activity level

    return FetchHeartRate()

def interpret_free_monad(free_monad: FreeMonad) -> UserState:
    if isinstance(free_monad, FetchHeartRate):
        heart_rate = fetch_heart_rate()
        return interpret_free_monad(FetchActivityLevel())
    elif isinstance(free_monad, FetchActivityLevel):
        activity_level = fetch_activity_level()
        return UserState(heart_rate=heart_rate, activity_level=activity_level)
    else:
        return free_monad

# Example usage
user_state = interpret_free_monad(fetch_user_state())
print(f"User State: {user_state}") 