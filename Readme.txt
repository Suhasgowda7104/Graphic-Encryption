# Graphic Encryption

Graphic Encryption is an encryption technique that allows for the secure transmission of images. This project provides an implementation of visual cryptography algorithms and showcases how images can be encrypted and decrypted using these methods.

## Features

- **Encryption and Decryption**: Easily encrypt images into multiple shares and decrypt them back to the original image.
- **Support for Various Image Formats**: Compatible with common image formats like PNG, JPEG, and BMP.
- **User-friendly Interface**: Simple and intuitive interface for users to upload, encrypt, and decrypt images.
- **Customizable Parameters**: Adjust encryption parameters such as the number of shares and the threshold for decryption.
- **High Security**: Ensures that individual shares do not reveal any information about the original image unless combined correctly.

## Getting Started

### Prerequisites

- Python 3.x
- Virtual environment tool (e.g., `venv`)
- Visual Studio Code (VS Code)

### Installation

1. **Clone the Repository**:
    ```bash
    ```

2. **Navigate to the Project Directory**:
    ```bash
    cd Visual-Cryptography
    ```

3. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    ```

4. **Activate the Virtual Environment**:
    - On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```

5. **Install the Required Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Project

1. **Open the Project in VS Code**:
    - Open VS Code.
    - Select `File` > `Open Folder`.
    - Navigate to and select the `Visual-Cryptography` folder.

2. **Activate the Virtual Environment in VS Code**:
    - Press `Ctrl+Shift+P` to open the command palette.
    - Type `Python: Select Interpreter` and select the virtual environment you created (`venv`).

3. **Run the Main Script**:
    - Open the `main.py` file.
    - Press `F5` to start debugging and run the script.

4. **Follow the On-screen Instructions**:
    - Upload an image, choose encryption parameters, and generate encrypted shares.
    - To decrypt, upload the necessary shares and follow the instructions to reconstruct the original image.

## Examples

### Encrypting an Image

1. Upload an image file.
2. Choose the number of shares and threshold.
3. Generate and save the encrypted shares.

### Decrypting an Image

1. Upload the required number of shares.
2. Combine the shares to reconstruct the original image.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Reference Paper/Project](link to reference)
- Contributors and their GitHub profiles
