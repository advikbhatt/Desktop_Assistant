## Voice-Controlled Personal Assistant

This project is a voice-controlled personal assistant designed to perform various tasks using speech recognition and the OpenAI API. The assistant is built in Python and utilizes several libraries for its functionality.

## Features

- **Speech Recognition**: The assistant can understand voice commands using the `speech_recognition` library.
- **OpenAI Integration**: It leverages the OpenAI API to perform tasks like generating text, answering questions, and more.
- **Customizable**: Users can add additional functionalities by extending the codebase.
- **Multi-Platform**: The assistant can run on any platform that supports Python.

## Installation

To install the required libraries, use the following `pip` commands:

```bash
pip install speech_recognition
pip install numpy
pip install win32com.client
```
Before running the assistant, make sure to obtain an API key from the OpenAI website by following this link
<br>(https://openai.com/index/openai-api). <br>Once you have the API key, replace `"Enter Your OPEN AI API KEY HERE"` in the code with your actual API key.

## Usage

1. Clone the repository to your local machine.<br>
2. Install the required libraries as mentioned above.<br>
3. Obtain an API key from the OpenAI website and replace `"Enter Your OPEN AI API KEY HERE"` in the code with your actual API key.<br>
4. Run the Python script `main.py`.<br>
5. Follow the on-screen instructions to interact with the voice-controlled assistant.

## Dependencies

- `speech_recognition`: For speech recognition functionality.<br>
- `openai`: For integrating with the OpenAI API.<br>
- `numpy`: For numerical computations.<br>
- `win32com.client`: For interacting with Windows applications.<br>
- `datetime`, `random`, `webbrowser`, `os`: Python's built-in libraries used for various tasks.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, feel free to fork the repository and submit a pull request with your changes.
