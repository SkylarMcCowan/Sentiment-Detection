# Sentiment Detection

This project provides a simple sentiment detection tool using the VADER (Valence Aware Dictionary and sEntiment Reasoner) sentiment analysis tool from the NLTK library.

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd Sentiment-Detection
    ```

2. Create and activate a virtual environment:
    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the sentiment detection script:
    ```sh
    python emotion_detection.py
    ```

2. Run the tests:
    ```sh
    python -m unittest test_emotion_detection.py
    ```

## Files

- `emotion_detection.py`: Contains the sentiment detection logic using VADER.
- `test_emotion_detection.py`: Contains unit tests for the sentiment detection logic.

## License

This project is licensed under the MIT License.
