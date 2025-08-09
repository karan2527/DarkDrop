# 🔒 DarkDrop - Secure File Transfer Tool

**DarkDrop** is a secure, encrypted file transfer tool that enables safe file sharing between devices over a network. Built with Python and featuring AES-256 encryption, it provides a user-friendly GUI for both sending and receiving files securely.

## ✨ Features

- 🔐 **AES-256 Encryption**: Military-grade encryption for maximum security
- 🖥️ **User-Friendly GUI**: Clean, dark-themed interface built with Tkinter
- 🌐 **Network Transfer**: Send files over local network or internet
- 🔑 **Password Protection**: PBKDF2 key derivation with 100,000 iterations
- 📱 **Dual Mode**: Both sender and receiver functionality in one application
- 🛡️ **Secure by Default**: No plaintext transmission, encrypted end-to-end

## 🚀 Quick Start

### Prerequisites

```bash
pip install cryptography
```

### Installation

1. Clone the repository:
```bash
git clone https://github.com/karan2527/DarkDrop.git
cd darkdrop
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python DarkDrop.py
```

## 📖 How to Use

### Ensure the listener is running before initiating the file transfer.

### Sending a File

1. Launch DarkDrop
2. Select "Send" mode
3. Enter the receiver's IP address
4. Set a port number (e.g., 8888)
5. Enter a strong password
6. Choose the file to send
7. Click "Execute"

### Receiving a File

1. Launch DarkDrop
2. Select "Receive" mode
3. Set the same port number as sender
4. Enter the same password
5. Click "Execute"
6. Wait for the file transfer to complete

## 🔧 Technical Details

### Encryption Specifications

- **Algorithm**: AES-256 in CBC mode
- **Key Derivation**: PBKDF2 with SHA-256
- **Salt**: Fixed salt (consider using random salt for production)
- **Iterations**: 100,000
- **Padding**: PKCS7
- **IV**: Randomly generated for each transfer

### Network Protocol

- **Transport**: TCP/IP
- **Data Format**: 
  - 4 bytes: filename length
  - Variable: filename
  - 16 bytes: IV
  - Variable: encrypted file data

## ⚠️ Security Considerations

### Current Implementation

- Uses a fixed salt for key derivation
- No authentication mechanism
- Vulnerable to man-in-the-middle attacks
- No integrity verification

### Recommended Improvements for Production

1. **Dynamic Salt Generation**: Use random salts for each session
2. **HMAC Authentication**: Add message authentication codes
3. **Key Exchange**: Implement secure key exchange protocol
4. **Certificate Validation**: Add TLS/SSL layer
5. **Integrity Checks**: Implement file hash verification

## 🛠️ Development

### Project Structure

```
DARKDROP/
├── DarkDrop.py          # Main application
├── requirements.txt     # Dependencies
├── README.md           # Documentation
├── LICENSE             # License file
└── screenshots/        # Application screenshots
```

## 📋 Requirements

- Python 3.7+
- cryptography library
- tkinter (usually included with Python)

## 🔗 Use Cases

- **Secure File Sharing**: Share sensitive documents safely
- **Network Administration**: Transfer configuration files securely
- **Development**: Share code and assets between team members
- **Personal Use**: Backup files between personal devices

## ⚡ Performance

- **File Size**: No theoretical limit (limited by available memory)
- **Network**: Optimized for both LAN and WAN transfers
- **Encryption Speed**: Efficient AES implementation via cryptography library


## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Known Issues

- Fixed salt reduces security (planned fix in v2.0)
- No connection timeout handling
- Limited error handling for network issues

## 💬 Support

If you have any questions or issues, please:

1. Check the existing issues
2. Create a new issue with detailed description
3. Contact: [amazing2311asus@gmail.com]

**⚠️ Disclaimer**: This tool is for educational and legitimate purposes only. Users are responsible for complying with all applicable laws and regulations. The developers are not responsible for any misuse of this software.

**🔒 Security Notice**: While DarkDrop provides strong encryption, it should not be used for highly sensitive data without additional security measures. Always use in trusted network environments.
