# -*- coding: utf-8 -*-
"""auth"""


from mozilla_django_oidc.auth import OIDCAuthenticationBackend


class CustomOIDCAuthenticationBackend(OIDCAuthenticationBackend):

    """CustomOIDCAuthenticationBackend"""

    def get_email(self, claims):
        email = claims.get('email')
        if not email:
            email = claims.get('sub')
        return email

    def filter_users_by_claims(self, claims):
        """Create user with email base custom user model."""
        email = self.get_email(claims)
        if not email:
            return self.UserModel.objects.none()
        try:
            return self.UserModel.objects.filter(email=email)
        except self.UserModel.DoesNotExist:
            return self.UserModel.objects.none()

    def create_user(self, claims):
        """Create user with email base custom user model."""
        email = self.get_email(claims)
        return self.UserModel.objects.create_user(email)

    # def verify_claims(self, claims):
    #     """Verify the provided claims to decide
    #     if authentication should be allowed."""
    #     scopes = self.get_settings('OIDC_RP_SCOPES')
    #     if not scopes:
    #         return False
    #     elif 'offline' in scopes.split():
    #         return 'offline' in claims
    #     return False
