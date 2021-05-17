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