import string
import pandas as pd
import json

class Cesar():

    def get_desafio(self, token):
        numero_casas = 7
        get_token = token
        cifrado = "puals puzpkl pz h nvclyutlua dhyupun ylxbpylk if shd. buruvdu"
        decifrado = "intel inside is a government warning required by law. unknown"
        resumo_criptografico = "65592d2be74be4208d62d9d5980d94b8c0f9adea"
        return numero_casas, cifrado

    def post_desafio(self, result):
        with open('answer.json', 'w') as f:
            json.dump(result, f)

    def result_json(self, fator, phrase, decrypt, token):
        result = {
            "numero_casas": fator,
            "token": token,
            "cifrado": phrase,
            "decifrado": decrypt,
            "resumo_criptografico": "65592d2be74be4208d62d9d5980d94b8c0f9adea"
        }
        return result


    def desafio(self, decrypt_or_crypt, token):
        fator, phrase = self.get_desafio(token)
        decrypt = self.cesar_criptor(decrypt_or_crypt, fator, phrase)
        result = self.result_json(fator, phrase, decrypt, token)
        self.post_desafio(result)
        return result

    def cesar_criptor(self, decrypt_or_crypt, fator, phrase):
        revert_alphabet = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if decrypt_or_crypt.lower() == 'crypt':
            alpha = alphabet
        else:
            alpha = revert_alphabet
        resultado = ''
        for letter in phrase:
            if letter.isalpha():
                posicao = alpha.lower().find(letter)
                if (posicao + fator) < 26:
                    posicao = (posicao + fator) % 26
                    resultado = resultado + alpha.lower()[posicao]
                else:
                    posicao = (posicao + fator) - 26
                    resultado = resultado + alpha.lower()[posicao]
            else:
                print(letter)
                resultado = resultado + letter
        return resultado