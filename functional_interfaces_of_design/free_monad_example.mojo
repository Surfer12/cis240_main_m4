# Example of using Free Monads for effectful operations
from mojo.free_monad import FreeMonad

# Define a sample data structure
struct UserState:
    var heart_rate: Int
    var activity_level: String

# Define effectful operations
struct FetchHeartRate()
struct FetchActivityLevel()

# Define the Free Monad
type UserStateMonad = FreeMonad[UserState, FetchHeartRate, FetchActivityLevel]

# Function to fetch user state
fn fetch_user_state() -> UserStateMonad:
    return UserStateMonad(
        FetchHeartRate(),
        lambda heart_rate: UserStateMonad(
            FetchActivityLevel(),
            lambda activity_level: UserState(heart_rate=heart_rate, activity_level=activity_level)
        )
    )

# Example usage
let user_state = fetch_user_state()
print(user_state)
