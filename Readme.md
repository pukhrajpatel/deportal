## List of API Endpoints

- /auth/users/ - POST request to signup new user (required fields - email, password, re_password)
- /auth/users/me/ - access users profile
- /auth/users/auth/token/logout/ - logout api
- /auth/users/activation/ - activation of user ( This endpoint is not a URL which will be directly exposed to your users - you should provide site in your frontend application (configured by ACTIVATION_URL) which will send POST request to activate endpoint)
- /auth/jwt/create/ - POST request on clicking Login button get JWT access and refresh token
- /auth/jwt/refresh/ - get JWT refresh token
- /villages/?state_name={state_name}/ - get villages boundary for these state
    - GET request for getting village boundary
- /mapping/?state_name={state_name}&ac_no={ac_no}/ - get mapping file of the respective AC