from flask_login import LoginManager, AnonymousUserMixin

class MyAnonymousUser(AnonymousUserMixin):

    def get_role(self):
        return 'AnonymousRole'

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
login_manager.anonymous_user = MyAnonymousUser
