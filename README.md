## Keyword Extractor API
Created by Michael Barrows (22686134)

### Installation
To install the required dependencies for the keyword extractor, it is recommended that these actions are performed within a Python virtual environment, a new environment can be created using the following command:

```
mkvirtualenv keywordextractor --python /usr/bin/python3
workon keywordextractor
```
To run the keyword extractor various software needs to be installed using the `pip` command:
```
pip install Flask
pip install flask-restful
python nltk_install.py

```
when the NLTK GUI loads, please click the `All Packages` tab and select the `punkt` package and click download. The following additional packages may be required: `averaged_perceptron_tagger` and `stopwords`.

Once this is complete, the keyword extractor can be run by executing the following command:
```
FLASK_APP=keyword-extractor.py flask run --host=0.0.0.0 --port=5000
```
Once this is complete, the keyword extractor will be running and can be used automatically within the chatbot.
