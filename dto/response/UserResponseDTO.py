class UserResponseDTO():

    def formatDTO(userResponse):
        return {'firstName' :userResponse['firstName'], 'lastName':userResponse['lastName'], 'age': userResponse['age'], 'email':userResponse['email']}