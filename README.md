# llm-jpn-to-eng-translation-service

Services to translate japanese sentences into english ones.

## Table of Contents
1. [File Descriptions](#files)
2. [Supporting Packages](#packages)
3. [How To Use This Repository](#howto)
4. [Example](#example)
5. [Licence & copyright](#license)

## File Descriptions <a name="files"></a>
| File | Description |
| :--- | :--- |
| main.py | the application entrypoint |
| src/routes | routes folder includes the api endpoints |
| src/schemas | pydantic schemas for data serialization |
| src/services | folder includes services with various business logic functionality |
| src/services/translation_service | the actual translation service |
| requirements.txt | list of python dependencies |

## Supporting Packages <a name="packages"></a>
In addition to the standard python library, this analysis utilizes the following packages:
- [FastAPI](https://fastapi.tiangolo.com/)
- [SentenceTransformers](https://www.sbert.net/)
- [PyTorch](https://pytorch.org/)
- [Transformers](https://pypi.org/project/transformers/)
- [Uvicorn](https://www.uvicorn.org/)

Please see `requirements.txt` for a complete list of packages and dependencies used in the making of this project.

## How To Use This Repository <a name="howto"></a>
1. Clone the repo locally or download and unzip this repository to a local machine.
2. Navigate to this directory and open the command line. For the purposes of running the scripts, this will be the root directory.
3. Create a virtual environment to store the supporting packages.

        python -m venv venv --upgrade-deps

4. Activate the virtual environment.

        source venv/bin/activate

5. Install the supporting packages from the requirements.txt file.

        pip install -r requirements.txt
        
6. Run the application 

        uvicorn main:app --reload --host --port 8001

8. Open up a browser and go to 127.0.0.1:8001/docs to access swagger.

9. Or send a curl request directly

          curl -X 'POST' \
                     'http://localhost:8001/query/' \
                     -H 'accept: application/json' \
                     -H 'Content-Type: application/json' \
                     -d '{
                     "query": "ホンダとスズキ原付きバイクの代わりに電動バイクを増やす"
            }'

Alternatively, you can run it via docker. To run it via docker:
1.  one of the folllowing
   * a) You can build the image locally: 
        ```docker build -t llm-translation-service .```
   * b) You can pull the already-build image from docker hub:
        ```docker pull kuator/llm-jpn-to-eng-translation-service``` 
2. run the image
        ```docker run -d -p 8001:8001 llm-translation-service```

## Example <a name="example"></a>
Translation of an example sentence in japanese "ホンダとスズキ原付きバイクの代わりに電動バイクを増やす" which roughly translates to "We're gonna increase number of electric bikes instead of honda and suzuki cars"
<p align="center">
    <img src="https://github.com/user-attachments/assets/70cdc0e9-9ee3-4d12-b961-c15dce09f7c0">
<p/>


Note: the application uses NLLB model by Meta for the translation functionality

## License & copyright <a name="license"></a>
© evakuator
Licensed under the [MIT License](LICENSE.txt)
