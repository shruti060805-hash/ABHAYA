# ABHAYA
# 🛡️ ABHAYA — AI-Powered Women Safety Application

<div align="center">

### Empowering Women. Enhancing Safety. Building a Fearless Future.

**ABHAYA** is an AI-powered women safety ecosystem designed to provide intelligent threat detection, emergency assistance, real-time location sharing and proactive safety support through modern technology.

![Project Status](https://img.shields.io/badge/Project-Under%20Development-orange)
![Platform](https://img.shields.io/badge/Platform-Android%20%7C%20Cross--Platform-blue)
![AI](https://img.shields.io/badge/AI-YOLO%20%7C%20Machine%20Learning-purple)
![Backend](https://img.shields.io/badge/Backend-FastAPI-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

</div>

---

## 🌸 About ABHAYA

The safety of women remains an important social and technological challenge. Traditional safety applications often depend on manual SOS activation, which may not always be possible during emergencies.

**ABHAYA aims to go beyond traditional SOS applications.**

It integrates Artificial Intelligence, computer vision, voice-based distress detection and real-time location services to create a smarter and more responsive safety ecosystem.

The goal is to develop a system that can assist users during emergencies, identify potential threats and help them connect with trusted contacts.

**Our vision:** Transform personal safety from a reactive response into a proactive, intelligent support system.

## 🎯 Problem Statement

Women may encounter situations where:
- They cannot manually access their phones during an emergency.
- They cannot communicate their distress verbally.
- Their location is unknown to trusted contacts.
- Traditional emergency applications require manual interaction.
- Immediate access to emergency assistance is limited.

ABHAYA explores technology-driven solutions to address these challenges.

## ✨ Key Features

### 1. 🚨 Intelligent SOS Emergency System
- One-touch emergency activation.
- Emergency alerts to registered trusted contacts.
- Location sharing during emergencies.
- Emergency incident tracking.

### 2. 📍 Real-Time Location Sharing
- GPS-based location tracking.
- Sharing location with trusted contacts.
- Location updates during active emergencies.
- Location-based safety assistance.

### 3. 👁️ AI-Powered Visual Threat Detection
- Integration with YOLO-based computer vision.
- Exploration of suspicious activity recognition.
- Real-time video analysis where supported.
- AI-assisted identification of potentially dangerous situations.

### 4. 🎙️ Voice-Based Distress Detection
- Exploration of voice distress recognition.
- Detection of predefined distress signals.
- AI-assisted emergency identification.
- Integration with the emergency alert system.

### 5. 📡 Offline Emergency Support
- Local storage of essential emergency information.
- Queuing emergency requests when connectivity is unavailable.
- Synchronization when connectivity returns.
- Offline-first safety functionality where technically supported.

### 6. 👥 Trusted Contacts Management
- Add and manage emergency contacts.
- Configure emergency notification preferences.
- Share emergency information with authorized contacts.

### 7. 🔐 Secure User Authentication
- User registration and login.
- Secure password handling.
- Protected user information.
- Authentication-based access control.

### 8. 📊 Emergency History
- Maintain emergency incident records.
- View previous SOS activities.
- Review emergency notifications and status.

---

## 🧠 Technology Stack

| Component | Technologies |
|---|---|
| Mobile Application | Flutter, Dart |
| UI/UX | Material Design 3 |
| State Management | BLoC / Provider |
| API Integration | Dio |
| Backend | Python, FastAPI |
| Database | MongoDB |
| Artificial Intelligence | Machine Learning |
| Computer Vision | YOLOv8 |
| Voice Processing | Python, Audio Processing |
| Authentication | JWT |
| Version Control | Git, GitHub |
| Development Environment | VS Code, GitHub Codespaces |

*Technologies listed represent the intended architecture; individual integrations may still be under development.*

## 🏗️ System Architecture

```text
              ABHAYA MOBILE APP
                  (Flutter)
                      |
          +-----------+-----------+
          |           |           |
         SOS       GPS/Location   User
          |           |         Authentication
          +-----------+-----------+
                      |
                 FASTAPI
                 BACKEND
                      |
          +-----------+-----------+
          |           |           |
       MongoDB     AI Engine   Notification
                    |          Service
              +-----+-----+
              |           |
            YOLO       Voice AI
         Detection    Detection
              |           |
              +-----+-----+
                    |
             SAFETY RESPONSE
```

## 📂 Project Structure

```text
ABHAYA/
│
├── frontend/
│   └── Flutter application
│
├── backend/
│   ├── app/
│   │   ├── routes/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── core/
│   │   └── main.py
│   │
│   ├── requirements.txt
│   └── .env.example
│
├── ai_engine/
│   ├── vision/
│   ├── voice/
│   └── models/
│
├── documentation/
│   ├── PRD.md
│   ├── TRD.md
│   └── API_DOCUMENTATION.md
│
├── tests/
│
├── .gitignore
└── README.md
```

*This is the proposed repository structure. Update it as implementation progresses.*

## ⚙️ Getting Started

### Prerequisites

Install the following tools:

- Flutter SDK
- Dart SDK
- Python 3.10+
- Git
- MongoDB
- Visual Studio Code

### 1. Clone the Repository

```bash
git clone https://github.com/shruti060805-hash/ABHAYA.git

cd ABHAYA
```

### 2. Backend Setup

```bash
cd backend

python -m venv venv
```

Activate the virtual environment.

**Windows:**
```bash
venv\Scripts\activate
```

**Linux / macOS:**
```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure environment variables by copying `backend/.env.example` to `backend/.env`. Set `MONGODB_URI` to your MongoDB server (and credentials, if required) in that ignored local file; never commit real credentials. `MONGODB_DATABASE` selects the database. The API attempts a MongoDB ping on startup and remains available for liveness and metadata if MongoDB is unavailable, but database-backed features will not work until it is reachable. See [backend setup](./backend/README.md) for details.

Run the backend:

```bash
uvicorn app.main:app --reload
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

### 3. Flutter Setup

```bash
cd frontend

flutter pub get

flutter run
```

*Run these commands after the corresponding frontend and backend files have been implemented.*

## 🔐 Security & Privacy

ABHAYA is designed with user safety and privacy as core principles.

- Secure authentication and password hashing.
- Protected API endpoints.
- Environment-based secret management.
- Consent-based location sharing.
- Restricted access to sensitive user information.
- Secure handling of emergency contact information.
- Responsible handling of camera and microphone permissions.

**Privacy principle:** User data should only be collected and shared when necessary for the application's functionality and with appropriate user consent.

## 🚀 Future Scope

ABHAYA aims to evolve into a comprehensive AI-powered personal safety platform.

Potential future developments include:

- Smartwatch integration.
- Intelligent emergency risk assessment.
- Advanced voice distress recognition.
- Improved offline emergency communication.
- Integration with verified emergency response services.
- Geographical safety insights.
- AI-assisted contextual threat analysis.

## ⚠️ Development Disclaimer

ABHAYA is an ongoing development project.

AI predictions may be inaccurate, GPS availability may vary and network connectivity may affect emergency notifications. AI-based detection must not be treated as proof of danger or as a replacement for emergency services.

The application should undergo extensive real-world testing, privacy reviews and security assessments before deployment.

## 👩‍💻 Project Vision

ABHAYA is built around a simple belief:

> Safety should not depend entirely on whether someone can reach their phone and press a button.

We aim to explore how artificial intelligence and modern software engineering can contribute to a safer and more responsive world.

---

## 🤝 Contributing

Contributions, ideas and technical discussions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Implement your changes.
4. Submit a pull request.

## 📜 License

This project is intended to be distributed under the MIT License. Add a `LICENSE` file before claiming the repository is officially licensed.

---

<div align="center">

### 🛡️ ABHAYA

**Technology with Purpose. Innovation with Responsibility.**

*Building a safer tomorrow, one innovation at a time.*

</div>