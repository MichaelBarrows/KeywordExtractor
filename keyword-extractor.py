# WRIGHT, J., 2018.Building a REST API in Python — Home Automation #02.
# [Online Video]. Available also from:https://www.youtube.com/watch?v=4T5Gnrmzjak


from flask import Flask
from flask_restful import Resource, Api, reqparse
from nltk import word_tokenize
from nltk import pos_tag

app = Flask(__name__)
api = Api(app)

class KeywordProcessor(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('query', required=True)
        args = parser.parse_args()
        questions_tokenised = []
        questions_tokenised = word_tokenize(args['query'])
        words_with_pos_tags = pos_tag(questions_tokenised)
        query = ''
        for word in words_with_pos_tags:
            if word[1] == "NNP" or word[1] == "NNS" or word[1] == "NN" or word[1] == "VBN" or word[1] == "JJ":
                query += word[0].lower()+' '
        return {'response': query}


api.add_resource(KeywordProcessor, '/')
