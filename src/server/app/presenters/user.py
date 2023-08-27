from app.models import User


def create_authenticated_user_data(user: User) -> dict:
    return {
        "isAuthenticated": user.is_authenticated,
        "loginId": user.login_id,
        "firstName": user.first_name,
        "lastName": user.last_name,
        "enFirstName": user.en_first_name,
        "enLastName": user.en_last_name,
    }
