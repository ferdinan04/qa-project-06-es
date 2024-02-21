import configuration
import requests
import data


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados


def post_new_client_kit(kit_body, auth_token):
    headers = data.headers.copy()
    headers["Authorization"] = f'Bearer {auth_token}'
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,  # inserta el cuerpo de solicitud
                         headers=headers)  # inserta el valor authToken de la cabecera
