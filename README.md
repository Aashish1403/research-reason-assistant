# 🤖 Research & Reason Assistant

A sophisticated web application powered by CrewAI multi-agent system that provides intelligent research assistance with comprehensive reasoning and source citations.

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)
![React](https://img.shields.io/badge/React-18+-blue.svg)
![CrewAI](https://img.shields.io/badge/CrewAI-Multi--Agent-orange.svg)

## 🌟 Features

- **🤖 Multi-Agent Intelligence**: CrewAI-powered research system with specialized agents
- **🔍 Web Research**: Real-time web search and content fetching using MCP tools
- **📊 Complete Tracing**: Transparent workflow with detailed agent action logs
- **💡 Intelligent Reasoning**: Step-by-step explanations for all conclusions
- **📚 Proper Citations**: Accurate source references for all information
- **⚡ Modern Stack**: FastAPI backend with React frontend

## 🏗️ Architecture

┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│ React Frontend │◄──►│ FastAPI Backend │◄──►│ CrewAI Agents │
└─────────────────┘ └─────────────────┘ └─────────────────┘
│
┌────────▼────────┐
│ MCP Tools │
│ - Web Search │
│ - Web Fetch │
└─────────────────┘


## 🔧 Tech Stack

### Backend
- **FastAPI** - Modern, fast Python web framework
- **CrewAI** - Multi-agent orchestration framework
- **MCP Tools** - Web search and content fetching
- **Pydantic** - Data validation and serialization
- **AsyncIO** - Asynchronous programming

### Frontend
- **React 18** - Modern UI framework
- **Vite** - Fast build tool and dev server
- **Axios** - HTTP client for API communication
- **CSS3** - Custom styling for responsive design

### AI & Tools
- **Multi-Agent System** - Research, Analysis, Synthesis agents
- **Web Search API** - Real-time information gathering
- **Content Processing** - Intelligent text extraction and parsing

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Node.js 18+
- npm or yarn

### Installation

1. **Clone the repository**
git clone https://github.com/yourusername/research-reason-assistant.git
cd research-reason-assistant

2. **Backend Setup**
cd backend
python -m venv venv

Windows
venv\Scripts\activate

Mac/Linux
source venv/bin/activate

pip install -r requirements.txt


3. **Frontend Setup**
cd ../frontend
npm install

4. **Environment Configuration**
Create backend/.env file
cp backend/.env.example backend/.env


GEMINI_API_KEY=your_key_here

### Running the Application

1. **Start Backend** (Terminal 1)
cd backend
python main.py

2. **Start Frontend** (Terminal 2)
cd frontend
npm run dev

3. **Access Application**
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

## 💡 Usage Examples

### Basic Query
Question: "What is machine learning?"
Response: Comprehensive explanation with reasoning and citations

### Technical Query
Question: "How does Python's GIL work?"
Response: Detailed technical explanation with source references

### Current Events
Question: "Latest developments in AI research"
Response: Up-to-date information with credible sources


## 🤖 Multi-Agent Workflow

1. **Research Agent** 🔍
   - Searches web for relevant information
   - Fetches detailed content from sources
   - Validates source credibility

2. **Analyzer Agent** 🧠
   - Processes and validates information
   - Identifies key facts and insights
   - Checks for consistency across sources

3. **Synthesizer Agent** ✍️
   - Creates comprehensive answers
   - Provides step-by-step reasoning
   - Formats proper citations

## 📊 API Endpoints

- `GET /` - Health check
- `POST /api/ask` - Submit research question
- `GET /health` - System status

## 🛠️ Development

### Project Structure
research-reason-assistant/
├── backend/
│ ├── app/
│ │ ├── agents/ # CrewAI agents
│ │ ├── tools/ # MCP tools
│ │ └── services/ # Business logic
│ ├── main.py # FastAPI application
│ └── requirements.txt # Python dependencies
├── frontend/
│ ├── src/
│ │ ├── components/ # React components
│ │ └── hooks/ # Custom hooks
│ ├── package.json # Node dependencies
│ └── vite.config.js # Vite configuration
└── README.md


### Adding New Agents
1. Create agent in `backend/app/agents/`
2. Define role, goal, and backstory
3. Integrate with existing workflow

### Adding New Tools
1. Implement in `backend/app/tools/`
2. Follow MCP tool interface
3. Add to agent toolkits

## 📈 Features Roadmap

- [ ] Multi-language support
- [ ] Advanced filtering and search options
- [ ] Export functionality (PDF, JSON)
- [ ] User authentication and saved queries
- [ ] Integration with more data sources
- [ ] Real-time collaboration features

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **CrewAI** - Multi-agent orchestration framework
- **FastAPI** - Modern Python web framework
- **React** - Frontend UI framework
- **OpenAI/Groq/Gemini** - LLM providers

## 📞 Contact

- **Author**: [Aashish M Kumar]
- **Email**: aashishmk14@gmail.com
- **GitHub**: [@Aashish1403](https://github.com/Aashish1403)

---

⭐ **Star this repository if you find it helpful!**

