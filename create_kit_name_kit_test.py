import sender_stand_request
import data


# Función para obtener el valor de authorization de un nuevo usuario creado
def get_new_user_token():
    # Copiar el diccionario con el cuerpo de la solicitud desde el archivo de datos
    current_body = data.user_body.copy()
    # El resultado de la solicitud para crear un nuevo usuario se guarda en la variable user_response
    user_response = sender_stand_request.post_new_user(current_body)
    # De la respuesta de la solicitud se guarda el authToken en la variable user_authtoken
    user_authtoken = user_response.json().get('authToken')
    # Se devuelve el valor authToken del nuevo usuario requerido
    return user_authtoken

# Función para cambiar el valor del parámetro name en el cuerpo de la solicitud
def get_kit_body(name):
    # Copiar el diccionario con el cuerpo de la solicitud desde el archivo de datos
    current_kit_body = data.kit_body.copy()
    # Se cambia el valor del parámetro name
    current_kit_body["name"] = name
    # Se devuelve un nuevo diccionario con el valor name requerido
    return current_kit_body

# Función de prueba positiva
def positive_assert(kit_body):
    # El cuerpo de la solicitud actualizada se guarda en la variable current_kit_body
    current_kit_body = get_kit_body(kit_body["name"])
    # El valor de la cabecera se guarda en la variable current_auth_token
    current_auth_token = get_new_user_token()
    # El resultado de la solicitud para crear un nuevo kit de un usuario se guarda en la variable kit_response
    kit_response = sender_stand_request.post_new_client_kit(current_kit_body, current_auth_token)
    # Comprueba si el código de estado es 201
    assert kit_response.status_code == 201
    # Comprueba que el valor de nombre de la respuesta es el mismo que el de la solicitud
    assert kit_response.json().get("name") == current_kit_body["name"]

def negative_assert(kit_body):
    # El cuerpo de la solicitud actualizada se guarda en la variable current_kit_body
    current_kit_body = get_kit_body(kit_body["name"])
    # El valor de la cabecera se guarda en la variable current_auth_token
    current_auth_token = get_new_user_token()
    # El resultado de la solicitud para crear un nuevo kit de un usuario se guarda en la variable kit_response
    kit_response = sender_stand_request.post_new_client_kit(current_kit_body, current_auth_token)
    # Comprueba que el atributo code en el cuerpo de respuesta es 400
    assert kit_response.status_code == 400

# Prueba 1. Kit creado con éxito. El parámetro name contiene 1 caracter
def test_create_kit_1_letter_in_name_get_success_response():
    kit_body = get_kit_body("a")
    # Comprueba la respuesta
    positive_assert(kit_body)

# Prueba 2. Kit creado con éxito. El parámetro name contiene 511 caracteres
def test_create_kit_511_letter_in_name_get_success_response():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    # Comprueba la respuesta
    positive_assert(kit_body)

# Prueba 3. Error. El parámetro name del kit no contiene caracteres
def test_create_kit_0_letter_in_name_get_error_response():
    kit_body = get_kit_body("")
    # Comprueba la respuesta
    negative_assert(kit_body)

# Prueba 4. Error. El parámetro name del kit tiene 512 caracteres
def test_create_kit_512_letter_in_name_get_error_response():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    # Comprueba la respuesta
    negative_assert(kit_body)

# Prueba 5. Kit creado con éxito. El parámetro name del kit contiene caracteres especiales
def test_create_kit_has_special_symbol_in_name_get_success_response():
    kit_body = get_kit_body("\"№%@\",")
    # Comprueba la respuesta
    positive_assert(kit_body)

# Prueba 6. Kit creado con éxito. El parámetro name del kit contiene espacios
def test_create_kit_allows_spaces_in_name_get_success_response():
    kit_body = get_kit_body(" A Aaa ")
    # Comprueba la respuesta
    positive_assert(kit_body)

# Prueba 7. Kit creado con éxito. El parámetro name del kit contiene números
def test_create_kit_allows_numbers_in_name_get_success_response():
    kit_body = get_kit_body("123")
    # Comprueba la respuesta
    positive_assert(kit_body)

# Prueba 8. Error. Falta el parámetro name en la solicitud
def test_create_kit_no_name_get_error_response():
    # El valor de la cabecera se guarda en la variable current_auth_token
    current_auth_token = get_new_user_token()
    # El diccionario con el cuerpo de la solicitud se copia del archivo "data" a la variable "kit_body"
    current_kit_body = data.kit_body.copy()
    # El parámetro name se elimina de la solicitud
    current_kit_body.pop("name")
    # El resultado de la solicitud para crear un nuevo kit de un usuario se guarda en la variable kit_response
    kit_response = sender_stand_request.post_new_client_kit(current_kit_body, current_auth_token)
    # Comprueba que el atributo code en el cuerpo de respuesta es 400
    assert kit_response.status_code == 400

# Prueba 9. Error. El parámetro name en la solicitud es de distinto tipo (número)
def test_create_kit_different_type_get_error_response():
    # El cuerpo de la solicitud actualizada se guarda en la variable kit_body
    kit_body = get_kit_body(123)
    # Comprueba la respuesta
    negative_assert(kit_body)
