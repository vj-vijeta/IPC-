# IPC Communication Using Unix Domain Sockets in Python

This repository demonstrates inter-process communication (IPC) between different programs using Unix domain sockets in Python. The example consists of two programs: a server that listens for connections and a client that sends messages to the server.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
  - [Server Program](#server-program)
  - [Client Program](#client-program)
- [License](#license)

## Introduction

IPC mechanisms allow different processes to communicate and share data. Unix domain sockets provide a reliable way for processes on the same machine to exchange information. This project demonstrates a simple server-client model using Unix domain sockets in Python.

## Prerequisites

- Python 3 installed on your system.
- Basic understanding of Python programming.
- Familiarity with sockets and IPC concepts.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/ipc-unix-sockets.git
    cd ipc-unix-sockets
    ```

2. Ensure Python 3 is installed:
    ```sh
    python3 --version
    ```

## Usage

1. **Start the Server**:
   - Open a terminal and run the server script.
     ```sh
     python3 server.py
     ```

2. **Send a Message from the Client**:
   - Open another terminal and run the client script with a message.
     ```sh
     python3 client.py "Hello, Server!"
     ```

3. **Expected Output**:
   - The server terminal should display:
     ```
     Server listening on /tmp/ipc_socket
     Client connected: ...
     Received: Hello, Server!
     ```

   - The client terminal should display:
     ```
     Sending: Hello, Server!
     Received: Hello, Server!
     ```

