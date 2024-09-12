# GeoExplorer - A demo LLM application

* [LangChain](https://python.langchain.com/docs/get_started/introduction) is a framework that is used to build a LLM application.
* TODO: Build a LLM application using LLM (GPT-3.5) viz OpenAI API.

1. Create a new secret key with [OpenAI](https://platform.openai.com/api-keys)

```
NAME: langchain
SECRET KEY: sk-<secret-key>
```

2. Install the required dependencies:
```
$ pip install langchain
$ pip install openai

$ pip install -U langchain-openai
```

* Simple Sequential chain has provides the  final output with responses from intermediate outputs as an input.
* Sequential chain allows to have all the outputs of the chain.

3. `Streamlit` is a Python library to that allows POC frontend.
```
$ pip install streamlit
$ streamlit run main.py

Local URL: http://localhost:8501
```

## References:

1. [CodeBasics YouTube](https://www.youtube.com/watch?v=nAmC7SoVLd8&ab_channel=codebasics)
2. [LangChain Documentation](https://python.langchain.com/docs/get_started/introduction)