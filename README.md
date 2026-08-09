# PySocket Chat System

A multi-client TCP/IP chat application built entirely with Python's standard library.

The project implements a complete client-server architecture with real-time messaging, multi-threaded connection handling, a Tkinter graphical interface, private and public messaging, automatic chat logging, and process lifecycle management.

## Features

* **TCP/IP Communication** — Reliable communication between multiple clients using TCP sockets.
* **Multi-Client Support** — Multiple computers or clients can connect to the same server simultaneously.
* **Multi-Threaded Server** — Each connected client is handled in a dedicated thread, allowing multiple users to communicate concurrently.
* **Broadcast Messaging** — Send messages to all connected users.
* **Private Messaging** — Send direct messages to a specific connected user.
* **Graphical User Interface** — Tkinter-based client interface with visually differentiated message types.
* **Dynamic Message Styling**

  * Public messages — Blue
  * Private messages — Purple
  * System messages — Gray / White
* **Automatic Logging** — The server records chat activity in `chat_history.txt`.
* **Process Automation** — `main.py` launches and manages the server and client processes automatically.
* **Watchdog Mechanism** — Monitors the server process and terminates remaining client processes when the server shuts down.

---

## Architecture

The application follows a classic client-server architecture:

```text
                   ┌─────────────────┐
                   │     Server      │
                   │   server.py     │
                   │                 │
                   │ TCP Socket      │
                   │ Client Routing  │
                   │ Chat Logging    │
                   └────────┬────────┘
                            │
                   TCP Connections
                      ┌─────┴─────┐
                      │           │
             ┌────────▼───┐ ┌────▼───────┐
             │  Client 1  │ │  Client 2  │
             │ client.py  │ │ client.py  │
             │            │ │            │
             │ Tkinter GUI│ │ Tkinter GUI│
             └────────────┘ └────────────┘
```

Each client establishes a TCP connection with the server.

The server maintains the active client connections and routes incoming messages either to all connected users or to a specific recipient.

---

## Project Structure

```text
PySocket-Chat/
│
├── main.py
├── server.py
├── client.py
├── chat_history.txt
└── README.md
```

### `main.py` — Process Orchestrator

Acts as the application launcher and lifecycle manager.

Responsibilities include:

* Starting the server process.
* Launching multiple client processes using `subprocess`.
* Monitoring the server process.
* Detecting server termination using `poll()`.
* Closing remaining client processes when the server shuts down.

The watchdog checks the server state every 0.5 seconds.

---

### `server.py` — Chat Server

The central component of the system.

Responsibilities include:

* Creating the TCP socket.
* Binding the server to a host and port.
* Listening for incoming connections.
* Accepting multiple clients.
* Maintaining connected client sockets.
* Handling each client using a dedicated thread.
* Routing broadcast and private messages.
* Recording chat activity in `chat_history.txt`.

---

### `client.py` — Chat Client

Provides the user-facing application.

Each client combines:

* A Tkinter graphical interface.
* A TCP socket connection to the server.
* A background listener for incoming messages.

The networking listener runs separately from the GUI flow so incoming network traffic does not freeze the interface.

---

## Communication Protocol

Messages use a lightweight text-based protocol:

```text
TARGET:MESSAGE
```

### Broadcast Message

```text
ALL:Hello everyone!
```

The server forwards the message to all connected clients.

### Private Message

```text
Moshe:Hello Moshe!
```

The server identifies the requested recipient and forwards the message only to that client.

Private messages are visually distinguished in the GUI from public messages.

> Note: Private messages are routed only to the intended recipient, but the current implementation does not provide cryptographic encryption.

---

## Concurrency

The server uses Python threading to support multiple simultaneous clients.

Conceptually:

```text
Server
├── Client 1 Handler Thread
├── Client 2 Handler Thread
├── Client 3 Handler Thread
└── ...
```

This prevents one connected client from blocking communication with the others while the server waits for network input.

The client also separates network reception from GUI activity, allowing messages to arrive without freezing the interface.

---

## Chat Logging

The server automatically stores chat activity in:

```text
chat_history.txt
```

This provides a persistent record of messages exchanged during the session.

---

## Watchdog & Lifecycle Management

`main.py` monitors the server process using:

```python
server_process.poll()
```

The server status is checked every 0.5 seconds.

When the server process terminates, the orchestrator automatically closes the remaining client processes.

On Windows, the implementation uses `taskkill` for process termination.

This allows the entire application lifecycle to be controlled from a single entry point.

---

## Running the Project

### Requirements

* Python 3.x
* No external packages required

The project uses only Python's standard library, including modules such as:

```text
socket
threading
tkinter
subprocess
time
```

### Start the Application

Clone the repository:

```bash
git clone <repository-url>
cd PySocket-Chat
```

Run:

```bash
python main.py
```

The launcher automatically starts:

* One server process
* Two client instances

You can then use the client windows to exchange messages.

---

## Running Across Multiple Computers

The application can also be used between different computers connected to the same local network.

The clients must connect to the IP address of the computer running the server.

Example architecture:

```text
Computer A
Server
192.168.1.10
      │
      ├──────── TCP ──────── Computer B / Client
      │
      └──────── TCP ──────── Computer C / Client
```

This demonstrates actual socket-based communication between independent machines rather than communication only between processes running on the same computer.

---

## Technical Concepts Demonstrated

This project demonstrates practical use of several computer networking and software-development concepts:

* TCP/IP networking
* Client-server architecture
* Socket programming
* Concurrent programming
* Multi-threading
* Message routing
* Application-layer protocols
* GUI programming
* Process management
* Logging
* Inter-process lifecycle management

---

## Possible Future Improvements

Potential extensions include:

* User authentication
* Cryptographic message encryption
* Group chats / channels
* File transfer
* Message timestamps
* Connection recovery
* Server-side user management
* Persistent message storage using a database
* Cross-platform process termination
* Custom binary or JSON-based messaging protocol

---

## About

PySocket Chat System was developed as a computer networking project to explore TCP socket programming, concurrent client handling, communication protocols, and client-server system design in Python.
