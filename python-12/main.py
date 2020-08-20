
doc = '''
#%RAML: "1.0"
info:
description: "API"
title: api
mediaType: application/json
host: "aceleradev-user.com"
basePath: "/api"

securitySchemes: 
  JWT:
    description: API Requests
    type: JWT
    describedBy:
      headers:
        Authorization:
          description: Token valido
          type: string
      queryParameters:
        access_token:
          description: JWT token
          type: string
      responses:
        401:
          description: Token invalido
        403:
          description: Bad request
      settings:
        authorizationUri: https://www.user.com/JWT/authorize
        accessTokenUri: https://api.user.com/JWT/token
        authorizationGrants: [authorization_code, implicit]     

types:
  Auth:
    type: object
    discriminator: token
    properties:
      token: string 

  Agent:
    type: object
    discriminator: agent_id
    properties:
      agent_id: integer
      user_id: integer
      name:
        type: string
        maxLenght: 50
      status:
        type: boolean
      environment:
        type: string
        maxLenght: 20
      version:
        type: string
        maxLenght: 5
      address:
        type: string
        maxLenght: 39 

  Event:
    type: object
    discriminator: event_id
    properties:
      event_id: integer
      agent_id: integer
      level:
        type: string
        maxLenght: 20
      payload: string  
      shelve: boolean
      date: datetime-only

  Group:
    type: object
    discriminator: group_id
    properties:
      group_id: integer
      name:
        type: string
        maxLenght: 20

  User:
    type: object
    discriminator: user_id
    properties:
      user_id: integer
      name:
        type: string
        maxLenght: 50
      password:
        type: string
        maxLenght: 50
      email:
        type: string
        maxLenght: 254
      last_login:
        type: date
 

traits:
  dataValidation:
    responses:
      400:
        description: Bad Request.
        body:
          properties:
            error: string        

/auth/token:
  post:
    description: Token
    is: [dataValidation]
    securedBy: JWT
    body:
      application/json:
        username: string
        password: string
    responses:
      201:
        body:
          application/json:
            type: Auth
      400:
        body:
          application/json: |
            {"error": "Falha ao autenticar!"}

/agents:
  get:
    description: "Agents"
    securedBy: JWT
    tags:
    - "agents"
    operationId: "listAgents"
    consumes:
    - "application/json"
    produces:
    - "application/json"
    queryParameters:
      name: string
      status:
        required: True
        type: bool    
      environment:
        required: True
        type: string
    responses:
      200:
        body:
          application/json: Agent[]
      500:
        body:
          type: Mensagem
  post:
    description: Adiciona Agent
    securedBy: JWT
    body:
      application/json:
        properties:
    responses:
      201:
        body:
          application/json:
            example: |
              {"agent_id": 1}
      401:
        body:
          application/json: |
              {"error": "unauthorized"}  
  /{id}:
    uriParameters:
      id:
        description: Identifica o Agent
        type: string
    get:
      description: Busca agent
      securedBy: JWT
      responses:
        200:
          description: Sucesso ao buscar agente
          body:
            application/json: Agent
        401:
          body:
            application/json: |
              {"error": "Unauthorized"}
        404:
          body:
            application/json: |
              {"error": "Bad Request"}      
    put:
      description: Atualiza um Agent
      securedBy: JWT
      responses:
        200:
          body:
            application/json: Agent
        401:
          body:
            application/json: |
              {"error": "Unauthorized"}
        404:
          body:
            application/json: |
              {"error": "Bad Request"}      
    delete:
      description: Deleta um Agent
      securedBy: JWT
      responses:
        200:
          body:
            application/json: Agent
        401:
          body:
            application/json: |
              {"error": "Unauthorized"}
        404:
          body:
            application/json: |
              {"error": "Bad Request"}
  /{id}/events:
    get:
      description: Lista eventos de um agent
      queryParameters:
        level:
          type: list
      securedBy: JWT    
      responses:
        200:
          body:
            application/json: Event[]
        401:
          body:
            application/json: |
              {"error": "Unauthorized"}
        404:
          body:
            application/json: |
              {"error": "Bad Request"}
    post:
      description: Adiciona evento
      securedBy: JWT
      body:
        application/json: Event[]
      responses:
        201:
          body:
            application/json: |
              {"message": "Created"}
        401:
          body:
            application/json: |
              {"error": "Unauthorized"}
        404:
          body:
            application/json: |
              {"error": "Bad Request"}
    put:
      description: Modifica um evento
      securedBy: JWT
      body:
        application/json: Event[]
      responses:
        200:
          body:
            application/json: |
              {"message": "Modificado"}
        401:
          body:
            application/json: |
              {"error": "Unauthorized"}
        404:
          body:
            application/json: |
              {"error": "Bad Request"}     
    delete:
      description: Remove um evento
      securedBy: JWT
      body:
        application/json: Event[]
      responses:
        200:
          body:
            application/json: |
              {"message": "Removed"}
        401:
          body:
            application/json: |
              {"error": "Unauthorized"}
        404:
          body:
            application/json: |
              {"error": "Bad Request"}                  
    /{id}:
      uriParameters:
        id:
          description: Identificador do Evento
          type: string
      get:
        description: Lista um evento especifico
        securedBy: JWT
        body:
          application/json: 
        responses:
          200:
            body:
              application/json: |
                {"message": "Ok"}
          401:
            body:
              application/json: |
                {"error": "Unauthorized"}
          404:
            body:
              application/json: |
                {"error": "Bad Request"}                 
      put:
        description: Modifica um evento
        securedBy: JWT
        body:
          application/json:
        responses:
          200:
            body:
              application/json: |
                {"message": "Modificado"}
          401:
            body:
              application/json: |
                {"error": "Unauthorized"}
          404:
            body:
              application/json: |
                {"error": "Bad Request"}       
      delete:
        description: Remove um evento
        securedBy: JWT
        responses:
          200:
            body:
              application/json: |
                {"message": "Removido"}
          401:
            body:
              application/json: |
                {"error": "Unauthorized"}
          404:
            body:
              application/json: |
                {"error": "Bad Request"}                                        

/users:
  get:
    description: Lista todos os usuários
    securedBy: JWT    
    responses:
      200:
        body:
          application/json: User[]
      401:
        body:
          application/json: |
            {"error": "Unauthorized"}
  post:
    description: Grava um novo cadastro
    securedBy: JWT
    body:
      application/json:
        properties:
          name:
            type: string
            maxLength: 50
          password:
            type: string
            maxLength: 50  
          email:
            type: string
            maxLength: 254
          last_login:
            type: date-only
    responses:
      201:
        body:
          application/json: |
            {"message": "Gravado"}
      401:
        body:
          application/json: |
            {"error": "Unauthorized"}
  /{id}:
    uriParameters:
      id:
        description: Identificação do usuário.
        type: string
    get:
      description: Lista um usuario especifico
      securedBy: JWT
      responses:
        200:
          body:
            application/json: User
        401:
          body:
            application/json: |
              {"error": "Unauthorized"}
        404:
          body:
            application/json: |
              {"error": "Bad Request"}          
    put:
      description: Modifica um usuário
      securedBy: JWT
      responses:
        200:
          body:
            application/json: |
              {"message": "Modificado"}
        401:
          body:
            application/json: |
              {"error": "Unauthorized"}
        404:
          body:
            application/json: |
              {"error": "Bad Request"}            
    delete:
      description: Remove usuario cadastrado
      securedBy: JWT
      body:
        application/json: User
      responses:
        200:
          body:
            application/json: |
              {"message": "Deletado"}
        401:
          body:
            application/json: |
              {"error": "Unauthorized"}
        404:
          body:
            application/json: |
              {"error": "Bad Request"}            

/groups:
  get:
    description: Lista grupos de usuario
    securedBy: JWT
    queryParameters:
      name:
        required: True
        type: string
    responses:
      200:
        body:
          application/json: Group[]
      401:
        body:
          application/json:
            {"error": "Unauthorized"}      
  post:
    description: Grava um novo grupo
    is: [dataValidation]
    securedBy: JWT
    body:
      application/json:
        properties:
          name:
            type: string
            maxLenght: 20
    responses:
      201:
        body:
          application/json: |
            {"message": "Gravado"}
      401:
        body:
          application/json: |
            {"error": "Unauthorized"} 
  put:
    description: Modifica um grupo
    securedBy: JWT
    responses:
      200:
        body:
          application/json: |
            {"message": "modificado"}
      401:
        body:
          application/json: |
            {"message": "Unauthorized"}    
  delete:
    description: Remove um grupo
    responses:
      200:
        body:
          application/json:                 
  /{id}:
    uriParameters:
      id:
        description: Identificador do Grupo
        type: string
    get:
      description: Lista um grupo especifico
      securedBy: JWT
      responses:
        200:
          body:
            application/json: Group
        401:
          body:
            application/json: |
              {"error": "Unauthorized"}
        404:
          body:
            application/json: |
              {"error": "Bad Request"}          
    put:
      description: Modifica o grupo criado
      is: [dataValidation]
      securedBy: JWT
      body:
        application/json: Group
      responses:
        200:
          body:
            application/json: |
              {"message": "Modificado"}
        401:
          body:
            application/json: |
              {"error": "Unauthorized"}      
    delete:
      description: Deleta o grupo
      securedBy: JWT
      responses:
        200:
          body:
            application/json: |
              {"message": "Deletado"}
        401:
          body:
            application/json: |
              {"error": "Unauthorized"}
        404:
          body:
            application/json: |
              {"error": "Bad Request"} 
'''
