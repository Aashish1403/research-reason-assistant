import { useState } from 'react'
import axios from 'axios'
import './index.css'

function App() {
  const [question, setQuestion] = useState('')
  const [response, setResponse] = useState(null)
  const [loading, setLoading] = useState(false)

  const handleSubmit = async (e) => {
    e.preventDefault()
    if (!question.trim()) return

    setLoading(true)
    try {
      const result = await axios.post('http://127.0.0.1:8000/api/ask', { question })
      setResponse(result.data)
    } catch (error) {
      console.error('Error:', error)
      setResponse({ 
        error: `Failed to get response: ${error.message}` 
      })
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="container">
      <div className="max-width">
        <h1 className="title">
          Research & Reason Assistant
        </h1>
        
        <form onSubmit={handleSubmit} className="form-container">
          <div className="input-group">
            <input
              type="text"
              value={question}
              onChange={(e) => setQuestion(e.target.value)}
              placeholder="Ask a factual question..."
              className="input-field"
              disabled={loading}
            />
            <button
              type="submit"
              disabled={loading || !question.trim()}
              className="submit-btn"
            >
              {loading ? 'Thinking...' : 'Ask'}
            </button>
          </div>
        </form>

        {response && (
          <div className="response-card">
            {response.error ? (
              <div className="error-text">Error: {response.error}</div>
            ) : (
              <>
                <div className="response-section">
                  <h3 className="response-title">Answer</h3>
                  <p className="response-text">{response.answer}</p>
                </div>
                
                <div className="response-section">
                  <h3 className="response-title">Reasoning</h3>
                  <p className="response-reasoning">{response.reasoning}</p>
                </div>

                {response.citations && response.citations.length > 0 && (
                  <div className="response-section">
                    <h3 className="response-title">Citations</h3>
                    <ul>
                      {response.citations.map((citation, index) => (
                        <li key={index}>
                          <a href={citation.url} target="_blank" rel="noopener noreferrer">
                            {citation.title}
                          </a>
                        </li>
                      ))}
                    </ul>
                  </div>
                )}

                {response.trace && response.trace.length > 0 && (
                  <div className="response-section">
                    <h3 className="response-title">Trace</h3>
                    <pre style={{ fontSize: '0.8rem', overflow: 'auto' }}>
                      {JSON.stringify(response.trace, null, 2)}
                    </pre>
                  </div>
                )}
              </>
            )}
          </div>
        )}
      </div>
    </div>
  )
}

export default App
