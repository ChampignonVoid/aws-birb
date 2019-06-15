from rest_framework.schemas import AutoSchema
import coreapi


class SignUpSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method == 'POST':
            extra_fields = [
                coreapi.Field(
                    name='username',
                    required=True,
                    location='form',
                    description='Unique username'
                ),
                coreapi.Field(
                    name='first_name',
                    required=True,
                    location='form',
                    description='User\'s firstname'
                ),
                coreapi.Field(
                    name='last_name',
                    required=True,
                    location='form',
                    description='User\'s lastname'
                ),
                coreapi.Field(
                    name='email',
                    required=True,
                    location='form',
                    description='User\'s email'
                ),
                coreapi.Field(
                    name='password',
                    required=True,
                    location='form',
                    description='User\'s password'
                ),
            ]

        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields


class BirbMemeSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method == 'GET':
            extra_fields = [
                coreapi.Field(
                    name='meme_id',
                    required=True,
                    location='query',
                    description='The meme id'
                )
            ]

        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields