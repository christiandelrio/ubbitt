class SessionDao:

    def __init__(self):
        self.sessions = []

    def save_session(self, session):
        self.sessions.append(session)

    def find_user_by_session(self, session_id):
        found_sessions = list(filter(lambda session: (session.session_id == session_id), self.sessions))
        user_session = None
        if len(found_sessions) > 0:
            user_session = found_sessions[0]
        return user_session

    def delete_session_by_id(self, session_id):
        # Elimina la sesión filtrando por el id
        self.sessions = list(filter(lambda session: (session.session_id != session_id), self.sessions))